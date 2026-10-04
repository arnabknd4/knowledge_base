# Distinguish the default bridge from user-defined bridge networks, including service-name DNS behavior

## What

The legacy default bridge is created automatically, while a user-defined bridge is an explicitly named network. User-defined bridges provide automatic container-name and network-alias DNS, better isolation, and per-network configuration; the default bridge traditionally relies on legacy linking or IP addresses.

## Why

State the tradeoff and assign operational ownership.

## How

Create a dedicated bridge per trust boundary or app stack, attach only required services, and connect using service/container names or aliases. Inspect membership when diagnosing connectivity. Do not rely on an IP: container replacement can change it while DNS names remain stable on that network.

## Features

User-defined networks support embedded DNS and scoped membership.

## Code snippets (if any)

```bash
docker network create app-net
docker run -d --name api --network app-net nginx:alpine
docker run --rm --network app-net busybox:1.36 nslookup api
```

## Do's and Don'ts

- **Do:** create named networks for apps and connect peers through DNS names; inspect network membership during incidents.
- **Don't:** expose every service to the default bridge or hard-code dynamic container IPs.

## Real-life implementation

A web container and API share `frontend`; the database joins only `backend`. DNS resolves `api` inside the shared network, while the database is not reachable directly from frontend peers.

## Q&A

- **Q: Does the default bridge provide the same name DNS?** Not with the same automatic service-name behavior; create a user-defined bridge.
- **Q: Can a service name resolve outside its network?** No; network-scoped DNS is available to attached peers.
- **Q: Are names an access-control mechanism?** No; network membership limits reachability, while service authentication authorizes requests.

**Docs:** [Docker](https://docs.docker.com/engine/network/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
