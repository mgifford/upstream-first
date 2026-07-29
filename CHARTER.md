# Project Charter

## 1. Mission

Help people and AI agents direct improvements to the open-source project best
positioned to own them, while respecting maintainer capacity, community rules,
security, privacy, accessibility, sustainability, and contributor development.

## 2. Lineage

Upstream First generalizes CivicActions' Contrib First practice:

> When work could benefit more than one project, assess existing and upstream
> options before accepting custom local code.

The original practice remains the policy source. This project adds
cross-ecosystem discovery, project-policy handling, contribution readiness,
AI-assistance review, structured outputs, and evaluations.

## 3. Scope

The project covers:

- Drupal core, contributed modules, themes, recipes, distributions, and custom
  code;
- JavaScript, Python, PHP, and other package ecosystems;
- documentation, tests, translations, design, standards, issue triage, and
  other non-code contributions;
- upstream issues, design proposals, patches, and pull requests;
- temporary downstream workarounds with an explicit upstream and retirement
  path;
- known or disclosed AI-assisted contributions.

The project does not:

- decide what a receiving project must accept;
- override a project's contribution, security, licensing, or AI policy;
- infer AI use from writing style or code patterns;
- guarantee that community maintenance will be available;
- require publication of client-confidential or security-sensitive material;
- treat creating a new open-source package as automatically sustainable;
- authorize an agent to publish, comment, assign, label, or open a pull request
  without human approval.

## 4. Principles

### 4.1 Right home before implementation

Choose the narrowest project that can responsibly own, review, release, and
maintain the change. Upstream is the default direction, not an absolute rule.

### 4.2 Local need is not proof of local ownership

A defect may be found in one implementation while belonging to a dependency.
Conversely, a broadly worded idea may still encode one organization's policy or
content model and belong locally.

### 4.3 Maintainer attention is a constrained resource

Prefer small, reproducible, well-scoped contributions. Do not transfer
unbounded diagnosis, verification, or cleanup work to maintainers.

### 4.4 Humans remain accountable

AI can support research, learning, drafting, implementation, and review only
within the receiving project's policy. A human contributor must understand the
work, approve it, answer questions, and remain available for revision.

### 4.5 Contribution includes more than code

Bug reports, reproductions, tests, documentation, translations, design,
accessibility testing, user research, review, funding, and maintenance are
valid contributions.

### 4.6 Standards before invention

Use applicable open standards and current stable releases where practical.
Record the exact version when making a conformance claim. Treat drafts and
community practices according to their actual status.

### 4.7 Evidence before assertion

Separate observations from interpretation. Cite specifications, project
policies, reproductions, tests, and prior decisions. Mark uncertainty.

### 4.8 Temporary divergence must expire

A downstream workaround must identify its upstream record, owner, review date,
removal condition, and migration path.

### 4.9 Quality gates are not cosmetic

Accessibility, security, privacy, licensing, provenance, and sustainability
findings can disqualify an otherwise convenient solution.

### 4.10 Communities are relationships

The goal is not higher pull-request volume. The goal is useful, accepted work
and contributors who can participate, learn, and take responsibility.

## 5. Decision hierarchy

Evaluate options in this order:

1. Use a suitable installed capability.
2. Use an existing public API or extension point.
3. Adopt a suitable maintained open-source package.
4. Contribute a focused improvement to an existing project.
5. Create a reusable open-source package when ownership and maintenance are
   credible.
6. Implement locally with a written justification and reassessment date.

A higher-ranked option is selected only when it satisfies the project's
functional and quality requirements. Popularity alone is insufficient.

## 6. Policy precedence

Apply requirements in this order:

1. Applicable law, regulation, contract, and confidential handling duties.
2. Receiving repository policy.
3. Receiving organization or foundation policy.
4. Published contribution, security, governance, licensing, and AI guidance.
5. This project's conservative defaults.

When policies conflict or remain ambiguous, stop before external action and ask
the responsible maintainer or the user.

## 7. Deliverables

The initial project delivers:

- three independently installable skills;
- reusable issue, patch, and review templates;
- machine-readable decision and review schemas;
- representative evaluation cases;
- a standards registry and evidence hierarchy;
- repository policies that model the expected contribution behaviour.

Accessibility and Drupal-specific adapters are deferred until the general
skills pass their evaluation cases.

## 8. Measures of success

Prefer:

- accepted upstream contributions;
- reduced long-lived downstream patches;
- time from report to actionable maintainer response;
- bounded review rounds;
- contributor follow-through;
- contributions beyond code;
- repeat contributors and progression toward maintenance;
- documented retirement of temporary workarounds;
- maintainer-reported reduction in avoidable review burden.

Do not use raw issue or pull-request volume as a success measure.

## 9. Release policy

Use Semantic Versioning after a public interface is declared. During `0.x`,
document breaking changes. A `1.0.0` release means the three output contracts,
policy precedence, and evaluation format are stable.

Review the standards registry at least every 90 days and before each minor or
major release.
