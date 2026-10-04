# Study Guide: Objective 036

> **Exact syllabus objective:** Compare Layer 4 and Layer 7 load balancing, health checks, backend pools, connection draining, session affinity, and TLS termination/pass-through.
>
> **Track:** Core · **Priority:** P1 · **Roles:** D/P/S/A

**Location:** [05. Load distribution, edge delivery, and availability](../../index.md) · **Topic:** Load balancing and edge availability · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

L4 balances transport connections; L7 routes application requests. Health checks, readiness, drain, affinity and TLS termination control behavior. The architecture lens is **Distribute traffic across healthy capacity and reason about the user-visible effects of edge and dependency failure**. Keep adjacent technologies in scope only where they alter this flow, trust boundary, user impact, or ownership.

## Why

Incorrect health checks remove healthy capacity or route users to broken backends. During a release or dependency loss, observe edge and origin separately and confirm the surviving capacity can meet the service objective.

## How

Define health from service readiness, document TLS and state boundaries, then test one controlled backend, zone, or dependency failure. Measure detection, traffic movement, recovery, and user impact.

For this objective, use this focused procedure: Choose layer by protocol needs; define readiness, pool sizing, bounded drain and TLS boundary; observe each backend.

**Decision criteria:** select the smallest change that meets the service need and least-privilege boundary. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Health-aware pools, bounded draining, explicit cache/DNS behavior, zone capacity, and tested failover.
- **Objective-specific design note:** A TCP check is not application readiness; affinity does not solve state.
- **Evidence:** choose the metric, log, flow record, packet observation, or application trace that can prove the expected behavior from this path.
- **Failure mode to test:** distinguish intended configuration from effective forwarding/enforcement; identify the first boundary with missing evidence and its owner.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
curl.exe -sS -o NUL -w "%{http_code} %{remote_ip} %{time_total}`n" https://service.example/
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

- [RFC 8446 — The Transport Layer Security (TLS) Protocol Version 1.3](https://www.rfc-editor.org/rfc/rfc8446)
