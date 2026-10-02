# MongoDB: Architect + Developer Revision Guide

**Flags:** `R` Required · `O` Optional · `E` Exam oriented · `L` Real life use
**Per module:** Topics (flagged) → How MongoDB solves it
**Baseline:** current MongoDB (self-managed and Atlas). Verify version-specific features (time series, queryable encryption, vector search, `$lookup` improvements) against the version you target.

---

## 1. Architecture & Fundamentals

### Topics
- Document model, BSON, `_id`, ObjectId — R, E, L
- Database → Collection → Document hierarchy — R, E
- Document vs relational model, when to choose MongoDB — R, E, L
- `mongod`, `mongos`, config servers — R, E, L
- Storage engine: WiredTiger, journaling, checkpoints — R, E, L
- Memory: WiredTiger cache, working set — R, E, L
- Document size limit (16 MB), schema flexibility — R, E
- Deployment options: self-hosted, Atlas, serverless — R, L
- Tools: `mongosh`, Compass, `mongodump`, `mongorestore` — R, L
- Data types and BSON gotchas (decimal128, dates, numbers) — R, E, L

### How MongoDB solves it
| Problem | MongoDB answer |
|---|---|
| Flexible, evolving schemas | Document model (BSON) |
| Durability | WiredTiger journal + checkpoints |
| Fast reads of hot data | WiredTiger cache (working set in RAM) |
| Operational convenience | Atlas managed service |
| Money / precision | `Decimal128` |
| Unique identity | `ObjectId` (time-ordered, client-generatable) |

---

## 2. CRUD & Query Language

### Topics
- Insert, find, update, delete (`insertMany`, `updateOne`, `bulkWrite`) — R, E, L
- Query operators: comparison, logical, element, array — R, E, L
- Projection, sort, limit, skip — R, E, L
- Update operators (`$set`, `$inc`, `$push`, `$pull`, `$addToSet`, `$unset`) — R, E, L
- Array operators and positional updates (`$`, `$[]`, `$[<id>]`) — R, E, L
- Upserts, `findOneAndUpdate` — R, E, L
- Write concerns, read concerns — R, E, L
- Cursors, batch size, pagination (range-based vs skip) — R, E, L
- Text search, regex, collation — R, E, L
- Querying embedded docs and arrays (`$elemMatch`) — R, E, L
- Bulk writes and ordered vs unordered — R, E, L

### How MongoDB solves it
| Problem | MongoDB answer |
|---|---|
| Atomic single-doc change | Single-document atomic operations |
| Modify nested arrays | Positional and array filter operators |
| Insert-or-update | `upsert: true`, `findOneAndUpdate` |
| Efficient pagination | Range queries on indexed field (avoid large `skip`) |
| Case/locale-aware sort | Collation |
| Many writes at once | `bulkWrite` |

---

## 3. Data Modeling

### Topics
- Embedding vs referencing — R, E, L
- One-to-one, one-to-many, many-to-many patterns — R, E, L
- Schema design principles: model for access patterns — R, E, L
- Design patterns: Bucket, Subset, Computed, Extended Reference, Outlier, Schema Versioning, Attribute, Polymorphic, Approximation — R, E, L
- Unbounded array anti-pattern — R, E, L
- Denormalisation and consistency trade-offs — R, E, L
- Schema validation (`$jsonSchema`) — R, E, L
- Time series modeling — O, E, L
- Multi-tenancy designs — R, L
- Document growth and `_id` choice — R, E

### How MongoDB solves it
| Problem | MongoDB answer |
|---|---|
| Read together, store together | Embedded documents |
| Large or shared entities | References + `$lookup` |
| Huge arrays | Bucket / Subset pattern |
| Schema evolution | Schema Versioning pattern |
| Enforce structure | `$jsonSchema` validation on collections |
| Expensive aggregates | Computed pattern (precompute) |
| IoT / metrics data | Time series collections |

---

## 4. Indexing

### Topics
- Single, compound, multikey indexes — R, E, L
- ESR rule (Equality, Sort, Range) for compound index order — R, E, L
- Covered queries — R, E, L
- Unique, partial, sparse, TTL, hashed indexes — R, E, L
- Text, geospatial (2dsphere), wildcard indexes — R, E, L
- Index intersection — E
- Atlas Search, Vector Search — O, E, L
- `explain()` (queryPlanner, executionStats) — R, E, L
- Index build impact, rolling builds — R, E, L
- Index cardinality, selectivity, index size and RAM — R, E, L
- Hidden indexes, index usage stats (`$indexStats`) — O, L

### How MongoDB solves it
| Problem | MongoDB answer |
|---|---|
| Fast lookups and sorts | B-tree indexes (compound with ESR rule) |
| Avoid fetching documents | Covered queries |
| Auto-expire data | TTL indexes |
| Index subset | Partial indexes |
| Search and relevance | Atlas Search (Lucene) / text indexes |
| Geo queries | 2dsphere indexes |
| Verify performance | `explain("executionStats")` |

---

## 5. Aggregation Framework

### Topics
- Pipeline concept, stages order and optimisation — R, E, L
- `$match`, `$project`, `$group`, `$sort`, `$limit`, `$skip` — R, E, L
- `$lookup`, `$unwind`, `$facet`, `$bucket` — R, E, L
- `$addFields`, `$set`, `$replaceRoot`, `$merge`, `$out` — R, E, L
- Operators: array, string, date, conditional (`$cond`, `$switch`) — R, E, L
- Window functions (`$setWindowFields`) — O, E, L
- Memory limits and `allowDiskUse` — R, E, L
- Pipeline indexes usage (early `$match`/`$sort`) — R, E, L
- Views and materialised views (`$merge`) — R, E, L
- Aggregation vs map-reduce (legacy) — E

### How MongoDB solves it
| Problem | MongoDB answer |
|---|---|
| Reporting and analytics in DB | Aggregation pipeline |
| Joins | `$lookup` (use sparingly, prefer modeling) |
| Multi-metric single pass | `$facet` |
| Persist results | `$merge` / `$out` |
| Large pipelines | `allowDiskUse`, early filtering, index-backed stages |
| Rolling calculations | `$setWindowFields` |

---

## 6. Transactions & Consistency

### Topics
- Single-document atomicity — R, E, L
- Multi-document ACID transactions (sessions) — R, E, L
- Transaction limits and performance cost — R, E, L
- Read concern: local, majority, snapshot, linearizable — R, E, L
- Write concern: `w:1`, `w:majority`, `j:true` — R, E, L
- Read preference: primary, secondary, nearest — R, E, L
- Causal consistency — O, E
- Retryable writes and reads — R, E, L
- Idempotency, optimistic concurrency (version field) — R, E, L
- Change Streams — R, E, L
- CAP theorem and MongoDB's position — R, E

### How MongoDB solves it
| Problem | MongoDB answer |
|---|---|
| Atomic multi-field update | Single-document atomicity (design for it) |
| Multi-collection atomicity | Multi-document transactions |
| Durable acknowledged writes | `w: "majority"` + journaling |
| Consistent reads | `readConcern: "majority" / "snapshot"` |
| Transient network errors | Retryable writes |
| React to data changes | Change Streams |
| Lost updates | Version field + conditional update |

---

## 7. Replication & High Availability

### Topics
- Replica set: primary, secondaries, arbiter — R, E, L
- Elections, voting, priority, majority — R, E, L
- Oplog, replication lag, oplog window — R, E, L
- Failover behaviour, rollback — R, E, L
- Read from secondaries trade-offs — R, E, L
- Hidden, delayed, priority-0 members — R, E
- Write concern with replication — R, E, L
- Backup strategies (snapshots, `mongodump`, Atlas backups, PITR) — R, E, L
- Disaster recovery, multi-region replica sets — R, E, L
- Monitoring replica health (`rs.status()`) — R, E, L

### How MongoDB solves it
| Problem | MongoDB answer |
|---|---|
| Automatic failover | Replica set elections |
| Data redundancy | Oplog-based replication |
| Offload reads | Secondary reads (accept staleness) |
| Protect against mistakes | Delayed secondary, PITR backups |
| Multi-region resilience | Geo-distributed replica set members |
| Know replica state | `rs.status()`, Atlas metrics |

---

## 8. Sharding & Scalability

### Topics
- Sharded cluster: shards, `mongos`, config servers — R, E, L
- Shard key selection: cardinality, frequency, monotonic change — R, E, L
- Hashed vs ranged sharding — R, E, L
- Zone sharding — O, E, L
- Chunks, balancer, jumbo chunks — R, E, L
- Targeted vs scatter-gather queries — R, E, L
- Resharding, refine shard key — R, E, L
- When to shard vs scale vertically/optimise — R, E, L
- Hot shard and monotonic key problem — R, E, L
- Atlas auto-scaling, global clusters — O, L
- Capacity planning (working set, IOPS) — R, L

### How MongoDB solves it
| Problem | MongoDB answer |
|---|---|
| Data larger than one node | Sharding (horizontal partitioning) |
| Even distribution | Hashed shard key / good compound key |
| Geo-locality of data | Zone sharding |
| Query routing | `mongos` router |
| Rebalancing | Balancer + chunk migration |
| Wrong shard key | Resharding / refine shard key |

---

## 9. Security

### Topics
- Authentication: SCRAM, x.509, LDAP, OIDC — R, E, L
- Authorization: RBAC, built-in and custom roles — R, E, L
- Least privilege per application — R, E, L
- TLS in transit, encryption at rest — R, E, L
- Client-Side Field Level Encryption, Queryable Encryption — O, E, L
- Auditing — R, E, L
- Network security: IP allowlist, VPC peering, private link — R, L
- Injection risks (operator injection, `$where`) — R, E, L
- Secrets and connection string management — R, L
- Atlas security features — R, L

### How MongoDB solves it
| Problem | MongoDB answer |
|---|---|
| Who can connect | SCRAM / x.509 / OIDC authentication |
| What they can do | RBAC with custom roles |
| Data in transit | TLS |
| Data at rest | WiredTiger encryption / Atlas encryption |
| Sensitive fields | CSFLE / Queryable Encryption |
| Track access | Audit logs |
| NoSQL injection | Input validation, avoid `$where`, parameterised drivers |

---

## 10. Performance Tuning & Monitoring

### Topics
- Working set vs RAM, WiredTiger cache pressure — R, E, L
- Slow query log and database profiler — R, E, L
- `explain()` plans: COLLSCAN vs IXSCAN, docs examined vs returned — R, E, L
- Index tuning, removing unused indexes — R, E, L
- Connection pooling and limits — R, E, L
- Write performance: batch writes, write concern cost — R, E, L
- Document size and update patterns (padding, moves) — R, E
- `mongostat`, `mongotop`, Atlas Performance Advisor — R, L
- Query optimization with projection and covered queries — R, E, L
- Pagination at scale — R, L
- Locking and concurrency (document-level) — R, E

### How MongoDB solves it
| Problem | MongoDB answer |
|---|---|
| Find slow queries | Profiler, slow query log, Performance Advisor |
| Fix full scans | Right compound index (ESR) |
| Reduce network/IO | Projection, covered queries |
| Connection storms | Driver pooling (`maxPoolSize`) |
| Live monitoring | `mongostat`, `mongotop`, Atlas / Ops Manager |

---

## 11. Drivers & Application Integration

### Topics
- Drivers: Node.js, .NET, Java, Python — R, L
- Mongoose (Node), EF Core provider / LINQ (.NET), Spring Data — R, L
- Connection strings, pooling, timeouts — R, E, L
- Retry logic and error handling — R, E, L
- Schema validation in app layer plus DB — R, L
- Repository / data access patterns — R, L
- ODM vs raw driver trade-offs — R, E, L
- Change Streams in services — R, E, L
- Event-driven integration (Kafka connector, Atlas triggers) — O, L

### How MongoDB solves it
| Problem | MongoDB answer |
|---|---|
| Language integration | Official drivers per language |
| Object mapping | Mongoose / Spring Data / EF Core MongoDB provider |
| Reactive pipelines | Change Streams |
| Stream integration | MongoDB Kafka Connector |
| Resilience | Retryable operations, driver timeouts |

---

## 12. Operations, Backup & Migration

### Topics
- Backup: `mongodump`, filesystem snapshots, Atlas continuous backup — R, E, L
- Restore and point-in-time recovery — R, E, L
- Upgrades (rolling), version compatibility, FCV — R, E, L
- Data import/export (`mongoimport`, `mongoexport`) — R, L
- Migration from RDBMS (modeling first, ETL, Relational Migrator) — R, E, L
- Monitoring and alerting (Atlas, Prometheus, Ops Manager) — R, L
- Capacity planning and cost — R, L
- Infrastructure as code (Atlas Terraform provider) — O, L
- Kubernetes operator — O, L
- Compliance and data residency — O, L

### How MongoDB solves it
| Problem | MongoDB answer |
|---|---|
| Recover to a moment in time | Continuous backup + oplog replay |
| Zero-downtime upgrade | Rolling upgrade of replica set members |
| Move off SQL | Remodel documents, then ETL (Relational Migrator) |
| Reproducible infra | Atlas Terraform / Operator |

---

## Mental Model (one line each)
- **Modeling rule:** data accessed together lives together; model for queries, not for tables
- **Atomicity:** one document = one atomic unit; design so most operations touch one document
- **Indexes:** ESR rule, covered queries, watch RAM
- **Consistency dial:** read/write concerns + read preference decide staleness vs durability
- **HA:** replica set first, shard only when needed
- **Scale:** shard key decides everything (cardinality, distribution, query targeting)
- **Aggregation:** filter early, project early, use indexes in first stages

## Top Interview Hotspots
1. Embedding vs referencing, and the data modeling patterns
2. Indexes: compound order (ESR), covered queries, `explain()`
3. Aggregation pipeline design and `$lookup` trade-offs
4. Replica sets: elections, oplog, failover, rollback
5. Sharding: shard key choice, hashed vs ranged, scatter-gather
6. Read concern, write concern, read preference combinations
7. Multi-document transactions: when to use and costs
8. MongoDB vs SQL: when to choose which (and CAP)
9. Performance troubleshooting: profiler, working set, slow queries
10. Security: RBAC, encryption, field-level encryption, injection

---

# Cut-Down Strategy

## Tier 1: Master in depth (~60% of effort)
1. Document modeling: embed vs reference, patterns, anti-patterns
2. Indexing: compound/ESR, multikey, partial, TTL, covered queries
3. CRUD + update operators, array handling
4. Aggregation pipeline (core stages and optimisation)
5. Read/write concerns, read preference, consistency model
6. Replica sets, elections, failover, backups and PITR
7. Sharding and shard key design
8. Transactions: scope, limits, alternatives
9. `explain()`, profiler, performance troubleshooting
10. Security: RBAC, TLS, encryption, injection

## Tier 2: Working knowledge (~30%)
- Change Streams
- Schema validation
- Time series collections
- Atlas features (Search, backups, alerts, auto-scaling)
- Driver and ODM integration (Mongoose / .NET driver)
- Capacity planning, monitoring tools
- Migration from RDBMS

## Tier 3: Awareness only (~10%)
- Vector Search, Atlas Search internals
- Queryable Encryption, CSFLE details
- Zone sharding, resharding internals
- Kubernetes operator, Terraform provider
- Map-reduce (legacy)

## Drop for now
- Deprecated features and old storage engines (MMAPv1)
- Deep WiredTiger internals
- Rarely used admin commands

---

# Steady 6-Week Plan

*Assumes ~1 to 1.5 hrs/day. With less time, stretch to 8-9 weeks, same order. Do not skip Tier 1.*

| Week | Focus | Output |
|---|---|---|
| **1** | Fundamentals, BSON, CRUD, query and update operators, arrays | 30 CRUD/array exercises in `mongosh`; one-page notes on atomicity and `_id` |
| **2** | Data modeling and patterns | Model an e-commerce and a social feed domain; document embed/reference decisions per access pattern |
| **3** | Indexing, `explain()`, performance basics | Seed 1M documents; fix 5 slow queries with ESR compound indexes; compare `executionStats` before/after |
| **4** | Aggregation pipeline, `$lookup`, `$facet`, `$merge`, window functions | 10 reporting pipelines; optimise one with early `$match` + indexes |
| **5** | Replication, read/write concerns, transactions, change streams, backups | Local 3-node replica set; simulate failover; run a multi-document transaction; consume a change stream |
| **6** | Sharding, security, Atlas/ops + interview revision | Pick and justify a shard key for 3 domains; configure RBAC + TLS; mock interviews on Top 10 |

## Daily rhythm
- **30 min** concept (one module)
- **45 min** hands-on (local Docker replica set or Atlas free tier)
- **15 min** revision (5 lines: problem → MongoDB answer → trade-off)

## Weekly checkpoints
- **Day 6:** Revise using Mental Model + Top Interview Hotspots
- **Day 7:** Explain 3 topics aloud as in an interview (why this, trade-offs, alternatives)

## Architect-standard test for every Tier 1 topic
You are ready when you can answer all four:
1. **What problem** does it solve?
2. **How** does MongoDB implement it?
3. **Trade-offs** and failure modes?
4. **When would you NOT use it?**