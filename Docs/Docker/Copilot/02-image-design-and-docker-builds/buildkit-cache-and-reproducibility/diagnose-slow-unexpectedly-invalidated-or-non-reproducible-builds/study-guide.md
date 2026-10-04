# Diagnose slow, unexpectedly invalidated, or non-reproducible builds.

## What

Build timings and cache behavior help isolate context transfer, dependency installation, emulation, network access, or nondeterministic inputs. Separate immutable image content, runtime settings, writable container state, and persistent storage; this makes replacement, rollback, and ownership explicit.

## Why

Balance control against compatibility and maintenance effort to enable reliable operations.

## How

Read stage timings, inspect context size and changed inputs, compare clean and cached builds, and profile one stage at a time.

## Features

A cache hit is not proof that external inputs are fresh. Clean builds cost more and should be used as a diagnostic comparison.

## Code snippets (if any)

```sh
docker buildx build --progress=plain --tag app:diagnostic .
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Disable all cache permanently or invalidate every stage to fix one slow instruction.

## Real-life implementation

CI builds and verifies the artifact once, promotes it unchanged, and keeps an exercised recovery path.

## Q&A

- **What is the key concept?** Build timings and cache behavior help isolate context transfer, dependency installation, emulation, network access, or nondeterministic inputs.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Disable all cache permanently or invalidate every stage to fix one slow instruction.

**Official reference:** [Docker documentation](https://docs.docker.com/build/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
