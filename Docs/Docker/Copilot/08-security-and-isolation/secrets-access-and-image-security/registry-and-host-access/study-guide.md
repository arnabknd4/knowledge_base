# Apply least-privilege registry and host access controls and rotate credentials

## What
Registry credentials authorize pulling or publishing artifacts; host access controls who can administer the Engine and its workload environment.

## Why
Broad, long-lived credentials can turn a leaked token or compromised workstation into a supply-chain or host incident. Scoped access constrains blast radius.

## How
Use individual identities, repository- or task-scoped permissions where supported, short-lived credentials when available, protected host administration, and documented rotation and revocation procedures.

## Features
Docker credential helpers reduce plaintext credential storage but do not replace access governance. Logging out or rotating a token does not remove already pulled images or stop an already running container.

## Code snippets (if any)
```console
docker login
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A release pipeline receives a narrowly scoped registry token only during publish. Operators use named accounts with audited access, and a rotation drill confirms old credentials are revoked.

## Q&A
- **Q: Is containerization sufficient isolation?** No. Containers share a kernel; apply layered controls.
- **Q: Where should I start?** Limit daemon, runtime, image, mount, and network trust.
- **Q: How do I verify a control?** Inspect effective settings and test on the target host.

Source: [Official Docker documentation](https://docs.docker.com/security/for-developers/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
