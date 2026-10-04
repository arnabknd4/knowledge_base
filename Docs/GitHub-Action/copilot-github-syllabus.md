# GitHub Actions Certification (GH-200) Syllabus

This syllabus follows the official **Exam GH-200: GitHub Actions** study guide. It is an exam-topic checklist, not a guarantee of passing: the official guide says its bullets illustrate how skills are assessed and that related topics may also appear.

> **Blueprint version:** Skills measured as of January 2026  
> **Audience:** People who create and maintain GitHub Actions workflows and actions, manage Actions at organizational or enterprise scale, and secure and optimize automation.

## Exam information

- **Exam code:** GH-200
- **Duration:** 100 minutes; the exam is proctored and may include interactive components.
- **Passing score:** 700 or higher.

## Exam domains

| Domain | Exam weight |
|---|---:|
| Author and manage workflows | 20–25% |
| Consume and troubleshoot workflows | 15–20% |
| Author and maintain actions | 15–20% |
| Manage GitHub Actions for the enterprise | 20–25% |
| Secure and optimize automation | 10–15% |

## 1. Author and manage workflows (20–25%)

### Configure workflow triggers and events

- [ ] Configure workflows to run for scheduled, manual, webhook, and repository events.
- [ ] Choose appropriate scope, permissions, and events for workflow automation.
- [ ] Define and validate `workflow_dispatch` inputs (types, required values, and defaults).
- [ ] Pass inputs to reusable workflows through `workflow_call`, including inputs and secrets mapping.

### Design and implement workflow structure

- [ ] Use jobs, steps, and conditional logic.
- [ ] Implement dependencies between jobs.
- [ ] Use workflow commands and environment variables.
- [ ] Use service containers (`services:`) for dependent services such as databases and queues; configure ports, health checks, and container options.
- [ ] Use `strategy` and `matrix` to generate job variations (for example, operating systems and language/runtime versions); apply `include`/`exclude`, control `fail-fast` and `max-parallel`, and optimize matrix size for cost and performance.
- [ ] Account for runner image changes and migrations (the study guide calls out Ubuntu 20.04 deprecation and the Windows Server 2025 migration for `windows-latest`).
- [ ] Use YAML anchors and aliases (`&`, `*`, and merge `<<`) to reuse mappings or steps within a workflow file.
- [ ] Use predefined contexts (`github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `strategy`, `job`, `steps`, `github.event`, and `github.ref`) to access workflow, repository, and runtime metadata.
- [ ] Understand immutable actions behavior and version-pinning requirements.
- [ ] Evaluate expressions with `${{ }}` and contexts; distinguish static (workflow-parse) and runtime evaluation.
- [ ] Prevent secret leakage in logs and expressions.
- [ ] Use editor tooling, including the GitHub Actions VS Code extension, YAML schema completion, metadata IntelliSense, and validation.

### Manage workflow execution and outputs

- [ ] Configure dependency caching and artifact management.
- [ ] Apply retention policies to logs, artifacts, and workflow runs at organization or repository level, including through REST APIs.
- [ ] Pass data between jobs and steps using artifacts, outputs, environment files (`GITHUB_ENV` and `GITHUB_OUTPUT`), and reusable workflow outputs.
- [ ] Generate Markdown job summaries with `GITHUB_STEP_SUMMARY`.
- [ ] Add workflow status badges and environment protections.

## 2. Consume and troubleshoot workflows (15–20%)

### Interpret workflow behavior and results

- [ ] Identify workflow triggers and their effects from configuration and logs.
- [ ] Diagnose failed workflow runs using logs and run history.
- [ ] Expand and interpret YAML anchors, aliases, and merged mappings when analyzing configuration.
- [ ] Interpret matrix expansions, connect job names to matrix axes, analyze failures across variants, and selectively rerun matrix jobs.

### Access workflow artifacts and logs

- [ ] Locate workflows, logs, and artifacts in the GitHub UI and through APIs.
- [ ] Download and manage workflow artifacts.

### Use and manage workflow templates

- [ ] Consume organization-level and reusable workflows.
- [ ] Consume non-public organization workflow templates.
- [ ] Use public and private/non-public starter workflows; customize and adapt them.
- [ ] Distinguish starter workflows, reusable workflows, and composite actions:
  - Starter workflows copy a scaffold that is independent after creation.
  - Reusable workflows provide a centrally versioned definition invoked with `workflow_call`.
  - Composite actions encapsulate step logic.
- [ ] Contrast disabling a workflow with deleting it.

## 3. Author and maintain actions (15–20%)

### Create and troubleshoot custom actions

- [ ] Identify and implement JavaScript, Docker, and composite actions.
- [ ] Understand immutable actions rollout on hosted runners and its implications for version pinning and registry sources.
- [ ] Troubleshoot action execution and errors.

### Define action structure and metadata

- [ ] Specify required files, directory structure, and metadata.
- [ ] Implement workflow commands within actions.

### Distribute and maintain actions

- [ ] Select distribution models (public, private, or Marketplace).
- [ ] Publish actions to GitHub Marketplace.
- [ ] Apply versioning and release strategies.

## 4. Manage GitHub Actions for the enterprise (20–25%)

### Distribute and govern actions and workflows

- [ ] Define and manage reusable components and templates.
- [ ] Control access to actions and workflows within the enterprise.
- [ ] Configure organizational use policies.

### Manage runners at scale

- [ ] Configure and monitor GitHub-hosted and self-hosted runners.
- [ ] Apply IP allow lists and networking settings.
- [ ] Manage runner groups and troubleshoot runner issues.
- [ ] Identify preinstalled software and tool versions on GitHub-hosted runners using image release notes and the tool cache.
- [ ] Install additional software at runtime using `setup-*` actions, package managers, caching, container images, or custom self-hosted images.

### Manage encrypted secrets and variables

- [ ] Define and scope encrypted secrets and variables at organization, repository, and environment levels.
- [ ] Access and use secrets and variables in workflows and actions.
- [ ] Manage secrets and variables programmatically through REST APIs.

## 5. Secure and optimize automation (10–15%)

### Implement security best practices

- [ ] Use environment protections and approval gates.
- [ ] Identify and use trustworthy actions from GitHub Marketplace.
- [ ] Mitigate script injection: sanitize and validate inputs, use least-privilege permissions, avoid untrusted data in `run:`, use proper shell quoting, and prefer vetted actions over inline scripts.
- [ ] Understand the `GITHUB_TOKEN` lifecycle and scope; configure granular permissions, contrast it with a personal access token (PAT), and restrict write scopes.
- [ ] Use OIDC (`id-token` permission) for cloud-provider federation instead of long-lived cloud secrets.
- [ ] Pin third-party actions to full commit SHAs; understand immutable-actions enforcement on hosted runners and avoid floating `@main`/`@v*` references without justification.
- [ ] Enforce action-usage policies, including organization/repository allow and deny lists and required reviewers for unverified actions.
- [ ] Generate and verify artifact attestations/provenance (for example, SLSA and build metadata) and integrate verification into deployments.

### Optimize workflow performance and cost

- [ ] Configure caching and artifact retention for efficiency, including programmatic retention policies through REST APIs.
- [ ] Recommend strategies for scaling and optimizing workflows.

## Readiness check

- [ ] Review every domain and be able to explain when and why to use each feature, not only recognize its syntax.
- [ ] Practice authoring workflows, reusable workflows, and custom actions in a test repository.
- [ ] Practice diagnosing failed runs, interpreting matrices, and working with logs and artifacts.
- [ ] Review security and governance choices, especially token permissions, untrusted input, action pinning, OIDC, runner isolation, and enterprise policies.
- [ ] Recheck the official study guide before booking; its skills-measured date and details can change.

## Official sources

- [Exam GH-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200) — authoritative domains, weights, and skills measured.
- [GitHub Actions certification page](https://learn.microsoft.com/en-us/credentials/certifications/github-actions/) — exam logistics and certification information.
- [Exam scoring and score reports](https://learn.microsoft.com/en-us/credentials/certifications/exam-scoring-reports) — passing-score information.
- [GitHub Actions documentation](https://docs.github.com/en/actions) — product documentation and hands-on references.
