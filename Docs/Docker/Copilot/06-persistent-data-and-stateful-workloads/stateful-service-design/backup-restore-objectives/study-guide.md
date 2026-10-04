# Design backup consistency, restore testing, encryption, retention, and recovery objectives for persistent data

## What

A useful backup is recoverable data captured consistently and retained outside the workload's failure domain. RPO bounds data loss; RTO bounds recovery time. Encryption, access, retention, and restore tests belong in the design.

## Why

State the tradeoff and assign operational ownership.

## How

Use application-native backup or coordinated snapshots; encrypt data, isolate credentials, and set retention. Restore on schedule to a clean environment, validate application invariants, and measure recovery time against RPO/RTO.

## Features

Crash-consistent filesystem archives may not be transaction-consistent.

## Code snippets (if any)

```bash
docker run --rm --mount type=volume,src=db-data,dst=/data,readonly --mount type=bind,src=/path/to/backups,dst=/backup alpine:3.20 sh -c 'tar -czf /backup/db-data.tgz -C /data .'
# Use only after a consistent snapshot or quiesced/application-aware backup.
```

## Do's and Don'ts

- **Do:** define owners, retention, encryption, recovery order, and recurring restore drills with measured RPO/RTO.
- **Don't:** call replication a backup, keep the only copy on the same host, or accept an untested archive as recovery evidence.

## Real-life implementation

A quarterly drill restores a database snapshot to an isolated volume, runs integrity queries, and records recovery time against the business objective.

## Q&A

- **Q: What is RPO?** The maximum acceptable amount of data loss, expressed as a time interval.
- **Q: Why test restore instead of only backup jobs?** A successful write does not prove data is complete, decryptable, compatible, or usable.
- **Q: Does replication replace backups?** No; replicas can propagate accidental deletion, corruption, or malicious changes.

**Docs:** [Docker](https://docs.docker.com/engine/storage/volumes/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
