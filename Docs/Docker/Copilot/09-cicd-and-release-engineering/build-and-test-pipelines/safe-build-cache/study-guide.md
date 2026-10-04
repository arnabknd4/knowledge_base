# Use build cache without letting untrusted builds poison trusted release caches

**Domain:** CI/CD and release engineering<br>
**Syllabus objective:** [Use build cache without letting untrusted builds poison trusted release caches](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
A build cache is a performance optimization, not trusted evidence. Scope cache read/write by trust level so fork or unreviewed PR builds cannot write entries consumed by privileged release builds.

## Why
A cache hit reuses prior results. An attacker who can seed trusted state or influence cache inputs can threaten confidentiality or artifact integrity; stale cache can hide changed inputs.

## How
Use separate cache namespaces for untrusted PR validation and protected release workflows. Prefer read-only access where possible, avoid sensitive intermediate layers, and test invalidation for changed dependencies and arguments.

## Features
BuildKit supports registry, inline, local, and other cache backends. Export/import authorization and retention are backend-specific and need policy.

## Code snippets (if any)
```sh
docker buildx build --cache-from type=registry,ref=registry.example/cache:trusted --cache-to type=registry,ref=registry.example/cache:trusted,mode=max .
```

## Do's and Don'ts
Do: isolate cache writers and scope permissions. Don’t: let fork PRs write release caches, store secrets in layers, or treat cache hits as tests or scans.

## Real-life implementation
PR jobs read a dependency cache but write to branch-scoped cache. Only protected release jobs publish to the trusted release cache; access and retention are audited.

## Q&A
- **Q: Can caches be shared?** Yes, with deliberate trust boundaries.
- **Q: Does cache prove a step ran?** No; keep independent test evidence.
- **Q: How handle build secrets?** Use secret mounts, never bake them into layers.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/build/cache/)
- [Docker documentation](https://docs.docker.com/build/cache/backends/)
- [Docker documentation](https://docs.docker.com/build/building/secrets/)
