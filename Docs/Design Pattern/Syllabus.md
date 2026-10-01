# Cloud Architect Prerequisites: Microservice Design Patterns, Cloud Native & DevOps Tools

**Level:** Architect

**Legend:** `R` = Required | `O` = Optional | `E` = Exam-oriented | `L` = Real-life use

---

## 1. Architecture Foundations

| Topic | Flags |
|---|---|
| Monolith vs SOA vs Microservices | `R` `E` `L` |
| Domain-Driven Design (bounded context, aggregate, ubiquitous language) | `R` `E` `L` |
| Twelve-Factor App | `R` `E` `L` |
| CAP theorem / PACELC | `R` `E` |
| Eventual vs strong consistency | `R` `E` `L` |
| Scalability (horizontal/vertical), availability, resilience, fault tolerance | `R` `E` `L` |
| SLI / SLO / SLA / error budget | `R` `E` `L` |
| Stateless vs stateful services | `R` `E` `L` |
| Coupling and cohesion | `R` `E` |
| Conway's Law | `O` `E` |
| Well-Architected pillars (AWS / Azure / GCP) | `R` `E` `L` |

---

## 2. Microservice Design Patterns

### Decomposition
| Topic | Flags |
|---|---|
| Decompose by business capability / subdomain | `R` `E` `L` |
| Strangler Fig | `R` `E` `L` |
| Anti-Corruption Layer | `O` `E` |

### Data
| Topic | Flags |
|---|---|
| Database per Service | `R` `E` `L` |
| Saga (choreography vs orchestration) | `R` `E` `L` |
| CQRS | `R` `E` `L` |
| Event Sourcing | `O` `E` |
| Transactional Outbox | `O` `L` |
| Shared database (anti-pattern) | `E` |

### Integration / Communication
| Topic | Flags |
|---|---|
| API Gateway | `R` `E` `L` |
| Backend for Frontend (BFF) | `O` `E` `L` |
| Aggregator / Gateway Aggregation | `O` `E` |
| Service Discovery (client-side / server-side) | `R` `E` `L` |
| Sync vs async communication | `R` `E` `L` |
| Pub/Sub, event-driven architecture | `R` `E` `L` |
| Message queue vs event stream | `R` `E` `L` |
| Idempotency, at-least-once / exactly-once delivery | `R` `L` |

### Resilience
| Topic | Flags |
|---|---|
| Circuit Breaker | `R` `E` `L` |
| Retry with backoff + jitter | `R` `L` |
| Timeout | `R` `L` |
| Bulkhead | `R` `E` `L` |
| Rate limiting / throttling | `R` `L` |
| Health checks (liveness / readiness) | `R` `E` `L` |

### Deployment / Structure
| Topic | Flags |
|---|---|
| Sidecar | `R` `E` `L` |
| Ambassador | `O` `E` |
| Adapter | `O` |
| Service Mesh | `R` `E` `L` |
| Blue-Green, Canary, Rolling deployment | `R` `E` `L` |
| Feature flags | `O` `L` |

### Observability
| Topic | Flags |
|---|---|
| Log aggregation, distributed tracing, metrics | `R` `E` `L` |
| Correlation ID | `R` `L` |

### Cross-cutting
| Topic | Flags |
|---|---|
| Externalized configuration | `R` `L` |
| Secrets management | `R` `L` |

---

## 3. Cloud Native Core

| Topic | Flags |
|---|---|
| Containers (image, registry, layers, runtime) | `R` `E` `L` |
| Kubernetes (Pod, Deployment, Service, Ingress, ConfigMap, Secret, HPA, StatefulSet, Namespace) | `R` `E` `L` |
| Container orchestration concepts | `R` `E` |
| Immutable infrastructure | `R` `E` `L` |
| Infrastructure as Code | `R` `E` `L` |
| Serverless / FaaS | `R` `E` `L` |
| IaaS / PaaS / CaaS / SaaS | `R` `E` |
| Autoscaling and elasticity | `R` `E` `L` |
| Multi-AZ / multi-region design | `R` `E` `L` |
| Disaster recovery (RTO, RPO, backup/restore, pilot light, warm standby, active-active) | `R` `E` `L` |
| CNCF landscape awareness | `O` `E` |
| OpenTelemetry | `O` `L` |
| Service mesh (Istio, Linkerd) | `O` `E` `L` |
| Zero trust, mTLS | `R` `E` `L` |
| Multi-cloud / hybrid cloud | `O` `E` |
| Cost optimization / FinOps basics | `R` `E` `L` |

---

## 4. DevOps Concepts

| Topic | Flags |
|---|---|
| CI/CD pipeline stages | `R` `E` `L` |
| Continuous Delivery vs Continuous Deployment | `R` `E` |
| GitOps | `R` `E` `L` |
| Trunk-based development, branching strategies | `R` `L` |
| Shift-left testing, testing pyramid | `R` `E` |
| DevSecOps (SAST, DAST, SCA, image scanning) | `R` `E` `L` |
| Artifact management | `R` `L` |
| Configuration management | `R` `E` |
| Environment promotion (dev / test / stage / prod) | `R` `L` |
| DORA metrics | `R` `E` |
| SRE basics (toil, postmortem, on-call) | `O` `E` `L` |
| Release strategies and rollback | `R` `E` `L` |
| Policy as Code | `O` `L` |

---

## 5. DevOps Tools (by category)

| Category | Tools | Flags |
|---|---|---|
| Source control | Git, GitHub / GitLab | `R` `L` |
| CI/CD | Jenkins, GitHub Actions, GitLab CI, Azure DevOps | `R` `E` `L` |
| GitOps | ArgoCD, Flux | `R` `L` |
| IaC | Terraform | `R` `E` `L` |
| IaC (cloud-native) | CloudFormation, Bicep, ARM | `O` `E` |
| Config management | Ansible | `R` `L` |
| Containers | Docker | `R` `E` `L` |
| Orchestration | Kubernetes | `R` `E` `L` |
| Packaging | Helm, Kustomize | `R` `L` |
| Monitoring | Prometheus, Grafana | `R` `L` |
| Logging | ELK/EFK, Loki, CloudWatch, Azure Monitor | `R` `L` |
| Tracing | Jaeger, Zipkin, X-Ray | `O` `L` |
| Security scanning | Trivy, SonarQube | `O` `L` |
| Secrets | HashiCorp Vault, cloud key vaults | `R` `L` |
| Messaging | Kafka, RabbitMQ, SQS/SNS, Service Bus, Event Hub | `R` `E` `L` |
| Caching | Redis | `R` `L` |
| API management | Kong, Apigee, API Gateway, APIM | `O` `E` `L` |
| Chaos engineering | Chaos Monkey, Litmus | `O` |
| Image building | Packer | `O` |

---

## 6. Architect-Level Skills

| Topic | Flags |
|---|---|
| Trade-off analysis (consistency / availability / cost / complexity) | `R` `E` `L` |
| Architecture Decision Records (ADR) | `R` `L` |
| Reference architectures | `R` `E` |
| Non-functional requirements (performance, security, compliance, availability) | `R` `E` `L` |
| Security design (IAM, least privilege, network segmentation, encryption at rest / in transit) | `R` `E` `L` |
| Networking basics (VPC/VNet, subnets, NAT, load balancers, DNS, CDN, peering) | `R` `E` `L` |
| API design (REST, gRPC, GraphQL, versioning, OpenAPI) | `R` `E` `L` |
| Data stores (relational, NoSQL types, polyglot persistence) | `R` `E` `L` |
| Cost and capacity planning | `R` `E` `L` |
| Migration strategies (6 Rs: rehost, replatform, refactor, etc.) | `R` `E` `L` |
| Governance, compliance, landing zones | `O` `E` `L` |
| Anti-patterns (distributed monolith, chatty services, shared DB) | `R` `E` |

---

## Suggested Study Order

1. Section 1: Architecture Foundations
2. Section 3: Cloud Native Core (containers, Kubernetes first)
3. Section 2: Microservice Design Patterns
4. Section 4: DevOps Concepts
5. Section 5: DevOps Tools
6. Section 6: Architect-Level Skills