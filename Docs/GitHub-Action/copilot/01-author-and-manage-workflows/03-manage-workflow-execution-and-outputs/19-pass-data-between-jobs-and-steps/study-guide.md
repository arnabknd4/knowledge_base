# Objective: Pass data between jobs and steps using artifacts, outputs, environment files (`GITHUB_ENV` and `GITHUB_OUTPUT`), and reusable workflow outputs.

## What

Workflow state must move through explicit durable channels. Jobs do not share memory; data must be passed forward deliberately. This is where architecture becomes operationally visible.

## Why

- Step output is best for small, single-step data.
- Job outputs are required for cross-job passing.
- Artifacts are the right choice for larger files, logs, or binaries.

## How

Map small values through step and job outputs, use environment files within a job, and transfer files through artifacts.

```yaml
jobs:
  build:
    outputs:
      artifact_name: ${{ steps.meta.outputs.name }}
    steps:
      - id: meta
        run: echo "name=release-${GITHUB_SHA::7}" >> "$GITHUB_OUTPUT"

  deploy:
    needs: build
    steps:
      - run: echo "Deploying ${{ needs.build.outputs.artifact_name }}"
```

## Features

Environment files pass values to later steps in one job; step and job outputs pass small named values across explicit dependencies; artifacts transfer files; reusable workflows expose declared outputs to callers.

**Official references**

- [Workflow commands for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions)
- [Defining outputs for jobs](https://docs.github.com/en/actions/using-jobs/defining-outputs-for-jobs)
- [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Keep outputs small and explicit.
- Avoid passing sensitive data unless necessary and reviewed.
- Validate artifact names and paths before using them downstream.

**Don't**

- Don't overlook that outputs are not automatically available to later jobs.
- Don't mix `GITHUB_OUTPUT` and `GITHUB_ENV` usage incorrectly.
- Don't use logs as a data transport mechanism instead of a stable output contract.

## Real-life implementation

Choose the handoff based on data size, lifetime, and trust. Keep outputs small, map them through job/workflow contracts, and never treat an output from untrusted code as trusted authorization.

## Q&A

**Q: Which mechanism should carry a large deployment package: artifact or output?**

**A:** Use an artifact for files; outputs are intended for small strings or metadata, not file payloads.

**Q: Which mechanism should carry a version string or release name across jobs?**

**A:** Use a step output mapped to a job output and consume it through `needs`; map reusable workflow outputs explicitly when crossing that boundary.

**Q: Are any sensitive values being passed unintentionally across job boundaries?**

**A:** Audit output and artifact contents and avoid exporting credentials. Secret values should remain in secret channels and be scoped only to the consumer.
