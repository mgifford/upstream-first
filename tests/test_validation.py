import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_repo", ROOT / "scripts" / "validate_repo.py"
)
assert SPEC and SPEC.loader
VALIDATE_REPO = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATE_REPO)


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


if __name__ == "__main__":
    unittest.main()
