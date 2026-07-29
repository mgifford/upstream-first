# Classification

## Nature

- **Bug:** behaviour violates documented, tested, specified, or accepted
  behaviour.
- **Feature:** adds capability or intentionally changes accepted behaviour.
- **Design question:** expected behaviour or architecture is unclear.
- **Security issue:** confidentiality, integrity, availability, authentication,
  or authorization may be affected. Use private reporting.
- **Accessibility defect:** disabled people are blocked or disadvantaged, or an
  applicable accessibility requirement is violated.
- **Maintenance:** structure, tests, tools, or documentation improve without an
  intended behaviour change.
- **Instance issue:** local content, configuration, policy, deployment, or
  unsupported use causes the behaviour.
- **Support question:** an existing capability may solve the need.

Evidence can include a minimal reproducer, failing test, specification,
documentation, prior decision, affected-user account, or compatibility record.

## Ownership

- **Instance:** local data, content, policy, branding, deployment, or workflow.
- **Integration:** supported components work alone but fail together.
- **Dependency:** a supported minimal installation reproduces the problem.
- **Ecosystem:** several projects need a shared convention or capability and no
  current project can own it.

## Disposition

Configure, report, contribute non-code evidence, patch upstream, extend,
create, apply a temporary workaround, implement locally, or stop.

The receiving project owns its final labels and product boundary.
