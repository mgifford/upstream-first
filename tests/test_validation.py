import copy
import datetime as dt
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_repo", ROOT / "scripts" / "validate_repo.py"
)
assert SPEC and SPEC.loader
VALIDATE_REPO = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATE_REPO)

sys.path.insert(0, str(ROOT / "scripts"))
DEBT_SPEC = importlib.util.spec_from_file_location(
    "check_upstream_debt", ROOT / "scripts" / "check_upstream_debt.py"
)
assert DEBT_SPEC and DEBT_SPEC.loader
CHECK_DEBT = importlib.util.module_from_spec(DEBT_SPEC)
DEBT_SPEC.loader.exec_module(CHECK_DEBT)


class RepositoryValidationTests(unittest.TestCase):
    def test_repository_is_valid(self):
        self.assertEqual([], VALIDATE_REPO.validate_repository(ROOT))

    def test_missing_required_property_is_rejected(self):
        schema = json.loads(
            (ROOT / "schemas" / "ai-review.schema.json").read_text(encoding="utf-8")
        )
        example = json.loads(
            (ROOT / "examples" / "ai-review.example.json").read_text(encoding="utf-8")
        )
        invalid = copy.deepcopy(example)
        del invalid["human_accountability"]
        errors = VALIDATE_REPO.validate_instance(invalid, schema)
        self.assertTrue(any("human_accountability" in error for error in errors))

    def test_unexpected_property_is_rejected(self):
        schema = {
            "type": "object",
            "additionalProperties": False,
            "properties": {"known": {"type": "boolean"}},
        }
        errors = VALIDATE_REPO.validate_instance(
            {"known": True, "invented": "value"}, schema
        )
        self.assertTrue(any("unexpected property" in error for error in errors))

    def test_boolean_is_not_an_integer(self):
        errors = VALIDATE_REPO.validate_instance(True, {"type": "integer"})
        self.assertTrue(errors)

    def test_decision_record_requires_engagement_path(self):
        schema = json.loads(
            (ROOT / "schemas" / "decision-record.schema.json").read_text(
                encoding="utf-8"
            )
        )
        example = json.loads(
            (ROOT / "examples" / "decision-record.example.json").read_text(
                encoding="utf-8"
            )
        )
        del example["engagement_path"]
        errors = VALIDATE_REPO.validate_instance(example, schema)
        self.assertTrue(any("engagement_path" in error for error in errors))


class UpstreamDebtTests(unittest.TestCase):
    def load_example(self):
        return json.loads(
            (ROOT / "examples" / "upstream-debt.example.json").read_text(
                encoding="utf-8"
            )
        )

    def validate(self, registry, root=ROOT, require_tags=False):
        with tempfile.TemporaryDirectory() as temp_dir:
            registry_path = Path(temp_dir) / "registry.json"
            registry_path.write_text(json.dumps(registry), encoding="utf-8")
            return CHECK_DEBT.validate_registry(
                registry_path,
                root,
                dt.date(2026, 7, 30),
                require_tags,
            )

    def test_example_registry_is_valid_on_fixed_date(self):
        errors, warnings = self.validate(self.load_example())
        self.assertEqual([], errors)
        self.assertEqual([], warnings)

    def test_reference_or_exception_is_required(self):
        registry = self.load_example()
        registry["records"][0]["upstream_reference"] = None
        registry["records"][0]["exception_reason"] = None
        errors, _ = self.validate(registry)
        self.assertTrue(any("reference or exception" in error for error in errors))

    def test_overdue_active_record_is_rejected(self):
        registry = self.load_example()
        registry["records"][0]["review_by"] = "2026-07-01"
        errors, _ = self.validate(registry)
        self.assertTrue(any("overdue" in error for error in errors))

    def test_embargoed_record_must_be_restricted(self):
        registry = self.load_example()
        registry["records"][0]["classification"] = "security-mitigation"
        registry["records"][0]["status"] = "under-embargo"
        registry["records"][0]["visibility"] = "public"
        errors, _ = self.validate(registry)
        self.assertTrue(any("must be restricted" in error for error in errors))

    def test_public_source_marker_can_be_required(self):
        registry = self.load_example()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "mitigation.txt"
            source.write_text("UPSTREAM-DEBT: UF-0042\n", encoding="utf-8")
            registry["records"][0]["locations"] = ["mitigation.txt"]
            errors, _ = self.validate(registry, root, require_tags=True)
        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
