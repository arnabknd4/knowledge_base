# Create and configure virtual network peering

## What

VNet peering connects two Azure VNets over Microsoft's backbone with private IP routing. Regional peering connects VNets in the same region; global peering connects VNets in different regions. Each side has a peering object, and both must be configured successfully for connectivity.

## Why

Peering is useful for hub-and-spoke, shared services, and regional application topologies without gateways in the data path. It provides low-latency private routing, but it is not transitive routing, segmentation, or a security control. Plan routing and security independently.

## How

Check address-space non-overlap and permitted connectivity first. Create reciprocal peerings and choose `allowVirtualNetworkAccess` based on the design. Gateway transit uses explicit settings: the hub can allow gateway transit, while spokes use remote gateways; a VNet using a remote gateway cannot also host its own gateway for that peering relationship. Forwarded traffic and gateway transit are distinct options—enable only when needed. Validate both peering states, effective routes, NSGs, DNS, and the return path. Peering does not automatically propagate routes among spokes, and a spoke cannot reach another spoke through a hub merely because both are peered to it.

Operationally, review peering state after address-space changes, maintain topology documentation, and account for egress/peering data-transfer charges. Global peering is not itself cross-region failover; applications still need a resilient service design.

## Features

- Private backbone transport; same-region and global variants.
- Separate directional configuration on each VNet.
- Options for VNet access, forwarded traffic, gateway transit, and remote gateways.
- Supports hub-and-spoke, subject to explicit routing and security configuration.
- Non-transitive; no automatic route propagation between peered VNets.

## Code snippets (if any)

```bash
az network vnet peering create --resource-group <rg-a> --name a-to-b --vnet-name <vnet-a> --remote-vnet <vnet-b-resource-id> --allow-vnet-access
az network vnet peering create --resource-group <rg-b> --name b-to-a --vnet-name <vnet-b> --remote-vnet <vnet-a-resource-id> --allow-vnet-access
az network vnet peering show --resource-group <rg-a> --vnet-name <vnet-a> --name a-to-b --query peeringState
```

Replace resource IDs with actual VNet resource IDs; create and validate both directions.

## Do's and Don'ts

- **Do** verify CIDR non-overlap and both peering states.
- **Do** configure gateway transit and forwarded traffic only to satisfy a defined path.
- **Don't** expect hub-and-spoke peering to provide spoke-to-spoke transit.
- **Don't** treat peering as an NSG or firewall; enforce least privilege separately.
- **Don't** assume peering alone configures DNS resolution across VNets.

## Real-life implementation

In a hub-and-spoke estate, peer each workload spoke to a centrally governed hub. For inspection, route spoke traffic through a firewall/NVA with appropriate UDRs and forwarding settings; peering alone will not force that path. Use a deliberate DNS design for shared services and private zones. Test representative flows in both directions and inspect effective routes and NSG rules before moving production traffic.

## Q&A

1. **Is VNet peering transitive?** No. A peered VNet does not relay traffic to another peered VNet by default.
2. **Must both sides be configured?** Yes, establish reciprocal peering objects and verify their states.
3. **Can peered VNets have overlapping ranges?** No.
4. **Does peering encrypt traffic or replace network security controls?** It provides private backbone connectivity, not a substitute for application encryption, NSGs, or firewalls.

---
Source: [Microsoft Learn — Virtual network peering](https://learn.microsoft.com/azure/virtual-network/virtual-network-peering-overview) · [AZ-104 syllabus](../../../copilot-az104-syllabus.md)
