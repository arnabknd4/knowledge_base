# 8b. Describe HCP Terraform collaboration and governance

## What

HCP Terraform supports shared infrastructure operations through teams and scoped permissions, private registries, shared variables, reviewed runs and policy controls. Governance also includes capabilities such as health assessments, workspace/resource visibility, dynamic provider credentials and change review, subject to product support and configuration.

## Why

Centralized collaboration can make ownership, approvals and audit history visible, while reusable modules and policy checks can improve consistency. Controls only work when permissions are least-privilege, policy outcomes have owners, and exceptions are deliberate. Governance does not replace sound module design, cloud IAM or operational review.

## How

Group users into teams and scope permissions to organization, project or workspace resources. Review memberships and tokens regularly, and separate administrative duties where risk warrants it. Use the private registry to publish and consume versioned internal modules/providers; review source, releases and compatibility. Variable sets share inputs across configured scopes, so limit their reach and keep secrets out of source control. Where supported, dynamic provider credentials can use short-lived credentials, but trust/claim mappings and cloud IAM must still be least-privilege.

Policy enforcement can evaluate plans; Sentinel and other policy-as-code integrations are available in supported configurations. Policies may be advisory or mandatory. Test changes against representative plans before mandatory rollout, assign exception ownership, and investigate rejected plans rather than bypassing controls.

Health assessments can check for configuration drift and configured continuous validation. HCP Terraform Explorer provides organization-level visibility for workspace/resource inventory and discovery. Drift is a signal to investigate, not an instruction to overwrite an external change. Change requests provide a reviewable path for supported workspace changes and work alongside run approvals. Availability and integrations vary: verify the organization's plan, settings, VCS integration and exact feature eligibility. Policy enforcement, drift/health assessment, Explorer, change requests and dynamic credentials must not be assumed available to every organization or workspace.

## Features

* Teams/permissions scope collaboration; the private registry distributes versioned modules and providers.
* Variable sets share inputs at configured scopes; their precedence and secret exposure need deliberate management.
* Policy-as-code checks plans with advisory or mandatory enforcement in supported configurations.
* Health assessments, Explorer, change requests and dynamic credentials support operations in eligible configurations.
* Plan- or configuration-dependent features must be checked against current product entitlements and workspace settings.

## Do's and Don'ts

**Do**
* Grant narrowly scoped permissions and review access, tokens and policy exceptions.
* Version and review private modules; scope variable sets to only workspaces that need them.
* Test policies before enforcement, and assign owners for failures, drift and exceptions.
* Verify plan eligibility and integration settings before designing an operational dependency on a feature.

**Don't**
* Distribute all secrets organization-wide or store credentials in source control.
* Treat drift detection as automatic repair or a decision about which version is correct.
* Assume dynamic credentials remove the need for least-privilege IAM and secure trust configuration.
* Assume a feature is universally included or bypass a mandatory policy without an approved exception.

## Real-life implementation

Before rolling out a mandatory policy for production, a platform team tests it against representative plans in a nonproduction project and documents approved exceptions with owners. They scope production credentials and team permissions to the production workspaces, use a versioned private module, and enable drift/health checks only after confirming their plan and settings support them. When a workspace reports drift, the owner investigates whether the external change was intentional before updating configuration or applying a correction.

## Q&A

1. **What is the private registry for?** Publishing and consuming versioned private modules and providers.
2. **Does drift detection automatically repair drift?** No; teams investigate and select a corrective action.
3. **Why use dynamic provider credentials where supported?** To avoid persisting long-lived cloud credentials, while retaining secure trust and least-privilege IAM.
4. **What should happen before mandatory policy rollout?** Test representative plans and define ownership for failures and exceptions.

Sources: [Teams and permissions](https://developer.hashicorp.com/terraform/cloud-docs/users-teams-organizations/permissions), [Private registry](https://developer.hashicorp.com/terraform/cloud-docs/registry), [Policy enforcement](https://developer.hashicorp.com/terraform/cloud-docs/policy-enforcement), [Variable sets](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/variables#variable-sets), [Dynamic provider credentials](https://developer.hashicorp.com/terraform/cloud-docs/dynamic-provider-credentials), [Health assessments](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/health), [HCP Terraform Explorer](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/explorer), [Change requests](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/change-requests).

[Back to the Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md)
