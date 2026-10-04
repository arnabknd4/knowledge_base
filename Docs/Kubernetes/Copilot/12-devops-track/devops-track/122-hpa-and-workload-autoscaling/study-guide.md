# Objective 122: Hpa And Workload Autoscaling

## Exact syllabus objective

> HPA and workload autoscaling [DevOps]

**Syllabus area:** 4.1 DevOps track<br>
**Role relevance:** DevOps; delivery/platform teams<br>
**Study path:** DevOps track → devops-track

## What

HPA adjusts replica counts using configured metrics; VPA concerns container resource sizing; node autoscaling provisions infrastructure through provider/distribution integrations. These are different feedback loops and time scales.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

Scaling is bounded by metric quality, startup time, quotas, topology, and capacity. More replicas do not fix a saturated database, unscalable singleton, or incorrect resource model.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Set requests and observability first; model demand and scale-up lag; choose min/max and stabilization behavior; verify metrics and node provisioning; load-test scale-out, scale-in, downstream limits, and cost.

**Objective-specific architect checkpoint:** Validate requests, metric availability/freshness, target, min/max and stabilization, downstream limits, scale-up delay, scale-in safety, and provider-specific node provisioning.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

HPA metric targets/behavior; VPA recommendations or updates; node autoscaler provisioning; separate workload and infrastructure control loops.

**Role lens:** DevOps; delivery/platform teams should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```sh
kubectl get hpa -A
kubectl describe hpa NAME -n NAMESPACE
kubectl top pods -n NAMESPACE
```
`top` requires a compatible metrics source; autoscaler availability is environment-specific.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Set realistic bounds and headroom; watch metric freshness, scheduling, startup, and downstream saturation; test scale-in safety.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Do not let competing controllers own the same replica count. HPA needs valid metrics and requests; Cluster Autoscaler is not a core Kubernetes API.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

A web tier scales on CPU and request demand while a node pool integration supplies capacity for unschedulable Pods. Database connections have a separate tested ceiling.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: Why do requested replicas remain Pending?** Quota, constraints, or node capacity may block them. **Q: Is node autoscaling universally present?** No; provider and distribution behavior differs.

## CKA alignment (separate from the role syllabus)

- **Workloads & Scheduling** — 15% (adjacent topic).

A role-track label is not an official CKA domain. The adjacent mapping is topic-level only; verify the current CNCF blueprint and version.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
- [kubernetes.io/docs/concepts/cluster-administration/node-autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/)
- [kubernetes.io/docs/concepts/workloads/autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
