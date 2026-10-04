# Assign roles at different scopes

Syllabus: [Domain 1 — Manage Azure identities and governance](../../../copilot-az104-syllabus.md#1-manage-azure-identities-and-governance-20-25)

## What

Create Azure RBAC role assignments at management group, subscription, resource group, or individual resource scope. An assignment is inherited by descendant resources unless a service or authorization boundary changes the effective result. Select the narrowest scope that completely covers the required work.

## Why

Scope controls blast radius, operational autonomy, and the amount of access that must be reviewed. Subscription-level access is convenient but broad; resource-level access is precise but may become difficult to operate at scale. Group-based assignments and management-group inheritance can balance centralized governance with team autonomy.

## How

In the portal, open the target scope's **Access control (IAM)** and add the role assignment. Azure CLI uses a resource ID or scope string with `az role assignment create`; PowerShell uses `New-AzRoleAssignment`. Confirm the principal is correct and the selected scope is the intended resource path. Audit inherited assignments separately from assignments created directly at the scope.

## Features

- Resource-group assignments apply to resources in that group; subscription assignments cover its resource groups and resources.
- Management-group assignments can flow down to subscriptions and their resources.
- Moving resources between scopes can change inherited authorization; reassess access after moves.
- **Exam trap:** assigning a role at the resource group does not grant access to sibling resource groups.
- Azure RBAC does not generally support an explicit deny assignment made by a normal role assignment; Azure Policy is not a substitute for access control.

**Microsoft Learn:** [Understand Azure role assignment scope](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview); [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal); [Assign Azure roles using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli)

## Code snippets (if any)

Example Azure CLI assignment of Reader to a group at one resource group:

```bash
az role assignment create --assignee-object-id "<group-object-id>" --assignee-principal-type Group --role Reader --scope "/subscriptions/<subscription-id>/resourceGroups/<resource-group>"
```

Run with an identity authorized to create role assignments and replace both placeholders with actual IDs.

## Do's and Don'ts

- Do choose the smallest usable scope, especially for privileged roles.
- Do prefer group principals for stable team access and make assignment ownership clear.
- Don't assume scope names are sufficient; validate the full resource ID and subscription.
- Don't use a broad parent scope merely to avoid documenting multiple assignments.

## Real-life implementation

A project operator manages only its workload group, while the platform team retains subscription-level governance. The operator group receives Contributor at the workload resource group and a separate data role at the exact storage boundary. A review confirms no inherited broader role undermines least privilege and that no sibling application is in scope.

## Q&A

**Q: Which scope is narrower: subscription or resource group?**
A: Resource group; it affects that group and its resources rather than the whole subscription.

**Q: What happens to a child resource when a role is assigned to its parent resource group?**
A: It normally inherits the assignment unless another authorization boundary applies.

**Q: Why review inherited access?**
A: A user may have effective access from a parent assignment that is not visible as a direct assignment on the resource.

**Q: What can change after moving a resource to another group?**
A: Its inherited assignments and therefore effective access.
