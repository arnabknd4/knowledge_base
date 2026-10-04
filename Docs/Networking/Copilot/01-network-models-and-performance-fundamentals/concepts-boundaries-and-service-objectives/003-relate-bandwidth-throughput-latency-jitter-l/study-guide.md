# Study Guide: Objective 003

> **Exact syllabus objective:** Relate bandwidth, throughput, latency, jitter, loss, MTU, and retransmissions to application behavior and user impact.
>
> **Track:** Core · **Priority:** P1 · **Roles:** D/P/S/A

**Location:** [01. Network models and performance fundamentals](../../index.md) · **Topic:** Concepts, boundaries, and service objectives · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

Bandwidth is a rate ceiling; throughput is delivered data. Latency, jitter, loss, MTU and retransmits identify different bottlenecks. The architecture lens is **Map a user request to the network layers and measure the performance properties that affect the service**. Keep adjacent technologies in scope only where they alter this flow, trust boundary, user impact, or ownership.

## Why

Use percentiles, representative payload size, both directions, and transport retransmit evidence; correlate them with application traces. A layered trace avoids changing the wrong layer. Compare a failed client with a healthy control, then repeat the original user-facing transaction after a scoped change.

## How

Start from a real request and user objective. Separate name resolution, link/local delivery, routing, transport, TLS, and application behavior; record timestamps and owners at each boundary.

For this objective, use this focused procedure: A link-speed result does not prove application throughput; avoid tuning before locating the bottleneck.

**Decision criteria:** select the smallest change that meets the service need and least-privilege boundary. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Layered request tracing, measurable service objectives, representative payloads, and explicit failure boundaries.
- **Objective-specific design note:** Compare small and large requests and investigate loss/MTU when only large payloads stall.
- **Evidence:** choose the metric, log, flow record, packet observation, or application trace that can prove the expected behavior from this path.
- **Failure mode to test:** distinguish intended configuration from effective forwarding/enforcement; identify the first boundary with missing evidence and its owner.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
ping -n 4 192.0.2.20  # reachability/RTT only; not application health
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

- [Cisco CCNA certification overview](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/enterprise/ccna/index.html)
