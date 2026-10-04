# Use read-only filesystems, no-new-privileges, resource limits, and network segmentation

## What
Runtime hardening combines a read-only root filesystem, privilege-escalation restrictions, resource ceilings, and restricted network paths where compatible with an application.

## Why
Layered constraints reduce persistence and lateral movement opportunities and protect shared hosts from runaway or unexpectedly exposed workloads.

## How
Inventory writable paths and use explicit tmpfs or named volumes for required writes. Set CPU and memory limits appropriate to observed demand, and restrict network membership and published ports.

## Features
Read-only root does not make mounted volumes read-only unless separately configured. Resource options and network features can differ by platform; resource limits are controls, not capacity planning.

## Code snippets (if any)
```console
docker run --rm --read-only --security-opt no-new-privileges --memory=256m busybox:1.36 sh -c 'echo hardened'
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A stateless API runs read-only with a bounded memory allocation and joins only its application network. A deliberate writable cache uses a size-limited temporary mount.

## Q&A
- **Q: Is containerization sufficient isolation?** No. Containers share a kernel; apply layered controls.
- **Q: Where should I start?** Limit daemon, runtime, image, mount, and network trust.
- **Q: How do I verify a control?** Inspect effective settings and test on the target host.

Source: [Official Docker documentation](https://docs.docker.com/engine/security/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
