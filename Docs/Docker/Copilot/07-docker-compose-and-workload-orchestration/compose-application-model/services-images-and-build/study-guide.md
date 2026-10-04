# Model services, images/builds, networks, volumes, configs, secrets, and dependencies

## What
Compose YAML models an application as services, each using an image or build context, with optional networks, volumes, configs, secrets, health checks, and dependencies.

## Why
Describing these relationships makes startup reproducible, clarifies connectivity and state, and gives teams one reviewed application model rather than ad hoc commands.

## How
Declare each component under `services`; attach only required networks and mounts. Use named volumes for durable state, configs for non-sensitive settings, and the target's supported secret mechanism for credentials. Keep secret files out of source control.

## Features
Service names resolve on shared Compose networks, while named volumes survive container replacement. Config, secret, health, and dependency behavior varies by implementation and deployment context; never infer readiness from declaration alone.

## Code snippets (if any)
```yaml
services:
  api:
    build: ./api
    networks: [app]
    depends_on: [db]
  db:
    image: postgres:16
    networks: [app]
    volumes: [db-data:/var/lib/postgresql/data]
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets: [db_password]
networks:
  app:
volumes:
  db-data:
secrets:
  db_password:
    file: ./secrets/db_password.txt
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A developer stack connects an API and database, persists database data in a named volume, and uses non-sensitive config. CI validates the Compose implementation before tests.

## Q&A
- **Q: How do I validate it?** Render the model, then smoke-test the target implementation.
- **Q: What does Compose not provide?** Multi-host scheduling or cluster-level failover.
- **Q: How can I limit surprises?** Pin supported versions and rehearse failure and recovery.

Source: [Official Docker documentation](https://docs.docker.com/compose/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
