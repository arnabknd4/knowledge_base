# Understand immutable actions rollout and version pinning

## What

Pin external actions to immutable commit SHAs and understand how rollout safety and version policy affect workflow trust.

Hosted runners and enterprise policy controls may enforce immutable-action behavior, so the safest practice is to make the dependency explicit and deterministic.

## Why

Floating references like `@main`, `@master`, and broad version tags can change without a visible workflow change. That means the same repository can produce different behavior over time even when the workflow file does not change.

This creates supply-chain drift and makes rollback and auditing harder. In security-sensitive jobs, that is unacceptable.

## How

Prefer this pattern:

```yaml
steps:
  - uses: actions/checkout@<full-commit-sha>
  - uses: docker/login-action@<full-commit-sha>
  - uses: actions/cache@<full-commit-sha>
```

Add a comment with the human-readable tag for context, for example `# v4.2.2`, but keep the actual reference immutable.

In regulated or enterprise environments, pinning to a full SHA is a standard supply-chain control. It reduces silent drift and makes each workflow dependency reviewable and reproducible.

## Features

- Deterministic execution across repeated runs.
- Improved auditability and rollback paths.
- Better protection against mutable upstream changes.
- Clearer dependency review for third-party actions.

## Do's and Don'ts

Do:
- Pin third-party actions to full commit SHAs in production and deployment workflows.
- Review the action repository and trust boundary before adoption.
- Track the approved version in a release or review record.

Don't:
- Use `@main`, `@master`, or an unreviewed tag in production automation.
- Assume a tag is immutable just because it looks stable.
- Ignore the source repository or registry when evaluating action risk.

## Real-life implementation

A release workflow calls three external actions: checkout, cache, and a dependency scanner. Each one is pinned to a specific commit SHA. The team reviews an update by changing the SHA in one workflow file and testing the job in a staging branch before shipping to the main deployment path.

Because the workflow reference is immutable, the action's behavior is reproducible and upgrade decisions are explicit.

## Q&A

Q: Why is a full SHA safer than `@main` for third-party actions?
A: Because a SHA corresponds to a specific code snapshot, while `@main` can change under the workflow without any repo change.

Q: What is the operational tradeoff in pinning to a SHA?
A: It adds governance overhead because every update requires deliberate review, but it reduces drift and supports safer rollback.

Q: How does this help with incident response?
A: An incident can be traced to a specific reviewed dependency version and rolled back by reverting the SHA reference.

Q: Why do enterprise policies often reinforce immutable pinning?
A: Because mutable action references are a supply-chain risk, especially when workflows have elevated permissions or cloud access.

## Official references

- [GH-200 syllabus](../../../../copilot-github-syllabus.md)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [Creating a JavaScript action](https://docs.github.com/en/actions/creating-actions/creating-a-javascript-action)
- [Creating a Docker container action](https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action)
- [Creating a composite action](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action)
- [Metadata syntax for GitHub Actions](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions)
- [Workflow commands for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions)
- [Versioning actions](https://docs.github.com/en/actions/creating-actions/about-custom-actions#using-release-management-for-actions)
- [About GitHub Marketplace for actions](https://docs.github.com/en/actions/creating-actions/publishing-actions-in-github-marketplace)
