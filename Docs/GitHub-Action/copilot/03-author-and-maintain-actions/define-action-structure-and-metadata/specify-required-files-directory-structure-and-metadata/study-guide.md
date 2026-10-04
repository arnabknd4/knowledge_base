# Specify required files, directory structure, and metadata

## What

Define the action contract, package layout, and metadata so GitHub can resolve, run, and document the action correctly.

Every action has an interface: inputs, outputs, permissions assumptions, and a runtime entry point. Those details are declared in `action.yml` and supported by a sensible repository layout.

## Why

A well-structured action is easier to build, test, and maintain. The metadata file is the public contract seen by workflows and by users who rely on the action.

If the metadata is wrong, the action may fail to start, produce unexpected outputs, or mislead users about its behavior. A clean structure also reduces confusion between source code, generated files, and packaged runtime assets.

## How

Choose the action type and then match the repository structure to it:

- JavaScript action: `action.yml`, `package.json`, `src/` or `dist/`, README, and often build/test assets.
- Docker action: `action.yml` with `runs.image`, plus Dockerfile and any supporting files.
- Composite action: `action.yml` plus shell scripts and reusable workflow steps.

Required metadata typically includes the action `name`, `description`, `inputs`, `outputs`, and `runs` block. The `runs` block tells GitHub how to execute the action (`node20`, `docker`, or `composite`).

## Features

- Explicit action contract for workflows and consumers.
- Clear separation between source files, runtime files, and documentation.
- Standardized runtime entry points for GitHub to execute.
- Better supportability and fewer metadata mistakes.

## Do's and Don'ts

Do:
- Keep the action metadata aligned with the actual runtime behavior.
- Document required inputs and stable output names.
- Make the repo structure consistent with the chosen action type.

Don't:
- Forget the required `runs` block.
- Ship generated files without a clear build or packaging process.
- Use undocumented or unstable output names across versions.

## Real-life implementation

A JavaScript action for release-note parsing includes a root `action.yml`, a `README.md`, a `package.json`, a `src/index.js` or compiled `dist/index.js`, and a test folder. The metadata declares the input `changelog`, the output `release-notes`, and the runtime `using: node20` together with the correct entry file.

That contract lets a workflow call the action reliably and ensures the repository layout remains maintainable as the action grows.

## Q&A

Q: What is the most important part of an action's metadata?
A: The `runs` block, because it tells GitHub how to execute the action and which file or container defines the runtime.

Q: Why do input and output names matter so much?
A: They are the interface contract used by workflows; changing them without notice breaks compatibility.

Q: How does a composite action differ from a Docker action?
A: A composite action defines steps directly in `action.yml`, while a Docker action runs from a container image and may isolate dependencies more strongly.

Q: What should the repo layout communicate to a maintainer?
A: It should clearly show whether the action is JavaScript, Docker, or composite, and where source code, generated assets, and docs live.

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
