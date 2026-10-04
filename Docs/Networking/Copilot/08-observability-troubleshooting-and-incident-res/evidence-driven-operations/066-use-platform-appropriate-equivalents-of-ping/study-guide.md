# Study Guide: Objective 066

> **Exact syllabus objective:** Use platform-appropriate equivalents of `ping`, `traceroute`/`tracert`, `ipconfig`/`ip`, `route`, `nslookup`/`dig`, socket inspection, and packet capture.
>
> **Track:** Core · **Priority:** P1 · **Roles:** D/P/S/A

**Location:** [08. Observability, troubleshooting, and incident response](../../index.md) · **Topic:** Evidence-driven operations · [Source syllabus](../../../copilot-Networking-syllabus.md)

## What

ICMP, traceroute, route, DNS, sockets and captures answer different questions; filtering and OS tooling alter evidence. The architecture lens is **Use platform-appropriate evidence to isolate one failing flow and communicate user impact safely**. Keep adjacent technologies in scope only where they alter this flow, trust boundary, user impact, or ownership.

## Why

Understanding limits avoids false failure/closure. A successful low-layer probe is not service recovery. Re-run the original user-facing transaction and record residual uncertainty and impact.

## How

Define source, destination, protocol, and time window. Compare working and failing cases through DNS, route, policy, transport, TLS, and application; preserve evidence and change one variable at a time.

For this objective, use this focused procedure: Choose native read-only probes at the real source; note endpoint, time, permission, capture point and limitations.

**Decision criteria:** select the smallest change that meets the service need and least-privilege boundary. Record source, destination, protocol, environment, identity, owner, assumptions, and failure domain before changing shared networking.

**Validation:** test from the real workload/client; record expected and actual result, timestamp, and vantage point. Check a negative/denied case where relevant. Correlate dataplane evidence with route, policy, DNS, host, provider, or application evidence. A control-plane success alone is not dataplane proof.

## Features

- **Architectural properties:** Read-only-first probes, synchronized timestamps, correlated flow/request identifiers, narrowly scoped captures, and explicit tool limitations.
- **Objective-specific design note:** Do not scan unrelated ranges or assume ping must work.
- **Evidence:** choose the metric, log, flow record, packet observation, or application trace that can prove the expected behavior from this path.
- **Failure mode to test:** distinguish intended configuration from effective forwarding/enforcement; identify the first boundary with missing evidence and its owner.

## Code snippets (if any)

This safe illustrative example is relevant to the objective. Use only an authorized test endpoint; read-only commands do not prove end-to-end application health.

```text
Resolve-DnsName service.example; Test-NetConnection service.example -Port 443
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
- [AWS Well-Architected Framework: Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
