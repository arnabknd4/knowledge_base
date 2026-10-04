# Objective 038: Understand Qos Classes Eviction Behavior And

## Exact syllabus objective

> Understand QoS classes, eviction behavior, and the relationship between resource requests, limits, and node pressure. [Core]

**Syllabus area:** 3.4 Resource management, scheduling, autoscaling, and disruption<br>
**Role relevance:** Core operators; DevOps; SRE; Platform; Architect<br>
**Study path:** Resource management, scheduling, autoscaling, and disruption → resource-management-scheduling-autoscaling

## What

Requests inform scheduling and resource accounting; limits constrain consumption according to resource semantics. QoS classification and node-pressure eviction depend on configuration and actual use. Quotas and LimitRanges constrain allocations but do not create capacity.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

Sizing affects placement, throttling, OOM behavior, noisy-neighbor risk, and cost. Excessive requests strand capacity; insufficient requests invite contention and latency.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Measure representative peak and recovery load; set requests from service needs; select limits with latency and safety policy in mind; set tenant quotas; compare use, throttling, and node allocatable capacity over time.

**Objective-specific architect checkpoint:** Use measured requests/limits and leave system/disruption headroom; understand quota as an allocation guardrail rather than capacity and diagnose throttling/OOM behavior from evidence.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

Requests/limits; QoS classes; ResourceQuota and LimitRange; allocatable capacity; pressure and eviction signals.

**Role lens:** Core operators; DevOps; SRE; Platform; Architect should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```yaml
resources:
  requests:
    cpu: 250m
    memory: 256Mi
  limits:
    memory: 512Mi
```
Choose CPU-limit policy using measured latency behavior.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Leave system and daemon headroom, observe throttling/OOMs, and align quotas with real capacity and tenant policy.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Do not assign arbitrary identical values to every workload or operate at full requested capacity without disruption headroom.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

The platform sets namespace guardrails; service owners tune requests from production metrics. Capacity includes system reservations, autoscaler lag, and failure-domain reserve.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: Are requests a latency guarantee?** No; they guide scheduling/accounting. **Q: What if a container exceeds a memory limit?** It may be OOM-terminated; diagnose actual use before changing policy.

## CKA alignment (separate from the role syllabus)

- **Workloads & Scheduling** — 15%.

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/configuration/manage-resources-containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- [kubernetes.io/docs/concepts/policy/resource-quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
- [kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
