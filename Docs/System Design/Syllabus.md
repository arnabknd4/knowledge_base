# System Design: Prerequisites for Cloud Architect (Architect Level)

**Legend:** **R** = Required | **O** = Optional | **E** = Exam oriented | **L** = Real-life use

---

## 1. Core Principles
- Scalability (Vertical vs Horizontal): R, E, L
- Availability & Reliability: R, E, L
- Latency vs Throughput: R, E, L
- Fault Tolerance & Resilience: R, E, L
- Consistency, Availability, Partition Tolerance (CAP Theorem): R, E
- PACELC Theorem: O, E
- Strong vs Eventual Consistency: R, E, L
- SLA, SLO, SLI: R, E, L
- RTO & RPO: R, E, L
- Single Point of Failure (SPOF): R, E, L
- Trade-off Analysis: R, L

## 2. Networking Essentials for Design
- Client-Server Model: R
- DNS: R, E, L
- HTTP/HTTPS, TLS: R, L
- REST vs gRPC vs GraphQL: R, L
- WebSockets, Long Polling, SSE: O, L
- CDN: R, E, L
- Load Balancers (L4 vs L7): R, E, L
- Reverse Proxy, Forward Proxy: R, L
- API Gateway: R, E, L
- Rate Limiting & Throttling: R, L

## 3. Compute & Scaling Patterns
- Stateless vs Stateful Services: R, E, L
- Auto Scaling: R, E, L
- Load Balancing Algorithms: R, E
- Service Discovery: R, L
- Serverless vs Containers vs VMs: R, E, L
- Monolith vs Microservices: R, E, L
- Event-Driven Architecture: R, E, L

## 4. Data Storage
- SQL vs NoSQL: R, E, L
- ACID vs BASE: R, E
- Indexing: R, L
- Replication (Leader-Follower, Multi-Leader): R, E, L
- Sharding / Partitioning: R, E, L
- Consistent Hashing: R, E
- Read Replicas: R, E, L
- Data Warehouse vs Data Lake: O, E, L
- Object vs Block vs File Storage: R, E, L
- Data Lifecycle & Tiering: O, E, L
- Backup & Restore Strategies: R, E, L

## 5. Caching
- Cache Types (Client, CDN, App, DB): R, E, L
- Cache Strategies (Cache-Aside, Write-Through, Write-Back): R, E
- Eviction Policies (LRU, LFU, TTL): R, E
- Cache Invalidation: R, L
- Distributed Cache: R, L

## 6. Messaging & Async Processing
- Message Queue vs Pub/Sub: R, E, L
- Event Streaming: R, L
- Dead Letter Queue: O, E, L
- Idempotency: R, L
- Delivery Guarantees (At-least-once, At-most-once, Exactly-once): R, E
- Backpressure: O, L

## 7. Distributed System Patterns
- Leader Election: O, E
- Consensus (Paxos/Raft, concept only): O
- Distributed Transactions, Saga Pattern: R, E, L
- Two-Phase Commit: O, E
- CQRS: R, E, L
- Event Sourcing: O, E, L
- Circuit Breaker: R, E, L
- Retry with Exponential Backoff: R, L
- Bulkhead Pattern: O, E
- Sidecar / Strangler / Anti-Corruption Layer: O, E, L

## 8. Security by Design
- AuthN vs AuthZ: R, E, L
- OAuth2, OIDC, JWT: R, L
- Least Privilege, Zero Trust: R, E, L
- Encryption at Rest & in Transit: R, E, L
- Secrets Management: R, L
- Network Segmentation: R, E, L

## 9. Observability & Operations
- Logging, Metrics, Tracing: R, E, L
- Monitoring & Alerting: R, L
- Health Checks: R, L
- Deployment Strategies (Blue-Green, Canary, Rolling): R, E, L
- Infrastructure as Code: R, E, L
- Chaos Engineering: O, L

## 10. Resilience & DR
- Multi-AZ vs Multi-Region: R, E, L
- DR Strategies (Backup & Restore, Pilot Light, Warm Standby, Active-Active): R, E, L
- Failover vs Failback: R, E
- Graceful Degradation: R, L

## 11. Architect-Level Skills
- Requirement Gathering (Functional vs Non-Functional): R, E, L
- Capacity Estimation (QPS, Storage, Bandwidth): R, L
- Cost Optimization / FinOps: R, E, L
- Well-Architected Pillars: R, E
- High-Level vs Low-Level Design: R
- Architecture Diagrams & Documentation: R, L
- Architecture Decision Records (ADR): O, L
- Build vs Buy: O, L

## 12. Classic Design Case Studies (practice only)
- URL Shortener: O, L
- Rate Limiter: O, L
- Notification System: O, L
- Chat System: O
- News Feed: O
- File Storage / Sync: O

---

**Suggested order:** Sections 1, 2, 4, 5, 3, 6, 7, 10, 8, 9, 11. Use section 12 for practice once the rest is solid.