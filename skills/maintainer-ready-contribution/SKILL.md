---
name: maintainer-ready-contribution
description: Prepare a bounded open-source issue, design proposal, reproduction, test, documentation change, patch, or pull request that follows the receiving project's rules and minimizes avoidable maintainer work. Use after an upstream path is selected, when a dependency flaw is found, when turning local work into a reusable contribution, or when a user asks for an upstream issue draft, patch proposal, or contribution-ready handoff.
---

# Maintainer-Ready Contribution

Prepare work for the receiving community. Optimize for correctness, fit,
clarity, reviewability, and follow-through, not superficial polish or volume.

## Workflow

### 1. Confirm the upstream decision

Obtain or reconstruct:

- problem and affected users;
- issue, ownership, and disposition classifications;
- receiving project and component;
- why this project is the responsible home;
- local constraints and any temporary workaround.

Return to `upstream-first` if ownership is unresolved.

### 2. Read the project's rules

Inspect current contribution, governance, security, support, licensing,
release, accessibility, and AI policies.

Read [policy-discovery.md](references/policy-discovery.md) for a full checklist.
Record missing, conflicting, or ambiguous requirements.

If the project prohibits the relevant AI use, stop producing contribution
content within that scope. If the issue is a vulnerability, use the private
security process, hand off to `responsible-security-disclosure`, and do not
prepare a public issue.

### 3. Choose the smallest useful contribution

Select:

- question or discussion;
- reproducible issue;
- failing test;
- documentation or translation;
- design proposal;
- focused patch or pull request;
- funding, review, or maintenance offer.

Ask maintainers before substantial features, architectural work, new
dependencies, standards changes, or broad refactoring.

Do not assume code is the most useful contribution.
Follow the engagement path selected by `upstream-first`. Do not infer that a
small accessibility change is necessarily low-risk.

### 4. Establish evidence

Include:

- concise problem statement;
- affected people and tasks;
- minimal reproducible steps;
- supported versions and environment;
- actual and expected behaviour;
- specification, documentation, test, or prior-decision evidence;
- scope and non-goals;
- privacy-safe artifacts;
- uncertainty and alternative explanations.

For accessibility issues, identify user impact and combine automated and manual
evidence. For regressions, prefer a failing test when feasible. Require evidence
appropriate to the contribution type. When an automated regression test is not
feasible or supported, explain why and provide a minimal manual or visual test
case. Visual tests alone do not establish accessibility.

### 5. Prepare the change

Follow existing architecture, style, tests, and documentation. Use analogous
accepted contributions as evidence, not as authority over written policy.

Keep the diff focused. Remove unrelated formatting, speculative abstractions,
invented dependencies, generated verbosity, and duplicate documentation.

Run deterministic tests and checks available to the contributor. Never claim a
test was run when it was not.

For Git-based cross-repository work, read
[cross-repository-git.md](references/cross-repository-git.md). Discover remotes,
the target branch, and the release process before proposing commands. Never
hardcode `main`, `master`, or `develop`.

### 6. Prepare maintainer context

Explain:

- why the change belongs here;
- why this approach was chosen;
- alternatives rejected;
- compatibility and release impact;
- accessibility, security, privacy, licensing, and sustainability findings;
- tests run and results;
- follow-up work and who owns it;
- material AI assistance when required.

Use [readiness-checklist.md](references/readiness-checklist.md).

### 7. Produce the handoff

Choose the matching asset:

- [upstream-issue.md](assets/upstream-issue.md)
- [design-proposal.md](assets/design-proposal.md)
- [pull-request.md](assets/pull-request.md)

Distinguish facts, inferences, and open questions. Keep the final text concise
enough to review.

Do not publish or interact externally without human approval. Run
`ai-contribution-review` before submission when AI materially assisted the
work.

## Review response

When maintainers respond:

- answer the actual question directly;
- distinguish must-fix, important follow-up, and optional suggestions;
- revise the work rather than generate defensive volume;
- state promptly if unable to continue;
- close or hand off abandoned work responsibly;
- update the downstream workaround and migration record when upstream status
  changes.

## Completion check

Complete only when:

- receiving policy and contribution channel are known;
- substantial work has maintainer agreement or is explicitly marked as a
  proposal;
- evidence is reproducible and privacy-safe;
- scope, non-goals, tests, and risks are explicit;
- the contributor can explain and revise the work;
- follow-through has an owner;
- external action remains subject to human approval.
