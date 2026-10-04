# Rehearse container and data recovery

Portfolio exercise: Demonstrate replacing a container from a known image, restoring required data, validating health, and recording recovery gaps.

## What

Recovery shows known artifacts and protected data can restore a service within accepted targets.

## Why

Recreating a container alone cannot restore state, dependencies, identity, or user availability.

## How

In a disposable environment use a known digest, simulate container loss, restore from documented backup, reapply safe configuration, validate representative behavior, and measure recovery time and data loss.

## Features

A volume is not automatically a backup; use synthetic data and test restoration.

## Code snippets (if any)

No snippet required: follow an approved test runbook using synthetic data only.

## Do's and Don'ts

DO use a disposable environment, state assumptions, capture evidence, and assign follow-up ownership. DON’T use production data or credentials, infer safety from one passing check, or leave temporary resources behind.

## Real-life implementation

Record timeline, image reference, restore source, validation, recovery gaps, owner, and retest date. Note exclusions and target results. This is a practice exercise, not an official exam objective.

## Q&A

- Does container replacement recover data? No; data needs independent recovery design.
- What should health validation include? Service checks and representative behavior.
- Why record gaps? To assign and retest resilience improvements.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/engine/storage/volumes/)
- [Official Docker documentation](https://docs.docker.com/compose/how-tos/production/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
