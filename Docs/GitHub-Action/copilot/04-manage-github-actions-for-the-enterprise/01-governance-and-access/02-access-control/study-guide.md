# Control access to actions and workflows within the enterprise

## What
Enterprise access control limits who can run workflows, which actions are trusted, and how workflow permissions map to production risk. The goal is to protect the organization from accidental changes, unsafe deployments, and over-scoped automation.

## Why
A workflow can read secrets, deploy infrastructure, publish artifacts, and interact with cloud systems. Access must be constrained at the organization, repository, and environment layers, not just by who can write code.

## How
- Configure org and repo settings to allow or restrict GitHub Actions by default.
- Require environment approvals for production and sensitive deployments.
- Restrict workflow permissions to the minimum needed for the job.
- Review and pin third-party actions so the action source and version are trusted and explicit.

## Features
- Organization-level governance for allowed actions and runner usage.
- Repository settings for enabling or restricting workflows.
- Environment protection rules for approvals and deployment gates.
- Least-privilege workflow permissions and OIDC-based cloud authentication.

## Do's and Don'ts
- Do: align access decisions to the trust boundary: org policy, repo settings, environment protection, and action source.
- Do: require approval or manual review for production deployments.
- Do: enforce least-privilege permissions and protect sensitive secrets.
- Do: document how untrusted or newly approved actions are reviewed.
- Don't: rely on repository settings alone to enforce enterprise policy.
- Don't: treat all third-party actions as equally safe.
- Don't: allow broad workflow permissions for release jobs.
- Don't: skip environment protection when deploying to production.

## Real-life implementation
A finance platform permits GitHub-hosted runners for standard CI work and only allows a curated set of approved actions. Production deployment requires an environment approval and a security scan before the workflow can proceed. This combination reduces risk while keeping development velocity high for non-production work.

## Q&A
### Q: Why is environment protection critical for production workflows?
A: It adds explicit approvals, required checks, or gating logic before a workflow can reach a sensitive deployment target.

### Q: What is the difference between org-level and repo-level action controls?
A: Org-level policies define enterprise-wide trust rules; repo-level settings fine-tune control for an individual project.

### Q: How does least privilege reduce risk?
A: It limits each workflow to the permissions it truly needs, reducing blast radius if an action is abused or a token leaks.

### Q: Why pin actions to immutable SHAs?
A: It prevents silent changes from a mutable tag or branch and makes the trusted action version explicit and auditable.

## Official docs
- [Disabling or limiting GitHub Actions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization)
- [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository)
- [Using environments for deployment](https://docs.github.com/en/actions/deployment/using-environments-for-deployment)
- [Using OIDC with cloud providers](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- [GitHub Enterprise Cloud policies for GitHub Actions](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-github-actions-policies-for-your-enterprise)

## Back to syllabus
- [Manage GitHub Actions for the enterprise](../../README.md)
