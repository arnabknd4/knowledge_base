# Manage sizing and scaling for containers

## What
Set compute and memory allocation, replica/group count, and scale behavior for ACI and Azure Container Apps. ACI allocates resources to a container group; ACA uses per-replica resources and autoscaling rules. These are different lifecycle models.

## Why
Resource sizing determines latency, throttling, reliability, and cost. Scaling should respond to workload while protecting downstream systems. Consider cold starts, startup duration, concurrency, state, quotas, regional capacity, and minimum/maximum bounds—not just CPU utilization.

## How
Profile a representative workload and observe CPU, memory, request latency, restarts, and queue depth. For ACI, size the group and use external orchestration to create/replace instances when scale is required. For ACA, configure min/max replicas and suitable HTTP, CPU/memory, or event scaler; test scale-out, scale-in, and scale-to-zero behavior. Portal charts and logs aid initial operations; use Azure Monitor and IaC for sustained governance. Load-test the full dependency chain.

## Features
ACI offers straightforward fixed group allocation and restart policy, not built-in horizontal autoscale. ACA supports KEDA-backed scalers, replica limits, revisions, and workload profiles. Scale-to-zero saves idle cost but can create startup latency. Larger allocations or always-on minimums improve performance/readiness but establish a higher cost floor.

## Code snippets (if any)
No snippet required: correct sizing/scaler values depend on observed workload and downstream capacity. Use a load test to derive bounds, then encode those explicit bounds in the deployment configuration.

## Do's and Don'ts
**Do** set upper bounds, alerts, and a load test at peak; include downstream rate limits. **Don't** use scale-out to mask a saturated database or assume ACI automatically creates additional groups.

## Real-life implementation
An event processor runs in ACA with queue-depth scaling, minimum replicas during business hours, a defined maximum tied to database capacity, and controlled scale-to-zero off-hours. Compare queue age and end-to-end latency against cost.

## Q&A
1. **Which service has built-in event-based replica scaling?** ACA; ACI by itself does not provide equivalent autoscale orchestration.
2. **Why might scale-to-zero fail a latency SLO?** The first request/event may wait for a cold replica to start and become ready.
3. **Should replicas scale without a maximum?** No. A maximum controls cost and protects downstream services; quota and capacity also bound scale.

**References:** [ACI overview](https://learn.microsoft.com/azure/container-instances/container-instances-overview) · [Container Apps scaling](https://learn.microsoft.com/azure/container-apps/scale-app)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#provision-and-manage-containers-in-the-azure-portal)
