# Terraform (TCA) – Prerequisites Before You Dive In

**Level:** Architect

**Legend:** 🔴 Required | 🟡 Optional | 📝 Exam-oriented | 🛠️ Real-life use

---

## 1. Infrastructure as Code (IaC) Fundamentals
- IaC concept (declarative vs imperative) – 🔴 📝 🛠️
- Idempotency – 🔴 📝
- Immutable vs mutable infrastructure – 🔴 📝 🛠️
- Configuration drift – 🔴 📝 🛠️
- Desired state vs current state – 🔴 📝
- IaC vs configuration management (Terraform vs Ansible) – 🔴 📝 🛠️
- Provisioning vs configuration vs orchestration – 🔴 📝
- Benefits of IaC (repeatability, versioning, auditability) – 📝

## 2. Cloud Fundamentals
- Public / private / hybrid / multi-cloud – 🔴 📝 🛠️
- IaaS / PaaS / SaaS – 🔴 📝
- Regions, availability zones – 🔴 🛠️
- IAM basics (users, roles, policies, service principals) – 🔴 🛠️
- Shared responsibility model – 🟡
- Basic compute, storage, network resources (VM, bucket, VPC/VNet) – 🔴 🛠️
- Cloud provider APIs – 🔴 📝
- Tagging and naming strategy – 🟡 🛠️

## 3. Networking Basics
- IP addressing, CIDR, subnets – 🔴 🛠️
- VPC / VNet concepts – 🔴 🛠️
- Public vs private subnets – 🔴 🛠️
- Security groups / NSGs / firewall rules – 🔴 🛠️
- Load balancer basics – 🟡 🛠️
- DNS basics – 🟡 🛠️
- NAT, gateways, routing – 🟡 🛠️

## 4. Linux and CLI Basics
- Terminal navigation and file handling – 🔴 🛠️
- Environment variables – 🔴 📝 🛠️
- Package installation, PATH – 🔴
- SSH and key pairs – 🔴 🛠️
- Basic shell scripting – 🟡 🛠️
- curl / jq basics – 🟡 🛠️

## 5. Data Formats and Syntax
- JSON – 🔴 📝 🛠️
- YAML – 🟡 🛠️
- Key-value pairs, maps, lists, objects – 🔴 📝
- HCL (HashiCorp Configuration Language) basics – 🔴 📝 🛠️
- Data types (string, number, bool, list, map, set, object, tuple) – 🔴 📝
- Expressions and string interpolation – 🔴 📝
- Conditionals, loops, functions (general programming logic) – 🟡 📝

## 6. Version Control (Git)
- Git basics (clone, commit, branch, merge) – 🔴 🛠️
- Branching strategies – 🟡 🛠️
- Pull requests and code review – 🟡 🛠️
- Remote repositories (GitHub / GitLab / Bitbucket) – 🔴 🛠️
- .gitignore (state files, secrets) – 🔴 📝 🛠️
- Tags and semantic versioning – 🔴 📝 🛠️

## 7. Security Fundamentals
- Secrets management – 🔴 📝 🛠️
- Least privilege principle – 🔴 📝 🛠️
- Credentials handling (env vars, profiles, CLI login) – 🔴 📝 🛠️
- Encryption at rest / in transit – 🟡 📝
- Sensitive data in state files – 🔴 📝 🛠️
- Vault basics (HashiCorp Vault / cloud secret managers) – 🟡 📝 🛠️
- Policy as code concept – 🟡 📝 🛠️

## 8. Dependency and Graph Concepts
- Dependency graph – 🔴 📝
- Implicit vs explicit dependencies – 🔴 📝
- Resource lifecycle (create, update, destroy) – 🔴 📝 🛠️
- Parallelism – 🟡 📝

## 9. State and Remote Storage Concepts
- Why state exists (state vs real infrastructure) – 🔴 📝 🛠️
- Local vs remote storage (object storage, database) – 🔴 🛠️
- State locking concept – 🔴 📝 🛠️
- Concurrency and race conditions – 🟡 🛠️
- Backup and versioning of state – 🔴 🛠️

## 10. DevOps and CI/CD Context
- DevOps lifecycle – 🔴
- CI/CD pipeline basics – 🔴 🛠️
- GitOps concept – 🟡 🛠️
- Environments (dev / test / stage / prod) – 🔴 🛠️
- Workflow: write → plan → review → apply – 🔴 📝 🛠️
- Approval gates and change management – 🟡 🛠️
- Pipeline tools (GitHub Actions, GitLab CI, Jenkins, Azure DevOps) – 🟡 🛠️

## 11. Architecture-Level Concepts
- Modular and reusable design – 🔴 📝 🛠️
- DRY principle – 🔴 📝
- Environment separation strategy – 🔴 🛠️
- Multi-account / multi-subscription design – 🟡 🛠️
- Blast radius and state segmentation – 🔴 📝 🛠️
- Governance, compliance, audit trails – 🟡 🛠️
- Cost control and estimation – 🟡 🛠️
- Disaster recovery and rollback thinking – 🟡 🛠️

## 12. Related Tooling (Awareness Only)
- Terraform vs CloudFormation / ARM / Bicep / Pulumi – 🟡 📝
- Terraform vs Ansible – 🔴 📝
- OpenTofu (fork awareness) – 🟡
- Packer (image building) – 🟡 🛠️
- Docker and Kubernetes basics – 🟡 🛠️
- Terraform Cloud / HCP Terraform (concept only) – 🟡 📝 🛠️

---

## Suggested Learning Order
1. IaC fundamentals
2. Cloud and networking basics
3. Git and CLI
4. JSON and HCL syntax
5. Security and secrets
6. State concepts
7. CI/CD and architecture patterns