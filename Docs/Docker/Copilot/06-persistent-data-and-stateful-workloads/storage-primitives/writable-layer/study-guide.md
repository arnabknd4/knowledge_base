# Explain the container writable layer and why it is not durable application storage

## What

A container's writable layer sits above immutable image layers and records runtime filesystem changes. It belongs to that container instance, is not a backup, and is removed with the container. Replacing a container from an image does not restore data written only into that layer.

## Why

State the tradeoff and assign operational ownership.

## How

Treat the layer as scratch space for process-local changes. Put durable data in a volume or deliberate bind mount, and define its backup, ownership, and lifecycle independently. Recreate containers during routine upgrades in a test environment to prove required state survives.

## Features

Copy-on-write behavior can add overhead and layer growth.

## Code snippets (if any)

```bash
docker run --rm --name disposable nginx:alpine sh -c 'echo runtime-data >/tmp/state; cat /tmp/state'
```

## Do's and Don'ts

- **Do:** keep only reconstructible or ephemeral data in the writable layer and test container replacement.
- **Don't:** rely on container stop/start as durability or include runtime data in an image by committing containers.

## Real-life implementation

A stateless API container is replaced during deployment; user uploads persist in an externalized volume or object store, not its layer.

## Q&A

- **Q: What happens to the writable layer on container removal?** It is removed with that container unless data was separately persisted.
- **Q: Does the image contain runtime writes?** No; image layers are the template and the container layer holds its changes.
- **Q: What proves state is externalized?** Replace the container and verify required data remains available through its mount or service.

**Docs:** [Docker](https://docs.docker.com/engine/storage/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
