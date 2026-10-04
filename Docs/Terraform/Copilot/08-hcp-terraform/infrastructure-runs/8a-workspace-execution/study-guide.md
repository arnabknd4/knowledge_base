# 8a. Use HCP Terraform to create infrastructure

## What

An HCP Terraform workspace is an operational boundary for configuration and its runs, variables, state, history, and access controls. It is not simply a directory or a local `terraform workspace`: a cloud workspace retains its own state and associates each run with configuration and inputs. Workspace execution mode determines where Terraform runs execute.

## Why

Workspace boundaries can align ownership, lifecycle, access and blast radius. A workspace is not inherently one repository or cloud account. Splitting unrelated systems can improve separation; excessive fragmentation adds coordination and explicit cross-state data-sharing overhead. HCP Terraform centralizes state, locking, run history, credentials and collaboration, while making permissions, variable configuration, network access and worker availability part of the delivery path.

## How

A common workflow connects a workspace to version control. A commit can trigger a run that fetches the selected configuration, initializes providers/modules, plans with workspace state and variables, then waits for any configured review/approval. Operators can also initiate runs through the Terraform CLI.

* **Remote:** runs execute on HCP Terraform-hosted workers.
* **Agent:** runs execute on customer-managed agents in an agent pool, useful for private network access or a controlled execution environment.
* **Local:** Terraform executes on the operator's machine, while the HCP workspace can still provide remote state and coordination. Remote state does not mean remote execution.

Confirm the configured mode and current workspace settings rather than inferring execution location from the CLI or state location. Pin compatible Terraform/provider versions, use least-privilege credentials, protect sensitive variables, and define who can review, approve and apply. Production workflows commonly use a human approval or policy gate. Account for queued and canceled runs and coordinate changes to avoid competing applies.

## Features

* Workspaces keep their own state, variables, run history and configuration relationship.
* VCS-driven and CLI-driven workflows can initiate runs; the CLI can drive remote execution.
* Remote, agent and local modes differ in execution location and access.
* Workspace capabilities and governance integrations may depend on the organization's HCP Terraform plan and settings. Verify eligibility for plan-dependent features rather than assuming they are included universally.

## Do's and Don'ts

**Do**
* Set workspace boundaries around clear ownership, lifecycle and blast-radius needs.
* Verify execution mode, Terraform version, state, variables and permissions before a production run.
* Use least privilege, protect credentials, and require appropriate review/approval.

**Don't**
* Confuse an HCP Terraform workspace with a local CLI workspace.
* Infer remote execution just because state is remote or a CLI command initiated the run.
* Assume every governance/execution feature is included in every plan.
* Treat a workspace as an automatic cloud-account or repository boundary.

## Real-life implementation

A team deploys an application into a private network. It creates a production workspace with its own state and restricted apply permissions, configures an agent pool with access to the private API, and connects a protected VCS branch. A commit creates a plan; an authorized reviewer checks it before apply. The team confirms agent execution mode, pins supported versions, stores credentials as protected workspace inputs, and tests the workflow in a nonproduction workspace before production use.

## Q&A

1. **Where is HCP workspace state kept?** In that remote workspace's state.
2. **Can a CLI command initiate a remote run?** Yes, when the workspace and CLI workflow are configured for it.
3. **When is agent execution useful?** When runs need customer-managed execution or private-network access.
4. **Does local execution imply local state?** No; execution location and state location are separate.

Sources: [HCP Terraform workspaces](https://developer.hashicorp.com/terraform/cloud-docs/workspaces), [Remote operations](https://developer.hashicorp.com/terraform/cloud-docs/run/remote-operations), [Agents](https://developer.hashicorp.com/terraform/cloud-docs/agents), [Execution modes](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/settings#execution-mode).

[Back to the Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md)
