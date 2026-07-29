# Review Notes

This package is complete enough for policy and workflow review. The following
decisions are intentionally not invented:

1. **Repository owner and final URL:** replace `OWNER/upstream-first` after the
   repository is created.
2. **Private conduct reporting contact:** publish a private contact before
   opening community participation. Do not use a public issue for conduct
   reports.
3. **License:** MIT is used for the draft because it permits broad reuse.
   Confirm whether MIT, Apache-2.0, or a reciprocal license better matches the
   intended governance.
4. **Maintainer group:** `@mgifford` is proposed as the initial code owner.
   Add at least one additional maintainer before declaring stable governance.
5. **External publishing:** this archive has not been published to GitHub,
   skills.sh, or a package registry.
6. **Schema identifiers:** the JSON Schema `$id` values use the reserved
   `example.org` domain until the final repository URL is known.
7. **Package-fit threshold:** the original fixed 80 percent threshold was
   removed because it implies unsupported precision. Candidate selection now
   requires documented fit, gaps, risk, compatibility, and maintenance.
8. **Forward evaluation:** repository validation and rule-based evaluation
   manifests are included. Independent model runs are deliberately deferred
   until the policy language is reviewed.

The draft omits Drupal and accessibility adapters. The charter makes that
sequencing explicit so domain-specific assumptions do not harden into the
general workflow.
