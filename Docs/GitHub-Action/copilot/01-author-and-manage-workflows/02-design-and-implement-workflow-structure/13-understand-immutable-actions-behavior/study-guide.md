# Objective: Understand immutable actions behavior and version-pinning requirements.

## What

Actions are external dependencies. A workflow should not silently drift to a different implementation without review. Immutable references protect repeatability and supply-chain integrity.

## Why

- Floating major tags are easy to maintain but may drift unexpectedly.
- Full SHA pins are more secure and deterministic but require a deliberate update process.
- A security-sensitive workflow should not rely on loose references.

## How

Pin production dependencies to reviewed full commit SHAs and update those pins through a deliberate review and testing process.

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: docker/login-action@v3
  - uses: my-org/secure-action@<commit-sha>
```

## Features

An action reference may use a branch, tag, or commit SHA. Tags and branches can move; a full commit SHA identifies a specific revision and is the immutable pin recommended for security-sensitive dependencies.

**Official references**

- [Using actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsuses)
- [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Prefer immutable, reviewed references for production workloads.
- Keep action upgrades deliberate and auditable.
- Reduce the chance of supply-chain drift by using trusted sources and pinned versions.

**Don't**

- Don't assume `@v4` is equivalent to a pinned SHA.
- Don't overlook that floating refs can change without any code change in the repository.
- Don't treat marketplace action trust as a replacement for pinning discipline.

## Real-life implementation

Pin reviewed dependencies and automate deliberate updates. A SHA pin improves supply-chain integrity but does not establish that the pinned code is safe; review the source and update process.

## Q&A

**Q: Which ref is the safest for a production workflow: major tag or full commit SHA?**

**A:** A reviewed full commit SHA is the immutable choice; pair it with source review and a controlled update process rather than treating a pin as proof of safety.

**Q: What happens if a floating ref changes behavior after the workflow is already running?**

**A:** A run resolves the action reference for execution; a mutable ref can produce different code on later runs without a workflow-file change, so review and pin releases.

**Q: Is your organization reviewing action upgrades with the same rigor as code upgrades?**

**A:** It should: validate the upstream change, update the pinned SHA intentionally, and test the workflow before broad rollout.
