# Understand overlay networking prerequisites and the operational/security implications of cross-host container networking

## What

An overlay network provides a virtual network across Docker Swarm nodes for services. It requires Swarm membership, node-to-node connectivity on required control/data ports, non-overlapping address pools, and compatible firewall/routing. Overlay reachability expands the cross-host trust boundary.

## Why

State the tradeoff and assign operational ownership.

## How

Design the node network, subnets, firewall rules, encryption requirements, service membership, and ingress path before deploying. Test node failure and packet paths, monitor control-plane and data-plane health, and restrict which services join each overlay. Verify documented prerequisites for the Docker release and infrastructure.

## Features

Overlay is an orchestrator network, not a generic multi-host bridge.

## Code snippets (if any)

```bash
# Run on a Swarm manager after initializing or joining the Swarm:
docker network create --driver overlay --attachable app-overlay
docker network inspect app-overlay
```

## Do's and Don'ts

- **Do:** allow only required node traffic, use scoped overlays, and validate encryption/performance and recovery behavior.
- **Don't:** create an overlay expecting it to work on standalone engines or assume its encryption secures the whole application path.

## Real-life implementation

A Swarm platform uses separate overlays for frontend and database traffic and rehearses node loss while checking service discovery and recovery.

## Q&A

- **Q: What is required for an overlay?** A Swarm-capable deployment and reachable, correctly firewalled nodes with planned address space.
- **Q: Is overlay universally available across Docker hosts?** No; it is tied to Swarm scope and its deployment prerequisites.
- **Q: Does encrypted overlay remove need for TLS?** No; application-level TLS and identity remain appropriate for end-to-end protection.

**Docs:** [Docker](https://docs.docker.com/engine/network/drivers/overlay/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
