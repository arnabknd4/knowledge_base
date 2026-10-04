# Implement workflow commands within actions

## What

Use GitHub Actions runner commands to emit logs, warnings, annotations, debug details, and structured outputs from within an action.

Actions interact with the runner through special command syntax and environment files. These commands are part of the runtime contract that allows workflows to receive structured status and values.

## Why

Raw shell output alone is not enough for reliable automation. The runner recognizes specific command formats, which are used by GitHub to expose warnings, errors, logs, and step outputs cleanly.

Correct command usage improves observability, reduces operator confusion, and prevents secret leakage.

## How

Common commands include:

- `::warning::` and `::error::` for actionable operator notices.
- `::debug::` for verbose diagnostics.
- `::add-mask::` before printing a secret value.
- `::group::` / `::endgroup::` to organize logs.
- `GITHUB_ENV`, `GITHUB_OUTPUT`, and `GITHUB_PATH` for environment and output persistence.

Use the environment files instead of ad hoc parsing when you want a step output or expanded environment value to survive into subsequent workflow steps.

## Features

- Structured signals for warnings, errors, and debug output.
- Safer handling of secrets and sensitive values.
- Better log structure and workflow integration.
- Direct support for outputs and environment variables.

## Do's and Don'ts

Do:
- Mask secrets before logging them.
- Write outputs to `GITHUB_OUTPUT` and environment values to `GITHUB_ENV`.
- Keep command messages actionable and concise.

Don't:
- Print raw secrets or tokens during debugging.
- Treat log formatting as a replacement for an explicit output file.
- Emit vague warnings without remediation guidance.

## Real-life implementation

A Bash action validates a token before performing a release step. It checks whether `INPUT_TOKEN` is set, prints `::error::` if missing, masks the value with `::add-mask::`, and writes a result to `$GITHUB_OUTPUT` so the next step can consume it.

This pattern keeps the workflow understandable and avoids leaking credentials in logs.

## Q&A

Q: Which command is best for a failing step?
A: `::error::` is the correct mechanism when the step cannot proceed safely and the action should stop with a clear operator message.

Q: Why use `GITHUB_OUTPUT` instead of echoing a value to a log?
A: Because workflow steps consume structured outputs from environment files, while log lines are primarily for operators.

Q: What is the value of `::add-mask::`?
A: It prevents sensitive values from being exposed in the workflow log even when they appear in command output.

Q: How do `GITHUB_ENV` and `GITHUB_OUTPUT` differ?
A: `GITHUB_ENV` sets environment variables for subsequent steps, while `GITHUB_OUTPUT` exposes step outputs for downstream consumers.

## Official references

- [GH-200 syllabus](../../../../copilot-github-syllabus.md)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [Creating a JavaScript action](https://docs.github.com/en/actions/creating-actions/creating-a-javascript-action)
- [Creating a Docker container action](https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action)
- [Creating a composite action](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action)
- [Metadata syntax for GitHub Actions](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions)
- [Workflow commands for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions)
- [Versioning actions](https://docs.github.com/en/actions/creating-actions/about-custom-actions#using-release-management-for-actions)
- [About GitHub Marketplace for actions](https://docs.github.com/en/actions/creating-actions/publishing-actions-in-github-marketplace)
