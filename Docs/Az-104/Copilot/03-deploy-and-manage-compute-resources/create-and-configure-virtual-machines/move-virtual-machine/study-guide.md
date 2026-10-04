# Move a virtual machine

## What
Relocate an Azure VM and its dependent resources to another resource group, subscription, or region. These are distinct operations: resource-group/subscription moves keep resources in place; regional migration is a redeployment/replication workflow.

## Why
Moves support ownership, billing, organization, or residency changes. Dependency and provider constraints matter: NICs, disks, public IPs, availability constructs, extensions, and resource locks can affect eligibility. A region move requires data transfer, downtime/failover planning, and revalidation of capacity, IP, zone, and service support.

## How
For RG/subscription move, use portal **Move** or `az resource move`/resource-group move workflows after reviewing supported types, dependencies, locks, and permissions. Validate destination RBAC, policy, subscription registration, and quota. A move can lock source/destination resources during the operation and may not be reversible immediately. For region migration, build target resources from IaC or use Azure Site Recovery/backup-and-restore as appropriate; test application consistency, network/DNS changes, and rollback.

## Features
Resource moves do not change region and can change resource IDs. Cross-subscription moves can affect RBAC assignments and managed identities; review role scopes, Key Vault access, monitoring, backup, and automation references afterward. Regional migration can use replication and planned failover but has separate RPO/RTO and licensing implications.

## Code snippets (if any)
No snippet required: move eligibility is resource/dependency-specific. Use the portal move validation or Azure CLI's supported resource move command only after reviewing Microsoft's current move-support matrix.

## Do's and Don'ts
**Do** inventory dependencies and test in advance. **Don't** describe a resource-group move as a region migration, or assume resource IDs and external references remain unchanged.

## Real-life implementation
To reorganize subscriptions, inventory VM, NIC, disks, diagnostics, identity, and backup dependencies, validate a small move, then update automation and RBAC references. To change region, create target network and capacity, replicate data, test failover, then execute a controlled cutover.

## Q&A
1. **Does moving a VM to another resource group move it to a new region?** No; regional relocation is a separate migration.
2. **What is a common post-move failure?** A reference tied to the old resource ID or scope, such as a role assignment, monitoring rule, or automation parameter.
3. **Can every resource move across subscriptions?** No. Support depends on type, dependency set, and source/destination constraints.

**References:** [Move resources to a new resource group or subscription](https://learn.microsoft.com/azure/azure-resource-manager/management/move-resource-group-and-subscription) · [Move Azure VMs between regions](https://learn.microsoft.com/azure/azure-resource-manager/management/move-region)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#create-and-configure-virtual-machines)
