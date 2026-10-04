# Explain image layers and build cache invalidation; order Dockerfile steps to keep stable dependencies cacheable.

## What

BuildKit and buildx provide modern build execution, stage selection, cache controls, platform targeting, and optional build metadata. A changed earlier instruction or input can invalidate downstream cache. Deleting a file in a later layer does not remove its bytes from earlier layers.

## Why

Cache improves iteration speed, but stale or nondeterministic inputs can undermine correctness and reproducibility.

## How

Copy stable dependency manifests before frequently changing source, inspect build timings, and verify that cache reuse does not hide mutable network inputs.

## Features

Cache is an optimization, not a correctness guarantee. Cross-platform emulation, cache exporters, and attestations depend on builder, version, and registry support.

## Code snippets (if any)

```sh
docker buildx build --progress=plain --tag app:dev .
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Copy all source before dependency installation or rely on cache for correctness.

## Real-life implementation

CI builds and verifies the artifact once, promotes it unchanged, and keeps an exercised recovery path.

## Q&A

- **What is the key concept?** BuildKit and buildx provide modern build execution, stage selection, cache controls, platform targeting, and optional build metadata.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Copy all source before dependency installation or rely on cache for correctness.

**Official reference:** [Docker documentation](https://docs.docker.com/build/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
