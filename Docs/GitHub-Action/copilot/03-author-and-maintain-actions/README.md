# GH-200 Domain 03: Author and maintain actions

This domain covers how to design, package, secure, publish, and maintain GitHub Actions as reusable automation components. The primary emphasis is on action contracts, runner behavior, and long-term operational safety.

## Learning path

1. Start with action type selection and immutable action behavior.
2. Define the action structure and metadata contract before writing runtime logic.
3. Decide how the action will be distributed and versioned.
4. Practice troubleshooting and maintenance in a test repository before promoting to production automation.

## Topics

- [Create and troubleshoot custom actions](./create-and-troubleshoot-custom-actions/README.md)
- [Define action structure and metadata](./define-action-structure-and-metadata/README.md)
- [Distribute and maintain actions](./distribute-and-maintain-actions/README.md)

## Objective count

This domain contains 8 exam objectives across 3 topic groups.

## Official references

- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [Creating a JavaScript action](https://docs.github.com/en/actions/creating-actions/creating-a-javascript-action)
- [Creating a Docker container action](https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action)
- [Creating a composite action](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action)
- [Metadata syntax for GitHub Actions](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions)
- [Workflow commands for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions)
- [About GitHub Marketplace for actions](https://docs.github.com/en/actions/creating-actions/publishing-actions-in-github-marketplace)
- [Versioning actions](https://docs.github.com/en/actions/creating-actions/about-custom-actions#using-release-management-for-actions)

## Architecture mindset

Custom actions are reusable contracts, not only convenience wrappers. Treat them as part of the platform: they need a clear runtime model, a stable interface, security review, and a release policy.
