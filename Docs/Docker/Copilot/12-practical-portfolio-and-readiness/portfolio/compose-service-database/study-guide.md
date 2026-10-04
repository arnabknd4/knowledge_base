# Run a service and database with Compose

Portfolio exercise: Run an application and database with Compose using a private network, persistent named volume, health checks, and non-secret configuration.

## What

Assemble services with explicit discovery, health status, and persistent database storage.

## Why

The exercise clarifies readiness and state lifetime, avoiding data loss and secrets baked into images.

## How

Define app and DB services, private network, named volume, health check, and non-secret config. Start the stack, test service DNS, replace containers, and verify persistence.

## Features

Compose health is one signal, not guaranteed readiness or production observability.

## Code snippets (if any)

Outline: `services: app: ... db: ...`; mount `dbdata:/var/lib/database` and declare `volumes: dbdata:`. Verify health syntax and paths in Docker docs.

## Do's and Don'ts

DO use a disposable environment, state assumptions, capture evidence, and assign follow-up ownership. DON’T use production data or credentials, infer safety from one passing check, or leave temporary resources behind.

## Real-life implementation

Create an empty volume, write a harmless test record, replace the DB container, and verify health/persistence. Submit Compose config and cleanup instructions. This is practice, not official exam coverage.

## Q&A

- What survives replacement? Data deliberately stored in persistent storage.
- Does depends_on alone mean ready? No; readiness needs verification.
- Should DB port be published? Only if a host client needs it.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/compose/)
- [Official Docker documentation](https://docs.docker.com/engine/storage/volumes/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
