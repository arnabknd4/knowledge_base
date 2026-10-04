# Objective 028: Understand Pod Affinity Anti Affinity Topology

## Exact syllabus objective

> Understand Pod affinity/anti-affinity, topology spread, and topological constraints for scheduling quality. [Platform]

**Syllabus area:** 3.2 Pods, workloads, controllers, and jobs<br>
**Role relevance:** Platform; security; developer-experience teams<br>
**Study path:** Pods, workloads, controllers, and jobs → pods-workloads-controllers-and-jobs

## What

The scheduler filters feasible nodes, scores candidates, then binds a Pod. Constraints include requests, selectors, affinity, taints/tolerations, topology spread, priority, and available resources. Scheduling does not provision capacity by itself.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

Placement policy determines resilience, utilization, compliance, and cost. Over-constrained Pods can remain Pending; broad tolerations or affinity can undermine isolation.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Inspect events, requests, feasible pools, topology labels, and capacity. Choose hard versus preferred constraints intentionally, spread replicas across real failure domains, and check whether the node autoscaler can satisfy demand.

**Objective-specific architect checkpoint:** Trace feasibility and scoring constraints; distinguish hard requirements from preferences, verify failure-domain labels/capacity, and state the impact of preemption and autoscaler lag.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

Node/pod affinity; taints/tolerations; topology spread; priority/preemption; scheduler plugins and constraints.

**Role lens:** Platform; security; developer-experience teams should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```yaml
topologySpreadConstraints:
- maxSkew: 1
  topologyKey: topology.kubernetes.io/zone
  whenUnsatisfiable: DoNotSchedule
  labelSelector:
    matchLabels: {app: api}
```
Verify the label and zone capacity exist in the target cluster.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Use hard constraints only for actual requirements, preferred constraints for optimization, and test placement during failure.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Do not assume topology labels are populated or that a toleration provides exclusivity. Avoid constraints that eliminate all recovery placement.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

An API spans zones with spread constraints and capacity to tolerate a zone loss. A batch pool uses taints plus matching tolerations and does not consume reserved system capacity.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: Why is a Pod Pending?** Events expose unsatisfied constraints or resources. **Q: Does preemption add capacity?** No; it may evict lower-priority Pods.

## CKA alignment (separate from the role syllabus)

- **Workloads & Scheduling** — 15%.

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)
- [kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
