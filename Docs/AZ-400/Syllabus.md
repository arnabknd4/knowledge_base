# AZ-400 (Azure DevOps Engineer Expert): Prerequisite Topics (Architect Level)

**Flags:** R = Required | O = Optional | E = Exam oriented | L = Real-life use

---

## 1. DevOps Foundations
| Topic | Flag |
|---|---|
| DevOps culture & principles (CALMS) | R, E |
| SDLC models (Agile, Scrum, Kanban) | R, E |
| CI / CD / Continuous Deployment | R, E, L |
| Shift-left (testing & security) | R, E |
| DORA metrics | E, L |
| Value stream mapping | O, E |
| Release strategies (blue-green, canary, ring, feature flags, A/B) | R, E, L |
| Technical debt | O |

## 2. Azure Fundamentals (Prerequisite Layer)
| Topic | Flag |
|---|---|
| Entra ID (users, groups, service principals, managed identities) | R, E, L |
| RBAC & Azure Policy | R, E, L |
| Management groups, subscriptions, resource groups | R, E |
| Azure Resource Manager (ARM) | R, E |
| Azure networking basics (VNet, NSG, Private Endpoint) | R, L |
| Azure Key Vault | R, E, L |
| Azure Storage (Blob, Artifacts storage) | O |
| Azure Monitor / Log Analytics | R, E, L |

## 3. Source Control
| Topic | Flag |
|---|---|
| Git fundamentals (commit, branch, merge, rebase, cherry-pick) | R, L |
| Branching strategies (GitFlow, GitHub Flow, Trunk-based) | R, E, L |
| Pull requests & branch policies | R, E, L |
| Git hooks | O |
| Monorepo vs multi-repo | R, E |
| Large file handling (Git LFS, Scalar) | O, E |
| Repo permissions & security | R, E |
| Azure Repos vs GitHub | R, E |
| Inner source / fork workflow | O, E |

## 4. Azure DevOps Services
| Topic | Flag |
|---|---|
| Organization, project, team structure | R, E |
| Azure Boards (work items, backlogs, sprints, queries) | R, E, L |
| Azure Repos | R, E |
| Azure Pipelines | R, E, L |
| Azure Artifacts | R, E, L |
| Azure Test Plans | E, O |
| Dashboards, widgets, analytics views | O, E |
| Wikis & documentation | O |
| Service connections | R, E, L |
| Permissions, security groups, access levels | R, E, L |
| Azure DevOps vs GitHub Enterprise | R, E |
| Boards–GitHub integration | E, L |

## 5. Pipelines (CI/CD)
| Topic | Flag |
|---|---|
| YAML pipelines vs Classic | R, E |
| Pipeline structure (stages, jobs, steps, tasks) | R, E, L |
| Triggers (CI, PR, scheduled, pipeline resource) | R, E, L |
| Variables, variable groups, secrets | R, E, L |
| Templates (step, job, stage, extends) | R, E, L |
| Agents (Microsoft-hosted vs self-hosted, scale set agents) | R, E, L |
| Agent pools | R, E |
| Environments, approvals & checks | R, E, L |
| Deployment jobs & strategies | R, E |
| Multi-stage pipelines | R, E, L |
| Pipeline caching | O, L |
| Parallel jobs & concurrency | E, L |
| Conditions & expressions | R, L |
| Pipeline resources & artifacts | R, E |
| Release pipelines (Classic) | O, E |
| GitHub Actions basics (workflows, runners, secrets, reusable workflows) | R, E, L |

## 6. Build & Test
| Topic | Flag |
|---|---|
| Build systems (Maven, Gradle, npm, .NET) | O, L |
| Package management (NuGet, npm, Maven, PyPI) | R, E |
| Package feeds, upstream sources, views | R, E, L |
| Versioning (SemVer, CalVer) | R, E |
| Test types (unit, integration, load, UI) | R, E |
| Code coverage | E, L |
| Flaky test handling | O, L |
| Load testing (Azure Load Testing) | O, E |

## 7. Infrastructure as Code & Configuration
| Topic | Flag |
|---|---|
| IaC concepts (declarative vs imperative, idempotency) | R, E |
| ARM templates | R, E |
| Bicep | R, E, L |
| Terraform (basics) | O, L |
| Desired State Configuration (DSC) | O, E |
| Azure Automation | O, E |
| Ansible (overview) | O |
| Azure App Configuration | E, L |
| Azure Deployment Environments | O |
| Configuration drift | R, E |

## 8. Containers & Compute
| Topic | Flag |
|---|---|
| Docker (image, Dockerfile, registry) | R, E, L |
| Azure Container Registry (ACR) | R, E, L |
| AKS (basics) | R, E, L |
| Helm (overview) | O, L |
| Azure App Service (slots) | R, E, L |
| Azure Functions | O, E |
| Azure Container Apps / Instances | O, E |
| Virtual machines & scale sets | O, L |
| GitOps (concept, Flux) | O, E |

## 9. Security & Compliance (DevSecOps)
| Topic | Flag |
|---|---|
| DevSecOps principles | R, E |
| Secrets management | R, E, L |
| Managed identities & workload identity federation | R, E, L |
| SAST / DAST / SCA | R, E, L |
| Dependency scanning (Dependabot) | R, E, L |
| GitHub Advanced Security (code scanning, secret scanning) | R, E, L |
| Microsoft Defender for Cloud / DevOps | R, E |
| Container image scanning | E, L |
| Software supply chain security (SBOM, signing) | O, E |
| Open-source license compliance | E |
| Azure Policy for compliance | R, E |
| Least privilege & just-in-time access | R, E |

## 10. Monitoring, Feedback & Operations
| Topic | Flag |
|---|---|
| Application Insights | R, E, L |
| Azure Monitor (metrics, alerts, action groups) | R, E, L |
| Log Analytics & KQL (basics) | R, E, L |
| Dashboards & Workbooks | E, L |
| Distributed tracing | O, E |
| Alert strategy & noise reduction | E, L |
| SRE concepts (SLI, SLO, SLA, error budget) | R, E |
| Incident management & postmortems | O, L |
| Feedback loops (user telemetry, feature usage) | E |
| Availability tests | E, L |

## 11. Architecture & Governance (Architect Lens)
| Topic | Flag |
|---|---|
| Enterprise DevOps strategy | R, E |
| Pipeline governance at scale | R, E, L |
| Azure DevOps organization design (single vs multiple org/project) | R, E, L |
| Landing zones (CI/CD perspective) | O, E |
| Multi-environment promotion strategy | R, E, L |
| Zero-downtime deployment design | R, E |
| Rollback & recovery patterns | R, E, L |
| Cost management of pipelines & agents | O, L |
| Migration (TFS / Jenkins / GitHub to Azure DevOps) | O, E, L |
| Compliance & audit trails | E, L |
| Team topologies & collaboration | O, E |
| Platform engineering concept | O, L |

## 12. Adjacent Tools (Know the Names Only)
| Topic | Flag |
|---|---|
| Jenkins | O, L |
| SonarQube / SonarCloud | E, L |
| WhiteSource / Mend | O, E |
| Chef / Puppet | O, E |
| Slack / Teams integration | O, L |
| Microsoft Copilot in DevOps | O |