# Externalize durable state and design database lifecycle independently from application-container lifecycle

## What

Externalizing state means application instances are replaceable while durable records live in a separately managed database, volume, object store, or platform service. Database lifecycle includes schema migration, backups, credentials, upgrade, failover, and recovery—not just starting a container.

## Why

State the tradeoff and assign operational ownership.

## How

Keep API processes stateless where possible, use explicit persistent storage for stateful components, and coordinate schema changes with application rollout compatibility. Define ownership, migration, readiness, and rollback boundaries. For a single-host deployment, model the database container and data volume as separate lifecycle units.

## Features

A volume protects against container replacement but not host loss.

## Code snippets (if any)

```bash
docker volume create db-data
```

## Do's and Don'ts

- **Do:** use a secret mechanism rather than literal credentials, test compatible migrations, and document state ownership and restore.
- **Don't:** store durable state in the app container layer or assume restart policy is a database lifecycle plan.

## Real-life implementation

Web replicas are replaced freely, while database upgrade and schema migration proceed through a compatible, rehearsed change with recoverable data.

## Q&A

- **Q: Does a volume make the database highly available?** No; it persists locally but does not itself provide replication or failover.
- **Q: Can an app rollback always reverse a migration?** No; design expand/contract migrations and verify data compatibility.
- **Q: What is a restart policy for?** Restart behavior after exit; it does not replace backup, repair, or recovery design.

**Docs:** [Docker](https://docs.docker.com/engine/storage/volumes/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
