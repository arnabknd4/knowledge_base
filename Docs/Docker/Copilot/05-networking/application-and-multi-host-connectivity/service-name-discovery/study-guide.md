# Connect services by stable service names rather than hard-coded container IP addresses

## What

On a user-defined bridge, Docker's embedded DNS resolves container names and network aliases for attached peers. Compose services are discoverable by service name on their shared networks; Swarm service discovery uses service names across an overlay.

## Why

State the tradeoff and assign operational ownership.

## How

Configure clients with a DNS service name and container port, and give each dependency an explicit shared network. Account for DNS caching and reconnection: a service name may resolve to a changed address after replacement. Use health/readiness-aware retries instead of pinning the first resolved IP forever.

## Features

Name resolution is network-scoped and supports replacement better than IP configuration.

## Code snippets (if any)

```bash
docker network create app-net
docker run -d --name api --network app-net nginx:alpine
docker run --rm --network app-net busybox:1.36 wget -qO- http://api/
```

## Do's and Don'ts

- **Do:** use stable service identities, bounded retries, timeouts, and connection-pool refresh behavior.
- **Don't:** put transient container IPs in configs or assume DNS means the target is ready and authorized.

## Real-life implementation

When `api` is rescheduled, clients keep using the logical name and retry; they do not require a coordinated config change for its new address.

## Q&A

- **Q: What scope does a name have?** Only peers with DNS visibility on the relevant Docker network or orchestrator service network.
- **Q: Can DNS replace health checks?** No; resolution identifies an endpoint, not its readiness.
- **Q: Why avoid caching an IP indefinitely?** Replacement can assign a different address while the logical name remains stable.

**Docs:** [Docker](https://docs.docker.com/engine/network/#dns-services)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
