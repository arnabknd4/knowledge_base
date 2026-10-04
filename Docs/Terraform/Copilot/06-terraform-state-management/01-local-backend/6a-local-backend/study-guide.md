# 6a — Describe the local backend

## What

Terraform state maps configuration addresses (for example, `aws_instance.web`) to real infrastructure objects and records attributes needed for planning. A backend defines how and where state is stored and state operations are performed. With no backend configured, Terraform uses the built-in `local` backend.

```hcl
terraform {
  backend "local" {
    path = "terraform.tfstate"
  }
}
```

The default local backend needs no explicit block. State is normally stored in `terraform.tfstate` in the working directory, with a backup such as `terraform.tfstate.backup` created after updates; local workspace states use backend-specific paths. These files are not caches and should not be hand-edited.

## Why

Local state is convenient for experiments, isolated personal configurations, and some controlled automation. A state file on one machine does not provide reliable shared coordination, centralized access control, or dependable collaboration across machines. Losing the only copy can sever Terraform's mapping to existing objects; infrastructure may remain running, but safe recovery or import is needed before future management.

State can contain sensitive values even when outputs or variables are marked sensitive. Protect local files and backups and keep them out of source control.

## How

Backend configuration belongs in the top-level `terraform` block, not a provider block. `terraform init` initializes backend settings. Terraform commands manage state; preserve recoverable backups and use supported state operations instead of manually editing files. Protect local state with filesystem permissions, encrypted disks/backups, and restricted artifact handling. A workspace selects a separate state instance; it is not a provider credential boundary or security boundary.

## Features

- `local` is Terraform's default backend when none is declared.
- `path` can explicitly select the local state-file location.
- Local workspaces use separate backend-specific state paths.
- State contains mapping and planning data and may include sensitive values.
- Backend selection is separate from providers, which communicate with infrastructure APIs.

## Do's and Don'ts

**Do**
- Use local state for isolated work where one operator controls the state lifecycle.
- Restrict access to state and backup files and maintain tested recovery procedures.
- Exclude state files and backups from version control and casual artifact sharing.
- Use a shared remote backend with suitable access controls and locking for team production state.

**Don't**
- Hand-edit `terraform.tfstate` or treat it as a disposable cache.
- Assume a workspace separates credentials or provides security isolation.
- Assume a local file coordinates multiple operators or machines.
- Commit state, backups, or other state-derived sensitive artifacts.

## Real-life implementation

For a solo sandbox, keep local state on an encrypted, access-controlled workstation, exclude it from Git and CI artifacts, and back it up according to the sandbox's recovery needs. For a production team, use a remote backend with controlled access, supported locking, recovery/versioning, and auditability rather than copying local state between operators. If migrating existing local state, explicitly initialize the new backend with state migration, verify the destination and resulting state, then ensure the team uses only the authoritative location.

## Q&A

1. **What backend is used when none is declared?** The local backend.
2. **Where is default local state normally stored?** In `terraform.tfstate` in the working directory.
3. **Is a backend block the same as a provider configuration?** No. A backend stores/coordinates state; a provider manages infrastructure APIs.
4. **Why is local state risky for teams?** It lacks shared remote coordination and centralized access management.

**Official references:**

- [Local backend](https://developer.hashicorp.com/terraform/language/backend/local)
- [Terraform state](https://developer.hashicorp.com/terraform/language/state)

[Back to the Terraform Associate syllabus](../../../copilot-terraform-syllabus.md)
