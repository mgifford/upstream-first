---
name: upstream-first
description: Decide the responsible home and implementation path for requested software, documentation, standards, accessibility, integration, or dependency changes. Use before building a custom module, script, package, integration, workaround, Drupal change, npm/PyPI/Packagist dependency change, or local fix, and when deciding whether work belongs in an installed capability, upstream project, extension, new reusable project, or local implementation.
---

# Upstream First

Determine ownership before implementation. Prefer the highest viable option in
the decision hierarchy, but do not force work upstream when policy, scope,
security, confidentiality, timing, or maintenance makes that irresponsible.

## Workflow

### 1. Capture intent and constraints

Record:

- requested outcome and affected people;
- platform, ecosystem, versions, and deployment;
- deadline and reason for urgency;
- contract, confidentiality, security, legal, and policy constraints;
- functional and non-functional requirements;
- available maintainer and contributor capacity.

Ask only for missing information that can change the decision. Mark assumptions.

### 2. Discover controlling policy

Inspect installed dependencies and the receiving project's current policies
before recommending implementation or external interaction.

Check contribution, governance, security, support, licensing, accessibility,
release, and AI rules. If project policy is complex or ambiguous, read
[project-policy.md](references/project-policy.md).

Apply receiving-project policy before this skill's defaults. Stop and ask when
authority or permission is unclear.

### 3. Classify the issue

Classify three dimensions separately:

1. **Nature:** bug, feature, design question, security issue, accessibility
   defect, maintenance, support, or instance issue.
2. **Ownership:** instance, integration, dependency, or ecosystem.
3. **Disposition:** configure, report, contribute, extend, create, work around,
   implement locally, or stop.

Use a minimal clean reproduction where practical. Do not publish confidential
data. Read [classification.md](references/classification.md) for edge cases.

Treat the classification as provisional until the responsible project confirms
it.

### 4. Evaluate options in order

Evaluate:

1. Use a suitable installed capability.
2. Use an existing public API or extension point.
3. Adopt a suitable maintained open-source package.
4. Contribute a focused improvement to an existing project.
5. Create a reusable open-source package with credible ownership.
6. Implement locally with a written justification.

For each option, record evidence, fit, gaps, maintenance, compatibility,
community health, migration cost, and quality-gate results.

Do not use popularity or an arbitrary percentage as proof of suitability.
Reject a higher-ranked option when its material gaps or risks make it
unacceptable.

### 5. Apply gates

Assess:

- accessibility and affected users;
- security boundaries, input handling, and vulnerability disclosure;
- privacy, personal data, confidentiality, and retention;
- license compatibility, copyright, and provenance;
- sustainability, dependency cost, compute, polling, bundle size, queries, and
  maintainer burden;
- open-standard compatibility and exact versions where claims depend on them.

Read [quality-gates.md](references/quality-gates.md) when any gate is material.

### 6. Choose and justify

Choose the highest viable option. If choosing local code, state why every
higher option is unsuitable.

For an urgent temporary workaround, require:

- an upstream issue or recorded reason it cannot be public;
- downstream owner;
- introduced and review dates;
- supported versions;
- removal condition;
- migration and rollback path.

### 7. Produce the decision record

Use [decision-record.md](assets/decision-record.md). Include:

- discovery summary;
- issue, ownership, and disposition classifications;
- options 1 through 6 with evidence;
- gate findings;
- recommendation and confidence;
- upstream or local follow-up;
- unresolved questions;
- human approval required before external action.

If an upstream contribution is viable, hand off to
`maintainer-ready-contribution`. If AI materially assisted the work, run
`ai-contribution-review` before submission.

## Guardrails

- Do not open, comment on, assign, label, or submit external work without human
  approval.
- Do not treat a new open-source package as free maintenance.
- Do not claim that filing an issue eliminates downstream responsibility.
- Do not bypass accessibility, security, privacy, or license requirements for
  schedule reasons.
- Do not expose suspected vulnerabilities publicly.
- Do not use AI where the receiving project prohibits the relevant use.

## Completion check

Complete only when:

- controlling policies were checked or their absence recorded;
- issue nature, ownership, and disposition are separate;
- every option in the hierarchy has a reasoned result;
- all quality gates are explicit;
- temporary divergence has an expiry path;
- external action remains subject to human approval.
