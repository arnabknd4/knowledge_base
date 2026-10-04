# Understand Swarm mutual TLS and secrets without assuming standalone Docker support

## What
Swarm mode uses mutual TLS for node identity and encrypted control traffic; its secrets mechanism securely provides data to authorized Swarm services.

## Why
These cluster features protect communication and service credentials in a Swarm deployment, but similar-looking standalone Docker workflows do not automatically inherit them.

## How
Use documented Swarm join and rotation procedures, restrict manager access, grant secrets only to consuming services, and verify storage, backup, and recovery behavior for the cluster.

## Features
Swarm secrets are mounted into authorized service tasks and managed by the Swarm control plane. They are not a generic standalone Engine secret store, and they do not remove the need to secure the host.

## Code snippets (if any)
```console
docker secret ls
docker service ls
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A Swarm deployment rotates a database credential by creating a new secret, updating the service, verifying health, and removing the old secret after the transition succeeds.

## Q&A
- **Q: Is containerization sufficient isolation?** No. Containers share a kernel; apply layered controls.
- **Q: Where should I start?** Limit daemon, runtime, image, mount, and network trust.
- **Q: How do I verify a control?** Inspect effective settings and test on the target host.

Source: [Official Docker documentation](https://docs.docker.com/engine/swarm/secrets/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
