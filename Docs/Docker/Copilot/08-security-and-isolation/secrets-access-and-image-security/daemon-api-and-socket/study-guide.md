# Restrict Docker socket access and secure remote Engine API access

## What
The Docker daemon API controls containers, images, networks, and mounts. Access to the Unix socket or an equivalent remote endpoint is effectively privileged host access.

## Why
A process that can ask the daemon to mount host paths or start privileged containers can often gain control comparable to the daemon's host authority.

## How
Limit socket ownership and group membership, avoid mounting the socket into ordinary application containers, and protect remote API endpoints with authenticated, encrypted transport and network restrictions.

## Features
Socket permissions are not a fine-grained container authorization boundary by themselves. Never expose an unauthenticated daemon API on a reachable network; treat proxy access as privileged unless proven otherwise.

## Code snippets (if any)
```console
docker context ls
docker info --format '{{.Name}}'
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A CI job no longer receives the host Docker socket; it submits builds to an isolated builder with scoped credentials. Remote Engine access is limited to approved operators over secured transport.

## Q&A
- **Q: Is containerization sufficient isolation?** No. Containers share a kernel; apply layered controls.
- **Q: Where should I start?** Limit daemon, runtime, image, mount, and network trust.
- **Q: How do I verify a control?** Inspect effective settings and test on the target host.

Source: [Official Docker documentation](https://docs.docker.com/engine/security/protect-access/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
