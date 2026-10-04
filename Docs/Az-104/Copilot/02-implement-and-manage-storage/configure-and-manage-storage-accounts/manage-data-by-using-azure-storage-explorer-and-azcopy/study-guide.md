# Manage data by using Azure Storage Explorer and AzCopy

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Manage data by using Azure Storage Explorer and AzCopy](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [Transfer data with AzCopy](https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10)

## What

Storage Explorer is a cross-platform GUI for interactively browsing and managing Storage. AzCopy is a command-line utility for high-performance copy/sync between local systems and supported Azure endpoints. Both can use Entra authentication or delegated credentials, subject to scope and network access.

## Why

Use Explorer for operator inspection and one-off tasks; use AzCopy for repeatable, large-volume transfers. Entra ID avoids embedded secrets but requires the correct data-plane role and reachable endpoint. Plan bandwidth, concurrency, egress/transaction cost, integrity checks, resumability, and secure handling of job logs.

## How

Sign in as the intended Entra principal and verify data-plane access and firewall reachability. Use `copy` for explicit transfer; use `sync` only after reviewing deletion semantics. Pilot a batch, check filters and destination, verify results, and protect AzCopy job plans/logs. Storage Explorer can inspect blob properties, metadata, snapshots, and access controls.

## Features

- Management-plane roles such as Owner do not inherently grant blob data access.
- AzCopy supports resumable jobs; logs/plans can contain operational details and must be protected.
- Cross-region or cross-cloud data transfer can incur egress and transaction charges.
- Exam trap: `sync` may delete destination objects to match source; SAS and Entra auth do not bypass firewalls.

## Code snippets (if any)

```bash
# Placeholders: local folder, account, and destination container. Authenticate with Entra.
azcopy login
azcopy copy "<local-folder>/*" "https://<account>.blob.core.windows.net/<container>" --recursive=true
```

If SAS is required, protect the destination URL and avoid shared shell history.

## Do's and Don'ts

Do pilot large transfers, verify results, use least privilege, and secure job logs. Don't run destructive sync without review, paste SAS into scripts, or assume copied data has the right tier, ACLs, and metadata.

## Real-life implementation

For a datacenter exit, the team grants an Entra identity access only to the destination container, pilots representative files, then transfers in resumable batches. They measure throughput and costs and use Storage Explorer for spot checks, not the bulk migration pipeline. A reviewed final delta sync completes the cutover.

## Q&A

1. Which tool suits repeatable high-volume transfer? **AzCopy.**
2. Why can Owner still fail to list blobs? **Management-plane permission is not necessarily data-plane authorization.**
3. What is the `sync` caution? **It can delete destination data to match the source.**
