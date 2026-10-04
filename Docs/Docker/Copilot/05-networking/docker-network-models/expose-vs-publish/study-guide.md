# Distinguish a Dockerfile EXPOSE declaration from runtime port publishing (-p)

## What

`EXPOSE` is image metadata documenting the port an application intends to listen on; it does not open a host port. Runtime publishing (`-p`) maps a host address/port to a container port and establishes host reachability subject to network and firewall configuration.

## Why

State the tradeoff and assign operational ownership.

## How

Bind the application to the appropriate container interface, then publish only required ingress. Specify a host IP where possible to constrain exposure and choose a deliberate host port. Internal peers on the same user-defined network normally connect to the container port directly without publishing.

## Features

Compose `expose` is descriptive/internal network metadata, not the same as `ports`.

## Code snippets (if any)

```bash
docker run -d --name web -p 127.0.0.1:8080:80 nginx:alpine
docker port web
```

## Do's and Don'ts

- **Do:** keep service-to-service ports private and bind host-only development endpoints to loopback when appropriate.
- **Don't:** assume `EXPOSE` secures or publishes a port, or publish databases to all host interfaces without an approved need.

## Real-life implementation

A reverse proxy publishes 443; its application and database peers remain on an internal bridge and have no host port mappings.

## Q&A

- **Q: Does EXPOSE make a port reachable from the host?** No; publish it with `-p` or another explicit runtime mechanism.
- **Q: Do containers on a shared bridge need published ports?** No; they can usually reach the service's listening container port.
- **Q: What does `127.0.0.1:8080:80` do?** It maps host loopback port 8080 to container port 80, limiting host-side binding.

**Docs:** [Docker](https://docs.docker.com/engine/network/port-publishing/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
