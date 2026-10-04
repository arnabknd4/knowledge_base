# Manage secrets and variables programmatically through REST APIs

## What
The GitHub REST API lets platform teams automate the lifecycle of secrets and variables across organizations, repositories, and environments. This gives enterprises a repeatable and auditable path for provisioning and rotating values.

## Why
Manual secret management does not scale in large organizations. API-driven workflows support service accounts, central provisioning pipelines, and rotation policies without requiring human operators to create or edit each secret in the UI.

## How
- Use the GitHub REST API for org-, repo-, and environment-scoped values when automation is required.
- Protect the automation identity with least privilege and strict audit logging.
- Validate the target repository or environment before updating any secret or variable.
- Pair API automation with rotation, review, and approval patterns so credential changes remain controlled and traceable.

## Features
- Organization, repository, and environment API endpoints.
- Auditable automation for provisioning and updates.
- Rotation-friendly lifecycle management.
- Service-account or GitHub App identity controls for safe automation.

## Do's and Don'ts
- Do: protect the automation identity used to call the API.
- Do: log and review writes to secrets and variables.
- Do: validate repository and environment target before mutating values.
- Do: align automation with rotation and expiry policies.
- Don't: assume API access is automatically safe or appropriate for all use cases.
- Don't: forget that org, repo, and environment APIs have different permissions and scope semantics.
- Don't: allow broad automation identities to create or update production secrets without review.
- Don't: run secret provisioning without audit trails and rotation hygiene.

## Real-life implementation
A platform team exposes a provisioning job that calls the GitHub REST API to create or update environment variables for deployment pipelines. The job runs beneath a tightly scoped GitHub App or service account, with audit logging and rotation policies to keep access traceable and controlled.

## Q&A
### Q: Why automate secret creation through the REST API?
A: Because a platform team can provision and rotate values consistently across many repos and environments with built-in auditability.

### Q: Which identity should be used for API automation?
A: A least-privilege service account or GitHub App configured only for the endpoints and scope needed for the platform workflow.

### Q: What is the biggest correctness issue in secret API workflows?
A: Using the wrong endpoint or wrong scope, which can update the wrong repo or environment or create an accidental exposure.

### Q: What operational controls should accompany API access?
A: Audit logs, approval gates, rotation plans, and explicit validation before each create or update action.

## Official docs
- [REST API for GitHub Actions secrets](https://docs.github.com/en/rest/actions/secrets?apiVersion=2022-11-28)
- [REST API for GitHub Actions variables](https://docs.github.com/en/rest/actions/variables?apiVersion=2022-11-28)
- [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
- [Using environments for deployment](https://docs.github.com/en/actions/deployment/using-environments-for-deployment)
- [About GitHub Apps and permissions](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps)

## Back to syllabus
- [Manage GitHub Actions for the enterprise](../../README.md)
