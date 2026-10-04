# Apply versioning and release strategies

## What

Define a stable versioning model for an action so users can adopt tested releases and roll back confidently when needed.

Versioning is part of the action contract. It tells consumers which interface changes are compatible and which ones break behavior.

## Why

Actions are dependencies. When a workflow calls an action, it depends on that specific behavior staying predictable enough for automation to remain safe.

A clear version strategy reduces drift, improves rollback plans, and makes upgrade decisions traceable during incidents. Without it, a repository change can quietly change runtime behavior across many workflows.

## How

Use a consistent model:

- Major versions define compatibility boundaries (`v1`, `v2`).
- Minor versions add features while staying compatible where possible.
- Patch versions fix defects without changing the expected contract.
- Use immutable release tags and record the exact commit or tested SHA in workflows.

In practice, many actions use a major tag such as `v1` and create release tags or SHAs for each tested release. High-risk workflows often pin to a full commit SHA in addition to the major tag label.

## Features

- Clear compatibility boundaries for consumers.
- Predictable release expectations and deprecation windows.
- Better incident response and rollback.
- Stronger supply-chain control when paired with SHA pinning.

## Do's and Don'ts

Do:
- Keep major-version compatibility contracts explicit.
- Publish changelogs and release notes for breaking changes.
- Pin critical workflows to tested SHAs when security risk is high.

Don't:
- Treat a major-version change as if it were a harmless patch.
- Use floating `latest` or branch refs in production automation.
- Ship breaking changes without a documented migration path.

## Real-life implementation

A platform team maintains an action for artifact validation. The repo uses `v1` as the stable major tag, `v1.4.2` for a tested patch release, and `v2` only after a carefully announced migration period. Security-sensitive workflows pin the exact SHA for the tested version, while less-sensitive internal jobs use a major tag.

That gives the team a predictable compatibility model and a safe rollback path.

## Q&A

Q: Why are major versions important in action design?
A: They create explicit compatibility boundaries so consumers know when a breaking change is expected and can adopt it deliberately.

Q: What is the difference between a tag and a fully pinned SHA?
A: A tag is human-friendly but mutable; a full SHA is immutable and safer for supply-chain-sensitive automation.

Q: How does versioning support incident response?
A: It gives teams a clean rollback path and a documented upgrade history for deciding what changed and why.

Q: When should a release be treated as breaking?
A: When input names, output names, required permissions, or runtime behavior change in a way that causes existing workflows to fail or behave differently.

## Official references

- [GH-200 syllabus](../../../../copilot-github-syllabus.md)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [Creating a JavaScript action](https://docs.github.com/en/actions/creating-actions/creating-a-javascript-action)
- [Creating a Docker container action](https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action)
- [Creating a composite action](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action)
- [Metadata syntax for GitHub Actions](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions)
- [Workflow commands for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions)
- [Versioning actions](https://docs.github.com/en/actions/creating-actions/about-custom-actions#using-release-management-for-actions)
- [About GitHub Marketplace for actions](https://docs.github.com/en/actions/creating-actions/publishing-actions-in-github-marketplace)
