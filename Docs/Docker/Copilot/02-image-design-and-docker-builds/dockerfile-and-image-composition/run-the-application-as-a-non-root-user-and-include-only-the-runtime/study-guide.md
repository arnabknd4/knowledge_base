# Run the application as a non-root user and include only the runtime dependencies and files needed.

## What

A non-root USER and a minimal runtime reduce process privilege and unnecessary image contents. Non-root execution limits process privilege but is not a complete sandbox; combine it with appropriate mounts, capabilities, seccomp, and host controls.

## Why

Balance control against compatibility and maintenance effort to enable reliable operations.

## How

Create a dedicated user, set ownership only on required writable paths, minimize runtime contents, and test as that identity with a read-only root filesystem where feasible.

## Features

Non-root is one layer of defense, not a complete sandbox; mounts, capabilities, seccomp, and host controls also shape risk.

## Code snippets (if any)

```dockerfile
USER 10001:10001
ENTRYPOINT ["/app"]
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Run as root for convenience or remove libraries and certificates without testing the application.

## Real-life implementation

CI builds and verifies the artifact once, promotes it unchanged, and keeps an exercised recovery path.

## Q&A

- **What is the key concept?** A non-root USER and a minimal runtime reduce process privilege and unnecessary image contents.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Run as root for convenience or remove libraries and certificates without testing the application.

**Official reference:** [Docker documentation](https://docs.docker.com/build/concepts/dockerfile/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
