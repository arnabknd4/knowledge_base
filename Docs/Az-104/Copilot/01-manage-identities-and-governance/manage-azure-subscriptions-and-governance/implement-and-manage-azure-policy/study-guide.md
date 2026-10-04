# Implement and manage Azure Policy

Syllabus: [Domain 1 — Manage Azure identities and governance](../../../copilot-az104-syllabus.md#1-manage-azure-identities-and-governance-20-25)

## What

Azure Policy evaluates and governs resource state against definitions. A policy definition expresses a rule; an assignment applies it at a scope with parameters and optional exclusions. Initiatives group policies for a common objective. Effects include audit, deny, append/modify, deployIfNotExists, and disabled; the applicable effect depends on the definition and scenario.

## Why

Policy provides consistent guardrails and compliance visibility across subscriptions without relying on each operator to remember every requirement. Choose an effect based on the needed behavior: report existing noncompliance, prevent new violations, modify supported properties, or deploy a related configuration. Remediation effects can require a managed identity and appropriate permissions.

## How

In the portal, use **Policy > Definitions/Assignments/Compliance** to select or create a definition, assign it at the smallest appropriate scope, set parameters/exclusions, and review compliance. Azure CLI supports `az policy definition`, `az policy assignment`, and `az policy state`; PowerShell provides `New-AzPolicyAssignment` and related cmdlets. Test at a nonproduction scope first and inspect evaluation/remediation results. Use exemptions with documented justification and expiry where appropriate.

## Features

- Policy assignment inheritance follows scope hierarchy; evaluate applicable assignments and exemptions.
- **Audit** reports without blocking; **Deny** blocks a noncompliant create/update; **DeployIfNotExists** evaluates related configuration and can trigger remediation.
- Policy compliance evaluation is not necessarily instantaneous.
- **Exam trap:** Policy is not an RBAC permission grant/deny mechanism. RBAC controls who may act; Policy controls resource configuration requirements.

**Microsoft Learn:** [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview); [Policy effects](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects); [Assign a policy definition](https://learn.microsoft.com/en-us/azure/governance/policy/assign-policy-portal)

## Code snippets (if any)

Check assignment and compliance-related commands:

```bash
az policy assignment list --scope "/subscriptions/<subscription-id>" --output table
```

This inspects assignments; it does not itself create a policy or remediation task.

## Do's and Don'ts

- Do pilot Deny effects and review existing resources before enforcing.
- Do grant remediation identities only the permissions needed by the policy.
- Don't assume a new assignment instantly evaluates every resource.
- Don't use a broad exclusion as a substitute for tuning parameters or correcting the definition.

## Real-life implementation

A platform team requires storage accounts to use approved configurations. It first assigns an Audit policy to a development management group and reviews compliance results, then resolves exceptions and rolls out Deny at production scope. A separate remediation assignment with a managed identity handles supported existing-resource corrections, and exemptions are time-bound and owned.

## Q&A

**Q: Which effect reports violations without blocking creation?**
A: Audit.

**Q: Which effect blocks a noncompliant create or update?**
A: Deny.

**Q: What can an initiative do?**
A: Group related policy definitions into one governance assignment.

**Q: Does Policy decide whether a principal is authorized to call an operation?**
A: No; that is primarily Azure RBAC and other authorization controls.
