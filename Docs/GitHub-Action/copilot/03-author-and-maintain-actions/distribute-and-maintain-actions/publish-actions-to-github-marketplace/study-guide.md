# Publish actions to GitHub Marketplace

## What

Package, document, and publish a public action so it can be discovered, trusted, and consumed by the wider GitHub community.

Marketplace publication is an operational decision as much as a technical one. It turns a repository into a public dependency that users may rely on in production workflows.

## Why

GitHub Marketplace is a discoverability and trust layer. It helps users find high-quality action implementations, but it does not replace repository hygiene or maintainer accountability.

Public actions need maintainable releases, clear README instructions, and stable metadata. Without those, the action may be discoverable but not dependable.

## How

Publish in a disciplined way:

- Keep the repository README clear, actionable, and specific to real use cases.
- Provide example workflows, required permissions, inputs, outputs, and troubleshooting notes.
- Use a consistent release strategy and tag naming convention.
- Ensure the action has a clear owner and a support or maintenance model.
- Verify the repository security posture and review dependencies before listing it publicly.

Good publication is a release discipline, not a one-time checklist item.

## Features

- Marketplace listing improves visibility and trust for reusable actions.
- Clear metadata makes the action easier to adopt.
- Release notes and changelogs help users understand compatibility and updates.
- Public repository quality becomes part of the action's value story.

## Do's and Don'ts

Do:
- Document the action contract with examples and expected outputs.
- Keep version tags and release notes aligned with real repository changes.
- Maintain a known owner and support channel for user issues.

Don't:
- Publish without a tested README or a realistic workflow example.
- Treat Marketplace listing as a substitute for release management.
- Leave a public action with vague inputs, undocumented permissions, or floating examples.

## Real-life implementation

A team publishes a reusable action that standardizes release-note generation for repositories across multiple orgs. The README includes a minimal workflow example, required `GITHUB_TOKEN` permissions, input names, output names, and versioning details. The team also keeps a changelog and supports a deprecation plan for older major versions.

This makes the action predictable for users and gives maintainers a clean release contract.

## Q&A

Q: Why is README quality part of the action's trust story?
A: Users evaluate the README to understand inputs, permissions, outputs, and operational expectations before they adopt the action.

Q: What is the main risk of publishing without version discipline?
A: Consumers cannot tell which release is stable or compatible, which makes rollback and compliance harder.

Q: Why does Marketplace publication require ongoing maintenance?
A: Once published, the action enters a support relationship with users; they expect fixes, documentation, and compatibility updates.

Q: What makes a public action safer to adopt?
A: Clear ownership, explicit contract, tested examples, consistent tagging, and visible security and support practices.

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
