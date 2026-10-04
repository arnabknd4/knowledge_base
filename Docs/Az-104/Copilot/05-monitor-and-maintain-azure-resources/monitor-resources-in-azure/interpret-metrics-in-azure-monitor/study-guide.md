# Interpret metrics in Azure Monitor

## What

Azure Monitor Metrics stores numeric, time-series measurements emitted by Azure resources and applications. Each sample has a timestamp, value, resource, metric name, and optional dimensions such as status code or API name. Platform metrics are collected automatically for many services; custom metrics can be published by instrumented workloads.

## Why

Metrics are optimized for near-real-time health and trend analysis. Use them to identify saturation, latency, availability, and capacity trends, power dashboards, and trigger low-latency metric alerts. Establish baselines before setting thresholds: a CPU spike alone is not necessarily an incident, while sustained saturation coupled with latency can be.

## How

Choose the resource and metric namespace, then set time range, time grain, aggregation, and dimensions. Compare like-for-like periods and use splitting/filtering to find the affected instance or workload slice. Metrics can be explored in the Azure portal, queried through APIs/CLI, charted in Metrics Explorer, and routed to a workspace through diagnostic settings where supported.

## Features

- Common aggregations include Average, Minimum, Maximum, Total, and Count; availability and meaning depend on the metric.
- Dimensions let you filter or split series, but high-cardinality dimensions can make analysis and alerting expensive or unwieldy.
- Platform metrics are generally retained for 93 days in Azure Monitor Metrics; longer-term analysis may require export or another store.
- Metric alerts evaluate time-series conditions frequently and can evaluate multiple resources at scale.
- Exam trap: a metric is not the same as a log record. Metrics are numeric and efficient for trends; logs preserve richer event/context and support KQL.

## Code snippets (if any)

```bash
az monitor metrics list --resource "/subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Compute/virtualMachines/<vm-name>" --metric "Percentage CPU" --interval PT5M --aggregation Average
```

This requests five-minute CPU averages for one VM. Confirm the metric name and supported time grain for the target resource provider; use a full resource ID and an authenticated Azure CLI context.

## Do's and Don'ts

- Do select a useful grain and aggregation for the question; inspect peaks as well as averages when diagnosing brief saturation.
- Do correlate related signals (for example CPU, queue depth, request duration, and errors).
- Do verify the metric namespace, units, dimensions, and availability before building an alert.
- Don't treat a single data point as a trend or assume missing samples mean a healthy resource.
- Don't use a metric alert for rich event logic better expressed as a log alert.

## Real-life implementation

For a web API, chart request count, server response time, failed requests, and compute utilization together. Alert on sustained latency or failure-rate breaches, then split by region or backend to localize impact. Review the charts during capacity planning and adjust scale targets only after correlating demand with service health and cost.

## Q&A

1. **When choose metrics over logs?** For numeric time-series monitoring, fast trend visualization, and metric alerts.
2. **What does a dimension do?** It segments a metric series, such as CPU by VM or requests by response code.
3. **Why can Average hide an incident?** A short severe spike can be diluted by the averaging interval; inspect Maximum and finer grains too.
4. **Does an alert rule create the notification destination?** No. An alert rule detects a condition; an action group defines notification or automation actions.

References: [Azure Monitor metrics](https://learn.microsoft.com/azure/azure-monitor/metrics/data-platform-metrics), [Metrics Explorer](https://learn.microsoft.com/azure/azure-monitor/metrics/metrics-explorer).

Syllabus: [copilot-az104-syllabus.md](../../../copilot-az104-syllabus.md).
