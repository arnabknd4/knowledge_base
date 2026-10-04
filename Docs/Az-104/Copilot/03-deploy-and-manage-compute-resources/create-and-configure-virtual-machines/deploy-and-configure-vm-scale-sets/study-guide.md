# Deploy and configure Azure Virtual Machine Scale Sets

## What
A VM Scale Set (VMSS) manages a group of load-balanced, autoscaling VM instances from a common model. Flexible orchestration offers broader VM flexibility and availability-zone placement; Uniform is suited to homogeneous scale-out fleets with integrated scale-set behavior.

## Why
VMSS automates horizontal capacity and instance lifecycle for stateless or partitionable workloads. Architect for the scale trigger, boot time, image rollout, state externalization, capacity limits, and cost floors. Autoscale cannot make a non-scalable application horizontally safe.

## How
Choose orchestration mode and zone/availability model at design time. Define image, instance SKU, network, identity, disk, health extension/probe, and upgrade policy. Configure autoscale rules on meaningful metrics with minimum/maximum/ default capacity, cooldown, and schedules. Use portal, CLI, or IaC, then test scale-out/in and failed-instance replacement under load. Put state in resilient external services and ensure graceful drain before scale-in.

## Features
Scale sets support instance management, autoscale, rolling upgrades, health monitoring, and integration with Azure Load Balancer/Application Gateway. Spot instances can reduce cost but may be evicted; use only for interruption-tolerant work. Capacity reservations and SKU/zone availability can affect scale-out guarantees.

## Code snippets (if any)
No snippet required: VMSS configuration is lengthy and depends on orchestration, image, networking, and upgrade policy. Use the portal or Bicep/ARM with explicit minimum/maximum capacity and health configuration.

## Do's and Don'ts
**Do** define safe scale-in behavior and test image upgrades. **Don't** store session state only on one instance or rely on autoscale as a substitute for resilience and quota planning.

## Real-life implementation
A web tier scales on request/CPU metrics with a nonzero minimum, zone distribution, health probes, managed identity, and rolling image upgrades. The team tests warm-up, session handling, graceful draining, quota, and regional capacity before launch.

## Q&A
1. **What is the main architecture difference between scale-out and scale-up?** Scale-out adds instances; scale-up changes instance capacity. Scale-out requires workload and state design for multiple nodes.
2. **What protects a VMSS instance from serving traffic when unhealthy?** Health monitoring integrated with the load balancer/orchestration; verify probe and repair configuration.
3. **Should Spot VMs host a critical singleton?** No; eviction is possible. Use only for interruption-tolerant workloads with fallback capacity.

**References:** [Scale sets overview](https://learn.microsoft.com/azure/virtual-machine-scale-sets/overview) · [Autoscale with VM scale sets](https://learn.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-autoscale-overview)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#create-and-configure-virtual-machines)
