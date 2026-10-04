# Microsoft Azure Administrator (AZ-104) Exam Syllabus

This checklist follows Microsoft's official **Exam AZ-104 study guide**, including its skill-domain weights and objective hierarchy. The subtopic checkboxes restate the currently published skills in study-friendly form; they are not a promise that every listed item will appear on a particular exam.

> - **Certification:** Microsoft Certified: Azure Administrator Associate
> - **Exam code:** AZ-104
> - **Skills measured:** As of April 17, 2026
> - **Exam duration:** 100 minutes (proctored; interactive components may be included)
> - **Important:** Exam objectives can change. Recheck the official study guide before scheduling or sitting the exam.

## Exam domains

| Domain | Weight |
| --- | ---: |
| Manage Azure identities and governance | 20–25% |
| Implement and manage storage | 15–20% |
| Deploy and manage Azure compute resources | 20–25% |
| Implement and manage virtual networking | 15–20% |
| Monitor and maintain Azure resources | 10–15% |

## Candidate background

Microsoft describes AZ-104 candidates as administrators who implement, manage, and monitor an Azure environment, including identity, governance, security, networking, storage, and compute. Familiarity with operating systems, networking, servers, and virtualization is expected. Hands-on experience should include the Azure portal, Azure CLI, PowerShell, Microsoft Entra ID, and ARM templates or Bicep.

## 1. Manage Azure identities and governance (20–25%)

### Manage Microsoft Entra users and groups

- [ ] Create users and groups.
- [ ] Manage user and group properties.
- [ ] Manage licenses in Microsoft Entra ID.
- [ ] Manage external users.
- [ ] Configure self-service password reset (SSPR).

### Manage access to Azure resources

- [ ] Manage built-in Azure roles.
- [ ] Assign roles at different scopes.
- [ ] Interpret access assignments.

### Manage Azure subscriptions and governance

- [ ] Implement and manage Azure Policy.
- [ ] Configure resource locks.
- [ ] Apply and manage tags on resources.
- [ ] Manage resource groups.
- [ ] Manage subscriptions.
- [ ] Manage costs by using alerts, budgets, and Azure Advisor recommendations.
- [ ] Configure management groups.

## 2. Implement and manage storage (15–20%)

### Configure access to storage

- [ ] Configure Azure Storage firewalls and virtual networks.
- [ ] Create and use shared access signature (SAS) tokens.
- [ ] Configure stored access policies.
- [ ] Manage access keys.
- [ ] Configure identity-based access for Azure Files.

### Configure and manage storage accounts

- [ ] Create and configure storage accounts.
- [ ] Configure Azure Storage redundancy.
- [ ] Configure object replication.
- [ ] Configure storage account encryption.
- [ ] Manage data by using Azure Storage Explorer and AzCopy.

### Configure Azure Files and Azure Blob Storage

- [ ] Create and configure a file share in Azure Files.
- [ ] Create and configure a container in Azure Blob Storage.
- [ ] Configure storage tiers.
- [ ] Configure soft delete for blobs and containers.
- [ ] Configure snapshots and soft delete for Azure Files.
- [ ] Configure blob lifecycle management.
- [ ] Configure blob versioning.

## 3. Deploy and manage Azure compute resources (20–25%)

### Automate deployment by using ARM templates or Bicep

- [ ] Interpret an Azure Resource Manager (ARM) template or Bicep file.
- [ ] Modify an existing ARM template.
- [ ] Modify an existing Bicep file.
- [ ] Deploy resources by using an ARM template or Bicep file.
- [ ] Export a deployment as an ARM template or convert an ARM template to Bicep.

### Create and configure virtual machines

- [ ] Create a virtual machine.
- [ ] Configure encryption at host for Azure virtual machines.
- [ ] Move a virtual machine to another resource group, subscription, or region.
- [ ] Manage virtual machine sizes.
- [ ] Manage virtual machine disks.
- [ ] Deploy virtual machines to availability zones and availability sets.
- [ ] Deploy and configure Azure Virtual Machine Scale Sets.

### Provision and manage containers in the Azure portal

- [ ] Create and manage an Azure Container Registry.
- [ ] Provision a container by using Azure Container Instances.
- [ ] Provision a container by using Azure Container Apps.
- [ ] Manage sizing and scaling for containers, including Azure Container Instances and Azure Container Apps.

### Create and configure Azure App Service

- [ ] Provision an App Service plan.
- [ ] Configure scaling for an App Service plan.
- [ ] Create an App Service.
- [ ] Configure certificates and Transport Layer Security (TLS) for an App Service.
- [ ] Map an existing custom DNS name to an App Service.
- [ ] Configure backup for an App Service.
- [ ] Configure networking settings for an App Service.
- [ ] Configure deployment slots for an App Service.

## 4. Implement and manage virtual networking (15–20%)

### Configure and manage virtual networks in Azure

- [ ] Create and configure virtual networks and subnets.
- [ ] Create and configure virtual network peering.
- [ ] Configure public IP addresses.
- [ ] Configure user-defined routes.
- [ ] Troubleshoot network connectivity.

### Configure secure access to virtual networks

- [ ] Create and configure network security groups (NSGs) and application security groups.
- [ ] Evaluate effective security rules in NSGs.
- [ ] Implement Azure Bastion.
- [ ] Configure service endpoints for Azure platform as a service (PaaS).
- [ ] Configure private endpoints for Azure PaaS.

### Configure name resolution and load balancing

- [ ] Configure Azure DNS.
- [ ] Configure an internal or public load balancer.
- [ ] Troubleshoot load balancing.

## 5. Monitor and maintain Azure resources (10–15%)

### Monitor resources in Azure

- [ ] Interpret metrics in Azure Monitor.
- [ ] Configure log settings in Azure Monitor.
- [ ] Query and analyze logs in Azure Monitor.
- [ ] Set up alert rules, action groups, and alert processing rules in Azure Monitor.
- [ ] Configure and interpret monitoring of virtual machines, storage accounts, and networks by using Azure Monitor Insights.
- [ ] Use Azure Network Watcher and Connection Monitor.

### Implement backup and recovery

- [ ] Create a Recovery Services vault.
- [ ] Create an Azure Backup vault.
- [ ] Create and configure a backup policy.
- [ ] Perform backup and restore operations by using Azure Backup.
- [ ] Configure Azure Site Recovery for Azure resources.
- [ ] Perform a failover to a secondary region by using Site Recovery.
- [ ] Configure and interpret reports and alerts for backups.

## Architect-level preparation checklist

The following are study practices, not additional Microsoft exam objectives:

- [ ] For each service choice, explain the requirement it satisfies, operational responsibility, availability implications, security boundary, and cost impact.
- [ ] Practice interpreting requirements and choosing the correct Azure resource, scope, configuration, or troubleshooting step.
- [ ] Build and manage resources with the portal, Azure CLI, and PowerShell; understand equivalent ARM/Bicep deployment workflows.
- [ ] Work through identity and governance scenarios, especially role assignment scope, policy effects, locks, subscription organization, and budget alerts.
- [ ] Practice storage authorization and network restrictions; explain SAS, keys, identity-based access, redundancy, data protection, and lifecycle trade-offs.
- [ ] Practice VM, scale set, container, and App Service operations, including availability, sizing, scaling, deployment, and recovery.
- [ ] Trace network connectivity end to end across addressing, routes, NSGs, DNS, endpoints, and load balancing.
- [ ] Create monitoring queries and alerts, then practice backup restoration and Site Recovery failover concepts in a safe lab.
- [ ] Use the official practice assessment and exam sandbox to learn the question styles and interface; review missed objectives rather than memorizing answers.

## Official sources

- [Exam AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104) — authoritative skill domains, weights, objectives, and skills-measured date.
- [Microsoft Certified: Azure Administrator Associate](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/) — certification overview, exam duration, practice assessment, exam sandbox, and registration.
- [AZ-104 exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-104) — exam and preparation information.
- [Azure documentation](https://learn.microsoft.com/en-us/azure/) — official product documentation.
