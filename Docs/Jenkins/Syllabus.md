# Jenkins (DevOps): Architect-Level Prerequisites

**Legend:** 🔴 Required | 🟡 Optional | 📝 Exam-oriented | 🛠️ Real-life use

---

## 1. CI/CD Foundations
| Topic | Flag |
|---|---|
| CI vs Continuous Delivery vs Continuous Deployment | 🔴 📝 🛠️ |
| Build, Test, Release, Deploy stages | 🔴 📝 🛠️ |
| Pipeline as Code | 🔴 📝 🛠️ |
| Artifacts & Artifact Repositories | 🔴 🛠️ |
| Build Triggers (SCM, Webhook, Cron) | 🔴 📝 🛠️ |
| Deployment Strategies (Blue-Green, Canary, Rolling) | 🟡 📝 🛠️ |
| Shift-Left Testing | 🟡 📝 |

## 2. Version Control (Git)
| Topic | Flag |
|---|---|
| Git Basics (commit, branch, merge, rebase) | 🔴 🛠️ |
| Branching Strategies (GitFlow, Trunk-Based) | 🔴 📝 🛠️ |
| Webhooks | 🔴 🛠️ |
| Multibranch Workflow | 🔴 📝 🛠️ |
| Monorepo vs Polyrepo | 🟡 🛠️ |
| Git Submodules | 🟡 |

## 3. Build Tools & Languages
| Topic | Flag |
|---|---|
| Maven / Gradle | 🔴 🛠️ |
| npm / Yarn | 🟡 🛠️ |
| pip / Python build | 🟡 🛠️ |
| Dependency Management | 🔴 🛠️ |
| Unit Testing Frameworks | 🟡 🛠️ |

## 4. Linux & Scripting
| Topic | Flag |
|---|---|
| Linux Basics (users, permissions, processes, services) | 🔴 🛠️ |
| Shell / Bash Scripting | 🔴 🛠️ |
| SSH & Key Management | 🔴 📝 🛠️ |
| Cron | 🟡 🛠️ |
| Systemd | 🟡 🛠️ |

## 5. Groovy & Pipeline Syntax
| Topic | Flag |
|---|---|
| Groovy Basics | 🔴 🛠️ |
| Declarative vs Scripted Pipeline | 🔴 📝 🛠️ |
| Jenkinsfile | 🔴 📝 🛠️ |
| Shared Libraries | 🔴 📝 🛠️ |
| Groovy Sandbox & Script Approval | 🟡 📝 |
| YAML / JSON | 🔴 🛠️ |

## 6. Jenkins Architecture
| Topic | Flag |
|---|---|
| Controller (Master) | 🔴 📝 🛠️ |
| Agents (Nodes) | 🔴 📝 🛠️ |
| Executors | 🔴 📝 |
| Labels | 🔴 🛠️ |
| Agent Types (SSH, Inbound/JNLP, Docker, Kubernetes) | 🔴 📝 🛠️ |
| Distributed Builds | 🔴 📝 🛠️ |
| Jenkins Home Directory | 🔴 📝 🛠️ |
| Workspace | 🔴 📝 |
| Queue & Build Lifecycle | 🟡 📝 |

## 7. Job Types
| Topic | Flag |
|---|---|
| Freestyle Job | 🔴 📝 |
| Pipeline Job | 🔴 📝 🛠️ |
| Multibranch Pipeline | 🔴 📝 🛠️ |
| Organization Folder | 🟡 📝 🛠️ |
| Folders & Views | 🟡 🛠️ |
| Parameterized Builds | 🔴 📝 🛠️ |

## 8. Plugins
| Topic | Flag |
|---|---|
| Plugin Manager | 🔴 📝 🛠️ |
| Plugin Dependency & Compatibility | 🔴 🛠️ |
| Core Plugins (Git, Pipeline, Credentials, Blue Ocean) | 🔴 📝 🛠️ |
| Plugin Security Risks | 🟡 📝 🛠️ |

## 9. Security
| Topic | Flag |
|---|---|
| Authentication vs Authorization | 🔴 📝 🛠️ |
| Credentials Management | 🔴 📝 🛠️ |
| RBAC / Matrix-Based Security | 🔴 📝 🛠️ |
| LDAP / SSO / SAML / OIDC | 🟡 📝 🛠️ |
| Secrets Management (Vault) | 🟡 📝 🛠️ |
| CSRF Protection | 🟡 📝 |
| Agent-to-Controller Security | 🟡 📝 |
| Audit Logging | 🟡 🛠️ |

## 10. Containers & Orchestration
| Topic | Flag |
|---|---|
| Docker Basics (image, container, Dockerfile, registry) | 🔴 🛠️ |
| Docker-in-Docker / Docker Socket | 🟡 🛠️ |
| Kubernetes Basics (pod, deployment, service) | 🔴 🛠️ |
| Jenkins on Kubernetes | 🟡 📝 🛠️ |
| Helm | 🟡 🛠️ |

## 11. Infrastructure & Config Management
| Topic | Flag |
|---|---|
| Infrastructure as Code (Terraform) | 🟡 🛠️ |
| Configuration Management (Ansible) | 🟡 🛠️ |
| Jenkins Configuration as Code (JCasC) | 🔴 📝 🛠️ |
| Environment Promotion (Dev/QA/Stage/Prod) | 🔴 🛠️ |

## 12. Quality & Security Gates
| Topic | Flag |
|---|---|
| SonarQube / Static Analysis | 🟡 📝 🛠️ |
| SAST / DAST / SCA | 🟡 📝 🛠️ |
| Code Coverage | 🟡 🛠️ |
| Quality Gates | 🟡 📝 🛠️ |
| Artifact Repos (Nexus, Artifactory) | 🟡 🛠️ |
| Container Image Scanning | 🟡 🛠️ |

## 13. Networking & Web Basics
| Topic | Flag |
|---|---|
| HTTP/HTTPS, Ports | 🔴 🛠️ |
| Reverse Proxy (Nginx) | 🟡 🛠️ |
| SSL/TLS Certificates | 🟡 🛠️ |
| DNS & Firewalls | 🟡 🛠️ |

## 14. Cloud Basics
| Topic | Flag |
|---|---|
| Cloud Compute (EC2, VM) | 🟡 🛠️ |
| IAM Basics | 🟡 📝 🛠️ |
| Cloud Storage (S3) | 🟡 🛠️ |
| Autoscaling Agents | 🟡 🛠️ |

## 15. Operations & Observability
| Topic | Flag |
|---|---|
| Backup & Restore | 🔴 📝 🛠️ |
| High Availability & Scaling | 🔴 📝 🛠️ |
| Jenkins Upgrades (LTS vs Weekly) | 🔴 📝 🛠️ |
| Logging & Monitoring (Prometheus, Grafana) | 🟡 🛠️ |
| Build Notifications (Slack, Email) | 🟡 🛠️ |
| Performance Tuning (JVM, GC) | 🟡 📝 🛠️ |
| Disaster Recovery | 🟡 📝 🛠️ |

## 16. Related DevOps Concepts
| Topic | Flag |
|---|---|
| GitOps (vs Jenkins push model) | 🟡 📝 |
| Jenkins vs GitHub Actions vs GitLab CI | 🟡 📝 🛠️ |
| DevSecOps | 🟡 📝 🛠️ |
| DORA Metrics | 🟡 📝 |
| Release Management | 🟡 🛠️ |

---

**Suggested study order (architect level):** 1 → 2 → 4 → 6 → 5 → 7 → 9 → 15 → 10 → 11, then the optional sections as needed.