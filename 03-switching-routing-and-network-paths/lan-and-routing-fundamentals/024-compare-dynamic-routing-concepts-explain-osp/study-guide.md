# Study Guide: Compare dynamic routing concepts; explain OSPF's intra-domain role and BGP's inter-domain/policy role, autonomous systems, peering, route propagation, and convergence at a conceptual level

> **Exact syllabus objective:** Compare dynamic routing concepts; explain OSPF's intra-domain role and BGP's inter-domain/policy role, autonomous systems, peering, route propagation, and convergence at a conceptual level.
>
> **Track:** Role extension · **Priority:** P2 · **Roles:** A/S

**Location:** [03. Switching, routing, and network paths](../../index.md) · **Topic:** LAN and routing fundamentals · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

OSPF is an interior routing protocol; BGP exchanges routes using policy between autonomous systems and also serves enterprise/cloud designs. The architecture lens for this outcome is **Reason about how traffic is switched, routed, filtered, and returned across network boundaries.**. Keep the exact scope in the quoted syllabus objective; adjacent technologies matter only where they alter the defined flow, trust boundary, user impact, or ownership.

## Why

Convergence and route ownership affect recovery across independently operated networks. For a failed service path, predict the next hop before probing. Compare the source route, the first boundary's flow evidence, and the return path. Networks are shared systems: an unexplained route, policy, address, or dependency can affect multiple services and teams. A design must make the consequence and its owner visible, not just show that a configuration can be created.

## How

For the exact flow, identify the selected route and next hop, then verify policy and reverse reachability at each boundary. Compare intended route propagation with effective forwarding.

For this objective, use this focused procedure: Specify allowed prefixes, preference, redundancy, convergence and withdrawal behavior; test in a lab.

**Decision criteria:** prefer the smallest change that satisfies the service requirement, preserves least privilege, and can be observed and rolled back. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Longest-prefix selection, bounded route advertisement, explicit ownership, failure-domain separation, and observable convergence. 
- **Evidence:** name the metric, log, flow record, packet observation, or application trace that distinguishes a fault from expected behavior.
- **Failure modes:** Do not equate a healthy adjacency with correct route propagation.
- **Scale and ownership:** account for provider/CNI/OS-specific limits, shared dependencies, and who responds when the path fails.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
Get-NetRoute -AddressFamily IPv4
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

**Objective-specific caution:** Do not equate a healthy adjacency with correct route propagation.

## Real life implementation

For a failed service path, predict the next hop before probing. Compare the source route, the first boundary's flow evidence, and the return path. Implement the focused procedure by creating a short design note with the requirement, chosen approach, owner, expected flow, failure modes, validation results, and rollback criteria. Test one critical application flow and a relevant failure in a controlled environment; compare evidence with the design before rollout. If traffic volume, trust classification, region, provider, or node OS changes, repeat the validation rather than relying on old assumptions.

## Q&A

**Q: What proves that this objective is complete?**

**A:** You can explain the exact outcome above, apply it to a concrete flow or architecture, describe the decision criteria and failure modes, and show evidence from a safe validation. Specifically: Compare dynamic routing concepts; explain OSPF's intra-domain role and BGP's inter-domain/policy role, autonomous systems, peering, route propagation, and convergence at a conceptual level.

**Q: What is the most common architecture mistake?**

**A:** Treating intended configuration as proof of realized behavior. Confirm implementation, path, control enforcement, and user-visible result separately; document what could not be verified.

## References

- [RFC 4271 — A Border Gateway Protocol 4 (BGP-4)](https://www.rfc-editor.org/rfc/rfc4271)
