# Understand foreground/background execution, exit codes, signals, entrypoint/command behavior, and restart policies.

## What

Docker CLI lifecycle and diagnostic commands act on images, containers, or daemon state; knowing which object a command affects is essential for safe operations. Exec-form startup avoids an implicit shell and helps the application receive termination signals; test graceful shutdown and the actual process tree.

## Why

Balance control against compatibility and maintenance effort to enable reliable operations.

## How

Run foreground and detached examples, inspect exit status, deliver SIGTERM, and test the selected restart policy against crash-loop behavior.

## Features

A container is a process with configuration and a writable layer, not a VM. Logs, events, stats, and inspect provide different evidence; no single view is a full monitoring system.

## Code snippets (if any)

```sh
docker run --name once alpine:3.21 sh -c "exit 7"; docker inspect once --format "{{.State.ExitCode}}"; docker rm once
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Assume restart policies provide readiness, graceful signal handling, or high availability.

## Real-life implementation

CI builds and verifies the artifact once, promotes it unchanged, and keeps an exercised recovery path.

## Q&A

- **What is the key concept?** Docker CLI lifecycle and diagnostic commands act on images, containers, or daemon state.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Assume restart policies provide readiness, graceful signal handling, or high availability.

**Official reference:** [Docker documentation](https://docs.docker.com/reference/cli/docker/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
