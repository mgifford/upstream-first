# Vulnerability Report Safety

## Authorization

Record the exact target, actions, time window, accounts, data, and environments
authorized for testing. Source review does not authorize interaction with a
deployed system.

## Safe verification order

Prefer:

1. source and release-history review;
2. static analysis of supplied artifacts;
3. existing deterministic tests;
4. minimal local reproduction with inert data;
5. an isolated disposable environment;
6. more invasive validation only when explicitly authorized and necessary.

Do not execute untrusted PoCs by default. Inspect for network access, credential
use, file writes, destructive actions, persistence, encoded payloads, and
unexpected dependencies.

## Evidence minimization

- Use inert tokens and synthetic accounts.
- Quote the smallest relevant code or log fragment.
- Remove unrelated headers, environment variables, and identifiers.
- Keep precise exploit details in restricted attachments.
- Do not upload confidential evidence to an AI tool or external service unless
  that use is authorized.

## Impact and severity

Describe:

- affected asset and users;
- attacker starting privileges;
- trust boundary crossed;
- confidentiality, integrity, or availability effect;
- blast radius and required configuration;
- compensating controls;
- confidence and unverified assumptions.

CVSS and CWE may support communication when the project uses them. They do not
replace contextual risk analysis, and a reporter's rating remains provisional.

## Publication safety

Before coordinated disclosure, avoid:

- public issue or pull-request text;
- public forks and descriptive branches;
- filenames or commits naming the vulnerability class;
- logs that expose the vulnerable path;
- public source annotations or debt links;
- screenshots containing project, client, or user secrets.
