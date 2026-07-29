# Security Policy Discovery

Check sources in this order:

1. `SECURITY.md` in the affected repository and organization.
2. The repository's private vulnerability reporting or advisory interface.
3. The project's official security page and supported-version policy.
4. RFC 9116 `/.well-known/security.txt` on the official domain.
5. An official bug-bounty or vulnerability disclosure program.
6. Foundation, ecosystem, package-registry, or distribution security policy.
7. An already-published private maintainer contact.

Verify that the channel applies to the affected project and version. Do not
guess an address, send to a general public forum, or assume that a platform
feature is enabled.

Record:

- source URL or file;
- publisher and scope;
- date checked;
- supported versions;
- in-scope and out-of-scope systems or behaviours;
- authorized testing and safe-harbor terms;
- private contact method and encryption requirements;
- acknowledgment and disclosure expectations;
- credit preferences;
- AI-assisted report policy.

Useful references:

- [OpenSSF coordinated vulnerability disclosure guide](https://github.com/ossf/oss-vulnerability-guide)
- [NIST Secure Software Development Framework](https://doi.org/10.6028/NIST.SP.800-218)
- [RFC 9116 `security.txt`](https://www.rfc-editor.org/rfc/rfc9116.html)
- [GitHub private vulnerability reporting](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository)
- [Drupal security issue reporting](https://www.drupal.org/docs/develop/issues/issue-procedures-and-etiquette/reporting-a-security-issue)

If no verified private channel exists, return `blocked-no-channel` and request
direction. Coordinators such as a national CERT may be appropriate in some
cases, but selecting one depends on jurisdiction and should not be guessed.
