# Distinguish build-time `ARG` from runtime `ENV`; avoid treating either as a secure secret store.

## What

A Dockerfile declares image construction and runtime defaults. Its instructions affect filesystem layers, build inputs, configuration, permissions, and how the application starts. Neither ARG nor ENV is a secret store. BuildKit secret mounts avoid committing ordinary secret files to image layers, but commands must still avoid printing or copying the value.

## Why

Keeping credentials out of artifacts limits exposure through image distribution, layer history, build caches, and logs.

## How

Use ARG only for non-secret build variation, ENV for non-sensitive image defaults, and a secret manager or BuildKit secret mount for credentials. Validate the final image configuration.

## Features

RUN executes during build; CMD and ENTRYPOINT configure startup; EXPOSE is metadata and does not publish a host port. USER sets the default process identity.

## Code snippets (if any)

```dockerfile
ARG APP_MODE=production
ENV APP_MODE=${APP_MODE}
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Pass credentials through ARG, ENV, command history, or build logs.

## Real-life implementation

CI supplies a short-lived credential only to the required step and scans build outputs for accidental disclosure.

## Q&A

- **What is the key concept?** A Dockerfile declares image construction and runtime defaults.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Pass credentials through ARG, ENV, command history, or build logs.

**Official reference:** [Docker documentation](https://docs.docker.com/build/concepts/dockerfile/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
