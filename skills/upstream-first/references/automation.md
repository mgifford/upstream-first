# Upstream-First Automation

Automate evidence that can be checked reliably. Do not claim a generic linter
can determine architectural ownership or project intent.

## Portable checks

Run `scripts/check_upstream_debt.py` to check:

- record structure;
- unique identifiers;
- upstream reference or explicit exception;
- introduction and review dates;
- overdue active records;
- existing source locations;
- optional public source annotations;
- restricted visibility for embargoed records.

Run the repository validator and tests before review:

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
python3 scripts/check_upstream_debt.py examples/upstream-debt.example.json \
  --root . --today 2026-07-30
```

Use the real current date for an operational registry. The fixed date above
keeps the example deterministic.

## Repository-specific checks

Extend the project's existing tools rather than introducing a parallel lint
stack. Examples include:

- ESLint rules for direct use of internal JavaScript APIs;
- PHP_CodeSniffer rules for Drupal service bypasses;
- Semgrep rules for duplicated security or authorization primitives;
- design-system checks for hardcoded colors, spacing, or tokens;
- database analysis for unindexed queries;
- bundle budgets and dependency-policy checks.

Each rule must identify a specific prohibited pattern, document valid
exceptions, and have positive and negative fixtures. A heuristic warning should
not fail CI until maintainers have reviewed its false-positive rate.

## Required CI behavior

- Fail on invalid, duplicate, expired, or unowned public debt records.
- Fail when required source locations or public annotations are missing.
- Warn, rather than print details, when a restricted record requires review.
- Never read or echo confidential vulnerability evidence in public CI.
- Require human review before renewing, removing, or publishing a record.
