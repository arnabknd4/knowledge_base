# Modify an existing ARM template

## What
Change an existing JSON-based ARM template while preserving its schema, parameter contract, resource dependencies, and deployment behavior. Typical edits add or adjust resource properties, parameters, variables, conditions, copy loops, outputs, or linked/nested deployments.

## Why
Existing templates encode platform assumptions and are often consumed by pipelines and other teams. A seemingly small change can replace a resource, break consumers, widen access, change region/SKU costs, or disrupt dependent deployments. Review compatibility and blast radius as well as syntax.

## How
Identify deployment scope and template schema first. Locate the resource by fully qualified type and name; consult the matching provider schema/API version before adding properties. Prefer a new parameter with a safe default over hard-coded environment-specific values; use `secureString`/`secureObject` for sensitive parameter data and avoid outputs that reveal it. Validate JSON, run ARM template validation and what-if at the correct scope, then deploy to a test environment and inspect deployment operations. Portal deployment history helps compare prior input and failures.

## Features
ARM expressions use functions such as `parameters()`, `variables()`, `resourceId()` and `reference()`. Resource IDs should be constructed with scope-aware functions rather than guessed strings. Template specs and linked templates support reuse; version changes require testing callers. Incremental mode is the default for resource-group deployments, while complete mode can delete resources absent from the template—use extreme care.

## Code snippets (if any)
No snippet required; exact JSON edits depend on the target resource provider schema. Validate the edited template and use `az deployment group what-if --resource-group <resource-group> --template-file <path-to-template.json>` before deployment.

## Do's and Don'ts
**Do** preserve existing parameters and defaults unless a breaking change is intended; use what-if and review delete/replace operations. **Don't** switch deployment mode casually, put secrets in source control, or assume omitted properties always retain their previous values.

## Real-life implementation
A platform team adds a diagnostic setting to a shared template. It adds a parameterized destination and required role assignment, verifies the target resource supports the API version, checks the what-if result in a non-production RG, and rolls out through a versioned pipeline with approval.

## Q&A
1. **Will incremental mode delete a resource omitted from the template?** No; it generally leaves it. Complete mode can remove it, so confirm scope and impact before using that mode.
2. **How should a secret enter a deployment?** Prefer a Key Vault reference or managed identity flow; if a secure parameter is necessary, do not log or output it.
3. **Why can an ARM-valid template fail on deployment?** The resource provider can reject a property/API version, or the caller may lack RBAC, quota, or policy compliance.

**References:** [ARM template deployment modes](https://learn.microsoft.com/azure/azure-resource-manager/templates/deployment-modes) · [ARM template functions](https://learn.microsoft.com/azure/azure-resource-manager/templates/template-functions)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#automate-deployment-by-using-arm-templates-or-bicep)
