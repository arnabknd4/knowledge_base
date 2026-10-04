# Objective 131: Backup And Restore Planning For Etcd And

## Exact syllabus objective

> Backup and restore planning for etcd and stateful workloads [SRE]

**Syllabus area:** 4.2 SRE track<br>
**Role relevance:** SRE; operations/platform teams<br>
**Study path:** SRE track → sre-track

## What

PVCs request storage; StorageClasses describe provisioning policy; PVs represent capacity; CSI drivers connect Kubernetes storage APIs to specific backends. Access modes do not promise universal concurrent-write behavior.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

Storage choices determine durability, performance, topology, recovery time, data integrity, and cost. Provisioning, reclaim policy, expansion, snapshots, and backup must match the application contract.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Classify durability/performance and RTO/RPO; select a supported CSI class; verify topology, access and reclaim behavior; test expansion and restore in the target environment. Coordinate application consistency with snapshots.

**Objective-specific architect checkpoint:** Define a version-matched etcd snapshot/restore procedure, key protection, retention, isolated restore drill, and RTO/RPO; back up application volumes and external dependencies separately.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

PVC/PV lifecycle; dynamic provisioning; StorageClass parameters; CSI attach/mount; topology constraints; driver-dependent snapshots and expansion.

**Role lens:** SRE; operations/platform teams should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

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

- **Storage** — 10% (adjacent topic).

A role-track label is not an official CKA domain. The adjacent mapping is topic-level only; verify the current CNCF blueprint and version.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/storage](https://kubernetes.io/docs/concepts/storage/)
- [kubernetes.io/docs/concepts/storage/persistent-volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [kubernetes.io/docs/concepts/storage/storage-classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
