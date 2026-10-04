# Configure an internal or public load balancer

## What

Azure Load Balancer is a Layer 4 TCP/UDP load balancer. A frontend IP receives traffic and a rule maps protocol/port to a backend pool and health probe. A public frontend accepts internet-originated flows; an internal frontend uses a private IP for VNet or connected-network clients.

## Why

Load balancing distributes connections across healthy instances and provides a stable service endpoint. It does not provide HTTP path routing, TLS termination, or application-layer inspection; choose Application Gateway or another Layer 7 service when those are requirements.

## How

Design frontend scope, backend pool, rule protocol/ports, probe path/port, and outbound connectivity deliberately. Standard Load Balancer is the recommended SKU for new designs, with secure-by-default behavior and zone-aware options where available. Ensure backend NSGs allow the probe and intended client flows. A healthy probe indicates a transport-level response to the probe, not necessarily full application correctness. HA Ports and floating IP are specialized patterns with additional configuration.

For internal load balancers, select a frontend IP from the subnet and avoid conflicts. For public load balancers, use a Standard static public IP. Outbound access is a separate design concern; do not assume inbound load-balancing rules automatically provide the required outbound SNAT behavior. Plan zone/region architecture and probe monitoring for availability.

## Features

- Layer 4 TCP/UDP distribution with frontend IP configurations and backend pools.
- Health probes remove unhealthy backends from new flow distribution.
- Public and internal frontends; Standard SKU supports modern security and availability capabilities.
- Outbound rules and NAT rules serve different traffic patterns from inbound load-balancing rules.

## Code snippets (if any)

```bash
az network lb create --resource-group <rg> --name <lb-name> --location <region> --sku Standard --frontend-ip-name frontend --backend-pool-name backend --public-ip-address <standard-public-ip-name>
```

For an internal load balancer, configure a frontend IP in the target subnet instead of a public IP.

## Do's and Don'ts

- **Do** align probe behavior with genuine backend readiness and allow probe traffic in NSGs.
- **Do** choose public versus internal frontend based on client trust boundary.
- **Don't** expect Load Balancer to route by URL, host header, or HTTP path.
- **Don't** equate probe health with end-to-end transaction health.
- **Don't** forget outbound connectivity and SNAT capacity design.

## Real-life implementation

Place stateless web VMs in a backend pool behind a Standard public Load Balancer for TCP 443. Use a static frontend IP, a probe that reflects listener readiness, and NSG rules limited to the required client/probe flows. Keep application TLS and authorization on the backend unless a Layer 7 gateway is required. For a private API tier, use an internal frontend and restrict consumers to approved subnets.

## Q&A

1. **Which load balancer is Layer 4?** Azure Load Balancer; Application Gateway provides Layer 7 capabilities.
2. **What does a probe do?** It determines backend health for load distribution; it is not a full business-transaction check.
3. **When is an internal load balancer used?** When clients should reach the service through a private IP.
4. **Does an inbound rule configure outbound internet access?** No; outbound connectivity must be designed separately.

---
Source: [Microsoft Learn — Azure Load Balancer overview](https://learn.microsoft.com/azure/load-balancer/load-balancer-overview) · [AZ-104 syllabus](../../../copilot-az104-syllabus.md)
