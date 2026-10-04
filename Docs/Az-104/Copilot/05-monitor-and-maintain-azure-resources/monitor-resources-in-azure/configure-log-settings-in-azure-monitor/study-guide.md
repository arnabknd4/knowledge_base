# Configure log settings in Azure Monitor

## What

Azure Monitor Logs collects structured and semi-structured records into Log Analytics workspaces. Diagnostic settings on Azure resources route supported resource logs and platform metrics to destinations such as a workspace, Storage account, or Event Hubs. Guest OS and application logs require their own collection configuration, commonly through Azure Monitor Agent and data collection rules (DCRs).

## Why

Logging creates the evidence needed for troubleshooting, auditing, threat detection, and cross-resource analysis. Deliberate collection avoids gaps while controlling ingestion, retention, access, and export costs.

## How

Decide which categories and destinations serve each operational or compliance use case. Create a workspace in an appropriate region, configure diagnostic settings for each supported resource, and configure DCRs/agents for guest data. Validate that records arrive in the expected workspace tables, then set retention, access, and cost controls. Use resource-specific tables where available; Azure Diagnostics mode uses a shared `AzureDiagnostics` table.

## Features

- A resource can have diagnostic settings directing data to supported destinations; destination support differs by resource type.
- Diagnostic settings do not automatically collect every guest OS event or application trace.
- DCRs define what Azure Monitor Agent collects and where to send it; use least-privilege workspace access and secure agent deployment.
- Workspace retention and archive options affect queryability and cost. Storage/Event Hubs can serve export or downstream processing scenarios.
- Exam trap: enabling a setting is not proof of ingestion. Confirm category selection, destination permissions, workspace region/health, and actual arrival.

## Code snippets (if any)

```bash
az monitor diagnostic-settings categories list --resource "/subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Storage/storageAccounts/<storage-account>"
```

Discover supported categories before creating a diagnostic setting. Configure the selected categories and destination in the portal or with `az monitor diagnostic-settings create`; supply the resource ID and destination resource ID required by the chosen target.

## Do's and Don'ts

- Do collect only useful categories, define retention by requirement, and assign workspace roles narrowly.
- Do account for data residency, sensitive fields, ingestion volume, and export charges.
- Do test a representative resource and verify records before rolling the configuration out broadly.
- Don't assume the Azure Activity Log or platform metrics are equivalent to resource logs.
- Don't send all high-volume debug logs indefinitely to a workspace without a cost and privacy review.

## Real-life implementation

For a storage estate, route required resource logs to a central operations workspace, retain security-relevant data according to policy, and use a separate restricted workspace if data access boundaries demand it. Use DCRs for VM guest events, with filtering that captures incident evidence without collecting unnecessary verbose events. Alert on missing expected telemetry as well as on adverse events.

## Q&A

1. **What configures platform resource-log routing?** A diagnostic setting on the monitored resource.
2. **What configures guest collection with Azure Monitor Agent?** A data collection rule associated with the agent/resource.
3. **Where do resource-specific logs appear?** In resource-specific tables when supported and selected; otherwise some categories use `AzureDiagnostics`.
4. **Does a diagnostic setting create an alert?** No; it routes telemetry. Alert rules are configured separately.

References: [Diagnostic settings](https://learn.microsoft.com/azure/azure-monitor/essentials/diagnostic-settings), [Azure Monitor Agent overview](https://learn.microsoft.com/azure/azure-monitor/agents/agents-overview), [Data collection rules](https://learn.microsoft.com/azure/azure-monitor/data-collection/data-collection-rule-overview).

Syllabus: [copilot-az104-syllabus.md](../../../copilot-az104-syllabus.md).
