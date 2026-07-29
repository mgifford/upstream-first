# Break-Glass Workarounds

Use a break-glass workaround only when immediate harm cannot wait for the
normal upstream and release process.

## Required record

Record:

- stable identifier;
- affected source locations or a restricted reference;
- downstream owner;
- reason the workaround is necessary;
- upstream issue, pull request, advisory, or documented exception;
- introduced date;
- risk-based review date;
- supported versions;
- removal condition;
- migration and rollback instructions;
- status and human approval.

Use `schemas/upstream-debt.schema.json` and validate the record with
`scripts/check_upstream_debt.py`.

## Source annotation

For public, non-security work, use a stable identifier rather than repeating a
URL:

```text
UPSTREAM-DEBT: UF-0042
```

Keep the URL and lifecycle metadata in the structured registry. This avoids
stale links and supports different programming languages.

## Review dates

Use a review date based on risk, upstream release cadence, and supported
versions. Thirty days is a reasonable default only when no better project rule
exists. A review date is not permission to remove code automatically.

CI may flag overdue records. A human must decide whether to remove, renew, or
escalate the workaround.

## Security exception

Do not commit embargoed vulnerability details or a revealing source annotation
to a public repository. Store the full record in an access-controlled system
and use an opaque internal reference where necessary. After coordinated
disclosure, add public advisory references when appropriate and remove the
mitigation after deploying the supported upstream fix.
