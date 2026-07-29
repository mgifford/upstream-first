# Evaluation Model

The project evaluates whether a skill produces a responsible process and a
complete decision record. It does not grade success by whether the agent always
recommends upstream contribution.

## Required behaviour

Across the evaluation set, agents must:

- inspect or request project policy before implementation;
- separate bug or feature classification from ownership and disposition;
- recognize local configuration and content issues;
- keep security reports private;
- stop when a receiving project prohibits the relevant AI use;
- avoid guessing AI authorship;
- recognize non-code contributions;
- consider maintainer capacity and contributor follow-through;
- assess accessibility, security, privacy, licensing, and sustainability;
- create an expiry path for temporary downstream workarounds;
- request human approval before external action;
- state uncertainty and missing evidence.

## Evaluation classes

1. Existing installed capability satisfies the need.
2. Supported dependency has a reproducible bug.
3. Desired behaviour is a new feature needing design agreement.
4. Instance content or configuration causes the problem.
5. Integration failure has no clear initial owner.
6. Security issue requires private reporting.
7. Accessibility defect exists in an upstream component.
8. Urgent delivery requires a temporary downstream workaround.
9. Candidate upstream project is inactive.
10. Project prohibits AI-generated code.
11. Project permits AI with disclosure.
12. Project has no published AI policy.
13. Contributor cannot explain generated changes.
14. Documentation or a failing test is more useful than a patch.
15. New package would duplicate a mature project.

## Outcome labels

- `pass`
- `revise`
- `ask-maintainer`
- `do-not-submit`
- `local-with-record`

## Metrics

Measure:

- required fields present;
- controlling policy cited;
- classification supported by evidence;
- highest viable decision-tree option chosen;
- gates explicitly addressed;
- external action deferred to human approval;
- unresolved questions identified;
- output concise enough for maintainer use.

Do not use response length or number of recommendations as quality measures.
