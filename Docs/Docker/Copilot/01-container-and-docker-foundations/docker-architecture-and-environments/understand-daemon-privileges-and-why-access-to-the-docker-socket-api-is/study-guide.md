# Understand daemon privileges and why access to the Docker socket/API is highly privileged.

## What

The CLI communicates with a daemon selected through a Docker context; the server environment, not the command prompt, performs container operations. Docker socket/API access is highly privileged because its controller can request host-connected containers; rootless mode reduces some risks but does not make arbitrary clients trustworthy.

## Why

Daemon access can cross the container boundary, so convenience must be balanced against host compromise and trust.

## How

Restrict socket permissions and API reachability, audit trusted clients, and prefer isolated builders or narrowly scoped automation.

## Features

Linux Engine normally uses the host Linux kernel. Docker Desktop on Windows and macOS provides a managed Linux environment for Linux containers; host integration and platform behavior can differ.

## Code snippets (if any)

```sh
docker info --format "{{.Name}}"
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Mount the production Docker socket into an untrusted workload or expose an unauthenticated daemon.

## Real-life implementation

A platform team isolates builders, restricts daemon access, and audits every identity allowed to control the host.

## Q&A

- **What is the key concept?** The CLI communicates with a daemon selected through a Docker context.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Mount the production Docker socket into an untrusted workload or expose an unauthenticated daemon.

**Official reference:** [Docker documentation](https://docs.docker.com/engine/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
