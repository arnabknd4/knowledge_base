# Create and configure a file share in Azure Files

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Create and configure a file share in Azure Files](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [Create an Azure file share](https://learn.microsoft.com/azure/storage/files/storage-how-to-create-file-share)

## What

An Azure file share is a managed SMB or NFS file system hosted in a storage account. It supports shared file access and lift-and-shift workloads. Performance and billing depend on account/SKU and standard versus premium share model.

## Why

Choose Azure Files when a workload needs shared file-protocol access and file-system semantics. Decide between SMB and NFS based on client, identity, and application requirements; protocol support and authentication differ. Size capacity and performance against measured IOPS/throughput, and include snapshots, backup, redundancy, and transactions in total cost.

## How

Create the share in a supported account, set quota or provisioned capacity as applicable, choose protocol and security configuration, and configure network access. For SMB, prefer supported identity-based mounting and configure share-level RBAC plus NTFS ACLs. For NFS, validate network/security prerequisites and Unix permissions. Monitor utilization, latency, throttling, and protection status.

## Features

- SMB provides Windows-compatible semantics; NFS targets compatible Linux/Unix workloads with different configuration.
- Share capacity/performance billing depends on tier/model; check current regional support and pricing.
- Firewall, private DNS, and client connectivity affect mounting; a role assignment alone is insufficient.
- Exam trap: a file share is not a Blob container, and Blob hot/cool/archive tiers do not apply to Azure Files.

## Code snippets (if any)

```bash
# Placeholders: <resource-group>, <account>, <share>; verify supported account model.
az storage share-rm create --resource-group <resource-group> --storage-account <account> \
  --name <share> --quota 1024
```

## Do's and Don'ts

Do plan capacity and throughput, test identity and network access, and configure backup/snapshot retention. Don't distribute account keys to users or assume increasing quota alone raises performance for every model.

## Real-life implementation

A department application expects an SMB mapped drive. The architect selects a compatible account and identity model, sets a measured quota, and restricts connectivity to the corporate network. Group-level share authorization and folder ACLs provide separate departmental access, with capacity alerts and recovery tests before cutover.

## Q&A

1. When choose Azure Files over Blob? **When shared file-protocol access and filesystem semantics are required.**
2. What authorizes SMB access? **Share-level RBAC and NTFS ACLs, alongside identity and network prerequisites.**
3. Do Blob access tiers apply to Azure Files? **No.**
