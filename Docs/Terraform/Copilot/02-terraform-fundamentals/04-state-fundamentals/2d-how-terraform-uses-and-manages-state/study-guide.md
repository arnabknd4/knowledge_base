# 2d — Explain how Terraform uses and manages state

## What

Terraform state associates resource instances in configuration with real remote objects and stores values Terraform needs to plan and manage them. A configuration address such as `example_network.app` is not necessarily the remote API identity; state records the relationship, including provider-specific identifiers and attributes.

## Why

The mapping lets Terraform identify which object a declaration manages, detect changes, and determine possible operations. During planning, Terraform considers configuration, prior state, and refreshed provider information. State is not a disposable cache: without mappings, Terraform may not know an existing object belongs to a configured address and may propose a duplicate or lack context for safe management. Nor is it a complete live inventory; it tracks objects managed by Terraform.

## How

```hcl
resource "example_network" "app" {
  name = "application"
}
```

Terraform tracks the instance at `example_network.app` and associates it with the provider's remote identifier. Renaming the block to `example_network.application` changes its configuration address. Without a refactor treatment such as a `moved` block or carefully planned state move, Terraform may interpret the old address as removal and the new one as creation. This resource is schematic and requires an actual provider.

## Features

- State maps Terraform resource addresses to remote object identities.
- Planning uses configuration, prior state, and refreshed provider information to propose actions.
- State can contain sensitive values, including values marked sensitive in configuration; sensitivity primarily limits display and does not encrypt, omit, or remove values from state.
- Remote backends can support collaboration and locking, but must be configured and secured appropriately.
- Saved plan files can also contain sensitive information.

## Do's and Don'ts

### Do

- Protect state and saved plans using access controls, encrypted and durable storage, backups, and locking where supported.
- Use supported Terraform commands or declarative move/removal mechanisms for state/address refactors, then inspect the resulting plan.
- Back up state before high-impact state operations and keep state out of logs, source control, and shared artifacts.
- Securely configure remote backends; remote storage is not automatically safe.

### Don't

- Treat state as the configuration itself, a complete account inventory, or an optional cache that can be deleted safely.
- Assume `sensitive = true` removes or encrypts values in state.
- Edit state JSON casually or run concurrent operations against unlocked state.
- Rename resource addresses without considering a move; Terraform may plan destruction and creation.

## Real-life implementation

For a production network, store state in an appropriately secured, durable backend with access controls, backups, and locking where supported. Limit who can read state and saved plans because either may expose sensitive values. When refactoring a resource address, use a `moved` block or a carefully planned supported state move, back up first when intervening in state, and review the plan to confirm Terraform retains the remote object rather than replacing it. Exact backend and locking features depend on the selected backend.

## Q&A

1. **Why does Terraform need state?** To map configuration instances to remote object identities and support planning.
2. **Does state describe all live infrastructure?** No, it primarily tracks objects under Terraform management.
3. **Does `sensitive = true` remove a value from state?** No; it primarily limits display.
4. **What can an unmanaged address rename cause?** Terraform may plan destruction and creation rather than an in-place address move.
5. **Is a remote backend automatically safe?** No; it must be configured and secured appropriately.

## Official references

- [Purpose of Terraform state](https://developer.hashicorp.com/terraform/language/state/purpose)
- [Sensitive data in state](https://developer.hashicorp.com/terraform/language/state/sensitive-data)
- [State documentation](https://developer.hashicorp.com/terraform/language/state)

[Back to the Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md)
