# Configure Azure Site Recovery for Azure resources

## What

Azure Site Recovery (ASR) is a disaster recovery service that replicates supported workloads to a recovery location and orchestrates failover and failback. For Azure-to-Azure disaster recovery, it replicates supported Azure VMs from a primary region to a secondary region using a Recovery Services vault.

## Why

ASR supports business continuity when a region or site is unavailable. It can reduce recovery time by maintaining replicated state and enabling planned, unplanned, and test failovers. It complements, but does not replace, backups and long-term point-in-time retention.

## How

Design source/target regions, network mapping, target VM size/storage, replication policy, capacity, access, and application dependencies. Create/configure the Recovery Services vault, enable replication for supported VMs, and monitor initial replication and health. Build recovery plans to sequence multi-tier applications and define test failover, failover, and failback procedures. Regularly run non-disruptive test failovers in an isolated network.

## Features

- Replication policy controls recovery-point objectives and retention within supported limits; crash-consistent and application-consistent recovery points have different guarantees.
- Recovery plans can group and sequence machines and include manual actions/scripts where supported.
- Test failover validates recovery without disrupting production when isolated correctly.
- Network mapping and target resource design determine whether a recovered VM is reachable and correctly secured.
- Exam trap: ASR replicates workload state for DR; Azure Backup supplies retained recovery points. Neither alone addresses every recovery need.

## Code snippets (if any)

Snippet not required: ASR onboarding is a multi-resource, workload-specific setup with region, network, policy, and capacity choices. Use the portal workflow for supported Azure VM replication and validate each prerequisite; do not reduce it to a single command in a study example.

## Do's and Don'ts

- Do calculate RPO/RTO and validate target-region quotas and service availability.
- Do map virtual networks/subnets and verify NSGs, DNS, identity, and dependencies in the recovery region.
- Do regularly test failover and keep recovery plans synchronized with production changes.
- Don't assume replication guarantees an application-consistent recovery point at every moment.
- Don't skip backup because ASR is configured; replication can copy corruption or deletion.

## Real-life implementation

For a three-tier application, replicate the database and application VMs to a paired/approved recovery region, preconfigure target networks and capacity, and create a recovery plan that starts data services before application and web tiers. Run test failovers with isolated addressing, validate transactions and monitoring, and document who approves a real failover and how DNS/users are redirected.

## Q&A

1. **What is ASR's primary purpose?** Disaster recovery through replication and orchestrated failover.
2. **Does ASR provide long-term backup retention?** No; use Azure Backup for backup and point-in-time retention.
3. **Why configure network mapping?** To attach recovered workloads to the intended target networks/subnets and support connectivity.
4. **What validates the plan without disrupting production?** A test failover using an isolated test network.

References: [Azure Site Recovery overview](https://learn.microsoft.com/azure/site-recovery/site-recovery-overview), [Azure-to-Azure disaster recovery](https://learn.microsoft.com/azure/site-recovery/azure-to-azure-tutorial-enable-replication), [Recovery plans](https://learn.microsoft.com/azure/site-recovery/recovery-plan-overview).

Syllabus: [copilot-az104-syllabus.md](../../../copilot-az104-syllabus.md).
