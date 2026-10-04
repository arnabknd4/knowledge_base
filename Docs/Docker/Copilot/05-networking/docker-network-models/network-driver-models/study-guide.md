# Understand bridge, host, none, overlay, macvlan, and ipvlan drivers and their appropriate use cases

## What

Drivers define connectivity boundaries: bridge is host-local; host shares the host namespace; none has no ordinary network; overlay spans Swarm nodes. Macvlan/ipvlan expose containers through host interfaces at layer 2/3.

## Why

State the tradeoff and assign operational ownership.

## How

Prefer user-defined bridge for one host and overlay for Swarm. Use host only when host-stack behavior is essential; none isolates ordinary traffic. Verify platform support, routing, addressing, and policy before macvlan/ipvlan.

## Features

Bridge provides host-local isolation and NAT; overlay supports optional multi-host encryption in Swarm; host removes network isolation; none has loopback only.

## Code snippets (if any)

No snippet needed: driver selection depends on topology and platform constraints.

## Do's and Don'ts

- **Do:** select the narrowest driver that satisfies connectivity; document address pools, ingress, and failure boundaries.
- **Don't:** treat host as a faster bridge, or assume an overlay is available without Swarm setup; don't bypass network-owner controls with L2 drivers.

## Real-life implementation

A three-tier app on one VM uses an app bridge; a Swarm service spanning nodes uses an overlay. A batch parser with no network uses none. Review host firewall and routing before go-live.

## Q&A

- **Q: When is host mode appropriate?** Only when sharing the host stack is an explicit requirement and its exposure is accepted.
- **Q: Does none block every possible communication?** It removes normal external interfaces, but the container still has loopback.
- **Q: Does bridge span hosts?** A regular bridge is host-local; use an orchestrator-managed overlay for cross-node traffic.

**Docs:** [Docker](https://docs.docker.com/engine/network/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
