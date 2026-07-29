#!/usr/bin/env python3
"""Validate an upstream-debt registry and its local lifecycle controls."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

from validate_repo import validate_instance


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "schemas" / "upstream-debt.schema.json"
TERMINAL_STATUSES = {"resolved"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_registry(
    registry_path: Path,
    root: Path,
    today: dt.date,
    require_tags: bool = False,
) -> tuple[list[str], list[str]]:
    """Return errors and warnings for one upstream-debt registry."""
    errors: list[str] = []
    warnings: list[str] = []

    try:
        registry = load_json(registry_path)
        schema = load_json(SCHEMA_PATH)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{registry_path}: cannot read JSON: {exc}"], warnings

    errors.extend(
        f"{registry_path}: {error}"
        for error in validate_instance(registry, schema)
    )
    if errors:
        return errors, warnings

    seen: set[str] = set()
    for record in registry["records"]:
        record_id = record["id"]
        prefix = f"{registry_path}: {record_id}"

        if record_id in seen:
            errors.append(f"{prefix}: duplicate identifier")
        seen.add(record_id)

        if not record["upstream_reference"] and not record["exception_reason"]:
            errors.append(
                f"{prefix}: require an upstream reference or exception reason"
            )

        introduced = dt.date.fromisoformat(record["introduced_on"])
        review_by = dt.date.fromisoformat(record["review_by"])
        if review_by < introduced:
            errors.append(f"{prefix}: review date precedes introduction")

        if record["status"] not in TERMINAL_STATUSES and review_by < today:
            errors.append(f"{prefix}: review date is overdue")

        if (
            record["status"] == "under-embargo"
            and record["visibility"] != "restricted"
        ):
            errors.append(
                f"{prefix}: embargoed security records must be restricted"
            )

        for location in record["locations"]:
            if "://" in location:
                continue
            target = root / location
            if not target.is_file():
                errors.append(f"{prefix}: location does not exist: {location}")
                continue
            if require_tags and record["visibility"] == "public":
                marker = f"UPSTREAM-DEBT: {record_id}"
                if marker not in target.read_text(encoding="utf-8"):
                    errors.append(
                        f"{prefix}: location lacks source marker: {location}"
                    )

        if record["visibility"] == "restricted":
            warnings.append(
                f"{prefix}: verify this registry is access-controlled"
            )

    return errors, warnings


def parse_date(value: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"{value!r} is not an ISO 8601 date"
        ) from exc


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("registry", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--today", type=parse_date, default=dt.date.today())
    parser.add_argument("--require-tags", action="store_true")
    args = parser.parse_args()

    errors, warnings = validate_registry(
        args.registry,
        args.root,
        args.today,
        args.require_tags,
    )
    for warning in warnings:
        print(f"Warning: {warning}")
    if errors:
        for error in errors:
            print(f"Error: {error}")
        return 1
    print("Upstream-debt registry passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
