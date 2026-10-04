# Install additional software at runtime using setup actions, package managers, caching, containers, or custom self-hosted images

## What
Not every required tool is preinstalled, and some workloads need a specific runtime or OS-level package. The goal is to choose the most reliable, repeatable runtime installation model for the workload and the enterprise.

## Why
Workflow failure can come from missing tools, mismatched versions, or inconsistent package state. An enterprise needs a defined strategy for installing software without making builds unpredictable or hard to support.

## How
- Use `setup-*` actions for standard runtimes and language toolchains.
- Use package managers and caches when the tool is not covered by a setup action or requires OS-level installation.
- Use containers for isolated or reproducible runtime environments.
- Use custom self-hosted runner images when a dependency set is expensive to install each run or needs tighter governance and patching.

## Features
- Setup actions for reproducible runtime provisioning.
- Package manager-based installation for OS-specific dependencies.
- Caching to improve speed and reduce repeated downloads.
- Containers and custom images for controlled execution environments.

## Do's and Don'ts
- Do: pin versions and keep install scripts idempotent.
- Do: validate custom images or container runtimes before production adoption.
- Do: cache dependencies when it reduces cost and build time without compromising correctness.
- Do: document which tools are installed at runtime and why.
- Don't: assume runtime installation is harmless; it changes security and reproducibility posture.
- Don't: mix package installation and custom image decisions without clear ownership.
- Don't: rely on unpinned package versions in critical production jobs.
- Don't: forget that containers and custom images add patching and lifecycle responsibilities.

## Real-life implementation
A build workflow uses `actions/setup-java` and Maven dependency caching to stay fast and deterministic. Deployment jobs run on a self-hosted runner image that already contains `kubectl`, Helm, and the company CA bundle, reducing runtime setup and improving confidence for private-cloud operations.

## Q&A
### Q: When should you prefer a setup action over package installation?
A: When the runtime is a standard toolchain with official setup support and you want a clearer, more maintainable pattern.

### Q: What is the trade-off of self-hosted custom images?
A: They improve predictability and reduce runtime setup, but they add image maintenance, patching, and governance responsibilities.

### Q: Why is caching important?
A: It reduces iteration time and external downloads while keeping dependency set reproducibility more predictable.

### Q: When do containers make sense?
A: When you need a specific OS, dependencies, or isolation model that is not easy to reproduce on a generic host.

## Official docs
- [About GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners)
- [Using containers with GitHub Actions](https://docs.github.com/en/actions/using-jobs/running-jobs-in-a-container)
- [Caching dependencies to speed up workflows](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows)
- [Adding self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners)

## Back to syllabus
- [Manage GitHub Actions for the enterprise](../../README.md)
