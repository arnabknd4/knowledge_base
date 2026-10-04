# Apply seccomp and AppArmor or SELinux profiles where available

## What
Seccomp filters restrict system calls; AppArmor and SELinux can apply host security policies to processes. Availability and enforcement depend on the host kernel, distribution, Engine, and configuration.

## Why
These controls add defense in depth by limiting operations beyond ordinary user identity and namespace isolation. Misconfigured profiles can also break workloads or create a false assurance.

## How
Inspect active runtime defaults and host support, test workload behavior under the intended profile, and grant only necessary exceptions through reviewed policy. Monitor denials during rollout.

## Features
Do not assume every Docker environment has AppArmor or SELinux enabled, or that a Linux host setting applies identically through Docker Desktop. Avoid disabling protections without a reviewed reason.

## Code snippets (if any)
```console
docker run --rm --security-opt no-new-privileges nginx:alpine
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A service starts with the host-supported default profile. A required syscall denial is reproduced in staging, assessed for necessity, and addressed with a narrow policy change rather than blanket profile disabling.

## Q&A
- **Q: Is containerization sufficient isolation?** No. Containers share a kernel; apply layered controls.
- **Q: Where should I start?** Limit daemon, runtime, image, mount, and network trust.
- **Q: How do I verify a control?** Inspect effective settings and test on the target host.

Source: [Official Docker documentation](https://docs.docker.com/engine/security/seccomp/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
