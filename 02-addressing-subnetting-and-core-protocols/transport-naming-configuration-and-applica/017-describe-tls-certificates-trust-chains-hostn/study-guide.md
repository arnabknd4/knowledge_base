# Study Guide: Describe TLS certificates, trust chains, hostname validation, SNI, certificate expiry/rotation, and the difference between encryption in transit and authorization

> **Exact syllabus objective:** Describe TLS certificates, trust chains, hostname validation, SNI, certificate expiry/rotation, and the difference between encryption in transit and authorization.
>
> **Track:** Core · **Priority:** P1 · **Roles:** D/P/S/A

**Location:** [02. Addressing, subnetting, and core protocols](../../index.md) · **Topic:** Transport, naming, configuration, and application protocols · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

TLS validates a peer certificate and protects transport; SNI selects a server identity. Encryption does not authorize the user. The architecture lens for this outcome is **Build a collision-free address plan and reason about the protocol behavior needed by applications.**. Keep the exact scope in the quoted syllabus objective; adjacent technologies matter only where they alter the defined flow, trust boundary, user impact, or ownership.

## Why

Expiry, trust, hostname mismatch and rotation failures can cause outages. A cloud workload can fail despite a valid subnet when resolver, route, protocol, or return path differs. Validate a deployment from its actual source and record the observed address and path. Networks are shared systems: an unexplained route, policy, address, or dependency can affect multiple services and teams. A design must make the consequence and its owner visible, not just show that a configuration can be created.

## How

Specify source, destination, protocol, resolver, and expected path. Check allocation, route, record, and socket state from the workload context; validate the return path and both expected and denied behavior.

For this objective, use this focused procedure: Check SAN, chain, validity, trust store, SNI, renewal and termination boundary; test application authorization separately.

**Decision criteria:** prefer the smallest change that satisfies the service requirement, preserves least privilege, and can be observed and rolled back. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Hierarchical IPAM, non-overlapping pools, explicit DNS ownership, transport-aware rules, and documented provider reservations. 
- **Evidence:** name the metric, log, flow record, packet observation, or application trace that distinguishes a fault from expected behavior.
- **Failure modes:** Automate rotation and alert before expiry; never disable verification as a fix.
- **Scale and ownership:** account for provider/CNI/OS-specific limits, shared dependencies, and who responds when the path fails.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
openssl s_client -connect service.example:443 -servername service.example -verify_return_error
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

**Objective-specific caution:** Automate rotation and alert before expiry; never disable verification as a fix.

## Real life implementation

A cloud workload can fail despite a valid subnet when resolver, route, protocol, or return path differs. Validate a deployment from its actual source and record the observed address and path. Implement the focused procedure by creating a short design note with the requirement, chosen approach, owner, expected flow, failure modes, validation results, and rollback criteria. Test one critical application flow and a relevant failure in a controlled environment; compare evidence with the design before rollout. If traffic volume, trust classification, region, provider, or node OS changes, repeat the validation rather than relying on old assumptions.

## Q&A

**Q: What proves that this objective is complete?**

**A:** You can explain the exact outcome above, apply it to a concrete flow or architecture, describe the decision criteria and failure modes, and show evidence from a safe validation. Specifically: Describe TLS certificates, trust chains, hostname validation, SNI, certificate expiry/rotation, and the difference between encryption in transit and authorization.

**Q: What is the most common architecture mistake?**

**A:** Treating intended configuration as proof of realized behavior. Confirm implementation, path, control enforcement, and user-visible result separately; document what could not be verified.

## References

- [RFC 8446 — The Transport Layer Security (TLS) Protocol Version 1.3](https://www.rfc-editor.org/rfc/rfc8446)
