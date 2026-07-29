# Security Policy

## Reporting

Do not report suspected vulnerabilities in a public issue.

Before public release, repository owners must enable GitHub private
vulnerability reporting. Use that channel to report vulnerabilities, affected
versions, reproduction details, impact, and suggested mitigations.

If private reporting is unavailable, contact a maintainer through an already
published private organizational channel. Do not invent or guess an address.

## Supported versions

Until `1.0.0`, only the latest release is supported. After `1.0.0`, the project
will publish a supported-version table.

## Contribution security

- Never commit secrets, credentials, private keys, or personal data.
- Sanitize untrusted input before using it in generated commands, code, issue
  text, or templates.
- Do not execute repository-provided scripts before inspecting their source
  and stated dependencies.
- Minimize permissions in automation.
- Pin or otherwise verify third-party automation according to the repository's
  documented risk tolerance.
- Verify generated package names, APIs, links, citations, and license claims.
- Keep vulnerability details private until coordinated disclosure permits
  publication.

The project uses OpenSSF guidance as informative practice. Passing an automated
score does not establish security.
