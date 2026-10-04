# Select a runtime from requirements

Syllabus objective: Choose among containers, VMs, serverless, Compose, Swarm, Kubernetes, and managed container platforms using requirements rather than familiarity.

## What

Runtime selection balances workload shape, isolation, control, scale, team expertise, cost, and operating effort.

## Why

Orchestration can add operational surface without improving outcomes; too little capability can leave availability, scale, and governance unmet.

## How

List state, traffic, isolation, portability, compliance, deployment cadence, recovery, team skills, and total cost. Compare viable platforms, assign operational ownership, and test assumptions with a representative workload.

## Features

Compose can suit multi-container development and some one-host production use. Swarm and Kubernetes offer different orchestration models; managed platforms abstract selected operations.

## Code snippets (if any)

No snippet required: platform, workload, or threat-model decisions are the deliverable; verify syntax against your selected runtime.

## Do's and Don'ts

DO validate assumptions against actual workload behavior and record the owner and evidence. DON’T claim a container boundary, scan, signature, managed service, or successful test guarantees security or availability.

## Real-life implementation

Create an ADR for a stateless API and database with modest traffic and a small team. Compare Compose, Swarm, Kubernetes, managed containers, VMs, and serverless where relevant. Explain tradeoffs and validate the top assumption.

## Q&A

- Is Kubernetes always more scalable? No; scale depends on design and operations.
- Is Compose only for development? No; Docker documents production use cases with tradeoffs.
- Does managed mean serverless? No; service boundaries and scaling semantics differ.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/compose/)
- [Official Docker documentation](https://docs.docker.com/compose/how-tos/production/)
- [Official Docker documentation](https://docs.docker.com/engine/swarm/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
