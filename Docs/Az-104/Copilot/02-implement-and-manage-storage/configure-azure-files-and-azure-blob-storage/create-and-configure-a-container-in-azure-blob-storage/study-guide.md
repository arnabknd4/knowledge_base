# Create and configure a container in Azure Blob Storage

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Create and configure a container in Azure Blob Storage](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [Create Blob containers in the portal](https://learn.microsoft.com/azure/storage/blobs/blob-containers-portal)

## What

A Blob container groups blobs within a storage account namespace. It is a useful unit for access, lifecycle, and operational organization. In a flat namespace, slashes in blob names are naming conventions, not native directories; hierarchical namespace changes directory semantics.

## Why

Use separate containers for distinct ownership, access, lifecycle, retention, or operational needs. Keep anonymous access disabled unless explicitly required. Combine Entra data-plane authorization with networking controls. Do not confuse a container with a storage account or Azure Files share.

## How

Create the container in the intended account and set public access to private (off). Apply least-privilege data-plane RBAC and any HNS directory ACLs. Configure immutability or encryption requirements as appropriate. Upload a test blob using the portal, CLI, SDK, or AzCopy and verify access from allowed and denied principals.

## Features

- Account-level prohibition of anonymous access can override container-level configuration.
- HNS enables directory semantics and ACLs; flat namespace uses blob names with optional slash prefixes.
- Container SAS/policy permissions, RBAC roles, and network rules solve different authorization problems.
- Exam trap: management-plane Contributor is distinct from Blob data roles; public access should not be enabled as an authorization shortcut.

## Code snippets (if any)

```bash
# Placeholder account; creates a private container using Entra sign-in.
az storage container create --account-name <account> --name <container> \
  --auth-mode login --public-access off
```

## Do's and Don'ts

Do use private containers by default, clear ownership/naming, scoped roles, and deliberate lifecycle rules. Don't put secrets in names/metadata or assume container deletion is reversible without protection.

## Real-life implementation

An internal application serves static assets from a private container using its managed identity. A separately governed account is used only if a public delivery requirement exists; a CDN/cache and anonymous access are then explicitly designed. The internal application's account never has to become public.

## Q&A

1. What should new data containers default to? **Private; anonymous access disabled.**
2. Are slash-separated names native directories in a flat namespace? **No.**
3. Does Contributor necessarily grant reading blobs? **No; assign an appropriate data-plane role.**
