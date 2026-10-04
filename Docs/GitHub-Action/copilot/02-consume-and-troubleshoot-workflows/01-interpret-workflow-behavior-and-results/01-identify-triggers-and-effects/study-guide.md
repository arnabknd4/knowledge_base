# Identify workflow triggers and their effects

## What
A workflow run is created only when the event matches the workflow’s trigger rules and repository conditions. The `on:` block defines the event type, filters, and supporting semantics; the run metadata then shows the actual event that fired. For diagnosis, treat the workflow configuration and the run record as separate layers: one answers “what should have run?”, while the other answers “what actually ran?”

## Why
Trigger mistakes are common and easy to misread. A workflow can be valid YAML but never run because a branch filter, path filter, activity type, or default-branch rule excluded it. Similarly, a job can exist in a workflow yet still be skipped because of `if` conditions, dependencies, or concurrency policy. Without checking the true trigger and the run record, you may debug the wrong layer.

## How
1. Start with the event declaration in the workflow file and read the exact branch, path, and activity filters used on the intended ref.
2. Confirm whether the event is a push, pull request, pull_request_target, workflow_dispatch, workflow_run, or scheduled event, and note the ref/actor/branch semantics for that event type.
3. Compare the expected event against the run metadata: event name, branch, SHA, actor, and commit message in the run details.
4. If the workflow did not fire, inspect repository rules, default branch context, path filters, branch/tag filters, and any policy or workflow visibility constraints.
5. If the workflow did fire but later jobs are skipped, inspect job-level `if`, dependencies, permissions, and concurrency rather than assuming the trigger was wrong.

A pull request is a special case: `pull_request` runs against the synthetic merge ref, while the source branch still exists as a head branch. `pull_request_target` is executed in the base repository context and has a much higher trust boundary than `pull_request`, so it should be used only for carefully controlled privileged operations and never with untrusted contributor code.

## Features
- Event and payload awareness: events such as `push`, `pull_request`, `workflow_dispatch`, and `workflow_run` have different semantics.
- Filter logic: branch, path, tag, and activity-type filters are all gate conditions.
- Run evidence: event name, branch, SHA, actor, and ref are critical during triage.
- Security boundaries: `pull_request_target` should be treated as a high-risk trust boundary, not a drop-in replacement for `pull_request`.
- Operational clarity: separate trigger issues from job gating and downstream step failures.

## Do's and Don'ts
### Do
- Confirm the exact event and filters before changing a workflow.
- Inspect the run UI for event, ref, branch, and actor metadata.
- Check both trigger conditions and job-level gating when a workflow exists but a job is skipped.
- Validate branch, tag, and path logic against the actual repository state.

### Don't
- Don't assume a valid YAML file means it will run for the intended event.
- Don't confuse a skipped job with a missing workflow trigger.
- Don't treat `pull_request_target` as safe by default for untrusted contributor code.
- Don't ignore the repository’s default branch or ref semantics.

## Real-life implementation
```yaml
name: CI
on:
  push:
    branches: [main]
    paths:
      - 'src/**'
      - 'tests/**'
  pull_request:
    branches: [main]
    paths:
      - 'src/**'
      - 'tests/**'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm test
```

In this setup, a documentation-only PR does not trigger the workflow because the path filter excludes `docs/**`. If a run exists but the build job is skipped, the next check is the job `if` condition, dependency graph, or concurrency policy rather than the trigger itself.

### Official references
- [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)
- [Workflow syntax: `on` and filters](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)
- [Secure use reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)

## Q&A
### Q: A workflow did not trigger for a PR that only changed docs. What should I inspect first?
A: Inspect the workflow’s `on:` block, path filters, branch filters, and the actual PR ref. A valid workflow can be silently excluded by path or branch configuration.

### Q: A run exists, but the deploy job is skipped. What distinguishes a trigger issue from a job-level issue?
A: If the workflow run exists, the trigger fired. The missing deploy job usually means the job was skipped because of `if`, dependency conditions, or concurrency rules. Check the run timeline and the job-level conditions, not just `on:`.

### Q: Why is `pull_request_target` risky for contributor code?
A: It executes in the base repository context with elevated permissions. If untrusted code is executed there, it can access privileged tokens and repository context in ways that a normal `pull_request` job cannot.

### Q: What is the best troubleshooting sequence when a workflow is expected to run but does not?
A: Verify the exact event, expected ref, branch, path filters, default branch, and repository visibility rules; then compare the expected conditions with the actual run metadata and logs.
