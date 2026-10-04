# Configure networking settings for an App Service

## What
Configure how an App Service receives inbound traffic and reaches outbound dependencies. App Service has distinct controls for inbound access restrictions/private endpoints and outbound VNet integration; these are not interchangeable.

## Why
Network design establishes trust boundaries, private service access, egress control, DNS resolution, and integration with on-premises systems. Decisions affect plan eligibility, routing, private DNS, scale, operational complexity, and availability.

## How
For private ingress, evaluate a private endpoint and DNS; restrict or disable public access as required. For outbound access to VNet resources, configure regional VNet integration and subnet delegation/size, routes, DNS, and NSGs appropriately. Access restrictions filter inbound requests; they do not provide private outbound routing. Portal diagnostics, effective routes, DNS tests, and application logs can isolate issues. Verify both directions and failover paths.

## Features
VNet integration enables outbound access from the app to a VNet; it does not place the app worker into the subnet. Private endpoint provides a private inbound endpoint; private DNS makes the name resolve to it. Access restrictions provide network-based filtering. Feature/tier and configuration limits vary, and outbound IP behavior must be considered for firewall allowlists.

## Code snippets (if any)
No snippet required: subnet, DNS, and private-endpoint values depend on the existing network and plan. Validate the architecture in the portal and encode all linked network resources in reviewed IaC.

## Do's and Don'ts
**Do** distinguish inbound private endpoint from outbound VNet integration and test DNS from the app. **Don't** assume an access restriction creates private connectivity or that VNet integration automatically routes all egress through the VNet.

## Real-life implementation
A private API uses a private endpoint with private DNS for callers and VNet integration for outbound calls to a private database. Public access is disabled/restricted, routing and DNS are tested from the app, and dependencies have their own identity authorization.

## Q&A
1. **Which feature provides outbound VNet reachability?** VNet integration.
2. **Which feature provides private inbound access to the app?** A private endpoint, with correct DNS and access policy.
3. **Do access restrictions provide private networking?** No; they filter inbound requests by rules but do not establish private endpoint connectivity.

**References:** [App Service networking features](https://learn.microsoft.com/azure/app-service/networking-features) · [VNet integration](https://learn.microsoft.com/azure/app-service/overview-vnet-integration) · [Private endpoints](https://learn.microsoft.com/azure/app-service/overview-private-endpoint)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#create-and-configure-azure-app-service)
