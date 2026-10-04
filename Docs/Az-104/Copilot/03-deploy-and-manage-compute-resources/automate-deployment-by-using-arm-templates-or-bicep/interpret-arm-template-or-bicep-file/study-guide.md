# Interpret an ARM template or Bicep file

## What
Read infrastructure-as-code (IaC) as a declarative description of Azure resources: parameters, variables, resource types and API versions, properties, dependencies, outputs, and deployment scope. Bicep is a concise DSL compiled to an ARM JSON template; neither is an imperative sequence.

## Why
Interpretation exposes what a deployment will create or change before it runs. For architects, review identity and network boundaries, region/availability choices, SKU and capacity costs, data exposure, and whether names or values are reusable between environments. Explicit dependencies affect deployment ordering, not runtime availability.

## How
Start with `targetScope`, parameters and defaults, then trace referenced variables into each resource's `type`, `apiVersion`, `name`, `location`, SKU, identity, and properties. Check `dependsOn` only where implicit dependencies do not exist, and inspect outputs for accidental sensitive data. In portal, open the template/Bicep source and deployment details; locally use `az bicep build` to inspect generated JSON and `az deployment group what-if` to preview a resource-group deployment. Confirm scope matches the target (resource group, subscription, management group, or tenant).

## Features
Parameters separate configuration from code; modules/templates encourage reuse; symbolic references in Bicep establish implicit dependencies. What-if is a preview, not a guarantee against every runtime or policy failure. API versions determine available schema and behavior. Secure parameters and outputs help avoid exposing secrets, but prefer Key Vault references or managed identity rather than embedding credentials.

## Code snippets (if any)
No snippet required: this skill is primarily template reading. For review, use `az bicep build --file <path-to-main.bicep>` and inspect the compiled output; do not put secrets in parameter files.

## Do's and Don'ts
**Do** trace parameter-to-property flow and verify deployment scope, region, and API version. **Don't** infer runtime ordering from file order, assume a successful what-if means deployment will succeed, or print credentials in outputs.

## Real-life implementation
Before approving a shared platform module, compare the what-if output against a change request, verify private access and managed identity settings, and estimate the SKU/replica cost. Pin and test API versions in a non-production subscription; use policy and RBAC at the correct scope to enforce organizational guardrails.

## Q&A
1. **Does Bicep deploy directly?** The CLI compiles it to ARM JSON; Azure Resource Manager executes the resulting deployment.
2. **Does `dependsOn` make a VM highly available?** No. It orders provisioning; availability design needs zones, sets, scale sets, and health/recovery planning.
3. **What-if says no changes. Is deployment risk-free?** No. Provider validation, runtime conditions, permissions, quota, and policy can still cause failure.

**References:** [Bicep overview](https://learn.microsoft.com/azure/azure-resource-manager/bicep/overview) · [ARM template structure](https://learn.microsoft.com/azure/azure-resource-manager/templates/syntax)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#automate-deployment-by-using-arm-templates-or-bicep)
