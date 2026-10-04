# Manage GitHub Actions for the enterprise

This domain covers the enterprise control plane for GitHub Actions: reusable automation design, runner operations, and the secure handling of secrets and variables. In the GH-200 exam, the focus is on policy-compliant, observable, scalable, and safe automation across many repositories and environments.

## Learning path

1. Start with governance and access: understand how reusable components, workflow catalogs, and org-level policies become the operating model for the enterprise.
2. Learn runner design: choose between GitHub-hosted and self-hosted execution, apply perimeter controls, and plan for failure isolation and maintenance.
3. Master secrets and variables: scope them by organizational, repository, and environment boundaries, then validate runtime usage and automation flows.
4. Rehearse architecture decisions: explain when to centralize reusable workflows, when to use self-hosted runners, and how to protect trust boundaries without harming developer velocity.

## Topic folders

### 1. Distribute and govern actions and workflows
- [Define and manage reusable components and templates](./01-governance-and-access/01-reusable-components/study-guide.md)
- [Control access to actions and workflows within the enterprise](./01-governance-and-access/02-access-control/study-guide.md)
- [Configure organizational use policies](./01-governance-and-access/03-org-use-policies/study-guide.md)

### 2. Manage runners at scale
- [Configure and monitor GitHub-hosted and self-hosted runners](./02-runners-at-scale/01-github-hosted-and-self-hosted-runners/study-guide.md)
- [Apply IP allow lists and networking settings](./02-runners-at-scale/02-networking-and-ip-allowlists/study-guide.md)
- [Manage runner groups and troubleshoot runner issues](./02-runners-at-scale/03-runner-groups-and-troubleshooting/study-guide.md)
- [Identify preinstalled software and tool versions on GitHub-hosted runners](./02-runners-at-scale/04-hosted-runner-images-and-tool-cache/study-guide.md)
- [Install additional software at runtime](./02-runners-at-scale/05-runtime-software-installation/study-guide.md)

### 3. Manage encrypted secrets and variables
- [Define and scope encrypted secrets and variables](./03-secrets-and-variables/01-secrets-and-variables-scoping/study-guide.md)
- [Access and use secrets and variables in workflows and actions](./03-secrets-and-variables/02-secrets-and-variables-usage/study-guide.md)
- [Manage secrets and variables programmatically through REST APIs](./03-secrets-and-variables/03-secrets-and-variables-rest-api/study-guide.md)

## Architect-level focus

This domain is less about syntax and more about design choices that scale across engineering organizations:

- Centralizing reusable workflows and actions while preserving security boundaries.
- Choosing the correct runner type, network posture, and isolation model for each workload.
- Applying least privilege and environment-specific controls to secrets, variables, and automation access.
- Treating governance as an operating model, not a single repository setting.

## Official references

- [Exam GH-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [Using GitHub Actions in an enterprise](https://docs.github.com/en/actions/learn-github-actions/using-github-actions-in-your-enterprise)
- [GitHub Enterprise Cloud policies for GitHub Actions](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-github-actions-policies-for-your-enterprise)
