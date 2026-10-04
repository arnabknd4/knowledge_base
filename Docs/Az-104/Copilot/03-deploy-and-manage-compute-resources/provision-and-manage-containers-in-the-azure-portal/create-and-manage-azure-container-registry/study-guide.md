# Create and manage an Azure Container Registry

## What
Azure Container Registry (ACR) is a private registry for OCI container images and related artifacts. It provides managed registry endpoints, repository/image/version organization, authentication, network controls, and optional geo-replication and build capabilities.

## Why
Centralized image distribution improves supply-chain governance and supports private workloads. Choose SKU based on throughput, storage, availability, geo-replication, and network requirements—not image count alone. Protect image provenance, minimize pull latency, and avoid public exposure or long-lived registry credentials.

## How
Create a unique registry name in the intended region/SKU. Prefer Microsoft Entra authentication and managed identity for push/pull; assign least-privilege roles scoped to registry/repositories where supported. Configure private endpoint/firewall if required, then connect builds and runtime services. In portal, review access, networking, tasks, and replication. CLI can create a registry and enable admin only for constrained test scenarios; production clients should use identity-based access.

## Features
Basic, Standard, and Premium tiers differ in storage, throughput, availability, geo-replication, private endpoint, and other capabilities. ACR Tasks automate builds; content trust/signing and scanning integrations support supply-chain controls. Geo-replication improves regional availability and pull locality but has cost and replication considerations.

## Code snippets (if any)
```bash
az acr create --resource-group <resource-group> --name <globally-unique-registry-name> --sku <Basic-or-Standard-or-Premium> --admin-enabled false
az acr login --name <registry-name>
```
Use an authenticated Entra identity with appropriate RBAC; do not enable admin credentials as a shortcut.

## Do's and Don'ts
**Do** use immutable/versioned tags or digests in deployment, least-privilege identities, and image lifecycle cleanup. **Don't** treat a mutable `latest` tag as a release pin or embed registry passwords in deployment files.

## Real-life implementation
A team builds images in a CI identity, pushes signed release digests to Premium ACR, and grants a Container Apps managed identity pull access. Private networking and replication are selected based on runtime path and availability objectives.

## Q&A
1. **Is the ACR admin account preferred for production?** No. Use Entra-based identities and least privilege.
2. **Does a registry's existence mean a workload can pull privately?** No. Network reachability, DNS/private endpoint, and identity authorization must all work.
3. **What does geo-replication provide?** Regional registry replicas for availability/performance, not application failover by itself.

**References:** [ACR overview](https://learn.microsoft.com/azure/container-registry/container-registry-intro) · [Authenticate with managed identity](https://learn.microsoft.com/azure/container-registry/container-registry-authentication-managed-identity)

---
[Back to Domain 3 index](../../index.md) · [Syllabus objective](../../../copilot-az104-syllabus.md#provision-and-manage-containers-in-the-azure-portal)
