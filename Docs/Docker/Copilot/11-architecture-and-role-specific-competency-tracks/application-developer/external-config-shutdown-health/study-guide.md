# Externalize config and handle lifecycle

Syllabus objective: Keep configuration external, handle shutdown signals, expose meaningful health, and avoid reliance on container-local durable state.

## What

A robust containerized service accepts runtime configuration, handles termination, reports useful health, and stores durable state outside its writable layer.

## Why

Deployments replace processes and writable layers; bad signal handling, misleading health, or local state causes dropped work and data loss.

## How

Keep secrets out of image and logs. Ensure correct signal delivery, bounded graceful drain, meaningful health/readiness, and explicit persistent storage. Verify behavior in the actual runtime and its termination window.

## Features

Compose and orchestrators interpret health and secrets differently; check current platform behavior.

## Code snippets (if any)

No snippet required: first verify signal delivery, health semantics, and state location in your real runtime.

## Do's and Don'ts

DO test termination during work and define durable data. DON’T log secrets or treat liveness as readiness. DON’T depend on writable container storage or assume health checks repair dependencies.

## Real-life implementation

In a disposable Compose stack, stop the service mid-request and restart after writing test data. Verify shutdown, health, config, and persistence through container replacement.

## Q&A

- What is graceful shutdown? Stop new work, finish or safely cancel in-flight work, and exit in time.
- Does Compose health mean readiness everywhere? No; behavior depends on consumers.
- What persists after replacement? State deliberately stored outside the writable layer.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/compose/)
- [Official Docker documentation](https://docs.docker.com/engine/storage/volumes/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
