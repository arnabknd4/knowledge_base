# Configure blob lifecycle management

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Configure blob lifecycle management](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [Lifecycle management overview](https://learn.microsoft.com/azure/storage/blobs/lifecycle-management-overview)

## What

Blob lifecycle policies apply asynchronous, rule-based tiering or deletion based on blob age, modification/access time, prefix, blob type, and version/snapshot state. Policies automate retention and cost optimization at account scope.

## Why

Automate predictable transitions at scale, but align rules with legal retention, recovery, and access requirements. Tiering is economical only when retrieval and early-deletion costs are acceptable. Policy evaluation is periodic and asynchronous; do not build an exact-time scheduler assumption into the application.

## How

Create account-level rules with narrow container/prefix and blob-type filters. Define age conditions and actions for base blobs and, when needed, previous versions and snapshots. Pilot against a test prefix, inspect outcomes, and expand under change control. Enable access-time tracking before relying on last-access conditions.

## Features

- Supported actions include tier changes and deletion for eligible blobs and versions/snapshots.
- Last-access conditions require access-time tracking to be enabled.
- Tier moves can incur minimum-duration and retrieval charges; Archive requires rehydration.
- Exam trap: a base-blob deletion rule does not necessarily clean versions/snapshots; actions are asynchronous and not executed at an exact threshold instant.

## Code snippets (if any)

```json
{
  "rules": [{
    "enabled": true, "name": "archive-old-logs", "type": "Lifecycle",
    "definition": {
      "filters": {"blobTypes": ["blockBlob"], "prefixMatch": ["logs/"]},
      "actions": {"baseBlob": {
        "tierToCool": {"daysAfterModificationGreaterThan": 30},
        "delete": {"daysAfterModificationGreaterThan": 365}
      }}
    }
  }]
}
```

Illustrative fragment only: replace filters/retention with approved values and validate full API schema before deployment.

## Do's and Don'ts

Do pilot narrow rules, version-control policy, verify interaction with versioning/soft delete/immutability, and model retention and retrieval cost. Don't apply a broad delete rule without review or expect exact-time execution.

## Real-life implementation

Telemetry logs move to cool after 30 days and are deleted after an approved retention period. The team tests on a dedicated prefix, separately handles old versions/snapshots, and excludes active dashboard data from archive transitions. Monitoring checks both retention compliance and costs.

## Q&A

1. Is lifecycle evaluation immediate at the age threshold? **No; it is asynchronous.**
2. What must be enabled for last-access filters? **Access-time tracking.**
3. Does a base blob delete rule remove all previous versions? **No; configure version/snapshot actions as required.**
