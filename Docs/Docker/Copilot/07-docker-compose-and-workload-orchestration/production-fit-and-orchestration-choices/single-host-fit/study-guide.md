# Choose Compose for single-host, development, and CI workloads

## What
Compose defines and operates a multi-container application on a Docker host, making it useful for local development, suitable CI jobs, and intentionally single-host deployments.

## Why
Its compact operational model is valuable when a workload does not need cluster scheduling. A single host remains a failure domain, so simplicity must not be mistaken for high availability.

## How
Confirm that host capacity, restart policy, data protection, port exposure, and recovery objectives meet the workload requirements. Automate backups and test restoring on a replacement host.

## Features
Compose does not provide multi-host placement, distributed service discovery, or cluster-level failover. Docker Desktop may run Engine in a VM; understand where the host boundary and persistent data actually reside.

## Code snippets (if any)
```console
docker compose up -d
docker compose ps
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A small internal tool with a tested restore procedure runs on one managed host. The owner documents host recovery time and migrates when availability or placement requirements exceed that design.

## Q&A
- **Q: How do I validate it?** Render the model, then smoke-test the target implementation.
- **Q: What does Compose not provide?** Multi-host scheduling or cluster-level failover.
- **Q: How can I limit surprises?** Pin supported versions and rehearse failure and recovery.

Source: [Official Docker documentation](https://docs.docker.com/compose/production/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
