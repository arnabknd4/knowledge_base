# Configure resource locks

Syllabus: [Domain 1 — Manage Azure identities and governance](../../../copilot-az104-syllabus.md#1-manage-azure-identities-and-governance-20-25)

## What

Apply Azure management locks to subscriptions, resource groups, or supported individual resources to reduce accidental deletion or modification. The two lock levels are **CanNotDelete** (read and modify are allowed, deletion is blocked) and **ReadOnly** (read is allowed; updates and deletion are blocked at the management plane).

## Why

Locks add an operational safety guardrail for critical resources. They are not a backup, availability control, or substitute for access management. A lock can intentionally block legitimate changes, so change procedures must identify lock owners and account for lock removal/reapplication.

## How

In the portal, select the scope and use **Locks > Add**; choose lock type and document rationale. Azure CLI supports `az lock create/list/delete`; PowerShell uses `New-AzResourceLock` and `Remove-AzResourceLock`. Locks inherit to child resources where applicable. To modify or delete a locked resource, an authorized operator with lock-management permission must remove or change the lock, perform the approved operation, and restore it if required.

## Features

- Locks are enforced by Azure Resource Manager for management-plane operations; they do not replace data protection or service-specific data access controls.
- A ReadOnly lock can prevent operations that appear read-like but require a write action, such as certain `POST` operations.
- A lock at a parent scope can affect descendants and may need removal at the correct scope.
- **Exam trap:** CanNotDelete still allows modification; ReadOnly blocks modification as well as deletion.

**Microsoft Learn:** [Lock your Azure resources to protect your infrastructure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources); [Azure CLI resource locks](https://learn.microsoft.com/en-us/cli/azure/lock)

## Code snippets (if any)

Create a CanNotDelete lock on a resource group:

```bash
az lock create --name "protect-production" --lock-type CanNotDelete --resource-group "<resource-group>"
```

The caller needs permission to create locks at that scope.

## Do's and Don'ts

- Do record scope, business owner, expiration/review, and an emergency removal procedure.
- Do test deployment and automation workflows before applying ReadOnly.
- Don't assume a lock prevents data loss caused through a service's data plane.
- Don't apply broad locks without checking their effect on child resource operations.

## Real-life implementation

A production resource group receives CanNotDelete to protect its key resources from accidental removal. The change process explains that deployment tooling may still update resources but cannot delete them. For planned retirement, an approved operator temporarily removes the lock, performs the change, validates state, and restores protection where appropriate.

## Q&A

**Q: Which lock permits updates but blocks deletion?**
A: CanNotDelete.

**Q: Which lock blocks both updates and deletion at the management plane?**
A: ReadOnly.

**Q: Does a lock replace backups?**
A: No. It is a management-plane guardrail, not a recovery mechanism.

**Q: Why can a parent lock affect a child?**
A: Locks at a parent scope can be inherited by descendants.
