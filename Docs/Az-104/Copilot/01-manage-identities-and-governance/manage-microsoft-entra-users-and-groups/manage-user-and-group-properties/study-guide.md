# Manage user and group properties

Syllabus: [Domain 1 — Manage Azure identities and governance](../../../copilot-az104-syllabus.md#1-manage-azure-identities-and-governance-20-25)

## What

Maintain Microsoft Entra user and group properties such as display name, usage location, account status, contact/organizational attributes, group description, owners, members, and membership type. Properties have different effects: some are informational, some affect licensing or sign-in, and some are governed by an external source of authority.

## Why

Accurate attributes support directory search, access lifecycle, licensing, and operational ownership. Changes must respect the identity's source of authority and avoid confusing a profile update with a permission change. Disabling an account, changing a group member, or changing a group rule can have immediate access consequences and should be controlled.

## How

Use **Microsoft Entra ID > Users/Groups > select object > Properties** or the object's **Members/Owners** views. For bulk edits, use a controlled CSV or Microsoft Graph process, validate a small pilot, and retain results for audit. Azure CLI offers user/group update and membership commands; Microsoft Graph PowerShell offers update cmdlets such as `Update-MgUser` and group member/owner operations. Check whether the object is synchronized or dynamically populated before attempting a direct edit.

## Features

- Usage location is relevant to license assignment; it is not a user's physical location guarantee.
- Dynamic group membership is driven by a rule; manually editing its membership is not the control mechanism.
- Some synchronized attributes are read-only in the cloud because their source of authority is on-premises.
- **Exam trap:** changing a display name does not change a user's sign-in identity, and changing membership is not equivalent to changing a role assignment.

**Microsoft Learn:** [Manage user profiles in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-user-profile-info); [Manage users in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-create-delete-users); [Dynamic membership rules for groups](https://learn.microsoft.com/en-us/entra/identity/users/groups-dynamic-membership)

## Code snippets (if any)

No snippet required. Property names and permitted updates vary by object type, synchronization configuration, and Graph API version; use the portal for a single change or the official Graph cmdlet documentation for automation.

## Do's and Don'ts

- Do verify object ID and source of authority before updating.
- Do preview bulk changes, preserve a rollback/export, and log results.
- Don't manually edit dynamic membership or cloud-edit an authoritative synchronized attribute.
- Don't treat descriptive metadata as an enforcement mechanism.

## Real-life implementation

An HR-driven onboarding feed updates department and manager, while a separate access process controls group membership. Administrators first identify which system owns each field, validate changes against a pilot account, and monitor failed updates. Offboarding disables sign-in and triggers access removal through approved lifecycle processes rather than relying on display attributes.

## Q&A

**Q: Why can a cloud edit to a synchronized property fail or revert?**
A: The on-premises directory is authoritative and synchronization can overwrite the cloud-side value.

**Q: Can an administrator manually add a member to a dynamic group?**
A: No; membership is calculated from the configured rule.

**Q: Does updating a user's department automatically grant department permissions?**
A: No, unless a separately configured rule or application explicitly uses that attribute.

**Q: What should be done before a bulk property update?**
A: Confirm target identities and authority, test a small batch, validate results, and retain an audit trail.
