# Create, inspect, back up, restore, and safely remove volumes

## What

A named volume has an independent Docker/driver lifecycle. Safe operations identify the exact volume, check attachments and consistency, and retain tested recovery data before cleanup.

## Why

State the tradeoff and assign operational ownership.

## How

Inspect the volume. Quiesce writes or use native backup, save off-host, then restore fresh and validate integrity. Remove only after retention and backup checks.

## Features

A filesystem copy while a database is actively writing may be inconsistent.

## Code snippets (if any)

```bash
docker volume create app-data
docker volume inspect app-data
# Ensure /path/to/backups exists on the host; quiesce writers first:
docker run --rm --mount type=volume,src=app-data,dst=/data,readonly --mount type=bind,src=/path/to/backups,dst=/backup alpine:3.20 sh -c 'tar -czf /backup/app-data.tgz -C /data .'
docker volume create app-data-restore
docker run --rm --mount type=volume,src=app-data-restore,dst=/data --mount type=bind,src=/path/to/backups,dst=/backup,readonly alpine:3.20 sh -c 'tar -xzf /backup/app-data.tgz -C /data'
```

## Do's and Don'ts

- **Do:** verify the volume name, consistency point, archive integrity, restore procedure, and application behavior before declaring backup success.
- **Don't:** run `docker volume prune` casually, remove an in-use data volume, or mistake a successful tar command for a tested recovery.

## Real-life implementation

Use native backup or quiescence; encrypt and retain the archive off-host, restore into a fresh volume, and validate before use.

## Q&A

- **Q: Does inspect back up contents?** No; it reports metadata only.
- **Q: Can a live archive guarantee DB consistency?** No; quiesce writers or use an application-aware backup.
- **Q: How to validate restore?** Restore fresh; verify integrity and application queries.

**Docs:** [Docker](https://docs.docker.com/engine/storage/volumes/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
