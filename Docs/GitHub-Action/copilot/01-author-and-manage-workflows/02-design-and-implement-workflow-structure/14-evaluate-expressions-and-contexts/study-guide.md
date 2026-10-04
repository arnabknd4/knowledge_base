# Objective: Evaluate expressions with `${{ }}` and contexts; distinguish static (workflow-parse) and runtime evaluation.

## What

Expressions turn static YAML into dynamic workflow behavior. They are not just convenience logic; they are the mechanism for branching on metadata, conditions, and state. A strong design understands which parts are evaluated when.

## Why

- Simpler expressions are easier to audit.
- Complex expressions can hide logic and reduce maintainability.
- Runtime evaluation is necessary for event-driven decisions, but it must be understood and validated.

## How

Use expressions in supported fields, account for context availability at evaluation time, and keep untrusted values separate from shell syntax.

```yaml
env:
  BUILD_MODE: ${{ github.ref == 'refs/heads/main' && 'release' || 'dev' }}

jobs:
  deploy:
    if: ${{ github.event_name == 'push' && github.ref == 'refs/heads/main' }}
    runs-on: ubuntu-latest
```

## Features

Expressions use `${{ }}` to evaluate contexts and functions where the workflow syntax permits them. Available values depend on the key and evaluation phase; shell expansion is a separate mechanism.

**Official references**

- [Expressions](https://docs.github.com/en/actions/learn-github-actions/expressions)
- [Contexts](https://docs.github.com/en/actions/learn-github-actions/contexts)
- [Workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Avoid over-nesting expressions when named variables or a dedicated condition would be clearer.
- Validate untrusted data before using it in decisions or commands.
- Keep decision logic explicit so failures are obvious during review.

**Don't**

- Don't confuse parse-time and run-time evaluation.
- Don't ignore context availability and scope differences.
- Don't write expressions so dense that a reviewer cannot tell what they actually do.

## Real-life implementation

Keep expressions simple and understand where they are evaluated. Quote and validate untrusted values when passing them to scripts; expression interpolation into shell can create injection risk.

## Q&A

**Q: Which values are known at parse time and which are only known when the run starts?**

**A:** Workflow structure and literal configuration are available before execution; event, job, step, and runtime contexts become available only in the supported evaluation locations and phases.

**Q: What would happen if the branch or event payload changed unexpectedly during a run?**

**A:** A run is associated with its triggering event/ref, but event fields may be user-controlled; do not use them as trusted authorization or interpolate them unsafely.

**Q: Are your expressions readable to the next engineer without deep GitHub Actions expertise?**

**A:** Prefer named intermediate outputs and simple conditions over nested expressions, and document non-obvious policy decisions.
