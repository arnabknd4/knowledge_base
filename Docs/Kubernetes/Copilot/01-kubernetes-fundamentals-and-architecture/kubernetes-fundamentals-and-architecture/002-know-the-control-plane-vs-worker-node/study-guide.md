# Objective 002: Know The Control Plane Vs Worker Node Split And

## Exact syllabus objective

> Know the control plane vs worker node split and production HA topology. [Core]

**Syllabus area:** 3.1 Kubernetes fundamentals and architecture<br>
**Role relevance:** Core operators; DevOps; SRE; Platform; Architect<br>
**Study path:** Kubernetes fundamentals and architecture → kubernetes-fundamentals-and-architecture

## What

Kubernetes reconciles declarative desired state through controllers; the API is a contract, not a promise that every distribution behaves identically. Separate control-plane availability from workload availability and identify which failure domains the design tolerates.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

A healthy API server does not prove that workloads can reach storage or each other. The boundary between control plane, nodes, and external dependencies determines ownership, upgrades, and recovery.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Trace an API change through admission/persistence, controller or scheduler decisions, and kubelet/runtime execution. Draw the control-plane/data-plane boundary, record dependencies, and state what happens when each is unavailable.

**Objective-specific architect checkpoint:** Draw the control-plane/worker boundary and supported failure domains; distinguish quorum/API availability from workload capacity, then state what redundancy and recovery each layer requires.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

Declarative API; asynchronous reconciliation; distinct control-plane and data-plane failure modes; pluggable implementations; HA across supported failure domains.

**Role lens:** Core operators; DevOps; SRE; Platform; Architect should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```sh
kubectl cluster-info
kubectl get nodes -o wide
kubectl get --raw=/readyz?verbose
```
Managed clusters may restrict component endpoints and host access.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Document component ownership, dependencies, quorum-sensitive state, failure domains, and recovery objectives; validate control-plane HA separately from replica placement.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Do not equate several worker nodes with control-plane HA or self-healing with recovery of deleted data. Component topology differs by distribution.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

A regional design places control-plane replicas and workers across supported failure domains and has a tested etcd recovery plan. For managed control planes, confirm provider guarantees; application and policy ownership remains explicit.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: Does a healthy control plane prove service health?** No; verify workload data paths and SLOs independently. **Q: What is the useful design artifact?** A failure-mode diagram with owners and recovery actions.

## CKA alignment (separate from the role syllabus)

- **Cluster Architecture, Installation & Configuration** — 25%.

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/architecture](https://kubernetes.io/docs/concepts/architecture/)
- [kubernetes.io/docs/setup/production-environment](https://kubernetes.io/docs/setup/production-environment/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
