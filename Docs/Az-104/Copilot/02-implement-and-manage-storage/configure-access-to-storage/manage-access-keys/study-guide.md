# Manage access keys

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Manage access keys](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [Manage storage account access keys](https://learn.microsoft.com/azure/storage/common/storage-account-keys-manage)

## What

Storage account access keys are high-privilege shared secrets used by Shared Key authorization. Two keys are provided so clients can be moved to the alternate key before regenerating one. They are not Microsoft Entra identities, RBAC roles, or encryption keys.

## Why

Prefer Entra ID and managed identities for supported workloads: these avoid distributing long-lived secrets, support least privilege, and improve attribution. Keep Shared Key only for clients that require it. Key rotation is both security hygiene and an operational change; a blind rotation can interrupt every consumer still using the selected key.

## How

Inventory applications, tools, and SAS signed by each key. Store required keys in Key Vault, not source/config files. Rotate in stages: move consumers from key1 to key2 and test, regenerate key1, then migrate consumers back and rotate key2 in a later window. Restrict and monitor management-plane `listKeys`/regeneration operations. Disable Shared Key only after verifying compatibility.

## Features

- Regeneration immediately invalidates the selected key and dependent clients/SAS; the other key remains valid.
- Two-key overlap enables staged rotation.
- Retrieving keys is a sensitive management-plane operation.
- Exam trap: regenerating an account key is not the same as rotating a CMK used to encrypt data at rest.

## Code snippets (if any)

```bash
# Placeholder account. First confirm every key1 consumer has moved to key2.
az storage account keys renew -g <resource-group> -n <account> --key key1
```

## Do's and Don'ts

Do inventory dependencies, protect command output, use an overlap window, and migrate new workloads to identity auth. Don't rotate blindly, expose keys in scripts/logs, or grant broad access merely for convenience.

## Real-life implementation

A legacy appliance requires Shared Key. Operations stores key1 in Key Vault and stages its client onto key2 before regenerating key1. A test transaction and alert check verify the change. Newly deployed applications use managed identity and narrowly scoped Storage data roles instead.

## Q&A

1. Why are there two account keys? **To allow staged rotation.**
2. What can break when key1 is regenerated? **Consumers using key1 and SAS signed with key1.**
3. What do storage account keys do? **Authorize data access; they do not encrypt stored data.**
