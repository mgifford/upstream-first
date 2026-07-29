# Project Policy Discovery

Project policy discovery precedes implementation and external interaction.

## Sources to inspect

Check the receiving project and its parent organization for:

1. `README`, `CONTRIBUTING`, `GOVERNANCE`, `CODE_OF_CONDUCT`, `SECURITY`,
   `SUPPORT`, and license files.
2. `AGENTS.md`, AI contribution policies, bot policies, and automation
   instructions.
3. Issue forms, pull-request templates, labels, and contribution checklists.
4. CLA, DCO, sign-off, copyright, and provenance requirements.
5. Supported versions, release branches, deprecation policy, and compatibility
   matrix.
6. Public roadmaps, architecture decisions, and design-proposal processes.
7. Recent accepted and rejected issues and pull requests for the same type of
   change.
8. Private security-reporting instructions.

## Authority order

Apply:

1. law, regulation, contract, and confidentiality duties;
2. repository policy;
3. organization or foundation policy;
4. project documentation and maintainer decisions;
5. this project's defaults.

The newest document is not always authoritative. Check scope, status, and
whether a newer file supersedes it.

## AI policy model

Record both policy state and covered activity.

### State

- `prohibited`
- `restricted`
- `permitted-with-disclosure`
- `permitted-under-ordinary-rules`
- `unspecified`
- `conflicting`

### Activity

- code generation;
- tests;
- documentation;
- issue and pull-request text;
- review comments;
- translation;
- research and summarization;
- autocomplete;
- automated external actions.

Do not infer that `unspecified` means permission or prohibition. Ask before a
substantial contribution. Do not use a stylistic AI detector.

## Project readiness

Determine whether:

- the project is active enough to review the work;
- the affected version is supported;
- maintainers are accepting the proposed kind of contribution;
- the contribution channel is public or private;
- the work needs an issue or design agreement before a patch;
- a maintainer or working group has authority over the area;
- the contributor can remain available for follow-up.

## Evidence record

For each controlling rule, record:

- URL or repository path;
- title;
- authority and scope;
- version, branch, or date;
- exact requirement in a short paraphrase;
- uncertainty or conflict;
- date checked.

Quote only what is necessary and permitted. Prefer links and paraphrases.
