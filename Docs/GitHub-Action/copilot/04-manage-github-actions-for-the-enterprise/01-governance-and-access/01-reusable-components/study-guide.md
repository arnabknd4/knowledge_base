# Define and manage reusable components and templates

## What
Reusable workflows, composite actions, and workflow templates let an enterprise standardize the highest-value automation patterns while keeping teams productive. The goal is to create a trusted catalog of automation assets that is reviewed, versioned, and safe to call from many repositories.

## Why
Duplicate pipelines create drift, inconsistent release controls, and a weak security model. Centralized automation gives platform teams a control point for compliance, environment gating, and release quality without forcing every repo to reinvent the same deployment logic.

## How
- Build a shared automation repository or private enterprise catalog for CI, security, and deployment workflows.
- Define input contracts and outputs clearly so workflows remain portable and easy to review.
- Version reusable assets with immutable references, and require review for changes that affect multiple teams.
- Pair reusable workflows with CODEOWNERS, branch protections, or policy reviews so production standards stay enforced.

## Features
- Reusable workflow orchestration for shared pipeline logic.
- Private actions for domain-specific tasks such as deployment validation or artifact signing.
- Workflow templates for consistent onboarding and repository bootstrapping.
- Standard inputs and outputs for portability and safer upgrades.

## Do's and Don'ts
- Do: keep reusable assets in an approved catalog and assign clear ownership.
- Do: make shared workflow contracts explicit and versioned.
- Do: review and test changes before they impact many repositories.
- Do: document compatibility and migration expectations for downstream callers.
- Don't: use floating refs for critical production workflows.
- Don't: centralize everything into one giant workflow with unclear ownership.
- Don't: assume a template is compliant without policy and review checks.
- Don't: hide secrets or environment assumptions inside shared workflows.

## Real-life implementation
A platform team maintains a reusable deploy.yml workflow in a shared repo. Product teams call it with parameters for environment, region, and artifact name, and the workflow enforces required approvals, security scans, and release evidence. The shared catalog reduces duplicate logic while preserving a single place to tighten controls.

## Q&A
### Q: What is the main difference between a reusable workflow, a private action, and a template?
A: A reusable workflow orchestrates jobs across repositories; a private action packages a small, reusable task; a template bootstraps a new workflow or repo with standard defaults and guardrails.

### Q: Why is versioning important for reusable assets?
A: Version pinning prevents accidental breakage, makes governance review easier, and reduces surprise changes when a shared workflow is updated.

### Q: Which operational controls should be enforced for enterprise workflow catalogs?
A: Clear ownership, review gates, branch protections, documented interfaces, and compatibility testing for downstream repositories.

### Q: How do templates improve enterprise governance?
A: They reduce drift by forcing new projects to include the expected security, release, and artifact controls from the start.

## Official docs
- [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)
- [Creating a composite action](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action)
- [Using workflow templates](https://docs.github.com/en/actions/using-workflows/using-workflow-templates)
- [About GitHub Marketplace actions](https://docs.github.com/en/actions/using-workflows/using-github-marketplace-actions)

## Back to syllabus
- [Manage GitHub Actions for the enterprise](../../README.md)
