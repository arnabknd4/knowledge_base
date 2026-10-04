# Validate observable and automatable controls

Syllabus objective: Validate that controls are observable, automatable, and compatible with workload requirements.

## What

A useful control is testable, attributable, and integrated with delivery and runtime operations.

## Why

Invisible or brittle controls are bypassed, create alert fatigue, or block legitimate workloads without reducing risk.

## How

For each control define policy, enforcement, evidence, owner, failure response, and test. Exercise allow and deny cases in CI or a disposable runtime; monitor exceptions and drift.

## Features

Prevention, detection, and remediation are distinct; automation needs clear feedback and safe recovery.

## Code snippets (if any)

No snippet required: record control-test cases and evidence sources.

## Do's and Don'ts

DO test deny behavior, alert routing, audit retention, and approved exceptions. DON’T enforce changes operators cannot observe or recover. DON’T mistake a passing pipeline for runtime compliance or ignore false positives.

## Real-life implementation

Trial three controls—non-root runtime, approved base image, and daemon exposure. Define positive/negative tests, evidence, owner, and response; test on a representative service.

## Q&A

- What makes a control observable? Evidence and actionable owner signal.
- Does CI check runtime drift? Not necessarily; runtime checks may be needed.
- Should every failure block release? Risk and policy determine enforcement and exceptions.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/engine/security/)
- [Official Docker documentation](https://docs.docker.com/scout/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
