# Troubleshoot resources and connectivity

Portfolio exercise: Configure and troubleshoot CPU/memory limits, logs, DNS, published ports, and volume persistence in a disposable environment.

## What

Diagnose common symptoms across resources, logs, container DNS, published ports, and storage.

## Why

Evidence-led troubleshooting reinforces that runtime behavior depends on host, daemon, and network settings.

## How

Use a disposable stack; inspect limits, generate a harmless log, resolve a peer by service name, test a published port, and verify named-volume data after replacement. Change one factor and redact evidence.

## Features

Enforcement and metrics vary by OS, Docker Desktop VM, daemon, and configuration.

## Code snippets (if any)

Safe checks: `docker compose ps` and `docker compose logs SERVICE`. Never print environment values that may contain secrets.

## Do's and Don'ts

DO use a disposable environment, state assumptions, capture evidence, and assign follow-up ownership. DON’T use production data or credentials, infer safety from one passing check, or leave temporary resources behind.

## Real-life implementation

Create a worksheet for all five areas: symptom, hypothesis, safe check, result, resolution. State environment boundary and verify cleanup.

## Q&A

- Why can container DNS differ from host? Network/name-resolution configuration differs.
- Does publishing a port prove readiness? No; it creates a route only.
- Does a named volume guarantee backup? No; backup and restore are separate.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/engine/containers/resource_constraints/)
- [Official Docker documentation](https://docs.docker.com/engine/network/)
- [Official Docker documentation](https://docs.docker.com/engine/storage/volumes/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
