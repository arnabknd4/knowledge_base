# Create and configure storage accounts

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Create and configure storage accounts](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [Create a storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create)

## What

A storage account is the namespace, endpoint, networking, security, performance, replication, and billing boundary for Azure Storage services. Account choices influence supported features, access tiers, endpoint names, and data-movement options.

## Why

Design the account around protocol, workload performance, region, resiliency, security, and growth. General-purpose v2 is the common choice for modern workloads; specialized premium or block-blob accounts suit targeted performance patterns and may constrain features. Names are globally unique and immutable, so endpoint dependencies and boundaries deserve early design.

## How

Create in the intended subscription, resource group, and region. Select account kind/SKU, redundancy, secure transfer, minimum TLS, public access posture, hierarchical namespace if Data Lake Gen2 is required, network rules, and key management. Verify regional availability and feature compatibility before deployment. Configure diagnostics, data protection, and network connectivity before loading production data.

## Features

- GPv2 supports a broad mix of Blob, Files, Queue, and Table workloads; supported services vary by account type.
- HNS enables Data Lake Gen2 directory/ACL semantics but has feature compatibility considerations.
- Performance, redundancy, and access tier are separate decisions.
- Exam trap: premium is not a synonym for geo-redundant; account endpoints and boundaries are durable.

## Code snippets (if any)

```bash
# Placeholder account name must be globally unique; verify SKU availability in <region>.
az storage account create -g <resource-group> -n <account> -l <region> \
  --kind StorageV2 --sku Standard_LRS --https-only true --min-tls-version TLS1_2
```

## Do's and Don'ts

Do model transactions, capacity, residency, recovery objectives, protocol, and compatibility. Use separate accounts when isolation or distinct policy/billing boundaries matter. Don't enable public blob access by default or assume the account can be renamed later.

## Real-life implementation

An analytics workload needs hierarchical paths and ACLs, while a separate application serves ordinary blobs. The architect uses an HNS-enabled GPv2 account for analytics and isolates application data in another account. This separates network, identity, lifecycle, and billing decisions while making feature compatibility explicit.

## Q&A

1. What is the common account choice for general modern workloads? **GPv2, after checking feature and performance needs.**
2. Is redundancy a performance tier? **No, it is a separate resiliency selection.**
3. Why choose names and boundaries early? **Names are immutable and accounts establish long-lived endpoints/policy scope.**
