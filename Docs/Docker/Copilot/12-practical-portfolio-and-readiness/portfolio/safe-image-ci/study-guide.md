# Create a safe image CI workflow

Portfolio exercise: Create a CI workflow that builds and tests an image, publishes it to a registry using protected credentials, and records the resulting digest.

## What

Separate normal validation from privileged publishing and record artifact identity.

## Why

This limits credential exposure and creates a traceable handoff from tested build to deployment.

## How

Test pull requests without release credentials. In protected release jobs use scoped or supported short-lived credentials, publish, capture digest/metadata, and validate the published image. Limit permissions and trusted cache writers.

## Features

CI permissions, secrets, protected environments, and workload identity vary by provider.

## Code snippets (if any)

No YAML required: syntax is provider-specific. Use placeholders; never commit tokens or echo credentials.

## Do's and Don'ts

DO use a disposable environment, state assumptions, capture evidence, and assign follow-up ownership. DON’T use production data or credentials, infer safety from one passing check, or leave temporary resources behind.

## Real-life implementation

Implement or diagram separate PR and release paths, including tests, credential scope, approval, cache boundary, digest output, and a safe failure test in a test registry. This is a portfolio exercise, not certification coverage.

## Q&A

- What should PR validation access? Minimal test access, not release credentials.
- What does the digest provide? Identity and traceability for the exact image.
- Is branch protection enough? No; review permissions, events, runners, and environments.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/guides/gha/)
- [Official Docker documentation](https://docs.docker.com/build/building/secrets/)
- [Official Docker documentation](https://docs.docker.com/build/metadata/attestations/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
