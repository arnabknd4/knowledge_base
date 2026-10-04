# Use BuildKit/buildx for modern builds, multi-platform targets, cache import/export, and build attestations where supported.

## What

BuildKit and buildx provide modern build execution, stage selection, cache controls, platform targeting, and optional build metadata. A changed earlier instruction or input can invalidate downstream cache. Deleting a file in a later layer does not remove its bytes from earlier layers.

## Why

Balance control against compatibility and maintenance effort to enable reliable operations.

## How

Check builder capabilities, specify the target platform and stage, configure trusted cache endpoints, and request/verify attestations only where the builder and registry support them.

## Features

Cache is an optimization, not a correctness guarantee. Cross-platform emulation, cache exporters, and attestations depend on builder, version, and registry support.

## Code snippets (if any)

```sh
docker buildx build --platform linux/amd64,linux/arm64 --output=type=oci,dest=./image.tar .
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Assume cross-platform output is locally runnable or that all registries handle attestations identically.

## Real-life implementation

CI builds and verifies the artifact once, promotes it unchanged, and keeps an exercised recovery path.

## Q&A

- **What is the key concept?** BuildKit and buildx provide modern build execution, stage selection, cache controls, platform targeting, and optional build metadata.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Assume cross-platform output is locally runnable or that all registries handle attestations identically.

**Official reference:** [Docker documentation](https://docs.docker.com/build/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
