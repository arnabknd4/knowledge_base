# Objective: Add workflow status badges and environment protections.

## What

Badges communicate visibility; environment protections enforce real controls. A safe workflow uses both: visible status for transparency and protected environments for deployment governance.

## Why

- A badge is helpful for communication but is not a control plane.
- Protected environments slow down deployment but reduce the chance of accidental production change.
- The environment and branch policy should match actual operational risk.

## How

Add a badge for visibility and configure the deployment job to reference the named environment whose protection rules should govern it.

```yaml
jobs:
  deploy:
    environment:
      name: production
      url: https://example.com
    runs-on: ubuntu-latest
```

## Features

A status badge exposes selected workflow health as a link or image; an environment is a deployment boundary where configured protection rules, secrets, and deployment history can apply.

**Official references**

- [Adding a workflow status badge to your repository](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge)
- [Using environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)
- [Required reviewers for environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment#required-reviewers)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Require approvals for production environments.
- Keep badge status aligned with actual workflow health.
- Use environment metadata and URL targets to reduce confusion during operational runs.

**Don't**

- Don't treat a badge as a security control rather than an informational signal.
- Don't overlook that environment protection is runtime policy, not just a UI label.
- Don't allow high-impact deployments without the required approval gates.

## Real-life implementation

Choose a badge that represents the signal consumers need, but rely on environment protection—not badge state—for deployment authorization. Approval availability and protection features depend on repository/organization configuration.

## Q&A

**Q: Does the workflow badge reflect real deployment health and not just a partial build status?**

**A:** Select the relevant workflow and branch/status context; ensure its result actually covers the release or deployment outcome being communicated.

**Q: Is production protected by the right environment approvals and checks?**

**A:** Configure the production environment with the required reviewers and applicable branch/tag or other protection rules, then verify the deployment job references it.

**Q: Would an operator know which environment is being deployed and what risks are in play?**

**A:** Expose the environment name and deployment URL where useful, and present the change and checks clearly before approval.
