# Data Structures: Architect + Developer Revision Guide

**Flags:** `R` Required · `O` Optional · `E` Exam oriented · `L` Real life use
**Per module:** Topics (flagged) → What problem it solves → Where it runs in real systems
**Scope:** Data structures with the algorithms that define their cost (complexity, trade-offs, access patterns). Basics are skipped. Focus: choosing the right structure for a workload and recognising it inside databases, caches, queues and distributed systems.

---

## 1. Complexity, Cost Models & Memory Layout

### Topics
- Big-O, amortised cost, worst vs average vs expected — R, E, L
- Space-time trade-offs — R, E, L
- Cache locality: arrays vs linked structures, cache lines, prefetching — R, E, L
- Memory overhead per element (pointers, object headers, padding) — R, E, L
- Mutable vs immutable (persistent) structures, structural sharing — R, E, L
- Concurrency-safety of structures (thread-safe vs lock-free) — R, E, L
- Disk vs memory cost models (block I/O, B-tree fan-out) — R, E, L
- Why big-O alone misleads (constants, cache effects, small n) — R, E, L

### What problem it solves / where it shows up
| Problem | Idea |
|---|---|
| Choosing between structures | Cost model for the real workload (read-heavy, write-heavy, range queries) |
| Hidden performance cliffs | Cache misses and allocation overhead, not just asymptotics |
| Sharing data across threads or versions | Immutable/persistent structures |

---

## 2. Arrays, Dynamic Arrays & Strings

### Topics
- Contiguous arrays, dynamic array resizing, amortised append — R, E, L
- Sparse arrays, circular buffers/ring buffers — R, E, L
- Strings: immutability, interning, UTF-8/UTF-16 costs, ropes — R, E, L
- Slices/views without copying — R, E, L
- Struct-of-arrays vs array-of-structs — O, E, L
- Memory-mapped and columnar layouts — R, E, L
- Bit arrays and bit manipulation — O, E, L

### What problem it solves / where it shows up
| Problem | Structure | Real use |
|---|---|---|
| Fast sequential access, cache-friendly | Arrays/dynamic arrays | Default collection in most services |
| Fixed-capacity streaming buffer | Ring buffer | Logging, network buffers, LMAX-style queues |
| Large text edits | Rope / piece table | Editors |
| Analytics scans | Columnar arrays | Parquet, columnar databases |

---

## 3. Linked Structures, Stacks & Queues

### Topics
- Singly/doubly linked lists, why they are often slower in practice — R, E, L
- Stacks, call stack, undo, expression evaluation — R, E, L
- Queues, deques, priority queues — R, E, L
- Blocking queues, bounded vs unbounded, backpressure — R, E, L
- Lock-free queues, MPMC/SPSC queues — R, E, L
- LRU linked-list pattern (list + hash map) — R, E, L
- Skip lists (concurrent ordered map) — R, E, L
- Delay queues, timing wheels — O, E, L
- Message queues as distributed queue abstraction — R, E, L

### What problem it solves / where it shows up
| Problem | Structure | Real use |
|---|---|---|
| Task buffering and decoupling | Bounded queue | Thread pools, Kafka partitions, job queues |
| Scheduling by time/priority | Priority queue / timing wheel | Timers, schedulers, retry queues |
| Eviction ordering | Doubly linked list + hash map | LRU caches |
| Concurrent sorted map | Skip list | Redis sorted sets, LevelDB/RocksDB memtables |

---

## 4. Hash-Based Structures

### Topics
- Hash tables: collision handling (chaining, open addressing), load factor, resizing — R, E, L
- Hash function quality, avalanche, hash flooding attacks — R, E, L
- Consistent hashing, rendezvous hashing, virtual nodes — R, E, L
- Hash maps vs tree maps trade-offs (ordering, worst case) — R, E, L
- Concurrent hash maps and lock striping — R, E, L
- Bloom filters, counting Bloom filters, cuckoo filters — R, E, L
- HyperLogLog, Count-Min Sketch (probabilistic structures) — R, E, L
- Perfect hashing (awareness) — O
- Hash joins in databases — R, E, L
- Partitioning by hash and the hot-key problem — R, E, L

### What problem it solves / where it shows up
| Problem | Structure | Real use |
|---|---|---|
| O(1) average lookup | Hash table | Caches, indexes, dictionaries, session stores |
| Evenly spread keys across nodes with minimal movement on resize | Consistent hashing | DynamoDB, Cassandra, memcached clients, load balancers |
| "Definitely not present" check cheaply | Bloom filter | LSM-tree reads, CDN/cache pre-checks, spam/dedup |
| Count distinct at huge scale | HyperLogLog | Redis `PFCOUNT`, analytics |
| Frequency estimation in streams | Count-Min Sketch | Top-K, rate limiting, telemetry |

---

## 5. Trees: Balanced, Search & Disk-Oriented

### Topics
- Binary search trees, AVL, red-black trees — R, E, L
- B-tree and B+ tree (fan-out, page size, range scans) — R, E, L
- LSM trees (memtable, SSTables, compaction, write amplification) — R, E, L
- B-tree vs LSM-tree trade-offs (read, write, space amplification) — R, E, L
- Tries, radix trees, prefix compression — R, E, L
- Segment trees, Fenwick trees (awareness) — O, E
- Interval trees, R-trees (spatial), k-d trees — O, E, L
- Merkle trees (hashes for verification) — R, E, L
- Heaps (binary, d-ary, pairing), heap-based top-K — R, E, L
- Tree traversals and iteration costs — R, E
- Copy-on-write B-trees (LMDB, Btrfs) — O, E

### What problem it solves / where it shows up
| Problem | Structure | Real use |
|---|---|---|
| Ordered lookup + range queries on disk | B+ tree | PostgreSQL, SQL Server, MySQL InnoDB indexes |
| Write-heavy storage | LSM tree | Cassandra, RocksDB, LevelDB, HBase |
| Prefix and autocomplete | Trie / radix tree | Routers (URL routing), IP routing tables, search suggestions |
| Verify large data sets cheaply | Merkle tree | Git, blockchains, anti-entropy in Dynamo-style stores |
| Spatial queries | R-tree | PostGIS, geo indexes |
| Always get the min/max | Heap | Schedulers, top-K, Dijkstra |

---

## 6. Graphs & Graph Structures

### Topics
- Adjacency list vs matrix vs edge list, memory trade-offs — R, E, L
- Directed vs undirected, weighted, DAGs — R, E, L
- Traversals (BFS, DFS) and where they apply — R, E, L
- Shortest paths (Dijkstra, Bellman-Ford, A*) — R, E, L
- Topological sort (build systems, dependency resolution) — R, E, L
- Cycle detection (deadlock detection, dependency cycles) — R, E, L
- Minimum spanning tree, union-find (disjoint set) — R, E, L
- Strongly connected components — O, E
- PageRank-style and graph databases (property graphs) — O, E, L
- Distributed graph processing trade-offs — O, E, L
- Service dependency graphs and blast-radius analysis — R, E, L

### What problem it solves / where it shows up
| Problem | Structure/Algorithm | Real use |
|---|---|---|
| Order tasks with dependencies | DAG + topological sort | Build tools, CI pipelines, Airflow, Terraform plans |
| Detect circular waits | Cycle detection in wait-for graph | Database/OS deadlock detection |
| Route over a network | Shortest path | Network routing, maps, logistics |
| Merge groups dynamically | Union-find | Clustering, network connectivity, Kruskal |
| Relationship queries | Graph database | Fraud detection, recommendation, knowledge graphs |

---

## 7. Indexing & Search Structures

### Topics
- Database index types: B+ tree, hash, bitmap, GiST/GIN, covering — R, E, L
- Inverted index (search engines), posting lists, compression — R, E, L
- Full-text, fuzzy search (n-grams, edit distance structures) — R, E, L
- Vector indexes: HNSW, IVF, product quantisation (approximate nearest neighbour) — R, E, L
- Geohash, quadtree, S2/H3 spatial indexing — O, E, L
- Time-series structures and downsampling, columnar storage — R, E, L
- Index selection trade-offs: write cost, space, selectivity — R, E, L
- Search relevance vs data-structure trade-off (recall vs latency) — R, E, L

### What problem it solves / where it shows up
| Problem | Structure | Real use |
|---|---|---|
| Fast keyword search | Inverted index | Elasticsearch/OpenSearch, Lucene, Solr |
| Semantic similarity | HNSW / IVF vector index | Vector databases, RAG retrieval |
| Selective analytical filters | Bitmap/columnar indexes | Warehouses, columnstore |
| Location lookups | Geohash/H3/quadtree | Ride-hailing, delivery, maps |

---

## 8. Caching & Eviction Structures

### Topics
- LRU, LFU, FIFO, TinyLFU/W-TinyLFU, ARC, CLOCK — R, E, L
- Time-based expiry (TTL), timing wheels, lazy vs active expiry — R, E, L
- Cache stampede, negative caching, request coalescing — R, E, L
- Write-through, write-back, write-around, cache-aside — R, E, L
- Multi-level caches (L1 in-process, L2 distributed) — R, E, L
- Memory-efficient encodings (compressed lists, ziplists/listpacks) — O, E, L
- Cache sizing via hit-rate curves — R, E, L
- Consistency and invalidation patterns — R, E, L

### What problem it solves / where it shows up
| Problem | Structure/Policy | Real use |
|---|---|---|
| Keep hot data in limited memory | LRU/LFU/TinyLFU | Redis, Caffeine (Java), CPU caches, CDN |
| Expire millions of keys cheaply | Timing wheel / hierarchical wheel | Kafka purgatory, Netty, schedulers |
| Avoid thundering herd | Single-flight / request coalescing | API gateways, HybridCache |

---

## 9. Concurrent, Distributed & Persistent Structures

### Topics
- Concurrent collections and lock striping — R, E, L
- Lock-free queues/stacks, ABA problem — O, E, L
- Copy-on-write and persistent (immutable) data structures — R, E, L
- CRDTs (conflict-free replicated data types): counters, sets, registers — R, E, L
- Vector clocks, version vectors, Lamport clocks — R, E, L
- Gossip protocols and membership structures — O, E, L
- Log-structured structures: append-only logs, WAL, event logs — R, E, L
- Skip lists, memtables, and compaction strategies — R, E, L
- Sharded counters, hot-key mitigation — R, E, L
- Distributed hash tables and partition maps — R, E, L

### What problem it solves / where it shows up
| Problem | Structure | Real use |
|---|---|---|
| Concurrent access without global lock | Striped/concurrent maps | `ConcurrentHashMap`, .NET `ConcurrentDictionary` |
| Merge offline/replicated updates without conflicts | CRDTs | Collaborative editing, Redis Enterprise CRDB, Riak |
| Order events across nodes | Vector/Lamport clocks | Dynamo-style stores, causal consistency |
| Durable, replayable state | Append-only log | Kafka, WAL in databases, event sourcing |

---

## 10. Data Structures in Real Systems (Architect Mapping)

### Topics
- Relational database internals: B+ tree indexes, buffer pool (LRU variant), WAL, hash joins — R, E, L
- NoSQL internals: LSM trees (Cassandra, RocksDB), document stores on B-trees (MongoDB WiredTiger) — R, E, L
- Redis internals: hash tables, skip lists, listpacks, HyperLogLog, streams — R, E, L
- Kafka internals: append-only segmented log, sparse offset index — R, E, L
- Search engines: inverted index, segment merging — R, E, L
- Vector databases: HNSW graphs, quantisation — R, E, L
- Git: Merkle DAG of objects — R, E, L
- File systems: B-trees, inodes, extents — R, E, L
- Load balancers, routers: tries, consistent hashing — R, E, L
- Rate limiting: token bucket, leaky bucket, sliding window counters — R, E, L
- Choosing storage engine by workload: read-heavy vs write-heavy vs range-heavy — R, E, L

### What problem it solves / where it shows up
| Workload | Likely structure | Trade-off |
|---|---|---|
| Point lookups, ordered ranges, balanced read/write | B+ tree | Higher write amplification on random writes |
| Very high write throughput | LSM tree | Read and space amplification, compaction cost |
| Distinct counts at scale | HyperLogLog | Approximate answer, tiny memory |
| Membership pre-check | Bloom filter | False positives, no deletion (unless counting/cuckoo) |
| Event streams | Append-only log | Sequential reads great, random reads need index |
| Semantic retrieval | HNSW | Approximate results, high memory, tunable recall |

---

## Mental Model (one line each)
- **Choose by access pattern:** point lookup, range scan, ordered iteration, membership, nearest neighbour, or streaming.
- **Memory hierarchy rules:** cache-friendly arrays often beat theoretically better pointer-heavy structures.
- **Disk changes the game:** B+ trees minimise I/O; LSM trees minimise random writes.
- **Probabilistic structures trade accuracy for scale:** Bloom filter, HyperLogLog, Count-Min Sketch.
- **Distributed systems reuse the same ideas:** hashing for placement, logs for durability, trees for verification, clocks for ordering.
- **Amplification triangle:** read, write and space amplification cannot all be minimised together.

## Top Interview Hotspots
1. Hash table internals: collisions, resizing, hash flooding, ordering trade-offs
2. B+ tree vs LSM tree: when each wins
3. Consistent hashing and rebalancing on node changes
4. Bloom filter: false positives, use in LSM stores and caches
5. LRU cache design (list + map) and eviction policy alternatives
6. Heap/priority queue for top-K, scheduling and streaming
7. Graph algorithms in real systems: DAG scheduling, deadlock/cycle detection
8. Trie and radix trees in routing and autocomplete
9. HyperLogLog / Count-Min Sketch for large-scale analytics
10. How Redis, Kafka and Elasticsearch store data internally

---

# Cut-Down Strategy

## Tier 1: Master in depth (~60% of effort)
1. Hash tables and consistent hashing
2. B+ tree vs LSM tree, with amplification trade-offs
3. Heaps/priority queues and queue patterns (bounded queue, backpressure)
4. LRU/LFU cache designs and eviction policies
5. Graph basics for dependency and scheduling (DAG, topological sort, cycle detection)
6. Bloom filters and probabilistic structures
7. Append-only logs and WAL
8. Trie/radix tree usage in routing and search
9. Cost models: cache locality and memory overhead

## Tier 2: Working knowledge (~30%)
- Inverted indexes and vector indexes (HNSW)
- Skip lists, ring buffers, timing wheels
- Merkle trees
- CRDTs, vector clocks
- Rate limiting structures (token bucket, sliding window)
- Concurrent collections and lock-free ideas

## Tier 3: Awareness only (~10%)
- Segment/Fenwick trees, k-d trees, R-trees
- Perfect hashing, cuckoo filters
- Persistent/functional data structures internals
- Graph databases and distributed graph processing

## Drop for now
- Textbook proofs of balancing rotations (AVL/red-black rotations)
- Sorting algorithm minutiae beyond choosing a sort for the workload
- Competitive-programming-only structures

---

# Steady 4-Week Plan

*Assumes ~1 hr/day. The goal is selecting and recognising structures in systems, not coding drills.*

| Week | Focus | Output |
|---|---|---|
| **1** | Cost models, arrays/strings, queues/stacks, heaps, hash tables, consistent hashing | One-page "which structure for which access pattern" table; explain hash table resizing and hash flooding |
| **2** | Trees: B+ tree vs LSM tree, tries, Merkle trees; indexing | Write-up: "B+ tree vs LSM for a write-heavy telemetry store" with amplification trade-offs |
| **3** | Caches and eviction, probabilistic structures, graphs for dependencies | Design an LRU/TinyLFU cache on paper; pick Bloom filter vs HyperLogLog vs Count-Min for 3 scenarios; DAG scheduler sketch |
| **4** | Concurrent/distributed structures, logs, real-system mapping, interview revision | Map Redis, Kafka, Elasticsearch, Cassandra and PostgreSQL to their core structures; mock interviews on Top 10 |

## Daily rhythm
- **25 min** concept (one module)
- **20 min** apply: sketch or code a small version (LRU, Bloom filter, consistent hash ring)
- **15 min** revision (5 lines: problem → structure → trade-off → real system)

## Weekly checkpoints
- **Day 6:** Revise with Mental Model + Top Interview Hotspots
- **Day 7:** Explain 3 topics aloud as in an interview (why this structure, trade-offs, alternatives)

## Architect-standard test for every Tier 1 topic
You are ready when you can answer all four:
1. **What access pattern** does this structure optimise?
2. **What does it cost** (time, memory, write/read/space amplification)?
3. **Which real systems** use it and why?
4. **When would you NOT use it**, and what would you pick instead?