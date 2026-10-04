# Use non-root processes, rootless mode, and user namespace remapping appropriately

## What
A non-root container process reduces in-container privilege. Rootless mode runs the daemon and containers without host root; user namespace remapping maps container identities to different host IDs.

## Why
These controls reduce consequences of some container breakouts and accidental writes, but do not provide identical behavior or remove the need for kernel and daemon patching.

## How
Set the image's runtime user where possible. Evaluate rootless mode or daemon user namespace remapping against storage, networking, port, device, and operational requirements; test the actual host configuration.

## Features
Rootless mode changes daemon privilege and some resource/network behavior. User namespace remapping changes UID/GID mappings for containers while the daemon can remain root. Neither is simply a synonym for non-root application execution.

## Code snippets (if any)
```console
docker run --rm --user 10001:10001 busybox:1.36 id
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A web service runs as an unprivileged UID in the image. The platform team separately trials rootless Engine for suitable developer workloads and documents port, volume ownership, and monitoring differences.

## Q&A
- **Q: Is containerization sufficient isolation?** No. Containers share a kernel; apply layered controls.
- **Q: Where should I start?** Limit daemon, runtime, image, mount, and network trust.
- **Q: How do I verify a control?** Inspect effective settings and test on the target host.

Source: [Official Docker documentation](https://docs.docker.com/engine/security/rootless/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
