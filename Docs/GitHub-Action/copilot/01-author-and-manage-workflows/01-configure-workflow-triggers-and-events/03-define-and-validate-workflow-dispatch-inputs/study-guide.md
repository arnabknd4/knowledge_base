# Objective: Define and validate `workflow_dispatch` inputs (types, required values, and defaults).

## What

Manual triggers are an operational API. The workflow input contract is the interface that defines valid behavior. Good inputs are clear, typed, and limited to values the system can safely process.

## Why

- `choice` inputs keep the interface narrow and easier to validate.
- `string` inputs are flexible but require validation in the workflow logic.
- Defaults improve usability but should not hide dangerous production decisions.

## How

Declare inputs under `workflow_dispatch` with an intentional type, required setting, default, and allowed choices; validate values before consequential actions.

```yaml
name: deploy
on:
  workflow_dispatch:
    inputs:
      environment:
        description: Target environment
        required: true
        type: choice
        options: [staging, production]
      release_version:
        description: Version to deploy
        required: false
        default: latest
        type: string
      dry_run:
        description: Validate without changing resources
        required: false
        default: true
        type: boolean
```

## Features

Manual inputs form an operator-facing API. Declare types, required fields, defaults, and allowed values so the workflow receives an intentional request rather than an unchecked string.

**Official references**

- [Manual events for GitHub Actions](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch)
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Validate environment values before executing destructive actions.
- Keep the input surface small so operators cannot accidentally request impossible combinations.
- Document the intent of each input to reduce operator confusion.

**Don't**

- Don't overlook that booleans and strings may require conversion in shell scripts.
- Don't assume defaults are sufficient validation.
- Don't use manual inputs for tasks that should be event-driven or schedule-driven instead.

## Real-life implementation

Keep inputs constrained and validate them before side effects. A default improves usability but is not authorization or validation; sensitive targets still need permissions and environment protection.

## Q&A

**Q: Which input type would you choose for `environment` and why?**

**A:** Use the `environment` input type when operators should select a configured GitHub environment; use `choice` for a fixed non-environment set and validate any free-form input.

**Q: Which values should be required and which ones should default?**

**A:** Require values necessary to identify the operation or target; default only safe, predictable values that do not silently select a higher-risk action.

**Q: Is there any input that could trigger a security-sensitive action without clear validation?**

**A:** Validate the selected target against an allowlist and route deployments through environment protection; never let arbitrary input directly become a shell command.
