# Configure and interpret reports and alerts for backups

## What

Azure Backup provides monitoring, alerting, and reporting for protection health, jobs, policy compliance, and recovery activity. Built-in alerts and Azure Monitor alerts notify operators of failures or significant events; Backup Reports use diagnostic data routed to a Log Analytics workspace and curated workbooks.

## Why

Backup that silently fails is not recoverability. Operational visibility helps identify missed jobs, unhealthy protected items, configuration drift, and suspicious deletion or policy changes before an incident. Reports support fleet-wide governance and capacity/cost review.

## How

Configure the vault's diagnostic settings to send supported backup data to Log Analytics, enable Backup Reports/workbooks, and choose relevant alert rules and action groups. Define ownership, severity, escalation, and response runbooks. Review job failures, protected-instance coverage, policy compliance, retention, and recovery operations. Investigate whether failures are transient, permission-related, resource configuration, or capacity/region issues.

## Features

- Built-in backup alerts and Azure Monitor log/metric alerting serve different monitoring needs; configure recipients/actions deliberately.
- Backup Reports aggregate data from one or more vaults when telemetry is routed to the reporting workspace.
- Reporting data can be delayed; reports are not necessarily a real-time replacement for job status.
- Alert coverage should include failed jobs, stopped protection, unhealthy items, and destructive operations where supported.
- Exam trap: a workbook does not itself enable telemetry collection, and a diagnostic setting does not itself notify responders.

## Code snippets (if any)

```kusto
AddonAzureBackupJobs
| where TimeGenerated > ago(7d)
| summarize Jobs=count() by JobStatus
| order by Jobs desc
```

Use this as a starting point in a workspace populated by Azure Backup diagnostic data. Table and column availability depend on the configured reporting schema; inspect the workspace schema and replace fields if your data uses a different table version.

## Do's and Don'ts

- Do route required backup diagnostics, test alerts, and ensure action groups reach monitored responders.
- Do review failure trends and identify protected resources with no recent successful job.
- Do use least privilege for reporting workspaces and protect recovery-operation audit data.
- Don't treat a report's aggregation delay as proof that a recent job failed or succeeded; verify the job record in the vault.
- Don't monitor only job failures; detect missing coverage and policy drift too.

## Real-life implementation

For a subscription-wide backup service, route supported vault diagnostics to a central workspace, use Backup Reports to track protected-item coverage and job outcomes, and alert the on-call team on critical failures. A daily compliance review identifies resources without a recent recovery point, while a monthly restore drill reports actual recovery times. Separate alert recipients for operations and security incidents.

## Q&A

1. **What is required for Backup Reports in Log Analytics?** Configure supported vault diagnostics to send data to the workspace and use the reporting experience.
2. **Does a diagnostic setting notify an operator?** No; notification requires alerting and an action group.
3. **Why monitor successful-job recency as well as failures?** A workload might not be protected or might have stopped producing jobs without a visible current failure.
4. **Where verify an individual backup job?** In the vault's Backup jobs view or the corresponding ingested record, accounting for reporting delay.

References: [Azure Backup Reports](https://learn.microsoft.com/azure/backup/backup-azure-reports-introduction), [Configure Azure Backup reports](https://learn.microsoft.com/azure/backup/configure-reports), [Azure Backup monitoring and alerts](https://learn.microsoft.com/azure/backup/backup-azure-monitoring-built-in-monitor).

Syllabus: [copilot-az104-syllabus.md](../../../copilot-az104-syllabus.md).
