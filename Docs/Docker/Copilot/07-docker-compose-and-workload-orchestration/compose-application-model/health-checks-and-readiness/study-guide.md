# Use health checks and readiness-aware dependency behavior

## What
A health check reports a container-level condition; readiness is the application's ability to serve a particular request. Compose can gate startup on dependency health when supported.

## Why
Startup ordering alone cannot prevent connection races. Explicit readiness behavior improves recovery and makes failed dependencies visible, while application retry logic handles later outages.

## How
Define a health check that tests the service's actual readiness without excessive load. Use long-form `depends_on` with `service_healthy` where supported, and have clients retry with bounded backoff.

## Features
Short-form `depends_on` guarantees creation order, not readiness. Health checks are not an end-to-end availability test; a service can become unhealthy after dependents start.

## Code snippets (if any)
```yaml
services:
  db:
    image: postgres:16
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 3s
      retries: 5
  api:
    image: example/api:1.0
    depends_on:
      db:
        condition: service_healthy
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A test API waits for the database readiness check before initial creation, then retries failed connections during the test. Monitoring separately checks a user-facing endpoint rather than trusting container health alone.

## Q&A
- **Q: How do I validate it?** Render the model, then smoke-test the target implementation.
- **Q: What does Compose not provide?** Multi-host scheduling or cluster-level failover.
- **Q: How can I limit surprises?** Pin supported versions and rehearse failure and recovery.

Source: [Official Docker documentation](https://docs.docker.com/compose/how-tos/startup-order/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
