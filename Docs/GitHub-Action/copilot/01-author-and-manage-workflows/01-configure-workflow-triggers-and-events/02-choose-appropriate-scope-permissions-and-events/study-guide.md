# Objective: Choose appropriate scope, permissions, and events for workflow automation.

## What

Workflow scope is a trust boundary. Triggers determine when a workflow runs; permissions determine what it is allowed to do. A secure design uses the least privilege that still supports the use case.

## Why

- Repository-level permissions are simpler but broader than necessary.
- Job-level permissions are safer for sensitive automation and easier to review.
- `pull_request` and `pull_request_target` have very different trust implications.
- `id-token: write` is ideal for OIDC federation but should be scoped to the jobs that need it.

## How

Set minimal workflow permissions, then grant any additional capability at the narrowest job that needs it; choose triggers with the code trust level in mind.

```yaml
permissions:
  contents: read
  packages: write
  id-token: write

jobs:
  build:
    permissions:
      contents: read
      actions: read
  deploy:
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
```

## Features

Separate the event that starts automation from the permissions granted to each job. Trust depends on the source of the code and event payload as well as the token, secrets, and execution environment.

**Official references**

- [Workflow permissions for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#permissions)
- [Using GitHub Actions with OIDC](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Use the default `GITHUB_TOKEN` with narrow scopes.
- Keep untrusted code out of privileged jobs.
- Distinguish between a branch validation workflow and a production deployment workflow.

**Don't**

- Don't assume that trigger choice alone determines trust.
- Don't overlook that branch context changes the trust boundary.
- Don't use broad default permissions when job scoping is possible.

- Don't expand write permissions just because the workflow is convenient.

## Real-life implementation

A PR validation job can usually run with read-only repository permissions, while a deployment job can receive only its needed write permissions after trusted checks and environment gates. Treat fork contributions as untrusted input.

## Q&A

**Q: Which permissions are required for a PR validation job versus a production deploy?**

**A:** Start with `permissions: {}` and grant only what is needed: commonly read access for checkout/validation and narrowly scoped write access only in the deployment job.

**Q: Would a fork PR job be entitled to write to the repository or a cloud environment?**

**A:** Do not grant it privileged access. Fork PR workflows normally have restricted token/secrets behavior, but repository settings and trigger choice matter; isolate untrusted code from privileged jobs.

**Q: Does your workflow use the least privilege needed for each job?**

**A:** Review the effective `GITHUB_TOKEN` permissions, available secrets, and any OIDC trust policy per job; use short-lived identity federation when appropriate.
