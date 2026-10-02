# SQL Server: Architect + Developer Revision Guide

**Flags:** `R` Required · `O` Optional · `E` Exam oriented · `L` Real life use
**Per module:** Topics (flagged) → How SQL Server solves it
**Baseline:** current SQL Server / Azure SQL. Verify version-specific features (e.g. Intelligent Query Processing, Ledger, optimized locking) against the version you target.

---

## 1. Architecture & Internals

### Topics
- Database engine components (Relational Engine, Storage Engine, SQLOS) — R, E
- Query lifecycle: parse → bind → optimize → execute — R, E, L
- Data files (MDF, NDF), log file (LDF), filegroups — R, E, L
- Pages (8 KB), extents, allocation units — R, E
- Buffer pool, plan cache, memory grants — R, E, L
- System databases (master, model, msdb, tempdb) — R, E, L
- Editions, SQL Server vs Azure SQL (DB, Managed Instance, VM) — R, E, L
- Instances, collations, compatibility levels — R, E, L
- Transaction log, WAL (write-ahead logging), checkpoints — R, E, L
- tempdb usage and contention — R, E, L

### How SQL Server solves it
| Problem | SQL Server answer |
|---|---|
| Durability and crash recovery | Write-ahead transaction log + checkpoints |
| Fast repeated reads | Buffer pool (in-memory page cache) |
| Reuse compiled queries | Plan cache |
| Storage organisation | Filegroups, multiple data files |
| Temporary work | tempdb (sorts, spills, temp tables, version store) |
| Behaviour per version | Compatibility level |

---

## 2. T-SQL Fundamentals

### Topics
- DDL, DML, DQL, DCL, TCL — R, E
- SELECT logical processing order — R, E, L
- JOINs (inner, outer, cross, self, APPLY) — R, E, L
- Set operators (UNION, INTERSECT, EXCEPT) — R, E
- Subqueries, correlated subqueries, EXISTS vs IN — R, E, L
- CTEs, recursive CTEs — R, E, L
- Window functions (`ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, `SUM OVER`) — R, E, L
- Aggregation, GROUP BY, GROUPING SETS, ROLLUP, CUBE — R, E, L
- NULL handling, three-valued logic — R, E, L
- Data types, implicit conversions — R, E, L
- String, date/time functions — R, L
- `MERGE`, `OUTPUT`, `TOP`, `OFFSET/FETCH` — R, E, L
- JSON and XML support — O, L
- Dynamic SQL (`sp_executesql`) — R, E, L

### How SQL Server solves it
| Problem | SQL Server answer |
|---|---|
| Ranking, running totals, row comparison | Window functions |
| Hierarchical data | Recursive CTEs, `hierarchyid` |
| Per-row table logic | `CROSS APPLY` / `OUTER APPLY` |
| Flexible schema bits | JSON functions (`OPENJSON`, `JSON_VALUE`) |
| Upserts | `MERGE` (use with care) or `UPDATE`/`INSERT` pattern |
| Capture changed rows | `OUTPUT` clause |
| Safe dynamic queries | `sp_executesql` with parameters |

---

## 3. Database Design & Modeling

### Topics
- Normalisation (1NF-3NF, BCNF), denormalisation trade-offs — R, E, L
- Keys: primary, foreign, unique, surrogate vs natural — R, E, L
- Constraints (CHECK, DEFAULT, UNIQUE, NOT NULL) — R, E, L
- Data type selection (`datetime2`, `decimal`, `nvarchar` vs `varchar`) — R, E, L
- Relationships: 1:1, 1:N, M:N — R, E
- Schemas, naming conventions — R, L
- Temporal tables (system-versioned) — R, E, L
- Sequences vs IDENTITY, GUID keys, `NEWSEQUENTIALID` — R, E, L
- Dimensional modelling (star, snowflake) — O, E, L
- Soft delete, audit columns, multi-tenancy designs — R, L
- Partitioning design — R, E, L

### How SQL Server solves it
| Problem | SQL Server answer |
|---|---|
| Data integrity | PK / FK / CHECK / UNIQUE constraints |
| Row history and audit | System-versioned temporal tables |
| Key generation | IDENTITY, SEQUENCE, `NEWSEQUENTIALID()` |
| Logical grouping and security | Schemas |
| Large table management | Table partitioning |
| Computed values | Computed columns (persisted) |

---

## 4. Indexing

### Topics
- Clustered vs non-clustered index — R, E, L
- B-tree structure, fill factor, page splits — R, E, L
- Heap vs clustered table — R, E
- Covering index, included columns — R, E, L
- Composite index column order — R, E, L
- Filtered indexes — R, E, L
- Columnstore (clustered / non-clustered) — R, E, L
- Unique, XML, spatial, full-text indexes — O, E
- Index fragmentation: reorganize vs rebuild — R, E, L
- Statistics, auto-update, cardinality estimation — R, E, L
- Missing index DMVs and their risks — R, E, L
- Over-indexing cost on writes — R, E, L
- SARGability (index-friendly predicates) — R, E, L
- Memory-optimized tables (In-Memory OLTP) — O, E

### How SQL Server solves it
| Problem | SQL Server answer |
|---|---|
| Fast point and range lookups | B-tree clustered / non-clustered indexes |
| Avoid key lookups | Covering index with `INCLUDE` |
| Index only subset of rows | Filtered index |
| Analytics over huge tables | Columnstore indexes |
| Fragmentation | `ALTER INDEX REORGANIZE / REBUILD`, online options |
| Bad cardinality estimates | Statistics, `UPDATE STATISTICS` |
| Find index gaps | Missing index DMVs, Query Store |

---

## 5. Query Processing & Performance Tuning

### Topics
- Execution plans: estimated vs actual — R, E, L
- Operators: scans, seeks, lookups, joins (nested loop, hash, merge) — R, E, L
- Parameter sniffing, plan regression — R, E, L
- Sargability, implicit conversion, functions on columns — R, E, L
- Statistics and cardinality estimator — R, E, L
- Query Store (forced plans, regressions) — R, E, L
- Intelligent Query Processing (adaptive joins, memory grant feedback, PSP) — O, E, L
- Wait statistics analysis — R, E, L
- DMVs (`sys.dm_exec_*`, `sys.dm_os_wait_stats`) — R, E, L
- Table variables vs temp tables vs CTEs — R, E, L
- Cursors vs set-based thinking — R, E, L
- Query hints (`OPTION (RECOMPILE)`, `OPTIMIZE FOR`) — R, E, L
- Pagination patterns — R, L
- Extended Events, Profiler (legacy) — R, L

### How SQL Server solves it
| Problem | SQL Server answer |
|---|---|
| Understand slow query | Actual execution plan + `SET STATISTICS IO, TIME` |
| Plan regressions | Query Store (compare, force plan) |
| Parameter sniffing | `OPTION (RECOMPILE)`, `OPTIMIZE FOR`, PSP optimization |
| Find bottleneck type | Wait stats (`sys.dm_os_wait_stats`) |
| Capture workload | Extended Events |
| Auto-tuning | Automatic tuning (force last good plan) |

---

## 6. Transactions, Concurrency & Locking

### Topics
- ACID properties — R, E, L
- Isolation levels (Read Uncommitted, Read Committed, Repeatable Read, Serializable, Snapshot) — R, E, L
- `READ_COMMITTED_SNAPSHOT` (RCSI) vs Snapshot isolation — R, E, L
- Locks: shared, exclusive, update, intent; granularity — R, E, L
- Lock escalation — R, E, L
- Blocking vs deadlock — R, E, L
- Deadlock graphs and prevention — R, E, L
- Optimistic vs pessimistic concurrency — R, E, L
- `NOLOCK` hint risks — R, E, L
- Transaction scope, `XACT_ABORT`, `TRY...CATCH` — R, E, L
- Savepoints, nested transactions — O, E
- Distributed transactions (MSDTC) — O, E
- Row versioning and version store — R, E

### How SQL Server solves it
| Problem | SQL Server answer |
|---|---|
| Readers blocking writers | RCSI / Snapshot isolation (row versioning) |
| Deadlocks | Deadlock detection (victim selection) + consistent access order |
| Lost updates | `rowversion` column + optimistic checks |
| Large update lock escalation | Batching, partitioning, index design |
| Atomic multi-statement work | Explicit transactions + `SET XACT_ABORT ON` |
| Diagnose blocking | `sys.dm_tran_locks`, blocked process report, Extended Events |

---

## 7. Programmability

### Topics
- Stored procedures: parameters, `OUTPUT`, return codes — R, E, L
- User-defined functions: scalar, inline TVF, multi-statement TVF — R, E, L
- Triggers (AFTER, INSTEAD OF, DDL) — R, E, L
- Views, indexed views — R, E, L
- Error handling: `TRY...CATCH`, `THROW`, `RAISERROR` — R, E, L
- Table-valued parameters — R, E, L
- Temp tables, table variables — R, E, L
- Cursors and when to avoid — R, E
- Dynamic SQL and SQL injection — R, E, L
- SQLCLR — O
- `SET NOCOUNT ON`, `SCHEMABINDING` — R, L
- Bulk operations: `BULK INSERT`, `bcp`, `OPENROWSET` — R, E, L
- Migrations and deployment (DACPAC, scripts) — R, L

### How SQL Server solves it
| Problem | SQL Server answer |
|---|---|
| Reusable server-side logic | Stored procedures (plan reuse, permission boundary) |
| Parameterised sets of rows | Table-valued parameters |
| Reusable query logic | Inline TVFs (preferred over scalar UDF) |
| Enforce rules on change | Triggers (sparingly) |
| Pre-aggregated reads | Indexed views |
| Fast load | Bulk insert, minimal logging, `bcp` |

---

## 8. Security

### Topics
- Authentication: Windows, SQL logins, Entra ID — R, E, L
- Server logins vs database users, contained databases — R, E, L
- Roles (fixed server, fixed database, custom) — R, E, L
- Principle of least privilege, ownership chaining — R, E, L
- Row-Level Security — R, E, L
- Dynamic Data Masking — R, E, L
- Always Encrypted, TDE, column-level encryption — R, E, L
- Auditing (SQL Server Audit) — R, E, L
- SQL injection prevention — R, E, L
- Network security (firewall, private endpoints, TLS) — R, L
- Ledger tables — O
- Vulnerability Assessment, Defender for SQL — O, L

### How SQL Server solves it
| Problem | SQL Server answer |
|---|---|
| Per-user data filtering | Row-Level Security policies |
| Hide sensitive values | Dynamic Data Masking |
| Encryption at rest | TDE |
| Encryption from DBA too | Always Encrypted |
| Who did what | SQL Server Audit |
| Central identity | Entra ID authentication |
| Least privilege | Roles, schemas, granular GRANT/DENY |

---

## 9. High Availability & Disaster Recovery

### Topics
- Recovery models (Simple, Full, Bulk-logged) — R, E, L
- Backup types: full, differential, log, copy-only — R, E, L
- Restore sequences, point-in-time recovery — R, E, L
- RPO and RTO — R, E, L
- Always On Availability Groups — R, E, L
- Failover Cluster Instances — R, E
- Log shipping, database mirroring (legacy) — E, O
- Replication (transactional, merge, snapshot) — O, E
- Azure SQL HA: geo-replication, failover groups, zone redundancy — R, E, L
- Backup verification, `DBCC CHECKDB` — R, E, L
- Corruption handling — R, E

### How SQL Server solves it
| Problem | SQL Server answer |
|---|---|
| Data loss window | Log backups (Full recovery) |
| Fast recovery | Differential backups + restore chain |
| Automatic failover | Always On Availability Groups / FCI |
| Read scale-out | Readable secondary replicas |
| Cross-region DR | Auto-failover groups (Azure SQL), distributed AGs |
| Corruption detection | `DBCC CHECKDB`, page verify CHECKSUM |

---

## 10. Scalability & Data Management

### Topics
- Partitioning (function, scheme, switching, sliding window) — R, E, L
- Archiving and data retention — R, L
- Read replicas, scale-out — R, E, L
- Sharding / elastic pools (Azure SQL) — O, E, L
- Columnstore for analytics — R, E, L
- Compression (row, page) — R, E, L
- Change Data Capture (CDC), Change Tracking — R, E, L
- Service Broker, queuing in DB — O
- In-Memory OLTP — O, E
- Hybrid workloads (HTAP) — O

### How SQL Server solves it
| Problem | SQL Server answer |
|---|---|
| Very large tables | Partitioning + partition switching |
| Storage and IO cost | Row / page / columnstore compression |
| Incremental data feeds | CDC / Change Tracking |
| Read-heavy reporting | Readable secondaries, columnstore |
| Multi-tenant DB scale | Elastic pools, sharding patterns |

---

## 11. Integration & Data Movement

### Topics
- ETL/ELT: SSIS, Azure Data Factory — R, E, L
- Linked servers, `OPENQUERY` — O, E
- Import/export (BCP, BULK INSERT, bacpac) — R, L
- Replication vs CDC vs Change Tracking — R, E
- Application access: ADO.NET, EF Core, Dapper, JDBC, ODBC — R, L
- Connection pooling, retry logic (transient faults) — R, E, L
- PolyBase / external tables — O
- Reporting: SSRS, Power BI — O, L

### How SQL Server solves it
| Problem | SQL Server answer |
|---|---|
| ETL | SSIS / Azure Data Factory |
| Near-real-time sync | CDC + downstream consumers |
| App connectivity | Providers with pooling; retry on transient errors |
| Cross-source queries | PolyBase / external tables / linked servers |

---

## 12. Operations & Administration

### Topics
- SQL Server Agent jobs, alerts, operators — R, E, L
- Maintenance plans (index, stats, checks, backups) — R, E, L
- Monitoring: DMVs, Performance Monitor, Query Store, Azure Monitor — R, L
- Capacity planning, file growth settings — R, E, L
- Patching and upgrade strategies — R, L
- Migration approaches (DMA, DMS, backup/restore, Managed Instance link) — R, E, L
- Database Mail — O
- Resource Governor — O, E
- Config settings: MAXDOP, cost threshold, max server memory — R, E, L
- Infrastructure as code / DACPAC / CI/CD — R, L

### How SQL Server solves it
| Problem | SQL Server answer |
|---|---|
| Scheduled maintenance | SQL Server Agent / Elastic Jobs (Azure) |
| Resource contention | Resource Governor, MAXDOP, memory settings |
| Upgrades with low risk | Compatibility level + Query Store baselines |
| Migrations | DMA assessment + DMS / backup-restore |
| Schema deployment | DACPAC / migration scripts in CI/CD |

---

## Mental Model (one line each)
- **Query flow:** Parse → Optimize (plan from statistics) → Execute → Buffer pool → Disk
- **Durability:** change → log record first → data page later (checkpoint)
- **Speed:** right index + SARGable query + good statistics
- **Concurrency:** readers vs writers solved by row versioning (RCSI)
- **Recovery:** RPO decides backup/log strategy, RTO decides HA design
- **Scale:** partition and compress first, then scale out replicas
- **Set-based thinking:** let the engine process sets, not rows

## Top Interview Hotspots
1. Clustered vs non-clustered indexes, covering indexes, key lookups
2. Reading execution plans and fixing slow queries
3. Parameter sniffing: causes and fixes
4. Isolation levels, RCSI vs Snapshot, blocking vs deadlock
5. Window functions, CTEs, APPLY (T-SQL coding rounds)
6. Statistics, cardinality estimation, SARGability
7. Backup/restore strategy, recovery models, RPO/RTO
8. Always On Availability Groups vs FCI vs log shipping
9. Partitioning, columnstore, compression use cases
10. Row-Level Security, TDE, Always Encrypted, auditing

---

# Cut-Down Strategy

## Tier 1: Master in depth (~60% of effort)
1. Indexing (clustered, non-clustered, covering, filtered, SARGability)
2. Execution plans and tuning workflow
3. T-SQL: joins, CTEs, window functions, APPLY
4. Transactions, isolation levels, RCSI, locking, deadlocks
5. Statistics and parameter sniffing
6. Query Store and wait stats
7. Database design: normalisation, keys, constraints, data types
8. Backup/restore, recovery models, RPO/RTO
9. Always On AG basics and Azure SQL HA options
10. Security: roles, least privilege, RLS, TDE, Always Encrypted

## Tier 2: Working knowledge (~30%)
- Stored procedures, functions, error handling patterns
- Temporal tables, CDC / Change Tracking
- Partitioning, compression, columnstore
- tempdb behaviour and contention
- Monitoring, SQL Agent jobs, maintenance
- Migration paths (on-prem to Azure SQL / MI)
- ETL / data movement (ADF / SSIS)

## Tier 3: Awareness only (~10%)
- In-Memory OLTP, Service Broker
- Replication topologies, Resource Governor
- Ledger, PolyBase
- SQLCLR, spatial, full-text, XML indexes

## Drop for now
- Deep storage-engine page internals beyond interview awareness
- Mirroring (deprecated), legacy features
- Rarely used admin features you will not touch

---

# Steady 6-Week Plan

*Assumes ~1 to 1.5 hrs/day. With less time, stretch to 8-9 weeks, same order. Do not skip Tier 1.*

| Week | Focus | Output |
|---|---|---|
| **1** | Architecture, T-SQL fundamentals, logical processing, joins, CTEs, window functions | Solve 25 T-SQL problems (ranking, running total, gaps and islands, recursive CTE) |
| **2** | Database design, constraints, data types, temporal tables, partitioning basics | Design a normalised schema with constraints, temporal table and audit columns |
| **3** | Indexing, statistics, execution plans, SARGability | Take 5 slow queries, read actual plans, fix with indexes/rewrites, record before/after IO and time |
| **4** | Transactions, isolation, locking, deadlocks, RCSI; Query Store, wait stats, parameter sniffing | Reproduce blocking and a deadlock; fix with RCSI and access ordering; force a plan in Query Store |
| **5** | Programmability, security, HA/DR | Stored proc with TRY/CATCH and TVP; RLS + masking demo; full + diff + log backup and point-in-time restore |
| **6** | Scalability, Azure SQL, operations + interview revision | Partition + compress a large table; compare Azure SQL options; mock interviews on Top 10 |

## Daily rhythm
- **30 min** concept (one module)
- **45 min** hands-on (run it on a sample DB such as AdventureWorks / WideWorldImporters)
- **15 min** revision (5 lines: problem → SQL Server answer → trade-off)

## Weekly checkpoints
- **Day 6:** Revise using Mental Model + Top Interview Hotspots
- **Day 7:** Explain 3 topics aloud as in an interview (why this, trade-offs, alternatives)

## Architect-standard test for every Tier 1 topic
You are ready when you can answer all four:
1. **What problem** does it solve?
2. **How** does SQL Server implement it?
3. **Trade-offs** and failure modes?
4. **When would you NOT use it?**