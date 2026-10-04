# Explain high-impact Docker security risks

Portfolio exercise: Explain risks of Docker socket mounts, privileged/root containers, unauthenticated daemons, and secrets in image layers.

## What

Explain how shortcuts can expand access from an application or build step to host resources.

## Why

Accurate risk descriptions help teams choose controls without confusing container isolation with complete host protection.

## How

For each risk state precondition, impact, evidence, mitigation, and residual risk. Distinguish container root from host root and account for capabilities, mounts, daemon access, and configuration.

## Features

Privileged mode and daemon exposure have configuration-dependent consequences; assess the actual host and network path.

## Code snippets (if any)

No snippet required: present a threat table. Never expose an unauthenticated daemon on a reachable network.

## Do's and Don'ts

DO use a disposable environment, state assumptions, capture evidence, and assign follow-up ownership. DON’T use production data or credentials, infer safety from one passing check, or leave temporary resources behind.

## Real-life implementation

Give a five-minute briefing and one-page checklist. Ask a peer to identify residual risk; refine unclear claims and cite Docker docs. Use a harmless diagram only.

## Q&A

- Is container root identical to host root? Not necessarily, but config and flaws affect boundaries.
- Can deleting a secret in a later layer remove it? Earlier layers may retain it.
- Is a daemon safe behind a firewall? Filtering helps, but access must remain strongly protected and minimized.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/engine/security/protect-access/)
- [Official Docker documentation](https://docs.docker.com/engine/daemon/remote-access/)
- [Official Docker documentation](https://docs.docker.com/build/building/secrets/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
