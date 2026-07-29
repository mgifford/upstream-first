# Cross-Repository Git Workflow

Discover the receiving project's workflow before proposing commands. Do not
assume a remote name, forge, default branch, release branch, or contribution
model.

## Read-only discovery

Run only when local repository inspection is within scope:

```bash
git remote -v
git status --short --branch
git branch --show-current
git remote show origin
```

Also inspect:

- `CONTRIBUTING`, `SECURITY.md`, governance, and release documentation;
- repository metadata for the actual default branch;
- existing remotes before adding another;
- supported and release branches;
- required fork, issue, sign-off, CLA, DCO, and review procedures.

Dependency release cadence cannot be inferred from a branch name. Verify
release documentation, tags, supported-version policy, and maintainer guidance.

## Local setup template

Only after verifying each placeholder:

```bash
git remote add <verified-upstream-name> <verified-repository-url>
git fetch <verified-upstream-name> --prune
git switch --create <topic-branch> <verified-upstream-name>/<verified-base-branch>
```

Before `git remote add`, confirm that the chosen name does not already exist.
`upstream` is a convention, not a requirement.

## Permission boundaries

- Read-only discovery does not authorize a local change.
- A request to implement may authorize local branches and commits within the
  stated repository.
- Pushing, opening an issue, submitting a security report, or creating a pull
  request is an external write and requires human approval.
- Never force-push, rewrite shared history, or guess a remote target.
- Suspected vulnerabilities use `responsible-security-disclosure`, not this
  public workflow.
