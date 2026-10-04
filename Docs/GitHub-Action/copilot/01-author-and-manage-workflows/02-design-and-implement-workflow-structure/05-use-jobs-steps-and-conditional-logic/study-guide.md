# Objective: Use jobs, steps, and conditional logic.

## What

A workflow should map to an execution graph: build, test, package, deploy. Jobs isolate permissions and failure boundaries; steps handle tasks. Conditional logic decides when a node runs; use it to reflect real business rules instead of hiding missing design decisions.

## Why

- Separate jobs improve clarity and failure isolation.
- Sequential logic is easier to reason about than many nested conditions.
- Conditionals are powerful but risk accidental bypasses if overused.

## How

Organize work as jobs with sequential steps, and put conditions at the narrowest level that expresses the intended policy.

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - run: npm ci
      - run: npm run lint

  deploy:
    needs: lint
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploy"
```

## Features

Jobs define independently scheduled units and permission/failure boundaries; steps run sequentially within a job and share its runner. Conditions determine whether work is eligible to run.

**Official references**

- [Jobs](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobs)
- [Using conditional execution](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idif)
- [Expressions](https://docs.github.com/en/actions/learn-github-actions/expressions)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Keep privileged actions in dedicated jobs.
- Use conditions to stop expensive work early.
- Sequence tasks in a way that protects production and avoids wasted compute.

**Don't**

- Don't confuse step-level and job-level conditions.
- Don't ignore `needs` when expecting a job to wait for upstream validity.
- Don't mix broad shell logic into job conditions instead of making the DAG obvious.

## Real-life implementation

Choose job boundaries around isolation, parallelism, and trust. Conditions should express policy clearly: a deployment condition must not bypass failed required checks or accidentally include untrusted events.

## Q&A

**Q: Which jobs should run for pull requests and which should run only on main?**

**A:** Run validation on eligible PRs; restrict publishing or deployment to trusted branch/event combinations and protected environments.

**Q: What is the execution order for a build, test, and deploy chain?**

**A:** Put build and test in jobs with explicit `needs` dependencies, and make deploy depend on successful prerequisites; independent checks can run in parallel.

**Q: Would a failed lint job still allow a production deploy if the condition is incorrect?**

**A:** It could if the deploy condition overrides normal success behavior or omits the required dependency. Make prerequisites explicit and review uses of `always()` and status functions.
