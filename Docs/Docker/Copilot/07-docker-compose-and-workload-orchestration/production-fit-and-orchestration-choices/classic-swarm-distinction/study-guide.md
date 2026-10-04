# Distinguish Swarm mode from Docker Classic Swarm

## What
Docker Swarm mode is integrated into Docker Engine. Docker Classic Swarm was a separate, legacy clustering project; similar naming does not imply identical architecture or lifecycle.

## Why
Confusing the two can lead to incorrect commands, obsolete tutorials, unsupported operational assumptions, or a migration plan aimed at the wrong platform.

## How
Identify the actual engine and orchestration components in inventory, use current Engine Swarm documentation for Swarm mode, and assess legacy deployments against their own support and migration requirements.

## Features
Swarm mode uses managers, workers, services, and tasks through Engine APIs. Classic Swarm used a separate orchestration approach. Do not infer that Classic Swarm is current or interchangeable.

## Code snippets (if any)
```console
docker info --format '{{.Swarm.LocalNodeState}}'
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
During an inherited-platform review, the team checks deployment manifests and daemon versions, labels the orchestrator accurately, and creates a migration plan before changing cluster control components.

## Q&A
- **Q: How do I validate it?** Render the model, then smoke-test the target implementation.
- **Q: What does Compose not provide?** Multi-host scheduling or cluster-level failover.
- **Q: How can I limit surprises?** Pin supported versions and rehearse failure and recovery.

Source: [Official Docker documentation](https://docs.docker.com/engine/swarm/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
