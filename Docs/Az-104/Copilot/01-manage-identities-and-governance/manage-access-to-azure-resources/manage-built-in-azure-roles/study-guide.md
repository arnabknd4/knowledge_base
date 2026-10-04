# Manage built-in Azure roles

Syllabus: [Domain 1 — Manage Azure identities and governance](../../../copilot-az104-syllabus.md#1-manage-azure-identities-and-governance-20-25)

## What

Use Azure role-based access control (Azure RBAC) built-in roles to authorize identities to perform actions on Azure resources. A role definition contains permitted actions/data actions and exclusions; a role assignment binds a role to a security principal at a scope. Common built-in roles include Owner, Contributor, Reader, and service-specific roles such as Storage Blob Data Reader.

## Why

RBAC is the authorization plane for Azure resource management and supported data operations. Least privilege reduces accidental changes and compromise impact. Role selection must satisfy the task without granting unrelated permissions, and the administrator must distinguish management-plane operations from data-plane access.

## How

Use **Access control (IAM) > Add role assignment** on the target scope. Compare role descriptions and JSON definitions before selection. Azure CLI can inspect built-ins with `az role definition list --name Reader`; PowerShell uses `Get-AzRoleDefinition`. To assign, choose the principal, role, and scope, then validate via **Check access** or `az role assignment list`. For recurring access, prefer group principals and consider eligible/time-bound assignment through Privileged Identity Management if licensed and configured.

## Features

- **Owner** can manage resources and role assignments; **Contributor** can manage resources but cannot assign RBAC roles; **Reader** is read-only for management-plane resource configuration.
- A general management role does not necessarily grant access to data stored in a service. Use an appropriate data role when required.
- Entra directory roles and Azure RBAC roles are distinct authorization systems, although the same principal may hold both.
- **Exam trap:** Contributor is not a way to delegate role assignment; Owner or a role with `Microsoft.Authorization/roleAssignments/write` is needed.

**Microsoft Learn:** [Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles); [Azure RBAC role definitions](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions); [Azure RBAC overview](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)

## Code snippets (if any)

Inspect the built-in Reader role definition:

```bash
az role definition list --name Reader --output table
```

Use the role's permitted actions and intended plane—not just the display name—to determine whether it satisfies the scenario.

## Do's and Don'ts

- Do use a service-specific role where a broad role is unnecessary.
- Do verify both management-plane and data-plane requirements.
- Don't grant Owner to solve a simple resource-operation requirement.
- Don't confuse an Entra administrator role with an Azure resource role.

## Real-life implementation

A support team needs visibility into a production resource group and must read blob contents for diagnostics. Assigning only Reader to the resource group allows inspection of Azure resource configuration, but not necessarily blob data. Add the narrow Storage Blob Data Reader role at the storage account or container scope only if the business case requires it, then validate access and periodically review it.

## Q&A

**Q: What does a role assignment combine?**
A: A security principal, role definition, and scope.

**Q: Can Contributor grant another user an Azure role?**
A: No, not by default; Contributor cannot manage role assignments.

**Q: Does Reader automatically permit reading blobs?**
A: Not necessarily. Blob content access generally needs an appropriate data-plane role.

**Q: Are Entra directory roles and Azure RBAC roles interchangeable?**
A: No. They govern different authorization domains.
