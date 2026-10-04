# Understand container interfaces, IP addressing, routing, DNS, NAT, firewall interaction, and port publishing

## What

Docker creates container interfaces and routes, provides DNS on user-defined networks, and configures host networking rules for bridge traffic and published ports. NAT and firewall behavior depend on driver, host OS, daemon settings, and the selected platform.

## Why

State the tradeoff and assign operational ownership.

## How

Trace a flow from source namespace through route and DNS, network interface, host forwarding/firewall, destination listener, and return path. Separate DNS failure, refusal, timeout, and routing failure. Validate effective host firewall policy because Docker-managed rules may interact with or bypass assumptions in host tooling.

## Features

Container IPs are internal and may be ephemeral.

## Code snippets (if any)

```bash
docker network inspect app-net
docker inspect --format '{{json .NetworkSettings.Networks}}' my-container
docker port my-container
```

## Do's and Don'ts

- **Do:** test from the actual source network and inspect routes, DNS, listeners, and host firewall rules as distinct layers.
- **Don't:** infer reachability from a successful DNS lookup or assume every host firewall frontend sees Docker's forwarding rules identically.

## Real-life implementation

For a timeout, compare a peer-to-peer service-name request with a host-published request, then inspect listener binding, route, firewall, and NAT independently.

## Q&A

- **Q: What does connection refused suggest?** The path reached a host that rejected the connection, often because no listener is bound there.
- **Q: What does a timeout suggest?** Possible filtering, routing, MTU, or an unresponsive endpoint; it is not a DNS diagnosis.
- **Q: Is a container IP stable?** No; use network DNS names unless a planned static addressing design requires otherwise.

**Docs:** [Docker](https://docs.docker.com/engine/network/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
