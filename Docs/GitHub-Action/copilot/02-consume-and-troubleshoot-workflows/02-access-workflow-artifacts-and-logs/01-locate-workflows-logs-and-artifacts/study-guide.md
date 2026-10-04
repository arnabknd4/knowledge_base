# Locate workflows, logs, and artifacts in the UI and through APIs

## What
Workflow files, run history, job logs, and artifacts are related but distinct pieces of evidence. A workflow file defines the automation; a workflow run captures execution; job logs show the step-by-step runtime output; artifacts are persisted files attached to a run for later inspection or transfer.

## Why
When a run fails or a deployment needs traceability, you need to move from the workflow definition to the exact execution record and then to its outputs. Without the right identifiers and traversal path, you may look at the wrong workflow or fetch a run that lacks the necessary artifact or log evidence.

## How
1. Open the repository’s Actions tab, select the workflow, and filter the run list by event, branch, or date.
2. Open the specific run to view jobs, job IDs, statuses, and metadata such as commit SHA, actor, and branch.
3. Open the failing job and step logs to diagnose errors, then use the full log stream when deeper evidence is required.
4. Inspect the run summary for artifacts and use the artifact ID to download or delete if authorized.
5. Use the GitHub CLI or REST APIs for repeatable access: `gh run list`, `gh run view`, `gh api /repos/{owner}/{repo}/actions/runs/{run_id}/jobs`, and the artifacts endpoints.

## Features
- UI navigation: quickly move from workflow history to run details to logs.
- API and CLI sequence: run ID, job ID, and artifact ID are the keys to deeper automation.
- Artifact lookup: artifacts are run-scoped, retention-controlled, and may expire or require different permissions.
- Evidence handling: logs and artifacts can contain sensitive data and must be treated accordingly.

## Do's and Don'ts
### Do
- Start with the run or workflow file that matches the commit and branch you are diagnosing.
- Use run IDs and artifact IDs to retrieve the exact evidence needed.
- Use least-privilege tokens and record the IDs you accessed.

### Don't
- Don't confuse the workflow definition with the workflow execution record.
- Don't assume a run has artifacts just because it has logs.
- Don't store signed artifact URLs or log URLs as if they were permanent references.

## Real-life implementation
```bash
gh run list --limit 20
gh run view 123456789 --log-failed
gh run download 123456789 --name build-artifact
```

These commands show the practical path from run discovery to log examination to artifact retrieval. The same flow is available through REST endpoints when scripting incident response or auditing repository automation.

### Official references
- [Viewing workflow run history](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/viewing-workflow-run-history)
- [REST API: workflow runs](https://docs.github.com/en/rest/actions/workflow-runs)
- [REST API: workflow jobs](https://docs.github.com/en/rest/actions/workflow-jobs)
- [REST API: workflow run logs](https://docs.github.com/en/rest/actions/workflow-runs#download-workflow-run-logs)
- [REST API: artifacts](https://docs.github.com/en/rest/actions/artifacts)
- [GitHub CLI: `gh run`](https://cli.github.com/manual/gh_run)

## Q&A
### Q: You know the workflow file but not the failing job. What is the normal discovery sequence?
A: Start with the workflow’s run history, select the failing run, then inspect its jobs and logs. The run provides the job list; the job provides the step log evidence.

### Q: What identifiers are required to retrieve an artifact through the API?
A: Usually the repository owner/repo, the run ID, and the artifact ID. Some endpoints also require the artifact name or a specific API route for the artifact lifecycle.

### Q: Why should a signed artifact download URL not be treated as a long-lived bookmark?
A: Download URLs can be short-lived and may expire. Use the concrete run or artifact API to request fresh evidence when needed.

### Q: Which is faster for exploratory diagnosis: UI or CLI/API?
A: The UI is quickest for interactive read-through and context. CLI/API are better for repeatability, bulk retrieval, and automation.
