# 8c. Organize HCP Terraform workspaces and projects

## What

HCP Terraform projects organize workspaces. A project can group workspaces by coherent ownership or application boundary and apply project-level access/settings where supported. It does not merge state: each workspace retains separate configuration associations, variables, runs and state.

## Why

Workspace and project boundaries should make ownership, lifecycle, permissions and blast radius clear. A team should know which workspace is authoritative for each state and how another workspace consumes required values. Excessive sharing or automation links can make changes harder to reason about and expand the impact of a mistake.

## How

Align a workspace with a lifecycle and team able to review/apply its changes; use projects to group related workspaces without treating them as one state. Run triggers can start a downstream workspace run after successful upstream changes. They express sequencing, not a general dependency graph or automatic transfer of arbitrary resource attributes. For cross-state values, use remote-state data or another explicit interface; make dependencies directional and avoid cycles. Check relevant workspace settings and permissions.

Variable sets provide reusable workspace variables. They may be associated with specific workspaces and, where supported, a project, with selection/scope determined by configuration. Choose the narrowest association, manage precedence when workspace-specific values overlap, and separate credentials by environment/trust boundary. A variable set does not make broad secret distribution safe and is not a substitute for suitable dynamic credentials.

At scale, document project ownership, workspace/state authority, and stable output interfaces. Use names and labels for discoverability, not as access control. Isolate production state and credentials from development where blast radius or regulatory requirements call for it. Verify plan eligibility and current workspace/project settings for plan-dependent capabilities before relying on them.

## Features

* Projects group workspaces; each workspace retains its own state and lifecycle.
* Run triggers sequence downstream runs after upstream changes but do not transfer outputs.
* Variable sets share inputs at configured workspace/project scopes, with precedence and sensitivity implications.
* Project/workspace settings and feature availability vary; verify current plan support and permissions for plan-dependent capabilities.

## Do's and Don'ts

**Do**
* Assign clear project and workspace owners and document state boundaries and cross-state interfaces.
* Use run triggers only for intentional sequencing dependencies, with an explicit way to share values.
* Scope variable sets narrowly, manage precedence, and isolate credentials by environment.
* Verify feature availability and permissions before making a capability part of operations.

**Don't**
* Assume a project combines workspace state or creates a single run.
* Treat a run trigger as an output/value transfer mechanism or build circular triggers.
* Distribute sensitive variables more broadly than required.
* Rely on names/labels as access controls.

## Real-life implementation

A platform team has a shared network workspace and separate application workspaces. It groups them in a project with named owners, retains separate state for independent lifecycles, and configures a downstream run trigger only where an application deployment must follow a network change. The application receives needed values through a reviewed explicit interface rather than assuming the trigger passes outputs. Shared nonsecret settings use a narrowly scoped variable set; production credentials remain isolated. The team checks project/workspace permissions and feature eligibility before enabling optional controls.

## Q&A

1. **What does an HCP Terraform project contain?** Workspaces grouped under a project boundary.
2. **Does a run trigger transfer upstream outputs automatically?** No; use an explicit cross-state or other data interface.
3. **Where can variable sets be associated?** With configured workspaces and, where supported, projects.
4. **How should variable-set scope be selected?** As narrowly as necessary, especially for sensitive values.

Sources: [Projects](https://developer.hashicorp.com/terraform/cloud-docs/projects), [Workspaces](https://developer.hashicorp.com/terraform/cloud-docs/workspaces), [Run triggers](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/settings/run-triggers), [Variable sets](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/variables#variable-sets), [Remote state data](https://developer.hashicorp.com/terraform/language/state/remote-state-data).

[Back to the Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md)
