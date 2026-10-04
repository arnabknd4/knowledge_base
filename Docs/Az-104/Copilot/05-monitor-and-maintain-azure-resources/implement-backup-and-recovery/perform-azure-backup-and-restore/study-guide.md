# Perform backup and restore operations by using Azure Backup

## What

Azure Backup protects supported Azure and hybrid workloads through scheduled or on-demand recovery points. Restore operations recover data, disks, files, or workloads using a selected recovery point and workload-specific restore mode.

## Why

Backup protects against deletion, corruption, ransomware, and operator error, complementing redundancy and replication. Recovery is only proven when operators can locate a valid point, restore it securely, validate the workload, and meet the RTO.

## How

Enable protection with the correct vault and policy, run the initial backup, and monitor job status. For recovery, choose the protected item, recovery point, and restore mode; select a safe target/location/network and validate permissions and dependencies. For VM recovery, options can include creating a VM, restoring disks, or replacing disks, depending on scenario. Record the recovery point and outcome, then re-protect recovered resources as appropriate.

## Features

- Azure Backup supports workload-specific restore paths; do not assume every workload has the same granularity or restore options.
- Azure VM restores can offer file recovery, disk restore, or VM restore workflows, subject to the backup scenario.
- Soft delete, immutability, multi-user authorization, and role separation can reduce ransomware/destructive-operation risk.
- Cross-region restore depends on vault redundancy and supported configuration; restore target constraints and charges apply.
- Exam trap: successful backup job is not a recovery test, and a restore is not necessarily an in-place operation.

## Code snippets (if any)

```bash
az backup protection enable-for-vm --resource-group "<resource-group>" --vault-name "<recovery-services-vault>" --vm "<vm-name>" --policy-name "<backup-policy>"
```

After ensuring a compatible policy exists and the vault is selected correctly, this enables VM protection. Check job state with Azure Backup job commands; use the portal or workload-specific restore commands for the required recovery mode.

## Do's and Don'ts

- Do monitor failed/skipped jobs and verify recovery points meet the policy's RPO.
- Do conduct isolated restore drills and measure actual RTO, including application validation.
- Do restrict who can stop protection, delete backup data, or alter retention.
- Don't restore over production until the target and impact are understood.
- Don't treat storage redundancy, snapshots, or a green job indicator as a complete recovery strategy.

## Real-life implementation

For a deleted production VM, locate the latest valid recovery point, restore disks or create a new VM in a controlled network, and validate OS, application, identity, and data consistency. Confirm DNS/routing and security controls before redirecting users. Preserve the original evidence and communicate recovery status; enable backup on the restored resource if it is a replacement.

## Q&A

1. **What should happen before relying on backup?** Confirm successful jobs and perform a restore test.
2. **Why restore to an isolated network?** To validate safely and prevent a recovered, potentially vulnerable system from impacting production.
3. **Does enabling protection instantly create a usable recovery point?** It starts protection; an initial backup job must complete.
4. **What complements backup against malicious deletion?** Strong vault security, soft delete/immutability where supported, and separation of duties.

References: [Back up Azure VMs](https://learn.microsoft.com/azure/backup/backup-azure-arm-vms-prepare), [Restore Azure VMs](https://learn.microsoft.com/azure/backup/backup-azure-arm-restore-vms), [Azure Backup security features](https://learn.microsoft.com/azure/backup/security-overview).

Syllabus: [copilot-az104-syllabus.md](../../../copilot-az104-syllabus.md).
