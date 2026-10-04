# Study Guide: Objective 061

> **Exact syllabus objective:** Plan dual-stack clusters, non-overlapping address pools, multi-cluster connectivity, service exposure, and network-policy governance.
>
> **Track:** Role extension · **Priority:** P2 · **Roles:** P/A

**Location:** [07. Containers and Kubernetes networking](../../index.md) · **Topic:** Container and Kubernetes networking · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

Dual-stack and multi-cluster need disjoint pools, routing, policy parity, DNS and service exposure per family. The architecture lens is **Trace container and Kubernetes traffic through API intent and the actual CNI, node, and service dataplane**. Keep adjacent technologies in scope only where they alter this flow, trust boundary, user impact, or ownership.

## Why

One address family can fail while another appears healthy. An accepted Kubernetes object does not prove dataplane enforcement. Validate from the workload on each supported node/CNI and inspect the effective endpoint and policy.

## How

Identify source Pod/container, destination and node. Check DNS, endpoints/readiness, route, policy, plugin health, OS support, and external NAT in order; test allowed and denied flows.

For this objective, use this focused procedure: Reserve pools, test endpoint selection, route advertisement, policy and failover for each family.

**Decision criteria:** select the smallest change that meets the service need and least-privilege boundary. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Non-overlapping address pools, verified CNI enforcement, health-aware endpoints, explicit exposure, and operating-system compatibility.
- **Objective-specific design note:** Don't assume advertised IPv6 implies working backends.
- **Evidence:** choose the metric, log, flow record, packet observation, or application trace that can prove the expected behavior from this path.
- **Failure mode to test:** distinguish intended configuration from effective forwarding/enforcement; identify the first boundary with missing evidence and its owner.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
kubectl get services -A -o wide
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

- [RFC 8200 — Internet Protocol, Version 6 (IPv6) Specification](https://www.rfc-editor.org/rfc/rfc8200)
