# Study Guide: On Windows, inspect adapter/IP configuration, routes, DNS, listening/connected sockets, firewall rules, and packet evidence using Windows-native tools such as `ipconfig`, `route`, `Get-Net*`, `Test-NetConnection`, and approved capture tooling

> **Exact syllabus objective:** On Windows, inspect adapter/IP configuration, routes, DNS, listening/connected sockets, firewall rules, and packet evidence using Windows-native tools such as `ipconfig`, `route`, `Get-Net*`, `Test-NetConnection`, and approved capture tooling.
>
> **Track:** Core · **Priority:** P1 · **Roles:** D/P/S

**Location:** [08. Observability, troubleshooting, and incident response](../../index.md) · **Topic:** Operating systems and tools · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

Windows evidence includes adapter and IP state, routes, DNS, sockets, firewall and approved capture. The architecture lens for this outcome is **Use platform-appropriate evidence to isolate one failing flow and communicate user impact safely.**. Keep the exact scope in the quoted syllabus objective; adjacent technologies matter only where they alter the defined flow, trust boundary, user impact, or ownership.

## Why

Windows filtering and stack behavior cannot be inferred from Linux commands. A successful low-layer probe is not service recovery. Re-run the original user-facing transaction and record residual uncertainty and impact. Networks are shared systems: an unexplained route, policy, address, or dependency can affect multiple services and teams. A design must make the consequence and its owner visible, not just show that a configuration can be created.

## How

Define source, destination, protocol, and time window. Compare working and failing cases through DNS, route, policy, transport, TLS, and application; preserve evidence and change one variable at a time.

For this objective, use this focused procedure: Use ipconfig, Get-NetRoute, Resolve-DnsName, Get-NetTCPConnection and Test-NetConnection from impacted host.

**Decision criteria:** prefer the smallest change that satisfies the service requirement, preserves least privilege, and can be observed and rolled back. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Read-only-first probes, synchronized timestamps, correlated flow/request identifiers, narrowly scoped captures, and explicit tool limitations. 
- **Evidence:** name the metric, log, flow record, packet observation, or application trace that distinguishes a fault from expected behavior.
- **Failure modes:** Record adapter/profile and effective policy; don't assume a present rule is effective.
- **Scale and ownership:** account for provider/CNI/OS-specific limits, shared dependencies, and who responds when the path fails.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
Get-NetIPConfiguration; Get-NetRoute; Get-NetTCPConnection -State Listen
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

**Objective-specific caution:** Record adapter/profile and effective policy; don't assume a present rule is effective.

## Real life implementation

A successful low-layer probe is not service recovery. Re-run the original user-facing transaction and record residual uncertainty and impact. Implement the focused procedure by creating a short design note with the requirement, chosen approach, owner, expected flow, failure modes, validation results, and rollback criteria. Test one critical application flow and a relevant failure in a controlled environment; compare evidence with the design before rollout. If traffic volume, trust classification, region, provider, or node OS changes, repeat the validation rather than relying on old assumptions.

## Q&A

**Q: What proves that this objective is complete?**

**A:** You can explain the exact outcome above, apply it to a concrete flow or architecture, describe the decision criteria and failure modes, and show evidence from a safe validation. Specifically: On Windows, inspect adapter/IP configuration, routes, DNS, listening/connected sockets, firewall rules, and packet evidence using Windows-native tools such as `ipconfig`, `route`, `Get-Net*`, `Test-NetConnection`, and approved capture tooling.

**Q: What is the most common architecture mistake?**

**A:** Treating intended configuration as proof of realized behavior. Confirm implementation, path, control enforcement, and user-visible result separately; document what could not be verified.

## References

- [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034)
- [RFC 1035 — Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035)
