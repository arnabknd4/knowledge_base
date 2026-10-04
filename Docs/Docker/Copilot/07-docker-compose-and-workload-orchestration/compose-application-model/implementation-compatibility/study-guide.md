# Verify Compose implementation differences and feature support

## What
Compose is an application specification interpreted by implementations. The Docker Compose plugin and other implementations may differ in supported fields, lifecycle details, and integrations.

## Why
A YAML file that parses in one environment is not proof that its semantics match elsewhere. Compatibility checks catch surprises before CI, workstation, or deployment behavior diverges.

## How
Pin or document the supported Compose version, validate with the actual target CLI, and test important behavior rather than relying only on schema acceptance. Treat warnings and ignored fields as release blockers.

## Features
Compose V2 is the Docker CLI plugin invoked as `docker compose`; the legacy standalone `docker-compose` executable may have different version and support status. Platform capabilities such as secrets and deploy settings are context-specific.

## Code snippets (if any)
```console
docker compose version
docker compose config
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A team validates configuration with the same Docker Compose plugin version used by CI, then runs a smoke test on the deployment host. Unsupported optional fields are removed or handled outside Compose.

## Q&A
- **Q: How do I validate it?** Render the model, then smoke-test the target implementation.
- **Q: What does Compose not provide?** Multi-host scheduling or cluster-level failover.
- **Q: How can I limit surprises?** Pin supported versions and rehearse failure and recovery.

Source: [Official Docker documentation](https://docs.docker.com/compose/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
