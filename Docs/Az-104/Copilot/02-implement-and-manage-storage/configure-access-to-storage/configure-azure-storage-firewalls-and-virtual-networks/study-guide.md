# Configure Azure Storage firewalls and virtual networks

**AZ-104 Domain 2 — Implement and manage storage**
**Official skill bullet:** [Configure Azure Storage firewalls and virtual networks](../../../copilot-az104-syllabus.md)
**Microsoft Learn:** [Storage network security](https://learn.microsoft.com/azure/storage/common/storage-network-security)

## What

Storage networking controls which networks can reach a storage account; it is independent of data authorization. The account firewall can allow all networks or limit access to selected public IPs and virtual networks. Private endpoints provide a private IP through Private Link; service endpoints keep the Storage public endpoint but identify eligible subnets.

## Why

Restricting network reachability reduces exposure, but does not prove who a caller is or what data they may access. Combine network policy with Microsoft Entra ID, least-privilege data roles, and TLS. Choose service endpoints for simpler subnet-scoped connectivity to a public service endpoint; choose private endpoints when a private address and private connectivity are required. Private Link adds DNS, routing, approval, and operations dependencies.

## How

In the portal, use **Storage account > Networking** to select networks, configure IP/VNet rules, trusted-service exceptions, and public network access. For service endpoints, enable the Storage endpoint on the subnet and add the subnet rule. For private endpoints, approve the connection, configure private DNS zone links, and verify client name resolution before disabling public access. CLI/PowerShell can create rules and endpoints; always test from each actual client network.

## Features

- Default action must be changed to `Deny` for selected-network-only access.
- IP rules are for public IPv4 egress addresses, not a client's private IP.
- “Allow trusted Microsoft services” is limited to eligible services, not a blanket bypass.
- Exam trap: neither an RBAC assignment nor a SAS bypasses the firewall; network reachability and authorization must both succeed.

## Code snippets (if any)

```bash
# Placeholders: <resource-group>, <account>, <client-public-ip>.
az storage account update -g <resource-group> -n <account> --default-action Deny
az storage account network-rule add -g <resource-group> --account-name <account> --ip-address <client-public-ip>
```

## Do's and Don'ts

Do test DNS, routing, and access from representative clients; preserve a controlled admin path; and document rule owners. Don't broadly allow IP ranges, disable public access before validating private DNS, or confuse CORS with network authorization.

## Real-life implementation

An application subnet accesses a storage account through a private endpoint. The architect links the correct private DNS zone to the VNet and validates storage FQDN resolution from the app. Public access is disabled only after testing. Separately, the app's managed identity receives the required data role: the private route itself grants no data permission.

## Q&A

1. Does an allowed subnet rule grant blob read permission? **No; it only admits network traffic.**
2. Service endpoint vs private endpoint? **Subnet-scoped access to a public endpoint vs a private IP/Private Link path.**
3. Why might a private endpoint fail despite being approved? **DNS, routing, or client resolution may be incorrect.**
