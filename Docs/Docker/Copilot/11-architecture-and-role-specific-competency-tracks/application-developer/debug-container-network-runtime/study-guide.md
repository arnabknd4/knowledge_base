# Debug in the real container environment

Syllabus objective: Debug the application inside its actual container/network/runtime environment.

## What

Container-aware debugging examines the built image, process, runtime settings, DNS, network, mounts, and host limits.

## Why

Host success does not guarantee container success; paths, users, DNS, ports, and resources differ.

## How

Reproduce with the same image and Compose topology. Inspect exit status, redacted logs, user, mounts, health, DNS, ports, and limits. Change one variable at a time and isolate app, host, and platform causes.

## Features

Container localhost means the container itself; service DNS and host-published ports are distinct.

## Code snippets (if any)

Safe checks: `docker compose ps` and `docker compose logs SERVICE`. Do not dump environment values that may include secrets.

## Do's and Don'ts

DO use a disposable environment and redact evidence. DON’T assume host paths, user IDs, or localhost behave identically inside a container. DON’T expose debug ports in production without approval and a cleanup plan.

## Real-life implementation

Break one harmless service hostname or mount locally. Diagnose with status and redacted logs, restore it, and write a runbook with safe checks and expected results.

## Q&A

- What does localhost mean inside a container? That container’s network namespace.
- Why compare users? File ownership and permissions can differ.
- Should logs include full environment? No; avoid exposing secrets.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/engine/network/)
- [Official Docker documentation](https://docs.docker.com/reference/cli/docker/compose/logs/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
