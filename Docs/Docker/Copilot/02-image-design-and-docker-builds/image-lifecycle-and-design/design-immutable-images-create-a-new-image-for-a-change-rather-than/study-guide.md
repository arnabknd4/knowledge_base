# Design immutable images: create a new image for a change rather than patching a running container.

## What

An immutable-image workflow creates a new artifact for a change and replaces containers from that artifact instead of patching running instances. Separate immutable image content, runtime settings, writable container state, and persistent storage; this makes replacement, rollback, and ownership explicit.

## Why

Balance control against compatibility and maintenance effort to enable reliable operations.

## How

Build and test a new image, record its digest, deploy a replacement, verify readiness, then retire the old instance after the rollback window.

## Features

Runtime configuration and persistent state remain separate from the image; immutable artifact identity does not make all runtime state immutable.

## Code snippets (if any)

```sh
docker image inspect alpine:3.21 --format "{{.Id}}"
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Patch production binaries inside a running container.

## Real-life implementation

CI builds and verifies the artifact once, promotes it unchanged, and keeps an exercised recovery path.

## Q&A

- **What is the key concept?** An immutable-image workflow creates a new artifact for a change and replaces containers from that artifact instead of patching running instances.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Patch production binaries inside a running container.

**Official reference:** [Docker documentation](https://docs.docker.com/build/building/best-practices/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
