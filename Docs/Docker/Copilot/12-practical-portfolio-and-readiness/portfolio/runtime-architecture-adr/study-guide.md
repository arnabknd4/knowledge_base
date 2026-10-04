# Compare runtime choices in an ADR

Portfolio exercise: Write a short architecture decision record comparing Compose on one host, Swarm, Kubernetes, and a managed container service for a realistic workload.

## What

Record workload constraints, candidate runtimes, decision, tradeoffs, and conditions for revisiting.

## Why

Comparing operations as well as features avoids popularity-driven choices and portability overclaims.

## How

Describe state, traffic, availability, isolation, compliance, team skills, cost, scaling, and recovery. Compare effort, scheduling, upgrades, failure domains, ecosystem, and lock-in; validate assumptions with owners.

## Features

Compose can suit one host; Swarm and Kubernetes provide different orchestration; managed services shift selected duties. None universally wins.

## Code snippets (if any)

No snippet required: the ADR and evidence are the deliverable.

## Do's and Don'ts

DO use a disposable environment, state assumptions, capture evidence, and assign follow-up ownership. DON’T use production data or credentials, infer safety from one passing check, or leave temporary resources behind.

## Real-life implementation

Write a one-page ADR for an API with stateful dependency. Give rejection reasons, proof-of-concept question, operating owner, and revisit trigger.

## Q&A

- Is managed platform the same as serverless? No; abstractions and scaling semantics differ.
- Does Kubernetes guarantee portability? No; extensions and services create differences.
- What makes an ADR useful later? Assumptions, tradeoffs, owner, and revisit triggers.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/compose/how-tos/production/)
- [Official Docker documentation](https://docs.docker.com/engine/swarm/)
- [Official Docker documentation](https://docs.docker.com/compose/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
