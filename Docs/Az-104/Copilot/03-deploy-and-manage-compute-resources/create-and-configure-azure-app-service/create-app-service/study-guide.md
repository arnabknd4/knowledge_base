# Create an App Service

## What
Azure App Service hosts web applications and APIs as a managed platform. The app resource defines runtime stack, deployment configuration, identity, networking, custom hostnames, and diagnostic settings; the App Service plan supplies its compute.

## Why
App Service reduces guest OS and web-server management versus VMs, accelerating delivery and patching. Trade-offs include platform/runtime constraints, plan feature dependence, shared compute, and data/network architecture. Choose it when a managed web runtime meets requirements; use containers or VMs when greater runtime/OS control is essential.

## How
Create the app in the correct subscription, region, plan, OS/runtime, and deployment source. Configure managed identity and least privilege, environment settings without secrets, logging/health checks, TLS, custom hostname, and deployment method. Use portal for initial creation and diagnostics, CLI/PowerShell for operations, and IaC/CI-CD for reproducibility. Validate startup, readiness, logs, scaling, rollback, and identity access in staging.

## Features
App Service supports language runtimes and custom containers, deployment slots (tier dependent), autoscale, managed identity, TLS, backups, VNet integration, and access restrictions with differing plan requirements. Settings may be slot-sticky. Platform-managed hosting does not mean application data is automatically backed up or private.

## Code snippets (if any)
```bash
az webapp create --resource-group <resource-group> --plan <app-service-plan> --name <globally-unique-app-name> --runtime "<supported-runtime>"
```
Use a supported runtime identifier and configure application secrets through a secure store/reference, not inline settings.

## Do's and Don'ts
**Do** decouple app state from local worker storage and enable diagnostics. **Don't** assume app creation enables HTTPS-only, private ingress, backup, or high availability automatically.

## Real-life implementation
A public API uses a production-capable plan, managed identity for database access, HTTPS-only and custom-domain TLS, staging slot, health checks, structured logs, and external durable storage. IaC and pipeline promotion reduce portal drift.

## Q&A
1. **Where does compute capacity come from?** The App Service plan, which can host multiple apps.
2. **Is content in local app storage a durable backup?** No. Design durable storage and configure/test backup separately.
3. **Should app configuration contain credentials?** Prefer managed identity and Key Vault references; never place secrets in source or deployment logs.

**References:** [App Service overview](https://learn.microsoft.com/azure/app-service/overview) · [Create a Node.js app with Azure CLI](https://learn.microsoft.com/azure/app-service/quickstart-nodejs)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#create-and-configure-azure-app-service)
