# Choose base images with regard to compatibility, maintenance, size, package ecosystem, and support—not size alone.

## What

A base image supplies the operating-system user space, runtime libraries, package ecosystem, and maintenance lifecycle on which the application depends. Separate immutable image content, runtime settings, writable container state, and persistent storage; this makes replacement, rollback, and ownership explicit.

## Why

Image minimization reduces transfer and attack surface, but compatibility, maintenance, and debuggability still matter.

## How

Compare supported variants, architectures, runtime compatibility, update cadence, and package needs; test changes and automate digest updates.

## Features

Compatibility, support cadence, architecture, libc, and debugging needs can matter more than compressed size. Digest pinning fixes identity but not patch freshness.

## Code snippets (if any)

```dockerfile
FROM python:3.12-slim
WORKDIR /app
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Choose an unsupported base solely for size or pin a digest without a patch-update process.

## Real-life implementation

A platform team maintains approved base families and tests automated rebuilds when security updates arrive.

## Q&A

- **What is the key concept?** A base image supplies the operating-system user space, runtime libraries, package ecosystem, and maintenance lifecycle on which the application depends.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Choose an unsupported base solely for size or pin a digest without a patch-update process.

**Official reference:** [Docker documentation](https://docs.docker.com/build/concepts/dockerfile/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
