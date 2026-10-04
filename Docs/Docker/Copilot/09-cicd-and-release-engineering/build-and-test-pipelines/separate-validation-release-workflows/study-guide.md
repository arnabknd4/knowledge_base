# Separate pull-request validation from privileged release and deployment workflows

**Domain:** CI/CD and release engineering<br>
**Syllabus objective:** [Separate pull-request validation from privileged release and deployment workflows](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Validation executes potentially untrusted code; release/deploy workflows use powerful credentials. Keep trust domains distinct and make promotion an explicit protected transition.

## Why
A PR can modify build scripts, tests, and actions. If it inherits write or deployment rights, changes can exfiltrate credentials or publish a poisoned image.

## How
Run PR checks read-only on isolated runners, without production secrets and with constrained cache access. Release only from protected refs or approved tags; use environment approvals and scoped identities.

## Features
Separate jobs are not automatically isolated if they share persistent runners, credentials, writable caches, or artifacts. Make permissions explicit.

## Code snippets (if any)
```sh
PR job: read-only checkout, tests, no registry push. Release job: protected ref, approval, scoped identity, digest publication.
```

## Do's and Don'ts
Do: gate privileged work on trusted refs and approval. Don’t: run untrusted PR code in a secret-bearing release context or rely on branch-name checks alone.

## Real-life implementation
A fork PR uses an ephemeral runner. After merge and approval, a protected job signs and publishes the candidate; deployment identity can access only its target.

## Q&A
- **Q: Can PRs publish?** Only to isolated non-release namespaces with no promotion path.
- **Q: What is a protected environment?** A deployment gate with reviewers and scoped secrets.
- **Q: Are separate jobs isolated?** Not if runner, cache, artifacts, or credentials persist.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/build/ci/)
- [Docker documentation](https://docs.docker.com/build/ci/github-actions/)
