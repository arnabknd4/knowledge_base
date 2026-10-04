# Configure blob versioning

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Configure blob versioning](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [Blob versioning overview](https://learn.microsoft.com/azure/storage/blobs/versioning-overview)

## What

Blob versioning preserves prior blob states when a blob is modified or deleted, where supported. Each version has its own identifier and incurs storage cost. Versioning supports recovery and can be combined with soft delete and point-in-time restore where compatible.

## Why

Enable it when recovery from accidental overwrites justifies added capacity and lifecycle complexity. Versioning alone is not immutable backup: privileged users may delete versions, and compromise can affect the account. Check account compatibility, application behavior, object replication prerequisites, and cleanup policy before enabling.

## How

Enable versioning on the Blob service, test overwrite and delete behavior, and restore an earlier version using a supported portal, CLI, or SDK workflow. Add lifecycle rules to expire old versions according to business retention. Monitor version count/capacity and verify feature compatibility, especially with HNS and point-in-time restore.

## Features

- A write creates a new current version while retaining prior versions.
- Every retained version consumes capacity; lifecycle rules are needed to manage cost.
- Versioning is required for object replication and some recovery designs, but feature combinations have constraints.
- Exam trap: enabling versioning does not set retention or make versions tamper-proof; confirm HNS and feature support in current documentation.

## Code snippets (if any)

```bash
# Placeholder account; inspect current versioning state.
az storage account blob-service-properties show -g <resource-group> --account-name <account> \
  --query "isVersioningEnabled" -o tsv
```

Use current portal/CLI/API steps to enable it after confirming compatibility and lifecycle policy.

## Do's and Don'ts

Do pair versioning with lifecycle cleanup, test rollback, and monitor capacity/cost. Don't enable it without a retention strategy or assume deleting the current blob deletes every version.

## Real-life implementation

A document service occasionally overwrites source files incorrectly. Versioning lets operators restore the prior state, and lifecycle rules expire old versions after the approved recovery period. Legal records use an additional immutable-retention control rather than relying on versions alone.

## Q&A

1. What is retained after a blob overwrite? **A prior version with its own version ID.**
2. What cost can grow after enabling versioning? **Capacity used by retained versions.**
3. Is versioning immutable protection? **No; privileged actions can still affect versions.**
