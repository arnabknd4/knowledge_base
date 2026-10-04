# Objective 124: Ci Cd Integration With Kubernetes Deployment

## Exact syllabus objective

> CI/CD integration with Kubernetes deployment patterns [DevOps]

**Syllabus area:** 4.1 DevOps track<br>
**Role relevance:** DevOps; delivery/platform teams<br>
**Study path:** DevOps track → devops-track

## What

A Kubernetes CI/CD integration connects source changes to tested artifacts and controlled cluster reconciliation. CI builds, tests, scans, and publishes an artifact; delivery promotes that same immutable artifact and applies approved manifests through a deployment identity or a GitOps controller. Kubernetes defines APIs and rollout status, not a mandated pipeline.

## Why

Separating artifact production from environment promotion improves provenance, repeatability, rollback, and auditability. Pipelines are privileged cluster actors; a compromised or over-broad runner can alter workloads or exfiltrate secrets.

## How

Build and test once; publish an immutable image digest with provenance; render manifests and validate schema/policy; obtain required approvals; deploy with namespace-scoped short-lived identity or a scoped GitOps controller; then gate promotion on rollout status and application SLOs. Keep environment configuration separate and define rollback/data-migration limits.

**Objective-specific architect checkpoint:** Draw the artifact and permission path from commit to production, identify who can build, approve, deploy, and reconcile, and show how a failed health gate stops promotion without granting CI cluster-admin.

## Features

Build/test/scan stages; image registry and immutable digests; manifest rendering and server-side validation; provenance/attestation; promotion gates; short-lived workload identity; deployment or GitOps reconciliation; rollout and SLO verification.

## Code snippets (if any)

Read-only/reviewable deployment checks after a controlled pipeline apply:

```sh
kubectl config current-context
kubectl apply --dry-run=server -f rendered/
kubectl diff -f rendered/
kubectl rollout status deployment/api -n app --timeout=120s
```

Use an explicit target context and least-privileged pipeline identity. The dry-run and diff do not deploy; rollout status does not replace application-level health checks.

## Do's and Don'ts

**Do**
- Build once and promote the same digest; record commit, artifact provenance, approvals, deployment identity, and health-gate result.
- Restrict runner or reconciler permissions and rehearse rollback with database/API compatibility constraints.

**Don't**
- Do not store long-lived cluster-admin credentials in CI or rebuild a different image per environment.
- Do not treat successful API apply as successful deployment or service health.

## Real life implementation

A pipeline builds/tests/scans a web image, publishes a digest, and opens a reviewed environment change. A scoped delivery identity applies the rendered manifests; the gate waits for Deployment readiness, Service endpoints, and application error/latency SLOs. If a gate fails, promotion halts and the runbook rolls back the workload template while preserving compatible data state.

## Q&A

**Q: Should each environment rebuild the artifact?** Prefer reproducible build-once promotion of the same digest with environment-specific configuration. **Q: Does `kubectl apply` prove the release is healthy?** No; check controller rollout, ready endpoints, and user-facing SLOs. **Q: Should CI have cluster-admin?** No; use narrow, auditable permissions and separate approval/production boundaries.

## CKA alignment (separate from the role syllabus)

- **Workloads & Scheduling** — 15% (adjacent topic).

A role-track label is not an official CKA domain. The adjacent mapping is topic-level only; verify the current CNCF blueprint and version.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/workloads](https://kubernetes.io/docs/concepts/workloads/)
- [kubernetes.io/docs/concepts/workloads/pods](https://kubernetes.io/docs/concepts/workloads/pods/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
