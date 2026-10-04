# Use build secrets and SSH forwarding features rather than embedding credentials in Dockerfile instructions or image layers.

## What

BuildKit and buildx provide modern build execution, stage selection, cache controls, platform targeting, and optional build metadata. Neither ARG nor ENV is a secret store. BuildKit secret mounts avoid committing ordinary secret files to image layers, but commands must still avoid printing or copying the value.

## Why

Keeping credentials out of artifacts limits exposure through image distribution, layer history, build caches, and logs.

## How

Provide a scoped secret through the BuildKit client and mount it only in the RUN instruction that needs it. Inspect image layers and build logs to confirm it was not copied or printed.

## Features

Cache is an optimization, not a correctness guarantee. Cross-platform emulation, cache exporters, and attestations depend on builder, version, and registry support.

## Code snippets (if any)

```dockerfile
# syntax=docker/dockerfile:1
FROM alpine:3.21
RUN --mount=type=secret,id=token,target=/run/secrets/token test -s /run/secrets/token
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Copy a credential and delete it later; earlier layers or logs may still expose it.

## Real-life implementation

CI supplies a short-lived credential only to the required step and scans build outputs for accidental disclosure.

## Q&A

- **What is the key concept?** BuildKit and buildx provide modern build execution, stage selection, cache controls, platform targeting, and optional build metadata.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Copy a credential and delete it later; earlier layers or logs may still expose it.

**Official reference:** [Docker documentation](https://docs.docker.com/build/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
