# Create users and groups

Syllabus: [Domain 1 — Manage Azure identities and governance](../../../copilot-az104-syllabus.md#1-manage-azure-identities-and-governance-20-25)

## What

Create and manage Microsoft Entra ID user objects and security or Microsoft 365 groups. Users can be cloud-only or synchronized from an on-premises identity source; the source of authority determines where identity attributes should be changed. Security groups are for access control, while Microsoft 365 groups provide collaboration membership and shared resources.

## Why

Identity lifecycle and group-based access are foundational control-plane operations. Groups reduce one-by-one assignments and make onboarding/offboarding auditable. Choose a group type based on intended use, not merely convenience: security groups can be used for Azure RBAC and app access; Microsoft 365 groups are for collaboration, not a replacement for every authorization group.

## How

In the Azure portal, use **Microsoft Entra ID > Users > New user** or **Groups > New group**; review user type, sign-in name, group type, membership type, owners, and members before creation. Azure CLI supports cloud user and group operations (`az ad user create`, `az ad group create`, `az ad group member add`); Microsoft Graph PowerShell provides `New-MgUser` and `New-MgGroup`. Use current Graph modules and least-privileged directory permissions. Synchronized identities should normally be administered at their authoritative source.

## Features

- A group can use assigned membership or supported dynamic membership; dynamic membership requires the relevant Entra licensing.
- Assign owners so group administration is not dependent on one administrator.
- Avoid embedding secrets in scripts. Use secure parameter input, managed automation credentials, and approved provisioning workflows.
- **Exam trap:** an Azure resource's role assignment is not the same thing as a directory group or an application role.

**Microsoft Learn:** [Create, configure, and manage users](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-create-delete-users); [Create a group and add members in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-groups)

## Code snippets (if any)

Illustrative Azure CLI example for a cloud-only security group; substitute a unique display name and verify the resulting object before assigning access:

```bash
az ad group create --display-name "App-Readers" --mail-nickname "app-readers" --security-enabled true
```

## Do's and Don'ts

- Do use groups for repeatable access patterns and review owners/membership.
- Do distinguish cloud-only from synchronized users before changing attributes.
- Don't create duplicate identities to work around source-of-authority restrictions.
- Don't grant broad directory roles just to create a user or group.

## Real-life implementation

For a new application team, create a dedicated security group, add two accountable owners, and document its intended resource scope. Add users through the organization's joiner/mover/leaver process; attach Azure RBAC to the group only after validating the target scope and role. Periodically reconcile actual membership with the approved roster.

## Q&A

**Q: Which group is the normal choice for Azure resource access?**
A: A security group, because it can be used as a principal in Azure RBAC assignments.

**Q: Where should a synchronized user's authoritative attributes be changed?**
A: At the source of authority, typically the on-premises directory or its identity synchronization system.

**Q: Does creating a group grant it access?**
A: No. Access requires an explicit assignment or application authorization.

**Q: What should be planned when creating a group?**
A: Purpose, type, membership model, owners, lifecycle, and the permissions that will later be assigned.
