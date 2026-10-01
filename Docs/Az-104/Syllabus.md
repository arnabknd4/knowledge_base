# AZ-104 Prerequisites: Architect Level

**Legend:** R = Required | O = Optional | E = Exam-oriented | L = Real-life use

---

## 1. Cloud & Azure Foundations

| Topic | Flag |
|---|---|
| Cloud models (IaaS / PaaS / SaaS) | R, E |
| Shared responsibility model | R, E, L |
| Public / Private / Hybrid cloud | R, E |
| Azure Regions & Region Pairs | R, E, L |
| Availability Zones | R, E, L |
| Azure Geography | O, E |
| Azure Resource Manager (ARM) | R, E, L |
| Resource Groups | R, E, L |
| Subscriptions | R, E, L |
| Management Groups | R, E, L |
| Azure Portal / Cloud Shell | R, E, L |
| Azure CLI | R, E, L |
| Azure PowerShell | R, E, L |
| ARM Templates | R, E, L |
| Bicep | R, E, L |
| Terraform on Azure | O, L |
| Resource Providers | O, E |
| Tags | R, E, L |
| Resource Locks | R, E, L |
| Cost basics (Pricing Calculator, TCO) | O, L |

## 2. Identity & Access

| Topic | Flag |
|---|---|
| Microsoft Entra ID (Azure AD) | R, E, L |
| Tenant vs Subscription | R, E, L |
| Users / Groups / Dynamic Groups | R, E, L |
| Guest Users (B2B) | R, E, L |
| Administrative Units | O, E |
| Self-Service Password Reset (SSPR) | R, E, L |
| MFA | R, L |
| Conditional Access | O, L |
| Entra Connect / Hybrid Identity | O, E, L |
| Azure RBAC | R, E, L |
| Built-in vs Custom Roles | R, E |
| Role Assignment Scope | R, E, L |
| Entra Roles vs Azure Roles | R, E |
| Managed Identities | R, E, L |
| Service Principals / App Registrations | O, L |
| Privileged Identity Management (PIM) | O, L |
| Identity Protection | O |

## 3. Governance & Compliance

| Topic | Flag |
|---|---|
| Azure Policy | R, E, L |
| Initiatives | R, E |
| Policy Effects (Deny, Audit, DeployIfNotExists) | R, E |
| Blueprints (deprecated, awareness only) | O |
| Microsoft Defender for Cloud basics | O, L |
| Cost Management + Budgets | R, E, L |
| Azure Advisor | O, E, L |
| Service Health | O, L |

## 4. Networking Fundamentals (pre-Azure)

| Topic | Flag |
|---|---|
| IP addressing, CIDR, subnetting | R, E, L |
| Public vs Private IP | R, E, L |
| DNS basics | R, E, L |
| TCP/UDP, common ports | R, L |
| NAT | R, L |
| Routing basics | R, E, L |
| VPN / IPsec basics | R, E |
| Load balancing (L4 vs L7) | R, E, L |
| Firewall concepts | R, L |
| HTTP/HTTPS, TLS | R, L |

## 5. Azure Virtual Networking

| Topic | Flag |
|---|---|
| Virtual Network (VNet) | R, E, L |
| Subnets | R, E, L |
| NSG (Network Security Groups) | R, E, L |
| Application Security Groups | R, E |
| Service Tags | R, E |
| VNet Peering (regional, global) | R, E, L |
| Gateway Transit | O, E |
| User-Defined Routes (UDR) | R, E, L |
| System Routes | R, E |
| Azure DNS (public, private zones) | R, E, L |
| Service Endpoints | R, E, L |
| Private Endpoint / Private Link | R, E, L |
| Azure Load Balancer | R, E, L |
| Application Gateway / WAF | R, E, L |
| Azure Front Door | O, L |
| Traffic Manager | O, E |
| VPN Gateway (S2S, P2S) | R, E, L |
| ExpressRoute | O, E, L |
| Azure Bastion | R, E, L |
| Azure Firewall | O, E, L |
| Network Watcher | R, E, L |
| NAT Gateway | O, L |

## 6. Storage

| Topic | Flag |
|---|---|
| Storage Account types | R, E, L |
| Redundancy (LRS, ZRS, GRS, GZRS, RA-) | R, E, L |
| Blob / File / Queue / Table | R, E, L |
| Access Tiers (Hot, Cool, Cold, Archive) | R, E, L |
| Lifecycle Management | R, E, L |
| Shared Access Signature (SAS) | R, E, L |
| Stored Access Policy | O, E |
| Storage Account Keys | R, E |
| Entra ID auth for storage | R, E, L |
| Storage Firewalls & VNet rules | R, E, L |
| Azure Files / File Sync | R, E, L |
| AzCopy | R, E, L |
| Storage Explorer | O, L |
| Import/Export, Data Box | O, E |
| Blob versioning, soft delete, snapshots | R, E, L |
| Immutable storage | O, E |
| Object replication | O, E |
| Managed Disks (types, encryption) | R, E, L |
| Encryption (SSE, CMK) | O, E |

## 7. Compute

| Topic | Flag |
|---|---|
| Virtual Machines (sizes, series) | R, E, L |
| Availability Sets | R, E |
| Availability Zones for VMs | R, E, L |
| VM Scale Sets (VMSS) | R, E, L |
| Autoscale | R, E, L |
| VM Extensions / Custom Script | R, E, L |
| VM Images / Compute Gallery | O, E |
| Disk encryption (ADE) | O, E |
| Azure Backup / Recovery Services Vault | R, E, L |
| Azure Site Recovery | R, E, L |
| Azure Migrate | O, E |
| App Service / App Service Plan | R, E, L |
| Deployment Slots | R, E, L |
| Scaling (up vs out) | R, E, L |
| Azure Container Instances (ACI) | R, E, L |
| Azure Container Registry (ACR) | R, E, L |
| Azure Container Apps | R, E |
| AKS (basics only) | O, L |
| Azure Functions | O, L |
| Docker basics | R, L |

## 8. Monitoring & Maintenance

| Topic | Flag |
|---|---|
| Azure Monitor | R, E, L |
| Metrics vs Logs | R, E, L |
| Log Analytics Workspace | R, E, L |
| KQL (basics) | R, E, L |
| Alerts, Action Groups | R, E, L |
| Diagnostic Settings | R, E, L |
| Application Insights | O, E, L |
| Activity Log | R, E, L |
| VM Insights | O, E |
| Network Insights | O, E |
| Update Management / Azure Update Manager | O, L |
| Backup reports | O |

## 9. Supporting Skills

| Topic | Flag |
|---|---|
| Windows Server & Linux admin basics | R, L |
| Active Directory (on-prem) basics | R, E, L |
| PowerShell basics | R, E, L |
| JSON / YAML | R, L |
| REST API basics | O, L |
| High Availability vs Disaster Recovery | R, E, L |
| RTO / RPO | R, E, L |
| SLA calculation | R, E |
| Well-Architected Framework (pillars) | R, L |
| Cloud Adoption Framework | O, L |

## 10. Architect-Level Add-ons (beyond AZ-104 scope)

| Topic | Flag |
|---|---|
| Hub-and-Spoke topology | O, L |
| Landing Zones | O, L |
| Azure Policy at scale | O, L |
| Multi-region DR design | O, L |
| Zero Trust | O, L |