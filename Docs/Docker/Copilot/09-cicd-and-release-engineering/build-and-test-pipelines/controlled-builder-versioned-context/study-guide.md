# Build in CI with a controlled builder and versioned context

**Domain:** CI/CD and release engineering<br>
**Syllabus objective:** [Build in CI with a controlled builder and versioned context](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Treat a CI build as a reproducible production operation. Pin the builder or Buildx version, select a known BuildKit builder, and build from a committed revision with a deliberate context and Dockerfile.

## Why
Builder drift, mutable inputs, or an accidentally broad context can change output or disclose files. Context control makes cache behavior and incident reconstruction understandable.

## How
Check out the exact commit, verify the context, exclude irrelevant and sensitive paths with .dockerignore, and record builder, platform, base-image references, and build arguments. Build from reviewed source in a least-privileged job.

## Features
Buildx supports controlled BuildKit builders and multi-platform output. Build context is the set of files available to the build, not necessarily the whole repository.

## Code snippets (if any)
```sh
docker buildx build --builder ci-builder --platform linux/amd64 --tag registry.example/app:ci-$GIT_SHA .
```

## Do's and Don'ts
Do: pin toolchain versions and use a commit-specific context. Don’t: build unreviewed code with ambient credentials or include local secrets and unrelated files.

## Real-life implementation
A platform team maintains a versioned CI builder. PR jobs build the merge candidate; protected release jobs identify the exact commit and retain builder metadata.

## Q&A
- **Q: Why pin the builder?** To reduce toolchain drift and improve reproducibility.
- **Q: Does a tag pin source?** No; build from a verified commit.
- **Q: Should the whole repository be context?** Only if required; minimize and exclude sensitive files.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/build/builders/)
- [Docker documentation](https://docs.docker.com/build/building/context/)
- [Docker documentation](https://docs.docker.com/build/building/best-practices/)
