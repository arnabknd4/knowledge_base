# 3d — Generate and review an execution plan

## What

`terraform plan` previews the actions Terraform proposes to reconcile configuration with tracked state and observed remote infrastructure. Planning normally refreshes information about managed objects, evaluates expressions and data sources, and builds the dependency graph. Its result can include creates, in-place updates, replacements (destroy then create or create then destroy), and destroys. A plan is a proposal, not a guarantee of successful execution.

Read the action symbol for each address and the details beneath it. `+` indicates creation, `~` an in-place update, `-` destruction, and `-/+` or `+/-` replacement order. Attribute-level differences explain what led to the action. Unknown values are computed during apply, often because provider-generated values or dependencies are not yet known.

## Why

Planning is the key control point between desired state and execution. A saved plan improves consistency between review and execution because Terraform applies the calculated action set rather than recalculating it. However, plan files are bound to context and can become stale; Terraform rejects some stale plans, and organizations should regenerate/review after meaningful changes instead of treating plans as long-lived deployment artifacts.

Use plans to reason about blast radius and lifecycle implications. A small HCL edit can force replacement if an attribute is immutable. A plan showing broad recreation can reveal an address/refactor issue, wrong workspace, missing state, or unexpected input. Changes to existing real infrastructure should never be approved just because the command succeeded.

## How

```shell
terraform plan
terraform plan -out=tfplan
terraform show tfplan
```

A normal plan is interactive and does not execute managed-resource actions, but it may perform remote reads and update state metadata depending on backend and options. Planning is therefore not the same as applying, but it is not necessarily a zero-side-effect API operation. Saving with `-out` creates a plan file that can be reviewed or passed to apply. Treat that file as sensitive: it can include sensitive values, and it represents a specific proposed change. `terraform show` renders a saved plan; JSON output can support automation but may expose values too.

Review addresses, action types, replacement reasons, unknowns, output changes, and any unexpected destructive scope. Confirm expected variables, workspace/backend, provider identities, and state context before approval.

## Features

- Plan is a preview based on configuration, state, and refreshed information; it is not itself the apply.
- Replace is not the same as an in-place update and may involve downtime or temporary duplication.
- `terraform plan -out` creates a sensitive artifact; `terraform apply tfplan` consumes it.
- A no-op plan means no changes are currently proposed, not that the configuration is universally correct.

## Do's and Don'ts

### Do

- Verify workspace/backend, variables, identities, and target addresses before interpreting actions.
- Review create/update/replace/destroy actions, replacement triggers, unknown values, and output changes.
- Secure saved plan files and regenerate them when their context becomes stale.

### Don't

- Do not treat a plan as an apply or as proof that apply will succeed.
- Do not approve unexpected replacement or deletion just because the command exited successfully.
- Do not expose saved plans or rendered JSON; they may contain sensitive values.

## Real-life implementation

For a disposable non-production environment, generate `terraform plan -out=tfplan`, inspect it with `terraform show tfplan`, and have a second reviewer verify the expected addresses and action types before the deployment stage consumes it. Store the artifact in restricted CI storage with short retention. If code, state, variables, or remote context changes, discard it and create a newly reviewed plan.

## Q&A

**Q:** What do `+`, `~`, and `-` represent?  
**A:** Create, in-place update, destroy; replacement combines destroy/create indicators.

**Q:** Why are values sometimes “known after apply”?  
**A:** They depend on provider-computed values or actions that have not run yet.

**Q:** What should be reviewed before approval?  
**A:** Scope, addresses, action types, replacement reasons, variables/context, and sensitive output.

**Q:** Why protect a saved plan?  
**A:** It can contain sensitive data and embodies an executable change proposal.

Further reading: [terraform plan](https://developer.hashicorp.com/terraform/cli/commands/plan), [terraform show](https://developer.hashicorp.com/terraform/cli/commands/show).

---

Back to the [Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md).
