# Pull, inspect, tag, run, stop, start, restart, remove, and list containers and images.

## What

Docker CLI lifecycle and diagnostic commands act on images, containers, or daemon state; knowing which object a command affects is essential for safe operations. Tags can move, including latest, which has no inherent freshness or stability guarantee. Deploy by digest when exact artifact identity is required.

## Why

Readable tags simplify release operations, while digest pinning trades convenience for exact promotion and rollback identity.

## How

Practice against a disposable image: pull and inspect, run with a name, stop/start/restart, list, remove the container, then remove an unused image.

## Features

A container is a process with configuration and a writable layer, not a VM. Logs, events, stats, and inspect provide different evidence; no single view is a full monitoring system.

## Code snippets (if any)

```sh
docker pull alpine:3.21; docker run --name demo alpine:3.21 echo ready; docker ps -a; docker rm demo
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Use broad removal commands on a production context without confirming the target.

## Real-life implementation

Release automation records a tag-to-digest mapping and promotes the verified digest through each environment.

## Q&A

- **What is the key concept?** Docker CLI lifecycle and diagnostic commands act on images, containers, or daemon state.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Use broad removal commands on a production context without confirming the target.

**Official reference:** [Docker documentation](https://docs.docker.com/reference/cli/docker/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
