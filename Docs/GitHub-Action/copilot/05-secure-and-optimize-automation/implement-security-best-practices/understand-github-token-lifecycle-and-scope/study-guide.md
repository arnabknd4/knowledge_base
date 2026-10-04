# GH-200 study guide: understand the GITHUB_TOKEN lifecycle and scope

## What

`GITHUB_TOKEN` is a GitHub App installation token that GitHub Actions creates for workflow jobs. It is available to that job, scoped to the repository and permissions granted for the run, and expires when the job finishes (with a maximum lifetime of 24 hours). Workflow- and job-level `permissions` control its access; when explicit permissions are set, unspecified permissions are set to `none`.

Objective link: [GH-200 syllabus — implement security best practices](../../../../copilot-github-syllabus.md#implement-security-best-practices).

## Why

An over-permissioned token can let compromised workflow code change repository contents, publish packages, or affect other resources. Pull-request workflows that handle untrusted contributions are especially sensitive. `GITHUB_TOKEN` is usually safer than a long-lived user PAT for same-repository automation, but it remains a credential and must be scoped to the job's actual work.

## How

- Set a restrictive workflow-level baseline, then grant additional permissions only to jobs that require them.
- Use `contents: read` for ordinary checkout/build jobs; grant narrowly scoped writes only for publishing, checks, attestations, or other necessary operations.
- Remember that the `permissions` map both grants and removes scopes: omitted permissions become `none` when specifying the map.
- Avoid exposing write-capable tokens to untrusted pull-request code. Fork pull-request workflows generally receive read-only token permissions unless repository settings explicitly allow write tokens; do not rely on that safeguard as the only control.
- Use a PAT or GitHub App only when needed for an identity or access boundary that `GITHUB_TOKEN` cannot satisfy; prefer fine-grained scope, short lifetime, and managed ownership.

```yaml
permissions:
  contents: read

jobs:
  publish:
    permissions:
      contents: read
      packages: write
```

Only the `publish` job can publish packages; add other permissions only if its steps need them.

## Features

- **Short-lived job token:** generated for Actions work and not a durable user credential.
- **Granular permission scopes:** configure read/write rights at workflow or job level.
- **Default permission settings:** repository/organization settings influence defaults, so explicit least privilege is more predictable.
- **Different credential models:** PATs represent a user and may remain valid beyond a run; GitHub Apps can provide managed automation identities and installation scopes.

## Do's and Don'ts

**Do**
- Specify `permissions` explicitly and make write grants job-specific.
- Check event type and fork behavior for workflows handling untrusted code.
- Store no token in logs, artifacts, or generated files; use secrets masking as a safeguard, not a guarantee.
- Prefer the ephemeral token for same-repository operations and evaluate GitHub Apps for managed cross-repository automation.

**Don't**
- Assume `GITHUB_TOKEN` is harmless because it is automatically created.
- Grant `write-all` or repository-wide write scopes to test jobs.
- Assume setting permissions at workflow level prevents a job from receiving a broader token configuration—verify effective job permissions.
- Replace a needed identity design with a broadly scoped, long-lived PAT.

## Real-life implementation

A CI workflow sets `contents: read` for all jobs. A release job gets `contents: write` only if it must create a release, while a package job receives `packages: write`. The PR test job has no write permissions and no deployment secrets. This reduces the impact of malicious PR code or a compromised build dependency without blocking authorized release tasks.

## Q&A

**Q: Is `GITHUB_TOKEN` shared as a single long-lived token across runs?**

A: No. GitHub creates a token for Actions jobs, with a short lifetime tied to the job and configured permissions.

**Q: What happens to omitted permissions after an explicit `permissions` map is added?**

A: They are set to `none`; grant every required permission deliberately.

**Q: Is a PAT always more capable than `GITHUB_TOKEN`?**

A: A PAT can act with its associated user's access and may satisfy cross-repository or user-identity use cases, but that broader and longer-lived authority also increases risk.

**Q: Does read-only fork token behavior remove the need to isolate PR workflows?**

A: No. Untrusted code can still attack runners or accessible data; keep the job isolated, avoid secrets, and minimize permissions.

### References

- [About GITHUB_TOKEN](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)
- [Workflow permissions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#permissions)
- [Managing personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
