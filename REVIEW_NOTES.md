# Review Notes

This package is complete enough for policy and workflow review. The following
decisions are intentionally not invented:

1. **Private conduct reporting contact:** publish a private contact before
   opening community participation. Do not use a public issue for conduct
   reports.
2. **License:** MIT is used for the draft because it permits broad reuse.
   Confirm whether MIT, Apache-2.0, or a reciprocal license better matches the
   intended governance.
3. **Maintainer group:** `@mgifford` is proposed as the initial code owner.
   Add at least one additional maintainer before declaring stable governance.
4. **skills.sh publishing:** the repository is public but the skills have not
   been separately reviewed or promoted through skills.sh.
5. **Package-fit threshold:** the original fixed 80 percent threshold was
   removed because it implies unsupported precision. Candidate selection now
   requires documented fit, gaps, risk, compatibility, and maintenance.
6. **Forward evaluation:** repository validation and rule-based evaluation
   manifests are included. Independent model runs are deliberately deferred
   until the policy language is reviewed.
7. **Security integration:** the disclosure skill is reporter-side. It does
   not replace a maintainer security-response program, incident response, or
   authorized security testing.

The draft still omits Drupal and accessibility adapters. The charter makes that
sequencing explicit so domain-specific assumptions do not harden into the
general workflow.
