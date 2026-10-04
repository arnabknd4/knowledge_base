# Use Azure Network Watcher and Connection Monitor

## What

Azure Network Watcher provides network diagnostics and visualization for Azure networking, including IP flow verification, next hop, effective security rules, packet capture, topology, and connection troubleshooting. Connection Monitor continuously tests connectivity between supported Azure, hybrid, and on-premises endpoints using configured sources, destinations, and tests.

## Why

Network problems cross multiple control points: DNS, routing, NSGs, firewalls, peering, service endpoints, and the target listener. Network Watcher tools narrow the fault domain; Connection Monitor detects ongoing path degradation instead of relying on one-time manual tests.

## How

Choose a diagnostic that matches the question: effective rules/IP flow for NSG decisions, next hop for route selection, connection troubleshoot for a one-off path, packet capture for packet-level evidence, and Connection Monitor for recurring end-to-end tests. Configure source/destination, protocol/port, frequency, and workspace/log destination where applicable. Ensure required agents and permissions exist for the selected endpoint type.

## Features

- Connection Monitor tracks reachability, latency, and path changes for configured test groups; it is distinct from a one-time Connection troubleshoot operation.
- Azure Network Watcher availability and tools are regional; enable or verify the service in the relevant region.
- IP flow verify evaluates whether an NSG allows or denies a flow; it does not prove that the application is listening or that every intervening device is healthy.
- Effective routes and security rules help inspect applied configuration; packet capture offers deeper evidence but has data-handling and cost implications.
- Exam trap: a successful route/NSG check does not guarantee DNS resolution, remote firewall allowance, or service availability.

## Code snippets (if any)

```bash
az network watcher test-ip-flow --resource-group "<resource-group>" --vm "<vm-name>" --direction Outbound --protocol TCP --local "<source-ip>" --local-port "<source-port>" --remote "<destination-ip>" --remote-port 443
```

The Azure CLI command evaluates the VM's NSG decision for a flow. Use `az network watcher test-ip-flow -h` to check any version-specific required parameters.

## Do's and Don'ts

- Do investigate in layers: name resolution, effective route, NSGs, firewalls, peering, and service listener.
- Do test the actual protocol and port and use Connection Monitor for sustained path SLOs.
- Do limit packet capture duration and protect captured data.
- Don't infer application health from an NSG allow result.
- Don't forget region, endpoint agent, and permissions prerequisites for diagnostics.

## Real-life implementation

For a hybrid application, create a Connection Monitor test from an Azure VM to an on-premises endpoint on the required TCP port. Alert on sustained reachability or latency degradation. If it fails, use next hop and effective security rules to check the Azure path, then validate VPN/ExpressRoute, on-premises firewall, DNS, and listener. This yields actionable evidence without making a broad, risky network rule change.

## Q&A

1. **Which tool checks an NSG decision for a flow?** IP flow verify.
2. **Which tool checks selected route next hop?** Next hop.
3. **What is Connection Monitor for?** Repeated connectivity and latency tests between endpoints.
4. **Does IP flow verify prove the application is working?** No; it evaluates network security rules, not DNS, remote firewall, or application state.

References: [Network Watcher overview](https://learn.microsoft.com/azure/network-watcher/network-watcher-overview), [Connection Monitor](https://learn.microsoft.com/azure/network-watcher/connection-monitor-overview), [IP flow verify](https://learn.microsoft.com/azure/network-watcher/ip-flow-verify-overview).

Syllabus: [copilot-az104-syllabus.md](../../../copilot-az104-syllabus.md).
