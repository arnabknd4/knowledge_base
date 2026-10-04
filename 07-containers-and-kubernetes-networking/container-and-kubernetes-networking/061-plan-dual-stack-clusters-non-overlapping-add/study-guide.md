# Study Guide: Plan dual-stack clusters, non-overlapping address pools, multi-cluster connectivity, service exposure, and network-policy governance

> **Exact syllabus objective:** Plan dual-stack clusters, non-overlapping address pools, multi-cluster connectivity, service exposure, and network-policy governance.
>
> **Track:** Role extension · **Priority:** P2 · **Roles:** P/A

**Location:** [07. Containers and Kubernetes networking](../../index.md) · **Topic:** Container and Kubernetes networking · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

IPv6 uses 128-bit prefixes, global/link-local scope, Neighbor Discovery, and SLAAC/DHCPv6; dual-stack adds a second real datapath. The architecture lens for this outcome is **Trace container and Kubernetes traffic through API intent and the actual CNI, node, and service dataplane.**. Keep the exact scope in the quoted syllabus objective; adjacent technologies matter only where they alter the defined flow, trust boundary, user impact, or ownership.

## Why

Partial IPv6 can bypass IPv4-only security or create inconsistent DNS and reachability. An accepted Kubernetes object does not prove dataplane enforcement. Validate from the workload on each supported node/CNI and inspect the effective endpoint and policy. Networks are shared systems: an unexplained route, policy, address, or dependency can affect multiple services and teams. A design must make the consequence and its owner visible, not just show that a configuration can be created.

## How

Identify source Pod/container, destination and node. Check DNS, endpoints/readiness, route, policy, plugin health, OS support, and external NAT in order; test allowed and denied flows.

For this objective, use this focused procedure: Plan prefixes, listeners, routes, policies and telemetry; publish AAAA only after end-to-end readiness.

**Decision criteria:** prefer the smallest change that satisfies the service requirement, preserves least privilege, and can be observed and rolled back. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Non-overlapping address pools, verified CNI enforcement, health-aware endpoints, explicit exposure, and operating-system compatibility. 
- **Evidence:** name the metric, log, flow record, packet observation, or application trace that distinguishes a fault from expected behavior.
- **Failure modes:** Test both families and provider/host support; NAT is not a prerequisite for IPv6.
- **Scale and ownership:** account for provider/CNI/OS-specific limits, shared dependencies, and who responds when the path fails.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
ip -6 route show
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

**Objective-specific caution:** Test both families and provider/host support; NAT is not a prerequisite for IPv6.

## Real life implementation

An accepted Kubernetes object does not prove dataplane enforcement. Validate from the workload on each supported node/CNI and inspect the effective endpoint and policy. Implement the focused procedure by creating a short design note with the requirement, chosen approach, owner, expected flow, failure modes, validation results, and rollback criteria. Test one critical application flow and a relevant failure in a controlled environment; compare evidence with the design before rollout. If traffic volume, trust classification, region, provider, or node OS changes, repeat the validation rather than relying on old assumptions.

## Q&A

**Q: What proves that this objective is complete?**

**A:** You can explain the exact outcome above, apply it to a concrete flow or architecture, describe the decision criteria and failure modes, and show evidence from a safe validation. Specifically: Plan dual-stack clusters, non-overlapping address pools, multi-cluster connectivity, service exposure, and network-policy governance.

**Q: What is the most common architecture mistake?**

**A:** Treating intended configuration as proof of realized behavior. Confirm implementation, path, control enforcement, and user-visible result separately; document what could not be verified.

## References

- [RFC 8200 — Internet Protocol, Version 6 (IPv6) Specification](https://www.rfc-editor.org/rfc/rfc8200)
