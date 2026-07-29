#!/usr/bin/env python3
"""Validate the Upstream First repository without third-party dependencies."""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SHA_ACTION_RE = re.compile(r"uses:\s+([^/\s]+/[^@\s]+)@([^\s#]+)")

REQUIRED_ROOT_FILES = (
    "README.md",
    "CHARTER.md",
    "WHY_UPSTREAM_FIRST.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "ACCESSIBILITY.md",
    "SUSTAINABILITY.md",
    "AI_CONTRIBUTION_POLICY.md",
    "LICENSE",
)


class ValidationError(ValueError):
    """A repository validation error."""


def json_type_matches(value: Any, type_name: str) -> bool:
    if type_name == "null":
        return value is None
    if type_name == "object":
        return isinstance(value, dict)
    if type_name == "array":
        return isinstance(value, list)
    if type_name == "string":
        return isinstance(value, str)
    if type_name == "boolean":
        return isinstance(value, bool)
    if type_name == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if type_name == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    raise ValidationError(f"Unsupported schema type: {type_name}")


def validate_instance(value: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    """Validate the JSON Schema features used by this repository."""
    errors: list[str] = []

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}")

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} is not in {schema['enum']!r}")

    expected = schema.get("type")
    if expected is not None:
        expected_types = [expected] if isinstance(expected, str) else expected
        if not any(json_type_matches(value, item) for item in expected_types):
            errors.append(f"{path}: expected type {expected_types}, got {type(value).__name__}")
            return errors

    if isinstance(value, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                errors.append(f"{path}: missing required property {key!r}")

        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in properties:
                    errors.append(f"{path}: unexpected property {key!r}")

        for key, child in value.items():
            child_schema = properties.get(key)
            if child_schema is not None:
                errors.extend(validate_instance(child, child_schema, f"{path}.{key}"))

    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append(f"{path}: expected at least {schema['minItems']} items")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append(f"{path}: expected at most {schema['maxItems']} items")
        if "items" in schema:
            for index, child in enumerate(value):
                errors.extend(validate_instance(child, schema["items"], f"{path}[{index}]"))

    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append(f"{path}: string is shorter than {schema['minLength']}")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path}: string does not match {schema['pattern']!r}")
        if schema.get("format") == "date":
            try:
                dt.date.fromisoformat(value)
            except ValueError:
                errors.append(f"{path}: {value!r} is not an ISO 8601 date")

    if isinstance(value, int) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: value is below {schema['minimum']}")
        if "maximum" in schema and value > schema["maximum"]:
            errors.append(f"{path}: value is above {schema['maximum']}")

    return errors


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValidationError(f"{path}: missing opening frontmatter delimiter")
    try:
        raw = text.split("---\n", 2)[1]
    except IndexError as exc:
        raise ValidationError(f"{path}: missing closing frontmatter delimiter") from exc

    result: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValidationError(f"{path}: malformed frontmatter line {line!r}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip("\"'")
    return result


def quoted_yaml_value(text: str, key: str) -> str | None:
    match = re.search(rf"^\s*{re.escape(key)}:\s+\"([^\"]*)\"\s*$", text, re.MULTILINE)
    return match.group(1) if match else None


def validate_skills() -> list[str]:
    errors: list[str] = []
    skills_root = ROOT / "skills"
    for skill_dir in sorted(item for item in skills_root.iterdir() if item.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue
        try:
            metadata = parse_frontmatter(skill_file)
        except ValidationError as exc:
            errors.append(str(exc))
            continue

        if set(metadata) != {"name", "description"}:
            errors.append(f"{skill_file}: frontmatter must contain only name and description")
        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if name != skill_dir.name:
            errors.append(f"{skill_file}: name must match parent directory")
        if not SKILL_NAME_RE.fullmatch(name):
            errors.append(f"{skill_file}: invalid skill name {name!r}")
        if not 1 <= len(description) <= 1024:
            errors.append(f"{skill_file}: description must be 1 to 1024 characters")
        if len(skill_file.read_text(encoding="utf-8").splitlines()) >= 500:
            errors.append(f"{skill_file}: must remain under 500 lines")

        agent_file = skill_dir / "agents" / "openai.yaml"
        if not agent_file.is_file():
            errors.append(f"{skill_dir}: missing agents/openai.yaml")
            continue
        agent_text = agent_file.read_text(encoding="utf-8")
        short = quoted_yaml_value(agent_text, "short_description")
        prompt = quoted_yaml_value(agent_text, "default_prompt")
        if short is None or not 25 <= len(short) <= 64:
            errors.append(f"{agent_file}: short_description must be 25 to 64 characters")
        if prompt is None or f"${name}" not in prompt:
            errors.append(f"{agent_file}: default_prompt must mention ${name}")
    return errors


def validate_json_artifacts() -> list[str]:
    errors: list[str] = []
    schema_paths = sorted((ROOT / "schemas").glob("*.schema.json"))
    schemas: dict[str, dict[str, Any]] = {}

    for path in schema_paths:
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path}: invalid JSON: {exc}")
            continue
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            errors.append(f"{path}: must declare JSON Schema Draft 2020-12")
        schemas[path.name] = schema

    mappings = {
        ROOT / "examples" / "decision-record.example.json": "decision-record.schema.json",
        ROOT / "examples" / "ai-review.example.json": "ai-review.schema.json",
        ROOT / "examples" / "upstream-debt.example.json": "upstream-debt.schema.json",
    }
    for path, schema_name in mappings.items():
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: cannot parse example: {exc}")
            continue
        for error in validate_instance(value, schemas[schema_name]):
            errors.append(f"{path}: {error}")

    eval_schema = schemas.get("evaluation-manifest.schema.json")
    if eval_schema:
        for path in sorted((ROOT / "evals").glob("*.json")):
            try:
                value = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"{path}: invalid JSON: {exc}")
                continue
            for error in validate_instance(value, eval_schema):
                errors.append(f"{path}: {error}")
    return errors


def validate_markdown_links() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK_RE.findall(text):
            target = target.strip().split(" ", 1)[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            local_target = target.split("#", 1)[0]
            if not (path.parent / local_target).resolve().exists():
                errors.append(f"{path}: broken relative link {target!r}")
    return errors


def validate_text() -> list[str]:
    errors: list[str] = []
    text_suffixes = {".md", ".json", ".yaml", ".yml", ".py"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or (path.suffix not in text_suffixes and path.name != "LICENSE"):
            continue
        text = path.read_text(encoding="utf-8")
        if "\u2014" in text:
            errors.append(f"{path}: contains an em dash")
        placeholder_marker = "[TO" + "DO"
        if placeholder_marker in text:
            errors.append(f"{path}: contains an unresolved placeholder marker")
    return errors


def validate_workflow_actions() -> list[str]:
    errors: list[str] = []
    for path in (ROOT / ".github" / "workflows").glob("*.yml"):
        text = path.read_text(encoding="utf-8")
        for action, ref in SHA_ACTION_RE.findall(text):
            if not re.fullmatch(r"[0-9a-f]{40}", ref):
                errors.append(f"{path}: {action} must be pinned to a 40-character SHA")
    return errors


def validate_repository(root: Path | None = None) -> list[str]:
    global ROOT
    old_root = ROOT
    if root is not None:
        ROOT = root
    try:
        errors: list[str] = []
        for relative in REQUIRED_ROOT_FILES:
            if not (ROOT / relative).is_file():
                errors.append(f"{ROOT / relative}: missing required file")
        errors.extend(validate_skills())
        errors.extend(validate_json_artifacts())
        errors.extend(validate_markdown_links())
        errors.extend(validate_text())
        errors.extend(validate_workflow_actions())
        return errors
    finally:
        ROOT = old_root


def main() -> int:
    errors = validate_repository()
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
