# Study Guide: Explain DNS resolution, caching/TTL, recursive versus authoritative service, zones, and common A/AAAA/CNAME/NS/PTR/TXT records

> **Exact syllabus objective:** Explain DNS resolution, caching/TTL, recursive versus authoritative service, zones, and common A/AAAA/CNAME/NS/PTR/TXT records.
>
> **Track:** Core · **Priority:** P1 · **Roles:** D/P/S/A

**Location:** [02. Addressing, subnetting, and core protocols](../../index.md) · **Topic:** Transport, naming, configuration, and application protocols · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

DNS is distributed: recursive resolvers query authoritative zones and caches apply TTLs, negative answers and aliases. The architecture lens for this outcome is **Build a collision-free address plan and reason about the protocol behavior needed by applications.**. Keep the exact scope in the quoted syllabus objective; adjacent technologies matter only where they alter the defined flow, trust boundary, user impact, or ownership.

## Why

Clients on different resolver paths may see different answers or stale data. A cloud workload can fail despite a valid subnet when resolver, route, protocol, or return path differs. Validate a deployment from its actual source and record the observed address and path. Networks are shared systems: an unexplained route, policy, address, or dependency can affect multiple services and teams. A design must make the consequence and its owner visible, not just show that a configuration can be created.

## How

Specify source, destination, protocol, resolver, and expected path. Check allocation, route, record, and socket state from the workload context; validate the return path and both expected and denied behavior.

For this objective, use this focused procedure: Record query type, resolver, answer, CNAME chain, TTL and response code; compare affected and healthy clients.

**Decision criteria:** prefer the smallest change that satisfies the service requirement, preserves least privilege, and can be observed and rolled back. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Hierarchical IPAM, non-overlapping pools, explicit DNS ownership, transport-aware rules, and documented provider reservations. Plan TTLs around change windows and monitor resolver latency/error rates.
- **Evidence:** name the metric, log, flow record, packet observation, or application trace that distinguishes a fault from expected behavior.
- **Failure modes:** Do not assume one successful lookup proves every client sees the same answer.
- **Scale and ownership:** account for provider/CNI/OS-specific limits, shared dependencies, and who responds when the path fails.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
Resolve-DnsName service.example
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

**Objective-specific caution:** Do not assume one successful lookup proves every client sees the same answer.

## Real life implementation

A cloud workload can fail despite a valid subnet when resolver, route, protocol, or return path differs. Validate a deployment from its actual source and record the observed address and path. Implement the focused procedure by creating a short design note with the requirement, chosen approach, owner, expected flow, failure modes, validation results, and rollback criteria. Test one critical application flow and a relevant failure in a controlled environment; compare evidence with the design before rollout. If traffic volume, trust classification, region, provider, or node OS changes, repeat the validation rather than relying on old assumptions.

## Q&A

**Q: What proves that this objective is complete?**

**A:** You can explain the exact outcome above, apply it to a concrete flow or architecture, describe the decision criteria and failure modes, and show evidence from a safe validation. Specifically: Explain DNS resolution, caching/TTL, recursive versus authoritative service, zones, and common A/AAAA/CNAME/NS/PTR/TXT records.

**Q: What is the most common architecture mistake?**

**A:** Treating intended configuration as proof of realized behavior. Confirm implementation, path, control enforcement, and user-visible result separately; document what could not be verified.

## References

- [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034)
- [RFC 1035 — Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035)
