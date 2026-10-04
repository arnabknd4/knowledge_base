# Objective: Use `strategy` and `matrix` to generate job variations; apply `include`/`exclude`, control `fail-fast` and `max-parallel`, and optimize matrix size for cost and performance.

## What

A matrix is a way to express breadth in a controlled way. It should answer a business risk question: what combinations matter enough to verify? The matrix must be intentionally sized to cover risk without exploding cost.

## Why

- More dimensions yield more coverage but increase runner costs and run durations.
- `include` and `exclude` help control edge cases without exponential growth.
- `fail-fast: false` improves visibility but can waste broad compute if many jobs are failing at once.

## How

Define only supported matrix dimensions and use `include`, `exclude`, `fail-fast`, and `max-parallel` to shape coverage and resource use.

```yaml
strategy:
  fail-fast: false
  max-parallel: 4
  matrix:
    os: [ubuntu-latest, windows-latest]
    node-version: [18, 20]
    include:
      - os: ubuntu-latest
        node-version: 22
        experimental: true
    exclude:
      - os: windows-latest
        node-version: 18
```

## Features

A matrix expands one job definition across selected combinations. Axes, `include`, and `exclude` define coverage; `fail-fast` and `max-parallel` control failure response and concurrency.

**Official references**

- [Using a matrix for your jobs](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs)
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Keep matrix dimensions aligned with actual compatibility risk.
- Use `max-parallel` in shared enterprises to avoid runaway compute.
- Document the purpose of each axis so future maintainers do not add redundant combinations.

**Don't**

- Don't assume a matrix is automatically the minimal set of needed tests.
- Don't overlook that `include` and `exclude` change the actual variant set.
- Don't ignore runner cost when a matrix expands in multiple dimensions.

## Real-life implementation

Use only dimensions that represent supported platforms or meaningful compatibility risk. Estimate total combinations and hosted/self-hosted capacity before widening a matrix.

## Q&A

**Q: Which matrix axis adds real compatibility value?**

**A:** Keep an axis only when it represents a supported runtime, platform, or configuration whose failure matters to users.

**Q: What is the cost impact of a 2x2x3 matrix on a repo with many PRs?**

**A:** It creates 12 job combinations per run before any `include` expansion, multiplying runner demand across frequent PRs; cap parallelism and consider a smaller risk-based set.

**Q: Would the current matrix detect a real compatibility break without testing meaningless combinations?**

**A:** Check that the selected combinations cover supported boundaries and that `include`/`exclude` modify the intended set; document why each axis exists.
