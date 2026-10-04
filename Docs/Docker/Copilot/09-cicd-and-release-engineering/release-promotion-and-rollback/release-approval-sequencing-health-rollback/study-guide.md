# Define approvals, policy checks, sequencing, health validation, and rollback criteria

**Domain:** CI/CD and release engineering<br>
**Syllabus objective:** [Define approvals, policy checks, sequencing, health validation, and rollback criteria](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Specify approvers, required checks, rollout order, validation signals, and stop/rollback conditions before release.

## Why
Without clear gates and thresholds, teams either promote risky changes or hesitate during failure. Container health alone does not prove user-visible service quality.

## How
Gate on verified artifact evidence, scan/policy results, approval, and readiness. Roll out progressively; compare error rate, latency, saturation, and business availability to defined thresholds.

## Features
Docker health status is container metadata, not a deployment controller or service SLO. Automation must implement sequencing and rollback decisions.

## Code snippets (if any)
```sh
Gate: verified digest + policy pass + approval; observe service SLO; halt rollout when agreed thresholds breach.
```

## Do's and Don'ts
Do: define owners and abort criteria. Don’t: equate healthy with safe release or automatically roll back a transient signal without impact analysis.

## Real-life implementation
Deploy to a small traffic slice, observe service indicators and dependencies, then expand. A breached threshold stops rollout and pages the release owner.

## Q&A
- **Q: Who sets rollback criteria?** Service owners and SRE define thresholds beforehand.
- **Q: Is a Docker health check enough?** No; measure readiness and user outcomes.
- **Q: What if telemetry fails?** Halt expansion and follow incident procedures.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/engine/containers/healthcheck/)
- [Docker documentation](https://docs.docker.com/build/ci/)
