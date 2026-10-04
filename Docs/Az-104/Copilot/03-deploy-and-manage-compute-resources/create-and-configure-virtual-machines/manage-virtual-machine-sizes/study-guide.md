# Manage virtual machine sizes

## What
Select or change a VM SKU to match CPU, memory, local storage, network throughput, accelerator, and disk-performance requirements. Size families optimize different workload profiles; regional and zonal availability and current quota constrain choices.

## Why
Right-sizing controls performance and cost while preserving headroom and service availability. An undersized VM creates saturation; oversizing wastes spend. A resize can require restart or deallocation, and changing family may constrain extensions, accelerated networking, ephemeral OS disk, or host encryption.

## How
Measure utilization and application latency, then compare candidate SKU specifications and price in the target region. Check subscription vCPU quota and family quota, zone availability, disk/network limits, and feature compatibility. Portal's **Size** blade, `az vm list-sizes`, and PowerShell size queries show candidates; stop/deallocate if required, resize, then verify boot, networking, storage, and workload performance. For fleet workloads use scale sets/autoscale instead of manually resizing each node.

## Features
General purpose, compute optimized, memory optimized, storage optimized, GPU, and HPC families represent trade-offs, not interchangeable capacity. Accelerated networking and premium storage support vary by SKU. Reservations and savings plans may lower eligible compute costs but can reduce flexibility; validate sustained demand and scope before commitment.

## Code snippets (if any)
```bash
az vm list-sizes --location <azure-region> --output table
az vm resize --resource-group <resource-group> --name <vm-name> --size <target-vm-size>
```
Check compatibility and maintenance impact before resizing production.

## Do's and Don'ts
**Do** benchmark using representative load and check quota. **Don't** assume a size exists in every zone or that resize is interruption-free.

## Real-life implementation
For a latency-sensitive database VM, measure CPU, memory pressure, disk IOPS/throughput, and network ceilings together. Change one bottleneck at a time in a maintenance window, compare service-level indicators, and keep a tested rollback size.

## Q&A
1. **Does more vCPU always improve performance?** No; memory, storage, network limits, licensing, and application parallelism may be bottlenecks.
2. **Why is a size shown in a region unavailable for a zonal VM?** SKU/zone capacity and feature compatibility differ; check the selected zone and current quota.
3. **Does resizing always require deallocation?** Not always, but some transitions require restart/deallocation; plan for possible downtime.

**References:** [VM sizes overview](https://learn.microsoft.com/azure/virtual-machines/sizes/overview) · [Resize a VM](https://learn.microsoft.com/azure/virtual-machines/sizes/resize-vm)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#create-and-configure-virtual-machines)
