# Define hardened build and runtime policy

Syllabus objective: Define hardened build/runtime baselines, vulnerability SLAs, trusted image policies, signing/provenance verification, and exception processes.

## What

A baseline sets measurable requirements for image construction, artifact trust, runtime privilege, and vulnerability response.

## Why

Policies without enforceable checks, owners, timelines, and exceptions cannot reliably reduce risk.

## How

Set base-image, patch, identity, capability, secret, scan, SBOM/provenance, and verification requirements. Map severity to workload context and remediation SLA; govern exceptions and revalidation.

## Features

Scans are imperfect and time-bound; exploitability, reachability, compensating controls, and vendor support inform priority.

## Code snippets (if any)

No snippet required: requirements depend on the threat model, tooling, and workload class.

## Do's and Don'ts

DO verify policy at build/deploy boundaries and retain evidence. DON’T block on untriaged noise without an exception path. DON’T claim a signature proves safety or provenance proves source integrity.

## Real-life implementation

Apply a draft baseline to a sample image. Record failed checks, severity rationale, accountable remediation, deadline, and evidence needed for a temporary exception.

## Q&A

- Does a clean scan prove safety? No; coverage is limited and issues emerge.
- Does signing prove code is benign? No; it can establish artifact identity or origin claims.
- Why allow exceptions? To record bounded risk decisions when immediate compliance is infeasible.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/scout/)
- [Official Docker documentation](https://docs.docker.com/build/metadata/attestations/)
- [Official Docker documentation](https://docs.docker.com/engine/security/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
