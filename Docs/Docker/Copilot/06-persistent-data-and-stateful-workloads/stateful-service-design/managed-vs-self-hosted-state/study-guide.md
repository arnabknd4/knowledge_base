# Decide when to use a managed database/storage service rather than operating a stateful container

## What

A managed database or storage service transfers some infrastructure operations—such as patching, failover, and backups—to a provider under a defined service contract. A stateful container gives control but leaves the team responsible for data durability, upgrades, monitoring, security, and recovery.

## Why

State the tradeoff and assign operational ownership.

## How

Compare required extensions and versions, control/data residency, latency, scale, RPO/RTO, operational skill, total cost, portability, and provider lock-in. Verify actual backup/restore, identity, network, and failover features rather than relying on the word managed. Self-host only when ownership and on-call capacity are explicit.

## Features

Managed services still need application-level backup validation, access controls, capacity planning, and incident response.

## Code snippets (if any)

No snippet needed: this is an architecture decision based on workload requirements and operating capability.

## Do's and Don'ts

- **Do:** record the decision, failure responsibilities, recovery evidence, and exit strategy.
- **Don't:** choose self-hosting solely to avoid a service fee or assume managed means zero operational responsibility.

## Real-life implementation

A small team with a strict recovery target selects a managed database after validating restore and regional recovery; a local development stack uses a disposable database container.

## Q&A

- **Q: Does managed mean no backups are needed?** No; confirm provider protection and independently test the recovery path.
- **Q: When is a stateful container reasonable?** When the workload and team can meet its durability, security, and operational requirements.
- **Q: What should a decision record include?** Requirements, alternatives, responsibilities, costs, recovery evidence, and exit considerations.

**Docs:** [Docker](https://docs.docker.com/engine/storage/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
