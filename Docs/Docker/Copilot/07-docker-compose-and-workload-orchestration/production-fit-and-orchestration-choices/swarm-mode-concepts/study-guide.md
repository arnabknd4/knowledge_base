# Operate Swarm services, tasks, placement, updates, networking, and secrets

## What
Swarm mode is Docker Engine's cluster orchestrator. Managers maintain cluster state; workers run tasks; services declare desired state including replicas and placement.

## Why
Swarm can reconcile tasks, distribute replicas, and support rolling updates and rollback, but adds control-plane, networking, storage, and operational responsibilities.

## How
Follow an approved node join procedure, define replicas and placement constraints, set update and rollback behavior, and monitor service state. Plan overlay networks, configs, secret access, and manager quorum.

## Features
A service is desired workload state; tasks are scheduled instances. Swarm overlay networks span nodes, and Swarm secrets are granted to services. This is distinct from legacy Docker Classic Swarm.

## Code snippets (if any)
```console
docker service create --name web --replicas 3 nginx:alpine
docker service ls
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A team deploys stateless API replicas across workers with a controlled rolling update and rollback policy. Only the consuming service receives its Swarm secret; operators monitor manager quorum and node health.

## Q&A
- **Q: How do I validate it?** Render the model, then smoke-test the target implementation.
- **Q: What does Compose not provide?** Multi-host scheduling or cluster-level failover.
- **Q: How can I limit surprises?** Pin supported versions and rehearse failure and recovery.

Source: [Official Docker documentation](https://docs.docker.com/engine/swarm/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
