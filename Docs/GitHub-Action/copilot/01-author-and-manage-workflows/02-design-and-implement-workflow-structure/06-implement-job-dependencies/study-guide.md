# Objective: Implement dependencies between jobs.

## What

`needs` creates a dependency graph. It should represent real business and technical dependencies so the workflow fails early and only runs what is necessary.

## Why

- Dependencies create rigor but may increase cycle time.
- Parallelization speeds feedback but adds cost and operational complexity.
- A clear dependency map is easier to debug than a single long-running job.

## How

Use `needs` to encode real prerequisites; this makes ordering and failure propagation part of the visible job graph.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
  test:
    needs: build
    runs-on: ubuntu-latest
  deploy:
    needs: [build, test]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
```

## Features

`needs` forms the job dependency graph. Jobs without dependencies may run concurrently; a dependent job normally waits for its direct prerequisites and is skipped when a prerequisite fails or is skipped unless its condition changes that behavior.

**Official references**

- [Defining needs between jobs](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idneeds)
- [Jobs](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobs)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Gate deploys behind upstream success to ensure artifacts are valid.
- Make job dependency design explicit so downstream jobs do not start with stale or incomplete state.
- Balance parallelism with runner budget and time-to-feedback.

**Don't**

- Don't assume `needs` is optional for deploy logic.
- Don't overlook that jobs can still run in parallel when they do not depend on each other.
- Don't reuse stale artifacts without a dependency graph that ensures freshness.

## Real-life implementation

Model only true dependencies. A clear graph exposes critical path, parallel opportunities, and failure propagation, while unnecessary edges increase latency and overly broad conditions can weaken gates.

## Q&A

**Q: Does `deploy` really need the results of both build and test?**

**A:** If deployment requires both successful outputs, list both jobs in `needs`; otherwise depend only on the jobs that are genuine prerequisites.

**Q: What happens when `test` fails but `build` succeeds?**

**A:** A job needing both is normally skipped after the failed prerequisite. A custom condition can alter this, so use status functions intentionally and never bypass required deployment checks.

**Q: Which jobs should run concurrently and which should wait for earlier stages?**

**A:** Run independent linting, tests, or platform builds concurrently; serialize packaging or deployment only after required validation and approvals.
