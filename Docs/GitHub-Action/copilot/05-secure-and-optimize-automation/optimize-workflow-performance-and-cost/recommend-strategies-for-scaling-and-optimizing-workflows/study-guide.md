# GH-200 study guide: recommend strategies for scaling and optimizing workflows

## What

Workflow optimization balances time-to-feedback, test coverage, reliability, and runner cost. Scaling means structuring the job graph, matrix, triggers, reuse, concurrency, and caching around actual requirements—not maximizing parallelism or minimizing runtime at any cost.

Objective link: [GH-200 syllabus — optimize workflow performance and cost](../../../../copilot-github-syllabus.md#optimize-workflow-performance-and-cost).

## Why

Excessive matrices and redundant triggers consume runner minutes, increase queue pressure, and produce noisy failures. Too little coverage can miss platform defects; aggressive cancellation or skipped jobs can compromise required checks and releases. The practical aim is to reduce unnecessary work without weakening important quality and security gates.

## How

- Profile queue time and job duration; optimize the critical path and remove repeated setup or work that does not add coverage.
- Use matrices only for needed OS/runtime/version combinations. Apply `max-parallel` to control capacity and `fail-fast` according to whether early cancellation helps.
- Run fast, high-signal checks on each change and place broader or expensive tests on an appropriate schedule or release path.
- Use path filters and job conditions carefully so required checks are not unexpectedly skipped.
- Use reusable workflows for consistent shared orchestration, and pin/review external reusable workflows.
- Apply `concurrency` to cancel superseded CI runs or serialize deployments only when the behavior matches the workload.
- Measure cost as runner usage and operational impact, not just wall-clock duration; review cache hit rate and artifact retention too.

```yaml
jobs:
  test:
    strategy:
      fail-fast: false
      max-parallel: 4
      matrix:
        os: [ubuntu-latest, windows-latest]
        node: [18, 20]
```

This four-variant matrix is an example, not a universal recommendation; select supported OS/runtime combinations based on product coverage and runner capacity.

## Features

- **Matrix strategy:** generates job variants; `max-parallel` limits concurrent jobs and `fail-fast` controls cancellation after a matrix failure.
- **Concurrency groups:** prevent overlapping runs or deployments within a selected group; cancellation semantics should fit the task.
- **Reusable workflows:** reduce duplicated orchestration while centralizing maintenance and policy.
- **Selective execution and caching:** avoid unnecessary jobs and repeated setup, while retaining required checks and validating cached data.
- **Runner and cost controls:** workflow scope, matrix size, job duration, and artifact retention all influence usage and spend.

## Do's and Don'ts

**Do**
- Base optimization on run data and retain the tests needed for supported environments.
- Bound matrix size and parallelism according to queue capacity, rate limits, and spend.
- Separate verification from release/deployment and protect the latter with trusted refs and least privilege.
- Use cancellation for superseded work only when it will not interrupt required release or cleanup operations.

**Don't**
- Assume more parallel jobs always mean lower cost or faster completion; queueing and contention can offset gains.
- Remove checks solely to reduce minutes or use filters that cause required checks to disappear.
- Serialize unrelated work in one concurrency group or cancel deployment runs without understanding release semantics.
- Treat reusable workflows, caching, or matrix expansion as security boundaries by themselves.

## Real-life implementation

A team keeps lint and unit tests on each pull request, runs a measured OS/runtime matrix for supported configurations, and schedules a broader compatibility suite nightly. The matrix's `max-parallel` is capped to control runner usage, while superseded PR runs are cancelled by a scoped concurrency group. Deployment jobs use a separate group and are not cancelled until the team verifies that cancellation is safe. Monthly review compares queue times, duration, and runner spend before changing coverage.

## Q&A

**Q: What does `max-parallel` optimize?**

A: It caps simultaneous matrix jobs, helping manage runner capacity and cost at the possible expense of total elapsed time.

**Q: When should `fail-fast` be disabled?**

A: When results from all variants are useful for diagnosis or when early cancellation would hide meaningful failures; choose based on feedback needs.

**Q: Does concurrency guarantee jobs run in a particular order?**

A: No. It groups runs and controls overlap/cancellation behavior; it is not a general FIFO deployment queue.

**Q: Is a nightly broad matrix a replacement for pull-request checks?**

A: No. Keep timely, required checks on changes and use scheduled coverage to supplement them.

### References

- [Workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Using a matrix for your jobs](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs)
- [Using concurrency](https://docs.github.com/en/actions/using-jobs/using-concurrency)
- [Caching dependencies](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows)
