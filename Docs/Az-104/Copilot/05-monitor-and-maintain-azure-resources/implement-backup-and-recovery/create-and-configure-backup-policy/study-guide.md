# Create and configure a backup policy

## What

An Azure Backup policy defines when protected data is backed up and how long recovery points are retained. Policy structure and options depend on vault type and workload: for example, Azure VM policies differ from Azure Files, disks, and SQL/SAP workload policies.

## Why

The policy operationalizes RPO and retention requirements. It determines how much data loss is tolerable, how far back recovery is possible, and the ongoing storage/transaction cost. An overly short schedule can miss the required RPO; excessive retention can create unnecessary cost.

## How

Translate business objectives into backup frequency, retention tiers, and application-consistency requirements. Select the right policy type for the workload and vault, set schedules and retention for daily/weekly/monthly/yearly recovery points as supported, then assign it to data sources. Check policy limits, backup windows, time zones, and resource eligibility. Run an initial backup and monitor subsequent jobs.

## Features

- Azure VM Backup offers policy types/options such as standard or enhanced for supported scenarios; schedules, instant restore retention, and long-term retention vary.
- Policies can be changed, but changes may affect future recovery points and costs; determine how updates apply to existing items.
- Application-consistent recovery depends on supported workload integration and healthy guest components; crash-consistent points are not equivalent.
- Retention controls recovery-point lifecycle, not the organization's complete archive strategy.
- Exam trap: backup frequency drives RPO; retention determines how far back a restore can go. These are separate requirements.

## Code snippets (if any)

Snippet not required: policy creation is workload- and vault-specific, with different parameters and supported schedules. For the exam, be able to map stated RPO/retention requirements to the appropriate policy settings and validate them in the portal or workload-specific CLI/PowerShell cmdlets.

## Do's and Don'ts

- Do define RPO, RTO, retention, consistency, and regulatory needs before creating policy.
- Do estimate protected-instance and storage costs, including long-term retention and geo-redundancy.
- Do assign policies explicitly and verify all intended data sources are protected.
- Don't assume a daily schedule meets an hourly RPO.
- Don't confuse backup retention with operational snapshots or Site Recovery replication.

## Real-life implementation

For a tier-1 VM with a four-hour RPO and year-long compliance retention, first confirm the supported policy can meet the required frequency. Configure frequent recovery points and the required longer-term retention tiers, then test application-consistent recovery and cross-region options. For lower-tier workloads, use less frequent backups and shorter retention if business approval permits.

## Q&A

1. **What sets RPO in a backup plan?** Primarily the permitted interval between successful recovery points, bounded by schedule and job reliability.
2. **What sets how far back a restore can go?** Retention rules and available recovery points.
3. **Does changing a policy rewrite existing backups?** No; effects depend on policy and workload behavior, so assess current documentation and recovery-point implications.
4. **Does replication replace backup retention?** No; replication supports continuity/failover, while backup provides retained point-in-time recovery.

References: [Azure Backup policies](https://learn.microsoft.com/azure/backup/backup-azure-backup-policy-understand), [VM backup policy overview](https://learn.microsoft.com/azure/backup/backup-azure-vms-introduction), [Azure Backup pricing](https://azure.microsoft.com/pricing/details/backup/).

Syllabus: [copilot-az104-syllabus.md](../../../copilot-az104-syllabus.md).
