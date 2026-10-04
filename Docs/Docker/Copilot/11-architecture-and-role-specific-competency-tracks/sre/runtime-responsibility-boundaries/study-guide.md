# Map runtime responsibility boundaries

Syllabus objective: Understand where Docker ends and the host, orchestrator, cloud service, or application takes responsibility.

## What

A responsibility map assigns controls and failures among runtime, host, scheduler, provider, and workload.

## Why

Incidents fall through gaps when every team assumes another handles patches, backups, access, or application recovery.

## How

Assign an owner, evidence, and escalation for image lifecycle, daemon access, host patching, scheduling, secrets, storage, networking, backups, and application recovery. Verify managed-service boundaries against actual documentation.

## Features

Managed services shift selected operations, not workload correctness, identity, configuration, or data responsibility.

## Code snippets (if any)

No snippet required: template and operating decisions must reflect your actual build system, team ownership, and runtime.

## Do's and Don'ts

DO verify assumptions with workload owners, document ownership, and test the proposed path in a disposable environment. DON’T equate a template, restart policy, managed label, or successful build with a secure and recoverable service.

## Real-life implementation

Create a responsibility matrix for Docker Engine and a managed container service. Mark duties moved, retained, or unknown; verify unknowns with operators and test one critical recovery scenario.

## Q&A

- Does managed mean provider runs the app? No; application correctness remains yours.
- Do containers isolate host kernel failures? No, they share the host kernel.
- What makes an ownership assignment useful? A named responder, evidence, and escalation route.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/engine/)
- [Official Docker documentation](https://docs.docker.com/engine/security/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
