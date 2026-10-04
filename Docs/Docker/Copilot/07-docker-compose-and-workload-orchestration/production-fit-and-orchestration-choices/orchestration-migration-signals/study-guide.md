# Recognize when a workload has outgrown single-host Compose

## What
A move beyond Compose is warranted when the service requires multi-host scheduling, automated placement, higher availability, coordinated scaling, or platform controls unavailable in the current setup.

## Why
Migration at the right point avoids both premature platform complexity and a brittle single-host design that cannot meet recovery objectives.

## How
Measure availability targets, deployment frequency, recovery time, resource contention, operator burden, and stateful dependencies. Select a supported orchestrator or managed service, then migrate incrementally with rollback and data plans.

## Features
Adding replicas on one Compose host does not remove the host failure domain. Moving containers does not automatically migrate durable data, networking policy, secrets, or monitoring.

## Code snippets (if any)
```console
docker compose ps
docker compose logs --tail=100
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A service's recovery objective falls below what manual host replacement can meet. The team prototypes a managed platform, validates storage and health behavior, and performs a staged traffic cutover.

## Q&A
- **Q: How do I validate it?** Render the model, then smoke-test the target implementation.
- **Q: What does Compose not provide?** Multi-host scheduling or cluster-level failover.
- **Q: How can I limit surprises?** Pin supported versions and rehearse failure and recovery.

Source: [Official Docker documentation](https://docs.docker.com/compose/production/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
