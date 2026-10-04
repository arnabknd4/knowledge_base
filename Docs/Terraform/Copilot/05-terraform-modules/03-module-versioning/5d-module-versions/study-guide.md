# 5d — Manage module versions

## What

Version selection is source-specific. A registry module uses the `version` constraint in its `module` block. A Git module uses a VCS ref such as `?ref=<tag-or-commit>`; a local module follows the checked-out filesystem. Provider plugins are selected separately through `required_providers` constraints and the provider dependency lock file, `.terraform.lock.hcl`. Terraform CLI compatibility is separately constrained with `required_version`.

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0" # compatible 5.x, but not 6.0
}
```

## Why

Module releases are configuration API releases: an update can change resource arguments, behavior, or addresses and may propose replacement or deletion. Constraints communicate which releases a caller accepts; reviewed initialization and plan workflows control when upgrades are adopted. A provider lock file does not pin module versions.

## How

Use an intentional registry constraint: broad ranges can select unreviewed behavior changes, while overly narrow pins may delay fixes. `terraform init` generally reuses installed selections where possible; `terraform init -upgrade` asks Terraform to reconsider eligible registry module and provider selections. Review changes and plans before applying. A VCS tag is a ref, not a registry version constraint; prefer an immutable commit or governed, immutable tag over mutable branches. Module source metadata in `.terraform` is useful for inspecting an installation, not a replacement for reviewed source constraints.

Modules may declare provider requirements. The root's provider constraints and `.terraform.lock.hcl` govern selected provider plugins, not module configuration releases. `required_version` constrains the Terraform CLI executable, not a module or provider.

## Features

- Registry module constraints are specified with `version` in the module call.
- Git/VCS revision selection uses `ref` in the source string.
- `.terraform.lock.hcl` records provider selections/checksums; it does not lock registry modules.
- `terraform init -upgrade` reconsiders eligible module and provider selections.
- A module-version update can change resource plans and state addresses.

## Do's and Don'ts

**Do**
- Define a version strategy per environment and criticality, and stage production upgrades.
- Treat module interface changes as API changes; test representative callers.
- Pin VCS sources to reviewed immutable revisions where reproducibility matters.
- Review initialization changes and the complete plan before applying an upgrade.

**Don't**
- Confuse module `version`, provider constraints, `.terraform.lock.hcl`, and Terraform `required_version`.
- Assume `.terraform.lock.hcl` pins registry module code.
- Rely on mutable VCS branches for repeatable production deployments.
- Treat a successful `init -upgrade` as approval to apply its resulting plan.

## Real-life implementation

A platform team can publish versioned modules with documented compatibility and test them against representative root configurations. Application teams declare approved registry constraints in their roots; CI runs initialization and planning, records the provider lock file, and routes module changes through review. Promote a candidate module update through nonproduction states first, compare address and replacement changes, and schedule production applies under the team's change controls. For VCS-only dependencies, record an immutable revision so a fresh runner installs the same code. Keep module release cadence independent of provider-plugin upgrades unless both are intentionally part of the same reviewed change.

## Q&A

1. **Where is a registry module constraint written?** In the module call's `version` argument.
2. **What selects the provider plugin version?** Provider constraints and `.terraform.lock.hcl`, not the module version.
3. **How should a Git module be pinned?** Through `ref`, preferably to a reviewed immutable commit.
4. **What does `terraform init -upgrade` reconsider?** Eligible module and provider selections; inspect the updates and plan.

**Official references:**

- [Module block syntax and version argument](https://developer.hashicorp.com/terraform/language/modules/syntax)
- [Provider requirements and version constraints](https://developer.hashicorp.com/terraform/language/providers/requirements)
- [Dependency lock file](https://developer.hashicorp.com/terraform/language/files/dependency-lock)

[Back to the Terraform Associate syllabus](../../../copilot-terraform-syllabus.md)
