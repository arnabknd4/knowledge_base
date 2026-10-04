# Create and configure virtual networks and subnets

## What

An Azure virtual network (VNet) is a private, regional IP network boundary. Subnets divide its address space into deployment and policy segments. VNet address spaces must be valid, non-overlapping CIDR ranges; subnets consume portions of that space. Azure reserves five addresses in every IPv4 subnet, so account for these when sizing.

## Why

Treat the VNet and subnet plan as an architecture contract. Good segmentation limits blast radius, enables subnet-scoped NSGs and routes, and reserves room for growth, peering, VPN/ExpressRoute, and private endpoints. Changing address plans after deployment is possible but disruptive; overlapping ranges prevent straightforward routing and peering.

## How

Start with connected-network inventory, growth estimates, and IPAM. Allocate a non-overlapping VNet CIDR, then use distinct subnets for workload tiers and Azure services with subnet-specific requirements. Do not make subnets unnecessarily small: some Azure services require minimum sizes or dedicated subnets, and private endpoint policies may affect a subnet's use. Associate NSGs and route tables deliberately and document ownership. VNet peering does not merge address spaces or make them transitive.

For packet-path analysis, verify the NIC's subnet and private IP, subnet and NIC NSG associations, effective routes, and destination resolution before blaming the application. Confirm the target listener and return path as well as the outbound path.

## Features

- Regional VNet with one or more address spaces; subnets are within those ranges.
- VNet and subnet address prefixes can be expanded when free adjacent/non-overlapping space exists; plan carefully around connected networks.
- Delegated subnets reserve a subnet for a service; service-specific sizing and policy constraints apply.
- NSGs, UDRs, service endpoints, and private endpoints can be applied at subnet scope as appropriate.
- Availability is regional; use zone-aware workload design separately from address planning.

## Code snippets (if any)

```bash
az network vnet create --resource-group <resource-group> --name <vnet-name> --location <region> --address-prefixes 10.20.0.0/16 --subnet-name app --subnet-prefixes 10.20.1.0/24
az network vnet subnet create --resource-group <resource-group> --vnet-name <vnet-name> --name data --address-prefixes 10.20.2.0/24
```

Use private, non-overlapping example ranges only after checking enterprise IPAM.

## Do's and Don'ts

- **Do** reserve capacity for future subnets and Azure platform requirements.
- **Do** use subnet boundaries that reflect trust tiers and routing requirements.
- **Don't** assume a VNet is a firewall or that subnet separation alone enforces security.
- **Don't** use overlapping ranges across peered, VPN-connected, or on-premises networks.
- **Don't** put unrelated workloads together merely to conserve address space.

## Real-life implementation

For a three-tier application, allocate a VNet sized for future instances and separate web, application, and data tiers into subnets. Apply least-privilege NSGs and route inspection at each boundary; use private connectivity to PaaS where required. Keep a reviewed IPAM record that includes peered VNets, hub networks, and on-premises prefixes. Before rollout, validate address capacity, platform subnet requirements, and deployment templates in a non-production subscription.

## Q&A

1. **Can two peered VNets use the same CIDR?** No. Overlapping address spaces prevent peering because Azure cannot unambiguously route traffic.
2. **Does a subnet create a security boundary by itself?** No. Use NSGs, routes, and service-level controls to enforce intended flows.
3. **How many IPv4 addresses are usable in a subnet?** Azure reserves five addresses; subtract five from the subnet's total.
4. **Can a subnet be resized?** Often, if the new prefix is valid and does not overlap another subnet; assess dependencies and active resources first.

---
Source: [Microsoft Learn — Plan virtual networks](https://learn.microsoft.com/azure/virtual-network/virtual-network-vnet-plan-design-arm) · [AZ-104 syllabus](../../../copilot-az104-syllabus.md)
