# Know the differences among development workstation, CI builder, single-host runtime, and clustered/container-platform environments.

## What

The CLI communicates with a daemon selected through a Docker context; the server environment, not the command prompt, performs container operations. Separate immutable image content, runtime settings, writable container state, and persistent storage; this makes replacement, rollback, and ownership explicit.

## Why

Balance control against compatibility and maintenance effort to enable reliable operations.

## How

Use a disposable workload, inspect the selected daemon and image identity, change one controlled variable, and verify both normal behavior and recovery. Record the exact artifact and runtime settings.

## Features

Linux Engine normally uses the host Linux kernel. Docker Desktop on Windows and macOS provides a managed Linux environment for Linux containers; host integration and platform behavior can differ.

## Code snippets (if any)

```sh
docker image inspect alpine:3.21 --format "{{.Id}}"; docker run --rm alpine:3.21 echo ready
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Patch a production container manually or assume mutable names and local state are reliable recovery records.

## Real-life implementation

CI builds and verifies the artifact once, promotes it unchanged, and keeps an exercised recovery path.

## Q&A

- **What is the key concept?** The CLI communicates with a daemon selected through a Docker context.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Patch a production container manually or assume mutable names and local state are reliable recovery records.

**Official reference:** [Docker documentation](https://docs.docker.com/engine/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
