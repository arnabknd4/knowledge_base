# Inspect image metadata, layers, size, platform/architecture, labels, and history.

## What

Image inspection reveals configuration, platform, identity, labels, and history; layer analysis adds evidence about contents and size. A changed earlier instruction or input can invalidate downstream cache. Deleting a file in a later layer does not remove its bytes from earlier layers.

## Why

Balance control against compatibility and maintenance effort to enable reliable operations.

## How

Inspect image configuration and history, verify platform and labels, and use an approved layer or SBOM tool to analyze contents.

## Features

History is not a complete provenance record or SBOM. Deleting a file in a later layer does not erase earlier layer bytes.

## Code snippets (if any)

```sh
docker image inspect alpine:3.21; docker image history --no-trunc alpine:3.21
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Treat image history as a complete SBOM or provenance record.

## Real-life implementation

CI builds and verifies the artifact once, promotes it unchanged, and keeps an exercised recovery path.

## Q&A

- **What is the key concept?** Image inspection reveals configuration, platform, identity, labels, and history.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Treat image history as a complete SBOM or provenance record.

**Official reference:** [Docker documentation](https://docs.docker.com/build/building/best-practices/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
