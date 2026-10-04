# Emit application logs to stdout/stderr or a configured system and collect centrally

**Domain:** Observability, reliability, and incident response<br>
**Syllabus objective:** [Emit application logs to stdout/stderr or a configured system and collect centrally](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Containers should emit structured application logs to stdout/stderr for collection by a runtime logging driver or explicitly configured agent. Keep application policy separate from container lifecycle.

## Why
Central collection enables cross-instance investigation and retention. Logs only in a writable container layer can disappear on replacement and are hard to search.

## How
Standardize timestamp, severity, service, instance, deployment, and correlation fields. Choose a supported driver or agent, test delivery/backpressure, and grant responders least-privilege access.

## Features
Docker Engine supports multiple logging drivers and options. Delivery mode and local buffering affect loss, latency, and disk use; select for workload needs.

## Code snippets (if any)
```sh
docker run --log-driver local --name api registry.example/api@sha256:VERIFIED_DIGEST
```

## Do's and Don'ts
Do: define collection path and monitor ingestion failures. Don’t: keep important logs only in ephemeral containers or log credentials, tokens, or unnecessary personal data.

## Real-life implementation
A service emits JSON on stdout; a host-managed collector forwards with bounded retention. Responders filter by service, instance, digest, and correlation ID.

## Q&A
- **Q: Does stdout mean centralized?** No; configure a collector or logging driver.
- **Q: Can logs be lost?** Yes; understand buffering, delivery, disk, and destination outages.
- **Q: Should secrets be logged?** Never; redact sensitive fields at source and collector.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/engine/logging/)
- [Docker documentation](https://docs.docker.com/engine/logging/configure/)
- [Docker documentation](https://docs.docker.com/engine/logging/drivers/)
