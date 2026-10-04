# Study Guide: Objective 016

> **Exact syllabus objective:** Explain HTTP request/response semantics, common status classes, connection reuse, proxies, and the effect of HTTP versions without memorizing wire-level details.
>
> **Track:** Core · **Priority:** P1 · **Roles:** D/P/S/A

**Location:** [02. Addressing, subnetting, and core protocols](../../index.md) · **Topic:** Transport, naming, configuration, and application protocols · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

HTTP defines methods, headers, status and representation; intermediaries terminate connections, and protocol versions change multiplexing/transport behavior. The architecture lens is **Build a collision-free address plan and reason about the protocol behavior needed by applications**. Keep adjacent technologies in scope only where they alter this flow, trust boundary, user impact, or ownership.

## Why

Status and timing distinguish application/upstream failures from path failures. A cloud workload can fail despite a valid subnet when resolver, route, protocol, or return path differs. Validate a deployment from its actual source and record the observed address and path.

## How

Specify source, destination, protocol, resolver, and expected path. Check allocation, route, record, and socket state from the workload context; validate the return path and both expected and denied behavior.

For this objective, use this focused procedure: Record status, host, protocol, proxy, upstream timing, connection reuse and backend health.

**Decision criteria:** select the smallest change that meets the service need and least-privilege boundary. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Hierarchical IPAM, non-overlapping pools, explicit DNS ownership, transport-aware rules, and documented provider reservations.
- **Objective-specific design note:** Bound retries/timeouts and preserve request identity; do not retry non-idempotent actions blindly.
- **Evidence:** choose the metric, log, flow record, packet observation, or application trace that can prove the expected behavior from this path.
- **Failure mode to test:** distinguish intended configuration from effective forwarding/enforcement; identify the first boundary with missing evidence and its owner.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
curl.exe -sS -D - -o NUL https://service.example/
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

- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
