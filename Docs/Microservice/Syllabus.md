# Microservice Design: Architect-Level Prerequisites

**Legend:** **R** = Required · **O** = Optional · **E** = Exam-oriented · **L** = Real-life use

---

## 1. Foundations
| Topic | Flag |
|---|---|
| Monolith vs Modular Monolith vs Microservices | R, E, L |
| SOA vs Microservices | E |
| Distributed systems basics | R |
| CAP theorem | R, E |
| PACELC | O, E |
| Consistency models (strong, eventual) | R, E, L |
| Fallacies of distributed computing | E |
| Scalability (horizontal/vertical) | R, L |
| High availability, fault tolerance, resiliency | R, L |
| Latency vs throughput | R |
| SLA / SLO / SLI | R, L |
| 12-Factor App | R, E, L |
| Conway's Law | E |
| Idempotency | R, E, L |
| Stateless vs stateful services | R, E |

## 2. Design Principles & Domain Modeling
| Topic | Flag |
|---|---|
| Domain-Driven Design (Bounded Context, Aggregate, Entity, Value Object, Ubiquitous Language, Context Map) | R, E |
| Service decomposition (by business capability / subdomain) | R, E |
| Coupling & cohesion | R |
| SOLID | R |
| Database per service | R, E |
| Event Storming | O, L |
| Hexagonal / Clean Architecture | O, L |
| API-first design | R, L |

## 3. Communication
| Topic | Flag |
|---|---|
| REST | R, E, L |
| gRPC | R, E, L |
| GraphQL | O, L |
| WebSockets / SSE | O |
| Sync vs Async communication | R, E |
| Message queue vs Event streaming | R, E |
| Pub/Sub, Request-Reply | R, E |
| HTTP/1.1 vs HTTP/2, TLS, DNS | R |
| JSON, Protobuf | R |
| Avro | O |
| OpenAPI | R |
| AsyncAPI | O |
| API versioning | R, E, L |

## 4. Design Patterns

### Decomposition / Migration
| Pattern | Flag |
|---|---|
| Strangler Fig | R, E, L |
| Decompose by Business Capability / Subdomain | R, E |
| Anti-Corruption Layer | R, E |

### Data Management
| Pattern | Flag |
|---|---|
| Database per Service | R, E |
| Saga (choreography / orchestration) | R, E, L |
| CQRS | R, E, L |
| Event Sourcing | R, E |
| Transactional Outbox | R, E, L |
| API Composition | R, E |
| Change Data Capture | O, L |
| Shared Database (anti-pattern) | E |
| 2PC / Distributed Transactions (anti-pattern) | E |

### Integration / Routing
| Pattern | Flag |
|---|---|
| API Gateway | R, E, L |
| Backend for Frontend (BFF) | R, E, L |
| Aggregator / Gateway Routing / Gateway Offloading | E |
| Sidecar | R, E, L |
| Ambassador | O, E |
| Service Mesh | R, E, L |

### Reliability
| Pattern | Flag |
|---|---|
| Circuit Breaker | R, E, L |
| Retry + Exponential Backoff + Jitter | R, E, L |
| Timeout | R, L |
| Bulkhead | R, E |
| Rate Limiting / Throttling | R, L |
| Fallback | R, L |
| Dead Letter Queue | R, L |
| Idempotent Consumer | R, E |
| Health Check API | R, L |
| Leader Election | O, E |

### Discovery & Config
| Pattern | Flag |
|---|---|
| Client-side / Server-side Discovery | R, E |
| Service Registry | R, E |
| Externalized Configuration | R, E, L |

### Observability
| Pattern | Flag |
|---|---|
| Distributed Tracing | R, E, L |
| Log Aggregation | R, E, L |
| Metrics / Health Metrics | R, L |
| Correlation ID | R, L |

### Deployment
| Pattern | Flag |
|---|---|
| Blue-Green | R, E, L |
| Canary | R, E, L |
| Rolling Update | R, L |
| Feature Flags | O, L |
| Immutable Infrastructure | E |
| Service per Container | R, E |

### Security
| Pattern | Flag |
|---|---|
| Access Token | R, E |
| API Key | O |
| Zero Trust | E |

## 5. Data
| Topic | Flag |
|---|---|
| ACID vs BASE | R, E |
| SQL vs NoSQL types (KV, document, column, graph) | R, E |
| Polyglot persistence | R, E |
| Caching strategies (cache-aside, write-through, write-behind) | R, E, L |
| Sharding, Replication, Partitioning | R, E |
| Read replicas | L |

## 6. Security
| Topic | Flag |
|---|---|
| AuthN vs AuthZ | R |
| OAuth 2.0 | R, E, L |
| OpenID Connect | R, E, L |
| JWT | R, E, L |
| RBAC / ABAC | R, E |
| mTLS | R, E, L |
| Secrets management | R, L |
| OWASP API Top 10 | E, L |
| SAML | O |
| API security (gateway auth, WAF) | R, L |

## 7. Observability
| Topic | Flag |
|---|---|
| Logs / Metrics / Traces (three pillars) | R, E |
| OpenTelemetry | R, L |
| Alerting, Dashboards | L |

## 8. DevOps & Delivery
| Topic | Flag |
|---|---|
| Docker / Containers | R, L |
| Kubernetes | R, E, L |
| Helm | R, L |
| CI/CD | R, E, L |
| GitOps | O, L |
| Infrastructure as Code | R, L |
| Testing pyramid, Contract Testing, Consumer-driven contracts | R, E |
| Trunk-based development / Git branching | O, L |

## 9. Tools

### Messaging / Streaming
| Tool | Flag |
|---|---|
| Kafka | R, E, L |
| RabbitMQ | R, E, L |
| NATS | O |
| Pulsar | O |
| ActiveMQ | O |

### API Gateway
| Tool | Flag |
|---|---|
| Kong | R, L |
| NGINX | R, L |
| Apigee | O, L |
| Spring Cloud Gateway | O |
| Traefik | O |

### Service Mesh / Proxy
| Tool | Flag |
|---|---|
| Istio | R, E, L |
| Linkerd | O |
| Envoy | R, E, L |

### Frameworks (pick one stack, know others by name)
| Tool | Flag |
|---|---|
| Spring Boot / Spring Cloud | R, L |
| Node.js / NestJS | O, L |
| .NET | O, L |
| Go | O, L |
| FastAPI | O, L |
| Quarkus / Micronaut | O |
| Dapr | O |

### Resilience / Discovery / Config
| Tool | Flag |
|---|---|
| Resilience4j | R, L |
| Polly | O |
| Hystrix (deprecated) | E |
| Consul | R, L |
| Eureka | O, E |
| etcd | O |
| Spring Cloud Config | O |

### Workflow / Orchestration
| Tool | Flag |
|---|---|
| Temporal | O, L |
| Camunda | O |
| Netflix Conductor | O |

### Identity / Secrets
| Tool | Flag |
|---|---|
| Keycloak | R, L |
| Auth0 / Okta | O, L |
| HashiCorp Vault | R, L |

### Observability
| Tool | Flag |
|---|---|
| Prometheus | R, E, L |
| Grafana | R, L |
| ELK / EFK | R, E, L |
| Jaeger / Zipkin | R, E, L |
| Loki | O |
| Datadog / New Relic | O, L |

### Testing / Docs
| Tool | Flag |
|---|---|
| Pact | R, E |
| Postman | R, L |
| WireMock | O |
| k6 / JMeter | O, L |
| Swagger UI | R, L |

### DevOps
| Tool | Flag |
|---|---|
| Terraform | R, L |
| ArgoCD | O, L |
| Jenkins / GitHub Actions / GitLab CI | R, L |

## 10. Cloud Offerings
| Area | AWS | Azure | GCP | Flag |
|---|---|---|---|---|
| Containers | ECS, EKS, Fargate | AKS, Container Apps | GKE, Cloud Run | R, E, L |
| Serverless | Lambda | Functions | Cloud Functions | R, E, L |
| API Gateway | API Gateway | API Management | Apigee, API Gateway | R, E, L |
| Queue / Pub-Sub | SQS, SNS | Service Bus, Event Grid | Pub/Sub | R, E, L |
| Event bus | EventBridge | Event Grid | Eventarc | R, E |
| Streaming | MSK, Kinesis | Event Hubs | Pub/Sub, Dataflow | R, E, L |
| Workflow | Step Functions | Logic Apps, Durable Functions | Workflows | R, E |
| Service mesh | ECS Service Connect (App Mesh: discontinued) | Istio add-on for AKS | Cloud Service Mesh | O, E |
| Databases | DynamoDB, Aurora, RDS | Cosmos DB, Azure SQL | Spanner, Firestore, Cloud SQL | R, E, L |
| Cache | ElastiCache | Azure Cache for Redis | Memorystore | R, L |
| Load balancing | ALB, NLB | App Gateway, Front Door | Cloud Load Balancing | R, E, L |
| Identity | IAM, Cognito | Entra ID | Cloud IAM, Identity Platform | R, E, L |
| Secrets / Keys | Secrets Manager, KMS | Key Vault | Secret Manager, Cloud KMS | R, L |
| Registry | ECR | ACR | Artifact Registry | R, L |
| Observability | CloudWatch, X-Ray | Azure Monitor, App Insights | Cloud Operations | R, E, L |
| CI/CD | CodePipeline, CodeBuild | Azure DevOps | Cloud Build | O, L |
| IaC | CloudFormation, CDK | Bicep, ARM | Deployment Manager | O, L |
| Framework | Well-Architected Framework | Well-Architected / Cloud Adoption Framework | Architecture Framework | R, E |

## 11. Architect-Level Topics
| Topic | Flag |
|---|---|
| Non-Functional Requirements (NFRs) | R, E |
| Architecture trade-off analysis (ATAM) | E |
| Architecture Decision Records (ADR) | R, L |
| C4 model / UML basics | O, L |
| Event-Driven Architecture | R, E, L |
| Serverless architecture | R, E |
| Multi-tenancy | O, E |
| Multi-region / Disaster Recovery (RPO, RTO) | R, E, L |
| Capacity planning | R, L |
| Cost optimization / FinOps | O, L |
| Migration strategies (6 Rs) | E |
| Data mesh | O |
| Team Topologies | O |
| Microservice anti-patterns (distributed monolith, chatty services, nano-services, shared DB) | R, E |