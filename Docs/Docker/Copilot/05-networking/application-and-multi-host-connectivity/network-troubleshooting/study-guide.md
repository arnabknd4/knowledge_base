# Troubleshoot name resolution, connection refusal, port collisions, routing, firewall rules, and MTU-related failures

## What

Network symptoms identify different layers: DNS errors indicate name lookup, refusal commonly indicates a reached address without an accepting listener, timeouts suggest filtering or an unreachable path, and bind errors may indicate a host-port collision. MTU mismatch can cause selective failures for larger packets.

## Why

State the tradeoff and assign operational ownership.

## How

Reproduce from the affected namespace. Check DNS, address, listener/bind, route, published mapping, firewall, and return path in order. Compare request sizes for MTU clues; change one variable at a time.

## Features

A port being listed as published does not prove the application is ready.

## Code snippets (if any)

```bash
docker network inspect app-net
docker port my-container
docker exec my-container getent hosts api
```

## Do's and Don'ts

- **Do:** capture exact source, destination, port, timestamp, and error; validate any fix with a repeatable probe.
- **Don't:** change firewall, MTU, or address pools blindly, and don't expose a service publicly as a troubleshooting shortcut.

## Real-life implementation

An API timeout to a database is isolated by resolving the DB service name, probing its port from API, checking DB listen address, then reviewing firewall and MTU only if earlier layers pass.

## Q&A

- **Q: What does refusal usually mean?** The destination was reached but no process accepted the connection at that address and port.
- **Q: How can an MTU issue appear?** Small exchanges work while larger transfers stall or fail due to fragmentation/path-MTU problems.
- **Q: Should the first step be a firewall change?** No; verify source, DNS, listener, port mapping, routing, and evidence first.

**Docs:** [Docker](https://docs.docker.com/engine/network/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
