# Design least-exposure ingress: publish only required ports and place dependent services on appropriate networks

## What

Ingress design separates external entry points from internal service connectivity. Port publishing creates a host-facing path; network membership determines which containers can communicate. Least exposure means only approved entry points are reachable from outside their intended boundary.

## Why

State the tradeoff and assign operational ownership.

## How

Map public clients to a proxy or gateway, publish its required ports, and attach dependencies to scoped internal networks. Use host-IP binding and firewall/cloud controls as defense in depth. Confirm which layer terminates TLS, authenticates users, and enforces request policy.

## Features

Networks segment reachability, not identity.

## Code snippets (if any)

```bash
docker run -d --name gateway --network edge -p 127.0.0.1:8443:443 nginx:alpine
docker network connect app-backend gateway
```

## Do's and Don'ts

- **Do:** document allowed source/destination flows and review effective firewall policy after changes.
- **Don't:** publish internal databases, admin interfaces, or every service port merely to make debugging easier.

## Real-life implementation

A host proxy publishes external 443 and forwards to the gateway's loopback binding; app and database stay on a private backend network.

## Q&A

- **Q: Does an internal network authenticate callers?** No; pair segmentation with application-layer identity and authorization.
- **Q: Should every service be published?** No; publish only approved ingress points.
- **Q: Is loopback binding suitable for public traffic?** No; use an intentionally reachable address and enforce an approved perimeter policy.

**Docs:** [Docker](https://docs.docker.com/engine/network/port-publishing/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
