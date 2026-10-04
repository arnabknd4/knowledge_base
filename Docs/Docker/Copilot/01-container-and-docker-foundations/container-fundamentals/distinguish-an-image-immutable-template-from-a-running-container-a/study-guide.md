# Distinguish an image (immutable template) from a running container (a process with runtime configuration and a writable layer).

## What

Containers package user-space files and run isolated processes that share a host kernel; a VM runs a guest OS kernel, while managed runtimes shift more operations to a provider. The image is the immutable template; a running container is a process with runtime configuration and its own writable layer.

## Why

Separating ephemeral container writes from durable storage makes replacement safer but requires an explicit persistence design.

## How

Inspect the image, create a disposable instance with explicit runtime settings, compare image and container inspect data, then remove the instance.

## Features

Linux namespaces isolate views and cgroups account for or constrain resources. OCI specifies image and runtime interfaces; Docker Engine, containerd, and an OCI runtime have distinct roles.

## Code snippets (if any)

```sh
docker run -d --name demo alpine:3.21 sleep 60; docker inspect demo --format "{{.Config.Image}} {{.State.Status}}"; docker rm -f demo
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Treat the container writable layer as image content or durable storage.

## Real-life implementation

Teams select a container, VM, or managed boundary from isolation and operating needs, then test on the target platform.

## Q&A

- **What is the key concept?** Containers package user-space files and run isolated processes that share a host kernel.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Treat the container writable layer as image content or durable storage.

**Official reference:** [Docker documentation](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
