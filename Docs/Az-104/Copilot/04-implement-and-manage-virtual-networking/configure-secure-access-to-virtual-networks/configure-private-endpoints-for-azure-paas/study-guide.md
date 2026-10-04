# Configure private endpoints for Azure PaaS

## What

A private endpoint is a network interface with a private IP in a VNet subnet that connects privately to a specific Azure PaaS resource through Azure Private Link. A private DNS zone or equivalent DNS configuration maps the service FQDN to that private IP for clients on intended networks.

## Why

Private endpoints support private access and help remove dependency on public service endpoints. They are resource-specific, not a general route into a service. DNS, access authorization, and service public-network settings must be designed together; a private IP alone does not guarantee that clients select it or are authorized.

## How

Create the endpoint in a subnet with capacity, select the correct resource and subresource/group ID, and approve the connection if approval is required. Configure private DNS zone integration and link the zone to each client VNet that needs resolution; hybrid clients may require conditional forwarding. Validate from a client: resolve the normal service FQDN to the endpoint's private IP and connect using the expected hostname/TLS name. Confirm service firewall and identity authorization.

Review private endpoint network policies, NSGs, and routes according to current platform behavior and workload needs. Avoid duplicate/conflicting DNS records. For resiliency, consider endpoint placement, zone/region architecture, and recovery of DNS links and endpoint approvals. Monitor connection state and stale endpoints during decommission.

## Features

- Private IP from a VNet subnet; Private Link reaches the selected PaaS resource.
- Service-specific subresource/group ID and connection approval workflow.
- Private DNS zones provide private resolution for service FQDNs.
- Public access can be separately restricted or disabled based on service support.

## Code snippets (if any)

```bash
az network private-endpoint create --resource-group <rg> --name <endpoint-name> --vnet-name <vnet-name> --subnet <subnet-name> --private-connection-resource-id <paas-resource-id> --group-id <subresource> --connection-name <connection-name> --location <region>
```

Check the target service's supported subresource and use its recommended private DNS zone.

## Do's and Don'ts

- **Do** test DNS from every client network, including hybrid networks.
- **Do** verify approval state, correct subresource, and service-level authorization.
- **Don't** assume creating the endpoint automatically disables public access.
- **Don't** use the endpoint IP directly in application config when service DNS/TLS names are required.
- **Don't** link private zones broadly without understanding DNS visibility and record ownership.

## Real-life implementation

For a storage account, deploy the appropriate private endpoint, integrate its recommended private DNS zone, and link that zone to the application VNet. Configure on-premises DNS forwarding if hybrid clients require access. First validate FQDN resolution and connectivity from a test VM, then restrict public access after confirming all consumers use the private path. Track approvals and endpoint ownership as part of service lifecycle.

## Q&A

1. **What does a private endpoint add to the VNet?** A NIC with a private IP that represents a Private Link connection to a specific service resource.
2. **Does it automatically configure DNS?** Only when DNS integration/configuration is also performed; otherwise clients may still resolve a public address.
3. **Does private connectivity bypass authorization?** No; service identity and data-plane permissions still apply.
4. **How is it different from a service endpoint?** It uses a private IP and Private Link; service endpoints keep using the service's public endpoint with subnet-based firewall identity.

---
Source: [Microsoft Learn — What is a private endpoint?](https://learn.microsoft.com/azure/private-link/private-endpoint-overview) · [Microsoft Learn — Private endpoint DNS](https://learn.microsoft.com/azure/private-link/private-endpoint-dns) · [AZ-104 syllabus](../../../copilot-az104-syllabus.md)
