# Configure public IP addresses

## What

An Azure public IP address is a public-facing resource that can be associated with supported services such as a VM NIC, load balancer frontend, or VPN gateway. Public IPs are IPv4 or IPv6, static or dynamic where supported, and use Basic or Standard SKU characteristics; Basic SKU public IPs have been retired, so new designs should use Standard.

## Why

Public addressing is an exposure decision, not merely an addressing convenience. Prefer private access through VPN, ExpressRoute, Bastion, or private endpoints when possible. When internet access is required, use a controlled frontend such as a load balancer or application gateway and narrowly scoped security policy.

## How

Choose SKU, IP version, region, zone behavior, and association based on the consuming resource. Standard public IPs are secure by default: inbound traffic needs an NSG rule permitting it. A VM public IP is directly reachable only if routing, NSG policy, and guest firewall/application listener allow it. Static assignment is appropriate when DNS or allowlists require a stable address. Dynamic allocation can change on deallocation for supported configurations; do not build dependencies on an address that is not reserved.

For troubleshooting, confirm the IP resource is allocated, attached to the intended frontend/NIC, and in a compatible region/SKU/zone configuration. Trace inbound traffic through DNS, public frontend, load-balancing rules if present, NSG, guest firewall, and listener; verify return routing.

## Features

- IPv4/IPv6 and static/dynamic allocation options vary by SKU and resource.
- Standard SKU supports zone-redundant or zonal configurations where available and has secure-by-default inbound behavior.
- Public IPs can be associated to supported NICs and service frontends.
- Public IP Prefix reserves a contiguous range for scenarios requiring multiple predictable addresses.

## Code snippets (if any)

```bash
az network public-ip create --resource-group <resource-group> --name <public-ip-name> --location <region> --sku Standard --allocation-method Static --version IPv4
az network public-ip show --resource-group <resource-group> --name <public-ip-name> --query "{ip:ipAddress,state:provisioningState,sku:sku.name}"
```

## Do's and Don'ts

- **Do** minimize direct VM exposure and prefer a hardened entry point.
- **Do** use Standard SKU and explicit NSG allow rules for modern deployments.
- **Don't** publish management ports broadly to the internet.
- **Don't** assume a public IP bypasses NSGs, guest firewalls, or application authentication.
- **Don't** hard-code an address that can change; reserve a static address when dependencies require it.

## Real-life implementation

Expose a web application through a resilient public frontend and backend pool rather than assigning each VM a public IP. Restrict backend access to the frontend and management access to Bastion or a controlled admin network. Use static IP/DNS records, monitor exposure inventory, and make cleanup of orphaned public IPs part of operations. Review zone choices and regional availability against the service's resiliency objectives.

## Q&A

1. **Does a Standard public IP accept inbound traffic automatically?** No. It is secure by default; required inbound flows need explicit NSG allowance.
2. **When should an IP be static?** When clients, DNS, or partner allowlists require a stable address.
3. **Does assigning a public IP guarantee reachability?** No. Association, routes, NSGs, host firewall, and a listening service must all permit the path.
4. **Should every VM have a public IP for administration?** No. Prefer private administration through Bastion or a private network.

---
Source: [Microsoft Learn — Public IP addresses](https://learn.microsoft.com/azure/virtual-network/ip-services/public-ip-addresses) · [AZ-104 syllabus](../../../copilot-az104-syllabus.md)
