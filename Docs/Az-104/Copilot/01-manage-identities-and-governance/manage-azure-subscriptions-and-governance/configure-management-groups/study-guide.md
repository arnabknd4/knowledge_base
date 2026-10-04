# Configure management groups

Syllabus: [Domain 1 — Manage Azure identities and governance](../../../copilot-az104-syllabus.md#1-manage-azure-identities-and-governance-20-25)

## What

Use management groups to organize multiple Azure subscriptions into a hierarchy. Azure Policy and Azure RBAC assignments at a management-group scope can be inherited by descendant subscriptions and resources, subject to assignment behavior, exemptions, and authorization rules.

## Why

Management groups provide a governance layer above subscriptions. They help scale consistent controls across business units, environments, or regulatory boundaries while allowing targeted exceptions. A poor hierarchy creates confusing inherited access and policy; structure it around durable governance requirements rather than temporary projects.

## How

In the portal, open **Management groups**, create or move groups/subscriptions within authorized boundaries, and apply policies/roles at the intended node. Azure CLI uses `az account management-group`; PowerShell provides `Get-AzManagementGroup` and management-group policy/role assignment cmdlets. Confirm the current tenant, hierarchy, management-group ID, and inheritance before applying broad assignments. Tenant root group changes require appropriate elevated authorization.

## Features

- Subscriptions are placed under one management-group hierarchy at a time; moving them changes inherited governance.
- Parent assignments can govern descendants; child scopes can have additional assignments and documented policy exemptions.
- Management groups organize subscription governance, not resources directly in the way a resource group does.
- **Exam trap:** a policy or RBAC assignment at a management group can affect many subscriptions—verify scope before applying.

**Microsoft Learn:** [Azure management groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview); [Create and manage management groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/manage); [Azure CLI management groups](https://learn.microsoft.com/en-us/cli/azure/account/management-group)

## Code snippets (if any)

List management groups visible to the current Azure CLI identity:

```bash
az account management-group list --output table
```

Visibility and management rights depend on the identity's tenant permissions.

## Do's and Don'ts

- Do use a small, comprehensible hierarchy aligned to governance boundaries.
- Do test inherited policy and access before moving production subscriptions.
- Don't use management groups as project/resource containers.
- Don't grant broad roles or assign restrictive policy at the tenant root without impact analysis and an exception strategy.

## Real-life implementation

A platform team places subscriptions under separate production and nonproduction branches while both inherit baseline security policy from a parent. A regional team receives delegated rights at its branch, not the tenant root. Before a subscription is reparented, the team evaluates policy compliance, effective access, and possible deployment impact.

## Q&A

**Q: What can be organized under a management group?**
A: Other management groups and Azure subscriptions.

**Q: What happens to inherited governance when a subscription moves?**
A: It can change because the subscription is now under a different parent hierarchy.

**Q: Can resource groups be placed directly under management groups?**
A: No. Subscriptions are the resource hierarchy level directly governed under management groups.

**Q: Why is root-scope assignment high impact?**
A: It may affect all descendant management groups and subscriptions.
