# 7b. Use the CLI to inspect state

## What

Terraform state maps configuration addresses to remote objects and records attributes used to plan changes. CLI state commands let operators inspect those bindings and, with greater care, change them. State is operationally critical and may contain secrets even when values are marked sensitive.

## Why

Accurate state is necessary for safe plans and applies. State inspection helps establish what Terraform currently manages, diagnose address mismatches, and verify a refactor or recovery. State is not a hand-edited inventory: direct edits and uncoordinated writes risk losing bindings, overwriting newer state, or causing destructive plans.

## How

Begin with read-oriented commands in the initialized working directory and confirm its backend, selected workspace, account, and address:

```shell
terraform state list
terraform state list 'module.app'
terraform state show 'module.app.aws_instance.web[0]'
terraform state pull
```

`state list` prints addresses and can filter by address; `state show` displays stored attributes for one address. `state pull` retrieves the state representation and should be treated as secret-bearing data. Quote complex module paths and indexed addresses as required by the shell.

Mutation commands require explicit intent:

* `terraform state mv OLD NEW` changes the state address association, not the remote object's identity. Align it with the configuration refactor and review a plan afterward. For collaborative refactors, a version-controlled `moved` block is often easier to apply consistently.
* `terraform state rm ADDRESS` removes the binding but leaves the real object running; Terraform stops managing it at that address unless it is imported again. It is not a destroy command.
* `terraform state replace-provider` updates provider source references recorded in state. Review provider configuration and plans afterward.
* `terraform state push` is an exceptional recovery tool, not routine editing. It can overwrite newer state; lineage/serial checks do not replace secure backups and coordination.

Commands that alter state may lock it when the backend supports locking; guarantees vary by backend and command. Avoid concurrent writes, preserve a secure backup before high-risk repair, and do not disable locking just to bypass contention. A failed lock is safer than a racing write. After changes, run `terraform plan` to verify the intended mapping before applying infrastructure changes.

## Features

* `terraform state list` enumerates addresses; `terraform state show` inspects one binding's attributes.
* `terraform state pull` retrieves state for inspection or recovery and exposes sensitive data.
* `state mv`, `state rm`, `state replace-provider`, and `state push` have distinct, potentially consequential effects.
* `moved` blocks encode address refactors in configuration for consistent collaboration.

## Do's and Don'ts

**Do**
* Verify backend, workspace, account, and full address before interpreting or changing state.
* Use read commands first, protect pulled state and backups, and plan after a mutation.
* Coordinate state writes and honor backend locking.

**Don't**
* Hand-edit state JSON or treat state output as safe to share.
* Confuse `state rm` (forget binding) with destroying the remote object.
* Confuse `state mv` (change address) with changing the cloud object's identity.
* Push recovery state or disable locking without a reviewed recovery plan.

## Real-life implementation

A team renames `module.app.aws_instance.web[0]` during a code refactor. Before changing production, the operator confirms the target workspace and backend, lists and shows the current address, and updates configuration with a reviewed `moved` block. They plan against the existing state, confirm Terraform recognizes the move without replacement, and apply through the team's normal approval path. State access and any recovery snapshot remain restricted.

## Q&A

1. **Which command lists managed addresses?** `terraform state list`.
2. **Which command shows one object's stored attributes?** `terraform state show ADDRESS`.
3. **What happens after `terraform state rm ADDRESS`?** The binding is removed; the real object remains and is no longer tracked at that address.
4. **What is usually preferable for a collaborative address refactor?** A reviewed `moved` block where applicable.

Sources: [Terraform state](https://developer.hashicorp.com/terraform/language/state), [State command reference](https://developer.hashicorp.com/terraform/cli/commands/state), [Resource addressing](https://developer.hashicorp.com/terraform/cli/state/resource-addressing), [Moved block](https://developer.hashicorp.com/terraform/language/moved).

[Back to the Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md)
