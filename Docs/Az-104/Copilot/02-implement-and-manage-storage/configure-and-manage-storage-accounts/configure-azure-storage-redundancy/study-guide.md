# Configure Azure Storage redundancy

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Configure Azure Storage redundancy](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [Storage redundancy](https://learn.microsoft.com/azure/storage/common/storage-redundancy)

## What

Redundancy controls how Storage copies data and which failures it can withstand. LRS keeps copies in one datacenter; ZRS distributes copies across availability zones in the primary region; GRS/GZRS add asynchronous replication to a secondary region. RA variants expose a secondary read endpoint.

## Why

Choose by required RPO/RTO and failure domain, not by the SKU name alone. LRS is lowest cost but weaker against facility failure; ZRS protects against zone loss but not regional disaster; geo-redundancy improves regional durability at additional cost and asynchronous data-loss risk. RA is useful for secondary reads, not for secondary writes.

## How

Select a supported redundancy option at account creation or use a supported conversion path after verifying eligibility. Check region/service support, account features, failover authority, endpoint behavior, and pricing. For geo-redundant accounts, document customer-managed failover and practice application recovery; failover changes which region accepts writes.

## Features

- LRS: multiple copies within one physical location.
- ZRS: synchronous replication across zones within the primary region.
- GRS asynchronously copies to a secondary; GZRS combines primary ZRS and geo-replication.
- Exam trap: geo replication is not synchronous; RA enables secondary reads, not writes or automatic failover.

## Code snippets (if any)

```bash
# Placeholder account; inspect its SKU before planning a conversion or failover.
az storage account show -g <resource-group> -n <account> --query "{sku:sku.name,kind:kind}" -o table
```

Use the documented conversion/failover workflow only after confirming current account eligibility.

## Do's and Don'ts

Do map the SKU to explicit failure scenarios, RPO/RTO, regional support, and recovery procedure. Don't call geo-replication a backup, promise zero-loss failover, or pay for RA when no secondary-read requirement exists.

## Real-life implementation

A service must continue operating through zone failure but can use a regional recovery plan for disaster. ZRS meets the zone requirement; GZRS is selected only if regional durability warrants added cost. The runbook states replication is asynchronous and defines who initiates failover and how clients use the new primary endpoint.

## Q&A

1. Which option gives synchronous zone copies in the primary region? **ZRS (also the primary side of GZRS).**
2. Does GRS promise zero write loss at regional failover? **No, secondary replication is asynchronous.**
3. What does RA provide? **Read access to the secondary, not secondary writes.**
