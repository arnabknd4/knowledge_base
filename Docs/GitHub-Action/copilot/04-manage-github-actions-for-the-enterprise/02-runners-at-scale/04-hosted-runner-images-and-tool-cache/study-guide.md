# Identify preinstalled software and tool versions on GitHub-hosted runners using image release notes and the tool cache

## What
GitHub-hosted runner images contain a standard toolchain, but the exact software and versions change over time. The goal is to read the image release notes and tool cache docs so the workflow can be built against a known, supported runtime stack.

## Why
An app may fail if it expects a specific compiler, SDK, or package version that is not installed or is updated unexpectedly. A platform team needs predictable tooling for builds, security checks, and release automation.

## How
- Review the GitHub-hosted runner image release notes before assuming software versions.
- Check the tool cache for language runtimes and common dependencies used by the workflow.
- Pin versions with explicit setup actions in CI when compatibility matters.
- Treat the hosted environment as a managed platform that changes over time, not as a fixed local workstation.

## Features
- Preinstalled software inventory on hosted runners.
- Image release notes and version updates.
- Tool cache for common runtimes and dependencies.
- Workflow-level version pinning via `setup-*` actions.

## Do's and Don'ts
- Do: read the image release notes before migrating or scaling a workflow.
- Do: pin runtime versions when reproducibility matters.
- Do: document the expected toolchain for build and deployment jobs.
- Do: use setup actions to enforce exact versions in critical pipelines.
- Don't: assume the runner always contains the version your app needs.
- Don't: ignore image drift when a build suddenly fails after a runner update.
- Don't: depend on an unpinned toolchain in production automation.
- Don't: treat the tool cache as a guarantee of a specific version without checking the release notes.

## Real-life implementation
A build workflow reads the hosted runner release notes and then pins Node.js and .NET versions using `actions/setup-node` and `actions/setup-dotnet`. This keeps the workflow deterministic while still taking advantage of the convenience of managed GitHub-hosted execution.

## Q&A
### Q: Where do you check preinstalled versions on GitHub-hosted runners?
A: In the hosted runner documentation and the runner image release notes, plus the GitHub Actions tool cache metadata for common runtimes.

### Q: Why is version pinning still necessary on hosted runners?
A: Because the managed environment changes over time and important dependencies may shift between image versions.

### Q: How do setup actions help?
A: They let the workflow select the exact language or SDK version it expects and ensure consistent behavior across runner revisions.

### Q: What operational pattern is best for production builds?
A: Validate the image notes, pin required runtime versions, and test compatibility before relying on hosted runner defaults.

## Official docs
- [About GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners)
- [Preinstalled software on GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#preinstalled-software)
- [GitHub-hosted runner images release notes](https://github.com/actions/runner-images/releases)
- [Actions/toolkit](https://github.com/actions/toolkit)

## Back to syllabus
- [Manage GitHub Actions for the enterprise](../../README.md)
