# Explain the difference between `ENTRYPOINT` and `CMD`, exec form and shell form, and how signals reach the application process.

## What

A Dockerfile declares image construction and runtime defaults. Its instructions affect filesystem layers, build inputs, configuration, permissions, and how the application starts. Exec-form startup avoids an implicit shell and helps the application receive termination signals; test graceful shutdown and the actual process tree.

## Why

Balance control against compatibility and maintenance effort to enable reliable operations.

## How

Prefer exec-form JSON arrays, define a clear default command, and test argument overrides, exit codes, and SIGTERM handling with the real process.

## Features

RUN executes during build; CMD and ENTRYPOINT configure startup; EXPOSE is metadata and does not publish a host port. USER sets the default process identity.

## Code snippets (if any)

```dockerfile
ENTRYPOINT ["./app"]
CMD ["--port","8080"]
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Assume a shell-form wrapper forwards signals or that restart policies repair application failures.

## Real-life implementation

CI builds and verifies the artifact once, promotes it unchanged, and keeps an exercised recovery path.

## Q&A

- **What is the key concept?** A Dockerfile declares image construction and runtime defaults.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Assume a shell-form wrapper forwards signals or that restart policies repair application failures.

**Official reference:** [Docker documentation](https://docs.docker.com/build/concepts/dockerfile/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
