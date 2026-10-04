# 2a — Install and version Terraform providers

## What

A provider requirement tells Terraform which plugin a configuration depends on. In the root module's `terraform.required_providers` block, declare a local name, **source address**, and **version constraint**. The source identifies the provider in a registry namespace; the local name is how configuration refers to it.

## Why

Version constraints define acceptable releases, while `.terraform.lock.hcl` records selected versions and checksums. Committing this generated lock file lets teams and automation reuse provider selections and verify downloaded packages. Constraints and lock selections together balance predictable behavior with the ability to take reviewed security and compatibility updates.

## How

```hcl
terraform {
  required_providers {
    example = {
      source  = "example.org/acme/example"
      version = "~> 1.4"
    }
  }
}
```

The address is illustrative; use a real source address operationally. `~> 1.4` permits compatible releases from 1.4 up to, but not including, 2.0. `terraform init` discovers and installs compatible provider packages, respecting locked selections when they satisfy constraints. Use `terraform init -upgrade` to deliberately reconsider eligible selections; review the lock-file diff and resulting plans/tests.

## Features

- `required_providers` declares plugin identity and acceptable version range.
- `.terraform.lock.hcl` records selected provider versions and package checksums for platforms in use.
- Checksums allow Terraform to verify that downloaded packages match recorded packages.
- Installed provider packages reside in the working directory's `.terraform` data directory, which is generally regenerated.
- The lock file does not store constraints, provider configuration values, credentials, or remote infrastructure state.

## Do's and Don'ts

### Do

- Commit `.terraform.lock.hcl` and review its changes.
- Use `terraform init -upgrade` intentionally, then inspect updates, release notes, compatibility, and plans.
- Coordinate lock-file updates across operating systems where relevant.
- Select bounds that allow reviewed fixes while limiting unreviewed behavioral changes.

### Don't

- Confuse `terraform init` with `terraform apply`; init installs providers and apply executes infrastructure operations.
- Put credentials or provider settings in `required_providers`; configure provider instances separately and handle credentials securely.
- Treat the lock file as a replacement for version constraints, configuration, or state.
- Let every environment independently make unreviewed provider upgrades.

## Real-life implementation

In a team repository, declare the provider source and a deliberate constraint, run `terraform init`, and commit the generated lock file. In CI and developer workflows, use ordinary init for consistent selections. For an upgrade, change constraints if required, run init with `-upgrade`, review the lock-file diff and provider release notes, then validate and plan across relevant environments before merge. The sample provider address is illustrative.

## Q&A

1. **Where declare source and version?** `terraform.required_providers`.
2. **What does init do with requirements?** Selects and installs compatible provider plugins.
3. **Why commit the lock file?** Teams reuse consistent selections and verify package checksums.
4. **How request an intentional upgrade?** Run `terraform init -upgrade`, then review changes and plans.
5. **Does the lock file contain version constraints or state?** No; it records provider selections and checksums.

## Official references

- [Provider requirements](https://developer.hashicorp.com/terraform/language/providers/requirements)
- [Dependency lock file](https://developer.hashicorp.com/terraform/language/files/dependency-lock)
- [terraform init command](https://developer.hashicorp.com/terraform/cli/commands/init)

[Back to the Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md)
