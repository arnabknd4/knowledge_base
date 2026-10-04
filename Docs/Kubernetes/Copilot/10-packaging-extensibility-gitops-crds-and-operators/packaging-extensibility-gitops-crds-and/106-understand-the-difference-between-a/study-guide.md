# Objective 106: Understand The Difference Between A Crd And A

## Exact syllabus objective

> Understand the difference between a CRD and a full runtime controller/operator model. [Platform]

**Syllabus area:** 3.10 Packaging, extensibility, GitOps, CRDs, and operators<br>
**Role relevance:** Platform; security; developer-experience teams<br>
**Study path:** Packaging, extensibility, GitOps, CRDs, and operators → packaging-extensibility-gitops-crds-and

## What

Helm packages templates and values; Kustomize composes bases and overlays; GitOps controllers reconcile declared state. A CRD defines an API type; a controller/operator implements ongoing behavior.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

Packaging adds version, drift, and upgrade concerns. GitOps does not solve RBAC, secrets, policy, or observability. Extensions need controller availability and an API lifecycle plan.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Choose one source of truth and ownership boundary; render and validate against the target API; pin versions; separate environment configuration; test reconciliation, upgrades, rollback, and CRD/controller sequencing.

**Objective-specific architect checkpoint:** Define one source-of-truth and controller owner; pin/chart or overlay versions, review rendered manifests, sequence CRD/controller upgrades, and observe reconciliation separately from app health.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

Helm chart values/releases; Kustomize overlays; Git reconciliation; custom API schemas; reconciliation loops; versioned dependencies.

**Role lens:** Platform; security; developer-experience teams should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```sh
kubectl kustomize overlays/staging
# Helm, if installed: helm template app ./chart -f values-staging.yaml
```
Render and inspect; these commands do not apply resources.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Pin versions, protect repository credentials, review rendered YAML, and define ownership so competing reconcilers do not overwrite each other.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Do not store plaintext secrets in Git or create a CRD without ownership, support, upgrade, and controller plans.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

A platform repository contains versioned charts and overlays. A scoped GitOps identity reconciles staging and production; readiness and sync status are monitored separately.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: Is a CRD an Operator?** No; the controller/operator implements behavior. **Q: Does GitOps guarantee application health?** No; reconciliation status and application SLOs are separate.

## CKA alignment (separate from the role syllabus)

- **Related platform/architecture practice; no direct domain named in the cited list** — not a separate domain.

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
- [kubernetes.io/docs/concepts/extend-kubernetes/operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
- [kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/)
- [helm.sh/docs](https://helm.sh/docs/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
