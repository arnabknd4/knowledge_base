# GH-200 study guide: identify and use trustworthy actions from GitHub Marketplace

## What

Marketplace is a discovery channel for actions, not a security certification. An action is executable dependency code, so assess the source repository, maintainer, release process, permissions and data it handles, then select and pin the exact revision used by the workflow.

Objective link: [GH-200 syllabus — implement security best practices](../../../../copilot-github-syllabus.md#implement-security-best-practices).

## Why

Actions run with the permissions and runtime context granted to their job. A compromised action or maintainer account can expose accessible data, alter build outputs, or misuse credentials. Floating refs such as `@main` or a mutable version tag can change without a workflow-file change, undermining reproducibility and review.

## How

- Confirm the publisher and repository match the Marketplace listing; examine ownership, maintenance history, release notes, code, dependencies, and security advisories.
- Understand the action's inputs, outputs, network access, filesystem behavior, required permissions, and whether it runs third-party code.
- Prefer actions with a clear maintenance and release process. “Official,” popular, or widely used are useful signals, not a guarantee.
- Pin production use to a reviewed full commit SHA and keep a human-readable version comment for maintenance.
- Monitor upstream releases, assess updates, and review changes before deliberately changing the pin.

```yaml
steps:
  - uses: actions/checkout@11bd71901bbe5b1630ceea73d8e5b6821dfbee0d # v4.2.2
```

The SHA above illustrates a pinned revision; verify current ownership and code before adoption. Pin the exact approved commit of every third-party action.

## Features

- **Publisher and repository context:** Marketplace listings link users to the action's source and documentation.
- **Trust assessment:** review code, maintenance signals, dependency chain, permissions, and release history together.
- **Immutable dependency selection:** full commit SHA identifies a specific revision, while a tag can be moved.
- **Governance:** organization policy can limit eligible action sources, but policy does not inspect every action for safety.

## Do's and Don'ts

**Do**
- Review the exact revision and its transitive dependencies before using it in sensitive workflows.
- Grant minimal job permissions and avoid exposing secrets to jobs that do not need them.
- Use full SHAs and a process for reviewed updates.
- Prefer a small set of maintained actions with transparent behavior and clear support ownership.

**Don't**
- Treat Marketplace presence, stars, a verified badge, or an official-looking name as proof of safety.
- Assume a release tag is immutable.
- Give an action broad token permissions or production credentials without a demonstrated need.
- Ignore abandoned dependencies, changed maintainers, or new behavior during upgrades.

## Real-life implementation

A team evaluating a deployment action checks that the Marketplace publisher links to the expected source, reads the action code and release changes, checks what credentials and network access it needs, and tests it in a low-privilege workflow. After review, the workflow pins the approved commit SHA; a scheduled dependency review checks for updates. Production access is separately limited to the deployment job, reducing the damage if the action is later compromised.

## Q&A

**Q: Does Marketplace review certify that an action is safe?**

A: No. Marketplace helps discover actions; the consumer remains responsible for assessing and maintaining trust.

**Q: Why pin a full SHA if the action has a stable major tag?**

A: A tag may move. A full SHA fixes the referenced source revision until the workflow is deliberately updated.

**Q: Are GitHub-maintained actions exempt from review?**

A: No. They may have stronger trust signals, but production dependencies should still be pinned, permissioned, and updated deliberately.

**Q: What is more important, stars or least privilege?**

A: Popularity is only one weak signal. Review the code and limit permissions so an action compromise has a smaller blast radius.

### References

- [GitHub Marketplace actions](https://github.com/marketplace?type=actions)
- [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [Using actions in a workflow](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobs-job-id-steps)
