# Objective 094: Understand How To Diagnose Pending

## Exact syllabus objective

> Understand how to diagnose Pending, CrashLoopBackOff, ImagePullBackOff, OOMKilled, Evicted, NotReady, and network policy-related failures. [SRE]

**Syllabus area:** 3.9 Observability, SLOs, monitoring, logging, and troubleshooting<br>
**Role relevance:** SRE; operations/platform teams<br>
**Study path:** Observability, SLOs, monitoring, logging, and troubleshooting → observability-slos-monitoring-logging-and

## What

Kubernetes exposes object status, events, component/node metrics, and logs. Application telemetry adds request metrics, traces, and structured logs. metrics-server, Prometheus, Grafana, Loki, and OpenTelemetry are ecosystem components with separate operations and retention.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

No single signal explains every failure. Correlating API events, scheduling/runtime state, network/storage health, and application SLIs separates cause from symptom.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Start with user impact and time window; correlate SLI dashboards with events and deployments; inspect conditions, logs, metrics, and traces; capture evidence; restore service; record follow-up actions.

**Objective-specific architect checkpoint:** Correlate events, previous-container logs, scheduling constraints, registry authentication, resource pressure, and eviction signals before changing a workload.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

Metrics, logs, events, traces; platform and application telemetry; retention/cardinality/cost; alerts and runbooks; managed control-plane visibility varies.

**Role lens:** SRE; operations/platform teams should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```sh
kubectl get events -A --sort-by=.lastTimestamp
kubectl describe pod POD -n NAMESPACE
kubectl logs POD -n NAMESPACE --all-containers --since=15m
kubectl top nodes
```
`top` needs a compatible metrics source.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Define SLOs, attach actionable runbooks, preserve incident evidence, and budget telemetry cardinality, access, and retention.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Do not infer health from absent metrics, page on every event, or assume cluster logs replace application traces and user-facing SLIs.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

An error-budget alert links to dashboards and a runbook. SRE correlates a rollout, Pod events, traces, and dependency latency, then adds missing instrumentation as follow-up.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: Is `kubectl top` a complete monitoring system?** No; it is a resource-metrics view. **Q: Should every alert page?** Only actionable conditions with ownership and response guidance.

## CKA alignment (separate from the role syllabus)

- **Troubleshooting** — 30%.

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/tasks/debug](https://kubernetes.io/docs/tasks/debug/)
- [kubernetes.io/docs/concepts/cluster-administration/logging](https://kubernetes.io/docs/concepts/cluster-administration/logging/)
- [kubernetes.io/docs/concepts/cluster-administration/monitoring](https://kubernetes.io/docs/concepts/cluster-administration/monitoring/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
