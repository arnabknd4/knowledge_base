# Troubleshoot load balancing

## What

Load-balancer troubleshooting verifies the complete flow through DNS/client, frontend, rule, backend pool, health probe, NSGs/routes, guest firewall, and application listener. For Azure Load Balancer, focus on Layer 4 behavior; Layer 7 symptoms may belong to the application or an HTTP-aware gateway.

## Why

A frontend can be allocated and a rule configured while all backends remain unhealthy or return traffic is misrouted. The probe is a key control-plane signal, but probe health and user-perceived application health are not identical.

## How

Confirm the client resolves and reaches the correct frontend IP and port. Check the frontend configuration, rule protocol/ports, backend membership and NIC association, probe protocol/port/path, and backend health. Verify NSGs permit client traffic and probe traffic, route tables preserve a valid return path, and guest firewall/service listen on the expected interface and port. Validate inbound NAT rules separately from load-balancing rules. Check outbound SNAT/outbound rules if only egress or return traffic fails.

Use Network Watcher, backend health metrics, packet capture, and application logs to isolate the layer. Test from inside and outside the VNet as appropriate. Change one item at a time; preserve healthy backend capacity and avoid disabling probes as a production workaround. Confirm zone placement, capacity, and failure-domain assumptions after the immediate fault is fixed.

## Features

- Backend health status reflects probe outcomes.
- NSGs must allow probe and application flows.
- Public and internal frontends have different reachability paths.
- Load-balancing rules, inbound NAT rules, and outbound rules address distinct traffic patterns.

## Code snippets (if any)

```bash
az network lb show --resource-group <rg> --name <lb-name> --query "{state:provisioningState,frontend:frontendIpConfigurations[].name,rules:loadBalancingRules[].name,probes:probes[].name}"
az network watcher test-connectivity --source-resource <client-vm-resource-id> --dest-address <frontend-ip-or-dns> --dest-port <port>
```

## Do's and Don'ts

- **Do** inspect backend health and probe requirements before changing rules.
- **Do** validate traffic from the correct network location and test the application response.
- **Don't** assume an allocated frontend means backends are reachable.
- **Don't** disable probes to make an unhealthy backend appear usable.
- **Don't** conflate inbound distribution with outbound SNAT or inbound NAT.

## Real-life implementation

Users report intermittent failures to a public frontend. Compare backend health with probe logs, then check if only one zone or pool member is unhealthy. Validate that probes are permitted by backend NSGs and that the application returns the expected probe response. Test the frontend from an external client, inspect route and return flow on the affected VM, and remove or repair the faulty backend without taking down healthy capacity.

## Q&A

1. **If all backends are down, what should be checked first?** Probe protocol/port/path, backend listener, NSG probe allowance, and backend health state.
2. **Does a successful probe guarantee users can complete a request?** No; it may not exercise DNS, authentication, or full application logic.
3. **What is the difference between inbound NAT and load balancing?** NAT maps an individual frontend port to a backend; load balancing distributes matching flows across a pool.
4. **If inbound works but egress fails, where do you look?** Outbound rules/SNAT design, routes, NSGs, and firewall egress policy.

---
Source: [Microsoft Learn — Azure Load Balancer troubleshooting](https://learn.microsoft.com/azure/load-balancer/load-balancer-troubleshoot) · [AZ-104 syllabus](../../../copilot-az104-syllabus.md)
