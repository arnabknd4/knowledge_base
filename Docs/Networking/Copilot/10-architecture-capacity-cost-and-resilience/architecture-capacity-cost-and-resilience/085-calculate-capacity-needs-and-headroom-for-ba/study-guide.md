# Study Guide: Objective 085

> **Exact syllabus objective:** Calculate capacity needs and headroom for bandwidth, connection counts, NAT ports, addresses, load balancers, DNS, and growth; identify provider quotas and operational limits.
>
> **Track:** Role extension · **Priority:** P2 · **Roles:** A/S

**Location:** [10. Architecture, capacity, cost, and resilience](../../index.md) · **Topic:** Architecture, capacity, cost and resilience · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

Capacity includes bandwidth, connections, NAT ports, addresses, load balancers, DNS and quotas; failure load can exceed average demand. The architecture lens is **Make network design choices measurable, resilient, cost-aware, reviewable, and owned**. Keep adjacent technologies in scope only where they alter this flow, trust boundary, user impact, or ownership.

## Why

Provider limits are design constraints, not just deployment errors. Accept architectural claims only with an owner and evidence from a realistic flow, capacity test, or failure exercise.

## How

State requirements and assumptions; map critical flows and failure domains; compare options; quantify capacity, quotas, cost, and recovery; test the critical failure and record the decision.

For this objective, use this focused procedure: Forecast peak/burst and failover traffic, estimate connection lifetime, compare quota and reserve headroom.

**Decision criteria:** select the smallest change that meets the service need and least-privilege boundary. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Data-flow inventory, explicit SLO/RTO/RPO, headroom, cost visibility, ownership, and recovery-test evidence.
- **Objective-specific design note:** Measure per-zone and per-destination; do not size from averages.
- **Evidence:** choose the metric, log, flow record, packet observation, or application trace that can prove the expected behavior from this path.
- **Failure mode to test:** distinguish intended configuration from effective forwarding/enforcement; identify the first boundary with missing evidence and its owner.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
peak connections = request rate × mean connection lifetime; compare with service/NAT limits
```

## Do's and Don'ts

**Do**
- Define the expected flow and its service/control owner before choosing a topology, rule, or tool.
- Confirm the result at the source and destination boundaries and preserve the evidence with the change.
- Keep exceptions, provider-specific behavior, and rollback ownership explicit.

**Don't**
- Infer end-to-end health from a route entry, policy object, API response, or single lower-layer probe.
- Broaden a shared route, rule, retry, or capture scope without a bounded requirement and review.

## Real life implementation

In a deployment or incident review, apply the quoted outcome to an owned test boundary. Use the example only against an authorized endpoint, correlate its observation with route/policy/DNS or application evidence, and record the owner, failure/rollback point, and retest result.

## Q&A

**Q: What proves that this objective is complete?**

**A:** Pair an appropriate test with the decision record: explain the expected behavior, authoritative evidence, and limits of the probe; show how an operator would know when to stop or roll back.

**Q: Which design check from this objective should be recorded?**

**A:** Treat the design note above as an acceptance check. If it cannot be verified, record the residual risk, owner, and mitigation instead of assuming success.

## References

- [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034)
- [RFC 1035 — Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035)
