# Inspect client/server versions, server configuration, storage, runtimes, and active context using `docker version`, `docker info`, and `docker context`.

## What

The CLI communicates with a daemon selected through a Docker context; the server environment, not the command prompt, performs container operations. The build context is the files available to the builder; .dockerignore prevents needless transfer and accidental inclusion, but cannot erase secrets already committed in older layers.

## Why

Balance control against compatibility and maintenance effort to enable reliable operations.

## How

Capture client and server version, daemon info, and active context; compare server-side storage and runtime settings with the expected host.

## Features

Linux Engine normally uses the host Linux kernel. Docker Desktop on Windows and macOS provides a managed Linux environment for Linux containers; host integration and platform behavior can differ.

## Code snippets (if any)

```sh
docker version; docker info; docker context show
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Infer server health from the client version alone or share raw host details without sanitizing.

## Real-life implementation

Release automation names the target context and verifies the daemon endpoint before any destructive operation.

## Q&A

- **What is the key concept?** The CLI communicates with a daemon selected through a Docker context.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Infer server health from the client version alone or share raw host details without sanitizing.

**Official reference:** [Docker documentation](https://docs.docker.com/engine/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
