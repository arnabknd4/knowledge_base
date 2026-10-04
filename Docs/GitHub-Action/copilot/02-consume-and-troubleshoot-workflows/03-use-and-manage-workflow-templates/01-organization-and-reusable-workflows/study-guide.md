# Consume organization-level and reusable workflows

## What
Organization-level workflows and reusable workflows address different needs. A starter or template is copied into a repository; a reusable workflow is invoked centrally. GitHub Actions can standardize both, but they are not the same control plane or lifecycle model.

## Why
You need to decide whether a team should own an independent copy of a workflow or consume centrally managed behavior. The decision affects versioning, drift, permissions, and blast radius.

## How
1. Decide whether the requirement is a scaffold for local customization or centrally managed execution.
2. Check repository visibility, organization policy, and allowed caller references before using a workflow from another repo or org.
3. Review the callee workflow’s inputs, secrets, outputs, permissions, runner assumptions, and ref before consumption.
4. Grant only the minimum required permissions and use a stable ref when reproducibility matters.
5. Test the workflow contract in a non-production repository before rollout.

## Features
- Reusable workflows: central logic invoked from a job using `uses` and `workflow_call`.
- Organization templates: approved starting points copied into a repository.
- Contract review: inputs, secrets, outputs, permissions, and compatibility all matter.
- Version discipline: pinned refs reduce drift and unreviewed behavior changes.

## Do's and Don'ts
### Do
- Choose the mechanism that matches the lifecycle: copied scaffold vs. centrally maintained runtime.
- Review the called workflow’s contract and permissions before enabling it.
- Pin the workflow ref where change control matters.

### Don't
- Don't mistake an organization template for a live reusable workflow.
- Don't assume a reusable workflow can bypass caller permission limits.
- Don't ignore the risk of a moving branch ref when supply-chain reproducibility matters.

## Real-life implementation
```yaml
jobs:
  compliance:
    uses: org/platform/.github/workflows/compliance.yml@v2
    with:
      environment: production
    secrets: inherit
```

This is a reusable workflow pattern: the caller invokes a centrally managed workflow through a job, and the callee defines the contract. A starter workflow would instead be copied into the repository as a new workflow file with local ownership and no automatic central synchronization.

### Official references
- [Reusing workflows](https://docs.github.com/en/actions/sharing-automations/reusing-workflows)
- [Creating starter workflows for your organization](https://docs.github.com/en/actions/sharing-automations/creating-starter-workflows-for-your-organization)
- [Workflow syntax: `workflow_call`](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onworkflow_call)
- [Sharing workflows, secrets, and variables within an organization](https://docs.github.com/en/actions/sharing-automations/sharing-workflows-secrets-and-runners-with-your-organization)

## Q&A
### Q: A team wants a baseline workflow they can customize independently. Which mechanism fits?
A: A starter workflow or template is the correct choice because it creates a local copy that can evolve independently.

### Q: A central compliance job should run in many repos. Which mechanism fits and what contract must it expose?
A: A reusable workflow fits. It must expose a stable contract through `workflow_call` inputs, secrets, outputs, and permissions that the caller can satisfy.

### Q: Why review a reusable workflow before switching from a pinned SHA to a moving branch?
A: A moving branch changes behavior without a caller diff, which can silently alter security, permissions, or deployment logic.
