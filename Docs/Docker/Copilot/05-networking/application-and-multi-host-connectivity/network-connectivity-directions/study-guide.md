# Understand outbound connectivity, host-to-container access, container-to-host access, and cross-network communication

## What

Connectivity depends on caller, listener, routes, network membership, published mappings, firewall, and platform. Bridge containers commonly use outbound NAT; host-to-container may need publishing, while container-to-host needs a platform-reachable host address.

## Why

State the tradeoff and assign operational ownership.

## How

Test from the actual caller. Share a network and use a service name for peers; publish a deliberate port for host access. For container-to-host, follow platform host-gateway guidance and constrain the host listener. Separate networks have no direct peer path unless deliberately joined.

## Features

Docker Desktop networking crosses a VM boundary; native Linux behavior may differ.

## Code snippets (if any)

```bash
docker run --rm --network app-net busybox:1.36 wget -qO- http://api:8080/ # peer-to-peer check
```

## Do's and Don'ts

- **Do:** test both directions from the actual network namespace and document platform-specific host gateway behavior.
- **Don't:** treat a successful host curl as proof that a container can connect, or bridge network separation as an absolute security boundary.

## Real-life implementation

A developer tests API-to-database traffic inside the backend network, then separately verifies a host-only published health endpoint.

## Q&A

- **Q: Do containers on separate bridges communicate automatically?** No; connect them to a shared network or use a deliberately routed/published path.
- **Q: Does publishing enable container-to-host access?** It creates host-to-container mapping; the reverse direction is a separate routing/listener concern.
- **Q: Why test on Docker Desktop?** Its host/container path includes a VM and may differ from native Linux.

**Docs:** [Docker](https://docs.docker.com/engine/network/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
