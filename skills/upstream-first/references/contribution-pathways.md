# Contribution Pathways

Choose the receiving project's required path before preparing external work.
Project policy overrides these defaults.

## Pathway table

| Path | Use when | Do not use when | Expected artifact |
| --- | --- | --- | --- |
| Direct pull request | The project accepts unsolicited pull requests; the change is narrow, reproducible, low-risk, and needs no prior design decision | Public API, architecture, dependency, security boundary, governance, or standards change | Focused pull request with appropriate regression evidence |
| Issue first | Ownership, expected behaviour, impact, priority, or implementation approach is uncertain | The project explicitly requests a different channel | Reproducible issue with facts, inferences, and questions separated |
| Design proposal first | The change affects public APIs, architecture, data models, dependencies, interoperability, governance, or standards | The project has a different formal proposal process | RFC, design issue, or discussion |
| Confidential report | A finding may affect confidentiality, integrity, availability, authentication, or authorization | Routine bugs with no credible security effect | Private report prepared with `responsible-security-disclosure` |
| Downstream ownership | The requirement is confirmed as instance-specific or the organization accepts durable local maintenance | A shared dependency clearly owns the defect and upstream is viable | Local decision record and maintenance plan |
| Break-glass workaround | Immediate harm cannot wait for upstream delivery | A normal release or supported configuration can meet the need | Structured upstream-debt record and temporary mitigation |

## Direct pull-request gate

Use a direct pull request only when all are true:

- the receiving project permits it;
- expected behaviour and ownership are clear;
- the change has one bounded purpose;
- no security vulnerability is suspected;
- no public API, architecture, data model, dependency, governance, or standards
  decision is introduced;
- compatibility and release effects are limited and understood;
- appropriate regression evidence is feasible;
- the contributor can explain, revise, and support the work.

Accessibility is not a shortcut around this gate. Changes to semantics, focus,
keyboard interaction, accessible names, localization, or component contracts
may require issue or design discussion first.

## Permission boundary

Reading policies, source, issues, and release documentation is discovery.
Preparing local text or a patch is local work. Opening an issue, submitting a
report, pushing a branch, or creating a pull request is an external write and
requires human approval.
