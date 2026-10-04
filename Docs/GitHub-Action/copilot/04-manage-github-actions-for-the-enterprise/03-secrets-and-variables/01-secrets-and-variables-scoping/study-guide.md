# Define and scope encrypted secrets and variables at organization, repository, and environment levels

## What
Secrets and variables are the enterprise control points for configuration and credentials. Their scope should align with their trust boundary so each workflow gets only the values it is allowed to use.

## Why
Scope determines exposure. Putting a sensitive value at the wrong level broadens blast radius, encourages unsafe sharing, and makes compliance harder to justify. The right scope is part of secure design, not a afterthought.

## How
- Use organization-level values for shared enterprise settings or approved platform-wide secrets.
- Use repository-level values when a secret or variable is specific to one project and should not be automatically shared across organizations.
- Use environment-level values for production and approval-sensitive release paths.
- Keep variables for non-sensitive metadata and secrets for sensitive credentials or tokens.

## Features
- Org-scoped secrets and variables for shared platform use.
- Repo-scoped configuration for project-specific trust boundaries.
- Environment-scoped access for production and stage-specific secrets.
- Clear separation between sensitive and non-sensitive configuration.

## Do's and Don'ts
- Do: scope each secret to the narrowest valid trust boundary.
- Do: prefer environment secrets for production deployments and environment approvals.
- Do: review ownership and rotation schedules for every shared secret.
- Do: document whether a value is a secret or a variable before sharing it broadly.
- Don't: store sensitive data in variables.
- Don't: treat org, repo, and environment scopes as interchangeable.
- Don't: assume environment secrets appear without selecting the environment.
- Don't: allow production secrets to be reused blindly across all repos.

## Real-life implementation
A platform team stores cloud federation configuration at the organization level. Each service repo retains its own repository-specific credentials, while production deployments rely on environment-scoped secrets and approvals tied to the `production` environment. This reduces shared risk while keeping the platform consistent.

## Q&A
### Q: When is org-level scope appropriate?
A: When multiple repos need the same approved, enterprise-owned value and the access model is intentionally shared.

### Q: When should you prefer environment scope?
A: When the value is sensitive, approval-driven, or only valid for a specific production or staging path.

### Q: Why separate variables from secrets?
A: Variables are for non-sensitive configuration; secrets protect credentials and other values that must not be exposed in logs or plain text.

### Q: What is the design principle behind scoping?
A: Use the smallest trust boundary that still enables the workflow to work, which minimizes exposure and simplifies governance.

## Official docs
- [Using variables in a workflow](https://docs.github.com/en/actions/learn-github-actions/variables)
- [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
- [Using environments for deployment](https://docs.github.com/en/actions/deployment/using-environments-for-deployment)
- [Managing secrets for an organization](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-an-organization)
- [Managing secrets for a repository](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)

## Back to syllabus
- [Manage GitHub Actions for the enterprise](../../README.md)
