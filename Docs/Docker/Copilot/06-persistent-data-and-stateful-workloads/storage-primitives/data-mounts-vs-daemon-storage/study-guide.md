# Distinguish Docker's container-data mounts from the daemon's image/layer storage backend

## What

Container mounts are application data presented at paths inside containers. The daemon storage backend stores image layers, container writable layers, and internal metadata. They are separate storage concerns with different capacity, backup, and recovery procedures.

## Why

State the tradeoff and assign operational ownership.

## How

Monitor daemon data-root capacity and inode pressure separately from mounted application data. Configure supported daemon storage settings deliberately and follow Docker's migration guidance; use volume or bind mount policies for app data. Back up required data explicitly rather than copying engine internals as an application backup.

## Features

Moving daemon storage affects all local images and containers and can require a stopped daemon.

## Code snippets (if any)

```bash
docker info --format '{{.DockerRootDir}}'
docker system df -v
docker volume ls
```

## Do's and Don'ts

- **Do:** alert on both daemon storage and application mounts and use the supported engine procedure for backend changes.
- **Don't:** assume changing an app volume moves image layers, or delete daemon storage files manually while Engine is active.

## Real-life implementation

An operator investigates a full host by checking Docker root usage and the database volume separately, then applies the correct cleanup or capacity plan.

## Q&A

- **Q: Does a named volume normally live in the container layer?** No; it is a separate mount managed by Docker or its driver.
- **Q: Can system prune back up application data?** No; prune is cleanup, not backup, and its effect depends on resources and options.
- **Q: Should Docker root files be edited manually?** No; use documented daemon configuration and migration procedures.

**Docs:** [Docker](https://docs.docker.com/engine/storage/drivers/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
