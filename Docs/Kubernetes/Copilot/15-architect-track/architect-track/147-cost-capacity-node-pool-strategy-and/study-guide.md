# Objective 147: Cost Capacity Node Pool Strategy And Platform

## Exact syllabus objective

> Cost, capacity, node pool strategy, and platform governance [Architect]

**Syllabus area:** 4.4 Architect track<br>
**Role relevance:** Architect; platform leadership; SRE<br>
**Study path:** Architect track → architect-track

## What

Managed-service, single/multi-cluster, regional, node-pool, and active/active/passive choices distribute responsibilities and failure domains differently. Select a model from isolation, compliance, operational capability, workload dependencies, recovery objectives, and cost.

## Why

More clusters can isolate failure but increase upgrade, policy, identity, telemetry, support, and cost overhead. A managed control plane reduces selected operations; it does not automatically transfer responsibility for workload behavior, identity, policy, storage data, backup, monitoring, capacity, or incident readiness. Exact boundaries are provider-specific.

## How

Map tenancy and workload requirements; name provider and customer owners; quantify steady-state and failover capacity; record identity, DNS, network, and data dependencies; compare alternatives against RTO/RPO, compliance, operational effort, and total cost; rehearse failover and failback before production.

**Objective-specific architect checkpoint:** Record requirements, alternatives, shared-responsibility boundaries, dependencies, capacity/cost, RTO/RPO, and tested failover.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm the active context before changes; provider lifecycle and recovery procedures are environment-specific.

## Features

Managed-control-plane and managed-node models; single- and multi-cluster layouts; regions and failure domains; node pools; workload isolation; active/active and active/passive patterns; capacity and cost planning; standardization/flexibility decisions.

## Code snippets (if any)

```text
Decision record:
  requirements | constraints | options | rejected alternatives
  provider/customer owners per control plane, nodes, IAM, network, storage
  data consistency | identity/DNS dependencies | steady/failover capacity
  RTO/RPO | cost model | failover/failback evidence
```

This is an architecture prompt, not a provider guarantee or a deployable Kubernetes manifest.

## Do's and Don'ts

**Do**
- Document shared responsibility, failure modes, data consistency, recovery objectives, failover triggers, and full cost.
- Include identity, DNS, network, storage, observability, and operational capability in cluster-count decisions.

**Don't**
- Do not call multi-cluster a DR solution without tested data recovery, capacity, identity/DNS dependencies, and failback ownership.
- Do not assume managed control planes operate application security, policy, backup, monitoring, or workload recovery for the customer.

## Real life implementation

An architect compares one multi-zone cluster with regional failover clusters for a regulated workload. The record covers provider-managed control-plane scope, data replication semantics, identity and DNS, duplicated failover capacity, recovery drills, service ownership, and the ongoing cost of operating both regions.

## Q&A

**Q: Does multi-cluster automatically improve availability?** No; it adds independent control planes and cross-cluster dependencies. **Q: Who owns application security in a managed cluster?** The customer/platform retains workload and configuration duties; exact control-plane and node responsibilities are provider-specific. **Q: Is active/active always preferable?** No; consistency, conflict handling, and operational complexity may favor active/passive.

## Official references

- [Kubernetes production environment](https://kubernetes.io/docs/setup/production-environment/)
- [Kubernetes architecture](https://kubernetes.io/docs/concepts/architecture/)

## CKA alignment (separate from the role syllabus)

- **Cluster Architecture, Installation & Configuration** — 25% (adjacent topic).

A role-track label is not an official CKA domain. The adjacent mapping is topic-level only; verify the current CNCF blueprint and version.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
- [kubernetes.io/docs/concepts/services-networking/network-policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [kubernetes.io/docs/concepts/services-networking](https://kubernetes.io/docs/concepts/services-networking/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
