# Use public and private starter workflows

## What
A starter workflow is a scaffold for creating a repository workflow file. It is copied into a repository and then customized. Public starter workflows are discoverable by a broad audience, while private or internal organization starters are scoped to eligible organizations or repos. The underlying idea is the same: You start from an approved pattern, not a centrally running workflow.

## Why
Most teams do not begin with a blank workflow file. A starter can provide best practices, runtime setup, and a tested convention, but it still needs review before you rely on it for production automation.

## How
1. Choose a starter that matches the task and supported platform.
2. Review the source, action versions, triggers, permissions, and secrets before adopting it.
3. Customize triggers, path filters, environment names, and runner selections to the target repository.
4. Remove sample deploy logic, unused permissions, and placeholder values that could point to production or expose secrets.
5. Validate the copied workflow in a non-production context and document ownership for future updates.

## Features
- Public discoverability: broad ecosystem reuse, but not necessarily the right governance model for your repo.
- Private/internal tailoring: aligned with organizational standards and access policies.
- Local ownership: after copy, the workflow is part of the destination repo and evolves there.
- Customization needs: review and harden all default values before production use.

## Do's and Don'ts
### Do
- Review the starter for permissions, action versions, and triggers before enabling it.
- Pin third-party actions to a full commit SHA when supply-chain assurance is required.
- Treat the starter as a template to adapt, not a safe default.

### Don't
- Don't assume a public starter is secure or policy-compliant just because it is public.
- Don't assume the source starter updates every copied workflow.
- Don't leave placeholder secrets, environment names, or deploy targets in a production workflow.

## Real-life implementation
```yaml
name: Node CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci && npm test
```

This is typical starter-based workflow scaffolding. It needs review and adaptation for organization policy, environment-specific permissions, and deployment needs before being trusted in production.

### Official references
- [Using starter workflows](https://docs.github.com/en/actions/writing-workflows/using-starter-workflows)
- [Creating starter workflows for your organization](https://docs.github.com/en/actions/sharing-automations/creating-starter-workflows-for-your-organization)
- [Secure use reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)

## Q&A
### Q: A copied starter contains a deploy step and broad token permissions. What should be reviewed before enabling it?
A: Review the deploy target, environment protections, permissions, secrets, runtime assumptions, and any placeholder values that could accidentally deploy to production.

### Q: How can an organization keep copied starters aligned over time?
A: Document the source, set ownership for periodic reviews, and re-apply approved improvements intentionally when copy drift is no longer acceptable.

### Q: Does changing the source starter alter repositories that already copied it?
A: No. The existing workflow copy remains independent unless someone manually updates or re-copies it.
