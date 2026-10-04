# Troubleshoot network connectivity

## What

Network connectivity troubleshooting is the systematic validation of the entire path between source and destination: name resolution, addressing, route selection, security policy, service reachability, and return traffic. Azure Network Watcher provides tools such as IP flow verify, connection troubleshoot, next hop, effective security rules, and packet capture.

## Why

A disciplined layered method shortens outages and avoids unsafe "open everything" changes. Many failures are not caused by the apparent endpoint: DNS can return the wrong address, a route can send traffic to an unhealthy appliance, or a guest firewall can reject a correctly delivered packet.

## How

1. Define source, destination, protocol/port, expected path, and a reproducible test.
2. Resolve DNS from the same network context as the client; compare the result with expected private/public records.
3. Check source and destination IPs, subnet membership, peering/gateway state, and effective route/next hop.
4. Evaluate NSGs on NIC and subnet, then firewall/NVA policy and state.
5. Confirm target service is listening, guest firewall permits it, and return routing is valid.
6. Use Network Watcher diagnostics and packet capture where supported; correlate timestamps with application and platform logs.

Change one layer at a time, record the prior state, and revert temporary diagnostics or rules. Distinguish control-plane provisioning state from data-plane behavior.

## Features

- Network Watcher includes connectivity diagnostics, IP flow verify, next hop, and packet capture.
- Connection Monitor evaluates reachability over time; it complements, not replaces, application-level health tests.
- Effective routes and effective NSG rules show the NIC's combined configuration.
- Network Watcher availability and supported operations are regional/resource dependent.

## Code snippets (if any)

```bash
az network watcher test-connectivity --source-resource <source-vm-resource-id> --dest-address <destination-fqdn-or-ip> --dest-port 443
az network watcher show-next-hop --resource-group <rg> --vm <vm-name> --source-ip <source-private-ip> --dest-ip <destination-ip>
```

## Do's and Don'ts

- **Do** test from the actual source subnet/VM and at the correct protocol and port.
- **Do** verify both forward and return paths and preserve diagnostic evidence.
- **Don't** respond by broadly allowing `Any` or disabling NSGs.
- **Don't** infer connectivity from successful ping alone; ICMP may be filtered while TCP works.
- **Don't** confuse DNS success, TCP establishment, and application health—they are separate layers.

## Real-life implementation

For a VM unable to reach a private PaaS endpoint, resolve the service FQDN from the VM, inspect the returned IP, validate private DNS zone links and endpoint connection state, then check effective routes and NSGs. Test the required TCP port with Network Watcher and validate the service's firewall policy. Capture only a bounded, approved diagnostic window and remove captures afterward.

## Q&A

1. **What is the best first step?** State the exact source, destination, protocol/port, and expected path; then reproduce from the source context.
2. **Does a successful DNS lookup prove the application is reachable?** No. It proves only that name resolution returned an answer.
3. **What does IP flow verify tell you?** Whether a specified flow is allowed or denied by NSG rules, not whether the application is listening.
4. **Why check return routing?** TCP is bidirectional; a missing or asymmetric response path still causes connection failure.

---
Source: [Microsoft Learn — Network Watcher](https://learn.microsoft.com/azure/network-watcher/network-watcher-overview) · [AZ-104 syllabus](../../../copilot-az104-syllabus.md)
