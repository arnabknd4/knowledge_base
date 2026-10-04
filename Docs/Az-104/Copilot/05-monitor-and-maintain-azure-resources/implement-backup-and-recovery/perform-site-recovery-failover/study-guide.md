# Perform a failover to a secondary region by using Site Recovery

## What

A Site Recovery failover activates replicated workloads at the recovery location. A planned failover is coordinated when the source is available; an unplanned failover is used when it is not. A test failover validates readiness without affecting production when isolated correctly. Reprotect and failback return protection or workloads toward the original location after recovery.

## Why

Failover is a business-impacting change, not simply a button press. Correct sequencing, data consistency, network readiness, access, and communication determine whether the service can safely resume and whether data loss stays within the RPO.

## How

Before a planned event, verify replication health, latest recovery point, capacity, recovery plan, target networking, identity, and approvals. Run a test failover periodically. For an actual failover, select the correct recovery point and plan, monitor job progress, validate each tier and user path, and update DNS/routing as designed. Commit the failover when validated. Reprotect the new primary direction and plan failback when the original region is ready.

## Features

- Test failover is for validation and must use an isolated network to avoid duplicate identities/IPs or production conflicts.
- Planned failover can synchronize data before switching; unplanned failover may incur data loss bounded by the available recovery point.
- Recovery plans sequence machines and can include manual steps; dependencies must be modeled accurately.
- Commit finalizes a selected recovery point for failover; reprotect/failback are distinct later actions.
- Exam trap: do not confuse test failover with planned/unplanned production failover, or assume replication is healthy without checking status.

## Code snippets (if any)

Snippet not required: failover is a controlled portal/ASR recovery-plan operation whose safe choice depends on incident state, recovery point, approvals, and dependencies. A generic command would conceal these essential decision points.

## Do's and Don'ts

- Do follow the approved incident runbook and select a recovery point based on RPO and corruption status.
- Do validate networking, application health, data integrity, security, and customer access before declaring recovery.
- Do communicate DNS/routing changes and keep an audit trail.
- Don't run an unplanned failover merely because a test failed; first establish outage scope and source status.
- Don't forget to reprotect after failover or to plan failback and resynchronization.

## Real-life implementation

During a regional outage, the incident commander confirms the source region is unavailable and authorizes unplanned failover. Operators choose the latest viable recovery point, execute the recovery plan, and bring up database before application tiers. They validate transactions in the recovery region, change traffic routing, and monitor service objectives. After the primary region is restored, they reprotect and schedule a controlled failback.

## Q&A

1. **When use planned failover?** When the source is available and can be gracefully synchronized before switching.
2. **What is a test failover for?** Readiness validation without disrupting production, using an isolated network.
3. **What can be lost during unplanned failover?** Changes after the selected/latest available recovery point, bounded by actual replication state.
4. **What comes after failover and recovery?** Reprotect in the new direction and perform failback when appropriate.

References: [Run a failover](https://learn.microsoft.com/azure/site-recovery/site-recovery-failover), [Test failover](https://learn.microsoft.com/azure/site-recovery/site-recovery-test-failover-to-azure), [Failback to primary region](https://learn.microsoft.com/azure/site-recovery/azure-to-azure-how-to-failback).

Syllabus: [copilot-az104-syllabus.md](../../../copilot-az104-syllabus.md).
