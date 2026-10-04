# Create a Recovery Services vault

## What

A Recovery Services vault is an Azure resource that stores recovery points and manages protection for supported workloads, including Azure VM Backup and several hybrid backup scenarios. It is also used to manage Azure Site Recovery for supported replication scenarios. A vault is a management and security boundary; protected data is stored according to the selected backup/replication configuration.

## Why

The vault provides a centralized place to define protection, retention, access, and recovery operations. Architect the vault around workload ownership, regional recovery strategy, security separation, and restore requirements rather than creating one indiscriminately for every resource.

## How

Select subscription, resource group, and a supported region. Plan vault redundancy (LRS/GRS, where supported and required), soft delete and security settings, private access/network requirements, RBAC, and monitoring. Create the vault, configure its protection/replication settings, and validate restore procedures. Vault configuration choices can be difficult or impossible to change after protected items or data are present; verify current constraints first.

## Features

- The vault is associated with a region; recovery topology and supported workload features vary by region.
- Backup storage redundancy and cross-region restore availability affect resilience and cost.
- Soft delete and multi-user authorization/security features help protect against accidental or malicious deletion; configure them in line with recovery security requirements.
- A vault supports specific backup workloads and Site Recovery scenarios; it is not interchangeable with an Azure Backup vault.
- Exam trap: a vault by itself does not protect anything. Enable backup/replication and assign a policy.

## Code snippets (if any)

```powershell
$vault = New-AzRecoveryServicesVault -Name "<vault-name>" -ResourceGroupName "<resource-group>" -Location "<azure-region>"
Set-AzRecoveryServicesVaultContext -Vault $vault
```

Run after connecting with an appropriately privileged Az account and selecting the intended subscription. Configure redundancy and security settings before onboarding workloads.

## Do's and Don'ts

- Do design vault boundaries for least privilege, workload ownership, and recovery operations.
- Do check supported regions, redundancy options, immutability/security controls, and change restrictions.
- Do test recovery access independently of ordinary production administrator credentials.
- Don't assume deleting a protected source deletes recovery data safely or that the vault is disposable.
- Don't onboard production workloads before validating retention, network, and security configuration.

## Real-life implementation

An enterprise may use a dedicated production recovery vault per region or operational boundary, with backup administrators separated from workload operators. Choose geo-redundancy and cross-region restore where the recovery objective requires regional survivability, accepting additional storage cost. Restrict destructive operations and exercise a restore in an isolated network.

## Q&A

1. **What is a Recovery Services vault used for?** Supported backup workloads and Site Recovery management.
2. **Does creating a vault enable protection automatically?** No; configure a policy and enable backup or replication for the workload.
3. **Why decide redundancy before onboarding?** Some vault/storage choices are constrained after use and directly affect resilience and cost.
4. **Is an Azure Backup vault the same resource type?** No; it is a separate vault type for supported newer workloads.

References: [Recovery Services vault overview](https://learn.microsoft.com/azure/backup/backup-azure-recovery-services-vault-overview), [Vault storage settings](https://learn.microsoft.com/azure/backup/backup-create-recovery-services-vault), [Site Recovery overview](https://learn.microsoft.com/azure/site-recovery/site-recovery-overview).

Syllabus: [copilot-az104-syllabus.md](../../../copilot-az104-syllabus.md).
