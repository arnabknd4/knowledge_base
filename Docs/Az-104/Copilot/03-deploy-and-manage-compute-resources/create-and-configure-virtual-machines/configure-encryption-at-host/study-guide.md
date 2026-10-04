# Configure encryption at host for Azure virtual machines

## What
Encryption at host protects VM host-cached data and data flows between compute and storage, in addition to encryption applied to managed disks. It is a host-level encryption setting, not a substitute for disk encryption, guest security, or key governance.

## Why
Select it when policy requires protection of data at rest on host caches or end-to-end encryption boundaries. Confirm supported VM size/region and disk configuration; encryption settings can constrain resizing and deployment. Consider performance and operational impact, plus customer-managed key (CMK) lifecycle and recovery responsibilities when applicable.

## How
Check subscription registration and regional/SKU support, then enable encryption at host on a supported VM or scale set. In portal, inspect the disk/encryption options during create or VM configuration. CLI/PowerShell and IaC can set the property at creation; existing deployments may require a stop/deallocate or redeployment path depending on support and configuration. Validate boot, data-disk attach, backup, and restore paths before broad rollout.

## Features
Host encryption complements platform-managed encryption of managed disks. Disk encryption sets can provide CMK control for supported managed disks; Azure Disk Encryption operates inside the guest and has different prerequisites and management. Understand which layer satisfies a requirement. CMK brings key version, permissions, rotation, availability, and recovery dependencies.

## Code snippets (if any)
```bash
az vm create --resource-group <resource-group> --name <vm-name> --image <image-reference> --size <supported-vm-size> --encryption-at-host
```
Confirm CLI/API support and VM compatibility first; use a non-production test. No keys or secrets belong in the command.

## Do's and Don'ts
**Do** map the control to data-at-rest requirements and test backup/restore. **Don't** confuse encryption at host with guest disk encryption or assume every VM size and region supports it.

## Real-life implementation
A regulated workload uses supported host encryption and managed disks encrypted per the organization's key policy. The operations design monitors key availability, limits key permissions, and proves recovery from backup if a key or disk becomes unavailable.

## Q&A
1. **Does encryption at host replace managed-disk encryption?** No. It adds host-level protection; the layers are complementary.
2. **Is Azure Disk Encryption the same feature?** No. ADE encrypts within the guest; host encryption is applied at the Azure host boundary.
3. **Can a VM always be resized after enabling it?** No. Only compatible sizes/configurations are usable; verify support before choosing a target.

**References:** [End-to-end encryption using encryption at host](https://learn.microsoft.com/azure/virtual-machines/disk-encryption) · [Encryption at host overview](https://learn.microsoft.com/azure/virtual-machines/disks-enable-host-based-encryption-portal)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#create-and-configure-virtual-machines)
