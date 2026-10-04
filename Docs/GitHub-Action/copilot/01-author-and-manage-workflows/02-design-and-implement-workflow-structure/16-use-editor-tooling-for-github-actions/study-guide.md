# Objective: Use editor tooling, including the GitHub Actions VS Code extension, YAML schema completion, metadata IntelliSense, and validation.

## What

Editor tooling is the first line of defense against workflow mistakes. It catches invalid keys, missing required fields, and obvious schema mismatches before the workflow runs in GitHub.

## Why

- Schema validation catches structural issues early but cannot verify business logic.
- Metadata IntelliSense helps authors create consistent workflows faster.
- Tooling reduces cost and frustration but does not replace a real run in a non-production branch.

## How

Enable GitHub Actions schema and metadata support in the editor, resolve actionable diagnostics, then test runtime behavior separately.

```yaml
name: ci
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
```

## Features

Editor tooling can provide YAML schema validation, completion for workflow keys, action metadata IntelliSense, and navigation. It catches authoring mistakes before a run but cannot prove runtime behavior or policy intent.

**Official references**

- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [GitHub Actions for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-github-actions)
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Use the editor to keep workflow files valid and easier to review.
- Reduce avoidable failed runs and wasted runner time by validating before pushing.
- Treat linting and schema guidance as a fast feedback layer, not a proof of correctness.

**Don't**

- Don't assume parsing success means the workflow is correct.
- Don't ignore schema warnings that indicate invalid keys or missing metadata.
- Don't underestimate the value of metadata IntelliSense in a production environment.

## Real-life implementation

Use validation in the local edit/review loop to reduce avoidable failed runs, then test behavior in a safe branch or environment. Keep schemas and extensions current and review warnings instead of suppressing them blindly.

## Q&A

**Q: Does the editor catch invalid or incomplete workflow syntax before you push?**

**A:** Schema-aware tooling can flag many structural and metadata errors; confirm the selected schema/tooling recognizes GitHub Actions syntax.

**Q: Are you still validating behavior in a test branch, even after the editor confirms valid YAML?**

**A:** Yes. Parsing cannot verify permissions, event payload assumptions, network access, service readiness, or deployment policy.

**Q: Which workflow errors would still remain undetected without a real run?**

**A:** Runtime failures, unavailable secrets, permission denials, incorrect conditions, runner-image differences, and external service issues require execution or targeted tests.
