# Create an Azure Backup vault

## What

An Azure Backup vault (Backup vault) is a vault resource used by Azure Backup for supported workloads, including newer protection scenarios such as Azure Disks and other workload-specific offerings. It is distinct from the Recovery Services vault and has its own supported data stores, policies, and operational features.

## Why

Choosing the correct vault is a prerequisite for configuring supported protection. The vault centralizes policy and recovery-point management while enabling appropriate identity, network, redundancy, and security boundaries.

## How

Check that the workload and region support Backup vault protection. Create the vault in the intended subscription/resource group/region, configure redundancy and identity/network/security settings, and then create the workload-specific policy and assign data sources. Validate protection status and restore capability before claiming the workload is covered.

## Features

- Backup vault and Recovery Services vault have different supported data sources and capabilities; choose based on workload documentation.
- Backup vault policies configure workload-specific backup frequency and retention.
- Redundancy and cross-region options affect recovery choices and cost; confirm support for the selected workload.
- Access control and soft-delete/security capabilities protect recovery data; feature availability can differ by workload and vault type.
- Exam trap: a Backup vault is not a generic replacement for an RSV, and neither vault protects data until protection is configured.

## Code snippets (if any)

```bash
az dataprotection backup-vault create --resource-group "<resource-group>" --vault-name "<backup-vault>" --location "<azure-region>" --type SystemAssigned --storage-settings datastore-type="VaultStore" type="LocallyRedundant"
```

This creates a Backup vault using a system-assigned identity and locally redundant vault store. Confirm the Azure CLI `dataprotection` command and supported storage settings for the intended workload and region; configure security/network settings and a policy afterward.

## Do's and Don'ts

- Do confirm workload compatibility and supported regions before selecting a vault type.
- Do use least privilege and secure the vault from unauthorized deletion or policy changes.
- Do design redundancy based on regional recovery objectives and cost.
- Don't assume storage replication alone provides application-consistent recovery.
- Don't use CLI syntax from an older API/extension without checking current command help.

## Real-life implementation

For Azure Disk Backup, create a Backup vault in a supported region, choose the required storage redundancy, establish an identity and permissions for backup operations, and assign a disk backup policy. Monitor protection health and perform a restore test to a non-production disk, measuring restore time and validating access to the recovered data.

## Q&A

1. **Which vault type is required?** The type supported by the specific workload—do not infer from the product name alone.
2. **Can an RSV and Backup vault protect identical workloads interchangeably?** No; support and capabilities differ.
3. **What is the first operational proof of success?** The data source is protected under the intended policy and successful recovery points appear.
4. **Does vault creation by itself create recovery points?** No.

References: [Azure Backup vault overview](https://learn.microsoft.com/azure/backup/backup-vault-overview), [Create a Backup vault](https://learn.microsoft.com/azure/backup/backup-vault-create), [Azure Disk Backup overview](https://learn.microsoft.com/azure/backup/disk-backup-overview).

Syllabus: [copilot-az104-syllabus.md](../../../copilot-az104-syllabus.md).
