# Objective: Pass inputs to reusable workflows through `workflow_call`, including inputs and secrets mapping.

## What

Reusable workflows are internal APIs. The caller invokes a definition with a bounded contract: inputs, outputs, and secrets. That contract should reflect the function the workflow exists to provide.

## Why

- Reusable workflows centralize logic but create a shared contract that must be maintained.
- Secrets mapping is explicit and reviewable, which is safer than relying on broad inheritance.
- Narrow, typed inputs improve maintainability and reduce accidental misuse.

## How

Declare the called workflow contract under `workflow_call` and map caller values and secrets explicitly at the job call site.

```yaml
# reusable workflow
on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
    secrets:
      CLOUD_CREDENTIALS:
        required: true
```

```yaml
# caller
jobs:
  call-deploy:
    uses: ./.github/workflows/deploy.yml
    with:
      environment: production
    secrets:
      CLOUD_CREDENTIALS: ${{ secrets.CLOUD_CREDENTIALS }}
```

## Features

A reusable workflow defines a typed interface under `workflow_call`; callers pass values through `with` and secrets through the declared secret interface. Explicit contracts make shared automation reviewable.

**Official references**

- [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Pass only required values and secrets, not everything from the caller context.
- Keep reusable workflow interfaces stable as code evolves.
- Validate inputs before cloud or deploy actions run.

**Don't**

- Don't assume a reusable workflow automatically gets every caller secret.
- Don't overlook that `workflow_call` uses a different contract than `workflow_dispatch`.
- Don't expose broad or loosely typed inputs to deployment logic.

## Real-life implementation

Reusable workflows centralize repeated policy and deployment logic, but callers must map the correct inputs and credentials. Validate target values in the called workflow and pin the called workflow ref according to organizational policy.

## Q&A

**Q: Which values belong in `with` versus `secrets`?**

**A:** Pass non-sensitive parameters through `with`; pass credentials through explicitly declared `secrets` (or deliberately use `inherit` when its scope is appropriate).

**Q: What happens if a required secret is omitted from the caller?**

**A:** The call does not satisfy the reusable workflow contract and fails validation or execution; declare required secrets and map them at the call site.

**Q: Could the reusable workflow accidentally run with a stale or invalid environment name?**

**A:** Yes, if the input is not constrained. Type and validate the target, then bind deployment to a configured environment with its protection rules.
