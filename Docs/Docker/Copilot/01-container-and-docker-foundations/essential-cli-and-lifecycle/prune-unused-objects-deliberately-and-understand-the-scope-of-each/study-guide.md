# Prune unused objects deliberately and understand the scope of each prune command.

## What

Docker CLI lifecycle and diagnostic commands act on images, containers, or daemon state; knowing which object a command affects is essential for safe operations. Prune scopes differ; volume deletion is especially consequential. Inventory candidates, verify the active context, preserve rollback/data requirements, and choose the narrowest cleanup.

## Why

Cleanup trades disk recovery against data loss and rollback gaps; unused objects still need ownership checks.

## How

Inspect docker system df and the active context first. Review the exact prune scope and filters, back up required data, apply the narrowest command, then confirm reclaimed space and retained rollback artifacts.

## Features

A container is a process with configuration and a writable layer, not a VM. Logs, events, stats, and inspect provide different evidence; no single view is a full monitoring system.

## Code snippets (if any)

```sh
docker context show; docker system df; docker container prune --filter "until=168h"
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Run broad system or volume pruning reflexively, or equate Docker's definition of unused with business-obsolete.

## Real-life implementation

A scheduled cleanup previews candidates, retains rollback images, and blocks volume deletion unless data owners approve.

## Q&A

- **What is the key concept?** Docker CLI lifecycle and diagnostic commands act on images, containers, or daemon state.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Run broad system or volume pruning reflexively, or equate Docker's definition of unused with business-obsolete.

**Official reference:** [Docker documentation](https://docs.docker.com/reference/cli/docker/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
