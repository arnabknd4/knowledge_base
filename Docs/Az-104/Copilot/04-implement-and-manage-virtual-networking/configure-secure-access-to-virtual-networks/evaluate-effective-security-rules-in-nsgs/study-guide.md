# Evaluate effective security rules in NSGs

## What

Effective security rules are the combined NSG policy that applies to a VM network interface after considering rules from associated subnet and NIC NSGs. Evaluation depends on direction, protocol, source/destination, ports, and priority; the first matching rule at a given evaluation layer decides allow or deny.

## Why

Reading a single NSG is insufficient when a NIC inherits subnet rules or has its own NSG. Effective-rule analysis helps explain why a flow is blocked or allowed and prevents risky troubleshooting changes that mask the actual policy conflict.

## How

For the exact flow, write down source IP/port, destination IP/port, protocol, and direction. Inspect all associated NSGs and effective security rules on the NIC. Find the first matching custom rule; if none matches, consider default rules. Remember outbound rules are evaluated independently from inbound rules, and stateful response traffic for an allowed connection is handled automatically. Then check route selection, firewalls, guest firewall, and service listener: an NSG allow does not prove end-to-end connectivity.

When a rule is unexpected, verify the association scope, rule priority, address-prefix/service-tag semantics, ASG membership, and whether the intended NIC actually belongs to that ASG. Use IP flow verify for a specific tuple and effective NSG listing for configuration evidence. Avoid temporary broad allows; if necessary, time-bound and approve a narrowly scoped diagnostic rule.

## Features

- Effective NSG view accounts for subnet and NIC association.
- IP flow verify evaluates allow/deny for a specified packet tuple.
- Custom rules precede default rules when their priority is higher (lower number).
- Network ACLs are stateful; response traffic for an allowed flow is permitted automatically.

## Code snippets (if any)

```bash
az network nic list-effective-nsg --resource-group <rg> --name <nic-name>
az network watcher test-ip-flow --resource-group <rg> --vm <vm-name> --direction Inbound --protocol TCP --local <destination-ip>:443 --remote <source-ip>:50000
```

## Do's and Don'ts

- **Do** analyze the exact five-tuple and both directions.
- **Do** inspect rule priority and every NSG association.
- **Don't** infer effective behavior from one NSG's rules alone.
- **Don't** mistake an NSG allow for proof that route, firewall, or application layers are healthy.
- **Don't** disable default protections to troubleshoot.

## Real-life implementation

An API VM times out on port 8443 from a web subnet. Query its effective NSG and run IP flow verify for the web source and API destination. If denied, identify the matching priority and correct the narrow rule or ASG membership. If allowed, inspect effective route/next hop, firewall policy, guest firewall, and listener. Validate the fix with a real TCP/application probe and preserve the before/after evidence.

## Q&A

1. **If subnet NSG allows and NIC NSG denies, is the flow allowed?** No. The flow must pass all applicable NSGs.
2. **Do lower or higher priority numbers run first?** Lower numbers run first.
3. **Does IP flow verify confirm an application is listening?** No; it diagnoses NSG decision for the specified flow.
4. **Does a permitted inbound flow need an explicit return rule?** Not for stateful response traffic of that allowed connection.

---
Source: [Microsoft Learn — Diagnose a VM network traffic filter problem](https://learn.microsoft.com/azure/virtual-network/diagnose-network-traffic-filter-problem) · [AZ-104 syllabus](../../../copilot-az104-syllabus.md)
