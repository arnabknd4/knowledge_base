# Maintain traceability from source revision to build, digest, evidence, and deployment

**Domain:** CI/CD and release engineering<br>
**Syllabus objective:** [Maintain traceability from source revision to build, digest, evidence, and deployment](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Traceability links a deployed digest to deployment, build, source revision, tests, scans, and attestations—and identifies deployments affected by a source change.

## Why
Responders need to assess exposure quickly, trust the build, and find a known-good artifact during vulnerability disclosures or incidents.

## How
Assign stable run/release IDs. Store source commit, builder identity, digest, evidence, approvals, configuration revision, environment, and rollout result in an auditable record.

## Features
Digest, provenance, SBOM, and deployment events are complementary evidence. Protect records from alteration and set retention/access policies.

## Code snippets (if any)
```sh
Record: source commit; artifact registry/app@sha256:…; evidence SBOM/provenance/scan; deployment environment + config revision.
```

## Do's and Don'ts
Do: make the chain queryable and integrity-protected. Don’t: store secrets in metadata, overwrite history, or treat registry labels as proof of source linkage.

## Real-life implementation
An incident query by vulnerable package returns each digest, source commit, environment, and owner, supporting targeted rebuild and rollback.

## Q&A
- **Q: What is the artifact key?** Digest, paired with source and build identity.
- **Q: Why record config revision?** Same image can behave differently under different config.
- **Q: Who needs traceability?** Operators, security, release teams, and auditors.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/build/metadata/attestations/)
- [Docker documentation](https://docs.docker.com/build/metadata/attestations/slsa-provenance/)
