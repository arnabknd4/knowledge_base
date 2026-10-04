# Separate development, test, and deployment settings safely

## What
Compose supports configuration layering and variable interpolation so the same service image can run with environment-specific non-secret settings.

## Why
Separating deployment settings from image contents avoids rebuilding for every environment and reduces accidental drift between development, test, and production.

## How
Keep a shared base file, use narrowly scoped overrides or environment-specific inputs, and validate the merged model with `docker compose config`. Store secrets in the target runtime's dedicated secret facility.

## Features
Do not put credentials in image layers, `ARG`, `ENV`, committed env files, or rendered logs. Compose env files and interpolation are configuration conveniences, not secret management.

## Code snippets (if any)
```console
docker compose -f compose.yaml -f compose.test.yaml config
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A test override points to a disposable database and enables diagnostics; a deployment override selects the production service endpoint. CI checks each resolved model and uses no real production secret values.

## Q&A
- **Q: How do I validate it?** Render the model, then smoke-test the target implementation.
- **Q: What does Compose not provide?** Multi-host scheduling or cluster-level failover.
- **Q: How can I limit surprises?** Pin supported versions and rehearse failure and recovery.

Source: [Official Docker documentation](https://docs.docker.com/compose/how-tos/multiple-compose-files/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
