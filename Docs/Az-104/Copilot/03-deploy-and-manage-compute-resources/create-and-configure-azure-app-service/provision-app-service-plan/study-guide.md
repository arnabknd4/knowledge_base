# Provision an App Service plan

## What
An App Service plan defines the compute resources, operating system, region, pricing tier, and scale boundary for one or more Web Apps, API apps, or Functions (where supported). The app is the deployment/configuration unit; the plan is the shared compute host boundary.

## Why
Plan choice determines features, isolation, performance, scale options, and baseline cost. Apps in the same plan share workers and can compete for CPU/memory; moving or scaling a plan can affect every hosted app. Architects should separate workloads when trust, performance, release, or billing boundaries require it.

## How
Select OS, region, pricing tier, and worker count based on required networking, TLS, slots, backup, scaling, and availability features. Portal creation lets you make or reuse a plan; CLI and IaC make app-plan associations repeatable. Check regional capacity and quota, configure autoscale or zone redundancy only when supported by the tier/region, and establish monitoring and budgets. Evaluate current pricing rather than relying on tier names alone.

## Features
Plans offer Free/Shared, Basic, Standard, Premium, Isolated and other tier variants with differing quotas and capabilities. Dedicated tiers provide reserved app compute; Isolated offers stronger network isolation at higher cost. Multiple apps can share workers. Scaling a plan changes capacity for all its apps; per-app scaling is available in certain tiers.

## Code snippets (if any)
```bash
az appservice plan create --resource-group <resource-group> --name <plan-name> --location <azure-region> --sku <plan-sku> --is-linux
```
Select an SKU with the capabilities and OS required by the app; no secrets are needed.

## Do's and Don'ts
**Do** model plan sharing as a noisy-neighbor and blast-radius decision. **Don't** assume adding apps to an existing plan is free of contention or that every tier supports every feature.

## Real-life implementation
A production API is placed on a supported dedicated plan with capacity for peak traffic and required deployment slots. A low-risk internal app may share that plan only after resource isolation, scaling impact, access, and cost ownership are explicitly reviewed.

## Q&A
1. **Can one plan host multiple apps?** Yes, subject to platform limits; they share plan workers and capacity.
2. **Does scaling the plan affect all apps on it?** It changes shared worker capacity, so all hosted apps can be affected.
3. **Can a Free plan satisfy private networking and production availability needs?** Usually not; check tier feature availability and select a production-capable plan.

**References:** [App Service plans](https://learn.microsoft.com/azure/app-service/overview-hosting-plans) · [Scale up an app](https://learn.microsoft.com/azure/app-service/manage-scale-up)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#create-and-configure-azure-app-service)
