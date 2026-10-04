# Identify and implement JavaScript, Docker, and composite actions

## What

Choose the right action implementation type for the runtime, dependency isolation, and maintenance model needed by the workflow.

GitHub supports three main custom action types: JavaScript, Docker, and composite. Each gives you a different balance of speed, isolation, simplicity, and runtime control.

## Why

The action type determines how much dependency management, shell behavior, and environment isolation the workflow must handle. The wrong type increases maintenance complexity and creates hidden runtime risk.

A good design matches the action to the problem: runner-native logic, containerized dependencies, or workflow-level orchestration.

## How

Use the decision model below:

- JavaScript action: best for lightweight logic that runs directly on the runner with Node.js support.
- Docker action: best when you need controlled dependencies, system libraries, or a consistent runtime environment.
- Composite action: best for combining existing steps and commands into a reusable workflow abstraction.

If you need a quick internal reuse pattern, a composite action is often a good first step. If the action is a reusable platform capability with stricter runtime needs, JavaScript or Docker is usually a better long-term choice.

## Features

- JavaScript actions run natively on the runner and are easy to integrate with Node-based tooling.
- Docker actions isolate runtime dependencies and native libraries.
- Composite actions combine steps without building a full standalone runtime.
- Each model has different security, portability, and maintainability tradeoffs.

## Do's and Don'ts

Do:
- Use JavaScript when Node-based logic fits the requirement and the runtime is straightforward.
- Use Docker when the action needs specific libraries or a stable environment that the runner does not provide.
- Use a composite action when the goal is reusable orchestration rather than packaged runtime logic.

Don't:
- Choose Docker just because it is flexible when a simpler JavaScript action would be easier to maintain.
- Treat a composite action as if it were a full runtime or a secure isolation boundary by default.
- Ignore runner permissions and environment differences when designing shell-based abstractions.

## Real-life implementation

A team creates a deployment manifest validation action for a cloud platform. The validation logic is mostly Node.js parsing and schema checks, so a JavaScript action is the cleanest choice. Another team uses a Docker action to run a CLI that depends on native packages not present on GitHub-hosted runners. A third team uses a composite action to wrap a few `bash` commands and environment setups for internal release pipelines.

Each action type is chosen for the runtime constraint it solves, not for personal preference or convenience.

## Q&A

Q: Which action type is best for dependency-heavy tooling that is not preinstalled on runners?
A: A Docker action is usually the safest and most portable option when the required runtime or libraries are not available on the runner image.

Q: Why is a composite action simpler but less isolated than a JavaScript action?
A: It directly executes workflow steps and shell logic on the runner, so it inherits the shell environment and permissions of the calling workflow.

Q: When is a JavaScript action preferable to Docker?
A: When the logic is straightforward, the runner environment already supports Node.js, and you want something simpler to build, test, and maintain.

Q: What is the main design risk with composite actions?
A: They can hide unexpected shell behavior, untrusted command execution, and environment-dependent assumptions inside a reusable abstraction.

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
