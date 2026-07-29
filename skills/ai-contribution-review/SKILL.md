---
name: ai-contribution-review
description: Review known or disclosed AI-assisted open-source code, documentation, tests, issues, pull requests, reviews, translations, or design work before submission. Use when AI materially helped produce a contribution, when a project has AI contribution rules, when a contributor or maintainer requests AI-specific preflight review, or when checking disclosure, provenance, privacy, human understanding, test evidence, scope, and maintainer burden. Do not use it to detect undisclosed AI authorship from style.
---

# AI Contribution Review

Apply the receiving project's AI policy before evaluating quality. Review the
work and the contributor's accountability, not a guessed identity or writing
style.

## Modes

- **Contributor preflight:** determine whether known AI-assisted work is ready
  to submit.
- **Maintainer review:** evaluate disclosed AI-assisted work consistently with
  project policy.
- **Policy assessment:** determine what activities a project's AI rules cover.

Do not use this skill as an AI detector.

## Workflow

### 1. Establish known facts

Record:

- receiving project and contribution type;
- AI tool or model if known;
- activities materially assisted;
- human review and tests completed;
- data or repository context provided to the tool;
- contributor availability for follow-up.

Do not require a person to prove a negative when AI use is unknown.

### 2. Discover policy

Inspect repository, organization, foundation, contribution, security,
licensing, privacy, and AI policies.

Read [policy-model.md](references/policy-model.md). Classify each relevant
activity as:

- prohibited;
- restricted;
- permitted with disclosure;
- permitted under ordinary rules;
- unspecified;
- conflicting.

If prohibited, stop producing or submitting content within the prohibited
scope. If restricted, enforce the stated boundary. If unspecified or
conflicting, ask before substantial external contribution.

### 3. Check human accountability

Confirm that a human:

- initiated and approved the contribution;
- reviewed the final diff or text;
- can explain material choices and limitations;
- can revise the work without blindly regenerating it;
- verified claims, dependencies, APIs, citations, and tests;
- will respond to maintainer feedback.

If the contributor cannot explain a material change, return `do-not-submit` or
`revise`.

### 4. Review the contribution

Read [review-gates.md](references/review-gates.md). Check:

- project fit and prior agreement;
- smallest coherent scope;
- correctness and final-state accuracy;
- test evidence and manual review;
- generated verbosity, unrelated refactoring, and speculative abstractions;
- accessibility and affected-user impact;
- security, privacy, confidential data, and authorization boundaries;
- copyright, license, attribution, and provenance;
- dependency and supply-chain risk;
- compatibility and standards;
- sustainability and maintainer review cost.

Require deterministic checks where they can answer the question. Do not accept
claims that tools or tests ran without evidence.

### 5. Check disclosure

Follow the project's required wording and location. When material disclosure is
required, include tool or model if known, uses, human verification, and known
limitations.

Do not expose private prompts, confidential data, or security details merely to
prove disclosure.

If the material under review may describe an undisclosed vulnerability, stop
the public review path and use `responsible-security-disclosure`. Apply any AI
restrictions in the security policy before placing evidence in an AI system.

### 6. Select an outcome

Use one:

- `pass`: policy permits the work and all material gates pass;
- `revise`: correctable problems remain;
- `ask-maintainer`: policy, scope, or authority is ambiguous;
- `do-not-submit`: prohibited use, absent human understanding, unsafe data
  handling, fabricated evidence, or unacceptable risk;
- `local-with-record`: external submission is unsuitable but a justified local
  path remains.

Use [ai-review-report.md](assets/ai-review-report.md). Cite evidence and state
uncertainty.

External submission always requires human approval.

## Maintainer fairness

- Apply published policy consistently.
- Review the contribution rather than inferred authorship.
- Do not use AI detection scores as evidence.
- Do not penalize concise assistive use, translation, or accessibility tooling
  that policy permits.
- Distinguish mandatory corrections from optional suggestions.
- Close unreviewable work promptly and explain the controlling rule.

## Completion check

Complete only when:

- policy state and covered activities are explicit;
- no AI-authorship inference is treated as evidence;
- human understanding and follow-through are assessed;
- final work, tests, provenance, privacy, and scope are reviewed;
- outcome and required corrections are concise;
- human approval remains required before external action.
