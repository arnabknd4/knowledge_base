# AZ-305 (Azure Solutions Architect Expert): Prerequisites and Core Topics

**Legend:** **[R]** Required | **[O]** Optional | **[E]** Exam-oriented | **[L]** Real-life use

---

## 1. Cloud Fundamentals
- Cloud service models: IaaS / PaaS / SaaS: **[R][E][L]**
- Deployment models: public / private / hybrid / multi-cloud: **[R][E]**
- Shared responsibility model: **[R][E][L]**
- CapEx vs OpEx: **[R][L]**
- Consumption-based pricing: **[R][L]**
- High availability, scalability, elasticity, fault tolerance, agility: **[R][E]**
- Well-Architected Framework (5 pillars: Reliability, Security, Cost, Operational Excellence, Performance): **[R][E][L]**
- Cloud Adoption Framework (CAF): **[R][E][L]**
- Azure Landing Zones: **[R][E][L]**

## 2. Azure Core Architecture
- Geography, region, region pairs: **[R][E]**
- Availability Zones vs Availability Sets: **[R][E][L]**
- Management groups → Subscriptions → Resource groups → Resources: **[R][E][L]**
- Azure Resource Manager (ARM): **[R][E][L]**
- ARM templates / Bicep: **[R][E][L]**
- Tags, resource locks: **[R][L]**
- Azure Portal / CLI / PowerShell / Cloud Shell: **[R][L]**
- Azure Resource Graph: **[O][L]**

## 3. Identity & Access
- Microsoft Entra ID (Azure AD): tenants, users, groups: **[R][E][L]**
- Authentication vs Authorization: **[R][E]**
- Azure RBAC vs Entra roles: **[R][E][L]**
- Conditional Access: **[R][E][L]**
- MFA, passwordless: **[R][L]**
- Managed Identities, Service Principals, App Registrations: **[R][E][L]**
- Privileged Identity Management (PIM): **[R][E][L]**
- Entra ID B2B / B2C / External ID: **[R][E]**
- Entra Connect (hybrid identity), SSO, federation: **[R][E][L]**
- OAuth 2.0 / OpenID Connect / SAML basics: **[R][L]**
- Identity Protection, Access Reviews: **[O][E]**
- Entra Domain Services: **[O][E]**

## 4. Governance & Compliance
- Azure Policy, initiatives: **[R][E][L]**
- Blueprints (legacy) vs Template Specs / Deployment Stacks: **[O][E]**
- Microsoft Defender for Cloud: **[R][E][L]**
- Microsoft Purview: **[O][E]**
- Cost Management + Budgets, Advisor: **[R][E][L]**
- Reservations, Savings Plans, Hybrid Benefit, Spot: **[R][E][L]**
- Azure Service Health, Resource Health: **[O][L]**

## 5. Networking
- IP addressing, CIDR, subnetting: **[R][L]**
- DNS basics: **[R][L]**
- Ports, protocols (TCP/UDP/HTTP/HTTPS): **[R][L]**
- OSI model (high-level only): **[O]**
- VNet, Subnets: **[R][E][L]**
- NSG, ASG: **[R][E][L]**
- VNet peering, Virtual WAN: **[R][E][L]**
- VPN Gateway, ExpressRoute: **[R][E][L]**
- Azure Firewall, Firewall Manager, WAF: **[R][E][L]**
- Load balancing options: Load Balancer, Application Gateway, Front Door, Traffic Manager: **[R][E][L]**
- Private Endpoint vs Service Endpoint, Private Link: **[R][E][L]**
- Azure DNS, Private DNS zones: **[R][E][L]**
- Hub-and-spoke topology: **[R][E][L]**
- UDR / route tables, NAT Gateway: **[R][L]**
- Azure Bastion: **[R][L]**
- DDoS Protection: **[O][E]**

## 6. Compute
- VMs, VM sizes/series, VM Scale Sets: **[R][E][L]**
- App Service (plans, slots): **[R][E][L]**
- Azure Functions: **[R][E][L]**
- Containers: ACI, AKS, Container Apps, ACR: **[R][E][L]**
- Containers vs VMs (concept): **[R]**
- Azure Batch: **[O][E]**
- Azure Virtual Desktop: **[O][E]**
- Serverless vs PaaS vs IaaS selection: **[R][E]**

## 7. Storage
- Storage account types, redundancy (LRS/ZRS/GRS/GZRS/RA-): **[R][E][L]**
- Blob, Files, Queue, Table, Disk: **[R][E][L]**
- Access tiers (Hot/Cool/Cold/Archive), lifecycle management: **[R][E][L]**
- SAS, access keys, Entra-based storage access: **[R][E][L]**
- Managed disk types: **[R][E]**
- Azure NetApp Files: **[O][E]**
- Data Lake Storage Gen2: **[R][E]**
- Azure File Sync, Data Box, AzCopy, Storage Explorer: **[O][E]**

## 8. Databases & Data
- Relational vs NoSQL vs analytical (concept): **[R]**
- Azure SQL: Database, Managed Instance, SQL on VM: **[R][E][L]**
- Purchasing models (DTU vs vCore), elastic pools, serverless: **[R][E]**
- Cosmos DB: APIs, consistency levels, partitioning, RU/s: **[R][E][L]**
- PostgreSQL / MySQL Flexible Server: **[O][E]**
- Azure Cache for Redis: **[R][E][L]**
- Synapse, Data Factory, Databricks, Microsoft Fabric (overview level): **[R][E]**
- Event Hubs, Stream Analytics: **[O][E]**
- Data partitioning, sharding, replication: **[R][E]**

## 9. Integration & Application Architecture
- Microservices vs monolith: **[R][E]**
- REST APIs, API Management: **[R][E][L]**
- Messaging: Service Bus vs Event Grid vs Event Hubs vs Storage Queue: **[R][E][L]**
- Logic Apps: **[R][E]**
- Event-driven architecture, pub/sub: **[R][E]**
- Caching patterns, CDN: **[R][E]**
- Cloud design patterns (Retry, Circuit Breaker, CQRS, Sidecar, Strangler, etc.): **[R][E][L]**

## 10. Business Continuity & Resilience
- RTO / RPO / SLA / SLO / Composite SLA: **[R][E][L]**
- Azure Backup, Recovery Services vault, Backup vault: **[R][E][L]**
- Azure Site Recovery: **[R][E][L]**
- Active-active vs active-passive, failover strategies: **[R][E]**
- Geo-replication, failover groups: **[R][E]**
- Chaos Studio: **[O]**

## 11. Monitoring & Operations
- Azure Monitor, Metrics, Logs: **[R][E][L]**
- Log Analytics workspace, KQL basics: **[R][E][L]**
- Application Insights: **[R][E][L]**
- Alerts, Action Groups, Workbooks: **[R][L]**
- Microsoft Sentinel (overview): **[O][E]**
- Diagnostic settings, Activity Log: **[R][L]**
- Azure Automation, Update Manager: **[O][L]**

## 12. Security
- Zero Trust, defense in depth, least privilege: **[R][E]**
- Key Vault (keys, secrets, certs): **[R][E][L]**
- Encryption at rest / in transit, CMK vs PMK, TLS: **[R][E][L]**
- Confidential computing: **[O][E]**
- Secure score, Defender plans: **[R][E]**

## 13. Migration & Hybrid
- 5 Rs / 6 Rs of migration (rehost, refactor, rearchitect, rebuild, replace): **[R][E]**
- Azure Migrate, Database Migration Service: **[R][E][L]**
- Azure Arc: **[R][E]**
- Azure Stack (HCI / Hub): **[O][E]**
- Hybrid connectivity (VPN / ExpressRoute) design: **[R][E]**
- Assessment, discovery, dependency mapping: **[R][L]**

## 14. DevOps & IaC (Awareness Level)
- IaC concept, declarative vs imperative: **[R][L]**
- Bicep / ARM / Terraform (overview): **[R][E][L]**
- CI/CD basics, Azure DevOps / GitHub Actions (overview): **[O][L]**
- Deployment strategies (blue-green, canary, rolling): **[R][E]**

## 15. Exam-Specific Skills
- Requirement-to-service mapping: **[R][E]**
- Cost vs performance vs availability trade-offs: **[R][E]**
- Case study format and reading strategy: **[R][E]**
- Microsoft Learn sandbox / free tier practice: **[R][L]**