# Provision a container by using Azure Container Instances

## What
Azure Container Instances (ACI) runs containers without provisioning or managing VM hosts. It is suited to simple containerized tasks and workloads that need rapid startup; it is not a full orchestration platform.

## Why
ACI reduces host management for burst, job, and isolated utility workloads. Architect around its networking, persistence, availability, scaling, and orchestration limitations. For continuously running event-driven services, revisions, ingress, and richer autoscaling, compare Azure Container Apps; for full Kubernetes control, compare AKS.

## How
Choose image source (often private ACR), CPU/memory allocation, region, restart policy, port exposure, DNS/network mode, and secrets handling. Prefer managed identity for ACR pulls where supported. Portal deployment lets you specify container settings and inspect logs/events; CLI/IaC supports repeatable deployment. Test startup probes, resource limits, outbound access, and graceful termination. ACI group placement and networking options affect isolation and reachability.

## Features
Container groups can contain related containers sharing lifecycle, network, and storage. Restart policies include `Always`, `OnFailure`, and `Never`; choose by job/service semantics. Persistent storage options are limited compared with orchestrated services. ACI does not provide native horizontal autoscaling or full deployment rollout management.

## Code snippets (if any)
```bash
az container create --resource-group <resource-group> --name <container-group-name> --image <registry>/<repository>:<immutable-tag> --cpu <cpu-count> --memory <memory-gb> --restart-policy <Always-or-OnFailure-or-Never> --assign-identity
```
For a private image, configure the registry identity/pull permissions before deployment. Do not pass passwords in CLI arguments.

## Do's and Don'ts
**Do** choose restart policy and logs/monitoring for the workload type. **Don't** expect ACI alone to orchestrate multi-replica high availability or apply Kubernetes manifests.

## Real-life implementation
A nightly conversion job runs as ACI with `Never` restart policy, pulls a version-pinned image using identity, reads/writes through controlled storage access, emits logs to the configured monitoring destination, and reports job status to its scheduler.

## Q&A
1. **Does ACI require an AKS cluster?** No, ACI runs containers without the customer managing cluster nodes.
2. **Does `Always` provide high availability across zones?** No. It controls restart behavior for the group, not multi-zone service resilience.
3. **When choose Container Apps instead?** When the service needs revisions, ingress, event-based autoscaling, or more managed application lifecycle.

**References:** [ACI overview](https://learn.microsoft.com/azure/container-instances/container-instances-overview) · [ACI restart policy](https://learn.microsoft.com/azure/container-instances/container-instances-restart-policy)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#provision-and-manage-containers-in-the-azure-portal)
