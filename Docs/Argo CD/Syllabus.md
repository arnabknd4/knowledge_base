# ArgoCD Prerequisites: Architect Level

**Legend:** R = Required | O = Optional | E = Exam-oriented | L = Real-life use

## 1. Git & Source Control
| Topic | Flag |
|---|---|
| Git fundamentals (commit, branch, merge, tag) | R, E, L |
| Branching strategies (trunk-based, GitFlow) | R, E, L |
| Pull/Merge Request workflow | R, L |
| Git webhooks | R, L |
| Monorepo vs Polyrepo | E, L |
| Git signing (GPG commit verification) | O, L |

## 2. Kubernetes Fundamentals
| Topic | Flag |
|---|---|
| Pod, Deployment, ReplicaSet, StatefulSet, DaemonSet | R, E, L |
| Service, Ingress | R, E, L |
| ConfigMap, Secret | R, E, L |
| Namespace | R, E, L |
| Labels, Selectors, Annotations | R, E, L |
| Kubernetes Manifests (YAML) | R, E, L |
| Custom Resource Definition (CRD) | R, E, L |
| Controller / Operator pattern | R, E |
| Reconciliation loop | R, E |
| RBAC (Role, ClusterRole, ServiceAccount) | R, E, L |
| kubeconfig, Contexts, Clusters | R, L |
| Health probes (liveness, readiness) | R, L |
| Resource quotas, Limits | O, L |
| Admission controllers | O, E |

## 3. Packaging & Templating
| Topic | Flag |
|---|---|
| Helm (chart, values, release) | R, E, L |
| Kustomize (base, overlay, patches) | R, E, L |
| Plain YAML / Directory of manifests | R |
| Jsonnet | O |
| Config Management Plugins | O, L |

## 4. GitOps Concepts
| Topic | Flag |
|---|---|
| GitOps principles | R, E |
| Declarative vs Imperative | R, E |
| Desired state vs Live state | R, E |
| Pull-based vs Push-based deployment | R, E, L |
| Drift detection | R, E, L |
| Single source of truth | R, E |
| Progressive delivery | E, L |
| Rollback via Git revert | R, L |

## 5. CI/CD Basics
| Topic | Flag |
|---|---|
| CI vs CD vs Continuous Deployment | R, E |
| CI tools (Jenkins, GitHub Actions, GitLab CI) | R, L |
| Image build and registry push | R, L |
| Container registry (ECR, ACR, GCR, Docker Hub) | R, L |
| Image tagging strategy (immutable tags, digests) | R, E, L |
| Separation of app repo and config repo | R, E, L |
| Image updater automation | O, L |

## 6. Deployment Strategies
| Topic | Flag |
|---|---|
| Rolling update | R, E |
| Blue-Green | R, E, L |
| Canary | R, E, L |
| Recreate | O, E |
| Argo Rollouts | O, L |

## 7. Secrets & Security
| Topic | Flag |
|---|---|
| Kubernetes Secrets limitations | R, E |
| Sealed Secrets | R, L |
| External Secrets Operator | R, L |
| HashiCorp Vault | O, L |
| SOPS | O, L |
| Least privilege | R, E |
| SSO / OIDC / SAML | R, L |
| TLS / Certificates | R, L |
| Network Policies | O, E |
| Policy as Code (OPA Gatekeeper, Kyverno) | O, E, L |

## 8. Multi-Cluster & Multi-Environment
| Topic | Flag |
|---|---|
| Environment promotion (dev, staging, prod) | R, E, L |
| Multi-cluster management | R, E, L |
| Hub-and-spoke model | E, L |
| Cluster registration and credentials | R, L |
| Multi-tenancy | E, L |

## 9. Core ArgoCD Terms (Know Before Deep Dive)
| Topic | Flag |
|---|---|
| Application (CRD) | R, E, L |
| AppProject | R, E, L |
| ApplicationSet | R, E, L |
| Sync (manual vs automated) | R, E, L |
| Sync status vs Health status | R, E |
| Sync policy (prune, self-heal) | R, E, L |
| Sync waves and Hooks | R, E, L |
| Refresh vs Hard Refresh | E, L |
| Repository / Credentials | R, L |
| Source types (Git, Helm, OCI) | R, E |
| Target revision | R |
| Ignore differences | E, L |
| Resource tracking (label vs annotation) | O, E |
| App of Apps pattern | R, E, L |

## 10. ArgoCD Architecture
| Topic | Flag |
|---|---|
| API Server | R, E |
| Repo Server | R, E |
| Application Controller | R, E |
| Redis | O, E |
| Dex (SSO) | O, E |
| Notifications controller | O, L |
| ApplicationSet controller | E |
| HA setup | E, L |
| CLI and UI | R, L |

## 11. Observability & Operations
| Topic | Flag |
|---|---|
| Prometheus and Grafana metrics | O, L |
| Logging and Audit | O, L |
| Notifications (Slack, email, webhook) | O, L |
| Disaster recovery and backup | E, L |
| Upgrade strategy | O, L |

## 12. Cloud & Infrastructure Context
| Topic | Flag |
|---|---|
| Managed Kubernetes (EKS, AKS, GKE) | R, L |
| Infrastructure as Code (Terraform) | O, L |
| Cluster bootstrapping | O, L |
| Service Mesh (Istio) | O |

## 13. Architect-Level Decision Topics
| Topic | Flag |
|---|---|
| ArgoCD vs Flux | E, L |
| GitOps vs traditional CI/CD push | E, L |
| Repo structure design | E, L |
| Scaling ArgoCD (sharding) | E, L |
| Governance and compliance via GitOps | E, L |
| Auditability and change traceability | E, L |

**Suggested study order:** 1 → 2 → 3 → 4 → 5 → 9 → 10 → 7 → 8 → 6 → 11 → 13 (12 as needed)