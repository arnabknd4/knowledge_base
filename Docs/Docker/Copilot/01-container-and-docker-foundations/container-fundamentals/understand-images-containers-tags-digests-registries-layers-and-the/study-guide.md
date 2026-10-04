# Understand images, containers, tags, digests, registries, layers, and the writable container layer.

## What

Containers package user-space files and run isolated processes that share a host kernel; a VM runs a guest OS kernel, while managed runtimes shift more operations to a provider. A container writable layer is ephemeral and separate from image layers; use a volume or external data service for state that must survive replacement.

## Why

Readable tags simplify release operations, while digest pinning trades convenience for exact promotion and rollback identity.

## How

Run a disposable image, inspect its metadata, and compare the process and resource boundary with a VM or managed service. Record kernel, isolation, state, and operational ownership assumptions.

## Features

Linux namespaces isolate views and cgroups account for or constrain resources. OCI specifies image and runtime interfaces; Docker Engine, containerd, and an OCI runtime have distinct roles.

## Code snippets (if any)

```sh
docker run --rm --read-only --memory=256m alpine:3.21 uname -a
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Claim that a container includes its own kernel or provides the same isolation boundary as a VM.

## Real-life implementation

Release automation records a tag-to-digest mapping and promotes the verified digest through each environment.

## Q&A

- **What is the key concept?** Containers package user-space files and run isolated processes that share a host kernel.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Claim that a container includes its own kernel or provides the same isolation boundary as a VM.

**Official reference:** [Docker documentation](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
