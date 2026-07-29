# Evaluations

Each JSON manifest describes representative prompts and observable behaviours.
The manifests are inputs for human or model evaluation. They are not claims
that keyword matching can establish skill quality.

Validate their structure with:

```bash
python3 scripts/validate_repo.py
```

For forward evaluation:

1. Run each prompt in a fresh context with only the named skill available.
2. Preserve the raw response.
3. Have a reviewer score required and forbidden behaviours.
4. Record disagreements and ambiguous expectations.
5. Revise the skill or evaluation, not the model response.
6. Rerun from a fresh context.

Do not show the expected outcome or behaviour lists to the agent under test.
