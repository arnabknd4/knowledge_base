# Define health checks and distinguish process health, service readiness, and user-visible availability

**Domain:** Observability, reliability, and incident response<br>
**Syllabus objective:** [Define health checks and distinguish process health, service readiness, and user-visible availability](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
A container health check tests a narrow condition. Liveness asks whether a process should continue; readiness asks if it can serve traffic; availability asks whether users complete service operations successfully.

## Why
Conflating states can route traffic to an unready service, restart a live process during a transient dependency issue, or label a service available despite failed requests.

## How
Define checks with timeout, interval, retries, and clear action. Keep liveness local and cheap; readiness checks required initialization/dependencies; measure availability through request outcomes or external probes.

## Features
Docker health is metadata; it does not itself route traffic, remove an instance, or provide an application-level SLO. The platform must consume the signal.

## Code snippets (if any)
```sh
HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD ["/app/healthcheck"]
```

## Do's and Don'ts
Do: document what each check proves and who acts. Don’t: make liveness depend on every downstream service or equate healthy container with end-to-end availability.

## Real-life implementation
A web service has local liveness and readiness that stays false until initialization completes. An external synthetic probe validates an actual user transaction.

## Q&A
- **Q: Does Docker health restart a container?** Not by itself; health and restart policies differ.
- **Q: Can health represent readiness?** Yes, if routing consumes it explicitly.
- **Q: What proves availability?** Successful user operations measured against an objective.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/engine/containers/healthcheck/)
- [Docker documentation](https://docs.docker.com/compose/how-tos/startup-order/)
