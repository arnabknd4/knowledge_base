# Objective: Apply retention policies to logs, artifacts, and workflow runs at organization or repository level, including through REST APIs.

## What

Retention policy is an operational governance control. It balances debugability and auditability against storage cost and data exposure risk. A good retention policy is explicit and aligned with release and compliance requirements.

## Why

- Shorter retention saves cost but may hamper incident investigation.
- Longer retention helps compliance and audits but increases exposure risk.
- Organization policies provide consistency but can reduce team flexibility.

## How

Set organization or repository defaults and choose artifact-level retention only within the applicable policy limits.

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: app-dist
    path: dist/
    retention-days: 14
```

## Features

Workflow logs, run records, and artifacts have retention settings governed by repository or organization policy; artifact retention can also be set for an upload within the allowed policy limits.

**Official references**

- [Artifact retention policies](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts#configuring-artifact-retention)
- [Workflow run retention policies](https://docs.github.com/en/organizations/managing-organization-settings/configuring-the-retention-period-for-github-actions-workflow-runs)
- [REST API for workflow runs and artifacts](https://docs.github.com/en/rest/actions)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Keep only the artifacts needed for evidence and debugging.
- Remove or restrict long-lived outputs containing secrets.
- Use organization-level governance for large-scale consistency and easier enforcement.

**Don't**

- Don't overlook that logs and artifacts have different retention controls.
- Don't assume a per-workflow override eliminates the need for organization policy.
- Don't retain sensitive artifacts longer than the business or compliance requirement.

## Real-life implementation

Balance investigation and compliance needs against storage cost and exposure. Set centrally governed defaults where available, use shorter retention for sensitive transient outputs, and preserve required release evidence intentionally.

## Q&A

**Q: What artifact retention window makes sense for a production deployment pipeline?**

**A:** Choose a period that supports incident response, audit, and release needs while respecting repository/organization limits; keep durable evidence in an approved records system if necessary.

**Q: Which artifacts should be deleted quickly because they contain environment-specific secrets or generated data?**

**A:** Do not upload secrets; minimize environment-specific files and set the shortest allowed retention for transient outputs that must be retained.

**Q: Can your org manage retention centrally rather than one repository at a time?**

**A:** Use organization or enterprise policy where available, then verify repository settings and per-artifact overrides remain within its constraints.
