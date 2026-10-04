# Objective: Configure dependency caching and artifact management.

## What

Caching and artifacts are both optimization tools, but they solve different problems. Caching reduces repeated dependency or build work; artifacts preserve outputs for debugging, release, and downstream jobs. The goal is to avoid unnecessary compute without creating stale or overly large outputs.

## Why

- Caching improves speed but requires a stable keying strategy.
- Artifacts are essential for downstream delivery but create retention and storage overhead.
- Fine-grained artifacts usually provide better operational visibility than one huge blob.

## How

Create caches from stable dependency keys and upload only the files consumers need as artifacts, with retention suited to their purpose.

```yaml
steps:
  - uses: actions/cache@v4
    with:
      path: ~/.npm
      key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}

  - uses: actions/upload-artifact@v4
    with:
      name: build-output
      path: dist/
```

## Features

Caches accelerate later runs by reusing dependency or build data; artifacts preserve files produced by a run for later jobs, release workflows, or review. Neither is a substitute for a source of truth.

**Official references**

- [Caching dependencies to speed up workflows](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows)
- [Uploading artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts)
- [Artifact retention policies](https://docs.github.com/en/actions/administering-github-actions/configuring-workflow-uploads-for-github-actions-storing-data-in-version-control-and-artifacts)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Cache only expensive dependencies and keep keys precise.
- Upload only files required by tests, release, or debugging.
- Review artifact content for secrets or environment-specific state before upload.

**Don't**

- Don't use a cache key so broad that it risks stale data.
- Don't upload whole directories without filtering to the needed outputs.
- Don't overlook that artifact storage and cost grow with retention length and file volume.

## Real-life implementation

Use cache keys that reflect dependency inputs and treat cache contents as untrusted acceleration data. Upload only required artifact files and set retention to match operational and compliance needs.

## Q&A

**Q: Is the cache key stable enough to avoid incorrect reuse?**

**A:** Include relevant lockfiles, toolchain, and platform dimensions; use restore prefixes deliberately so a fallback cache cannot silently substitute incompatible data.

**Q: Would a downstream job still work if it consumed only the required artifact files?**

**A:** Design artifacts as explicit handoff packages with documented paths and contents; consumers should download and validate only what they need.

**Q: Are any artifacts leaking secrets or generated data that should not be retained?**

**A:** Inspect the upload path and file contents, exclude credentials and unnecessary generated material, and use an appropriate retention window.
