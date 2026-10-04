# Objective 023: Use Labels Selectors And Annotations Correctly

## Exact syllabus objective

> Use labels, selectors, and annotations correctly for service discovery, grouping, policy scoping, and automation. [Core]

**Syllabus area:** 3.2 Pods, workloads, controllers, and jobs<br>
**Role relevance:** Core operators; DevOps; SRE; Platform; Architect<br>
**Study path:** Pods, workloads, controllers, and jobs → pods-workloads-controllers-and-jobs

## What

A Pod is the smallest schedulable unit. Deployments manage interchangeable replicas and rollouts; StatefulSets model ordered identity/storage; DaemonSets target nodes; Jobs and CronJobs represent finite or scheduled work. Containers in a Pod share its lifecycle and network identity.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

Choosing a controller from the workload contract avoids accidental data loss, unstable identity, or inappropriate retries. Controller ownership governs replacement and rollout behavior.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Decide whether work is long-running or finite, whether replicas are interchangeable, and where durable state lives. Select the controller; define health, resources, shutdown, and scheduling; test restart and rescheduling.

**Objective-specific architect checkpoint:** Treat labels/selectors as contracts used by controllers, Services, policy, and automation. Keep selectors intentional and stable; annotations are not a secret store.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

Declarative reconciliation; controller-owned replicas; rollout history; stable identity when requested; bounded/scheduled completion; node-scoped workloads.

**Role lens:** Core operators; DevOps; SRE; Platform; Architect should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata: {name: web}
spec:
  replicas: 3
  selector:
    matchLabels: {app: web}
  template:
    metadata:
      labels: {app: web}
    spec:
      terminationGracePeriodSeconds: 30
      containers:
      - name: web
        image: nginx:1.27
```
Use an approved immutable image reference in production.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Use unique selectors, declare health/resource/shutdown behavior, externalize durable state, and test replacement and rollback.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Do not use a Deployment when each replica needs stable identity, or a Job for an unbounded daemon. Pod IP and writable container filesystem are not durable identities.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

A stateless API runs behind a Service as a Deployment; a migration is a bounded Job; a node log agent is a DaemonSet. Persistent application data uses an explicit storage service or volume.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: Does a Deployment create Pods directly?** It manages a ReplicaSet that creates and replaces them. **Q: Do containers in a Pod scale independently?** No; they share a scheduling and lifecycle unit.

## CKA alignment (separate from the role syllabus)

- **Workloads & Scheduling** — 15%.

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/workloads](https://kubernetes.io/docs/concepts/workloads/)
- [kubernetes.io/docs/concepts/workloads/pods](https://kubernetes.io/docs/concepts/workloads/pods/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
