# Objective: Use workflow commands and environment variables.

## What

Workflow commands and environment variables are the structured I/O of GitHub Actions. They let a shell step communicate with the runner and with later steps in a predictable, machine-readable way.

## Why

- `GITHUB_ENV` is best for values needed later in the job.
- `GITHUB_OUTPUT` is better for step output and job output handoff.
- Workflow commands are helpful for annotations and summaries but should not replace actual structured data exchange.

## How

Write values to the appropriate runner-provided environment file and expose only the variables or outputs that later steps require.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      BUILD_MODE: release
    steps:
      - name: Export value for later steps
        run: echo "artifact_name=app-${GITHUB_SHA::7}" >> "$GITHUB_ENV"
      - name: Add warning
        run: echo "::warning title=Build notice::Using release config"
      - name: Set step output
        id: meta
        run: echo "name=app-${GITHUB_SHA::7}" >> "$GITHUB_OUTPUT"
```

## Features

Workflow commands communicate with the runner through environment files and standard output protocols. `GITHUB_ENV` shares an environment value with later steps in the same job; `GITHUB_OUTPUT` records a step output for explicit mapping.

**Official references**

- [Workflow commands for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions)
- [Environment variables](https://docs.github.com/en/actions/learn-github-actions/variables)
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Use the correct file for the appropriate lifecycle: env for job scope, output for step/job handoff.
- Avoid broad shell exports unless the value is truly relevant for the rest of the job.

**Don't**

- Don't mix env and output semantics incorrectly.
- Don't assume shell variables persist across steps without explicit export.
- Don't treat annotations as ordinary log lines.

- Don't print secrets in logs or environment output.

## Real-life implementation

Choose the narrowest data channel and scope. Environment files reduce unsafe command-string patterns, but their contents remain data that must be validated and protected from untrusted values.

## Q&A

**Q: When should you use `GITHUB_ENV` instead of `GITHUB_OUTPUT`?**

**A:** `GITHUB_ENV` makes a value available as an environment variable to later steps in the same job; `GITHUB_OUTPUT` exposes a named step output that can be mapped and consumed explicitly.

**Q: Which values should be passed forward and which should stay within a single step?**

**A:** Keep transient implementation details local; publish only small values required by later steps or jobs, and use outputs or artifacts for deliberate handoff.

**Q: Is any workflow command or environment variable exposing data that should stay private?**

**A:** Avoid writing secrets to logs, outputs, summaries, or broadly scoped environment variables; pass credentials only to the step that needs them.
