# Configure snapshots and soft delete for Azure Files

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Configure snapshots and soft delete for Azure Files](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [Azure Files snapshots](https://learn.microsoft.com/azure/storage/files/storage-snapshots-files)

## What

An Azure Files share snapshot is a point-in-time, read-only view for recovering files or folders. Share soft delete retains a deleted share for a defined period. Azure Backup adds policy-based protection and vault recovery; these capabilities have different scope and operational models.

## Why

Use snapshots for granular point-in-time recovery and soft delete for accidental share deletion. Use Azure Backup where centralized policy, retention, or vault-based recovery is required. Snapshots consume incremental capacity as data changes. Same-account snapshots are not an isolated backup against account compromise.

## How

Enable share soft delete and set its retention. Create snapshots manually or through Azure Backup schedules. Test recovering a file and a deleted share; verify ACLs and application consistency. Monitor snapshot count and consumed capacity. Document how recovery works if the account itself is unavailable or deleted.

## Features

- Snapshots are generally incremental and represent a share state at a point in time.
- Soft delete protects a deleted share during retention; it does not recover overwritten file contents unless a snapshot/backup exists.
- Azure Backup supplies managed policy/vault workflows; validate retention and recovery requirements.
- Exam trap: snapshots and soft delete are complementary, not interchangeable; neither automatically guarantees application consistency.

## Code snippets (if any)

```powershell
# Placeholder context/share; inspect the account and use current Az.Storage/Azure Backup workflow.
Connect-AzAccount
$ctx = New-AzStorageContext -StorageAccountName <account> -UseConnectedAccount
Get-AzStorageShare -Context $ctx
```

## Do's and Don'ts

Do align snapshot frequency and retention to RPO, enable soft delete, and rehearse recovery. Don't treat an in-account snapshot as immutable/offsite backup or assume soft delete restores overwritten files.

## Real-life implementation

A file share has a two-hour RPO. Operations schedules snapshots at a matching interval, enables soft delete, and uses Azure Backup for centrally governed retention. A quarterly exercise restores one file and one deleted test share, checks ACLs, and records recovery time and incremental capacity cost.

## Q&A

1. Which control recovers a deleted share? **Share soft delete within its retention window.**
2. Which is appropriate for a prior file state? **A share snapshot or Azure Backup recovery point.**
3. Are same-account snapshots isolated from account compromise? **No.**
