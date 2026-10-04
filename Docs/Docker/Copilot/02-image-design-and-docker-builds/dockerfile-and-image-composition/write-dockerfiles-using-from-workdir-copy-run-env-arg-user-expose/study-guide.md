# Write Dockerfiles using `FROM`, `WORKDIR`, `COPY`, `RUN`, `ENV`, `ARG`, `USER`, `EXPOSE`, `ENTRYPOINT`, `CMD`, and `HEALTHCHECK` appropriately.

## What

A Dockerfile declares image construction and runtime defaults. Its instructions affect filesystem layers, build inputs, configuration, permissions, and how the application starts. Exec-form startup avoids an implicit shell and helps the application receive termination signals; test graceful shutdown and the actual process tree.

## Why

Balance control against compatibility and maintenance effort to enable reliable operations.

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

CI builds and verifies the artifact once, promotes it unchanged, and keeps an exercised recovery path.

## Q&A

- **What is the key concept?** A Dockerfile declares image construction and runtime defaults.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Pass credentials through ARG, ENV, command history, or build logs.

**Official reference:** [Docker documentation](https://docs.docker.com/build/concepts/dockerfile/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
