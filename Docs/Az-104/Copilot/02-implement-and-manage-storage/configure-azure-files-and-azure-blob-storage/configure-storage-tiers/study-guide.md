# Configure storage tiers

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Configure storage tiers](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [Blob access tiers](https://learn.microsoft.com/azure/storage/blobs/access-tiers-overview)

## What

Blob access tiers balance storage price against access and retrieval costs. Hot suits frequent use; cool and cold suit infrequent access with minimum residency considerations. Archive is offline and must be rehydrated before reads. Supported tiers depend on account and blob type.

## Why

Use observed access patterns and retention duration. Cool/cold/archive reduce capacity cost but may add retrieval, transaction, and early-deletion charges. Archive adds restore latency, potentially hours. Include the restore time objective, redundancy, and lifecycle operations in the cost decision. Azure Files does not use Blob tiers.

## How

Set an account default tier where suitable, then choose per-blob tiers or lifecycle rules. Estimate retrieval and early-deletion penalties before transition. Rehydrate archived blobs to an online tier using a recovery priority aligned with RTO, and wait for completion before serving reads. Monitor tier distribution and costs.

## Features

- Hot, cool, and cold are online; Archive is offline.
- Minimum storage-duration/early deletion charges may apply to cool, cold, and archive tiers.
- Last-access lifecycle rules require access-time tracking.
- Exam trap: the cheapest capacity tier may cost more overall for frequent reads; tiering is not redundancy, backup, or encryption.

## Code snippets (if any)

```bash
# Placeholder blob; choose tier after measuring reads and reviewing current pricing.
az storage blob set-tier --account-name <account> --container-name <container> \
  --name <blob> --tier Cool --auth-mode login
```

## Do's and Don'ts

Do model access frequency, retention, retrieval time, and minimum-duration costs. Don't place active application data in Archive or assume tier transitions are free.

## Real-life implementation

Monthly compliance exports stay cool while auditors may need quick access. After an operational window, lifecycle policy moves eligible objects to Archive. Compliance approves longer rehydration time and operations document restore priority and cost. Active dashboards are excluded from Archive to avoid delays.

## Q&A

1. Can an archived blob be read immediately? **No; rehydrate it to an online tier first.**
2. Why may moving to cool raise cost? **Retrieval, transaction, or early-deletion charges.**
3. Do Blob tiers apply to Azure Files shares? **No.**
