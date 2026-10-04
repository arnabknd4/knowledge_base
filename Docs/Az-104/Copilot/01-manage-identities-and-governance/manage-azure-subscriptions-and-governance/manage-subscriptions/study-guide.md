# Manage subscriptions

Syllabus: [Domain 1 — Manage Azure identities and governance](../../../copilot-az104-syllabus.md#1-manage-azure-identities-and-governance-20-25)

## What

Manage Azure subscriptions as billing, quota, access, and resource-management boundaries. Subscription operations include selecting the correct context, controlling access and ownership, reviewing subscription properties, and organizing subscriptions under management groups and the appropriate billing arrangement.

## Why

Subscription boundaries influence cost visibility, quotas, policy/RBAC inheritance, and operational separation. A separate subscription can isolate workloads or environments, but increases governance overhead. Subscription lifecycle and billing ownership must be planned carefully because changing directory or billing relationships can affect access, services, and agreements.

## How

Use **Subscriptions** in the portal to inspect IDs, offer/billing details, access, and status. Azure CLI can list/set the active context with `az account list` and `az account set`; PowerShell uses `Get-AzSubscription` and `Set-AzContext`. Confirm tenant and subscription IDs before changes. Use controlled processes for transfers, cancellation, or directory changes, and check current documentation for impact and eligibility.

## Features

- A subscription is a boundary for resource organization, access delegation, quotas, and cost analysis; it is not itself a guarantee of isolation from all shared tenant-level controls.
- Management groups can organize multiple subscriptions and apply governance above them.
- Resource moves between subscriptions are subject to resource-type and dependency limitations.
- **Exam trap:** the active CLI/PowerShell context may not be the intended subscription; verify it before deployment or modification.

**Microsoft Learn:** [Azure subscriptions overview](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/create-subscription); [Add or change Azure subscription administrators](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/add-change-subscription-administrator); [Azure CLI account commands](https://learn.microsoft.com/en-us/cli/azure/account)

## Code snippets (if any)

Select and verify the target subscription in Azure CLI:

```bash
az account set --subscription "<subscription-id>"
az account show --output table
```

Prefer the subscription ID over an ambiguous display name in automation.

## Do's and Don'ts

- Do design boundaries around compliance, billing, quotas, and delegated administration.
- Do verify tenant, subscription ID, permissions, and billing context before changes.
- Don't move or cancel a subscription without assessing resource/service dependencies and business continuity.
- Don't create a new subscription as a substitute for proper policy, role, or resource-group design.

## Real-life implementation

A company separates production and development subscriptions for budget reporting and access governance. Both remain under a shared management-group hierarchy for baseline policy; workload teams receive rights only in their subscription. Deployment pipelines explicitly select the target subscription and log its ID, avoiding accidental production changes from a stale local context.

## Q&A

**Q: What does an Azure subscription commonly provide?**
A: A boundary for resource management, access delegation, quotas, and billing/cost tracking.

**Q: What should be confirmed before running a deployment?**
A: The authenticated tenant and active subscription ID.

**Q: Can all resources always move between subscriptions?**
A: No. Support and prerequisites vary by resource type and dependency.

**Q: What is a management group used for?**
A: Organizing subscriptions and applying governance at a level above them.
