# Distributed Systems: Architect-Level Prerequisites

**Legend:** `R` Required · `O` Optional · `E` Exam-oriented · `L` Real-life use

## 1. Core Concepts

| Topic | Flags |
|---|---|
| Distributed system characteristics | R, E |
| Fallacies of distributed computing | R, E |
| Scalability (vertical vs horizontal) | R, E, L |
| Availability | R, E, L |
| Reliability | R, E, L |
| Fault tolerance | R, E, L |
| Resilience | R, E, L |
| Elasticity | R, E, L |
| Latency vs throughput | R, E, L |
| Durability | R, E, L |
| SLA / SLO / SLI | R, E, L |
| RTO / RPO | R, E, L |
| Single point of failure | R, E, L |
| Failure modes (partial failure, network partition) | R, L |

## 2. Theory

| Topic | Flags |
|---|---|
| CAP theorem | R, E |
| PACELC | O, E |
| Consistency models (strong, eventual, causal, read-your-writes) | R, E, L |
| ACID vs BASE | R, E, L |
| Consensus (Paxos, Raft), conceptual only | O, E |
| Quorum (read/write) | R, E, L |
| Leader election | R, L |
| Logical / vector clocks | O |
| CRDTs | O |
| Byzantine fault tolerance | O |

## 3. Data Distribution

| Topic | Flags |
|---|---|
| Replication (leader-follower, multi-leader, leaderless) | R, E, L |
| Replication lag | R, L |
| Partitioning / sharding | R, E, L |
| Consistent hashing | R, E |
| Hot partitions / data skew | R, L |
| SQL vs NoSQL (KV, document, column, graph) | R, E, L |
| Caching (patterns, eviction, invalidation) | R, E, L |
| Distributed transactions (2PC) | R, E |
| Saga pattern | R, E, L |
| Outbox pattern | O, L |
| Change Data Capture (CDC) | O, L |
| Idempotency | R, E, L |
| Delivery semantics (at-most-once, at-least-once, exactly-once) | R, E, L |

## 4. Communication

| Topic | Flags |
|---|---|
| Synchronous vs asynchronous | R, E, L |
| REST / gRPC | R, L |
| Message queues vs event streaming | R, E, L |
| Pub/Sub | R, E, L |
| Event-driven architecture | R, E, L |
| Event sourcing | O, E |
| CQRS | O, E |
| Dead-letter queue | R, E, L |
| Backpressure | O, L |

## 5. Resilience Patterns

| Topic | Flags |
|---|---|
| Timeouts | R, L |
| Retries with exponential backoff and jitter | R, E, L |
| Circuit breaker | R, E, L |
| Bulkhead | O, E |
| Rate limiting / throttling | R, E, L |
| Graceful degradation | R, L |
| Health checks | R, L |
| Failover (active-active vs active-passive) | R, E, L |

## 6. Infrastructure & Traffic

| Topic | Flags |
|---|---|
| Load balancing (L4 vs L7, algorithms) | R, E, L |
| Reverse proxy | R, L |
| API gateway | R, E, L |
| CDN | R, E, L |
| DNS (routing policies, TTL) | R, E, L |
| Service discovery | R, L |
| Service mesh | O, L |
| Auto scaling | R, E, L |
| Regions / Availability Zones | R, E, L |
| Multi-region design | R, E, L |
| Disaster recovery strategies (backup/restore, pilot light, warm standby, multi-site) | R, E, L |

## 7. Architecture Patterns

| Topic | Flags |
|---|---|
| Monolith vs microservices | R, E, L |
| Stateless vs stateful services | R, E, L |
| Shared-nothing architecture | O |
| Twelve-factor app | R, L |
| Strangler fig pattern | O, E, L |
| Sidecar pattern | O, L |
| Cell-based architecture | O |
| Well-Architected Framework pillars | R, E |

## 8. Observability

| Topic | Flags |
|---|---|
| Logging, metrics, tracing | R, E, L |
| Correlation IDs | R, L |
| Alerting and on-call basics | O, L |
| Chaos engineering | O, L |

## 9. Security in Distributed Systems

| Topic | Flags |
|---|---|
| AuthN vs AuthZ | R, E, L |
| OAuth2 / OIDC | R, E, L |
| mTLS | O, L |
| Zero trust | O, E |
| Secrets management | R, L |
| Encryption at rest / in transit | R, E, L |

## 10. Cost & Capacity

| Topic | Flags |
|---|---|
| Capacity planning | O, L |
| Back-of-envelope estimation | O, E |
| FinOps basics | O, L |

## Skip for Now

- Paxos/Raft internals
- CRDT math
- Byzantine proofs
- Formal verification
- TLA+
- Gossip protocol internals