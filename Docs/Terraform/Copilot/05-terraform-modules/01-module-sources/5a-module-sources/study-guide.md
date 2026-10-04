# 5a — Explain how Terraform sources modules

## What

A module is a directory of Terraform configuration. The root module is the working directory where Terraform runs; each `module` block instantiates a child module. Its `source` identifies the module's code location/package—not a provider, backend, or remote-state location.

Common sources include local paths, public or private registry addresses, Git/Mercurial repositories, HTTP URLs, and object-storage/archive URLs. VCS and archive sources can select a subdirectory with `//path`.

```hcl
module "network" {
  source = "./modules/network" # relative to the calling module
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0" # registry module constraint
}

module "shared" {
  source = "git::https://example.com/platform/iac.git//modules/shared?ref=v2.1.0"
}
```

## Why

The source determines how module code is distributed, reviewed, reproduced, and upgraded. Local modules are convenient when code is co-located and released with its caller. A registry offers a discoverable, versioned contract for shared modules. VCS/archive sources fit workflows that need a repository or artifact as the delivery unit, but require deliberate pinning and review.

Treat source selection as a supply-chain and lifecycle decision. Prefer portable relative paths, trusted origins, stable interfaces, and immutable references for production. A moving local directory or mutable branch can change behavior without a deliberate release.

## How

`terraform init` discovers modules and installs remote module code into Terraform's working data directory, normally `.terraform/modules`; it does not copy that code into configuration. Initialize after adding a module or changing its source. `terraform init -upgrade` deliberately reconsiders eligible registry module and provider selections; review the resulting changes and plan.

Registry module versions use the `version` argument. Git/VCS sources use a ref such as `?ref=<tag-or-commit>`; local sources use the current filesystem. The `version` argument is not a universal version selector. Provider addresses such as `hashicorp/aws` belong in `required_providers`; they are not module sources. Provider versions are governed separately by provider constraints and `.terraform.lock.hcl`.

## Features

- Local paths can be relative or absolute; relative paths make repositories portable and resolve relative to the calling module.
- Registry module addresses can be constrained using `version`.
- VCS and archive sources may select a subdirectory with `//path`; use `?ref=` to select a VCS revision.
- Source strings are static configuration, not Terraform expressions.
- `terraform init` installs modules; planning does not replace initialization after a source change.

## Do's and Don'ts

**Do**
- Pin VCS sources to a reviewed tag or immutable commit for repeatable production installs.
- Use registry constraints that match your upgrade and compatibility policy.
- Supply private-source credentials through supported secure mechanisms, not embedded URLs or committed configuration.
- Review source changes, run init/validation, and inspect the plan before applying.

**Don't**
- Confuse a module source with a provider address, backend, or state location.
- Use `version` as a substitute for a Git `ref`.
- Treat a mutable branch, moving local directory, or broad constraint as an immutable release.
- Assume `terraform init -upgrade` upgrades Terraform CLI itself.

## Real-life implementation

For a platform team publishing network and identity modules, release tested versions to a private registry, document each module's supported inputs and provider requirements, and have application roots select an approved version range. CI runs `terraform init`, validation, and plan review using least-privilege credentials. A root using an in-repository module can instead use a relative path when caller and module intentionally share a release cadence. For an exceptional VCS dependency, pin a reviewed commit and make the upgrade an explicit dependency change. Keep module distribution credentials separate from provider credentials: module installation happens during initialization, while providers authenticate to infrastructure APIs during operations.

## Q&A

1. **Does `source = "hashicorp/aws"` select the AWS provider?** No. Provider addresses belong in `required_providers`; a module source locates Terraform configuration.
2. **How does Terraform resolve `source = "./modules/network"`?** Relative to the module containing that call.
3. **How should a Git module be pinned?** Put a reviewed tag or immutable commit in its `?ref=` query parameter.
4. **What should follow a module-source change?** Run `terraform init`, then validate and inspect a plan.

**Official references:**

- [Module sources](https://developer.hashicorp.com/terraform/language/modules/sources)
- [Module block syntax](https://developer.hashicorp.com/terraform/language/modules/syntax)

[Back to the Terraform Associate syllabus](../../../copilot-terraform-syllabus.md)
