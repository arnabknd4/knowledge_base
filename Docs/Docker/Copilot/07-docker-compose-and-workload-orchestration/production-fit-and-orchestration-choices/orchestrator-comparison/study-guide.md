# Compare Compose, Swarm, Kubernetes, and managed container platforms

## What
Compose, Swarm mode, Kubernetes, and managed container platforms address different operational scopes. Their tradeoffs include scale, ecosystem, availability, portability, and platform ownership.

## Why
Selecting a platform based on feature lists alone can add complexity without improving service outcomes, or leave availability and governance needs unmet.

## How
Compare workload placement, autoscaling needs, upgrade ownership, network and storage integrations, team expertise, support, and exit strategy. Validate the decision with an operational prototype and failure exercise.

## Features
Compose is principally single-host application definition and operation. Swarm is an Engine-integrated cluster orchestrator. Kubernetes has a broader ecosystem and operational model; managed offerings shift some control-plane duties but retain workload responsibilities.

## Code snippets (if any)
```console
docker compose version
docker info --format '{{.Swarm.LocalNodeState}}'
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A team with modest internal services selects an existing managed platform rather than building a new cluster, while preserving container image portability and testing platform-specific manifests separately.

## Q&A
- **Q: How do I validate it?** Render the model, then smoke-test the target implementation.
- **Q: What does Compose not provide?** Multi-host scheduling or cluster-level failover.
- **Q: How can I limit surprises?** Pin supported versions and rehearse failure and recovery.

Source: [Official Docker documentation](https://docs.docker.com/engine/swarm/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
