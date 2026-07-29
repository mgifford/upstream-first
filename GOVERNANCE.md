# Governance

## Roles

- **Contributors** report, research, document, test, review, design, fund, or
  implement improvements.
- **Maintainers** review changes, manage releases, interpret project scope, and
  enforce project policies.
- **Lead maintainers** appoint maintainers, resolve governance disputes, and
  authorize stable releases.

`@mgifford` is proposed as the initial lead maintainer. Stable governance
should include at least one additional maintainer who can independently review
policy and release changes.

## Decisions

Prefer documented consensus. For substantial changes:

1. Open a design issue before implementation.
2. State the problem, affected users, alternatives, standards, risks, and
   compatibility impact.
3. Allow a reasonable review period based on urgency and community activity.
4. Record the decision and dissenting concerns.

Lead maintainers may make a decision when consensus cannot be reached. They
must state the rationale and identify how the decision can be revisited.

## Maintainer appointment

Consider contributors who demonstrate:

- repeated useful contributions;
- respectful participation;
- sound policy and technical judgment;
- willingness to do review, documentation, triage, and release work;
- reliable follow-through;
- understanding of accessibility, security, privacy, and sustainability
  responsibilities relevant to this project.

Maintainer status is a responsibility, not a reward for commit volume.

## Releases

- Use Semantic Versioning 2.0.0.
- Require one maintainer approval for `0.x` releases.
- Require two maintainer approvals for `1.x` and later major releases.
- Identify policy, output-schema, and trigger changes in release notes.
- Do not alter a published release.

## Policy changes

Changes to the charter, AI policy, governance, schemas, or normative skill
requirements require a design issue and explicit maintainer approval.

## Project health

Review maintainer capacity, unresolved security reports, standards currency,
open governance decisions, and temporary downstream exceptions before each
minor or major release.

If the project can no longer be maintained, document that status, stop claiming
active support, and seek adoption or archival rather than leaving users to
infer its state.
