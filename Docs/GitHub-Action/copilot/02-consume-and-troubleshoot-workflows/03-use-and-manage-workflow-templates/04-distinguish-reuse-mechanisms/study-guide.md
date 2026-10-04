# Distinguish starter workflows, reusable workflows, and composite actions

## What
The three mechanisms address different layers of reuse in GitHub Actions:
- Starter workflows are copied as a new workflow file.
- Reusable workflows are called by a job through `uses` and `workflow_call`.
- Composite actions package step logic for use inside a job.

## Why
Each mechanism creates a different ownership model, lifecycle, and permission boundary. Picking the wrong one often creates drift, hidden coupling, or a broader blast radius than intended.

## How
1. Ask what is being shared: an initial file, a workflow contract, or a step sequence.
2. Determine the invocation level: copy a file, call a job-level workflow, or use a step-level action.
3. Decide whether the consumer should own a local copy or receive centrally maintained behavior.
4. Compare interfaces, security boundaries, versioning expectations, and failure blast radius.

## Features
- Starter workflow: initial scaffold, local ownership after copy.
- Reusable workflow: centralized workflow contract invoked at job level.
- Composite action: step-level packaging for common actions or setup logic.
- Distinct trust and coupling models: each mechanism is designed for a different operational boundary.

## Do's and Don'ts
### Do
- Pick the smallest reusable unit that fits the requirement.
- Match the ownership model to the expected update pattern.
- Review interface and permissions for each mechanism before adoption.

### Don't
- Don't use a composite action when you need whole-workflow orchestration.
- Don't expect a starter workflow to provide central runtime updates.
- Don't treat a reusable workflow as a drop-in replacement for a step-level composite action.

## Real-life implementation
```yaml
jobs:
  ci:
    uses: org/platform/.github/workflows/ci.yml@v3

  setup:
    steps:
      - uses: org/platform/actions/setup-env@v1
```

The first example is job-level reusable workflow orchestration. The second is step-level action reuse. A starter workflow would instead create a new workflow file in the repository and let that copy evolve independently.

### Official references
- [Using starter workflows](https://docs.github.com/en/actions/writing-workflows/using-starter-workflows)
- [Reusing workflows](https://docs.github.com/en/actions/sharing-automations/reusing-workflows)
- [Creating a composite action](https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-composite-action)
- [Creating actions: choosing an approach](https://docs.github.com/en/actions/sharing-automations/creating-actions/about-custom-actions)

## Q&A
### Q: Every repository should start with the same CI skeleton but can evolve independently. Which mechanism fits?
A: A starter workflow fits because the repo gets a copied baseline, not a runtime dependency.

### Q: A centrally managed release pipeline should be updated once and used by many repositories. Which mechanism fits?
A: A reusable workflow fits because the orchestration remains centralized while callers invoke it with a stable contract.

### Q: A team wants to share repeated setup and test steps inside jobs. Which mechanism fits?
A: A composite action fits because those are step-level reusable commands that run inside a job.

### Q: Why does choosing the wrong reuse mechanism cause operational drift?
A: Because each mechanism carries different ownership and update semantics. A copied template drifts locally, a reusable workflow is centrally managed, and a composite action shares only step logic.
