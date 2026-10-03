# Cloud IaC Architecture – Prerequisites Before You Dive In

**Level:** Architect

**Scope:** Terraform, OpenTofu, Bicep, Pulumi, CloudFormation

**Legend:** 🔴 Required | 🟡 Optional | 📝 Certification-oriented | 🛠️ Real-life use

---

# 1. Infrastructure as Code (IaC) Foundations

- IaC concepts (declarative vs imperative) – 🔴 📝 🛠️
- Desired state vs current state – 🔴 📝
- Idempotency – 🔴 📝
- Immutable vs mutable infrastructure – 🔴 📝 🛠️
- Configuration drift – 🔴 📝 🛠️
- Infrastructure lifecycle management – 🔴 📝 🛠️
- Provisioning vs configuration vs orchestration – 🔴 📝
- Infrastructure testing concepts – 🟡 🛠️
- Infrastructure documentation practices – 🟡 🛠️
- Benefits of IaC (consistency, repeatability, auditability) – 🔴 📝

---

# 2. Cloud Fundamentals

- Public cloud concepts – 🔴 📝 🛠️
- Private cloud concepts – 🔴 📝
- Hybrid cloud architecture – 🔴 📝 🛠️
- Multi-cloud architecture – 🔴 📝 🛠️
- IaaS / PaaS / SaaS – 🔴 📝
- Regions and availability zones – 🔴 🛠️
- Resource groups, projects, accounts, subscriptions – 🔴 🛠️
- Cloud provider APIs – 🔴 📝
- IAM fundamentals – 🔴 🛠️
- Service identities and managed identities – 🔴 🛠️
- Cloud governance basics – 🟡 🛠️
- Tagging and naming strategies – 🟡 🛠️

---

# 3. Networking Fundamentals

- TCP/IP basics – 🔴 🛠️
- CIDR and subnetting – 🔴 🛠️
- VPC, VNet, Virtual Networks – 🔴 🛠️
- Public and private subnets – 🔴 🛠️
- Routing concepts – 🔴 🛠️
- NAT and gateways – 🟡 🛠️
- Security groups and firewall rules – 🔴 🛠️
- DNS fundamentals – 🔴 🛠️
- Load balancing concepts – 🟡 🛠️
- VPN and hybrid connectivity – 🟡 🛠️
- Network segmentation – 🟡 🛠️

---

# 4. Operating Systems and CLI

- Linux fundamentals – 🔴 🛠️
- Command-line navigation – 🔴 🛠️
- File management – 🔴 🛠️
- Environment variables – 🔴 📝 🛠️
- PATH concepts – 🔴
- Package management – 🔴
- SSH and key pairs – 🔴 🛠️
- Shell scripting basics – 🟡 🛠️
- curl and jq – 🟡 🛠️
- API interaction basics – 🟡 🛠️

---

# 5. Programming and Data Formats

- JSON – 🔴 📝 🛠️
- YAML – 🔴 🛠️
- Key-value structures – 🔴 📝
- Arrays and collections – 🔴 📝
- Maps and dictionaries – 🔴 📝
- Objects and nested structures – 🔴 📝
- Variables and parameters – 🔴 📝
- Expressions and interpolations – 🔴 📝
- Functions and reusable logic – 🟡 📝
- Loops and conditionals – 🟡 📝
- Error handling concepts – 🟡 🛠️

---

# 6. Version Control and Collaboration

- Git fundamentals – 🔴 🛠️
- Clone, commit, push, pull – 🔴 🛠️
- Branching strategies – 🟡 🛠️
- Merge and rebase awareness – 🟡 🛠️
- Pull requests – 🔴 🛠️
- Code review practices – 🔴 🛠️
- GitHub / GitLab / Azure Repos – 🔴 🛠️
- Semantic versioning – 🔴 📝 🛠️
- Release management – 🟡 🛠️
- .gitignore practices – 🔴 📝 🛠️

---

# 7. Security Foundations

- Least privilege principle – 🔴 📝 🛠️
- Identity and access management – 🔴 🛠️
- RBAC concepts – 🔴 🛠️
- Secrets management – 🔴 📝 🛠️
- API credentials handling – 🔴 📝 🛠️
- Managed identities – 🟡 🛠️
- Encryption at rest – 🟡 📝
- Encryption in transit – 🟡 📝
- State and secret exposure risks – 🔴 📝 🛠️
- Secret rotation concepts – 🟡 🛠️
- Compliance awareness – 🟡 🛠️
- Policy-as-Code concepts – 🟡 📝 🛠️

---

# 8. State, Dependency and Execution Concepts

- Dependency graphs – 🔴 📝
- Resource ordering – 🔴 📝
- Implicit dependencies – 🔴 📝
- Explicit dependencies – 🔴 📝
- Resource lifecycle – 🔴 📝 🛠️
- Create, update and destroy operations – 🔴 📝
- Parallel execution – 🟡 📝
- Execution planning – 🔴 🛠️
- Drift detection concepts – 🔴 🛠️

---

# 9. State Management and Backend Concepts

- Why state exists – 🔴 📝 🛠️
- Desired state management – 🔴 📝
- Local state storage – 🔴 🛠️
- Remote state storage – 🔴 🛠️
- State locking – 🔴 📝 🛠️
- State security – 🔴 🛠️
- State backup and versioning – 🔴 🛠️
- State migration – 🟡 🛠️
- Concurrency issues – 🟡 🛠️
- Blast radius reduction through state separation – 🔴 🛛️

---

# 10. DevOps and CI/CD Context

- DevOps lifecycle – 🔴
- CI pipeline concepts – 🔴 🛠️
- CD pipeline concepts – 🔴 🛠️
- GitOps principles – 🟡 🛠️
- Environment promotion strategies – 🔴 🛠️
- Approval workflows – 🟡 🛠️
- Pipeline security – 🟡 🛠️
- Infrastructure validation workflows – 🔴 🛠️
- Pipeline platforms:
  - GitHub Actions – 🟡 🛠️
  - Azure DevOps – 🟡 🛠️
  - GitLab CI/CD – 🟡 🛠️
  - Jenkins – 🟡 🛠️

---

# 11. Architecture-Level Design Concepts

- Modular architecture – 🔴 📝 🛠️
- Reusable component design – 🔴 🛠️
- DRY principle – 🔴 📝
- Environment isolation – 🔴 🛠️
- Multi-account strategies – 🔴 🛠️
- Multi-subscription strategies – 🔴 🛠️
- Landing zone concepts – 🟡 🛠️
- Governance and policy enforcement – 🟡 🛠️
- Auditability and compliance – 🟡 🛠️
- Cost management principles – 🟡 🛠️
- Disaster recovery considerations – 🟡 🛠️
- High availability architecture – 🟡 🛠️
- Platform engineering concepts – 🟡 🛠️
- Self-service infrastructure platforms – 🟡 🛠️

---

# 12. Cloud IaC Tools Architecture Comparison

## Terraform

### Strengths
- Multi-cloud standard
- Largest provider ecosystem
- Massive community adoption
- Mature module ecosystem
- Excellent enterprise support

### Best For
- Multi-cloud architecture
- Enterprise platform teams
- Cloud-agnostic deployments

### Architect Focus
- Provider design
- Module architecture
- State strategies
- Enterprise governance

---

## OpenTofu

### Strengths
- Open-source governance
- Terraform compatibility
- Community-driven roadmap
- Vendor-neutral approach

### Best For
- Organizations preferring fully open-source IaC
- Terraform migration compatibility
- Long-term vendor independence

### Architect Focus
- Migration planning
- Ecosystem evaluation
- Community provider strategy

---

## Bicep

### Strengths
- Native Azure experience
- First-class ARM integration
- Simplified Azure resource deployment

### Best For
- Azure-only environments
- Microsoft-centric organizations
- Azure landing zones

### Architect Focus
- Azure platform architecture
- Subscription and management group design
- Native Azure governance

---

## Pulumi

### Strengths
- Uses real programming languages
- Strong developer experience
- Software engineering practices

### Best For
- Developer-heavy organizations
- Complex business logic
- Cloud platform engineering

### Architect Focus
- Infrastructure SDK design
- Internal developer platforms
- Infrastructure abstractions

---

## CloudFormation

### Strengths
- Native AWS integration
- AWS feature parity
- Deep AWS ecosystem alignment

### Best For
- AWS-only organizations
- Highly regulated AWS environments

### Architect Focus
- AWS governance
- Account architecture
- Native AWS service adoption

---

# 13. Related Technologies

- Docker fundamentals – 🟡 🛠️
- Kubernetes fundamentals – 🟡 🛠️
- Helm basics – 🟡 🛠️
- Packer image creation – 🟡 🛠️
- Vault fundamentals – 🟡 🛠️
- Atlantis awareness – 🟡 🛠️
- Terragrunt awareness – 🟡 🛠️
- OPA (Open Policy Agent) awareness – 🟡 🛠️
- Crossplane awareness – 🟡 🛠️
- Platform Engineering concepts – 🟡 🛠️

---

# Suggested Learning Order

## Phase 1 – Core Foundations

1. IaC Fundamentals
2. Cloud Fundamentals
3. Networking Fundamentals
4. Linux and CLI
5. Git Fundamentals

## Phase 2 – IaC Engineering

6. JSON, YAML and Programming Concepts
7. Security and Secrets
8. Dependency Graphs
9. State Management
10. CI/CD Pipelines

## Phase 3 – Tool Mastery

11. Terraform
12. OpenTofu
13. Bicep
14. Pulumi
15. CloudFormation

## Phase 4 – Architecture

16. Module Design
17. Multi-Environment Strategies
18. Multi-Account Architecture
19. Governance and Compliance
20. Platform Engineering

## Phase 5 – Architect Mindset

21. Cost Optimization
22. Disaster Recovery
23. Enterprise Landing Zones
24. Self-Service Platforms
25. Cloud IaC Strategy and Tool Selection

---

# Architect Rule of Thumb

**Don't become a Terraform Architect, OpenTofu Architect, Bicep Architect, or Pulumi Architect.**

Become a **Cloud IaC Architect** who understands:

- Infrastructure abstraction
- State management
- Modular design
- Platform engineering
- Multi-cloud strategy
- Governance and compliance
- DevOps and GitOps
- Cost and risk management

Tools evolve. Architectural principles endure.

A senior Cloud Architect should be able to explain *why* a solution should use Terraform, OpenTofu, Bicep, Pulumi, or CloudFormation, not just *how* to write the code.
