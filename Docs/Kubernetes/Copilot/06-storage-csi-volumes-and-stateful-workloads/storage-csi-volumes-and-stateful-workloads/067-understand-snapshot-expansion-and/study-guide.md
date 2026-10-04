# Objective 067: Understand Snapshot Expansion And Backup

## Exact syllabus objective

> Understand snapshot, expansion, and backup implications for stateful workloads. [Platform]

**Syllabus area:** 3.6 Storage, CSI, volumes, and stateful workloads<br>
**Role relevance:** Platform; security; developer-experience teams<br>
**Study path:** Storage, CSI, volumes, and stateful workloads → storage-csi-volumes-and-stateful-workloads

## What

PVCs request storage; StorageClasses describe provisioning policy; PVs represent capacity; CSI drivers connect Kubernetes storage APIs to specific backends. Access modes do not promise universal concurrent-write behavior.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

Storage choices determine durability, performance, topology, recovery time, data integrity, and cost. Provisioning, reclaim policy, expansion, snapshots, and backup must match the application contract.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Classify durability/performance and RTO/RPO; select a supported CSI class; verify topology, access and reclaim behavior; test expansion and restore in the target environment. Coordinate application consistency with snapshots.

**Objective-specific architect checkpoint:** Verify PVC/PV lifecycle, CSI support, topology, access/reclaim semantics, expansion and snapshot behavior; test application-consistent backup restore to the required RTO/RPO.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

PVC/PV lifecycle; dynamic provisioning; StorageClass parameters; CSI attach/mount; topology constraints; driver-dependent snapshots and expansion.

**Role lens:** Platform; security; developer-experience teams should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata: {name: data, namespace: app}
spec:
  accessModes: [ReadWriteOnce]
  storageClassName: approved-ssd
  resources:
    requests: {storage: 20Gi}
```
Class, access mode, and features depend on the storage driver.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Test restores, understand reclaim semantics, monitor capacity/latency, and validate application consistency.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Do not assume deleting a claim is safe, a snapshot is an application-consistent backup, or a managed control plane backs up volume data.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

A stateful service uses a validated CSI class; recovery drills restore protected data to an isolated cluster and verify application-level integrity.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: Does Kubernetes provide the storage backend?** No; the CSI/provider implementation does. **Q: Is a snapshot a complete DR strategy?** No; retention, consistency, isolation, and restore must be tested.

## CKA alignment (separate from the role syllabus)

- **Storage** — 10%.

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/storage](https://kubernetes.io/docs/concepts/storage/)
- [kubernetes.io/docs/concepts/storage/persistent-volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [kubernetes.io/docs/concepts/storage/storage-classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
