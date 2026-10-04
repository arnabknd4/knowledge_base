# Objective 024: Configure Readiness Liveness And Startup Probes

## Exact syllabus objective

> Configure readiness, liveness, and startup probes correctly for production workloads. [Core]

**Syllabus area:** 3.2 Pods, workloads, controllers, and jobs<br>
**Role relevance:** Core operators; DevOps; SRE; Platform; Architect<br>
**Study path:** Pods, workloads, controllers, and jobs → pods-workloads-controllers-and-jobs

## What

Readiness controls whether a Pod is eligible for traffic; liveness can restart a container that is stuck; startup probes protect slow initialization before the other probes run. A probe must measure the failure its action is intended to handle.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

Misconfigured probes remove healthy capacity or create restart storms. Readiness is an availability signal; liveness is a recovery action. A transient downstream outage should not restart every replica unless that is an intentional recovery policy.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Define a cheap local health check; set timing from measured startup/recovery under load; use startup probes for slow boot; test dependency degradation and termination behavior. Keep readiness and liveness semantics distinct.

**Objective-specific architect checkpoint:** Use readiness to control traffic, liveness to recover a stuck process, and startup to protect slow initialization; tune thresholds to measured behavior and test dependency failures.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

HTTP, TCP, and exec probes; independent readiness/liveness behavior; startup protection; endpoint eligibility; initial delay, period, timeout, and failure thresholds.

**Role lens:** Core operators; DevOps; SRE; Platform; Architect should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```yaml
startupProbe:
  httpGet: {path: /healthz, port: 8080}
  periodSeconds: 5
  failureThreshold: 30
readinessProbe:
  httpGet: {path: /ready, port: 8080}
  periodSeconds: 5
livenessProbe:
  httpGet: {path: /live, port: 8080}
  periodSeconds: 10
```
Tune thresholds from measured application behavior.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Keep liveness local and bounded; use readiness to gate serving; set termination grace and probe budgets from measurements.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Do not make liveness fail on every remote dependency or use aggressive timeouts without load testing.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

A slow-starting service receives a startup probe; readiness waits for usable configuration; liveness checks process health so a transient database interruption does not restart all replicas.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: Which probe removes a Pod from ready endpoints?** Readiness. **Q: Does startup replace readiness?** No; readiness and liveness continue after startup succeeds.

## CKA alignment (separate from the role syllabus)

- **Workloads & Scheduling** — 15%.

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/)
- [kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
