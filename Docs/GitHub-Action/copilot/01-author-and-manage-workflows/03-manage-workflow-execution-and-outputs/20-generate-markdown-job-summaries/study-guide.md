# Objective: Generate Markdown job summaries with `GITHUB_STEP_SUMMARY`.

## What

A job summary is a concise, human-readable report created at runtime. It captures the key facts of a run in a format that is easy for a reviewer to scan without exploring the full logs.

## Why

- Summaries improve readability and release traceability.
- They should remain concise; otherwise they duplicate logs instead of clarifying them.
- Good summaries make approvals and incident reviews faster.

## How

Append concise, sanitized Markdown to `GITHUB_STEP_SUMMARY` so the run gives operators a useful result without exposing sensitive data.

```yaml
steps:
  - name: Write summary
    run: |
      echo "## Build results" >> "$GITHUB_STEP_SUMMARY"
      echo "- Commit: ${{ github.sha }}" >> "$GITHUB_STEP_SUMMARY"
      echo "- Status: successful" >> "$GITHUB_STEP_SUMMARY"
```

## Features

`GITHUB_STEP_SUMMARY` lets a step append Markdown to the workflow run summary. Summaries are an operator-facing report assembled during the run, separate from logs, outputs, and approval controls.

**Official references**

- [Workflow commands for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions)
- [Defining outputs for jobs](https://docs.github.com/en/actions/using-jobs/defining-outputs-for-jobs)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Use summaries for operational highlights, not exhaustive dumps.
- Keep them deterministic so reviewers can trust the state they represent.

**Don't**

- Don't write raw secrets into the summary by mistake.
- Don't expect the summary to replace formal approvals or checks.
- Don't overload the markdown with log output rather than business/release context.

- Don't include secrets or untrusted values in markdown summaries.

## Real-life implementation

Publish concise, actionable status and links to relevant artifacts or deployment targets. Sanitize untrusted text and exclude secrets because summaries are visible to users with run access.

## Q&A

**Q: Would a reviewer understand this run's purpose and result from the summary alone?**

**A:** Include the operation, outcome, relevant version or target, and useful links without duplicating all logs.

**Q: Is the summary free of sensitive values or secret material?**

**A:** Render only reviewed fields; never print secrets or raw untrusted payloads, and escape or sanitize user-controlled Markdown.

**Q: Is the summary concise enough to be useful during an approval or incident review?**

**A:** Keep the report focused on decision-relevant facts, failures, and evidence links; retain detailed diagnostics in logs or artifacts.
