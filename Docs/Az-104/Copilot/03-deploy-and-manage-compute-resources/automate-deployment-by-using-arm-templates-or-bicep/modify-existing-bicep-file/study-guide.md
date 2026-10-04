# Modify an existing Bicep file

## What
Safely evolve a Bicep source file: edit parameters, variables, resource declarations, modules, conditions, loops, outputs, and references while retaining valid types and deployment scope.

## Why
Bicep improves readability and reuse, but source changes still describe real infrastructure changes. A type or SKU edit can replace resources, alter availability, expose data, or raise costs. Shared modules also have consumers whose compatibility must be considered.

## How
Review `targetScope` and module interfaces before changing anything. Use current resource type declarations and provider schemas; use symbolic references for dependencies and existing-resource declarations for resources managed elsewhere. Keep environment values parameterized, sensitive inputs secure, and outputs non-sensitive. Compile with `az bicep build --file <path-to-main.bicep>`, lint with `az bicep lint`, and run what-if through the matching `az deployment <scope> what-if` command. Review all create, modify, delete, and replace operations before deployment.

## Features
Bicep provides type-aware resource definitions, modules, loops, conditions, decorators, and implicit dependencies. `existing` references avoid redeploying a resource. Modules can be versioned via registry aliases; pin a known version for repeatable deployments. Compilation checks syntax and types but cannot validate every runtime or policy constraint.

## Code snippets (if any)
No snippet required; the resource schema is specific to the change. Standard checks: `az bicep build --file <path-to-main.bicep>` and `az bicep lint --file <path-to-main.bicep>`.

## Do's and Don'ts
**Do** make small, reviewable module changes and compare compiled/what-if output. **Don't** rename a deployed resource symbol/name believing it is cosmetic; resource identity is often tied to the deployed name, and a changed name can create a new resource.

## Real-life implementation
When introducing zone redundancy to a reusable module, first verify the service and SKU support zones in each target region. Expose the decision as a constrained parameter, default conservatively, and validate cost, rollout, and consumer compatibility in a test subscription.

## Q&A
1. **Does `existing` import or modify a resource?** No. It references a resource for expressions; declare a deployable resource to create or update it.
2. **Are Bicep resource order and file order deployment order?** No. Dependencies are inferred from symbolic references or specified explicitly when necessary.
3. **Does successful compilation guarantee a successful deployment?** No. RBAC, provider validation, policy, quota, and runtime conditions remain.

**References:** [Bicep file structure](https://learn.microsoft.com/azure/azure-resource-manager/bicep/file) · [Bicep linter](https://learn.microsoft.com/azure/azure-resource-manager/bicep/linter)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#automate-deployment-by-using-arm-templates-or-bicep)
