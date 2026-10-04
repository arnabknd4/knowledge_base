# Manage resource groups

Syllabus: [Domain 1 — Manage Azure identities and governance](../../../copilot-az104-syllabus.md#1-manage-azure-identities-and-governance-20-25)

## What

Create, organize, manage, and where supported move Azure resources through resource groups. A resource group is a management and lifecycle container within one subscription; resources can be in different regions from the group's metadata location, subject to service-specific constraints.

## Why

Resource-group boundaries support ownership, role assignment, policy scope, deployment operations, and coordinated lifecycle. Put resources together when they share governance and lifecycle needs—not merely because they are deployed on the same day. Resource groups are not network or physical boundaries.

## How

In the portal, create a resource group in the intended subscription and metadata region, then assign access/policy and deploy resources. Azure CLI uses `az group create/show/delete`; PowerShell uses `New-AzResourceGroup` and `Get-AzResourceGroup`. Before moving resources, check source/target subscription, supported resource types, dependencies, locks, and move validation. A group move can change inherited policy and RBAC effects.

## Features

- A resource group belongs to one subscription; it cannot itself contain resources from multiple subscriptions.
- Its location stores resource-group metadata; it does not force every contained resource into that region.
- Deleting a group can delete contained resources, so review dependencies and protection controls first.
- **Exam trap:** resources can have a region different from the resource group's location, but service-specific placement rules still apply.

**Microsoft Learn:** [Manage Azure resource groups](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal); [Move Azure resources to another resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription)

## Code snippets (if any)

Create a resource group:

```bash
az group create --name "<resource-group>" --location "<azure-region>"
```

Use a valid Azure region name and an authenticated context targeting the intended subscription.

## Do's and Don'ts

- Do align group boundaries to ownership, policy, access, and lifecycle.
- Do inspect dependencies and inherited controls before moving/deleting.
- Don't assume moving a resource is supported or has no downtime; validate each resource type.
- Don't use resource groups as a substitute for management groups or network segmentation.

## Real-life implementation

A product team gets a dedicated resource group per environment, with a platform baseline policy and team access scoped to that group. Shared networking remains in a centrally managed group. Before decommissioning a test environment, the owner inventories resources, checks dependencies and data retention, and obtains approval because deleting the group may remove every resource within it.

## Q&A

**Q: Can a resource group contain resources from multiple subscriptions?**
A: No; a resource group exists within one subscription.

**Q: Must a resource's region match its resource group's location?**
A: No, not generally; the resource group location is for its metadata, subject to individual service rules.

**Q: What is a key risk of deleting a resource group?**
A: Its contained resources may be deleted as part of the operation.

**Q: What should be reviewed after moving a resource?**
A: Dependencies, supported move behavior, inherited access/policy, locks, and service-specific effects.
