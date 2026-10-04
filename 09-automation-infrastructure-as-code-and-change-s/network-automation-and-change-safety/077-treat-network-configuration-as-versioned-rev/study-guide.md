# Study Guide: Treat network configuration as versioned, reviewed, repeatable code; understand plan/review/apply, drift, state, and rollback concepts in infrastructure-as-code workflows

> **Exact syllabus objective:** Treat network configuration as versioned, reviewed, repeatable code; understand plan/review/apply, drift, state, and rollback concepts in infrastructure-as-code workflows.
>
> **Track:** Core · **Priority:** P1 · **Roles:** D/P/A

**Location:** [09. Automation, infrastructure as code, and change safety](../../index.md) · **Topic:** Network automation and change safety · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

IaC manages desired network state; plan, review, apply, protected state, drift and recovery must be designed together. The architecture lens for this outcome is **Deliver network changes as reviewed, bounded, repeatable code with tests and recovery.**. Keep the exact scope in the quoted syllabus objective; adjacent technologies matter only where they alter the defined flow, trust boundary, user impact, or ownership.

## Why

An erroneous route/rule can isolate or expose workloads. A disposable canary proves both planned configuration and effective traffic behavior before expanding the change. Networks are shared systems: an unexplained route, policy, address, or dependency can affect multiple services and teams. A design must make the consequence and its owner visible, not just show that a configuration can be created.

## How

Preview the desired-state diff; validate overlaps, exposure and routes; review scope and permissions; apply progressively; verify dataplane behavior and rollback or cleanup.

For this objective, use this focused procedure: Use isolated state and least privilege; preview diff; test overlap/exposure; review blast radius; apply progressively and verify.

**Decision criteria:** prefer the smallest change that satisfies the service requirement, preserves least privilege, and can be observed and rolled back. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Protected state, least privilege, deterministic tests, peer review, drift detection, and post-change evidence. 
- **Evidence:** name the metric, log, flow record, packet observation, or application trace that distinguishes a fault from expected behavior.
- **Failure modes:** A source revert may not reverse external side effects; do not apply unreviewed plans.
- **Scale and ownership:** account for provider/CNI/OS-specific limits, shared dependencies, and who responds when the path fails.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
terraform plan -out=network.plan  # preview only
```

## Do's and Don'ts

**Do**
- State the required flow and owner before selecting a topology, service, protocol, or rule.
- Validate both the normal path and an appropriate negative/failure path from the actual source.
- Keep changes scoped, retain evidence, and define a rollback or recovery check.

**Don't**
- Infer application health from one lower-layer probe or a configuration object.
- Broaden access, routing, capture, or retries without a bounded requirement and peer review.
- Assume provider, vendor, CNI, or operating-system behavior is interchangeable; verify the selected implementation.

**Objective-specific caution:** A source revert may not reverse external side effects; do not apply unreviewed plans.

## Real life implementation

A disposable canary proves both planned configuration and effective traffic behavior before expanding the change. Implement the focused procedure by creating a short design note with the requirement, chosen approach, owner, expected flow, failure modes, validation results, and rollback criteria. Test one critical application flow and a relevant failure in a controlled environment; compare evidence with the design before rollout. If traffic volume, trust classification, region, provider, or node OS changes, repeat the validation rather than relying on old assumptions.

## Q&A

**Q: What proves that this objective is complete?**

**A:** You can explain the exact outcome above, apply it to a concrete flow or architecture, describe the decision criteria and failure modes, and show evidence from a safe validation. Specifically: Treat network configuration as versioned, reviewed, repeatable code; understand plan/review/apply, drift, state, and rollback concepts in infrastructure-as-code workflows.

**Q: What is the most common architecture mistake?**

**A:** Treating intended configuration as proof of realized behavior. Confirm implementation, path, control enforcement, and user-visible result separately; document what could not be verified.

## References

- [Amazon VPC: What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [Azure Virtual Network overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
