# Patch the host kernel, Docker Engine, base images, and application dependencies

## What
Container security relies on a maintained host kernel, Docker Engine, base image, system packages, and application dependency set.

## Why
An image scan is only a point-in-time signal. Vulnerabilities can be introduced or disclosed later, and a patched image cannot compensate for a vulnerable host runtime.

## How
Track supported versions, monitor vendor advisories, rebuild from maintained base images, scan release artifacts, and deploy updates through a tested process. Verify the running digest after rollout.

## Features
Containers share the host kernel, so host patching remains essential. Rebuilding from a tag does not guarantee a new base unless the build process refreshes and verifies its inputs.

## Code snippets (if any)
```console
docker build --pull -t example/api:1.2 .
docker image inspect example/api:1.2
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A monthly maintenance pipeline rebuilds from current approved bases, reports changed package findings, stages the image, and rolls it out with health checks and a rollback path.

## Q&A
- **Q: Is containerization sufficient isolation?** No. Containers share a kernel; apply layered controls.
- **Q: Where should I start?** Limit daemon, runtime, image, mount, and network trust.
- **Q: How do I verify a control?** Inspect effective settings and test on the target host.

Source: [Official Docker documentation](https://docs.docker.com/build/building/best-practices/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
