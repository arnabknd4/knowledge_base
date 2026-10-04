# Study Guide: Review provider-specific equivalents across at least two clouds without assuming service names imply identical behavior or limits

> **Exact syllabus objective:** Review provider-specific equivalents across at least two clouds without assuming service names imply identical behavior or limits.
>
> **Track:** Role extension · **Priority:** P2 · **Roles:** D/P

**Location:** [06. Cloud, hybrid, and virtual networking](../../index.md) · **Topic:** Provider-independent design · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

Similar cloud service names do not guarantee equivalent routing, policy, endpoint, quota or cost semantics. The architecture lens for this outcome is **Make cloud, hybrid, overlay, and virtual paths explicit across address, route, policy, and provider boundaries.**. Keep the exact scope in the quoted syllabus objective; adjacent technologies matter only where they alter the defined flow, trust boundary, user impact, or ownership.

## Why

Portability assumptions become outages and hidden lock-in. A hybrid change needs validation in both control planes and at the workload dataplane; prove the exact DNS answer, route, and return path. Networks are shared systems: an unexplained route, policy, address, or dependency can affect multiple services and teams. A design must make the consequence and its owner visible, not just show that a configuration can be created.

## How

Draw the source-to-destination path; validate DNS, effective routes, inspection, return paths, address pools, provider limits, and failure ownership. Verify service semantics in the selected provider rather than relying on similar names.

For this objective, use this focused procedure: Compare at least two providers on limits, policy attachment, transit, endpoints, monitoring, cost and owner; prototype critical behavior.

**Decision criteria:** prefer the smallest change that satisfies the service requirement, preserves least privilege, and can be observed and rolled back. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Central IPAM, intentional transit and inspection, private service paths where suitable, documented provider-specific limits, and underlay visibility. 
- **Evidence:** name the metric, log, flow record, packet observation, or application trace that distinguishes a fault from expected behavior.
- **Failure modes:** Abstract intent but keep provider-specific behavior explicit; do not force a false lowest common denominator.
- **Scale and ownership:** account for provider/CNI/OS-specific limits, shared dependencies, and who responds when the path fails.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
Compare VPC and VNet for the same flow; validate distinct routes, policy and limits
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

**Objective-specific caution:** Abstract intent but keep provider-specific behavior explicit; do not force a false lowest common denominator.

## Real life implementation

A hybrid change needs validation in both control planes and at the workload dataplane; prove the exact DNS answer, route, and return path. Implement the focused procedure by creating a short design note with the requirement, chosen approach, owner, expected flow, failure modes, validation results, and rollback criteria. Test one critical application flow and a relevant failure in a controlled environment; compare evidence with the design before rollout. If traffic volume, trust classification, region, provider, or node OS changes, repeat the validation rather than relying on old assumptions.

## Q&A

**Q: What proves that this objective is complete?**

**A:** You can explain the exact outcome above, apply it to a concrete flow or architecture, describe the decision criteria and failure modes, and show evidence from a safe validation. Specifically: Review provider-specific equivalents across at least two clouds without assuming service names imply identical behavior or limits.

**Q: What is the most common architecture mistake?**

**A:** Treating intended configuration as proof of realized behavior. Confirm implementation, path, control enforcement, and user-visible result separately; document what could not be verified.

## References

- [Amazon VPC: What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [Azure Virtual Network overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
- [Google Cloud landing zone: Decide on a network design](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design)
