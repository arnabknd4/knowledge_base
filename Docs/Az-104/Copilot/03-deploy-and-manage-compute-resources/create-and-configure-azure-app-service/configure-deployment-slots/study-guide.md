# Configure deployment slots for an App Service

## What
Deployment slots are live app instances with separate hostnames in a supported App Service plan. They enable staged deployments and slot swaps; a swap moves eligible configuration/content between production and a nonproduction slot.

## Why
Slots reduce release downtime and enable pre-production validation and rapid traffic promotion. They do not guarantee zero downtime or safe database compatibility. Slot count, worker capacity, configuration stickiness, warm-up, and plan tier affect availability and cost.

## How
Create a staging slot, deploy the candidate build, configure slot-specific settings (connection strings, endpoints, secrets) as sticky where appropriate, and warm/test health and dependencies. Swap staging with production through portal, CLI, or pipeline after validation; monitor health and logs. Define rollback as a reverse swap only when app/data schema remains compatible. Avoid modifying production-only state during a swap window.

## Features
Slots have independent URLs and settings; some settings can be marked deployment-slot settings to remain with their slot during swap. Swap preview shows configuration changes. The platform warms an app before routing, but app-specific initialization and background tasks need design. Slots require a qualifying plan and additional worker capacity can increase cost.

## Code snippets (if any)
```bash
az webapp deployment slot create --resource-group <resource-group> --name <app-name> --slot <staging-slot>
az webapp deployment slot swap --resource-group <resource-group> --name <app-name> --slot <staging-slot> --target-slot production
```
Run only after reviewing slot-sticky settings and data/schema compatibility.

## Do's and Don'ts
**Do** warm, health-check, and monitor before/after swap. **Don't** assume a reverse swap rolls back database changes or that every setting follows the code.

## Real-life implementation
A CI pipeline deploys a tagged artifact to staging, applies staging-specific backend settings, runs smoke tests, previews the swap, and promotes after approval. Backward-compatible database migrations permit a quick swap-back if telemetry worsens.

## Q&A
1. **What is a slot-sticky setting?** A setting that remains associated with its slot through a swap rather than following the app content.
2. **Does a slot swap roll back database schema?** No. Database migrations need an independent compatible rollback strategy.
3. **Are slots available on every tier?** No; verify the selected plan tier and slot limits.

**References:** [Set up staging environments in App Service](https://learn.microsoft.com/azure/app-service/deploy-staging-slots) · [Swap deployment slots](https://learn.microsoft.com/azure/app-service/deploy-staging-slots)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#create-and-configure-azure-app-service)
