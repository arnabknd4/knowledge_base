# Distinguish Docker Engine on Linux from Docker Desktop environments on Windows and macOS, including the Linux VM boundary where applicable.

## What

The CLI communicates with a daemon selected through a Docker context; the server environment, not the command prompt, performs container operations. Do not assume Linux containers use the Windows or macOS kernel directly: Docker Desktop places a Linux environment between the host and Linux workloads.

## Why

Desktop simplifies local workflows, but its VM and host-integration boundary can differ from native Linux behavior.

## How

Check container mode, Docker Desktop resources, mounts, and architecture; reproduce kernel-dependent issues on a matching Linux target.

## Features

Linux Engine normally uses the host Linux kernel. Docker Desktop on Windows and macOS provides a managed Linux environment for Linux containers; host integration and platform behavior can differ.

## Code snippets (if any)

```sh
docker info --format "{{.OSType}}/{{.Architecture}}"
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Assume Linux containers use the macOS or Windows host kernel directly.

## Real-life implementation

Team setup guidance records container mode, resource limits, file sharing, and supported target architecture.

## Q&A

- **What is the key concept?** The CLI communicates with a daemon selected through a Docker context.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Assume Linux containers use the macOS or Windows host kernel directly.

**Official reference:** [Docker documentation](https://docs.docker.com/engine/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
