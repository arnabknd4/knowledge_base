# Avoid concurrent writers or unsafe sharing of filesystem-backed data unless the storage system and application explicitly support it

## What

A filesystem volume is not automatically a distributed coordination system. Concurrent writers can corrupt data or violate locking and consistency assumptions, especially when a filesystem or driver does not provide the semantics an application expects.

## Why

State the tradeoff and assign operational ownership.

## How

Confirm the database/application's supported shared-storage model, filesystem locking, cache coherence, and driver semantics. Prefer one authoritative writer, database-native replication, or a storage service designed for the workload. Test failover and fencing so an old writer cannot continue after ownership moves.

## Features

Read-only sharing reduces write risk but does not guarantee a coherent live view.

## Code snippets (if any)

No snippet needed: safe concurrency depends on application and storage guarantees, not a generic Docker command.

## Do's and Don'ts

- **Do:** document writer ownership, locking, fencing, and supported access mode; test split-brain scenarios.
- **Don't:** mount one database data directory read-write into multiple independent database processes or infer safety from a driver's multi-attach feature.

## Real-life implementation

A primary database owns the data directory; replicas use database replication. Failover first fences the old primary before a new writer is promoted.

## Q&A

- **Q: Does a shared mount mean multi-writer safe?** No; storage and application must explicitly guarantee the required concurrency semantics.
- **Q: Why fence the old writer?** To prevent two active owners from writing conflicting state during failover.
- **Q: Is a read-only mount always a consistent snapshot?** No; a live writer can still change data underneath the reader.

**Docs:** [Docker](https://docs.docker.com/engine/storage/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
