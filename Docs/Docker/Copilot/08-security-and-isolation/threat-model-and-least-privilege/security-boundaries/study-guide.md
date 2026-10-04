# Identify Docker security boundaries and trust relationships

## What
A Docker threat model includes the host kernel, daemon and API/socket, images and registries, runtime settings, mounts, credentials, and network paths.

## Why
Containers share the host kernel, and the daemon can create processes and mounts with host-level consequences. Security depends on controlling each boundary, not only scanning application code.

## How
Document who can control the daemon, which images are trusted, what host paths are mounted, which credentials are available, and which networks are reachable. Assign controls and owners to each trust boundary.

## Features
Docker socket access can grant effective host-level control. A mounted host path may expose sensitive files. Isolation is layered and does not turn an untrusted image into a safe workload.

## Code snippets (if any)
```console
docker inspect --format '{{.HostConfig.Binds}}' my-container
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A review finds a build helper mounted to the Docker socket. The team removes that access, uses a constrained build service, and audits image provenance and mount requirements.

## Q&A
- **Q: Is containerization sufficient isolation?** No. Containers share a kernel; apply layered controls.
- **Q: Where should I start?** Limit daemon, runtime, image, mount, and network trust.
- **Q: How do I verify a control?** Inspect effective settings and test on the target host.

Source: [Official Docker documentation](https://docs.docker.com/engine/security/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
