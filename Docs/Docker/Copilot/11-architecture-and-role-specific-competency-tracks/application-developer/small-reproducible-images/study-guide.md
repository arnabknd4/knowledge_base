# Build small, reproducible images

Syllabus objective: Create small, maintainable, reproducible images and run services locally with Compose.

## What

A maintainable image contains only runtime needs, uses controlled inputs, and separates build from execution where useful.

## Why

Understandable images reduce transfer and debugging friction; reproducible inputs improve confidence between environments.

## How

Use a supported base, explicit dependencies, controlled context, multi-stage build when appropriate, and non-root runtime. Test the final image and run dependencies locally with Compose.

## Features

Small is not automatically safe: support, patch cadence, architecture, diagnostics, and runtime compatibility matter.

## Code snippets (if any)

Illustrative pattern: `FROM approved-builder AS build`, then copy only runtime artifacts into a maintained runtime base. Replace placeholders with approved images; never copy secrets.

## Do's and Don'ts

DO inspect final layers and test startup. DON’T choose distroless or Alpine without compatibility and support checks. DON’T embed secrets in ARG, ENV, or copied files; avoid build tools in runtime without need.

## Real-life implementation

Build twice from a clean context. Explain layers, cache invalidation, base choice, final image contents, and non-root signal handling; run it in Compose and document variability.

## Q&A

- Why use multiple stages? Exclude build tools from runtime.
- Are smaller images always safer? No; maintenance and compatibility still matter.
- Are tags immutable? Not necessarily; record and promote the artifact digest.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/build/building/best-practices/)
- [Official Docker documentation](https://docs.docker.com/reference/dockerfile/)
- [Official Docker documentation](https://docs.docker.com/compose/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
