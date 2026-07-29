# Why Upstream-First Matters in the Age of AI

## Summary

AI can generate code, tests, documentation, and proposed fixes faster than most
organizations can review or maintain them. This changes the economics of
software development, but it does not remove the work required to understand a
problem, decide who should own it, evaluate risk, coordinate with maintainers,
support releases, or maintain deployed software.

Without an upstream-first discipline, AI can accelerate duplicated local fixes,
unnecessary wrappers, abandoned forks, insecure patches, and low-quality
contributions. Used responsibly, AI can instead help people discover existing
capabilities, reproduce defects, prepare tests, improve documentation, and
contribute bounded changes to the projects that should own them.

Upstream-first means deciding where a change should be owned before treating
custom local code as the default. It does not mean that every change must be
submitted upstream.

## The principle

When software depends on an open-source project, consider solutions in this
order:

1. Use a suitable capability that is already installed.
2. Use an existing public API or extension point.
3. Adopt a suitable maintained open-source package.
4. Contribute a focused improvement to an existing project.
5. Create a reusable open-source project with credible ownership.
6. Implement and maintain the change locally with a written justification.

The receiving project's contribution, governance, security, accessibility,
licensing, and AI policies control any contribution. Upstream-first does not
give a contributor permission to ignore those rules or impose work on
maintainers.

This principle extends CivicActions'
[Contrib First](https://guidebook.civicactions.com/en/latest/common-practices-tools/contribution/contrib-first/)
practice beyond contributed modules and patches. It applies to software,
documentation, tests, accessibility fixes, integrations, open standards,
security work, and other reusable improvements.

## AI changes the economics of software

AI lowers the immediate cost of producing another implementation. It does not
lower all of the costs that follow.

Generated code still needs:

- problem definition and ownership;
- architecture and design review;
- security, privacy, accessibility, and licensing review;
- deterministic testing and human evaluation;
- compatibility and release management;
- documentation and support;
- maintenance across future versions;
- accountable people who can explain and revise it.

This creates a dangerous imbalance. Generating a local workaround may take
minutes, while understanding its consequences and maintaining it may take years.
The apparent speed of the first change can conceal costs transferred to future
developers, clients, maintainers, users, and the public.

AI also makes it easier for many people to independently produce the same fix.
That can create duplicate downstream patches and duplicate upstream reports.
The 2026 OpenSSF and CNCF guide,
[Securing Open Source in the Age of AI](https://openssf.org/wp-content/uploads/2026/05/Securing-Open-Source-in-the-Age-of-AI.pdf),
describes increased report volume, duplicate vulnerability reports, unreliable
severity assessments, and additional pressure on maintainers.

Upstream-first adds a deliberate pause before implementation:

- Does the capability already exist?
- Does the problem reproduce outside this deployment?
- Which project owns the relevant behavior?
- Has the project already discussed or solved it?
- Does the project want an issue, a proposal, a test, or a patch?
- Is public contribution safe and permitted?
- Who will remain responsible after submission?

The objective is not to slow useful work. It is to avoid producing more code
than the ecosystem can responsibly absorb.

## Fix once, benefit many

A downstream fix affects the deployment where it is applied. An accepted,
released, and adopted upstream fix can benefit every downstream user of the
corrected version.

The benefit is not instantaneous or guaranteed. Maintainers must accept the
change, the project must release it, and downstream users must upgrade.
Nevertheless, a properly placed upstream contribution can replace many
independent local fixes with one reviewed implementation and one shared
regression test.

The multiplier can include:

- fewer organizations rediscovering the same problem;
- fewer incompatible fixes for the same behavior;
- shared tests that prevent regressions;
- documentation available to the full community;
- broader review across different environments and use cases;
- a supported migration path through normal releases.

The Linux Foundation's guide on
[participating in open-source communities](https://www.linuxfoundation.org/resources/open-source-guides/participating-in-open-source-communities)
warns that downstream patches must be retested, updated, and reapplied during
upgrade cycles. It recommends designing with upstream contribution in mind and
remaining involved after submission.

## Accessibility as a public good

An accessibility defect in a shared component can create the same barrier
across many websites, applications, and public services. Fixing only one
deployment leaves disabled people encountering the same barrier everywhere
else that component is used.

When the responsible source is corrected, the contribution can:

- remove a barrier across many downstream products;
- establish the expected semantic or interaction behavior;
- add a regression test that protects future releases;
- improve component documentation and examples;
- reduce repeated accessibility remediation in individual projects;
- give affected users and accessibility specialists a shared place to improve
  the solution.

Accessibility work must still follow the project's design and contribution
process. A change to keyboard interaction, focus behavior, accessible names,
semantics, localization, or component APIs may require discussion before a
patch. Automated test results are evidence, not a complete accessibility
assessment. Manual testing and participation by disabled people remain
important.

The purpose is not merely to distribute compliance work. It is to prevent
shared components from repeatedly excluding people.

## Public investment should produce reusable public value

When public agencies independently purchase local fixes for the same
open-source dependency, public money can pay for the same work repeatedly.
Contributing reusable improvements can turn one procurement deliverable into a
public asset that other agencies, organizations, and communities can adopt.

This supports the principle behind the Free Software Foundation Europe's
[Public Money? Public Code!](https://fsfe.org/activities/publiccode/)
campaign, but publishing source code is not enough. Reusable public value also
requires an appropriate project home, documentation, tests, governance,
licensing, and ongoing maintenance.

Public-sector contracts should therefore make upstream participation possible
and expected. They should:

- grant the rights needed to contribute suitable work;
- budget for discovery, maintainer engagement, review, and revision;
- require an upstream-first assessment before custom development;
- require contribution when it is viable and accepted by the receiving
  project;
- require a written explanation when work remains downstream;
- identify the owner and lifecycle of every local patch;
- include upstream releases in upgrade and removal planning;
- evaluate vendor conduct and follow-through, not only code volume;
- support maintainers when public services materially depend on their work.

A contract cannot require an independent project to accept a contribution.
Procurement should require responsible effort and documented decisions, not
pretend that acceptance is under the vendor's control.

## Vendor integrity and community participation

Upstream-first changes vendor incentives. It rewards suppliers that understand
the projects they depend on, work within community governance, and leave behind
maintainable public value.

It discourages:

- proprietary wrappers that duplicate existing public capability;
- local forks created without a maintenance plan;
- patches that conceal defects rather than address their source;
- dependency substitutions chosen only to increase billable work;
- large AI-generated changes that shift review costs to maintainers;
- abandonment after an issue or pull request is opened.

Wrappers and local integrations are not inherently wrong. They may be
appropriate for instance-specific policy, deployment, data, or interoperability
requirements. The vendor should explain why the work belongs downstream, who
will maintain it, and what would allow it to migrate upstream later.

Open-source participation is a relationship, not a source-code delivery
mechanism. The
[Open Source Guides](https://opensource.guide/how-to-contribute/) emphasize
that every community has its own norms and that contributors need to understand
the project before proposing substantial work. A vendor's responsibility
continues through review, revision, release, and downstream adoption.

## Avoid the downstream patch cycle

A local override often creates a recurring maintenance cycle:

1. A dependency behavior is patched locally.
2. The dependency changes.
3. The patch conflicts, fails, or silently stops applying.
4. The local team investigates and revises it.
5. Tests and documentation are repeated.
6. The cycle continues until the patch is removed or the behavior is corrected
   upstream.

This is not eliminated by calling the patch temporary. Temporary work becomes
durable when it lacks an owner, review date, removal condition, and funded
migration path.

An upstream contribution does not simply transfer maintenance to unpaid
maintainers. A responsible contributor:

- works within the receiving project's priorities and architecture;
- keeps the change focused;
- provides appropriate tests and evidence;
- responds to review;
- supports backports or follow-up when agreed;
- helps downstream users adopt the released fix;
- remains accountable for any temporary local patch.

Upstream-first shares maintenance through the responsible project. It must not
be used to externalize an organization's costs onto a community.

## Security requires a different upstream path

Security vulnerabilities must not be handled like ordinary bugs. Publicly
opening an issue, publishing proof-of-concept code, creating a visible fork, or
submitting a public pull request can expose users before a fix is available.

Upstream-first still applies, but the path to upstream is confidential and
coordinated.

### Follow the project's security process

Before discussing a suspected vulnerability publicly:

1. Read the project's `SECURITY.md`, security advisory policy, supported-version
   policy, and disclosure instructions.
2. Determine whether the report describes a product vulnerability, an
   instance-specific misconfiguration, a compromised deployment, or an
   unsupported use.
3. Preserve evidence without copying secrets, personal data, client data,
   credentials, or exploit details into public systems.
4. Use the project's designated private reporting channel.
5. Allow the security team or maintainers to assess scope, severity, affected
   versions, disclosure timing, and release coordination.

GitHub repositories can enable
[private vulnerability reporting](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).
Other projects use private trackers, security email addresses, or dedicated
response teams. A public issue is not an acceptable substitute when a
confidential channel exists.

Projects and deploying organizations can also publish a machine-readable
reporting contact and policy using
[RFC 9116 `security.txt`](https://www.rfc-editor.org/rfc/rfc9116.html).
Publishing a reporting channel does not grant permission to test a system.

Drupal, for example, directs reporters to its confidential security tracker and
explicitly warns against posting covered vulnerabilities in public issue
queues, chat channels, or other public forums. See
[Reporting a security issue](https://www.drupal.org/docs/develop/issues/issue-procedures-and-etiquette/reporting-a-security-issue).

The OpenSSF
[coordinated vulnerability disclosure guide](https://github.com/ossf/oss-vulnerability-guide)
provides guidance and templates for reporting, embargoes, remediation, and
public disclosure. NIST's
[Secure Software Development Framework](https://doi.org/10.6028/NIST.SP.800-218)
also calls for defined vulnerability disclosure, remediation, response, and
communications processes.

### Coordinate upstream repair and downstream protection

The responsible response may require several activities under embargo:

- confirm the vulnerability and affected versions;
- identify related weaknesses or variants;
- prepare and review a minimal fix;
- add tests that do not unnecessarily publish an exploit;
- arrange supported-version backports;
- coordinate releases, advisories, identifiers, and credit;
- prepare downstream mitigations for deployments that cannot immediately
  upgrade;
- notify affected distributors or integrators through approved channels.

An urgent downstream mitigation may need to precede the upstream release. That
is a legitimate break-glass exception, not a reason to abandon upstream
coordination.

The downstream organization should maintain a restricted record containing:

- a confidential upstream reference or opaque internal identifier;
- the downstream owner;
- affected and supported versions;
- the date introduced and next review date;
- deployment and rollback instructions;
- the condition for replacing the mitigation with an upstream release;
- disclosure restrictions and authorized recipients.

Do not place a public upstream URL or revealing comment in source code while the
vulnerability is embargoed. A public `UPSTREAM-DEBT` annotation can itself leak
the existence or location of a vulnerability. Security debt records may need
restricted access until coordinated disclosure.

After disclosure and release, replace confidential references with public
advisories where appropriate, deploy the supported upstream fix, remove the
temporary mitigation, and retain only the records required by policy.

### AI-assisted security reports need stronger verification

AI tools can help inspect code and propose hypotheses, but a model-generated
claim is not a confirmed vulnerability. AI-assisted security work can produce
false positives, duplicate reports, invented dependencies, exaggerated
severity, or unsafe proof-of-concept material.

Before reporting an AI-assisted finding:

- reproduce the behavior in an authorized environment;
- verify the relevant versions, configuration, and attack assumptions;
- search privately available project information for known or duplicate work
  without disclosing the issue;
- distinguish observed behavior from model inference;
- assess impact from the risk holder's context;
- minimize proof-of-concept code and handle it as sensitive;
- disclose material AI assistance when the project's policy requires it;
- remain available to answer questions and help validate a fix.

Do not use AI to probe systems without authorization. Do not submit unverified
model output to a security team and expect maintainers to perform the missing
investigation.

## Maintainer capacity is a limiting resource

AI can increase contribution volume much faster than it increases trusted
review capacity. A pull request that takes minutes to generate may require
hours of maintainer work to understand, test, revise, or reject.

The Linux kernel's
[guidelines for tool-generated content](https://www.kernel.org/doc/html/latest/process/generated-content.html)
state that maintainer and reviewer bandwidth is scarce, require contributors to
understand and defend what they submit, and leave maintainers discretion to
reject or scrutinize generated work. Drupal's
[AI contribution policy](https://www.drupal.org/docs/develop/issues/issue-procedures-and-etiquette/policy-on-the-use-of-ai-when-contributing-to-drupal)
similarly places responsibility on the human contributor and rejects
unreviewed, unexplained, or abandoned AI output.

Upstream-first must therefore be paired with maintainer-ready contribution:

- read before writing;
- search before reporting;
- reproduce before asserting;
- ask before undertaking architectural work;
- prefer the smallest useful contribution;
- run available deterministic checks;
- explain uncertainty;
- disclose material assistance when required;
- respond to review;
- stop when the project prohibits the relevant AI use.

Sending more generated code upstream is not the goal. Improving the ratio of
useful contributions to maintainer effort is.

## Sustainability and resilience

Every additional implementation carries costs for development, testing,
storage, builds, deployment, documentation, security review, and human
attention. AI also carries compute and environmental costs. Upstream-first can
reduce avoidable duplication by encouraging reuse and shared maintenance.

This does not prove that every upstream contribution has a lower environmental
impact. A new dependency, oversized abstraction, unnecessary AI workflow, or
poorly maintained package can increase cost. The responsible choice is the
smallest viable solution with a credible owner and lifecycle.

Sustainable upstream practice includes:

- preferring deterministic tools when AI adds no material value;
- avoiding repeated high-compute analysis of already-known results;
- contributing reusable tests and fixes instead of regenerating local
  variants;
- minimizing dependencies and duplicated primitives;
- funding maintenance, review, and release work;
- planning for adoption, migration, and eventual removal.

## Upstream-first is not upstream-only

Some changes should remain downstream. Legitimate reasons include:

- local content, configuration, branding, policy, or workflow;
- a client-specific integration or contractual requirement;
- confidential information that cannot be generalized safely;
- a security embargo or active incident;
- unsupported upstream versions;
- incompatible licensing or governance;
- an upstream project that does not want the change;
- an emergency mitigation that cannot wait for a release;
- no existing project with credible ownership;
- a durable local capability that the organization is prepared to maintain.

These are decision inputs, not loopholes. A downstream decision should identify:

- why higher-ranked options are not viable;
- the responsible owner;
- supported versions and dependencies;
- security, privacy, accessibility, licensing, and sustainability effects;
- tests and documentation;
- review dates;
- migration, rollback, and removal conditions;
- any upstream issue, proposal, or confidential reference.

The classification remains provisional. The receiving project has the final say
on whether a proposed change is a bug, feature, security issue, or acceptable
contribution.

## What responsible upstream-first practice requires

### Before implementation

- Define the user or public outcome.
- Identify affected people, including disabled people where relevant.
- Inspect installed capabilities and extension points.
- Search for maintained existing solutions.
- Read the receiving project's current policies.
- Reproduce and classify the issue.
- Decide whether the work is instance, integration, dependency, or ecosystem
  scope.
- Apply accessibility, security, privacy, licensing, provenance,
  sustainability, and open-standards checks.

### During contribution

- Use the project's required channel.
- Ask before substantial features or architectural changes.
- Prepare the smallest useful issue, test, documentation change, proposal, or
  patch.
- Separate facts, inferences, and open questions.
- Provide appropriate regression evidence.
- Follow project style, test, release, and disclosure requirements.
- Keep a human accountable for all AI-assisted work.

### After submission

- Respond to maintainer questions and revise the work.
- Avoid pressuring maintainers for acceptance or priority.
- Track upstream status and supported releases.
- Maintain any downstream mitigation until migration is complete.
- Remove obsolete local patches.
- Document unresolved ownership and maintenance obligations.

## What success looks like

Upstream-first succeeds when:

- fewer organizations solve the same problem independently;
- disabled people benefit from fixes to shared components;
- vulnerabilities reach the responsible security process without premature
  disclosure;
- public investment produces reusable and maintainable public value;
- vendors participate responsibly in the communities they depend on;
- maintainers receive focused contributions rather than generated volume;
- temporary divergence is visible, owned, reviewed, and removed;
- AI supports human judgment instead of bypassing it.

The measure is not the number of upstream pull requests. It is whether each
change has a responsible home, appropriate evidence, accountable people, and a
sustainable path through its lifecycle.

## References

- CivicActions,
  [Contrib First](https://guidebook.civicactions.com/en/latest/common-practices-tools/contribution/contrib-first/)
- Linux Foundation,
  [Participating in Open Source Communities](https://www.linuxfoundation.org/resources/open-source-guides/participating-in-open-source-communities)
- Open Source Guides,
  [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- Free Software Foundation Europe,
  [Public Money? Public Code!](https://fsfe.org/activities/publiccode/)
- OpenSSF and CNCF,
  [Securing Open Source in the Age of AI](https://openssf.org/wp-content/uploads/2026/05/Securing-Open-Source-in-the-Age-of-AI.pdf)
- OpenSSF,
  [Guide to Coordinated Vulnerability Disclosure for Open Source Projects](https://github.com/ossf/oss-vulnerability-guide)
- NIST,
  [Secure Software Development Framework, SP 800-218](https://doi.org/10.6028/NIST.SP.800-218)
- IETF,
  [RFC 9116: A File Format to Aid in Security Vulnerability Disclosure](https://www.rfc-editor.org/rfc/rfc9116.html)
- GitHub,
  [Configuring private vulnerability reporting](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository)
- Drupal,
  [Reporting a security issue](https://www.drupal.org/docs/develop/issues/issue-procedures-and-etiquette/reporting-a-security-issue)
- Drupal,
  [Policy on the use of AI when contributing](https://www.drupal.org/docs/develop/issues/issue-procedures-and-etiquette/policy-on-the-use-of-ai-when-contributing-to-drupal)
- Linux kernel documentation,
  [Guidelines for tool-generated content](https://www.kernel.org/doc/html/latest/process/generated-content.html)
