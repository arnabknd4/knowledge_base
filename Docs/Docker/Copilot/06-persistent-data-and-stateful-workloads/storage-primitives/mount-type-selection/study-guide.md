# Choose named volumes, anonymous volumes, bind mounts, tmpfs, or other supported mounts based on persistence, portability, performance, and access needs

## What

Named volumes are Docker-managed persistent stores; anonymous volumes lack a stable intentional name. Bind mounts expose a host path; tmpfs is memory-backed and disappears at stop. Other drivers are platform-specific.

## Why

State the tradeoff and assign operational ownership.

## How

Choose by lifecycle: named volumes for managed persistence, bind mounts for host-owned files or development source, tmpfs for temporary data. Validate permissions, backup, performance, and driver behavior on the target platform.

## Features

Mounts obscure image files at the target path.

## Code snippets (if any)

```bash
docker volume create app-data
docker run -d --name app --mount type=volume,src=app-data,dst=/var/lib/app nginx:alpine
```

## Do's and Don'ts

- **Do:** declare mount type, target, ownership, and lifecycle explicitly; keep host path access minimal.
- **Don't:** use tmpfs for data that must survive restart or assume a named local volume is portable or replicated.

## Real-life implementation

Development mounts source code read-write, a production database uses a managed named volume or storage service, and short-lived credentials can use tmpfs if the threat model and memory budget permit.

## Q&A

- **Q: Which mount survives container removal?** A named or anonymous volume persists independently, unless explicitly removed.
- **Q: When is a bind mount preferable?** When an intentional host path must be shared, such as source code or host-managed configuration.
- **Q: Is tmpfs encrypted or durable by default?** It is memory-backed and non-durable; security properties depend on host and platform controls.

**Docs:** [Docker](https://docs.docker.com/engine/storage/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
