# Configure identity-based access for Azure Files

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Configure identity-based access for Azure Files](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [Azure Files identity-based authentication](https://learn.microsoft.com/azure/storage/files/storage-files-active-directory-overview)

## What

Azure Files identity-based SMB authentication lets users access SMB shares with identities rather than a shared storage account key. Supported identity sources include AD DS, Microsoft Entra Domain Services, and Microsoft Entra Kerberos in supported configurations.

## Why

Choose identity-based access for per-user authorization, familiar SMB access, and centralized identity governance. Authentication, share authorization, file ACLs, and network reachability are separate prerequisites. Identity-based SMB is not equivalent to Blob data roles or to using an account key to mount a share.

## How

Enable the selected identity source on the account and complete directory integration prerequisites. Assign an Azure Files share-level role (for example, Storage File Data SMB Share Contributor) at the appropriate scope. Set NTFS ACLs from a suitably privileged client, then test with representative users. Validate domain join, Kerberos, DNS/time, client support, and SMB network reachability (commonly TCP 445).

## Features

- Effective SMB access requires both share-level Azure RBAC and NTFS ACL permission.
- Identity-source configuration and client requirements differ; select a supported model for the environment.
- SMB identity access is distinct from Blob OAuth and REST access paths.
- Exam trap: an assigned share role does not override restrictive NTFS ACLs; account keys bypass per-user identity controls.

## Code snippets (if any)

```powershell
# Placeholders: account/resource group; use identity-source-specific Learn setup steps.
Connect-AzAccount
Get-AzStorageAccount -ResourceGroupName <resource-group> -Name <account>
```

Identity-source enablement is environment-specific; use Microsoft Learn's current procedure rather than copying domain settings.

## Do's and Don'ts

Do configure least-privilege share RBAC and ACLs, test actual user mounts, and troubleshoot identity/network before permissions. Don't distribute account keys for routine user access or expect a Blob role to authorize SMB.

## Real-life implementation

Finance users map an SMB share. The architect enables the organization's supported identity model, grants the finance group share-level access, then applies NTFS ACLs to departmental folders. A test user verifies both successful access to authorized files and denial elsewhere.

## Q&A

1. What two authorization layers apply to SMB Azure Files? **Share-level Azure RBAC and NTFS ACLs.**
2. Why can the share role succeed while file access fails? **ACL, Kerberos, DNS, client identity, or network prerequisites may still block access.**
3. Is a Blob Storage data role the same as SMB share access? **No; the authorization paths differ.**
