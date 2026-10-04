# Objective 019: Know Rollout Revision History Rollout Strategy

## Exact syllabus objective

> Know rollout, revision history, rollout strategy, and rollback procedures for Deployments. [Core]

**Syllabus area:** 3.2 Pods, workloads, controllers, and jobs<br>
**Role relevance:** Core operators; DevOps; SRE; Platform; Architect<br>
**Study path:** Pods, workloads, controllers, and jobs → pods-workloads-controllers-and-jobs

## What

A Deployment changes its Pod template and tracks ReplicaSet revisions. RollingUpdate parameters control concurrent replacement; rollback restores a prior template, not external database writes or side effects.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

Progressive releases limit blast radius only when readiness and release gates are meaningful. Revision history is diagnostic state, not a substitute for artifact provenance or backward-compatible migrations.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Review the manifest diff; deploy a versioned immutable image; watch events and rollout status; check service SLOs; stop or revert when gates fail. Keep schema changes compatible while old and new replicas overlap.

**Objective-specific architect checkpoint:** Define readiness, traffic, SLO, and rollback gates. A Deployment template rollback cannot reverse schema changes, data writes, or other external side effects.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

RollingUpdate/Recreate strategies; maxSurge/maxUnavailable; revision history; status/history/undo; readiness-gated availability. Canary traffic splitting may require a controller or separate rollout tool.

**Role lens:** Core operators; DevOps; SRE; Platform; Architect should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```sh
kubectl rollout status deployment/web -n app --timeout=120s
kubectl rollout history deployment/web -n app
kubectl rollout undo deployment/web -n app
```
Undo reverts the template; validate data compatibility separately.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Use readiness gates, staged exposure, error/latency checks, immutable artifacts, and explicit rollback criteria.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Do not assume rollback undoes schema changes or that Pod readiness proves end-to-end correctness.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

A canary receives limited traffic through a supported routing layer. SLO checks compare latency/error rate with stable replicas and halt promotion on threshold breach.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: What does `rollout undo` revert?** A stored Deployment template revision. **Q: Is canary behavior built into every Deployment?** No; traffic splitting generally requires an implementation/tool.

## CKA alignment (separate from the role syllabus)

- **Workloads & Scheduling** — 15%.

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/workloads/controllers/deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
