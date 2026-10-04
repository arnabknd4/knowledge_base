# Configure user-defined routes

## What

User-defined routes (UDRs) are custom entries in a route table associated with a subnet. Each route specifies an address prefix and next-hop type, such as Virtual appliance, Virtual network gateway, VNet, Internet, or None. Azure combines system routes, BGP routes, and UDRs to determine effective routing.

## Why

UDRs direct traffic through inspection appliances, control egress, or steer traffic to gateways. Routing is a packet-path control, not a security policy: a route can direct a flow but does not itself allow or deny it. A bad or overly broad route can blackhole traffic or create asymmetric paths.

## How

Model source, destination, next hop, and return path before creating routes. For a firewall/NVA, ensure the target appliance is reachable, configured to forward packets, and has a valid return path; enable IP forwarding where required. Associate the route table to the correct subnet. Longest-prefix matching applies among routes; a UDR can override a system route when applicable. A `0.0.0.0/0` route has broad impact and should be rolled out with staged validation. Do not confuse BGP route propagation settings with a route that directly sets a next hop.

Inspect effective routes on a NIC when diagnosing. Validate both directions, NSGs, appliance health, and any peering or gateway settings. Maintain a rollback route/table and monitor for unexpected route changes.

## Features

- Route tables can be associated with multiple subnets; a subnet has one route-table association.
- Next-hop types include Virtual appliance, Virtual network gateway, VNet, Internet, and None.
- System routes and learned routes also contribute to effective routing.
- Route propagation can be controlled on route tables for gateway-learned routes.

## Code snippets (if any)

```bash
az network route-table create --resource-group <rg> --name <route-table> --location <region>
az network route-table route create --resource-group <rg> --route-table-name <route-table> --name default-to-firewall --address-prefix 0.0.0.0/0 --next-hop-type VirtualAppliance --next-hop-ip-address <firewall-private-ip>
az network vnet subnet update --resource-group <rg> --vnet-name <vnet> --name <subnet> --route-table <route-table>
```

## Do's and Don'ts

- **Do** trace the forward and return routes before enforcing inspection.
- **Do** validate next-hop health, forwarding, and route propagation.
- **Don't** use `None` or a broad default route without understanding its blackhole effect.
- **Don't** assume a UDR overrides every platform-specific route or service behavior.
- **Don't** rely on routes to replace NSGs or firewall policy.

## Real-life implementation

To inspect spoke internet egress, associate a route table with the workload subnet and send the default route to the firewall's private IP. Ensure firewall policy allows required destinations and the firewall has a working internet path. Test DNS, application egress, and return traffic in a pilot subnet, inspect effective routes, then expand by deployment automation. Keep a documented exception path for platform services with special network requirements.

## Q&A

1. **What determines the selected route?** Azure evaluates effective routes, with longest-prefix matching and route-source precedence rules.
2. **Does a UDR to a firewall configure the firewall?** No. Appliance forwarding, policy, and return routing must also be configured.
3. **What does next hop `None` do?** It drops traffic matching the route.
4. **Why can traffic reach a destination but the response fail?** Asymmetric or missing return routes, NSGs, or appliance stateful policy can block the response.

---
Source: [Microsoft Learn — Virtual network traffic routing](https://learn.microsoft.com/azure/virtual-network/virtual-networks-udr-overview) · [AZ-104 syllabus](../../../copilot-az104-syllabus.md)
