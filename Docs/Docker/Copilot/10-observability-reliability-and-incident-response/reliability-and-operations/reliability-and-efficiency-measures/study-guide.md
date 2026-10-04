# Measure deployment success, recovery time, failure rate, resource efficiency, and operational toil

**Domain:** Observability, reliability, and incident response<br>
**Syllabus objective:** [Measure deployment success, recovery time, failure rate, resource efficiency, and operational toil](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Measures should describe service outcomes and delivery effort: deployment success, change failure, time to restore, SLO attainment, resource efficiency, and recurring toil.

## Why
A single metric creates perverse incentives: speed without safety, low CPU from overprovisioning, or recovery estimates that ignore user impact and data integrity.

## How
Define each measure, denominator, window, source, owner, and target. Segment by service/release and interpret alongside reliability, cost, and quality; use trends to prioritize improvements rather than rank people.

## Features
Container resource metrics support efficiency analysis; deployment events and user telemetry measure delivery and outcomes. Separate leading indicators from lagging incident measures.

## Code snippets (if any)
```sh
Review dashboard: SLO/error budget, deploy and rollback rate, time-to-restore, resource cost per workload unit, recurring toil.
```

## Do's and Don'ts
Do: pair efficiency with service quality and headroom. Don’t: optimize one utilization percentage or penalize responders for reporting incidents.

## Real-life implementation
A platform review finds low cost but frequent rollbacks. The team improves artifact verification and staged rollout instead of further host consolidation.

## Q&A
- **Q: How measure restore time?** From user-impact start to verified recovery under consistent definitions.
- **Q: Is CPU alone efficiency?** No; relate resources to throughput, SLO, and headroom.
- **Q: Why track toil?** To identify automation and reliability improvements.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/engine/containers/runmetrics/)
- [Docker documentation](https://docs.docker.com/engine/containers/resource_constraints/)
