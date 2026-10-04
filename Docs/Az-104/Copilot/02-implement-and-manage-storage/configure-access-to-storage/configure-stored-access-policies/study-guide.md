# Configure stored access policies

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Configure stored access policies](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [SAS overview and stored access policies](https://learn.microsoft.com/azure/storage/common/storage-sas-overview)

## What

A stored access policy is a server-side policy on a supported Storage resource. An eligible service SAS can reference its identifier; the policy supplies shared permissions and validity controls and can be changed or removed to revoke linked access.

## Why

Use a policy when a group of service SAS tokens needs centrally managed validity or revocation. This is more controllable than relying only on SAS expiry, but not universal SAS management. Policies do not apply to account SAS or user delegation SAS. Keep policy count low and design identifiers around client/access purposes.

## How

Create a policy on the target container, queue, table, or file share, then issue a service SAS referencing its identifier. Specify least-privilege permissions and an expiry. To revoke linked tokens, modify or delete the policy and validate that a previously issued token is denied. Manage via portal, CLI, PowerShell, or SDK; check the current tool version for command parameters.

## Features

- Stored access policies are supported for service SAS on supported Blob, Queue, Table, and Azure Files resources.
- Up to five policies can be associated with a resource container, queue, table, or share.
- SAS permissions cannot exceed the associated policy.
- Exam trap: deleting a policy does not revoke account SAS or user delegation SAS; these do not reference it.

## Code snippets (if any)

```bash
# Placeholder <container>; policy governs service SAS that references its identifier.
az storage container policy create --account-name <account> --container-name <container> \
  --name vendor-read --permissions rl --expiry 2026-10-04T18:00Z --auth-mode login
```

## Do's and Don'ts

Do use stable identifiers, centralize related SAS lifecycle, and test revocation. Don't create one policy per token, assume every SAS type honors the policy, or remove a policy without locating dependent clients.

## Real-life implementation

A reporting job receives read/list service SAS linked to a `reporting-read` policy. When the integration is retired, operations disables that policy and verifies that an existing token no longer works. One-off user-delegation SAS are handled separately through expiry/delegation-key controls.

## Q&A

1. Which SAS type can reference a stored access policy? **A service SAS for a supported resource.**
2. How many policies can a resource hold? **Up to five.**
3. Does removing one policy revoke all account SAS? **No; it affects linked service SAS on that resource.**
