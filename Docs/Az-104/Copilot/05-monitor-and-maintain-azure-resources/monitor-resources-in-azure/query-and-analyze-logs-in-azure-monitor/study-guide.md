# Query and analyze logs in Azure Monitor

## What

Azure Monitor Logs uses Log Analytics workspaces and Kusto Query Language (KQL) to search, correlate, aggregate, and visualize log records. A query begins with a table and composes operators such as `where`, `project`, `summarize`, and `render`.

## Why

Logs answer contextual questions that a numeric metric alone cannot: which operation failed, for whom, and with what error? Querying lets administrators investigate incidents, find trends, validate controls, and define log alerts.

## How

In Log Analytics, select a workspace and an appropriate time range; inspect tables and schemas, then build a query incrementally. Filter early by time and relevant resource identifiers to reduce scan volume. Use `summarize` for aggregation and `join` only when necessary. Validate the result set, permissions, and time zone before turning a query into an alert or workbook.

## Features

- KQL is a read-only analytics language; use the correct table and column names for the selected data source.
- Workspace context and Azure resource context can differ. Resource-context access can limit data to resources the user is authorized to view.
- Basic and Analytics log plans have different capabilities and pricing; check current documentation before relying on query features or retention.
- Log alerts run a scheduled query and evaluate its results; query frequency, lookback, threshold, and dimensions affect detection and cost.
- Exam trap: KQL pipeline order matters. `where` filters rows; `project` selects columns; `summarize` groups/aggregates.

## Code snippets (if any)

```kusto
AzureActivity
| where TimeGenerated > ago(24h)
| where ResourceGroup =~ "<resource-group>"
| summarize Events=count() by OperationNameValue, ActivityStatusValue
| order by Events desc
```

The query summarizes recent control-plane activity for one resource group. Replace the placeholder with the exact group name and adjust the time window for the investigation.

## Do's and Don'ts

- Do start with a bounded time range and filters; inspect sample rows before assuming a schema.
- Do use `summarize` and visualizations to communicate patterns, and save tested queries as workbooks or functions where appropriate.
- Do validate query cost and alert semantics, including what happens when there are no rows.
- Don't confuse Azure Activity Log (control-plane operations) with resource-specific data-plane logs.
- Don't expose sensitive data in shared queries, workbooks, or alert descriptions.

## Real-life implementation

After a storage access incident, query the relevant workspace table for the target account, operation, status, and caller over a limited interval. Correlate that evidence with Azure Activity Log changes and identity sign-in information in their respective data sources. Keep a reusable investigation workbook, but use access controls so only authorized operators can inspect sensitive caller details.

## Q&A

1. **What language is used in Log Analytics?** Kusto Query Language (KQL).
2. **Which operator restricts rows?** `where`; apply it early to limit data.
3. **How does a log alert differ from a metric alert?** A log alert evaluates a scheduled KQL query; a metric alert evaluates metric time series.
4. **Can every resource log be queried in every workspace?** No. It must be routed/collected there, and the query must use the correct table and permissions.

References: [Log Analytics overview](https://learn.microsoft.com/azure/azure-monitor/logs/log-analytics-overview), [KQL tutorial](https://learn.microsoft.com/azure/data-explorer/kusto/query/tutorials/learn-common-operators), [Log alerts](https://learn.microsoft.com/azure/azure-monitor/alerts/alerts-create-log-alert-rule).

Syllabus: [copilot-az104-syllabus.md](../../../copilot-az104-syllabus.md).
