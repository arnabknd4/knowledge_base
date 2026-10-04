# Create a virtual machine

## What
Provision a compute instance with an image, size, disks, network interfaces, OS configuration, identity, and lifecycle settings. Azure manages the physical host; you remain responsible for guest OS configuration, patching strategy, application operations, and access unless a managed service takes over.

## Why
VMs provide OS-level control for legacy, specialized, or lift-and-shift workloads. Architects balance image compatibility, CPU/memory, disk IOPS, zone/region support, licensing, availability, and predictable cost against the increased operational burden relative to PaaS.

## How
In portal, choose a trusted image and size, region/zone, OS-disk type, VNet/subnet, and administrator access. Prefer Entra ID/managed access and Bastion or just-in-time controls over a public management port. Enable monitoring, backup, patch policy, and managed identity as needed. With CLI, specify every material choice instead of accepting ambiguous defaults; verify quota and SKU availability before rollout.

## Features
Managed disks, VM extensions, managed identities, trusted launch options, accelerated networking (supported SKUs), boot diagnostics, and Azure Monitor integrations support operations. Availability zones, availability sets, and scale sets address different redundancy patterns. VM size families and disk tiers affect regional availability and costs; deallocation can stop compute billing but storage/network resources may continue billing.

## Code snippets (if any)
```bash
az vm create --resource-group <resource-group> --name <vm-name> --image <publisher:offer:sku:version> --size <vm-size> --vnet-name <vnet-name> --subnet <subnet-name> --admin-username <admin-user> --authentication-type ssh --ssh-key-values <path-to-public-key>
```
Use an approved image and a public key file; do not open management ports to the internet by default.

## Do's and Don'ts
**Do** right-size and design recovery before production. **Don't** use shared local admin credentials, expose SSH/RDP publicly without a strong compensating control, or assume VM creation configures application HA.

## Real-life implementation
A migrated line-of-business server lands in a private subnet with managed disk, managed identity, zone-aware placement where supported, backup policy, patch schedule, diagnostics, and Bastion access. Validate application licensing, data consistency, and restore testing before cutover.

## Q&A
1. **Does stopping the VM stop every charge?** No. Compute may stop when deallocated; disks and other attached resources can still incur costs.
2. **Is a VM in a zone automatically application-resilient?** No. The application and its dependencies need a multi-instance design and tested failover.
3. **Can you change every VM size in place?** No. Available sizes depend on region, hardware, quotas, and attached features; resizing can require restart/deallocation.

**References:** [Create a Linux VM with Azure CLI](https://learn.microsoft.com/azure/virtual-machines/linux/quick-create-cli) · [VM sizes](https://learn.microsoft.com/azure/virtual-machines/sizes/overview)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#create-and-configure-virtual-machines)
