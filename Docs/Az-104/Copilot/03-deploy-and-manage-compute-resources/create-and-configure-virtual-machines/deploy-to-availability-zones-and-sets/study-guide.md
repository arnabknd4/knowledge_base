# Deploy virtual machines to availability zones and sets

## What
Availability zones place resources in physically separate datacenter locations within a region; availability sets distribute VMs across fault and update domains within a datacenter. They are alternative VM availability constructs with different failure boundaries.

## Why
Match redundancy to SLA and failure model. Zones protect against a datacenter/zone outage when the application has instances and dependencies across zones. Sets reduce correlated host/rack and planned-maintenance impact within a datacenter but do not provide zone-level separation. Consider latency, replication, data consistency, capacity, and cross-zone network/egress cost.

## How
Verify the region and VM SKU support zones; choose zone at provisioning and deploy redundant instances in separate zones. Configure load balancing, health probes, zone-resilient storage/data, and recovery. For availability sets, assign related VMs to one set at creation; Azure distributes them across fault/update domains. Portal and IaC expose placement settings. Validate actual application failover rather than relying on placement alone.

## Features
Fault domains represent shared power/network/physical boundaries; update domains define planned maintenance groups. Azure controls domain assignment limits. Availability sets and zones are not interchangeable and cannot always be changed after creation. Zone-redundant services and zonal resources have distinct behavior; check each dependency's resilience.

## Code snippets (if any)
```bash
az vm create --resource-group <resource-group> --name <vm-name> --image <image-reference> --size <zone-supported-size> --zone <zone-number> --vnet-name <vnet-name> --subnet <subnet-name> --admin-username <admin-user> --authentication-type ssh --ssh-key-values <path-to-public-key>
```
Use a non-production resource group for experimentation and configure the application to run multiple instances.

## Do's and Don'ts
**Do** place independent application instances and data dependencies across the selected fault boundary. **Don't** assume two VMs in one zone/set meet regional disaster recovery objectives.

## Real-life implementation
For a two-tier service requiring zone resilience, deploy stateless front ends across zones behind a zone-redundant load balancer, and choose a data tier with compatible replication/consistency. Test losing one zone and check capacity and cost in the remaining zones.

## Q&A
1. **Which option protects against a zone outage?** Availability zones, provided the workload and dependencies are distributed and the region supports zones.
2. **What do update domains do?** They group VMs for planned maintenance sequencing; they are not separate regions or a backup.
3. **Does availability-set placement distribute applications automatically?** No. It distributes VMs across fault/update domains; you still configure application load balancing and health.

**References:** [Availability options for virtual machines](https://learn.microsoft.com/azure/virtual-machines/availability) · [Availability sets](https://learn.microsoft.com/azure/virtual-machines/availability-set-overview)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#create-and-configure-virtual-machines)
