# Manage virtual machine disks

## What
Operate OS and data managed disks: select disk type and size, attach/detach, resize, snapshot, encrypt, and plan performance and backup. Disk IOPS and throughput are bounded by disk tier and VM limits; the effective ceiling may be the lower of them.

## Why
Disk design affects application latency, durability, recovery, and cost. Separate data/log/temp roles only when it improves performance or recovery semantics. Choose availability and redundancy appropriate to the workload; snapshots are point-in-time copies, not a complete application-consistent backup strategy by themselves.

## How
Estimate capacity, IOPS, throughput, and burst behavior under peak load. Check supported disk/SKU combinations and encryption policy. Portal, CLI, or PowerShell can create and attach managed disks; resize requires guest partition/filesystem expansion where applicable. Before maintenance, back up and confirm application quiescence. Test restore and access controls. Monitor disk latency, queue depth, and throttling alongside guest metrics.

## Features
Managed disk tiers include Standard HDD/SSD and Premium SSD variants; Ultra Disk and Premium SSD v2 have specialized capabilities and limits. Snapshots and disk restore points support recovery workflows. Disk encryption uses platform-managed keys by default, with disk encryption sets for CMK scenarios. Ephemeral OS disks are local and have different persistence/recovery characteristics.

## Code snippets (if any)
```bash
az disk create --resource-group <resource-group> --name <disk-name> --size-gb <capacity-gb> --sku <disk-sku> --location <azure-region>
az vm disk attach --resource-group <resource-group> --vm-name <vm-name> --name <disk-name>
```
Use a test VM and ensure filesystem/application consistency before production changes.

## Do's and Don'ts
**Do** size for both disk and VM throughput ceilings and test restore. **Don't** treat a snapshot as equivalent to tested application-consistent backup, or detach a disk while writes are active.

## Real-life implementation
A transactional application separates database data and logs only after profiling I/O patterns. The team sets disk and VM performance limits, enables backup with an appropriate consistency point, encrypts under policy, and runs periodic restore drills to an isolated network.

## Q&A
1. **What controls effective IOPS?** The lesser of configured disk performance and the VM's aggregate/storage limits, with workload/queue behavior also relevant.
2. **Does an Azure disk snapshot include the running application's consistent state?** Not inherently; coordinate application quiescing or use a backup workflow providing the needed consistency.
3. **What is special about an ephemeral OS disk?** It uses VM-local storage and is not persistent like a managed OS disk; confirm workload suitability and recovery design.

**References:** [Managed disks overview](https://learn.microsoft.com/azure/virtual-machines/managed-disks-overview) · [Managed disk types](https://learn.microsoft.com/azure/virtual-machines/disks-types)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#create-and-configure-virtual-machines)
