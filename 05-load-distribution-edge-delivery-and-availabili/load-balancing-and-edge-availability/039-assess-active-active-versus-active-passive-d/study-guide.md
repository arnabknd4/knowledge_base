# Study Guide: Assess active-active versus active-passive designs, redundancy, graceful degradation, failure domains, and tested recovery objectives

> **Exact syllabus objective:** Assess active-active versus active-passive designs, redundancy, graceful degradation, failure domains, and tested recovery objectives.
>
> **Track:** Role extension · **Priority:** P2 · **Roles:** A/S

**Location:** [05. Load distribution, edge delivery, and availability](../../index.md) · **Topic:** Load balancing and edge availability · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

Active-active shares traffic and consistency concerns; active-passive must keep standby ready. RTO/RPO depend on real recovery. The architecture lens for this outcome is **Distribute traffic across healthy capacity and reason about the user-visible effects of edge and dependency failure.**. Keep the exact scope in the quoted syllabus objective; adjacent technologies matter only where they alter the defined flow, trust boundary, user impact, or ownership.

## Why

Untested standby and split-brain can turn redundancy into data loss. During a release or dependency loss, observe edge and origin separately and confirm the surviving capacity can meet the service objective. Networks are shared systems: an unexplained route, policy, address, or dependency can affect multiple services and teams. A design must make the consequence and its owner visible, not just show that a configuration can be created.

## How

Define health from service readiness, document TLS and state boundaries, then test one controlled backend, zone, or dependency failure. Measure detection, traffic movement, recovery, and user impact.

For this objective, use this focused procedure: Set RTO/RPO, consistency and fencing; test failover and failback under load.

**Decision criteria:** prefer the smallest change that satisfies the service requirement, preserves least privilege, and can be observed and rolled back. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Health-aware pools, bounded draining, explicit cache/DNS behavior, zone capacity, and tested failover. 
- **Evidence:** name the metric, log, flow record, packet observation, or application trace that distinguishes a fault from expected behavior.
- **Failure modes:** Do not promote on infrastructure health alone; validate data and user path.
- **Scale and ownership:** account for provider/CNI/OS-specific limits, shared dependencies, and who responds when the path fails.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
RTO 15m; RPO 5m; owner on-call; verify synthetic and consistency check
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

**Objective-specific caution:** Do not promote on infrastructure health alone; validate data and user path.

## Real life implementation

During a release or dependency loss, observe edge and origin separately and confirm the surviving capacity can meet the service objective. Implement the focused procedure by creating a short design note with the requirement, chosen approach, owner, expected flow, failure modes, validation results, and rollback criteria. Test one critical application flow and a relevant failure in a controlled environment; compare evidence with the design before rollout. If traffic volume, trust classification, region, provider, or node OS changes, repeat the validation rather than relying on old assumptions.

## Q&A

**Q: What proves that this objective is complete?**

**A:** You can explain the exact outcome above, apply it to a concrete flow or architecture, describe the decision criteria and failure modes, and show evidence from a safe validation. Specifically: Assess active-active versus active-passive designs, redundancy, graceful degradation, failure domains, and tested recovery objectives.

**Q: What is the most common architecture mistake?**

**A:** Treating intended configuration as proof of realized behavior. Confirm implementation, path, control enforcement, and user-visible result separately; document what could not be verified.

## References

- [Cisco CCNA certification overview](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/enterprise/ccna/index.html)
- [Amazon VPC: What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
