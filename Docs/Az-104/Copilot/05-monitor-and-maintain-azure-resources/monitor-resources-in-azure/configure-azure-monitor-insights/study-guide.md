# Configure and interpret Azure Monitor Insights

## What

Azure Monitor Insights are curated monitoring experiences that combine relevant telemetry, visualizations, and health information for supported resources. Common examples include VM insights, Storage insights, and Network insights. They simplify resource-level and estate-level analysis but depend on the underlying metrics, logs, agents, and configuration.

## Why

Insights provide an operational starting point for common questions without requiring an administrator to build every chart from scratch. They help spot trends, bottlenecks, and unhealthy dependencies, and provide context for deeper metrics and KQL investigation.

## How

Open the appropriate insight for the resource or fleet. Confirm prerequisites such as Azure Monitor Agent/DCR collection for guest VM data, diagnostic settings for resource logs, and adequate permissions. Select time range and scope, inspect health and trends, drill into a resource or component, then validate suspected issues against raw metrics/logs.

## Features

- VM insights can show guest performance and dependency information when the required collection is configured; enabling the view alone does not install/configure collection automatically.
- Storage insights surfaces service and capacity metrics; use the account's supported metrics and dimensions to investigate.
- Network insights provides curated network monitoring views; Network Watcher has additional connectivity diagnostics and topology tools.
- Views and prerequisites change by resource type and portal experience. Insights are not a substitute for alerting or a backup.
- Exam trap: distinguish resource-health/insight visualization from an alert rule, and verify telemetry is actually being collected.

## Code snippets (if any)

Snippet not required: Insights are primarily configured and interpreted through the Azure portal experience; the operational task is to validate prerequisites and drill into the relevant metric/log signal.

## Do's and Don'ts

- Do verify freshness, scope, collection configuration, and time range before drawing conclusions.
- Do use Insights to discover a signal, then inspect its underlying metric or log for diagnosis.
- Do compare resource behavior with application-level service objectives and dependencies.
- Don't assume an empty chart means zero utilization; it may indicate missing collection or unsupported telemetry.
- Don't rely only on a dashboard: define alert rules for conditions requiring response.

## Real-life implementation

During a VM performance incident, use VM insights to locate high-resource guests and view trends, then correlate guest CPU/memory/disk signals with platform metrics and application latency. If guest telemetry is absent, check agent health, DCR association, workspace access, and ingestion before changing VM size. For a storage slowdown, compare latency and transaction metrics with availability and throttling indicators.

## Q&A

1. **Do Insights collect every guest metric automatically?** No. Check the insight's agent/DCR and telemetry prerequisites.
2. **What should follow an anomalous chart?** Drill into the underlying metric/log data and correlate with service symptoms.
3. **Are Insights alerts?** No. Configure alert rules separately for proactive notification.
4. **How is Network Watcher different?** It provides specific network diagnostics and monitoring tools beyond the curated Insights experience.

References: [VM insights](https://learn.microsoft.com/azure/azure-monitor/vm/vminsights-overview), [Storage insights](https://learn.microsoft.com/azure/storage/common/storage-insights-overview), [Azure Monitor Insights](https://learn.microsoft.com/azure/azure-monitor/insights/insights-overview).

Syllabus: [copilot-az104-syllabus.md](../../../copilot-az104-syllabus.md).
