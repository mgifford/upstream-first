# Quality Gates

## Accessibility

- Identify affected disabled people and tasks.
- Prefer semantic platform behaviour before ARIA or custom interaction.
- Require keyboard support, visible focus, contrast, and reflow where relevant.
- Combine automated evidence with appropriate manual testing.
- Propose an upstream accessibility fix when the defect belongs upstream.

## Security and privacy

- Sanitize and validate untrusted input.
- Preserve authorization boundaries.
- Keep secrets and vulnerability details private.
- Minimize personal data collection, retention, and model disclosure.
- Reject hardcoded secrets, weak authentication, unsafe command construction,
  or unnecessary tracking.
- If a finding may be a vulnerability, stop public contribution work and use
  `responsible-security-disclosure`.
- Keep embargoed details out of public issues, branches, forks, commits,
  source annotations, logs, and AI disclosures.

## License and provenance

- Identify project and dependency licenses with SPDX expressions where useful.
- Verify copied or generated material can be contributed.
- Meet CLA, DCO, sign-off, and attribution requirements.
- Verify citations, dependencies, and API claims.

## Sustainability

- Prefer deterministic checks to model calls.
- Avoid unnecessary polling, dependencies, packages, queries, bundles, and
  generated code.
- Account for maintainer review and long-term ownership.
- Give temporary divergence an expiry path.
- Do not make environmental claims without dated evidence and method.

## Standards

- Prefer the latest applicable stable open standard.
- Record exact versions for conformance claims.
- Preserve compatibility when a receiving project or legal rule requires an
  older version.
- Label drafts and community guidance accurately.
