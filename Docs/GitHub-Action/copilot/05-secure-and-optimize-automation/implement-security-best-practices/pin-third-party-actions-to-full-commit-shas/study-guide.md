# GH-200 study guide: pin third-party actions to full commit SHAs

## What

A full-length commit SHA identifies an exact action revision, while a branch or tag such as `@main` or `@v4` may move. Pinning actions to a reviewed full SHA makes the selected code explicit and prevents a later tag change from silently changing the dependency. GitHub recommends full-length SHAs as the immutable way to reference an action.

Objective link: [GH-200 syllabus — implement security best practices](../../../../copilot-github-syllabus.md#implement-security-best-practices).

## Why

If an upstream tag is moved or its repository is compromised, a workflow using that tag may fetch different code without a change in the workflow repository. The risk is highest when actions can access secrets, write permissions, or deployment credentials. Pinning improves integrity and repeatability, but does not prove that the chosen code is benign.

## How

- Resolve the intended release tag to its full commit SHA and review that exact revision.
- Use the 40-character SHA in `uses:` and include a comment with the human-readable release for maintainers.
- Apply the same rule to nested third-party action references, reusable workflows, and dependencies where your policy supports it.
- Update pins through a deliberate review process that checks release notes and source changes.
- Use applicable repository, organization, or enterprise policy to enforce SHA references; confirm the setting's actual scope and runner support.

```yaml
steps:
  - uses: actions/checkout@11bd71901bbe5b1630ceea73d8e5b6821dfbee0d # v4.2.2
  - uses: docker/setup-buildx-action@f95db51fddba0c2d1ec667646a06c2ce06100226 # v3.1.0
```

Verify that each SHA is the intended upstream release before copying it. A comment is descriptive only; the SHA controls the code fetched.

## Features

- **Immutable revision selection:** SHA pins do not follow later branch or tag movement.
- **Auditable upgrades:** a dependency update appears as a workflow diff that can be reviewed and reverted.
- **Policy support:** GitHub organization/enterprise policy can require immutable references in applicable configurations.
- **Tradeoff:** maintainers must update pins to receive upstream fixes and security patches.

## Do's and Don'ts

**Do**
- Use full, verified commit SHAs for production action references.
- Keep release tags in comments to make updates understandable, and ensure the SHA—not the comment—is authoritative.
- Automate update proposals where useful, but review and test changes before merging.
- Reduce action permissions and secrets exposure; a pin is not a substitute for least privilege.

**Don't**
- Treat semver tags, branches, or a short SHA as immutable pins.
- Copy a SHA without confirming repository, release, and commit provenance.
- Assume pinning prevents vulnerabilities already present in the selected revision.
- Leave pins untouched forever; stale pins can miss fixes and compatibility updates.

## Real-life implementation

An organization enables its available immutable-reference policy for production repositories and documents an exception process for tools that cannot be pinned. Dependency-update pull requests propose verified SHA changes with the corresponding release tag, changelog, and test results. Reviewers assess the upstream diff before merging, preserving a stable default while keeping security fixes manageable.

## Q&A

**Q: Why is a full commit SHA safer than `@v4`?**

A: A tag can be moved to a different commit; a full SHA selects the same revision unless the workflow is edited.

**Q: Does SHA pinning make an action safe?**

A: No. It makes the dependency immutable and reviewable, not free of bugs or malicious behavior.

**Q: Should workflows never update pinned SHAs?**

A: No. Update them deliberately to receive fixes and improvements, after reviewing and testing the new revision.

**Q: Does an immutable-actions policy apply everywhere automatically?**

A: No. Availability, enforcement scope, and settings depend on repository, organization, enterprise, and runner context.

### References

- [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [Using actions in a workflow](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobs-job-id-steps)
- [About GitHub-hosted runner updates](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners)
