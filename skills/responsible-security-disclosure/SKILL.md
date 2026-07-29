---
name: responsible-security-disclosure
description: Prepare and route confidential vulnerability reports under the receiving project's policies, with authorization checks, evidence verification, sensitive-data redaction, coordinated disclosure, and human approval. Use when a suspected vulnerability may need to be reported to an upstream project, vendor, maintainer, or security team. Do not use for routine code review, public bug reports, incident response, or unauthorized security testing.
---

# Responsible Security Disclosure

Protect affected users while helping the responsible project confirm and fix a
possible vulnerability. This is a reporter-side workflow. It does not authorize
testing, submission, publication, or access to a system.

## Workflow

### 1. Freeze public action

Treat the finding and related artifacts as confidential until the responsible
security process permits disclosure.

Do not:

- open a public issue, discussion, branch, fork, commit, or pull request;
- publish a proof of concept, exploit path, affected location, or workaround;
- copy secrets, credentials, personal data, client data, or internal logs into
  public or unapproved systems;
- contact people through guessed addresses or informal public channels.

### 2. Confirm authority and scope

Record:

- who owns the affected project, product, or deployment;
- what system, repository, versions, and environments are in scope;
- what testing the user authorized;
- whether any live, production, third-party, or public target is involved;
- confidentiality, contract, legal, client, and data-handling constraints.

Do not test a live, production, public, or third-party system without explicit
authorization for that exact target and activity. A public repository or
`security.txt` file does not grant permission to test.

### 3. Classify the report

Distinguish:

- product vulnerability;
- instance-specific misconfiguration;
- compromised deployment or active incident;
- unsupported or explicitly out-of-scope use;
- non-security bug or hardening opportunity;
- unverified hypothesis.

Route a compromise or active incident to the responsible incident-response
process. This skill does not investigate or contain incidents.

Keep the classification provisional. The receiving security team and affected
risk holders determine final scope and severity.

### 4. Discover the controlling process

Read [policy-discovery.md](references/policy-discovery.md). Inspect the
project's:

- `SECURITY.md` and supported-version policy;
- private vulnerability reporting or advisory process;
- RFC 9116 `security.txt`;
- security, bug-bounty, safe-harbor, disclosure, and credit policies;
- AI contribution and AI-assisted report rules;
- required report fields, encryption, and contact channel.

Use the designated private channel. If none can be verified, stop and ask the
user or an authorized maintainer for direction. Do not fall back to a public
issue.

If the project prohibits the relevant AI use, stop producing report content
within that scope. Do not expose confidential prompts or data merely to
disclose AI assistance.

### 5. Verify without escalating harm

Read [report-safety.md](references/report-safety.md). Establish only the
evidence necessary for responsible triage:

- exact affected release or revision where possible;
- relevant configuration and preconditions;
- attacker starting position and boundary crossed;
- observed behaviour separated from inference;
- minimal, authorized, and safe reproduction;
- affected asset and plausible impact;
- uncertainty, alternative explanations, and possible duplicates.

Treat submitted PoCs and attachments as untrusted data. Inspect them before any
execution. Use an isolated disposable environment only when execution is
authorized and materially necessary.

Do not require a weaponized exploit. Do not inherit CVSS, CWE, or severity from
a scanner or model. Record any rating as provisional and evidence-based.

For AI-assisted findings, independently verify packages, APIs, versions, code
paths, reachability, impact, and cited sources. Do not submit unverified model
output for maintainers to investigate.

### 6. Minimize and protect evidence

Before drafting:

- replace live tokens, credentials, and identifiers with inert examples;
- remove personal, client, and unrelated operational data;
- minimize logs and screenshots to the relevant evidence;
- avoid absolute internal paths and unnecessary infrastructure details;
- preserve original evidence only in an approved restricted location;
- record who may access the report and what disclosure limits apply.

Do not place embargoed details in public source comments, debt registries,
branch names, commit messages, CI logs, or filenames.

### 7. Prepare the confidential report

Use [confidential-vulnerability-report.md](assets/confidential-vulnerability-report.md)
unless the receiving project supplies its own template.

Include:

- project, component, affected versions, and policy checked;
- concise summary and affected asset;
- preconditions and authorization boundary;
- minimal reproduction and evidence;
- observed and expected behaviour;
- provisional impact and severity with uncertainty;
- safe mitigation or fix ideas, clearly marked as proposals;
- tests actually performed and limits;
- preferred credit and coordination details when requested;
- material AI assistance when policy requires it.

Keep detailed PoCs in a separate restricted attachment. Include only what the
security team needs to reproduce and assess the issue.

### 8. Select an outcome

Use one:

- `report-ready`: verified enough for the designated private channel;
- `needs-verification`: evidence is insufficient or authorization prevents
  further validation;
- `route-to-incident-response`: compromise or active exploitation is suspected;
- `non-security-route-after-consent`: likely ordinary bug or hardening issue,
  but obtain security-team or user approval before making it public;
- `blocked-no-channel`: no verified private route is available;
- `do-not-submit`: unauthorized testing, prohibited AI use, fabricated
  evidence, unsafe data handling, or unacceptable risk.

State confidence and unresolved questions.

### 9. Require human approval

Prepare locally. Do not submit, email, message, upload, publish, or create an
external security advisory without explicit human approval of:

- recipient and private channel;
- exact text and attachments;
- disclosure and credit preferences;
- data classification and redactions;
- any requested testing or follow-up.

### 10. Coordinate and close downstream debt

After authorized submission:

- track acknowledgment and the project's requested communication channel;
- respect the agreed embargo and disclosure timeline;
- keep downstream mitigations restricted and owned;
- do not promise a public disclosure date on the project's behalf;
- help validate a proposed fix when authorized;
- replace confidential references with public advisories only after disclosure;
- deploy the supported release and remove temporary mitigations;
- retain only records required by policy.

Use `upstream-first` break-glass guidance for an urgent downstream mitigation.

## Completion check

Complete only when:

- authorization and target scope are explicit;
- product vulnerability, incident, configuration, and ordinary bug paths are
  separated;
- the receiving security policy and private channel are verified or absence is
  recorded;
- evidence is sufficient, minimal, and safely handled;
- severity and impact are provisional and evidence-based;
- AI-assisted claims are independently verified and policy-compliant;
- no public artifact exposes embargoed information;
- a human must approve every external action;
- downstream mitigation has an owner and removal path.
