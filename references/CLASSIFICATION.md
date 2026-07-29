# Issue and Ownership Classification

Classification has three independent dimensions: nature, ownership scope, and
disposition. Do not collapse them into one label.

## Nature

| Classification | Test | Evidence |
| --- | --- | --- |
| Bug | Observed behaviour violates documented, tested, specified, or previously accepted behaviour | Reproducer, regression test, specification, documentation, or prior decision |
| Feature | Adds capability or intentionally changes accepted behaviour | Use case, affected users, alternatives, design agreement |
| Design question | Intended behaviour or architecture is unclear | Conflicting evidence or missing decision |
| Security issue | Could affect confidentiality, integrity, availability, authentication, or authorization | Private reproducer and impact analysis |
| Accessibility defect | Blocks or disadvantages disabled people or violates an applicable accessibility requirement | Affected task, people, requirement, manual and automated evidence |
| Maintenance | Improves structure, tests, tooling, or documentation without intentionally changing behaviour | Maintenance cost or risk evidence |
| Instance issue | Depends on local content, configuration, policy, deployment, or unsupported use | Clean environment does not reproduce |
| Support question | Existing capability may solve the problem but use is unclear | Documentation and configuration evidence |

The receiving project owns the final label.

## Ownership scope

### Instance

Choose instance scope when the behaviour depends on local data, content,
configuration, policy, branding, deployment, or a client-specific workflow.

### Integration

Choose integration scope when two projects work as documented independently but
their supported combination fails or lacks a defined bridge.

### Dependency

Choose dependency scope when the problem reproduces in a minimal supported
installation of one dependency and the fix belongs within its public contract.

### Ecosystem

Choose ecosystem scope when several projects need the same missing convention,
interoperability mechanism, or reusable capability and no existing project can
credibly own it.

## Clean-reproduction test

1. Record versions, environment, and configuration.
2. Remove client data and unrelated extensions.
3. Reproduce with supported versions and the smallest configuration.
4. Identify the earliest component where expected behaviour diverges.
5. Compare documentation, tests, and prior decisions.
6. Mark the result as confirmed, probable, ambiguous, or not reproduced.

Do not move private data into a public reproducer.

## Disposition

- Configure an existing capability.
- Report without implementing.
- Contribute a test, reproduction, documentation, or translation.
- Submit a focused upstream change.
- Create or extend an integration.
- Create a reusable package with named maintainers.
- Apply a temporary local workaround.
- Implement locally as the durable owner.
- Stop because the risk, policy, or maintenance case is unacceptable.

## Temporary workaround record

Record:

- stable upstream-debt identifier;
- affected source locations or a restricted reference;
- downstream owner;
- reason upstream delivery cannot meet the current need;
- upstream issue, pull request, advisory, or documented exception;
- introduced date;
- next review date;
- supported versions;
- removal condition;
- migration and rollback path.

Public, non-security work may carry an `UPSTREAM-DEBT: UF-####` source
annotation linked to a structured registry. Keep embargoed security details,
references, and records access-controlled.
