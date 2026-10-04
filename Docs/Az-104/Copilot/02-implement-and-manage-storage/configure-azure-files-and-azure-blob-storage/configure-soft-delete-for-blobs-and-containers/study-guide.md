# Configure soft delete for blobs and containers

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Configure soft delete for blobs and containers](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [Blob soft delete](https://learn.microsoft.com/azure/storage/blobs/soft-delete-blob-overview)

## What

Blob soft delete retains deleted (and, where configured, overwritten) blobs for a retention window. Container soft delete retains deleted containers and their contents for a configured period. These controls help recover from mistakes but are distinct from versioning, snapshots, point-in-time restore, and backup.

## Why

Enable protections before production data arrives and set retention to match incident response. Retained deleted data consumes billable capacity until expiry. Combine controls according to risk: versioning for earlier object states, soft delete for deletion recovery, and independent backup/immutability for stronger recovery against privileged or malicious changes.

## How

In the portal or supported CLI/PowerShell, enable blob and container soft delete separately and set retention. Test deleting and recovering a blob and a container in a nonproduction account. Confirm interactions with versioning, lifecycle policy, backups, and account feature support; ensure operators know the recovery path.

## Features

- Blob soft delete and container soft delete address different deletion scopes and need separate configuration.
- Soft-deleted content remains billable for the retention period.
- Versioning and soft delete are complementary, not equivalent.
- Exam trap: soft delete is not immutable backup; waiting beyond retention or disabling protection can remove recovery options.

## Code snippets (if any)

No snippet required; use the portal or current Storage account CLI/PowerShell commands to configure the retention settings.

## Do's and Don'ts

Do enable each needed protection, choose a policy-based retention window, test undelete, and include retained data in cost reviews. Don't assume container protection automatically replaces blob protection or that a toggle alone proves recovery.

## Real-life implementation

Deployment mistakes sometimes remove the wrong assets. The architect enables blob and container soft delete for the incident response window, then tests restore procedures. Versioning covers overwrites, and a separately protected backup covers account-level compromise. Lifecycle policies are checked so they do not undermine approved retention.

## Q&A

1. What does container soft delete protect? **Deleted containers and their contents during retention.**
2. Does soft delete replace versioning? **No, they protect related but distinct recovery cases.**
3. What is the cost tradeoff? **Deleted data remains stored and billed during the retention period.**
