# Promote a tested image through environments by digest

**Domain:** CI/CD and release engineering<br>
**Syllabus objective:** [Promote a tested image through environments by digest](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Promotion advances one verified artifact through environments without rebuilding. Use the registry manifest digest as content identity and keep environment configuration separate.

## Why
A rebuild per environment can produce different bytes, breaking links between tests, attestations, scans, approvals, and production.

## How
Resolve the digest after trusted publication; deploy that digest in each environment, record deployment and configuration revisions, and check target policy and approvals. Use tags only as labels.

## Features
Digests identify immutable content; tags may move. Retention and permissions still matter because immutability does not guarantee availability.

## Code snippets (if any)
```sh
docker pull registry.example/app@sha256:REPLACE_WITH_VERIFIED_DIGEST
```

## Do's and Don'ts
Do: promote by digest and verify policy at each boundary. Don’t: rebuild or retag different content as the tested artifact; never use an unverified digest in production.

## Real-life implementation
Staging tests digest D and records evidence. Production deploys D after approval; only configuration differs and both revisions are recorded.

## Q&A
- **Q: Why not rebuild?** It may differ from the tested artifact.
- **Q: Can tags be used?** For discovery, but digest selects content.
- **Q: Does digest ensure availability?** No; retain and replicate artifacts.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/dhi/core-concepts/digests/)
- [Docker documentation](https://docs.docker.com/docker-hub/repos/manage/hub-images/immutable-tags/)
