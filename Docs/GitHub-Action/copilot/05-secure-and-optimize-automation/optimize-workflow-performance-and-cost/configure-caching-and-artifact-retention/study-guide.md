# GH-200 study guide: configure caching and artifact retention

## What

GitHub Actions caches reusable dependency data to avoid repeating downloads or setup work; artifacts preserve files produced by a run so later jobs or people can consume them. Caches are an optimization, not an authoritative release store. Artifact and log retention settings control how long run data remains available, and REST APIs can support management workflows where appropriate.

Objective link: [GH-200 syllabus — optimize workflow performance and cost](../../../../copilot-github-syllabus.md#optimize-workflow-performance-and-cost).

## Why

Well-designed caches reduce network transfer and job time, while controlled artifact retention limits storage cost and exposure of sensitive outputs. Broad or poorly versioned cache keys can reuse incompatible data; overly long retention consumes storage and may preserve sensitive files, while overly short retention can harm debugging, audit, and rollback.

## How

- Cache dependencies rather than generated release artifacts or secrets. Key caches on relevant inputs such as OS, tool/runtime version, and lockfile hash.
- Use restore prefixes only for compatible fallback data; avoid broad keys that mix platforms, trust boundaries, or incompatible dependency states.
- Treat cache contents as untrusted input. Do not store credentials, and validate important outputs rather than assuming cache integrity.
- Upload artifacts only when later jobs or people need them; set retention to the minimum period compatible with release, audit, and incident-response needs.
- Apply repository/org retention settings and use supported REST endpoints for automation; inspect deletion scope before cleanup to avoid removing evidence or active release inputs.

```yaml
steps:
  - uses: actions/cache@<reviewed-full-commit-sha>
    with:
      path: ~/.npm
      key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
      restore-keys: |
        ${{ runner.os }}-node-
```

This cache is for npm download data, not secrets or a trusted deployable binary. Replace the placeholder with the reviewed full SHA before use.

## Features

- **Cache keys and restore keys:** exact matches are preferred; prefix restore keys can reuse a compatible older cache when appropriate.
- **Branch-aware cache behavior:** GitHub applies cache scope and access rules; caches are not universally shared across branches or trust contexts.
- **Artifacts:** explicit upload/download moves run outputs between jobs and supports later inspection or distribution.
- **Retention controls and REST APIs:** settings and APIs can help govern duration and remove selected run data; verify endpoint capabilities and target before automation.
- **Performance/cost tradeoff:** caches consume storage and incur save/restore time, so measure hit rate and total elapsed time.

## Do's and Don'ts

**Do**
- Use deterministic, narrow cache keys and measure hit rate, restore time, and saved build time.
- Keep cache payloads limited to reproducible dependency data and exclude secrets.
- Set artifact retention based on release, compliance, audit, and incident-response requirements.
- Test cleanup automation against the exact repository/run/artifact scope before enabling destructive actions.

**Don't**
- Treat a cache as a durable or integrity-verified release artifact.
- Use a single broad key for incompatible platforms or trust levels.
- Cache credentials, signing keys, or sensitive generated configuration.
- Delete artifacts automatically without checking whether they are needed for a release, investigation, or retention requirement.

## Real-life implementation

A Node.js CI pipeline caches npm's package download directory using the OS and lockfile hash, then measures whether it actually reduces total job time. It uploads a test report for a limited retention period and keeps release artifacts longer according to release and audit needs. A scheduled cleanup job uses a narrowly scoped API operation and logs affected artifacts before deletion, avoiding indiscriminate cleanup.

## Q&A

**Q: Should a cache hold a signed release binary?**

A: No. Use explicit artifacts or a release/package registry with appropriate integrity and retention controls for release outputs.

**Q: Why include a lockfile hash in the cache key?**

A: It invalidates the exact-match cache when dependency inputs change, reducing incompatible reuse.

**Q: Are restore keys always safe?**

A: No. They broaden reuse and should only fall back to data compatible with the current platform, toolchain, and trust boundary.

**Q: How long should workflow artifacts be retained?**

A: Retain them long enough for release operations, audit, and incident response, while balancing storage cost and data sensitivity.

### References

- [Caching dependencies to speed up workflows](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows)
- [Storing workflow data as artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts)
- [REST API endpoints for GitHub Actions](https://docs.github.com/en/rest/actions/workflow-runs)
