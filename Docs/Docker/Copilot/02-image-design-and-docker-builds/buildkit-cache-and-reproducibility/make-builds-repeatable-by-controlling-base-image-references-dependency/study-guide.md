# Make builds repeatable by controlling base-image references, dependency lockfiles, build inputs, and build environment.

## What

Repeatable builds control base images, dependency resolution, build inputs, and toolchain environment so changes in output can be investigated. Separate immutable image content, runtime settings, writable container state, and persistent storage; this makes replacement, rollback, and ownership explicit.

## Why

Balance control against compatibility and maintenance effort to enable reliable operations.

## How

Pin or govern base references, commit lockfiles, use deterministic install modes, limit network inputs, and record builder and platform details.

## Features

Digest pinning improves identity but creates an update obligation; repeatability does not mean that old dependencies remain secure.

## Code snippets (if any)

```sh
docker image inspect alpine:3.21 --format "{{.Id}}"
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Treat floating tags or package versions as repeatable inputs, or confuse pinning with security freshness.

## Real-life implementation

CI builds and verifies the artifact once, promotes it unchanged, and keeps an exercised recovery path.

## Q&A

- **What is the key concept?** Repeatable builds control base images, dependency resolution, build inputs, and toolchain environment so changes in output can be investigated.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Treat floating tags or package versions as repeatable inputs, or confuse pinning with security freshness.

**Official reference:** [Docker documentation](https://docs.docker.com/build/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
