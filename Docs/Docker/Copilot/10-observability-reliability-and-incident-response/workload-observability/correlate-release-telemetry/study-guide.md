# Correlate image digest, deployment version, instance, logs, metrics, and traces

**Domain:** Observability, reliability, and incident response<br>
**Syllabus objective:** [Correlate image digest, deployment version, instance, logs, metrics, and traces](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Operational signals should identify the instance and release that produced them. Correlation lets responders compare behavior across versions and separate rollout effects from host or dependency failure.

## Why
Mutable tags and short-lived container IDs are incomplete identities. Without stable release identity, logs, metrics, traces, and deploy events cannot be joined reliably.

## How
Attach service, environment, instance, deployment ID, and digest to deployment events and telemetry. Keep high-cardinality values in logs/traces rather than unlimited metric labels; retain mappings for replaced containers.

## Features
Docker inspect exposes image/container metadata; telemetry and deployment systems need to propagate digest and release identity.

## Code snippets (if any)
```sh
docker inspect --format "{{.Image}} {{.Name}}" api
```

## Do's and Don'ts
Do: preserve digest-to-deployment mappings. Don’t: use request/container IDs as unbounded metric dimensions or infer a release solely from mutable tag.

## Real-life implementation
During rollout, operators compare errors by digest, inspect matching traces/logs, and locate hosts still using previous or candidate image.

## Q&A
- **Q: Stable image identity?** Digest plus deployment and config revision.
- **Q: Should every value label metrics?** No; high-cardinality labels impair cost and usability.
- **Q: Why keep deployment events?** To correlate change timelines with symptoms.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/engine/reference/commandline/inspect/)
- [Docker documentation](https://docs.docker.com/engine/logging/)
