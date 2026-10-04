# Explain Linux namespaces and cgroups at a practical level; understand OCI image/runtime standards and the roles of Docker Engine, containerd, and OCI runtimes.

## What

Containers package user-space files and run isolated processes that share a host kernel; a VM runs a guest OS kernel, while managed runtimes shift more operations to a provider. Namespaces provide isolation views, cgroups account for and limit resources, and an OCI runtime such as runc creates the process; containerd commonly manages lifecycle but is not itself the OCI runtime.

## Why

Correctly mapping isolation and resource controls helps distinguish application faults from runtime and host limits.

## How

Run a disposable image, inspect its metadata, and compare the process and resource boundary with a VM or managed service. Record kernel, isolation, state, and operational ownership assumptions.

## Features

Namespaces isolate process views; cgroups account for and constrain resources. OCI defines portable interfaces; containerd manages lifecycle, while an OCI runtime creates processes.

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

Platform engineers inspect process isolation and configured resource limits on representative hosts before setting policy.

## Q&A

- **What is the key concept?** Containers package user-space files and run isolated processes that share a host kernel.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Claim that a container includes its own kernel or provides the same isolation boundary as a VM.

**Official reference:** [Docker documentation](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
