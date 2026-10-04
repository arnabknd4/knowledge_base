# Test host loss, registry outage, dependency failure, rollback, restore, and network interruption

**Domain:** Observability, reliability, and incident response<br>
**Syllabus objective:** [Test host loss, registry outage, dependency failure, rollback, restore, and network interruption](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Recovery plans are credible only after assumptions are exercised. Failure tests must be scoped, reversible, observable, approved, and normally run outside production unless specifically authorized.

## Why
Untested backups, registry access, failover, and rollback often fail when needed. Tests expose hidden single points and unclear ownership.

## How
Define hypothesis, blast radius, success/stop criteria, and recovery steps. Test failures individually, then selected combinations; verify user impact, data integrity, recovery time, and evidence.

## Features
Docker is not a complete DR system. Snapshot consistency, registry replication, control-plane failover, and network recovery depend on the larger platform.

## Code snippets (if any)
```sh
Test-only exercise: block registry access, confirm cached-image behavior, restore access, then validate deployment recovery.
```

## Do's and Don'ts
Do: obtain approval and verify restoration end-to-end. Don’t: simulate host loss on shared production without authorization or assume backup success proves recovery.

## Real-life implementation
A game day tests pulling an approved digest from a secondary registry and restoring a volume snapshot in isolation, measuring application recovery against a runbook.

## Q&A
- **Q: Useful result?** Evidence of recovery within target and documented gaps.
- **Q: Combine all failures at once?** No; establish component behavior first.
- **Q: Is a backup job sufficient?** No; restore and validate application consistency.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/engine/storage/volumes/)
- [Docker documentation](https://docs.docker.com/docker-hub/repos/manage/)
