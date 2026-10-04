# Configure object replication

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Configure object replication](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [Object replication overview](https://learn.microsoft.com/azure/storage/blobs/object-replication-overview)

## What

Blob object replication asynchronously copies selected block blobs between source and destination storage accounts. Rules can select containers and filter by prefix or blob index tags. This distributes data; it is not synchronous mirroring or an account failover mechanism.

## Why

Use it for regional read distribution or a controlled secondary copy when asynchronous lag is acceptable. Consider residency, destination protection, consistency, recovery objectives, and storage/transaction costs. Maintain an independent backup or retention design: replication can propagate unwanted changes and is not point-in-time recovery.

## How

Enable Blob versioning on source and destination and change feed on the source, verify account/feature compatibility, then configure a replication policy and rules. Scope rules narrowly, test new/updated blobs and tags, and monitor replication status and failures. Account for initial backfill behavior and validate supported blob types/features against current documentation.

## Features

- Replication is asynchronous; there is no universal fixed completion time.
- Versioning on both accounts and source change feed are prerequisites.
- Only supported blob types and account configurations replicate; check HNS and other feature constraints.
- Exam trap: replication does not automatically provide backup or make all deletes behave like a protected point-in-time copy.

## Code snippets (if any)

```bash
# Placeholder account; verify prerequisites before creating replication policies.
az storage account blob-service-properties show -g <resource-group> --account-name <account> \
  --query "{versioning:isVersioningEnabled,changeFeed:changeFeed.enabled}" -o json
```

Use the current portal/CLI/REST Learn procedure for policy creation and validate rule scope.

## Do's and Don'ts

Do test create/update/delete and tag behavior, monitor lag, secure destination access, and estimate transaction/capacity costs. Don't assume all blob features replicate or source deletion is harmless.

## Real-life implementation

A media platform serves immutable assets near two user regions. Selected block blobs replicate to a regional destination for local reads. Backlog alerts detect lag; destination lifecycle rules control cost. An independent backup protects against malicious or mistaken source changes that replication may copy.

## Q&A

1. Is object replication synchronous? **No, it is asynchronous.**
2. Name its key data-protection prerequisites. **Versioning on both accounts and change feed on the source.**
3. Is it equivalent to backup? **No; maintain an independent recovery design.**
