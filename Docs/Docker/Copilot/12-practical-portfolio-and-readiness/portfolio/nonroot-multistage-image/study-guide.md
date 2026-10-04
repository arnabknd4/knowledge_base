# Build a non-root multi-stage image

Portfolio exercise: Build a non-root, multi-stage image for a small service; explain image layers, cache behavior, base-image choice, and signal handling.

## What

Produce an image with distinct build and runtime stages and a non-root runtime identity.

## Why

Image layout, cache inputs, least privilege, and process lifecycle affect reproducibility and operational risk.

## How

Build from a controlled context, copy only runtime artifacts into a maintained runtime base, set an unprivileged user, inspect layers, and test startup and signal delivery.

## Features

Multi-stage is not automatically smaller or safer; assess compatibility, patch support, cache correctness, and diagnostics.

## Code snippets (if any)

Use `FROM approved-builder AS build`, followed by a maintained runtime stage. Replace placeholders and never copy secrets.

## Do's and Don'ts

DO use a disposable environment, state assumptions, capture evidence, and assign follow-up ownership. DON’T use production data or credentials, infer safety from one passing check, or leave temporary resources behind.

## Real-life implementation

Deliver the Dockerfile, layer/cache explanation, base choice, non-root evidence, and graceful-stop test in a disposable environment.

## Q&A

- Why separate stages? Keep build tools out of runtime.
- What invalidates cache? Changed inputs and dependent instructions.
- Does non-root eliminate risk? No; it only reduces some privilege.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/build/building/best-practices/)
- [Official Docker documentation](https://docs.docker.com/reference/dockerfile/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
