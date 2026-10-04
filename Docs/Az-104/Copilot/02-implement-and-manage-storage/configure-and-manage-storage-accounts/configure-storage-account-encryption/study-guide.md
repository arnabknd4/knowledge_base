# Configure storage account encryption

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Configure storage account encryption](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [Azure Storage service encryption](https://learn.microsoft.com/azure/storage/common/storage-service-encryption)

## What

Azure Storage encrypts data at rest by default with service-side encryption. Microsoft-managed keys are the default. Customer-managed keys (CMK) in Key Vault or Managed HSM add customer control over key lifecycle. Infrastructure encryption adds a second encryption layer where supported.

## Why

Microsoft-managed keys minimize operations when provider-managed lifecycle meets policy. Choose CMK for regulatory control, separation of duties, or customer key lifecycle needs, accepting Key Vault permissions, availability, rotation, and monitoring responsibilities. At-rest encryption is distinct from HTTPS/TLS and client-side encryption.

## How

Review account encryption settings, choose key source, configure the Key Vault/Managed HSM key and account managed identity, and grant the required key permissions. Confirm rotation/version handling and recovery. Enable infrastructure encryption only when required and supported. Alert on key access failures and expiry; ensure key availability before disabling or deleting it.

## Features

- Service-side encryption is on by default; TLS protects data in transit.
- CMK depends on Key Vault/Managed HSM availability and correct identity permissions; loss of key access can interrupt data operations.
- Infrastructure encryption adds another layer but does not itself imply CMK.
- Exam trap: account access keys authorize Storage data access; encryption keys protect data at rest.

## Code snippets (if any)

```bash
# Placeholder account; inspect key source and enabled services without exposing key material.
az storage account show -g <resource-group> -n <account> \
  --query "encryption.{keySource:keySource,services:services}" -o json
```

Configure CMK through an approved portal or deployment workflow; never print/embed key material.

## Do's and Don'ts

Do document key owners, identity permissions, rotation, monitoring, and recovery. Don't disable a CMK before checking dependent accounts or assume encryption prevents authorized reads.

## Real-life implementation

A regulated archive requires customer-managed rotation. A dedicated Key Vault key and storage managed identity separate key administration from data administration. Operations alerts before expiry and tests key-access recovery. Other workloads remain on Microsoft-managed keys where CMK adds no business value.

## Q&A

1. What protects data at rest by default? **Service-side encryption with Microsoft-managed keys by default.**
2. What operational dependency does CMK add? **Key Vault/Managed HSM availability, permissions, and lifecycle.**
3. Does CMK replace HTTPS? **No, at-rest and in-transit protections are separate.**
