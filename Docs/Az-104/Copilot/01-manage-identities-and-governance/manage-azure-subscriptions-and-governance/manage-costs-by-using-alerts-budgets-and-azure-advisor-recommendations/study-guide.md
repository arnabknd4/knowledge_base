# Manage costs by using alerts, budgets, and Azure Advisor recommendations

Syllabus: [Domain 1 — Manage Azure identities and governance](../../../copilot-az104-syllabus.md#1-manage-azure-identities-and-governance-20-25)

## What

Use Azure Cost Management budgets and alert conditions to track spending against a planned amount, and use Azure Advisor recommendations to identify possible cost, reliability, security, operational-excellence, and performance improvements. These tools inform action; they do not automatically make all costs stop or guarantee savings.

## Why

Cloud cost is driven by consumption, configuration, and commercial terms. Budgets provide a forecast/actual-spend signal for a defined scope and period; notifications make that signal actionable. Advisor highlights resource-specific opportunities that require validation against workload requirements, availability, and performance.

## How

In **Cost Management + Billing > Cost Management > Budgets**, choose scope, period, amount, thresholds, and notification recipients/action groups where supported. Review actual and forecast alerts and test notification routing. Azure CLI/PowerShell support Cost Management operations selectively; use the portal or documented APIs for budget configuration as appropriate. In **Advisor > Cost**, inspect recommendation details, affected resources, estimated savings, and prerequisites before action.

## Features

- Budgets trigger notifications when actual or forecast conditions meet thresholds; a budget is not a spending cap and does not automatically shut resources down.
- Cost scope and billing context matter; ensure the budget covers the intended subscription/resource group and charge type.
- Advisor recommendations are suggestions based on available telemetry and configuration; validate impact and business constraints.
- **Exam trap:** an alert notification is not an automatic remediation. Automation requires a separately configured action and safe controls.

**Microsoft Learn:** [Create and manage Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets); [Cost alerts](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-alerts-monitor-usage-spending); [Azure Advisor overview](https://learn.microsoft.com/en-us/azure/advisor/advisor-overview)

## Code snippets (if any)

No snippet required. Budget alert thresholds, billing scopes, and notification configuration are specific to the tenant and commercial agreement; configure and verify through Cost Management rather than using a generic command that may target the wrong billing scope.

## Do's and Don'ts

- Do configure multiple thresholds, responsible recipients, and a response runbook.
- Do compare Advisor savings with workload availability and performance needs.
- Don't present a budget as a hard spending limit.
- Don't implement an Advisor recommendation without assessing dependency, downtime, and rollback.

## Real-life implementation

A service owner sets a monthly resource-group budget with forecast and actual thresholds routed to the owner and finance operations. At each alert, the team checks cost analysis by service/tag, then reviews Advisor candidates in a change window. Any resize or shutdown is tested and monitored; alerts remain active because they detect drift, not prevent it.

## Q&A

**Q: Does exceeding an Azure budget automatically stop resources?**
A: No. Budgets generate notifications; separate automation would be needed for an action.

**Q: What does a forecast budget alert indicate?**
A: Based on current trends, projected spend is expected to reach its configured threshold.

**Q: Should an Advisor recommendation always be implemented?**
A: No. Validate savings, workload needs, risk, and operational impact first.

**Q: What makes a budget operationally useful?**
A: Correct scope/period, meaningful thresholds, recipients, and a defined response process.
