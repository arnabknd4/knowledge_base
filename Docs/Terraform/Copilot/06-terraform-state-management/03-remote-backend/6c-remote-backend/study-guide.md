# 6c — Configure remote state using the backend block

## What

A remote backend stores Terraform state in a shared service rather than only in an operator's working directory. It is configured in the top-level `terraform` block and is distinct from a provider: the backend stores and coordinates state; a provider authenticates to and manages infrastructure APIs.

For example, Terraform 1.12 supports the S3 backend's S3 lockfile option:

```hcl
terraform {
  backend "s3" {
    bucket       = "company-terraform-state"
    key          = "prod/network.tfstate"
    region       = "us-east-1"
    use_lockfile = true
  }
}
```

Backend configuration is processed during `terraform init`, before normal provider configuration can be used. It cannot reference Terraform variables, locals, data sources, or resource attributes. One configuration has one backend. Partial configuration can be supplied at initialization, for example `terraform init -backend-config=backend-prod.hcl`.

## Why

Remote state enables shared access and centralized controls and, when supported, locking. It also introduces dependencies on backend availability, credentials, permissions, and recovery design. Remote state can contain secrets, so remote location alone does not make it safe.

## How

Keep backend credentials out of HCL and source control. Use supported environment, workload identity, profile, or credential-chain mechanisms. Protect the state service with least-privilege access, encryption, versioning/recovery, audit controls, and appropriate network policies.

Run `terraform init` after adding or changing backend configuration. To move existing state to a new backend, back up and verify both locations, coordinate the migration, and use `terraform init -migrate-state` to copy the existing state when prompted. Confirm the destination state and workspace before applying; do not operate the old and new locations as separate authoritative states. `terraform init -reconfigure` discards the previously initialized backend configuration and initializes the new one without copying old state. It is not a migration command; use it only when deliberately repointing/reinitializing and you understand where the prior state remains.

Provider credentials do not automatically authenticate backend access. Backend initialization must be able to access the state service independently of ordinary resource provider configuration.

## Features

- Remote backends provide shared state; locking is backend-dependent.
- Backend arguments are initialized before normal Terraform evaluation and cannot use expressions.
- Partial backend configuration can be supplied using `-backend-config`.
- `-migrate-state` migrates existing state; `-reconfigure` initializes without migration.
- S3's `use_lockfile = true` enables its lockfile-based locking option.

## Do's and Don'ts

**Do**
- Separate backend and provider access credentials and grant each least privilege.
- Protect remote state and recovery copies as sensitive data.
- Back up, coordinate, and verify source, destination, workspace, and state during migration.
- Use `-migrate-state` when the intended operation is to transfer existing state.
- Keep backend secrets out of committed HCL and partial configuration files.

**Don't**
- Put credentials into HCL, committed backend files, or source-control URLs.
- Use Terraform expressions such as `var.bucket` in a backend block.
- Mistake `-reconfigure` for a state-copy or migration operation.
- Allow old and new backends to be independently applied as authorities for the same objects.
- Assume remote storage is automatically encrypted, locked, or protected from unauthorized access.

## Real-life implementation

For production, provision a dedicated state location per environment/system with encryption, versioning or recovery, audit logging, private access controls, and least-privilege identities. Ensure the backend's lock capability and failure modes are understood and that CI runners can access the backend independently from provider APIs. Keep nonsecret backend settings in configuration or reviewed partial files and inject credentials via workload identity. For local-to-remote migration, freeze applies, back up state, initialize with `-migrate-state`, verify the destination workspace and state, then switch all operators and pipelines to the single authoritative backend before resuming changes.

## Q&A

1. **What configures where Terraform stores state?** A backend block in the `terraform` block.
2. **Can `backend "s3"` set `bucket = var.bucket`?** No. Supply backend settings during initialization, not with Terraform expressions.
3. **Which option migrates existing state to a changed backend?** `terraform init -migrate-state`.
4. **What does `terraform init -reconfigure` do?** Initializes the new backend configuration without copying the old state.

**Official references:**

- [Backend configuration](https://developer.hashicorp.com/terraform/language/backend)
- [S3 backend](https://developer.hashicorp.com/terraform/language/backend/s3)
- [Backend initialization and migration](https://developer.hashicorp.com/terraform/cli/commands/init#backend-initialization)

[Back to the Terraform Associate syllabus](../../../copilot-terraform-syllabus.md)
