# Design restart and replacement behavior without confusing it with recovery or high availability

**Domain:** Observability, reliability, and incident response<br>
**Syllabus objective:** [Design restart and replacement behavior without confusing it with recovery or high availability](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Restart policies can restart a stopped container under configured conditions. They do not diagnose state, repair data, restore lost hosts, rebalance traffic, or ensure another instance serves users.

## Why
Automatic restart can hide crash loops, amplify overload, or repeat deterministic failure. Availability also needs capacity, dependency behavior, routing, and recovery beyond one process.

## How
Choose restart policy deliberately, detect crash loops, and document replacement. Use orchestrated replicas, readiness-aware routing, redundancy, and tested state recovery for continuity.

## Features
Docker restart policies govern container behavior and differ from health checks, host recovery, rescheduling, and application failover.

## Code snippets (if any)
```sh
docker run --restart unless-stopped --name api registry.example/api@sha256:VERIFIED_DIGEST
```

## Do's and Don'ts
Do: alert on repeated restarts and investigate exit cause. Don’t: use restart policy as HA, backup, or replacement strategy.

## Real-life implementation
A platform reschedules failed instances across hosts and routes only to ready replicas. Operators preserve crash evidence and prevent restart loops from hiding a bad release.

## Q&A
- **Q: Does restart policy restart unhealthy containers?** Health alone does not trigger it.
- **Q: Does it survive host loss?** No; another control plane or operator must replace it.
- **Q: When useful?** Recoverable exits with safe initialization and observable behavior.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/engine/containers/start-containers-automatically/)
- [Docker documentation](https://docs.docker.com/engine/containers/healthcheck/)
