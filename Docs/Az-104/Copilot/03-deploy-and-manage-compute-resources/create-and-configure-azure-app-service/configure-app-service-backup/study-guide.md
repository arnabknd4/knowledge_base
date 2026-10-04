# Configure backup for an App Service

## What
Configure scheduled or on-demand App Service backups to supported storage. Backup content and restore scope depend on platform features, configuration, plan tier, storage destination, and app settings.

## Why
Backups provide recovery from accidental changes, deployment errors, and corruption, but do not automatically satisfy every data-protection requirement. Define RPO/RTO, retention, restore testing, encryption/access, and protection of external databases and storage separately.

## How
Confirm the plan and app support the required backup capability. Choose a secure storage account/container, frequency, retention, and inclusion of app content/database components as supported. Limit access to backup storage and plan for its region/redundancy and lifecycle costs. Run a backup, inspect status and content, then restore to a staging app/slot or separate app and validate functionality before relying on it.

## Features
App Service backup can capture supported app configuration/content and selected databases; limitations apply to size, database types, and tiers. Restore can overwrite or create a separate target depending on workflow. Slots and app settings have their own behavior. Source control and deployment artifacts improve code recovery but are not substitutes for data backup.

## Code snippets (if any)
No snippet required: backup schedule and included resources vary with app OS, plan, and data source. Configure through the portal or supported CLI/API after confirming feature eligibility.

## Do's and Don'ts
**Do** test restores, secure destination storage, and monitor failed backups. **Don't** infer a backup is usable solely from a successful job status or assume it includes external dependencies and all secrets.

## Real-life implementation
A service stores app backups in a restricted, appropriately redundant storage account with alerts for failures and retention aligned to policy. Quarterly restore drills target an isolated staging app, and the database uses its own native backup/recovery design.

## Q&A
1. **Does App Service backup automatically protect an external database?** Only supported/configured databases are included; plan database protection independently.
2. **What proves recovery readiness?** A tested restore with application validation against the defined RTO/RPO.
3. **Can the backup account be broadly accessible?** No; enforce least privilege and secure networking/identity on backup data.

**References:** [Back up and restore an App Service app](https://learn.microsoft.com/azure/app-service/manage-backup) · [App Service backup configuration](https://learn.microsoft.com/azure/app-service/manage-backup)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#create-and-configure-azure-app-service)
