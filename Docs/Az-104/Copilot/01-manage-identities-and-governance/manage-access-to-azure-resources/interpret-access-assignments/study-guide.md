# Interpret access assignments

Syllabus: [Domain 1 — Manage Azure identities and governance](../../../copilot-az104-syllabus.md#1-manage-azure-identities-and-governance-20-25)

## What

Determine a principal's effective Azure access by examining role assignments, role definitions, scopes, inheritance, group membership, and applicable condition or eligibility state. Interpret both direct and indirect assignments and distinguish control-plane rights from data-plane permissions.

## Why

Troubleshooting must explain not only “which role?” but also “for which principal, at what scope, through what path, and with which actions?” A correct-looking role may not grant access because it is at the wrong scope, assigned to a different object, unavailable as an eligible assignment, or missing a required data action. Conversely, a parent-scope assignment can grant more access than a local view suggests.

## How

Use the portal's **Access control (IAM) > Check access** to inspect a user/group's effective assignments, and inspect **Role assignments** for scope and inheritance. Azure CLI provides `az role assignment list --assignee <id> --all --include-inherited`; PowerShell provides `Get-AzRoleAssignment`. Verify the principal object ID (especially for groups and guests), role definition actions/data actions, scope, and PIM activation state. For a denied request, check the exact operation, resource ID, data-plane endpoint, and propagation delay.

## Features

- A user's access may be inherited through group membership or parent scope.
- Group membership and RBAC updates can take time to propagate; refresh credentials/token or retry only after confirming configuration.
- Role assignments, role definitions, and Azure Policy answer different questions: authorization, permitted operations, and resource configuration/compliance.
- **Exam trap:** a role assignment's friendly name alone is insufficient; inspect scope and actions, and account for data actions.

**Microsoft Learn:** [View access for a user to Azure resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access); [List Azure role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-portal); [Azure RBAC troubleshooting](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting)

## Code snippets (if any)

List direct and inherited role assignments for a principal:

```bash
az role assignment list --assignee "<principal-object-id>" --all --include-inherited --output table
```

Use the principal object ID to avoid ambiguity where display names are duplicated.

## Do's and Don'ts

- Do trace the full authorization path and compare it to the failed operation.
- Do check whether the role includes the relevant data action.
- Don't infer effective access from one resource's direct assignments alone.
- Don't assume a policy denial is fixed by adding a broader role; diagnose the actual failure source.

## Real-life implementation

A user can list a storage account but receives authorization failure reading a blob. The administrator verifies the user's group membership and inherited assignments, then inspects role definition actions. The management-plane Reader assignment is present, but no blob data role is effective; a least-privilege data role is added at the intended container boundary and tested.

## Q&A

**Q: What are the three core elements to trace in an RBAC assignment?**
A: Principal, role definition, and scope.

**Q: Why might a user see a resource but fail to read its data?**
A: Management-plane permission does not necessarily include the required data-plane action.

**Q: Where can broader access come from if the resource shows no direct assignment?**
A: An inherited assignment from a parent scope or group membership.

**Q: What else can cause an otherwise correct assignment not to work immediately?**
A: Propagation, stale authentication tokens, an unactivated eligible role, or a different authorization failure such as policy.
