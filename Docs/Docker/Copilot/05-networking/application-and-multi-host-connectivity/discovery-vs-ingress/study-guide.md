# Plan service discovery and ingress/load balancing separately from container networking

## What

Container networking provides paths and name resolution within its scope; service discovery maps logical names to endpoints; ingress/load balancing accepts client traffic and selects a backend. These concerns interact but are separate architecture responsibilities.

## Why

State the tradeoff and assign operational ownership.

## How

Define internal service names and endpoint health, then choose an ingress controller, load balancer, or platform service for external traffic. Specify TLS termination, health probes, draining, retries, and failure domains. Do not assume Docker network DNS supplies internet-facing routing or production load balancing policy.

## Features

Embedded DNS supports network-scoped endpoint lookup.

## Code snippets (if any)

No snippet needed: ingress and load-balancing choices depend on the target platform and traffic policy.

## Do's and Don'ts

- **Do:** define ownership and health semantics for discovery, ingress, TLS, and backend networks separately.
- **Don't:** confuse service DNS with a public DNS record or treat a port mapping as a complete load-balancing and availability design.

## Real-life implementation

A public load balancer terminates or forwards TLS to gateway replicas; internal service DNS routes application calls, and health checks remove unhealthy backends.

## Q&A

- **Q: Does Docker DNS provide public ingress?** No; configure external DNS and an ingress/load-balancing path.
- **Q: What selects healthy backends?** An ingress or load-balancing component using an explicit health policy.
- **Q: Is publishing a port sufficient for HA?** No; availability requires redundant endpoints, health handling, and an external/client routing strategy.

**Docs:** [Docker](https://docs.docker.com/engine/swarm/ingress/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
