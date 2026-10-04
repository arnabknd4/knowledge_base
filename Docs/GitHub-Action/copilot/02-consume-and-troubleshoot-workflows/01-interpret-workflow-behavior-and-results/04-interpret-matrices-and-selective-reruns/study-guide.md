# Interpret matrices and selectively rerun jobs

## What
A matrix fan-out creates multiple job runs from one workflow job definition. Each combination of matrix values is a distinct job instance with its own name, logs, and result. Selective reruns work on that same granularity: you choose the matrix leg or job to re-execute, not the whole workflow definition.

## Why
Matrix workflows are an efficient way to test many OS/runtime combinations, but they can hide the real failure pattern if you look only at the aggregate workflow status. The right way to diagnose them is to map each failing job to the exact axis values it represented.

## How
1. Write down each matrix axis and its values, then apply `include`, `exclude`, and dynamic matrix generation.
2. Match the displayed job name and logs to the axis tuple for each variant.
3. Review `fail-fast`, `max-parallel`, and `continue-on-error` to understand why some combinations did not run or why a failure was not treated as a full workflow failure.
4. Compare passing and failing variants around OS, runtime version, dependency resolution, runner image, and shell differences.
5. When a fix is ready, use the rerun option for the affected matrix leg or failed job, but confirm the correct commit and selected subset before triggering it.

## Features
- Cartesian expansion: combinations are generated from matrix axes and filtered by `include`/`exclude` rules.
- Job identity: each matrix leg has its own name, logs, and result.
- Failure control: `fail-fast` and `continue-on-error` alter how a matrix behaves under failure.
- Selective reruns: reduce turnaround time when the fix is scoped to a specific variant.
- Runtime evidence: logs and environment details explain why a single OS or runtime failed.

## Do's and Don'ts
### Do
- List the matrix dimensions before debugging the failure.
- Check the exact subset of variants that ran versus the intended cartesian product.
- Rerun only the affected matrix leg when the diagnosis is specific and the change is narrow.

### Don't
- Don't treat “matrix failed” as a single monolithic issue without mapping it back to an OS or runtime tuple.
- Don't confuse `fail-fast` cancellation with a clean pass or an independent bug on every cancelled variant.
- Don't assume a selective rerun is equivalent to a full workflow replay.

## Real-life implementation
```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [18, 20]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
      - run: npm test
```

If only Windows + Node 20 fails, the investigation should focus on the runner OS, shell differences, node version, and any path or install step that differs from the passing variants.

### Official references
- [Running variations of jobs in a workflow](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs)
- [Rerunning workflows and jobs](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/re-running-workflows-and-jobs)
- [Workflow syntax: matrix, fail-fast, and max-parallel](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)

## Q&A
### Q: Only Windows/Node-current fails while Linux variants pass. What should you inspect first?
A: Inspect the matrix dimensions and compare environment-specific steps, shell behavior, path handling, dependency install commands, and runner differences.

### Q: Why can a matrix have fewer executed jobs than its cartesian product?
A: Because `exclude`, `include`, `fail-fast`, cancellation, job conditions, or dynamic matrix generation can remove or cancel specific combinations.

### Q: When is rerunning only a failed matrix leg insufficient?
A: When the change could affect the entire matrix, or when the failure pattern suggests a shared dependency or a component used by all variants, not just one OS/runtime combination.

### Q: What is the value of `fail-fast` in a matrix job?
A: It stops queued matrix jobs after the first failure to cut wasted compute, but it can also hide evidence from the remaining variants unless you intentionally disable it for more complete diagnostics.
