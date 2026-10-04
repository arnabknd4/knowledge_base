# Consume non-public organization workflow templates

## What
A non-public organization workflow template is an internal or private starter for approved automation. Access is controlled by repository visibility and organization policies, and the consumer must be allowed to discover and use the template. The source is a template authoring point, not a live runtime dependency.

## Why
Private or internal templates are useful when policy, deployment standards, or secrets must stay inside the organization. However, their behavior depends on access, copy lifecycle, and the destination repository’s settings, not just the template source itself.

## How
1. Confirm the template is meant for starter use and not a reusable workflow or action.
2. Verify the consumer repository has access to the template source and organization policy permits the use case.
3. Create or copy the workflow in the destination repository and review the generated file.
4. Replace placeholders for environment names, permissions, runner labels, and deployment targets.
5. Validate in a low-risk repository or branch and document the source/version used.
6. Track future updates explicitly because copied templates do not automatically stay in sync.

## Features
- Access boundaries: private and internal visibility add rules and administrative work.
- Local copy lifecycle: copied workflows are independent after creation.
- Policy alignment: organization templates help standardize approved automation.
- Drift risk: source updates do not automatically propagate to copies.

## Do's and Don'ts
### Do
- Verify access and intended audience before assuming a template can be used.
- Review the copied workflow in the target repository before enabling it.
- Keep a record of the template source and version used.

### Don't
- Don't assume a private template is automatically a reusable workflow.
- Don't assume copied workflows receive future source updates.
- Don't ignore target-repo permissions, secrets, and environment settings.

## Real-life implementation
```yaml
# Created from a private organization template
name: Release
on:
  workflow_dispatch:
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - run: ./release.sh
```

This generated workflow still runs under the destination repository’s permissions and environment protections. The template source only served as the starting point; all subsequent behavior depends on the copy and its target context.

### Official references
- [Creating starter workflows for your organization](https://docs.github.com/en/actions/sharing-automations/creating-starter-workflows-for-your-organization)
- [Sharing workflows, secrets, and runners within an organization](https://docs.github.com/en/actions/sharing-automations/sharing-workflows-secrets-and-runners-with-your-organization)
- [Repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)

## Q&A
### Q: A template source is updated after three repositories copied it. Do their workflows change automatically?
A: No. A copied workflow is a local copy, not a live reference to the source. It must be updated intentionally.

### Q: What organization and repository settings could prevent a consumer from finding or using the template?
A: Repository visibility, organization template settings, permissions, and whether the consumer repository is in the permitted organization or audience can all block use.

### Q: Which fields should be reviewed before enabling a copied deployment workflow?
A: Branch filters, triggers, permissions, secret usage, runner labels, environment names, and deployment target configuration should all be reviewed in the destination repository.
