# Consume and troubleshoot workflows

This domain accounts for **15–20%** of GH-200. It tests whether you can read what GitHub Actions actually did, retrieve the evidence, and choose the right way to adopt or manage existing automation.

## Learning path

1. [Interpret workflow behavior and results](./01-interpret-workflow-behavior-and-results/README.md): start with event triggers, run evidence, YAML reuse, and matrix behavior.
2. [Access workflow artifacts and logs](./02-access-workflow-artifacts-and-logs/README.md): locate run evidence in the UI/API, then retrieve and manage artifacts.
3. [Use and manage workflow templates](./03-use-and-manage-workflow-templates/README.md): select and govern the right reuse mechanism, then distinguish disabling from deletion.
4. For each objective, use the self-check without notes. In a test repository, explain the likely evidence, the next diagnostic action, and the operational tradeoff before making a change.

## Objectives

### [Interpret workflow behavior and results](./01-interpret-workflow-behavior-and-results/README.md)

- [Identify workflow triggers and their effects from configuration and logs](./01-interpret-workflow-behavior-and-results/01-identify-triggers-and-effects/study-guide.md)
- [Diagnose failed workflow runs using logs and run history](./01-interpret-workflow-behavior-and-results/02-diagnose-failed-runs/study-guide.md)
- [Expand and interpret YAML anchors, aliases, and merged mappings](./01-interpret-workflow-behavior-and-results/03-expand-yaml-anchors-aliases-and-merged-mappings/study-guide.md)
- [Interpret matrices and selectively rerun jobs](./01-interpret-workflow-behavior-and-results/04-interpret-matrices-and-selective-reruns/study-guide.md)

### [Access workflow artifacts and logs](./02-access-workflow-artifacts-and-logs/README.md)

- [Locate workflows, logs, and artifacts in the UI and through APIs](./02-access-workflow-artifacts-and-logs/01-locate-workflows-logs-and-artifacts/study-guide.md)
- [Download and manage workflow artifacts](./02-access-workflow-artifacts-and-logs/02-download-and-manage-artifacts/study-guide.md)

### [Use and manage workflow templates](./03-use-and-manage-workflow-templates/README.md)

- [Consume organization-level and reusable workflows](./03-use-and-manage-workflow-templates/01-organization-and-reusable-workflows/study-guide.md)
- [Consume non-public organization workflow templates](./03-use-and-manage-workflow-templates/02-non-public-organization-templates/study-guide.md)
- [Use public and private/non-public starter workflows](./03-use-and-manage-workflow-templates/03-public-and-private-starter-workflows/study-guide.md)
- [Distinguish starter workflows, reusable workflows, and composite actions](./03-use-and-manage-workflow-templates/04-distinguish-reuse-mechanisms/study-guide.md)
- [Contrast disabling a workflow with deleting it](./03-use-and-manage-workflow-templates/05-disable-versus-delete/study-guide.md)

## Reference frame

Use the [authoritative GH-200 syllabus](../../copilot-github-syllabus.md) as the objective boundary. GitHub behavior and API details can evolve; use the official references in each guide to verify current syntax and permissions.
