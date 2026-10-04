# Troubleshoot action execution and errors

## What

Diagnose why an action fails by checking the action reference, metadata, runner environment, input mapping, and emitted logs.

Most action failures are not random. They come from a specific layer: the step cannot resolve, the metadata is invalid, the runtime cannot start, or the script exits with a non-zero status.

## Why

Good troubleshooting reduces time-to-fix and prevents incorrect assumptions about workflow behavior. Many action problems are caused by mismatched assumptions, not by broken GitHub syntax alone.

The log is the evidence trail. It tells you which command failed, which value was missing, and whether the runner environment matched the action's expectations.

## How

Use a layered checklist:

1. Verify the `uses:` reference and repository access.
2. Check `action.yml` metadata such as `runs.using`, `runs.main`, `runs.image`, and `runs.steps`.
3. Inspect output and error messages from shell scripts or the runner.
4. Validate inputs, outputs, permissions, working directory, and environment variables.
5. Reproduce in a minimal workflow to isolate runner or dependency issues.

If a failure only happens in CI and not locally, suspect shell differences, missing tooling, permission mismatches, or hidden environment values.

## Features

- Clear triage path from reference to root cause.
- Structured resilience against runner and metadata issues.
- Better signal quality through step-by-step validation.
- Easier reproduction in minimal pipelines.

## Do's and Don'ts

Do:
- Check the action metadata when the step fails before startup.
- Read the failing command and its exit code before changing the workflow.
- Keep debug output focused and avoid exposing secrets.

Don't:
- Ignore permission differences between local runs and GitHub-hosted runners.
- Assume a tool installed on one runner is present on another.
- Rely on a vague top-level error without checking the actual failing command.

## Real-life implementation

A composite action calls `jq` to parse JSON output, but the runner image does not include it. The action fails with a shell error because the dependency is not declared or installed. The remedy is to either add a setup step or move the logic into a Docker or JavaScript action where the runtime dependency is explicit.

The root cause is missing runtime support, not a workflow problem in the abstract.

## Q&A

Q: Where should you start when a `uses:` step fails before the action even begins?
A: Check the action reference, repository access, and `action.yml` metadata before debugging the script itself.

Q: What is the difference between a workflow-level failure and a runner-environment issue?
A: A workflow-level failure may be caused by invalid `uses:` or input mapping, while a runner issue is often a missing tool, incorrect shell, or missing permission.

Q: How can you debug without leaking secrets?
A: Mask sensitive values, avoid printing raw tokens, and focus on the failing command and surrounding environment values.

Q: Why is reproducing in a minimal workflow valuable?
A: It isolates the actual failure boundary and prevents guessing across unrelated workflow layers.

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
