# Standards Registry

Checked: 29 July 2026

## Policy

Use the latest applicable stable release where practical. Do not upgrade
silently when a receiving project, law, contract, runtime, or interoperability
requirement depends on another version.

For each standard:

1. Verify its publisher, status, version, and latest published URL.
2. Distinguish standards, recommendations, drafts, community specifications,
   and practitioner guidance.
3. Record the exact version in conformance claims and machine-readable output.
4. Assess compatibility and migration impact before upgrading.
5. Review this registry at least every 90 days and before each minor or major
   release.

The key words "MUST", "MUST NOT", "REQUIRED", "SHOULD", "SHOULD NOT",
"RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in
BCP 14, RFC 2119 and RFC 8174, only when they appear in uppercase.

## Normative formats and conventions

| Item | Version or status | Use |
| --- | --- | --- |
| [Agent Skills specification](https://agentskills.io/specification/) | Current published specification, no numbered release exposed | Skill structure, frontmatter, progressive disclosure, and validation |
| [JSON Schema](https://json-schema.org/draft/2020-12/schema) | Draft 2020-12 | Decision-record and AI-review schemas |
| [YAML](https://yaml.org/spec/1.2.2/) | 1.2.2 | Skill frontmatter and agent interface metadata |
| [CommonMark](https://spec.commonmark.org/) | Current published specification | Portable Markdown where GitHub-specific syntax is unnecessary |
| [BCP 14](https://www.rfc-editor.org/info/bcp14) | RFC 2119 plus RFC 8174 | Normative requirement language |
| [Semantic Versioning](https://semver.org/spec/v2.0.0.html) | 2.0.0 | Project releases after a public interface is declared |
| [SPDX specification](https://spdx.github.io/spdx-spec/v3.0.1/) | 3.0.1 | License and provenance identifiers where machine-readable records are needed |

## Accessibility

| Item | Version or status | Use |
| --- | --- | --- |
| [WCAG](https://www.w3.org/TR/WCAG22/) | 2.2, W3C Recommendation | User-facing web content and interface target |

WCAG 2.2 Level AA is the project target. Applicable Level AAA criteria are
aspirational. A receiving project or legal requirement may require another
version or level.

## Informative guidance

| Item | Status | Use |
| --- | --- | --- |
| [W3C Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) | Group Note Draft, 29 July 2026 | Sustainability analysis; do not claim W3C Recommendation status |
| [OpenSSF Best Practices](https://best.openssf.org/) | Community and foundation guidance | Secure development and project evaluation |
| [OpenSSF Scorecard](https://openssf.org/projects/scorecard/) | Automated assessment tool | Security evidence; not proof of security |
| [REUSE Specification](https://reuse.software/spec/) | Community specification | File-level copyright and license information when adopted |
| [Contributor Covenant](https://www.contributor-covenant.org/version/3/0/code_of_conduct/) | Version 3.0 community agreement | Reference for community conduct policy |

## Update record

When updating this file, include:

- date checked;
- previous and new versions or status;
- compatibility effect;
- files and evaluations affected;
- migration or deprecation plan.
