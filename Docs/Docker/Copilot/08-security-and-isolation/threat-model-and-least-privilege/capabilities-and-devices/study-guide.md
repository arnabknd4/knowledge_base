# Minimize Linux capabilities and device access; avoid privileged mode

## What
Linux capabilities split some root powers into individually grantable permissions. Device mappings expose host devices, while `--privileged` broadly relaxes container isolation.

## Why
Excess authority increases the impact of a compromised process. Narrow grants reduce the path from application compromise to host or neighboring workload impact.

## How
Run without privileged mode, identify the exact kernel operation required, and grant only the documented capability or device. Review the resulting configuration and remove temporary exceptions.

## Features
`--privileged` grants broad access and disables important confinement. Capabilities and device access are Linux-specific and effective behavior depends on Engine and host support.

## Code snippets (if any)
```console
docker run --rm --cap-drop=ALL --cap-add=NET_BIND_SERVICE busybox:1.36 httpd -f -p 80
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A diagnostic agent needs a particular device but not unrestricted host access. The operator tests the smallest device mapping and capability set in staging, then records the risk and expiry of any exception.

## Q&A
- **Q: Is containerization sufficient isolation?** No. Containers share a kernel; apply layered controls.
- **Q: Where should I start?** Limit daemon, runtime, image, mount, and network trust.
- **Q: How do I verify a control?** Inspect effective settings and test on the target host.

Source: [Official Docker documentation](https://docs.docker.com/engine/containers/run/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
