# Apply and manage tags on resources

Syllabus: [Domain 1 — Manage Azure identities and governance](../../../copilot-az104-syllabus.md#1-manage-azure-identities-and-governance-20-25)

## What

Use Azure tags—name/value metadata attached to supported resources and resource groups—to organize assets, support cost allocation, automate operations, and identify ownership or environment. Tags are metadata, not authorization policies or an automatically inherited hierarchy.

## Why

Consistent tags make inventory, cost analysis, and operational filtering more useful. Their value depends on a governed taxonomy and reliable coverage. A tag such as `Environment=Prod` only helps if spelling, allowed values, scope, and lifecycle are standardized; it does not itself enforce that a resource is production-ready.

## How

Use **Tags** in the portal on a resource/group, or Azure CLI `az tag` commands and PowerShell `Update-AzTag`. For bulk governance, use Azure Policy to require tags on creation, inherit or modify selected tags where supported, and remediate existing resources when appropriate. Validate tag keys/values against the organization's convention, and use Cost Management analysis to check whether tags are actually used for allocation.

## Features

- Tag inheritance from resource group to child resources is not automatic; use policy or another automation process where required.
- Resource groups and resources can have tags, but resource support and limits should be checked for the service.
- Resource Manager tags are metadata and do not propagate as a security boundary into the service's data.
- **Exam trap:** applying a tag to a resource group does not automatically tag every resource inside it.

**Microsoft Learn:** [Use tags to organize Azure resources and management hierarchy](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources); [Azure Policy samples for tags](https://learn.microsoft.com/en-us/azure/governance/policy/samples/built-in-policies#tags)

## Code snippets (if any)

Set or merge a tag on a resource group with Azure CLI:

```bash
az tag update --resource-id "/subscriptions/<subscription-id>/resourceGroups/<resource-group>" --operation Merge --tags CostCenter=CC42 Environment=Production
```

Use `Merge` to preserve existing tags; validate the resource ID and organizational tag values.

## Do's and Don'ts

- Do define canonical keys, allowed values, ownership, and exception handling.
- Do automate required/inherited tags and check noncompliance.
- Don't store secrets, personal data, or sensitive operational details in tags.
- Don't use tags as a substitute for RBAC, policy, or resource organization.

## Real-life implementation

A finance team wants project-level cost reporting. It establishes approved `CostCenter` and `Service` values, applies them through deployment templates and policy, and reviews uncovered resources monthly. Resource-group tags are propagated by policy where supported; cost reports are checked to confirm the tag is available for the expected charge data.

## Q&A

**Q: Do tags inherit automatically from resource groups?**
A: No. Use policy or automation to propagate them where supported.

**Q: What is a tag useful for?**
A: Classification, filtering, operations, and cost allocation.

**Q: Does a tag prevent unauthorized changes?**
A: No. Tags are metadata and do not grant or deny access.

**Q: How can required tags be governed?**
A: Azure Policy can audit or enforce tag requirements and support supported remediation.
