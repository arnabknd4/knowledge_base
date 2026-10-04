# Create and configure NSGs and application security groups

## What

A network security group (NSG) contains stateful inbound and outbound allow/deny rules evaluated by priority. NSGs can be associated with subnets or NICs. Application security groups (ASGs) let rules refer to groups of NICs by application role instead of maintaining individual IP addresses.

## Why

NSGs implement network-layer least privilege and reduce accidental exposure. ASGs make policy easier to express across changing VM membership, but they do not replace identity controls, host firewalls, or a centralized firewall when deep inspection is required.

## How

Rules match source/destination address or service tag/ASG, protocol, and port range. Lower numeric priority is evaluated first; the first matching rule determines the result. Keep priorities unique within the NSG and leave room for future rules. Azure default rules allow VNet and load-balancer traffic and deny inbound Internet traffic; custom rules can override them when their priority matches first. Effective behavior can include both subnet and NIC NSGs, so assess both.

Use ASGs only where participating NICs satisfy the membership constraints. For a tiered service, permit web-to-app and app-to-data on explicit ports rather than broad VNet-to-VNet access. Plan outbound policy as carefully as inbound, and test critical platform dependencies before enforcing deny-by-default. Changes can affect live flows; use staged rollout and logs/flow analysis.

## Features

- Stateful filtering with inbound and outbound rule sets.
- Rule priority, service tags, IP prefixes, and ASG references.
- NSG association at subnet and/or NIC; combined effective policy applies.
- Default rules exist at lower precedence than custom rules.

## Code snippets (if any)

```bash
az network nsg create --resource-group <rg> --name <nsg> --location <region>
az network nsg rule create --resource-group <rg> --nsg-name <nsg> --name allow-https --priority 200 --direction Inbound --access Allow --protocol Tcp --source-address-prefixes Internet --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges 443
```

Apply an Internet-facing rule only to an intended frontend and constrain its destination where practical.

## Do's and Don'ts

- **Do** use explicit, least-privilege sources, destinations, ports, and priorities.
- **Do** name rules and ASGs for the workload function and document ownership.
- **Don't** assume a rule on one NSG is the whole effective policy.
- **Don't** expose SSH/RDP to all Internet sources.
- **Don't** use ASGs across incompatible network scopes; verify platform constraints before deployment.

## Real-life implementation

Create ASGs for web, application, and data NICs. Define inbound rules for HTTPS to web, approved application ports from web to app, and database ports from app to data. Associate NSGs at subnet boundaries and use NIC-level NSGs only where per-instance policy is needed. Stage changes on one pool member, verify health and diagnostics, and roll out consistently through infrastructure as code.

## Q&A

1. **Which rule wins?** The first matching rule in ascending priority order; lower numeric values are evaluated earlier.
2. **Do NSG rules support deny?** Yes, both allow and deny actions are supported.
3. **Do subnet and NIC NSGs combine?** Yes. A flow must be allowed through the applicable effective rules at both levels.
4. **What is an ASG?** A logical grouping of VM NICs used as a source or destination in NSG rules, not a firewall or IP address.

---
Source: [Microsoft Learn — Network security groups](https://learn.microsoft.com/azure/virtual-network/network-security-groups-overview) · [Microsoft Learn — Application security groups](https://learn.microsoft.com/azure/virtual-network/application-security-groups) · [AZ-104 syllabus](../../../copilot-az104-syllabus.md)
