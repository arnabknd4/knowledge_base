# AWS AND GCP: MULTI-CLOUD AWARENESS

Legend: P1–P4 = priority (P2 = learn alongside Azure, P3 = after Azure core, P4 = later). R = required, E = exam oriented, L = real life use, O = optional. Anchor every topic to its Azure equivalent from section 12.

---

## 13. AWS CLOUD

☐ 13.01 AWS fundamentals [P2 R E L] accounts; AWS Organizations; OUs; regions, AZs, Local Zones, edge locations; shared responsibility model; tags; Service Quotas; pricing models; SLAs; Console, CLI, CloudShell, SDKs; CloudFormation and CDK awareness; Resource Explorer; naming conventions

☐ 13.02 Identity and access [P2 R E L] IAM users, groups, roles; policy types (identity, resource, permission boundary, SCP, session); policy evaluation logic; STS and AssumeRole; instance profiles; IAM Identity Center; SAML and OIDC federation; Cognito awareness; MFA; Access Analyzer; cross-account access

☐ 13.03 Networking [P2 R E L] VPC; subnets; route tables; Internet Gateway; NAT Gateway; security groups vs NACLs; VPC peering; Transit Gateway; Site-to-Site VPN; Direct Connect; PrivateLink; gateway vs interface endpoints; Route 53; ELB (ALB, NLB, GWLB); CloudFront; Global Accelerator; WAF; Network Firewall; Flow Logs; Reachability Analyzer

☐ 13.04 Compute [P2 R E L] EC2 (instance families, EBS, AMIs, Auto Scaling, placement groups); Elastic Beanstalk; Lambda; ECS; Fargate; EKS; App Runner; Batch awareness; Savings Plans, Reserved, Spot; Graviton; Nitro awareness

☐ 13.05 Storage [P2 R E L] S3 (classes, lifecycle, versioning, replication, Object Lock, bucket policies, Block Public Access, presigned URLs); EBS; EFS; FSx; Glacier; Storage Gateway; DataSync; Transfer Family; Snow family awareness; AWS Backup

☐ 13.06 Databases and messaging [P3 R E L] RDS; Aurora; DynamoDB; ElastiCache; DocumentDB awareness; Redshift awareness; SQS; SNS; EventBridge; Kinesis; MSK awareness; Step Functions; API Gateway

☐ 13.07 Governance [P2 R E L] Organizations; SCPs; Control Tower; Config; CloudTrail; Service Catalog; Tag Policies; Resource Access Manager; Budgets; Cost Explorer; Trusted Advisor; Well-Architected Tool

☐ 13.08 Monitoring and operations [P3 R E L] CloudWatch (metrics, logs, alarms, Logs Insights, dashboards); X-Ray; CloudTrail; EventBridge; Systems Manager; AWS Health; AWS Backup; Elastic Disaster Recovery; ADOT and OpenTelemetry; Managed Grafana and Prometheus awareness

☐ 13.09 Security services [P3 R E L] KMS; Secrets Manager; Parameter Store; ACM; GuardDuty; Security Hub; Inspector; Macie; Detective; Shield; WAF; Firewall Manager; CloudHSM awareness; Artifact; encryption at rest and in transit

☐ 13.10 Migration to AWS [P3 R E L] the seven Rs; Migration Hub; Application Discovery Service; Application Migration Service (MGN); DMS and SCT; DataSync; Snow family; Migration Evaluator; MAP awareness; legacy .NET Framework on EC2, Windows containers, Elastic Beanstalk

☐ 13.11 Well-Architected Framework [P3 R E] six pillars and trade-offs; Well-Architected Tool; lenses; reference architectures (Architecture Center); architecture styles

☐ 13.12 High availability and DR [P3 R E L] Multi-AZ vs multi-region; DR strategies (backup and restore, pilot light, warm standby, multi-site active-active); Route 53 failover; Aurora Global Database; DynamoDB global tables; S3 replication; Resilience Hub; Fault Injection Service; RPO and RTO

☐ 13.13 Cost management and FinOps [P3 R L] Pricing Calculator; Cost Explorer; Cost and Usage Report; Budgets; Savings Plans; Reserved Instances; Spot; Compute Optimizer; Cost Anomaly Detection; data transfer costs; tagging and allocation; FinOps framework

☐ 13.14 Landing zones and multi-account design [P4 R E L] Control Tower; multi-account strategy; OU design; log archive and audit accounts; network account; SCP guardrails; Account Factory; Landing Zone Accelerator; Transit Gateway hub-spoke; IAM Identity Center

☐ 13.15 AWS certification blueprints [P4 O E] Cloud Practitioner; Solutions Architect Associate; Solutions Architect Professional; DevOps Engineer Professional; Security Specialty (verify current exam codes and domains as published)

---

## 14. GCP CLOUD

☐ 14.01 GCP fundamentals [P2 R E L] organization, folders, projects; resource hierarchy; billing accounts; regions and zones; labels vs tags; quotas; Console, gcloud, Cloud Shell, client libraries; Cloud Asset Inventory; pricing models; sustained use and committed use discounts; SLAs

☐ 14.02 Identity and access [P2 R E L] Cloud Identity; Google Workspace awareness; principals; basic, predefined, custom roles; policy inheritance; service accounts; impersonation; Workload Identity Federation; deny policies; IAP; Policy Troubleshooter; Organization Policy constraints

☐ 14.03 Networking [P2 R E L] global VPC; auto vs custom subnets; firewall rules; hierarchical firewall policies; Shared VPC; VPC peering; Cloud VPN; Cloud Interconnect; Cloud Router; Network Connectivity Center; Private Google Access; Private Service Connect; Cloud DNS; Cloud NAT; Cloud Load Balancing (global vs regional); Cloud CDN; Cloud Armor; Network Intelligence Center; Premium vs Standard tier

☐ 14.04 Compute [P2 R E L] Compute Engine (machine families, instance templates, MIGs, images, Persistent Disk, Hyperdisk); App Engine; Cloud Run; Cloud Functions; GKE (Autopilot vs Standard); Batch awareness; Spot VMs; committed use discounts

☐ 14.05 Storage [P2 R E L] Cloud Storage (classes, Autoclass, lifecycle, versioning, retention, signed URLs, uniform bucket-level access); Persistent Disk; Filestore; Storage Transfer Service; Transfer Appliance awareness

☐ 14.06 Databases, data and messaging [P3 R E L] Cloud SQL; AlloyDB; Spanner; Firestore; Bigtable; Memorystore; BigQuery; Pub/Sub; Dataflow awareness; Eventarc; Cloud Tasks; Workflows; API Gateway; Apigee awareness

☐ 14.07 Governance [P2 R E L] Organization Policy; folder design; labels; Cloud Asset Inventory; Cloud Audit Logs; Security Command Center; Billing budgets and alerts; Recommender and Active Assist; Assured Workloads awareness

☐ 14.08 Monitoring and operations [P3 R E L] Cloud Monitoring; Cloud Logging; Log Analytics; Error Reporting; Cloud Trace; Cloud Profiler; alerting policies; uptime checks; SLO monitoring; Ops Agent; Managed Service for Prometheus; OpenTelemetry; Backup and DR Service; Personalized Service Health

☐ 14.09 Security services [P3 R E L] Cloud KMS; CMEK; Secret Manager; Certificate Manager; Security Command Center; Cloud Armor; VPC Service Controls; Binary Authorization; Confidential Computing awareness; Sensitive Data Protection; IAP and BeyondCorp awareness

☐ 14.10 Migration to GCP [P3 R E L] the six Rs; Migration Center; Migrate to Virtual Machines; Database Migration Service; Storage Transfer Service; Migrate to Containers; legacy .NET Framework on Compute Engine, Windows containers, GKE Windows nodes

☐ 14.11 Architecture Framework [P3 R E] framework pillars and trade-offs; Cloud Architecture Center; reference architectures; SRE concepts (SLI, SLO, error budgets); architecture styles

☐ 14.12 High availability and DR [P3 R E L] zonal vs regional vs multi-regional; regional MIGs; Cloud SQL HA; Spanner multi-region; global load balancing failover; Backup and DR Service; RPO and RTO

☐ 14.13 Cost management and FinOps [P3 R L] Pricing Calculator; billing reports; BigQuery billing export; budgets and alerts; committed use discounts; Spot VMs; rightsizing recommendations; labels and allocation; network egress costs; FinOps framework

☐ 14.14 Landing zones and enterprise foundations [P4 R E L] enterprise foundations blueprint; organization and folder hierarchy; Shared VPC host and service projects; hub-spoke; Organization Policy at scale; Terraform blueprints; Assured Workloads awareness

☐ 14.15 GCP certification blueprints [P4 O E] Cloud Digital Leader; Associate Cloud Engineer; Professional Cloud Architect; Professional Cloud DevOps Engineer; Professional Cloud Security Engineer (verify current exam names and domains as published)

---

## 15. MULTI-CLOUD AWARENESS

☐ 15.01 Service mapping Azure ↔ AWS ↔ GCP [P2 R E L] compute; containers; serverless; object, block, file storage; relational and NoSQL databases; messaging and eventing; load balancing; DNS; CDN; WAF; secrets and keys; monitoring and logging; IaC; policy; cost tools

☐ 15.02 Hierarchy and identity model comparison [P2 R E L] tenant, management group, subscription, resource group vs organization, OU, account vs organization, folder, project; Azure RBAC vs IAM vs GCP IAM; managed identity vs IAM role vs service account; workload identity federation across clouds; CI/CD OIDC to each cloud

☐ 15.03 Cross-cloud networking [P3 R L] VPN between clouds; dedicated interconnect options; colocation and cloud exchange awareness; overlapping CIDR; DNS across clouds; egress costs; latency and data gravity; ExpressRoute, Direct Connect, Cloud Interconnect comparison

☐ 15.04 Portable platform layer [P2 R E L] Kubernetes (AKS, EKS, GKE); containers; Terraform and OpenTofu; Helm; Argo CD; GitHub Actions; OpenTelemetry; Istio; Vault awareness; Crossplane and Pulumi awareness; policy as code (OPA, Kyverno, Checkov)

☐ 15.05 Multi-cloud strategy and trade-offs [P3 R E L] reasons for multi-cloud; anti-patterns; vendor lock-in; data gravity; egress; skills cost; concentration risk; exit strategy; regulatory drivers (DORA awareness); data sovereignty; best-of-breed vs standardization; cross-cloud DR; active-active difficulty

☐ 15.06 Hybrid and multi-cloud management [P3 R L] Azure Arc; AWS Outposts; Google Distributed Cloud; EKS Anywhere; Arc-enabled Kubernetes; centralized monitoring; centralized logging; single pane of glass limits; FinOps across clouds; FOCUS specification awareness (verify current names of hybrid offerings)

☐ 15.07 Security and compliance across clouds [P3 R E L] CSPM and CNAPP; Defender for Cloud multi-cloud connectors; Security Hub; Security Command Center; unified identity provider; shared responsibility comparison; compliance frameworks (ISO 27001, SOC 2); key management across clouds; audit logging comparison

☐ 15.08 Hands-on labs and revision [P4 R L] free tier labs per cloud; one reference architecture per cloud; same three-tier app deployed on each cloud; mapping-sheet drills; Terraform across all three; Kubernetes on each; cost comparison of the same workload