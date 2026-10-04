# 8d. Configure and use HCP Terraform integration

## What

The Terraform CLI integrates with HCP Terraform for centralized state and coordinated runs. A root module can configure this connection with a `cloud` block that selects an organization and maps the working directory to remote workspace(s). The `cloud` block is an alternative to a `backend` block, not an additional backend configuration in the same root module.

## Why

The integration centralizes state, locking, run history and collaboration. It also makes correct organization/workspace selection, credentials, execution mode, Terraform version and migration planning important. A wrong mapping can direct a plan or state migration at the wrong workspace.

## How

Authenticate with `terraform login`; the CLI stores an API token in its credentials file. Treat it like a password: use approved credential storage, restrict access, and revoke it when no longer needed. Never place tokens in HCL, source control, shell history or build logs.

```hcl
terraform {
  cloud {
    organization = "acme-platform"
    workspaces {
      name = "network-prod"
    }
  }
}
```

The workspace mapping can use a fixed name or a prefix-based mapping. After adding or changing cloud configuration, run `terraform init` and carefully verify the effective workspace before planning. Keep the CLI, workspace Terraform version, configuration and providers compatible.

When changing from local state to HCP Terraform, `terraform init` detects the configuration change and offers state migration. First make a secure state backup, verify the destination organization/workspace and its readiness, coordinate with teammates/automation, and stop competing applies. Follow the migration prompts; do not assume configuration upload migrates state or copy/edit state manually. Inspect the destination state and run a plan to verify continuity.

With remote execution, CLI `plan`/`apply` commands initiate and display remote runs; the HCP workspace's configured execution mode determines where work runs. Remote mode uses HCP-hosted workers, agent mode uses a customer-managed agent pool, and local mode executes on the operator's machine. Remote state and remote execution are separate. Exact governance and execution integrations can be plan-dependent; check entitlement and workspace settings before relying on them.

## Features

* `terraform login` authenticates the CLI; it does not select a workspace or configure cloud integration.
* `cloud` configures HCP Terraform organization/workspace mapping; `backend` is an alternative.
* `terraform init` handles configuration changes and offers backend/cloud state migration.
* CLI-driven runs may execute remotely; workspace execution mode and settings determine where they run.
* Execution/governance feature availability can depend on plan and configuration; verify before use.

## Do's and Don'ts

**Do**
* Protect CLI API tokens and verify organization, workspace mapping, execution mode and Terraform version.
* Back up state, coordinate operators and automation, and stop competing applies before migration.
* Review migration prompts, inspect destination state and run a plan to confirm continuity.

**Don't**
* Configure both `cloud` and a `backend` block in the same root module.
* Assume `terraform login` configured the workspace or that remote state guarantees remote execution.
* Copy/edit state manually or migrate into an unverified destination.
* Assume plan-dependent features are universally available.

## Real-life implementation

A team moves a local production root module to an HCP Terraform workspace. They authenticate through the approved CLI process, add the `cloud` block to a reviewed change, and have an operator verify the organization and fixed workspace name. Before `terraform init`, they secure a state backup, pause local and CI applies, and confirm the destination workspace is ready. After following the migration prompt, they inspect the remote state and run a plan; only after a no-unintended-change review do they resume the production pipeline. The workspace's configured execution mode and permissions are independently verified.

## Q&A

1. **How does the CLI authenticate to HCP Terraform?** `terraform login` obtains credentials stored in the CLI credentials file.
2. **Can a root module use both `cloud` and `backend` blocks?** No; cloud configuration is an alternative.
3. **Which command handles backend/cloud reconfiguration and migration?** `terraform init`.
4. **What should precede a state migration?** A secure backup, destination verification, and coordination to prevent concurrent applies.

Sources: [HCP Terraform CLI-driven workflow](https://developer.hashicorp.com/terraform/cloud-docs/run/cli), [`terraform login`](https://developer.hashicorp.com/terraform/cli/commands/login), [Cloud integration configuration](https://developer.hashicorp.com/terraform/language/terraform#cloud), [Backend configuration and migration](https://developer.hashicorp.com/terraform/language/backend), [Terraform version settings](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/settings#terraform-version).

[Back to the Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md)
