# Objective 045: Design For Disruption Budgets And Safe

## Exact syllabus objective

> Design for disruption budgets and safe maintenance windows, including drain, cordon, uncordon, node replacement, and rolling upgrades. [SRE]

**Syllabus area:** 3.4 Resource management, scheduling, autoscaling, and disruption<br>
**Role relevance:** SRE; operations/platform teams<br>
**Study path:** Resource management, scheduling, autoscaling, and disruption → resource-management-scheduling-autoscaling

## What

A PodDisruptionBudget limits eviction-mediated voluntary disruptions; it does not prevent involuntary failures or guarantee a replica count. Cordon prevents new scheduling; drain requests safe eviction and can block on a PDB or workload policy.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

Maintenance safety requires both replica redundancy and replacement capacity. A PDB can also stall maintenance when stricter than the service can satisfy.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Check replicas, readiness, PDB status, local data, and replacement capacity; drain one failure domain at a time; observe recovery before continuing. Treat blocked eviction as evidence to investigate.

**Objective-specific architect checkpoint:** Check healthy replicas, PDB allowance, local data, and replacement capacity. PDBs constrain voluntary eviction; they do not prevent involuntary failure.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

Eviction API; minAvailable/maxUnavailable; disruption allowance; node cordon/drain/uncordon; controller replacement.

**Role lens:** SRE; operations/platform teams should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```sh
kubectl get pdb -A
kubectl get nodes
kubectl get pods -A -o wide
```
Use drain only in an authorized maintenance window and follow the environment runbook.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Configure budgets to match measured tolerance and verify capacity and health after each node.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- A PDB does not protect against node failure. Do not blindly bypass eviction safeguards with force or local-data deletion flags.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

A worker upgrade advances one node at a time. If eviction is blocked, the team reviews budget and capacity rather than bypassing protection.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: Does a PDB prevent involuntary disruption?** No. **Q: Why can drain stall?** PDBs, unmanaged Pods, storage, or termination; inspect before bypassing.

## CKA alignment (separate from the role syllabus)

- **Workloads & Scheduling** — 15%.

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/workloads/pods/disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)
- [kubernetes.io/docs/tasks/administer-cluster/safely-drain-node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
