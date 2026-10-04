# Manage external users

Syllabus: [Domain 1 — Manage Azure identities and governance](../../../copilot-az104-syllabus.md#1-manage-azure-identities-and-governance-20-25)

## What

Manage external collaboration identities in Microsoft Entra External ID, commonly represented in workforce-tenant collaboration as guest users. Invite or otherwise onboard an external person, govern their authentication and access, collaborate through groups/apps, and remove or review that access when no longer needed.

## Why

External access extends the tenant's trust boundary. A guest should receive only the resources required, for a defined business purpose and duration. Invitation is not equivalent to authorization: resource access still requires app permissions, group membership, or Azure role assignment. Cross-tenant settings and external collaboration policies can influence whether guests can be invited and what they can access.

## How

In the portal, use **Microsoft Entra ID > Users > New user > Invite external user** (labels can vary by portal experience), supply the verified address and a business justification, and assign only the approved access. Azure CLI supports guest invitations with `az ad user invite`; Microsoft Graph PowerShell offers invitation APIs/cmdlets. Confirm redemption/status, apply access packages or entitlement processes if configured, and use access reviews where appropriate. Coordinate invitation policy, cross-tenant access settings, and resource-side authorization.

## Features

- Invitation creates a guest representation in the resource tenant; the person commonly authenticates with their home identity provider.
- External collaboration settings can restrict who may invite and what guest users can see/do.
- Access reviews can support periodic review of guest membership/access; they do not replace an offboarding policy.
- **Exam trap:** deleting a guest identity may not revoke every separately issued credential or remove access to resources outside the tenant; revoke and review relevant access paths.

**Microsoft Learn:** [Add and invite guest users](https://learn.microsoft.com/en-us/entra/external-id/add-users-administrator); [External collaboration settings](https://learn.microsoft.com/en-us/entra/external-id/external-collaboration-settings-configure); [Microsoft Entra access reviews](https://learn.microsoft.com/en-us/entra/id-governance/access-reviews-overview)

## Code snippets (if any)

```bash
az ad user invite --email-address "partner@example.com" --invite-redirect-url "https://myapps.microsoft.com"
```

Confirm current CLI parameter behavior and tenant policy before using; the invitation alone does not grant Azure resource access.

## Do's and Don'ts

- Do validate the sponsor, business purpose, target resources, and expiry/review date.
- Do use least privilege and monitor external collaboration settings.
- Don't invite a partner as an internal member simply to bypass guest controls.
- Don't assume accepting an invitation grants access to a subscription or resource.

## Real-life implementation

A vendor engineer needs read-only access to one project resource group for a short engagement. The sponsor invites the verified account, adds it to an approved guest group, and an owner grants a narrow Reader assignment at the resource-group scope. An access review confirms continued need; at contract end the assignment and guest access are removed and audited.

## Q&A

**Q: Does inviting an external user automatically grant Azure resource access?**
A: No. The guest must receive a separate authorization assignment.

**Q: What identity usually authenticates a collaboration guest?**
A: Their home identity provider, subject to tenant configuration and redemption flow.

**Q: Why use an access review?**
A: To periodically validate that guest access remains necessary and appropriately scoped.

**Q: What is the key architectural distinction?**
A: Authentication establishes identity; authorization to each app/resource must still be granted separately.
