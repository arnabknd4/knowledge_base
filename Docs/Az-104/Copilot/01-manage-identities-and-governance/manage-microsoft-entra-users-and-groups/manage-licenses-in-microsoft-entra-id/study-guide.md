# Manage licenses in Microsoft Entra ID

Syllabus: [Domain 1 — Manage Azure identities and governance](../../../copilot-az104-syllabus.md#1-manage-azure-identities-and-governance-20-25)

## What

Assign, remove, and troubleshoot user-based product licenses in Microsoft Entra ID. Licenses may be assigned directly to a user or through a group. Group-based licensing centralizes assignment and can apply selected service plans; the tenant must own sufficient eligible licenses.

## Why

Licensing enables product capabilities but is a separate concern from Azure RBAC and resource authorization. Group assignment helps align entitlements with role or department lifecycle and simplifies joiner/mover/leaver administration. It also introduces dependencies: membership, usage location, available quantity, service-plan configuration, and directory licensing state.

## How

In the portal, review **Billing > Licenses > All products**, choose a product, then assign directly or use group-based licensing where available. Set usage location before assigning a license. Azure CLI has limited licensing workflows; use Microsoft Graph PowerShell/Graph API for automation and follow the official license-assignment procedure. Review processing errors and service-plan selections after assignment rather than assuming the operation succeeded.

## Features

- Group-based licensing evaluates group membership and applies configured product/service plans; it can take time to process.
- A user may have overlapping direct and group-based entitlements; removing one assignment does not necessarily remove the effective license.
- Licensing errors can result from insufficient seats, invalid usage location, conflicting plans, or unsupported combinations.
- **Exam trap:** an Azure subscription's billing relationship does not mean every Entra user automatically has a Microsoft 365 license.

**Microsoft Learn:** [Assign licenses to users by group membership in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/users/licensing-groups-assign); [Assign or remove licenses in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/license-users-groups)

## Code snippets (if any)

No snippet required. License SKU identifiers and service-plan selections are tenant-specific; for production automation use Microsoft Graph's documented license assignment API and resolve the tenant's SKUs first.

## Do's and Don'ts

- Do track entitlement ownership, available seats, usage location, and group membership.
- Do inspect per-user license assignment details and processing errors.
- Don't remove a direct assignment without checking for a group assignment that still grants the license.
- Don't assume license assignment grants Azure resource permissions.

## Real-life implementation

An organization maps approved job functions to licensing groups. HR-approved group membership drives entitlements; a licensing administrator monitors group processing errors and seat consumption. A transfer between departments updates group membership through the identity lifecycle process, with a review of overlapping assignments before old entitlements are removed.

## Q&A

**Q: What must be set for many user license assignments?**
A: The user's usage location, which helps determine regional licensing eligibility.

**Q: If a direct license is removed, is the product always removed?**
A: No. A group-based assignment or another assignment can still provide it.

**Q: Is group-based licensing the same as Azure RBAC?**
A: No. It manages product entitlements, not authorization to Azure resources.

**Q: What are common reasons for a licensing error?**
A: No available seat, missing/invalid usage location, conflicting service plans, or an unsupported license combination.
