# Plan capacity, redundancy, failure domains, dependencies, and maintenance

**Domain:** Observability, reliability, and incident response<br>
**Syllabus objective:** [Plan capacity, redundancy, failure domains, dependencies, and maintenance](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Reliability spans application instances, hosts, storage, networks, registries, and dependencies. Capacity planning identifies demand, limits, headroom, scaling action, and maintenance constraints.

## Why
Containers on one host share a failure domain. CPU/memory limits do not create capacity; dependencies or a single host can defeat apparent redundancy.

## How
Map dependencies and failure domains, model peak and degraded load, reserve capacity for replacement and maintenance, and test multi-host recovery. Choose a platform that places replicas across independent domains.

## Features
Docker Engine runs containers; multi-host placement, traffic management, and service availability require broader orchestration. Resource limits are not capacity planning.

## Code snippets (if any)
```sh
Capacity review: peak demand + failure headroom + rollout surge; verify host, storage, and dependency limits.
```

## Do's and Don'ts
Do: test host loss and dependency failure in a controlled environment. Don’t: call multiple containers on one host HA or assume more replicas fix a shared bottleneck.

## Real-life implementation
Replicas span separate hosts/zones with capacity to survive a failure. Maintenance drains one domain while synthetic checks and SLOs verify impact.

## Q&A
- **Q: Do replicas on one host provide HA?** No; they share failure modes.
- **Q: What does a memory limit guarantee?** A bound, not available capacity or graceful recovery.
- **Q: Who owns dependency resilience?** The service architecture defines budgets, fallbacks, and escalation.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/engine/containers/resource_constraints/)
- [Docker documentation](https://docs.docker.com/engine/swarm/)
