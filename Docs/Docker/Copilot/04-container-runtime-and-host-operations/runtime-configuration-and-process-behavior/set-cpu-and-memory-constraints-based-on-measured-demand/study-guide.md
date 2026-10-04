# Objective study guide

> Architect study guide · Runtime configuration and process behavior

## What

**Syllabus objective:** Set CPU and memory constraints based on measured demand and host capacity; understand OOM behavior and resource contention.

## Why

Runtime behavior directly affects availability, host isolation, exposure, and graceful recovery.

## How

Set CPU and memory bounds from measurements and host headroom; CPU may throttle and memory pressure can trigger OOM. Record an owner, test behavior, and define a recovery step.

## Features

- Identify the security boundary, reliability target, operational owner, and evidence.
- Limits and hardening contain blast radius, but poor workload fit can throttle or interrupt service.

## Code snippets (if any)

```bash
docker run --memory=512m --cpus=1.5 <image>@sha256:<digest>
```

Placeholders only; test in a disposable environment.

## Do's and Don'ts

- **Do:** Verify the target and effective state; preserve evidence and assign an owner.
- **Don't:** Assume defaults or command success prove the outcome; bypass neither access controls nor rollback planning.

## Real-life implementation

Apply this to a real service in staging: name the owner, expected evidence, failure mode, and fallback. Exercise the procedure before making it a release or operations standard.

## Q&A

Self-check prompts (not claims about an official Docker exam):

**Q: What is the key operational practice?**
**A:** Set CPU and memory bounds from measurements and host headroom; CPU may throttle and memory pressure can trigger OOM.

**Q: Which trade-off should be explicit?**
**A:** Limits and hardening contain blast radius, but poor workload fit can throttle or interrupt service.

**Q: What confirms implementation?**
**A:** Repeatable evidence, an owner, and a recovery action.

## References

- [Syllabus objective](../../../copilot-docker-syllabus.md)
- [Domain index](../../index.md)
- [Official Docker documentation](https://docs.docker.com/engine/containers/resource_constraints/)
