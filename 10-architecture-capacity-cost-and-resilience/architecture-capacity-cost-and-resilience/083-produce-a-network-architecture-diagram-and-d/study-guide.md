# Study Guide: Produce a network architecture diagram and data-flow inventory showing workloads, zones, trust boundaries, routes, DNS, ingress/egress, and dependencies

> **Exact syllabus objective:** Produce a network architecture diagram and data-flow inventory showing workloads, zones, trust boundaries, routes, DNS, ingress/egress, and dependencies.
>
> **Track:** Core · **Priority:** P1 · **Roles:** D/P/S/A

**Location:** [10. Architecture, capacity, cost, and resilience](../../index.md) · **Topic:** Architecture, capacity, cost and resilience · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

A data-flow diagram shows workloads, CIDRs, routes, DNS, trust boundaries, ingress/egress, dependencies, and failure domains. The architecture lens for this outcome is **Make network design choices measurable, resilient, cost-aware, reviewable, and owned.**. Keep the exact scope in the quoted syllabus objective; adjacent technologies matter only where they alter the defined flow, trust boundary, user impact, or ownership.

## Why

It makes hidden owners, dependencies, and unobserved paths visible. Accept architectural claims only with an owner and evidence from a realistic flow, capacity test, or failure exercise. Networks are shared systems: an unexplained route, policy, address, or dependency can affect multiple services and teams. A design must make the consequence and its owner visible, not just show that a configuration can be created.

## How

State requirements and assumptions; map critical flows and failure domains; compare options; quantify capacity, quotas, cost, and recovery; test the critical failure and record the decision.

For this objective, use this focused procedure: Label every arrow with direction, protocol/port, owner, zone and control; reconcile it to actual routes and telemetry.

**Decision criteria:** prefer the smallest change that satisfies the service requirement, preserves least privilege, and can be observed and rolled back. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Data-flow inventory, explicit SLO/RTO/RPO, headroom, cost visibility, ownership, and recovery-test evidence. 
- **Evidence:** name the metric, log, flow record, packet observation, or application trace that distinguishes a fault from expected behavior.
- **Failure modes:** Version assumptions and distinguish logical from deployed topology.
- **Scale and ownership:** account for provider/CNI/OS-specific limits, shared dependencies, and who responds when the path fails.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
Client -> edge:443 -> API:8443 -> data:5432; annotate zone, route, DNS and owner
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

**Objective-specific caution:** Version assumptions and distinguish logical from deployed topology.

## Real life implementation

Accept architectural claims only with an owner and evidence from a realistic flow, capacity test, or failure exercise. Implement the focused procedure by creating a short design note with the requirement, chosen approach, owner, expected flow, failure modes, validation results, and rollback criteria. Test one critical application flow and a relevant failure in a controlled environment; compare evidence with the design before rollout. If traffic volume, trust classification, region, provider, or node OS changes, repeat the validation rather than relying on old assumptions.

## Q&A

**Q: What proves that this objective is complete?**

**A:** You can explain the exact outcome above, apply it to a concrete flow or architecture, describe the decision criteria and failure modes, and show evidence from a safe validation. Specifically: Produce a network architecture diagram and data-flow inventory showing workloads, zones, trust boundaries, routes, DNS, ingress/egress, and dependencies.

**Q: What is the most common architecture mistake?**

**A:** Treating intended configuration as proof of realized behavior. Confirm implementation, path, control enforcement, and user-visible result separately; document what could not be verified.

## References

- [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034)
- [RFC 1035 — Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035)
