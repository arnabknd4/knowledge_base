# Provision a container by using Azure Container Apps

## What
Azure Container Apps (ACA) is a managed application platform for containerized services, jobs, and APIs. It abstracts Kubernetes operations while offering revisions, ingress, managed identities, and KEDA-based event scaling.

## Why
ACA fits teams that need container flexibility and scale-to-zero/event-driven patterns without operating Kubernetes. Decide environment isolation, networking, workload profile, ingress, secrets, log destination, and scale rules up front. Compare with ACI for simple tasks and AKS when Kubernetes API/control is required.

## How
Create a Container Apps environment, then app with image, resources, ingress/target port, identity, secrets/references, and scale rules. Use managed identity for ACR pulls and backend authorization. Set minimum/maximum replicas and concurrency thresholds according to latency/SLO and downstream capacity. Deploy a new revision, verify readiness and logs, then shift traffic deliberately. Portal supports guided creation; CLI and IaC improve repeatability.

## Features
Revisions allow multiple versions and traffic splitting; ingress can be external or internal. Dapr integration, jobs, workload profiles, and environment networking support varied designs. KEDA scalers enable event-driven scale, potentially to zero; cold starts and trigger latency matter. Secrets are app-level configuration but should be sourced and rotated safely.

## Code snippets (if any)
```bash
az containerapp create --resource-group <resource-group> --name <app-name> --environment <container-apps-environment> --image <registry>/<repository>:<immutable-tag> --target-port <container-port> --ingress <external-or-internal> --min-replicas <minimum-replicas> --max-replicas <maximum-replicas>
```
Set registry identity, secrets, and authentication through supported secure configuration; do not include secret values in shell history.

## Do's and Don'ts
**Do** define probes, resource requests/limits, scaling boundaries, and revision strategy. **Don't** assume scale-to-zero has no cold-start impact or that splitting traffic makes database schemas backward-compatible.

## Real-life implementation
A public API uses external ingress at the app edge, private backend connectivity, managed identity, ACR image digest, and HTTP concurrency autoscaling with a safe replica cap. A new revision receives test traffic before gradual promotion.

## Q&A
1. **What is an ACA revision?** An immutable snapshot of an app configuration/image version used for rollout and traffic management.
2. **Can an app scale to zero?** Depending on configuration and scaler, yes; account for cold starts and minimum availability.
3. **Does ACA expose a customer-managed Kubernetes cluster?** No; it abstracts cluster operations. Choose AKS if direct Kubernetes control is required.

**References:** [Container Apps overview](https://learn.microsoft.com/azure/container-apps/overview) · [Scale apps in Container Apps](https://learn.microsoft.com/azure/container-apps/scale-app)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#provision-and-manage-containers-in-the-azure-portal)
