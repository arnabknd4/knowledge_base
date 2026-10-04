# GH-200 study guide: environment protections and approval gates

## What

GitHub Actions environments represent deployment targets such as staging and production. A job that references an environment can be subject to protection rules, deployment branch/tag restrictions, wait timers, and required reviewers. Environment secrets and variables are scoped to jobs that reference that environment; secrets are not made available to the job until its protection rules are satisfied. Availability and some protection-rule options vary by repository visibility, plan, and administrative settings.

Objective link: [GH-200 syllabus — implement security best practices](../../../../copilot-github-syllabus.md#implement-security-best-practices).

## Why

Production credentials exposed to ordinary build and pull-request jobs increase blast radius. Environment gates put a deliberate control in front of deployments, while branch restrictions help ensure that only intended refs can deploy. They complement—not replace—code review, branch protection, safe workflow triggers, and least-privilege cloud permissions.

## How

- Create separate environments for distinct targets and scope each target's credentials there rather than in repository-wide secrets.
- Reference the intended environment on the deployment job. Protection rules apply to jobs that reference that environment; they do not automatically gate unrelated jobs.
- Restrict deployment branches/tags and configure required reviewers or wait timers where supported and appropriate.
- Check which users can approve, whether self-review is disallowed, and which event/ref can reach the deployment job.
- Keep build/test work separate from deploy work so untrusted PR code does not receive production credentials.

```yaml
jobs:
  deploy:
    if: github.ref == 'refs/heads/main'
    environment:
      name: production
      url: https://apps.example.com
    permissions:
      contents: read
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d8e5b6821dfbee0d # v4.2.2
      - name: Deploy
        run: ./deploy.sh
```

Configure required reviewers and deployment-ref restrictions on the `production` environment in repository settings; the YAML reference alone does not create those protections.

## Features

- **Required reviewers:** pause a deployment job until a configured reviewer approves, if enabled and available for the repository.
- **Deployment branch/tag rules:** limit which refs may deploy through that environment.
- **Wait timers and custom protection rules:** add delays or external checks where supported.
- **Environment-scoped values:** provide environment-specific secrets/variables to jobs after applicable protection rules pass.
- **Deployment visibility:** environment URLs and deployment records make releases easier to trace.

## Do's and Don'ts

**Do**
- Put production secrets in the production environment and grant them only to deploy jobs that need them.
- Test protections with the actual workflow trigger and ref; check the pending-deployment experience.
- Require approval from appropriate people and use protected source branches.
- Keep cloud IAM, token permissions, and deployment script access narrow.

**Don't**
- Assume naming a job's environment in YAML automatically configures reviewer or branch rules.
- Put sensitive deployment credentials in repository-level secrets if they only belong to production.
- Treat an approval gate as proof that the workflow's code or artifact is trustworthy.
- Allow untrusted PR code to run in a privileged deployment job merely because approval is configured.

## Real-life implementation

A service team runs tests for every pull request using read-only permissions and no production credentials. Only a deployment job on the protected `main` branch references `production`; that environment permits the protected branch and requires an operations reviewer. The job receives its environment-scoped credential only after protection rules pass. A reviewer still confirms the artifact and change; the approval is not a substitute for provenance checks or cloud-side least privilege.

## Q&A

**Q: When do environment secrets become available to a deployment job?**

A: The job must reference the environment, and its protection rules must be satisfied before it proceeds with those secrets available.

**Q: Do required reviewers apply to every job in a workflow?**

A: No. They gate jobs that reference the protected environment, not unrelated jobs.

**Q: Does a branch restriction replace repository branch protection?**

A: No. It restricts deployment refs for that environment; branch protection governs changes and merges to the source branch.

**Q: Does using an environment guarantee production safety?**

A: No. Trigger design, code review, artifact verification, token scope, and cloud authorization remain important.

### References

- [Environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)
- [Environment protection rules](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment#environment-protection-rules)
- [Required reviewers](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment#required-reviewers)
