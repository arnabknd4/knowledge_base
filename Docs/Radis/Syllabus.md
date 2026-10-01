# Redis → Distributed Caching: Prerequisite Topics (Architect Level)

**Flags:** 🔴 Required | 🟡 Optional | 📝 Exam-oriented | 🛠️ Real-life use

## 1. Caching Fundamentals
- Cache hit / miss / hit ratio: 🔴 📝 🛠️
- Latency vs throughput: 🔴 📝
- Cache-aside (lazy loading): 🔴 📝 🛠️
- Read-through: 🔴 📝
- Write-through: 🔴 📝
- Write-behind (write-back): 🔴 📝 🛠️
- Write-around: 🟡 📝
- Refresh-ahead: 🟡
- TTL (time to live): 🔴 📝 🛠️
- Cache invalidation strategies: 🔴 📝 🛠️
- Eviction policies (LRU, LFU, FIFO, random): 🔴 📝 🛠️
- Cache warming / pre-loading: 🟡 🛠️
- Local (in-process) cache vs distributed cache: 🔴 📝 🛠️
- Multi-level caching (L1/L2): 🟡 🛠️
- CDN / edge caching vs application caching: 🟡 🛠️

## 2. Cache Failure Patterns
- Cache stampede (thundering herd): 🔴 📝 🛠️
- Cache penetration: 🔴 📝 🛠️
- Cache avalanche: 🔴 📝 🛠️
- Hot key problem: 🔴 🛠️
- Big key problem: 🟡 🛠️
- Stale data / data inconsistency: 🔴 📝 🛠️
- Negative caching: 🟡
- Bloom filter (for penetration): 🟡 📝

## 3. Distributed Systems Basics
- CAP theorem: 🔴 📝
- Consistency models (strong, eventual): 🔴 📝
- Replication (leader-follower / primary-replica): 🔴 📝 🛠️
- Partitioning / sharding: 🔴 📝 🛠️
- Consistent hashing: 🔴 📝 🛠️
- Hash slots: 🔴 📝
- Failover / high availability: 🔴 📝 🛠️
- Split-brain: 🟡 📝
- Quorum: 🟡 📝
- Gossip protocol: 🟡
- Network partition: 🟡 📝
- Horizontal vs vertical scaling: 🔴 📝

## 4. Redis Core Concepts
- In-memory data store: 🔴 📝
- Single-threaded event loop (command execution model): 🔴 📝
- I/O threading (Redis 6+): 🟡
- Key-value model and key naming conventions: 🔴 🛠️
- RESP protocol: 🟡
- Redis CLI: 🔴 🛠️
- Redis vs Memcached: 🔴 📝 🛠️
- Redis vs database (use-case boundaries): 🔴 📝

## 5. Redis Data Types
- Strings: 🔴 📝 🛠️
- Hashes: 🔴 📝 🛠️
- Lists: 🔴 📝 🛠️
- Sets: 🔴 📝 🛠️
- Sorted Sets: 🔴 📝 🛠️
- Bitmaps: 🟡 📝
- HyperLogLog: 🟡 📝
- Streams: 🟡 📝 🛠️
- Geospatial indexes: 🟡
- Pub/Sub: 🔴 📝 🛠️
- JSON / Search / TimeSeries modules (Redis Stack): 🟡

## 6. Key Management & Memory
- Key expiry (EXPIRE, TTL, PERSIST): 🔴 📝 🛠️
- Active vs lazy expiration: 🔴 📝
- maxmemory and maxmemory-policy: 🔴 📝 🛠️
- Redis eviction policies (allkeys-lru, volatile-lru, allkeys-lfu, noeviction, etc.): 🔴 📝 🛠️
- Memory fragmentation: 🟡 🛠️
- Memory optimization (encodings, key design): 🟡 🛠️
- SCAN vs KEYS: 🔴 🛠️
- Lazy freeing (UNLINK): 🟡

## 7. Persistence
- RDB snapshots: 🔴 📝 🛠️
- AOF (append-only file): 🔴 📝 🛠️
- AOF fsync policies: 🔴 📝
- RDB vs AOF vs hybrid: 🔴 📝 🛠️
- Persistence vs pure-cache trade-off: 🔴 📝

## 8. Replication, HA & Scaling
- Master-replica replication: 🔴 📝 🛠️
- Async replication and data-loss window: 🔴 📝
- Redis Sentinel: 🔴 📝 🛠️
- Redis Cluster: 🔴 📝 🛠️
- Cluster hash slots (16384): 🔴 📝
- Resharding / rebalancing: 🟡 📝 🛠️
- Client-side sharding vs proxy-based vs cluster-mode: 🟡 📝
- Read replicas for read scaling: 🔴 🛠️
- Multi-region / active-active (CRDT): 🟡 🛠️

## 9. Transactions & Atomicity
- MULTI / EXEC: 🔴 📝
- WATCH (optimistic locking): 🔴 📝
- Lua scripting: 🔴 📝 🛠️
- Redis Functions: 🟡
- Pipelining: 🔴 📝 🛠️
- Atomic operations (INCR, SETNX): 🔴 📝 🛠️

## 10. Common Redis Patterns (Real-World)
- Session store: 🔴 🛠️
- Rate limiting: 🔴 📝 🛠️
- Distributed lock (SET NX PX, Redlock): 🔴 📝 🛠️
- Leaderboards: 🟡 🛠️
- Message queue / job queue: 🟡 🛠️
- Pub/Sub vs Streams: 🟡 📝
- Counters / analytics: 🟡 🛠️
- Idempotency keys: 🟡 🛠️
- API response / DB query caching: 🔴 🛠️

## 11. Performance & Operations
- Slow log: 🟡 🛠️
- Latency monitoring: 🔴 🛠️
- Connection pooling: 🔴 🛠️
- Client libraries (Jedis, Lettuce, redis-py, ioredis): 🟡 🛠️
- INFO command and key metrics: 🔴 🛠️
- Benchmarking (redis-benchmark): 🟡
- Backup and restore: 🔴 🛠️
- Monitoring tools (Prometheus exporter, RedisInsight): 🟡 🛠️

## 12. Security
- AUTH / ACLs: 🔴 📝 🛠️
- TLS encryption in transit: 🔴 📝 🛠️
- Network isolation (VPC, bind, protected mode): 🔴 🛠️
- Dangerous commands (FLUSHALL, KEYS, CONFIG): 🟡 🛠️
- Encryption at rest (managed services): 🟡

## 13. Deployment & Managed Offerings
- Standalone vs Sentinel vs Cluster deployment: 🔴 📝 🛠️
- Redis on Kubernetes (Helm, operators): 🟡 🛠️
- AWS ElastiCache for Redis: 🔴 📝 🛠️
- Azure Cache for Redis: 🟡 📝
- GCP Memorystore: 🟡
- Redis Enterprise / Redis Cloud: 🟡 🛠️
- Valkey (open-source fork): 🟡

## 14. Architect-Level Design Concerns
- Cache sizing and capacity planning: 🔴 📝 🛠️
- Choosing TTL vs invalidation strategy: 🔴 📝
- Consistency vs availability trade-offs in caching: 🔴 📝
- Cache as source of truth vs derived data: 🔴 📝
- Failure modes and graceful degradation (cache down): 🔴 📝 🛠️
- Cost vs performance trade-offs: 🔴 🛠️
- Observability and SLOs for cache layer: 🟡 🛠️
- Choosing between Redis, Memcached, Hazelcast, and others: 🟡 📝