# Deploy resources by using ARM or Bicep

## What
Submit a declarative ARM JSON template or Bicep source to Azure Resource Manager at the intended scope. Deployment operations include validation, preview (what-if), authorization, provider execution, and deployment-history review.

## Why
Repeatable deployments reduce drift and make change review auditable. Scope selection controls which resources can be managed; identity and RBAC determine what the deployment can do. A production rollout should account for quota, region availability, policy, dependencies, cost, and recovery.

## How
Choose resource-group, subscription, management-group, or tenant deployment based on the resources and role assignments required. In portal, use a custom deployment or a template spec; with CLI/PowerShell, validate and run what-if first. The deploying principal needs permissions at the target scope, and any role assignment operation may require elevated authorization. Deploy to a test stage, inspect operations/errors, then promote the same reviewed artifact. Use parameter files for non-secret configuration; handle secrets through secure references.

## Features
ARM tracks deployment operations and supports idempotent declarative updates. Bicep compiles to ARM. What-if previews likely changes; deployment stacks can help manage lifecycle and protection but are not a substitute for reviewing scope. Incremental mode is normally safer than complete mode. For repeatability, pin artifact and module versions and avoid environment-specific values embedded in source.

## Code snippets (if any)
```bash
az deployment group what-if --resource-group <resource-group> --template-file <path-to-main.bicep>
az deployment group create --name <deployment-name> --resource-group <resource-group> --template-file <path-to-main.bicep>
```
Run with an authenticated identity authorized at that resource group; do not include secrets in command-line arguments.

## Do's and Don'ts
**Do** verify scope, principal, parameters, what-if, and delete/replace results. **Don't** assume a deployment is a transaction with automatic rollback or run production changes without a recovery plan.

## Real-life implementation
An application release pipeline deploys a versioned Bicep artifact to a staging RG, evaluates what-if, verifies policy and quota, then obtains production approval. A managed identity receives only the deployment permissions it needs at the target scope.

## Q&A
1. **Can an RG deployment create a subscription-level policy assignment?** No; use an appropriate subscription or management-group deployment scope.
2. **Who needs permission to deploy?** The signed-in deployment principal needs resource permissions at scope; the resources' runtime identities need their own separate permissions.
3. **Does ARM automatically roll back all prior changes after one resource fails?** No. Check deployment operations and design compensating/recovery actions.

**References:** [Deploy Bicep with Azure CLI](https://learn.microsoft.com/azure/azure-resource-manager/bicep/deploy-cli) · [What-if operation](https://learn.microsoft.com/azure/azure-resource-manager/templates/deploy-what-if)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#automate-deployment-by-using-arm-templates-or-bicep)
