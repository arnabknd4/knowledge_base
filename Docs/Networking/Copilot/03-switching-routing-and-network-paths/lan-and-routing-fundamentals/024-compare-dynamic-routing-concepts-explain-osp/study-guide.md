# Study Guide: Objective 024

> **Exact syllabus objective:** Compare dynamic routing concepts; explain OSPF's intra-domain role and BGP's inter-domain/policy role, autonomous systems, peering, route propagation, and convergence at a conceptual level.
>
> **Track:** Role extension · **Priority:** P2 · **Roles:** A/S

**Location:** [03. Switching, routing, and network paths](../../index.md) · **Topic:** LAN and routing fundamentals · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

OSPF is an interior routing protocol; BGP exchanges routes using policy between autonomous systems and also serves enterprise/cloud designs. The architecture lens is **Reason about how traffic is switched, routed, filtered, and returned across network boundaries**. Keep adjacent technologies in scope only where they alter this flow, trust boundary, user impact, or ownership.

## Why

Convergence and route ownership affect recovery across independently operated networks. For a failed service path, predict the next hop before probing. Compare the source route, the first boundary's flow evidence, and the return path.

## How

For the exact flow, identify the selected route and next hop, then verify policy and reverse reachability at each boundary. Compare intended route propagation with effective forwarding.

For this objective, use this focused procedure: Specify allowed prefixes, preference, redundancy, convergence and withdrawal behavior; test in a lab.

**Decision criteria:** select the smallest change that meets the service need and least-privilege boundary. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Longest-prefix selection, bounded route advertisement, explicit ownership, failure-domain separation, and observable convergence.
- **Objective-specific design note:** Do not equate a healthy adjacency with correct route propagation.
- **Evidence:** choose the metric, log, flow record, packet observation, or application trace that can prove the expected behavior from this path.
- **Failure mode to test:** distinguish intended configuration from effective forwarding/enforcement; identify the first boundary with missing evidence and its owner.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
Get-NetRoute -AddressFamily IPv4
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

- [RFC 4271 — A Border Gateway Protocol 4 (BGP-4)](https://www.rfc-editor.org/rfc/rfc4271)
