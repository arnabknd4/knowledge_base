# Understand that a local Docker volume is generally host-local; it is not automatically replicated or highly available

## What

A default local volume is managed by one Docker daemon and typically resides on that host. It persists across container removal on that host, but does not automatically replicate, follow a service to another node, or survive host/disk failure.

## Why

State the tradeoff and assign operational ownership.

## How

Choose an explicit availability design: managed database, replicated storage, application-level replication, or a tested node-recovery process. Validate driver scope and failure semantics before scheduling stateful workloads across hosts. Align RPO/RTO with backup, replication, and restore evidence.

## Features

Swarm scheduling a task elsewhere does not magically move local volume contents.

## Code snippets (if any)

```bash
docker volume inspect db-data
docker info --format '{{.Swarm.LocalNodeState}}'
```

## Do's and Don'ts

- **Do:** identify the storage failure domain and test host loss, volume reattachment, and data recovery.
- **Don't:** claim HA because a volume survives container deletion or because an orchestrator can restart the task on another node.

## Real-life implementation

A single-node service documents host-level recovery and off-host backups; a multi-node database uses a supported replication/storage architecture with tested failover.

## Q&A

- **Q: What does local volume persistence protect against?** Container replacement/removal, but not necessarily host or disk loss.
- **Q: Will Swarm move local volume contents?** No; local volume data is node-local unless a separate storage/replication design exists.
- **Q: What evidence supports an HA claim?** Successful, measured failover and recovery tests within stated RPO/RTO.

**Docs:** [Docker](https://docs.docker.com/engine/storage/volumes/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
