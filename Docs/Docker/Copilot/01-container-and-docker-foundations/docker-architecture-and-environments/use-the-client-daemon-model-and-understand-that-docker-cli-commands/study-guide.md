# Use the client/daemon model and understand that Docker CLI commands operate against a selected Docker context/daemon.

## What

The CLI communicates with a daemon selected through a Docker context; the server environment, not the command prompt, performs container operations. The build context is the files available to the builder; .dockerignore prevents needless transfer and accidental inclusion, but cannot erase secrets already committed in older layers.

## Why

Balance control against compatibility and maintenance effort to enable reliable operations.

## How

Check the active context and endpoint before mutations; use an explicit context in automation and verify the daemon target.

## Features

Linux Engine normally uses the host Linux kernel. Docker Desktop on Windows and macOS provides a managed Linux environment for Linux containers; host integration and platform behavior can differ.

## Code snippets (if any)

```sh
docker context show; docker context ls
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Assume CLI commands always affect the local machine.

## Real-life implementation

Release automation names the target context and verifies the daemon endpoint before any destructive operation.

## Q&A

- **What is the key concept?** The CLI communicates with a daemon selected through a Docker context.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Assume CLI commands always affect the local machine.

**Official reference:** [Docker documentation](https://docs.docker.com/engine/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
