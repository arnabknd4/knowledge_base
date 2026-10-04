# Explain containers as isolated processes that share the host operating-system kernel, and compare containers with virtual machines and managed/serverless runtimes.

## What

Containers package user-space files and run isolated processes that share a host kernel; a VM runs a guest OS kernel, while managed runtimes shift more operations to a provider. Separate immutable image content, runtime settings, writable container state, and persistent storage; this makes replacement, rollback, and ownership explicit.

## Why

Balance control against compatibility and maintenance effort to enable reliable operations.

## How

Run a disposable image, inspect its metadata, and compare the process and resource boundary with a VM or managed service. Record kernel, isolation, state, and operational ownership assumptions.

## Features

Linux namespaces isolate views and cgroups account for or constrain resources. OCI specifies image and runtime interfaces; Docker Engine, containerd, and an OCI runtime have distinct roles.

## Code snippets (if any)

No code snippet is needed for this objective.

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Claim that a container includes its own kernel or provides the same isolation boundary as a VM.

## Real-life implementation

Teams select a container, VM, or managed boundary from isolation and operating needs, then test on the target platform.

## Q&A

- **What is the key concept?** Containers package user-space files and run isolated processes that share a host kernel.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Claim that a container includes its own kernel or provides the same isolation boundary as a VM.

**Official reference:** [Docker documentation](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
