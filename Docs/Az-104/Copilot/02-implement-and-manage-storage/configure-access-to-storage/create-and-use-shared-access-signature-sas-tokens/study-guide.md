# Create and use shared access signature (SAS) tokens

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Create and use shared access signature (SAS) tokens](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [SAS overview](https://learn.microsoft.com/azure/storage/common/storage-sas-overview)

## What

A shared access signature delegates a bounded set of Storage operations using a signed URI. Its scope can limit the resource, permissions, start/expiry time, IP range, and protocol. Treat it as a bearer secret: anyone holding it may exercise its capability.

## Why

SAS supports time-limited client access without disclosing an account key or provisioning a user identity for each client. Prefer Entra authorization and user delegation SAS for Blob Storage when supported. Limit each token to the minimum resource and permissions, keep its lifetime short, require HTTPS, and plan revocation before distribution.

## How

Create SAS in the portal, Storage Explorer, CLI, PowerShell, or SDK. Set only required permissions, a short expiry, HTTPS-only, and suitable IP restrictions. User delegation SAS is created after obtaining a user delegation key through Entra authorization. Protect the returned URI: redact it from logs, shell history, source code, support tickets, and telemetry.

## Features

- User delegation SAS is Entra-backed and Blob-only; service SAS targets a service resource; account SAS can cover supported operations across services.
- SAS is not an identity and does not bypass account networking rules.
- A signed SAS is not necessarily individually revocable. Stored access policies apply only to eligible service SAS; rotating its account key has broader impact.
- Exam trap: account-key-signed SAS inherits the risk of the signing key; a long expiry increases exposure.

## Code snippets (if any)

```bash
# Placeholder <container>; protects the returned SAS as a secret.
az storage container generate-sas --account-name <account> --name <container> \
  --permissions rl --expiry "<UTC-expiry>" --https-only --auth-mode login --as-user -o tsv
```

`<UTC-expiry>` is a near-future ISO 8601 UTC time. `--as-user` requests a user delegation SAS; never commit the returned output.

## Do's and Don'ts

Do use HTTPS, least privilege, short validity, protected delivery, and Entra user delegation when suitable. Don't embed SAS in code or logs, grant write/delete unnecessarily, or assume firewall access is granted by SAS possession.

## Real-life implementation

A vendor uploads a single export. The service issues a short-lived HTTPS-only SAS scoped to that blob and only the necessary write operation. The application separately records the vendor's business identity, since Storage authorization via a bearer token does not identify the person who received it.

## Q&A

1. Which SAS is generally preferred for Entra-delegated Blob access? **User delegation SAS.**
2. Can any SAS be individually revoked immediately? **No; use policy-linked service SAS, short expiry, or rotate a signing key with broader impact.**
3. What does `rl` grant? **Read and list, not write or delete.**
