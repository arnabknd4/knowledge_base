# Disable versus delete a workflow

## What
Disabling and deleting a workflow are different states with different operational consequences. Disabling pauses the workflow in GitHub without removing the file; deleting removes the workflow definition from the repository, which affects future triggers and repository state.

## Why
An incident can require a temporary pause, a safe retirement, or a permanent removal. Choosing the wrong action can leave automation running unexpectedly or break required checks and release processes.

## How
1. Decide whether the goal is temporary pause or permanent removal.
2. For a temporary pause, disable the workflow in the Actions UI or through the supported API/CLI path.
3. For retirement, review any required checks, branch protections, schedules, and release requirements before removing the file.
4. Delete the workflow only after change control and after confirming the repository no longer depends on it.
5. Remember: neither action cancels already running workflow runs automatically.

## Features
- Disable: reversible pause; the definition remains in the repo.
- Delete: permanent removal of the workflow file from the branch; future triggers stop.
- Evidence preservation: historical runs and artifacts are not retroactively removed by deleting the workflow definition.
- Operational safety: a disabled workflow can be re-enabled; a deleted workflow must be recreated from version control.

## Do's and Don'ts
### Do
- Disable a risky workflow for a temporary containment action.
- Review required checks and release automation before deleting a workflow.
- Document the incident and re-enable plan if the workflow is only paused.

### Don't
- Don't confuse disabling with deleting.
- Don't assume deleting the workflow file erases prior run history or artifacts.
- Don't forget to handle active runs separately from the workflow definition state.

## Real-life implementation
```yaml
# Workflow file remains in the repo
name: release
on:
  workflow_dispatch:
```

If a release automation is generating unexpected deployments, disable the workflow first to stop future runs while the incident is investigated. If the workflow is retired, review branch protection, required checks, and deployment automation before deleting the file permanently.

### Official references
- [Disabling and enabling a workflow](https://docs.github.com/en/actions/using-workflows/disabling-and-enabling-a-workflow)
- [REST API: workflows](https://docs.github.com/en/rest/actions/workflows)
- [Deleting a workflow run](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/deleting-a-workflow-run)

## Q&A
### Q: A reversible pause is needed while investigating unexpected deployments. Which action is appropriate?
A: Disable the workflow. Confirm whether there are active runs, branch protection rules, and any exposed secrets or credentials that must also be addressed.

### Q: Does deleting the workflow file erase old run history?
A: No. Old run history and artifacts remain in the repository’s log and artifact records, even if the workflow file is deleted.

### Q: What do you need to check before permanently removing a workflow that is a required status check?
A: Check branch protection rules, required checks, deployment gates, and any repository automation that still expects the workflow status to exist.

### Q: Why is disabling a compromised workflow not always enough on its own?
A: Because active runs may still be in progress, and the underlying secret or token exposure may still need remediation. Disabling stops future runs; it does not automatically revoke access or undo a security incident.
