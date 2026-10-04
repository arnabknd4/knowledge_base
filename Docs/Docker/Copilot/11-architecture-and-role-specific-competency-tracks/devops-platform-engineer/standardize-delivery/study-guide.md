# Standardize Docker delivery

Syllabus objective: Standardize Dockerfiles, build actions, registry namespaces, base images, and Compose templates.

## What

A maintained, versioned paved road standardizes useful defaults while leaving room for workload-specific requirements.

## Why

Consistency reduces repeated effort and makes security improvements reusable, but rigid one-size rules encourage forks.

## How

Inventory friction, publish tested and versioned templates, name owners, define supported base images and registry conventions, and document upgrades and time-bounded exceptions.

## Features

Keep the templates small, composable, and tested against more than one representative service.

## Code snippets (if any)

No snippet required: template and operating decisions must reflect your actual build system, team ownership, and runtime.

## Do's and Don'ts

DO verify assumptions with workload owners, document ownership, and test the proposed path in a disposable environment. DON’T equate a template, restart policy, managed label, or successful build with a secure and recoverable service.

## Real-life implementation

For two different services, propose a Dockerfile, Compose, and CI template set. Run a developer through onboarding, record friction, and define owners, versioning, adoption signals, and exception review.

## Q&A

- Why version templates? So consumers can upgrade predictably.
- Must all services use one base image? No; curate a supported set.
- When is an exception acceptable? When documented requirements cannot be met, with an owner and review date.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/build/building/best-practices/)
- [Official Docker documentation](https://docs.docker.com/reference/dockerfile/)
- [Official Docker documentation](https://docs.docker.com/compose/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
