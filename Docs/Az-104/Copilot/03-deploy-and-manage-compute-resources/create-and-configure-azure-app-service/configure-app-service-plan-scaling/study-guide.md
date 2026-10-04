# Configure scaling for an App Service plan

## What
Scale up changes the plan's pricing tier/worker capabilities (vertical capacity); scale out changes the number of workers (horizontal capacity). Autoscale can adjust worker count based on metrics, schedules, or predictive behavior where supported.

## Why
Scaling balances response time, availability, quota, and spend. Scaling a shared plan affects all its apps. Horizontal scaling benefits stateless or external-state apps; vertical scaling may help constrained single-instance workloads but can require restart and has a ceiling.

## How
Measure app-level latency, CPU/memory, request queues, and worker health. Upgrade to a tier that supports required features before configuring autoscale. Set minimum/maximum/default instances, thresholds, scale-out/in cooldown, schedules, and alerts; choose metrics meaningful to the bottleneck. Validate quota and regional capacity, test load and scale-in behavior, and ensure sessions/files are not tied to one worker.

## Features
Manual plan scale, autoscale rules, per-app scaling in supported tiers, and zone redundancy (supported tiers/regions) can improve capacity/resilience. Autoscale decisions lag metrics and take time to provision workers. A higher minimum improves warm capacity but raises cost; scale-to-zero is not the standard behavior for dedicated App Service plans.

## Code snippets (if any)
No snippet required: autoscale is a policy configuration in portal/Azure Monitor and depends on measured thresholds, tier, and application behavior. Record min/max and rules in IaC where supported.

## Do's and Don'ts
**Do** use load tests and bounded scaling. **Don't** set aggressive scale-in thresholds that cause flapping, or scale a plan without assessing every app hosted on it.

## Real-life implementation
A public web API starts with two workers, scales out on sustained CPU/request demand with cooldown, and caps capacity based on database connections and quota. A synthetic peak test validates recovery time and cost at maximum.

## Q&A
1. **Scale up versus scale out?** Up changes worker size/tier; out changes worker count.
2. **What usually blocks safe horizontal scaling?** Local/session state, shared plan contention, downstream bottlenecks, or quota.
3. **Does autoscale react instantly to a traffic spike?** No; metric evaluation and worker provisioning introduce delay, so keep sufficient baseline capacity.

**References:** [Scale up an App Service app](https://learn.microsoft.com/azure/app-service/manage-scale-up) · [Scale out an App Service app](https://learn.microsoft.com/azure/app-service/manage-scale-up)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#create-and-configure-azure-app-service)
