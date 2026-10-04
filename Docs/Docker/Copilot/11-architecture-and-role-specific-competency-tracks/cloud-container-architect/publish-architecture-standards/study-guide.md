# Publish architecture standards and migration plans

Syllabus objective: Produce reference architectures, operational standards, threat models, lifecycle policies, and migration plans.

## What

Architecture standards make design intent reusable through patterns with applicability, ownership, and maintenance rules.

## Why

Teams need a safe path from current state to target state, not merely a diagram or technology preference.

## How

For each pattern state workload, assumptions, runtime, identity/network/data controls, operations, risks, and alternatives. Threat-model important paths, stage migrations, define acceptance and rollback checks, and assign document owners.

## Features

Reference architectures are guidance, not universal guarantees; exceptions should explain requirements and compensating controls.

## Code snippets (if any)

No snippet required: platform, workload, or threat-model decisions are the deliverable; verify syntax against your selected runtime.

## Do's and Don'ts

DO validate assumptions against actual workload behavior and record the owner and evidence. DON’T claim a container boundary, scan, signature, managed service, or successful test guarantees security or availability.

## Real-life implementation

Write a reference pattern for a low-risk service and migration plan for a legacy VM workload. Add a threat scenario, validation, compatible data transition, rollback, dependencies, and target owner.

## Q&A

- Why include alternatives? Workload requirements differ.
- Who maintains a reference architecture? A named owner with a review lifecycle.
- What makes migration safe? Incremental validation and credible rollback.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/engine/security/)
- [Official Docker documentation](https://docs.docker.com/compose/how-tos/production/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
