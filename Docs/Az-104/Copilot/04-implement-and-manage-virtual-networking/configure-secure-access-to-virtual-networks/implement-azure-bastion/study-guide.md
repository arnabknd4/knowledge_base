# Implement Azure Bastion

## What

Azure Bastion provides browser-based or native-client RDP/SSH access to VMs over their private IP addresses. The managed service is deployed into a dedicated `AzureBastionSubnet` in a VNet; administrators connect through the Azure portal or supported client workflow rather than exposing VM management ports publicly.

## Why

Bastion reduces attack surface by removing the need for VM public IPs and inbound Internet RDP/SSH. It centralizes the management entry point, but does not replace strong identity, MFA, least-privilege role assignment, endpoint hardening, or auditing.

## How

Plan the dedicated subnet and required prefix according to the selected Bastion SKU and current service requirements. Deploy Bastion in the target VNet and ensure operator permissions, licensing/SKU capabilities, and network connectivity to target VM private IPs. NSGs and UDRs on the dedicated subnet must follow Bastion service requirements; overly restrictive policy can break control or data paths. VM NSGs must allow management traffic from the appropriate Bastion subnet/service path. Keep VM public IPs removed unless a separate, justified workload requirement exists.

Availability and scaling capabilities vary by SKU and region; select the tier based on concurrent sessions, native client, IP-connect, zone, and scaling needs. Monitor deployment health, session capacity, connectivity, and cost. For failures, check Bastion provisioning state, subnet name/prefix, SKU, role permissions, target reachability, NSGs, and supported client settings.

## Features

- Private-IP access to Windows and Linux VMs using RDP/SSH.
- Browser-based sessions and supported native client options.
- SKU-dependent features include scaling, native client, IP-based connection, and zone support.
- Managed service; a dedicated `AzureBastionSubnet` is required.

## Code snippets (if any)

```bash
az network bastion create --resource-group <rg> --name <bastion-name> --vnet-name <vnet-name> --location <region> --sku Standard --public-ip-address <bastion-public-ip-name>
```

Create the required dedicated subnet and Standard public IP first; verify current SKU-specific requirements before deployment.

## Do's and Don'ts

- **Do** use a dedicated Bastion subnet and follow current minimum-prefix and policy requirements.
- **Do** pair access with MFA, least privilege, privileged identity controls, and auditing.
- **Don't** place workloads in `AzureBastionSubnet`.
- **Don't** assume Bastion provides VM patching, endpoint protection, or authorization.
- **Don't** keep public management ports open as a fallback without documented need.

## Real-life implementation

In a production hub, deploy Bastion for administrative access to private workload VMs, while keeping workload traffic on private subnets. Grant time-bound operator access through privileged role workflows and log access events. Restrict VM NSGs to the Bastion path and approved application flows. Test access after NSG or route changes, and plan Bastion SKU capacity and regional recovery options.

## Q&A

1. **Does Bastion require public IPs on target VMs?** No; it connects to their private IPs.
2. **Can `AzureBastionSubnet` host VMs?** No, it is dedicated to Bastion.
3. **Does Bastion automatically grant VM permissions?** No. Azure RBAC and target OS authentication/authorization still apply.
4. **Is Bastion free?** No; service tier and usage incur charges, so select capacity to match need.

---
Source: [Microsoft Learn — Azure Bastion overview](https://learn.microsoft.com/azure/bastion/bastion-overview) · [AZ-104 syllabus](../../../copilot-az104-syllabus.md)
