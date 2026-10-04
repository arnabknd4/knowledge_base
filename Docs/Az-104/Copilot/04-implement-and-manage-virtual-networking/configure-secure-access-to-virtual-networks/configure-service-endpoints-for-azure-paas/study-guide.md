# Configure service endpoints for Azure PaaS

## What

Virtual network service endpoints extend a VNet subnet's identity to supported Azure services over the Azure backbone. The service resource's network firewall can then allow selected VNets/subnets. The service continues to use its public endpoint; the endpoint is not a private IP address in the VNet.

## Why

Service endpoints provide subnet-based access control and backbone routing without deploying private IP interfaces. They are a fit when public endpoint access is acceptable but should be limited to selected subnets. Choose private endpoints when private IP connectivity and private name resolution are requirements.

## How

Enable the appropriate service endpoint on the source subnet, then configure the target PaaS resource's network rules to allow that subnet. Validate both sides: endpoint enabled on subnet and firewall rule on the service. Service endpoint policies can further restrict eligible Azure Storage resources where supported. Existing connections and service-specific behavior should be tested during rollout.

Service endpoints change the source identity observed by the service to the subnet identity; evaluate dependencies such as outbound IP allowlists and service firewall behavior. They do not provide transitive access through peering and are not a substitute for service authorization. Troubleshoot DNS, subnet configuration, resource firewall rules, and identity/data-plane permissions separately.

## Features

- Supported Azure PaaS services, including Azure Storage and Azure SQL, offer service endpoint types.
- Service access is controlled by source subnet rules at the service resource.
- Traffic stays on the Azure backbone, while service access still targets its public endpoint.
- Service endpoint policies provide additional destination restrictions for supported scenarios.

## Code snippets (if any)

```bash
az network vnet subnet update --resource-group <rg> --vnet-name <vnet> --name <subnet> --service-endpoints Microsoft.Storage
```

Add the subnet to the target Storage account's virtual network rules separately.

## Do's and Don'ts

- **Do** configure both the subnet endpoint and the PaaS firewall allow rule.
- **Do** retain service-level identity authorization such as RBAC or SQL authentication policy.
- **Don't** call a service endpoint a private endpoint; DNS and endpoint addressing differ.
- **Don't** assume peered subnet access is automatically granted by a service endpoint rule.
- **Don't** enable endpoints without checking outbound allowlists and existing connectivity.

## Real-life implementation

A VM subnet needs access to one Storage account while the account remains reachable through its public endpoint. Enable the `Microsoft.Storage` endpoint on that subnet and add only that subnet to the account's network rules. Use identity-based data access for authorization, test access from an allowed VM and a disallowed network, and monitor firewall/network logs.

## Q&A

1. **Does a service endpoint assign a private IP to the PaaS service?** No; the service endpoint is reached through the service's public endpoint.
2. **What two configurations are needed?** Enable the endpoint on the subnet and allow that subnet in the service firewall.
3. **Does the endpoint grant data access?** No; identity and service authorization still apply.
4. **When is a private endpoint preferable?** When clients must use a private IP path and private DNS integration or public network disablement is required.

---
Source: [Microsoft Learn — Virtual network service endpoints](https://learn.microsoft.com/azure/virtual-network/virtual-network-service-endpoints-overview) · [AZ-104 syllabus](../../../copilot-az104-syllabus.md)
