# Attach and detach containers from networks and inspect network configuration

## What

A running container can be attached to or disconnected from a user-defined network. Network inspection reveals driver, scope, subnet, gateway, options, and connected endpoints; container inspection reveals assigned addresses and network aliases.

## Why

State the tradeoff and assign operational ownership.

## How

Use `docker network connect` and `docker network disconnect` for deliberate runtime changes, then verify both endpoint and application health. Compose or service definitions should encode intended membership so replacement containers retain it. Treat manual attachment as an operational intervention, not durable configuration.

## Features

A container may have multiple interfaces and routes.

## Code snippets (if any)

```bash
docker network inspect app-net
docker network connect app-net my-container
docker network disconnect app-net my-container
```

## Do's and Don'ts

- **Do:** confirm the target network and workload identity, capture current state, and persist intended topology in deployment config.
- **Don't:** disconnect a shared production endpoint without checking dependent flows or confuse temporary attachment with reproducible configuration.

## Real-life implementation

During a controlled migration, attach a service to a new bridge, test DNS and traffic, switch clients, then detach the old network after observing no dependencies.

## Q&A

- **Q: Does disconnect stop the container?** No, it removes that network endpoint; other interfaces and the process remain.
- **Q: Is a runtime connection preserved on replacement?** Not necessarily; declare the network in Compose or service configuration.
- **Q: What should be inspected?** Driver, scope, subnet, options, endpoint membership, aliases, and assigned addresses.

**Docs:** [Docker](https://docs.docker.com/engine/network/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
