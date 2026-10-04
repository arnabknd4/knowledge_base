# Define trust, tenancy, and state boundaries

Syllabus objective: Define trust boundaries, tenancy/isolation, identity, network paths, state ownership, failure domains, and operating model.

## What

A boundary identifies actors, workloads, networks, data, and the authority that can access or change them.

## Why

Containers alone do not establish tenant isolation, safe identity, durable state, or a recoverable failure domain.

## How

Trace users, CI, registry, daemon, runtime identity, network, volumes, and cloud APIs. Assess privilege, kernel sharing, data classification, backup ownership, and blast radius; test realistic threat scenarios.

## Features

Daemon-socket access is highly privileged; a private network or non-root process does not by itself create a strong tenant boundary.

## Code snippets (if any)

No snippet required: platform, workload, or threat-model decisions are the deliverable; verify syntax against your selected runtime.

## Do's and Don'ts

DO validate assumptions against actual workload behavior and record the owner and evidence. DON’T claim a container boundary, scan, signature, managed service, or successful test guarantees security or availability.

## Real-life implementation

Diagram two tenants. Mark daemon access, identity, ingress/egress, shared host risks, volume owners, and failure domains. For each high-risk path, name a control and verification test.

## Q&A

- Is a container a hard tenant boundary? Not by itself; assess host and platform controls.
- Who owns volume backups? An explicitly assigned team.
- Why map egress? It can expose data or enable unintended service access.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/engine/security/)
- [Official Docker documentation](https://docs.docker.com/engine/security/protect-access/)
- [Official Docker documentation](https://docs.docker.com/engine/storage/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
