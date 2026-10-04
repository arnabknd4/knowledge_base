# Select distribution models (public, private, or Marketplace)

## What

Choose how an action is shared based on audience, governance, security, and support expectations.

An action is not just code; it is a product with a distribution model. The right choice depends on whether the action is for a single enterprise, a small team, or the public ecosystem.

## Why

Distribution decisions shape trust, maintenance cost, and operational risk. A private action can be easier to govern, while a public or Marketplace action requires stronger documentation, release discipline, and support processes.

If the action is only for internal workflows, a private model reduces accidental misuse and keeps governance in one place. If the action is broadly reusable, a public model or Marketplace listing may improve adoption but raises the bar for quality and support.

## How

Start by answering four questions:

1. Who will use the action?
2. What level of trust and discoverability is required?
3. Who owns documentation, updates, and bug triage?
4. What is the blast radius if the action changes unexpectedly?

Then map the answers to a distribution model:

- Public action: broad reuse, public discovery, and higher support burden.
- Private action: limited use, stricter governance, and simpler change control.
- Marketplace: public-facing discoverability with release quality and trust expectations.

## Features

- Public actions are searchable and repeatable across organizations.
- Private actions stay within an org or repository boundary.
- Marketplace publication adds discoverability and a public trust signal.
- Governance, ownership, and support requirements become more visible as the audience grows.

## Do's and Don'ts

Do:
- Keep private actions private when they are internal platform standards.
- Define ownership, review gates, and release expectations before publishing.
- Match the model to the action's actual audience and support burden.

Don't:
- Publish a public action before the repository has a clear maintainer.
- Assume Marketplace discoverability is the same as operational safety.
- Use public distribution for internal-only automation that should never be broadly reused.

## Real-life implementation

A large organization builds a private action that validates signed deployment metadata in internal workflows. The action is restricted to enterprise repositories and reviewed by platform security teams.

Separately, the same organization maintains a public action that generates release notes for open-source projects. That convenience action is versioned, documented, and released with a maintainer model because external users depend on it.

The distribution model is different because the risk profile and support commitment are different.

## Q&A

Q: When is a private action the right choice?
A: When the action is tied to internal policies, protected workflows, or repo-scoped automation that should not be publicly discoverable.

Q: Why does Marketplace publication increase operational expectations?
A: Because public users expect clear docs, versioning, and timely maintenance; the action becomes a public dependency.

Q: What is the biggest design mistake in distribution planning?
A: Choosing the distribution model after the implementation is built instead of before the action becomes a supported dependency.

Q: How do governance and support differ between public and private actions?
A: Private actions are usually governed by org policy, while public actions require stronger documentation, release hygiene, and maintainer accountability.

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
