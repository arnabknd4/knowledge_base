# Objective: Configure workflows to run for scheduled, manual, webhook, and repository events.

## What

A workflow is a policy document for automation: it defines when a run starts, which permissions it gets, and how far it reaches into your environment. The trigger is the boundary between external intent and internal execution. Choose the smallest event surface that satisfies the business need.

## Why

- `push` is excellent for CI but can over-trigger on README-only changes unless paths are restricted.
- `workflow_dispatch` is precise for operator-driven jobs but should be permissioned carefully.
- `schedule` is useful for compliance and housekeeping but runs in UTC and may surprise teams.
- Repository and webhook events are strong automation primitives but must be filtered to avoid noisy pipelines.

## How

Declare the event set under `on` and use supported branch, path, type, or cron filters to control when this workflow starts.

```yaml
name: release-gate
on:
  push:
    branches: [main]
  pull_request:
    types: [opened, synchronize, reopened]
  workflow_dispatch:
    inputs:
      environment:
        description: Deployment target
        required: true
        default: staging
        type: choice
        options: [staging, production]
  schedule:
    - cron: '0 6 * * 1-5'
```

## Features

Use event filters to separate routine CI, operator-initiated work, scheduled maintenance, and webhook-driven automation; each event determines both when the run starts and which trust assumptions apply.

**Official references**

- [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)
- [Scheduled workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule)
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Restrict triggers by branch, path, or event type to minimize unnecessary compute.
- Use manual dispatch for sensitive operations and keep production gates explicit.
- Review event payloads carefully; webhook-driven workflows may receive unexpected input.
- Concurrency and branch filters help reduce duplicate or overlapping runs.

**Don't**

- Don't confuse `schedule` with manual or repository-driven events.
- Don't overlook that `push` and `pull_request` behavior changes with branch protection and fork settings.
- Don't assume the event type is the only thing that matters; permissions and branch scope are equally important.

## Real-life implementation

For a production deployment, keep the dispatch interface narrow, set least-privilege permissions, and target a protected environment. Review UTC schedule timing and event payloads before enabling automation.

## Q&A

**Q: Which trigger is best for CI on every main-branch commit?**

**A:** Use `push` with a `branches` filter for commits to `main`; add path filters only when skipping a run cannot leave required checks misleading or incomplete.

**Q: Which trigger is best for a human-operated production deployment?**

**A:** Use `workflow_dispatch` for an explicit operator action, then enforce deployment approvals and branch restrictions through a protected environment.

**Q: Would your current trigger set accidentally run expensive jobs during low-risk repo changes?**

**A:** Review branch, path, and event-type filters, plus concurrency. Keep scheduled work on its intended cadence and remember schedules use UTC and may be delayed during high load.
