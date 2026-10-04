# Threat-model Docker trust paths

Syllabus objective: Threat-model daemon/API access, image sources, build secrets, mounts, capabilities, runtime identity, and network exposure.

## What

A Docker threat model traces attacker-controlled inputs and privileged interfaces from source and build to daemon, image, runtime, and data.

## Why

A missed socket, secret, or host mount can turn an application or build compromise into broader access.

## How

List assets, actors, trust zones, and abuse cases. Trace Dockerfile/context, base images, CI runners, registry, daemon, mounts, capabilities, identity, and egress. Rate impact and assign preventive and detective controls.

## Features

A socket mount can confer daemon authority; the exact blast radius depends on configuration.

## Code snippets (if any)

No snippet required: diagram trust zones and abuse cases.

## Do's and Don'ts

DO inspect real permissions and test in isolation. DON’T infer security from the container boundary. DON’T expose an unauthenticated daemon or give untrusted builders broad host access.

## Real-life implementation

Threat-model a runner that builds pull requests and deploys releases. Trace untrusted inputs to daemon and credentials; propose a separation and test for each high-impact path.

## Q&A

- Is read-only socket mounting harmless? No; API operations may still control the daemon.
- Does a private registry guarantee trust? No; verify identity, provenance, policy, and access.
- Why review mounts? They expose host files or runtime data.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/engine/security/protect-access/)
- [Official Docker documentation](https://docs.docker.com/engine/daemon/remote-access/)
- [Official Docker documentation](https://docs.docker.com/build/building/secrets/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
