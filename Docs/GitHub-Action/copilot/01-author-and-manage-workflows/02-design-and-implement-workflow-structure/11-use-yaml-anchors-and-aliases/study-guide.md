# Objective: Use YAML anchors and aliases (`&`, `*`, and merge `<<`) to reuse mappings or steps within a workflow file.

## What

Anchors and aliases are YAML-level reuse mechanics. They reduce duplication for common step definitions and environment defaults, but they do not replace architecture-level abstraction such as reusable workflows or composite actions.

## Why

- Reuse reduces duplication and helps keep YAML consistent.
- Too much aliasing can hide the actual behavior of a workflow.
- YAML merges are convenient, but large nested anchor graphs reduce readability.

## How

Define a nearby anchor for genuinely repeated YAML nodes and alias it only where the expanded workflow remains clear.

```yaml
x-node-setup: &node-setup
  uses: actions/setup-node@v4
  with:
    node-version: 20

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - <<: *node-setup
      - run: npm run lint
```

## Features

YAML anchors (`&`) and aliases (`*`) reuse nodes within a YAML document; merge keys can share mapping values where supported. They reduce repetition but do not create workflow-level abstractions.

**Official references**

- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [YAML anchors and aliases](https://yaml.org/spec/1.2.2/#322-anchors-and-aliases)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Keep anchor logic limited and discoverable.
- Make the source of shared settings obvious during review.
- Use anchors to standardize repeated configuration without hiding crucial differences between jobs.

**Don't**

- Don't treat anchors as a GitHub Actions feature rather than YAML syntax.
- Don't overuse anchors until the workflow becomes harder to debug than a slightly duplicated version.
- Don't overlook that merge keys are expanded before workflow execution.

## Real-life implementation

Use anchors for small, stable repeated fragments when the expanded workflow remains understandable. For cross-file policy or complex repeated workflow logic, a reusable workflow or composite action is usually clearer.

## Q&A

**Q: Does the workflow remain readable when the anchor is expanded?**

**A:** Review the resulting effective mapping mentally or with editor tooling; avoid deeply nested or distant aliases that hide important behavior.

**Q: Are shared values truly shared across jobs, or should they be handled by a reusable workflow?**

**A:** Use anchors for local YAML reuse; use a reusable workflow when the shared unit needs its own interface, job boundaries, permissions, or cross-file reuse.

**Q: Would a reviewer understand where the default step came from without advanced YAML knowledge?**

**A:** Keep the anchor close to its use, give it an explanatory name, and prefer explicit steps when reuse obscures security or execution details.
