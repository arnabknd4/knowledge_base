# 7a. Import existing infrastructure

## What

Import associates an existing remote object with a Terraform resource address in state so Terraform can manage it. It does not create the object, and import alone does **not** generate complete Terraform configuration.

## Why

Import enables a controlled transition from manually managed infrastructure to configuration-driven operations without recreating the object. The configuration and state must ultimately describe the same object; otherwise subsequent plans can propose unexpected updates, replacement, or deletion. Each remote object should have one Terraform owner/address to avoid competing management.

## How

First inventory the object and dependencies, confirm the provider/account/workspace and state boundary, and choose a stable address with appropriate module/count/for_each placement. Usually write the matching resource block yourself. For import blocks, Terraform can optionally generate an initial configuration candidate with `terraform plan -generate-config-out=PATH` when the target resource configuration is not yet present. Generated configuration may be incomplete or need correction; inspect and maintain it as normal configuration. The import ID is provider-specific; consult the provider's documentation.

Two workflows are supported:

* **CLI import:** `terraform import ADDRESS ID` imperatively adds the binding to state. The destination resource configuration must already exist. Inspect it with `terraform state show ADDRESS`, then reconcile configuration and review a plan.
* **Import block:** Declare an `import` block in configuration. Review its import action in `terraform plan` and apply it through the normal plan/apply workflow. The block records the intended adoption; it does not by itself synthesize a complete `.tf` resource block. The optional `-generate-config-out` plan flag can write a starting resource configuration, which still requires review.

```hcl
import {
  to = aws_instance.web
  id = "i-0123456789abcdef0"
}
```

Assuming the provider and matching `aws_instance.web` configuration exist, plan and inspect **all** proposed changes before applying. Provider defaults, omitted arguments, computed values, and immutable attributes can make a successful import differ from a no-op plan. Investigate mismatches; use lifecycle settings such as `ignore_changes` only for an intentional policy, not to hide unexplained drift.

For estate-scale adoption, divide work into small reviewable batches. Secure a state backup, ensure locking is functioning, prevent concurrent applies, and coordinate a rollback path before state writes. Verify each address and run a fresh plan before considering the handoff complete.

## Features

* Both imperative CLI import and declarative import blocks bind existing objects into state.
* Import IDs and accepted arguments are provider-specific. `terraform plan -generate-config-out=PATH` can optionally generate a starting configuration for import blocks, not a guaranteed complete or production-ready configuration.
* State inspection and planning validate the binding and reveal configuration mismatches; neither import method guarantees a no-change plan.
* Import is a state operation and must be coordinated like other state changes.

## Do's and Don'ts

**Do**
* Confirm the correct provider, account, workspace, state and exact resource address before import.
* Write configuration that reflects the real object; inspect state and review a plan.
* Back up and protect state, use locking, and import in small batches.

**Don't**
* Expect either workflow to generate complete resource configuration.
* Assign the same remote object to multiple Terraform addresses or states.
* Apply a plan containing unexplained changes, or suppress them with `ignore_changes` without a deliberate policy.
* Run imports concurrently with another apply against the same state.

## Real-life implementation

A platform team adopts an existing production AWS instance into a new Terraform module. The owner confirms the account and workspace, records the instance ID and dependencies, writes the matching resource block, and adds an import block to a reviewed branch. A teammate checks the planned import and any proposed updates; the team applies only after confirming there is no replacement or unrelated change. They inspect the resulting state, remove the temporary import declaration if it is no longer needed, and run a fresh plan. The state snapshot remains access-controlled, and the production apply pipeline is paused during adoption.

## Q&A

1. **Does `terraform import ADDRESS ID` generate HCL?** No. The resource configuration must be written and reconciled separately.
2. **How is an import block executed?** Through the normal plan/apply workflow after reviewing the import action.
3. **What does an import ID identify?** An existing provider object; its format is defined by that provider.
4. **What must be checked after import?** The state binding and a plan for unintended updates, replacements, or deletions.
5. **Does import automatically produce complete configuration?** No. The optional `-generate-config-out` flag can produce a starting point for an import block, but it must be reviewed and completed.

Sources: [Import resources](https://developer.hashicorp.com/terraform/language/import), [`terraform import` command](https://developer.hashicorp.com/terraform/cli/commands/import), [Resource addressing](https://developer.hashicorp.com/terraform/cli/state/resource-addressing).

[Back to the Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md)
