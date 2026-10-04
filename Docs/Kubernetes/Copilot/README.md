# Kubernetes Architect-Level Study Library

Production-oriented study materials for DevOps, SRE, Platform, and Architect roles. Each of the **155** checkboxes in the [source syllabus](copilot-Kubernetes-syllabus.md) maps to exactly one objective guide. The guide's **Exact syllabus objective** preserves the source wording and role label.

## Two distinct scopes

1. **Real-world operations syllabus (main library):** the broad checklist covers architecture, workloads, configuration, scheduling, CNI/CSI, security, lifecycle, observability, GitOps, multi-cluster and cost decisions, role tracks, and production nuances. Role-oriented material is not automatically an official certification domain.
2. **Official CKA alignment (optional and separate):** the [CNCF CKA page](https://www.cncf.io/training/certification/cka/) is the authoritative certification source. The syllabus quotes the following domains and weights: Cluster Architecture, Installation & Configuration (25%); Workloads & Scheduling (15%); Services & Networking (20%); Storage (10%); Troubleshooting (30%). Guide mappings describe relevant topic overlap only. Platform/architect topics such as GitOps, managed-service responsibilities, multi-cluster strategy, and ecosystem controls are broader operational material, not additional official domains.

**Verify the current CNCF CKA blueprint, domain names, weights, and version before planning certification study.** The library is not an official CNCF exam guide; no claim is made that every role objective appears on the exam.

### CKA-to-library crosswalk (topic overlap only)

| CKA domain and syllabus weight | Relevant library subjects (not an assertion that every linked topic is examined) |
|---|---|
| Cluster Architecture, Installation & Configuration — 25% | [Fundamentals and architecture](<01-kubernetes-fundamentals-and-architecture/index.md>), [cluster lifecycle and recovery](<08-cluster-lifecycle-ha-backup-and-recovery/index.md>), and selected [security/API access](<07-security-identity-rbac-workloads-and-admission/index.md>) topics. |
| Workloads & Scheduling — 15% | [Pods and controllers](<02-pods-workloads-controllers-and-jobs/index.md>), [resources and scheduling](<04-resources-scheduling-autoscaling-and-disruption/index.md>), and selected [configuration](<03-configuration-secrets-and-policy-inputs/index.md>) topics. |
| Services & Networking — 20% | [Services, DNS, routing, and CNI](<05-services-networking-dns-ingress-gateway-and-cni/index.md>). Gateway API and CNI details are implementation/version dependent. |
| Storage — 10% | [Storage, CSI, and stateful workloads](<06-storage-csi-volumes-and-stateful-workloads/index.md>). CSI driver behavior is implementation specific. |
| Troubleshooting — 30% | [Observability and troubleshooting](<09-observability-slos-monitoring-and-troubleshooting/index.md>), with related failure diagnosis in [workloads](<02-pods-workloads-controllers-and-jobs/index.md>) and [cluster lifecycle](<08-cluster-lifecycle-ha-backup-and-recovery/index.md>). |

## Domain indexes

- [Kubernetes fundamentals and architecture](<01-kubernetes-fundamentals-and-architecture/index.md>) — 15 guides.
- [Pods, workloads, controllers, and jobs](<02-pods-workloads-controllers-and-jobs/index.md>) — 13 guides.
- [Configuration, Secrets, and policy inputs](<03-configuration-secrets-and-policy-inputs/index.md>) — 8 guides.
- [Resource management, scheduling, autoscaling, and disruption](<04-resources-scheduling-autoscaling-and-disruption/index.md>) — 11 guides.
- [Services, networking, DNS, Ingress, Gateway, and CNI](<05-services-networking-dns-ingress-gateway-and-cni/index.md>) — 14 guides.
- [Storage, CSI, volumes, and stateful workloads](<06-storage-csi-volumes-and-stateful-workloads/index.md>) — 8 guides.
- [Security: identity, RBAC, workloads, admission, and supply chain](<07-security-identity-rbac-workloads-and-admission/index.md>) — 11 guides.
- [Cluster lifecycle, upgrades, high availability, backup, and recovery](<08-cluster-lifecycle-ha-backup-and-recovery/index.md>) — 11 guides.
- [Observability, SLOs, monitoring, logging, and troubleshooting](<09-observability-slos-monitoring-and-troubleshooting/index.md>) — 10 guides.
- [Packaging, extensibility, GitOps, CRDs, and operators](<10-packaging-extensibility-gitops-crds-and-operators/index.md>) — 8 guides.
- [Cloud-managed Kubernetes, multi-cluster, capacity, costs, and architecture choices](<11-cloud-managed-multicluster-capacity-costs-and-architecture/index.md>) — 8 guides.
- [DevOps track](<12-devops-track/index.md>) — 8 guides.
- [SRE track](<13-sre-track/index.md>) — 8 guides.
- [Platform track](<14-platform-track/index.md>) — 8 guides.
- [Architect track](<15-architect-track/index.md>) — 8 guides.
- [Production nuances and anti-patterns](<16-production-nuances-and-anti-patterns/index.md>) — 6 guides.

## Role learning routes

- **DevOps:** [track guides](<12-devops-track/index.md>), plus workload, configuration, network, scaling, packaging, and delivery indexes.
- **SRE:** [track guides](<13-sre-track/index.md>), plus disruption, troubleshooting, observability, lifecycle, and recovery.
- **Platform:** [track guides](<14-platform-track/index.md>), plus policy, tenancy, CNI/Gateway, packaging, and GitOps.
- **Architect:** [track guides](<15-architect-track/index.md>), plus architecture, storage, security, lifecycle, multi-cluster, and responsibility boundaries.

## Practical and capstone checklist

These ten lab/capstone activities preserve the syllabus sequence and wording. The syllabus expresses them as a numbered progression, not objective checkboxes; the linked guides are the relevant preparation and this list does not duplicate any mapped objective. Use a local/disposable cluster for mutations and verify CNI, CSI, gateway, and managed-service boundaries.

1. [ ] Build a local or lab cluster and learn control plane/node basics. [Core] — [Fundamentals](<01-kubernetes-fundamentals-and-architecture/index.md>)
2. [ ] Deploy a stateless app with Service and Ingress or Gateway. [Core] — [Workloads](<02-pods-workloads-controllers-and-jobs/index.md>) · [Networking](<05-services-networking-dns-ingress-gateway-and-cni/index.md>)
3. [ ] Add ConfigMap, Secret, probes, scaling, and rollout/rollback. [Core] — [Configuration](<03-configuration-secrets-and-policy-inputs/index.md>) · [Resources](<04-resources-scheduling-autoscaling-and-disruption/index.md>) · [Workloads](<02-pods-workloads-controllers-and-jobs/index.md>)
4. [ ] Add a StatefulSet with persistent storage and storage class configuration. [Core] — [Workloads](<02-pods-workloads-controllers-and-jobs/index.md>) · [Storage](<06-storage-csi-volumes-and-stateful-workloads/index.md>)
5. [ ] Add RBAC, service accounts, and NetworkPolicy to enforce least privilege. [Core] — [Security](<07-security-identity-rbac-workloads-and-admission/index.md>) · [Networking](<05-services-networking-dns-ingress-gateway-and-cni/index.md>)
6. [ ] Add HPA, PDB, and resource limits to simulate production load. [SRE] — [Resources and scheduling](<04-resources-scheduling-autoscaling-and-disruption/index.md>)
7. [ ] Create a Helm chart or Kustomize overlay flow and compare deployment patterns. [DevOps] — [Packaging](<10-packaging-extensibility-gitops-crds-and-operators/index.md>)
8. [ ] Design a platform guardrail set with policy and GitOps automation. [Platform] — [Platform](<14-platform-track/index.md>) · [Packaging](<10-packaging-extensibility-gitops-crds-and-operators/index.md>)
9. [ ] Design a multi-cluster or multi-region cluster topology with DR and cost model. [Architect] — [Cloud architecture](<11-cloud-managed-multicluster-capacity-costs-and-architecture/index.md>) · [Lifecycle and recovery](<08-cluster-lifecycle-ha-backup-and-recovery/index.md>)
10. [ ] Run a formal incident review on a failed rollout, service outage, or node issue. [SRE] — [Observability and troubleshooting](<09-observability-slos-monitoring-and-troubleshooting/index.md>)

## Coverage

- Source syllabus checkboxes: **155**; objective guides: **155**; duplicates: **0**.
- Every guide contains the exact objective and all required study sections, CKA alignment, and relevant official references.
- Role-track checkboxes are guides. The capstone sequence above links prerequisite domains without generating duplicate objective guides.
