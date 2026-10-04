# Objective 001: Understand The Problem Kubernetes Solves

## Exact syllabus objective

> Understand the problem Kubernetes solves: declarative orchestration, self-healing, scaling, and service discovery. [Core]

**Syllabus area:** 3.1 Kubernetes fundamentals and architecture<br>
**Role relevance:** Core operators; DevOps; SRE; Platform; Architect<br>
**Study path:** Kubernetes fundamentals and architecture → kubernetes-fundamentals-and-architecture

## What

Kubernetes is a declarative orchestration system: operators submit desired objects through the API, and controllers repeatedly reconcile observed state toward that specification. This model supports workload placement, replacement after failures, horizontal replica changes, and stable service discovery; it does not make an application stateless or recover deleted data automatically.

The key design distinction is desired state versus observed state. A Deployment expresses replica intent, a controller creates/updates ReplicaSets and Pods, and a Service provides a stable discovery target for selected ready backends.

## Why

Declarative reconciliation makes operations repeatable and enables the platform to correct many forms of drift and transient failure without imperative per-node scripts. It gives teams a consistent API for scheduling and service discovery across nodes and distributions.

The boundary matters: controller self-healing can recreate a Pod, but durable data, application correctness, dependency health, and regional disaster recovery require separate design. Scaling replicas also helps only when the workload and its dependencies can scale.

## How

Describe the desired workload in version-controlled manifests; submit it through the API; observe controller reconciliation, Pod scheduling/readiness, and Service endpoints. Use declarative apply/diff workflows, define health probes and resource requests, and verify both recovery and scale behavior under a controlled lab failure.

**Objective-specific architect checkpoint:** Demonstrate one desired-state change, observe reconciliation to ready Pods and Service discovery, then remove one disposable replica and show controller replacement. Explain what would not self-heal (for example, corrupted external data or a failed dependency).

## Features

Declarative API objects; reconciliation loops; controller-managed workload lifecycle; self-healing by replacement/restart within policy; replica scaling; stable Service discovery independent of Pod IPs; labels/selectors for grouping and routing.

These are platform mechanisms, not application-level correctness guarantees. Actual networking and service forwarding still depend on the selected distribution and network implementation.

## Code snippets (if any)

A minimal declarative example ties replica intent to a stable service selector:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
  namespace: demo
spec:
  replicas: 2
  selector:
    matchLabels: {app: web}
  template:
    metadata:
      labels: {app: web}
    spec:
      containers:
      - name: web
        image: nginx:1.27
        resources:
          requests: {cpu: 100m, memory: 64Mi}
---
apiVersion: v1
kind: Service
metadata:
  name: web
  namespace: demo
spec:
  selector: {app: web}
  ports:
  - port: 80
    targetPort: 80
```

Safe disposable-lab observation:

```sh
kubectl get deployment,pods,service,endpointslices -n demo
kubectl describe deployment web -n demo
```

Use an approved image and test namespace; do not delete production Pods to demonstrate self-healing.

## Do's and Don'ts

**Do**
- Keep desired manifests in reviewed version control and observe reconciliation, rollout conditions, and ready endpoints.
- Design replicas, requests, probes, disruption policy, and dependency capacity together; rehearse recovery in a disposable cluster.

**Don't**
- Do not equate Pod replacement with recovery of persistent or external application data.
- Do not assume more replicas solve a stateful bottleneck, application bug, or unhealthy shared dependency.
- Do not infer a working dataplane merely from creation of a Service object.

## Real life implementation

A stateless API is described by a Deployment with multiple replicas and readiness probes, and exposed through a ClusterIP Service. A node or container failure causes reconciliation to replace the Pod; the Service continues to provide a stable name while ready endpoints change. The team separately monitors the API SLO and protects database state with its own backup/restore strategy.

## Q&A

**Q: What is declarative about Kubernetes?** The client records a desired object; controllers continuously compare actual state with that intent and reconcile differences. **Q: Does self-healing recover persistent data?** No; it can replace or restart workloads, but data recovery needs storage/application backup design. **Q: How does service discovery avoid Pod IP coupling?** Clients use Service identity and selectors rather than tracking ephemeral Pod addresses.

## CKA alignment (separate from the role syllabus)

- **Cluster Architecture, Installation & Configuration** — 25%.

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
- [kubernetes.io/docs/concepts/services-networking/network-policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [kubernetes.io/docs/concepts/services-networking](https://kubernetes.io/docs/concepts/services-networking/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
