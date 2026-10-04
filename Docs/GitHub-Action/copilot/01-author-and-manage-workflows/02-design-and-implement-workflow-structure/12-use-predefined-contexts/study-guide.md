# Objective: Use predefined contexts (`github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `strategy`, `job`, `steps`, `github.event`, and `github.ref`) to access workflow, repository, and runtime metadata.

## What

Contexts are the runtime metadata API of GitHub Actions. They provide branch, event, runner, secret, input, matrix, and dependency details. A workflow without context is static; a workflow with the right context can adapt to the environment and execution state.

## Why

- Context-based expression logic is powerful but can become harder to reason about when overused.
- `github.event` is valuable for release and webhook logic but must be treated as untrusted input.
- `vars` are ideal for non-secret config; `secrets` are for secret values only.

## How

Reference a context only where it is available and appropriate; pass values through explicit fields rather than assuming every context is global.

```yaml
jobs:
  build:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - run: echo "Branch: ${{ github.ref }}"
      - run: echo "Runner: ${{ runner.os }}"
      - run: echo "Secret check: ${{ secrets.GITHUB_TOKEN != '' }}"
```

## Features

Contexts expose data at different points in workflow evaluation: `github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `strategy`, `job`, and `steps` each have distinct availability and scope.

**Official references**

- [Contexts](https://docs.github.com/en/actions/learn-github-actions/contexts)
- [Expressions](https://docs.github.com/en/actions/learn-github-actions/expressions)
- [Variables](https://docs.github.com/en/actions/learn-github-actions/variables)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Validate event payload data before using it in anything sensitive.
- Keep expressions readable and not over-nested.
- Use environment variables to prevent magic strings repeated across the workflow.

**Don't**

- Don't assume every context is available everywhere.
- Don't confuse `vars` and `env`.
- Don't treat event payload data as inherently safe because it came from GitHub.

## Real-life implementation

Use the context whose source and timing match the requirement. Treat event payload fields as untrusted when they originate from users, and keep secrets out of contexts rendered to logs or summaries.

## Q&A

**Q: Which context gives the branch name and which gives the current runner OS?**

**A:** `github.ref` identifies the ref for the event; `runner.os` identifies the runner operating system.

**Q: Would you use `vars` or `secrets` for a deploy environment name?**

**A:** Use `vars` for non-sensitive configuration such as a target name; reserve `secrets` for credentials or other sensitive values.

**Q: Is any expression depending on untrusted event or payload data without validation?**

**A:** Validate or allowlist user-controlled fields before using them in shell commands, deployment targets, or privileged decisions.
