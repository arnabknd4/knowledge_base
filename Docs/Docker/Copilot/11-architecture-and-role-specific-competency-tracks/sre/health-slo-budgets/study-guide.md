# Define workload health and budgets

Syllabus objective: Define workload health, SLO signals, resource budgets, restart behavior, and incident diagnostics.

## What

A workload health model combines process state, readiness, user-visible signals, and bounded resource use.

## Why

A running container is not necessarily a working service; useful signals expose overload and failures before users report them.

## How

Start from user journeys and dependencies. Define latency and availability signals, health semantics, resource budgets, restart expectations, and diagnostic context. Alert on symptoms and link alerts to runbooks.

## Features

Keep liveness narrow; dependency failures can trigger harmful restart storms if coupled carelessly.

## Code snippets (if any)

No snippet required: template and operating decisions must reflect your actual build system, team ownership, and runtime.

## Do's and Don'ts

DO verify assumptions with workload owners, document ownership, and test the proposed path in a disposable environment. DON’T equate a template, restart policy, managed label, or successful build with a secure and recoverable service.

## Real-life implementation

In a disposable service, inject slow responses and memory pressure. Record metrics, health behavior, alerts, and whether restart helped. Tune budgets from observations and state how each signal maps—or does not map—to the SLO.

## Q&A

- Is Docker health an SLO? No, it is one signal, not user availability.
- Why define budgets? To make capacity and contention explicit.
- Should dependencies be in liveness? Usually not; this can cause cascading restarts.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/engine/containers/resource_constraints/)
- [Official Docker documentation](https://docs.docker.com/engine/logging/configure/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
