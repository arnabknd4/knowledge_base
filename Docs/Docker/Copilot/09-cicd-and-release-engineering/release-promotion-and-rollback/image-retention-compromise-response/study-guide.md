# Define retention, cleanup, and incident response for compromised or vulnerable images

**Domain:** CI/CD and release engineering<br>
**Syllabus objective:** [Define retention, cleanup, and incident response for compromised or vulnerable images](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Registry policy balances storage cost with reproducibility, investigation, and recovery. Image deletion, tag movement, and compromised credentials require ownership and response procedures.

## Why
Over-aggressive cleanup can remove rollback artifacts or evidence; unbounded retention raises cost and preserves vulnerable content without controls.

## How
Retain deployed digests and evidence for recovery/audit windows; expire disposable CI artifacts separately. On compromise, revoke credentials, block affected digests, identify deployments, preserve evidence, rebuild from trusted inputs, and communicate impact.

## Features
Consider manifest lists, attestations, rollback windows, replication, and legal policy. Retention cannot replace deployment inventory or incident runbooks.

## Code snippets (if any)
```sh
Keep deployed and rollback-eligible digests; expire only unreferenced CI artifacts after approved retention.
```

## Do's and Don'ts
Do: test rollback availability. Don’t: delete an image because its tag is old or assume deletion revokes host copies.

## Real-life implementation
After a token exposure, revoke it, audit pushes, quarantine suspicious digests, compare deployments with approved identities, then rebuild and redeploy with verified evidence.

## Q&A
- **Q: Does deleting a tag remove all copies?** No; hosts and mirrors may retain them.
- **Q: What should cleanup preserve?** Deployed and rollback-eligible artifacts and evidence.
- **Q: First compromise action?** Contain access, preserve evidence, and identify affected artifacts.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/docker-hub/repos/manage/)
- [Docker documentation](https://docs.docker.com/docker-hub/repos/manage/hub-images/immutable-tags/)
