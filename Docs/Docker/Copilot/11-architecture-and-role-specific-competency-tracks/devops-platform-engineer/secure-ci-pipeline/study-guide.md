# Secure CI build and release

Syllabus objective: Design secure CI build, test, scan, attest, sign, promote, and deploy workflows.

## What

A secure workflow tests an artifact, establishes its source and evidence, then promotes the same immutable artifact through protected stages.

## Why

Separating untrusted validation from privileged publishing limits credential exposure and strengthens incident traceability.

## How

Map trust boundaries from pull request to deployment. Test in controlled runners, scan and capture provenance/SBOM, protect release jobs, scope credentials, promote by digest, and record approvals and outcomes.

## Features

Treat pull-request code and caches as untrusted; credentials belong only in protected release steps.

## Code snippets (if any)

No snippet required: template and operating decisions must reflect your actual build system, team ownership, and runtime.

## Do's and Don'ts

DO verify assumptions with workload owners, document ownership, and test the proposed path in a disposable environment. DON’T equate a template, restart policy, managed label, or successful build with a secure and recoverable service.

## Real-life implementation

Diagram two paths—untrusted pull request and protected release. Mark credentials, tests, trusted cache writers, digest, approval, and deployment evidence. Verify no secret is exposed to PR code.

## Q&A

- Why promote by digest? It identifies the exact tested artifact.
- Should PRs publish release images? Normally no; untrusted code must lack release credentials.
- Does an SBOM prove safety? No; it records components, subject to tooling coverage.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/guides/gha/)
- [Official Docker documentation](https://docs.docker.com/build/building/secrets/)
- [Official Docker documentation](https://docs.docker.com/build/metadata/attestations/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
