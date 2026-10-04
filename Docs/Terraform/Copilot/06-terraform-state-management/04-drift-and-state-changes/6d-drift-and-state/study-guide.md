# 6d — Manage resource drift and Terraform state

## What

Drift is a difference between the infrastructure Terraform observes and the configuration's desired values. Changes may be made outside Terraform or by other automation. State records Terraform's latest known mapping and attributes; it is not a complete inventory of every object in an account.

A normal plan refreshes managed objects through providers, compares the observed state with configuration, and proposes actions to converge infrastructure. A refresh-only plan instead proposes updating state and outputs to reflect observed values without changing remote infrastructure when applied:

```shell
terraform plan -refresh-only
terraform apply -refresh-only
```

Terraform resource addresses identify managed objects by module path, resource type/name, and instance key. Refactoring a configuration may change an address even when the real object is unchanged.

## Why

External changes can require intentional reconciliation or acceptance into state. Address changes from refactoring can otherwise look like a destroy-and-create replacement. Explicit state migration preserves the relationship to existing objects. Removing an object from Terraform management is a separate, deliberate operation from destroying it.

## How

Inspect plans to determine whether a drifted value should be corrected in configuration, reverted by applying a normal plan, or accepted into state with reviewed refresh-only apply. Refresh-only does not change infrastructure, but can accept unexpected changes or deletions into state. `-refresh=false` skips observations and may produce a stale, misleading plan; it is not a drift-remediation method.

Use a `moved` block to map an old address to a new address when refactoring the same managed object:

```hcl
moved {
  from = aws_instance.web
  to   = module.app.aws_instance.web
}
```

Keep the mapping available until all relevant workspaces/operators have applied the refactor. For a deliberate removal from management, Terraform 1.12 supports a `removed` block. Be explicit when the real object should remain:

```hcl
removed {
  from = aws_instance.legacy

  lifecycle {
    destroy = false
  }
}
```

Without `destroy = false`, a removed block defaults to destroying the object. `terraform state mv` and `terraform state rm` are imperative alternatives for controlled state surgery. Back up and coordinate state operations; `state rm` forgets the mapping and leaves the real object unmanaged.

## Features

- Normal planning refreshes provider observations before calculating actions.
- Refresh-only plan/apply records observed values in state without changing infrastructure.
- `moved` blocks associate old and new Terraform addresses to preserve object identity.
- `removed` blocks declare intentional removal from configuration; `lifecycle { destroy = false }` forgets the object without destroying it.
- `terraform state mv` and `terraform state rm` provide imperative state-manipulation alternatives.

## Do's and Don'ts

**Do**
- Review drift and refresh-only plans before accepting changes into state.
- Update configuration if external changes are intended to become the desired configuration.
- Add `moved` mappings for address refactors that should retain the same real objects.
- Use `removed` with an explicit `destroy = false` lifecycle when intentionally ceasing management without destruction.
- Back up state, coordinate operators, and verify with a fresh plan after imperative state changes.

**Don't**
- Assume refresh alone reconciles infrastructure or that state is an inventory of all cloud objects.
- Use `-refresh=false` to resolve drift.
- Rename addresses and assume Terraform will infer that the object identity is unchanged.
- Assume refresh-only apply makes remote infrastructure match configuration.
- Remove an address from state without understanding that Terraform will no longer manage that real object.

## Real-life implementation

In production, treat out-of-band changes as incidents or reviewed change requests: identify the actor and intent, inspect a normal plan, then either update configuration and reconcile or accept actual values with refresh-only apply. For a module/resource refactor, stage configuration and `moved` blocks together, inspect the plan for address moves rather than replacement, and retain the blocks while rolling the change through every relevant workspace. When decommissioning Terraform ownership but retaining a resource, use a reviewed `removed` block with `destroy = false`, confirm the plan no longer destroys the object, and transfer operational ownership and monitoring. For direct `state mv`/`state rm`, pause concurrent applies, back up state, use the correct workspace, and run a follow-up plan before reopening deployment.

## Q&A

1. **What does a normal plan do before calculating changes?** It refreshes managed-object observations through providers and compares them with configuration.
2. **How can observed values be accepted without changing infrastructure?** Review a `-refresh-only` plan and apply it.
3. **How does a refactor preserve the identity of a managed object?** Use a `moved` block from the old address to the new address.
4. **How does `removed` with `lifecycle { destroy = false }` behave?** It removes the address from Terraform management without deleting the real object.

**Official references:**

- [Terraform state and refresh](https://developer.hashicorp.com/terraform/language/state)
- [Refresh-only mode](https://developer.hashicorp.com/terraform/cli/commands/plan#refresh-only-mode)
- [Refactoring with moved blocks](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring)
- [Removed block](https://developer.hashicorp.com/terraform/language/block/removed)

[Back to the Terraform Associate syllabus](../../../copilot-terraform-syllabus.md)
