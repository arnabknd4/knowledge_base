# Test rollback and recovery; account for data and schema changes

**Domain:** CI/CD and release engineering<br>
**Syllabus objective:** [Test rollback and recovery; account for data and schema changes](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Rollback restores a prior image after a failed release. It cannot reverse database writes or schema migrations.

## Why
Old code may fail against a changed schema. Decide whether to roll back, roll forward, or restore data from a validated backup.

## How
Use expand/contract migrations: add fields, deploy code that tolerates old and new forms, backfill, then remove obsolete fields after the rollback window. Define recovery objectives, retain prior digests/configuration, and rehearse restore with representative data.

## Features
Separate image rollback from schema recovery, name decision owners, and record checkpoints. A successful backup is not a tested restore.

## Code snippets (if any)
```text
Prior digest compatible with current schema?
Yes: redeploy and validate. No: approved forward fix or data recovery.
```

## Do's and Don'ts
Do: retain immutable artifacts and test end-to-end restore. Don't: assume image rollback reverses writes or automatically run destructive down-migrations during an incident.

## Real-life implementation
A service adds a nullable column, deploys compatible code, backfills, and drops old fields after the rollback window. During an incident, the commander checks compatibility before reverting; otherwise the team rolls forward or restores a validated checkpoint.

## Q&A
- **Q: Does an older image restore old data?** No; image rollback does not reverse database writes.
- **Q: When is roll-forward safer?** When current schema is incompatible with prior code.
- **Q: What proves a backup is usable?** A timed restore plus application-level integrity checks.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/engine/storage/volumes/)
- [Docker documentation](https://docs.docker.com/build/metadata/attestations/)
