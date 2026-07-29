# Upstream First

Upstream First is a set of agent skills for placing changes in the right
open-source project and preparing contributions that maintainers can review,
accept, and sustain.

The project generalizes CivicActions'
[Contrib First](https://guidebook.civicactions.com/en/latest/common-practices-tools/contribution/contrib-first/)
practice beyond Drupal. It does not require every change to go upstream.
It requires an explicit ownership decision before custom local code is treated
as the default.

This repository is a pre-release review draft.

## Skills

| Skill | Use it to | Primary output |
| --- | --- | --- |
| [`upstream-first`](skills/upstream-first/SKILL.md) | Decide whether a change belongs in an installed dependency, upstream project, extension, new reusable package, or local implementation | Decision record |
| [`maintainer-ready-contribution`](skills/maintainer-ready-contribution/SKILL.md) | Prepare an issue, proposal, patch, or pull request for the receiving project | Contribution package |
| [`ai-contribution-review`](skills/ai-contribution-review/SKILL.md) | Review known AI-assisted work against the receiving project's policy and human-accountability requirements | Review decision |

## Operating sequence

1. Use `upstream-first` before implementation.
2. Use `maintainer-ready-contribution` when an upstream path is viable.
3. Use `ai-contribution-review` before submitting any known AI-assisted
   contribution.
4. Require human approval before an agent creates or changes anything in an
   external project.

The receiving project's rules override this project's defaults.

## Install

The skills follow the
[Agent Skills specification](https://agentskills.io/specification/) and use the
standard `skills/<skill-name>/SKILL.md` layout.

After this repository is published, a named skill can be installed with a
compatible client. For example:

```bash
npx skills add OWNER/upstream-first --skill upstream-first
npx skills add OWNER/upstream-first --skill maintainer-ready-contribution
npx skills add OWNER/upstream-first --skill ai-contribution-review
```

Replace `OWNER` after the repository location is finalized.

## Project documents

- [Charter](CHARTER.md)
- [Contributing](CONTRIBUTING.md)
- [Governance](GOVERNANCE.md)
- [AI contribution policy](AI_CONTRIBUTION_POLICY.md)
- [Accessibility](ACCESSIBILITY.md)
- [Security](SECURITY.md)
- [Sustainability](SUSTAINABILITY.md)
- [Standards registry](references/STANDARDS.md)
- [Source bibliography](references/SOURCE_BIBLIOGRAPHY.md)
- [Review notes](REVIEW_NOTES.md)

## Validation

Run:

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

The validator checks skill metadata, required repository files, JSON schemas,
examples, evaluation manifests, and relative Markdown links. It does not claim
to prove that an agent will make correct contribution decisions.

## License

The review draft uses the [MIT License](LICENSE) to permit broad reuse and
adaptation. Confirm this choice before the first public release.
