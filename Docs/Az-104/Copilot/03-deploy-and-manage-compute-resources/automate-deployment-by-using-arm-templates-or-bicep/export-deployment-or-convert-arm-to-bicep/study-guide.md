# Export a deployment or convert ARM to Bicep

## What
Exporting produces an ARM-template representation of selected resources or deployment history. Decompilation converts an existing ARM JSON template into editable Bicep; it is a starting point, not a guaranteed faithful source reconstruction.

## Why
Export can bootstrap IaC for legacy resources and reveal their configured properties. Conversion can make an ARM template easier to maintain. Architecturally, generated templates often contain environment-specific values, defaults, unsupported properties, or secrets and may omit dependencies or lifecycle intent.

## How
Use portal **Export template** on a supported resource/resource group or CLI export commands, then inspect the result. For JSON-to-Bicep, run `az bicep decompile --file <path-to-template.json>`. Compile the Bicep, lint it, and compare generated output and what-if against the live environment in a non-production scope. Refactor into parameters/modules, remove unsafe values, and capture dependencies and identity deliberately before treating it as authoritative.

## Features
Exported templates reflect a point-in-time configuration; they do not automatically become a continuous management source. Not every resource type/property is exportable, and generated output may use hard-coded values. Decompilation cannot recover original names, comments, abstractions, or deployment intent. What-if and deployment history help validate, but do not eliminate drift or runtime risk.

## Code snippets (if any)
```bash
az bicep decompile --file <path-to-template.json>
az bicep build --file <path-to-template.bicep>
```
Review and sanitize generated source before committing or deploying.

## Do's and Don'ts
**Do** treat export/decompile as discovery, then parameterize, lint, and validate. **Don't** immediately redeploy exported JSON; inspect credentials, resource dependencies, immutable fields, and destructive changes.

## Real-life implementation
A team adopts a manually created VM environment: export a representative resource group, remove incidental resources and personal data, replace environment values with parameters, and build a clean Bicep module. Test what-if and deployment behavior against a disposable environment before production adoption.

## Q&A
1. **Does export guarantee a complete template?** No. Unsupported properties/resources and external dependencies may be absent.
2. **Does decompile reproduce original Bicep?** No. It translates JSON into approximate Bicep, without recovering original abstractions or intent.
3. **Can I safely check exported files into source control?** Only after reviewing for secrets, tenant-specific data, and sensitive configuration.

**References:** [Export template in Azure portal](https://learn.microsoft.com/azure/azure-resource-manager/templates/export-template-portal) · [Decompile ARM JSON to Bicep](https://learn.microsoft.com/azure/azure-resource-manager/bicep/decompile)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#automate-deployment-by-using-arm-templates-or-bicep)
