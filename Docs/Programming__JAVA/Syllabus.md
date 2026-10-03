# Java: Architect Awareness Guide

**Flags:** `R` Required · `O` Optional · `E` Exam oriented · `L` Real life use
**Level:** Awareness. You are not writing Java daily. Goal: review designs, challenge estimates, advise on trade-offs, and hold your own in a client or interview conversation.
**Per module:** Topics (flagged) → How Java solves it
**Baseline:** current LTS (Java 25) with Java 26 as the latest release. Verify version-specific features (structured concurrency, scoped values, Valhalla value classes, Leyden AOT cache) against the version your client runs.

---

## 1. Platform, Releases & Strategy

### Topics
- JDK vs JRE vs JVM, OpenJDK distributions (Temurin, Corretto, Zulu, Oracle) — R, E, L
- Six-month release cadence, LTS versions (8, 11, 17, 21, 25) — R, E, L
- Licensing and support model (Oracle JDK vs OpenJDK builds) — R, L
- Migration paths: 8 → 11 → 17 → 21 → 25 — R, E, L
- Jakarta EE namespace change (`javax` → `jakarta`) — R, E, L
- Build tools: Maven, Gradle — R, L
- Backward compatibility as a business strength — R, E, L
- Java vs C# vs Go vs Kotlin positioning — R, E, L

### How Java solves it
| Problem | Java answer |
|---|---|
| Long-lived enterprise systems | Strong backward compatibility, 10 to 15 year lifespans |
| Predictable upgrades | LTS releases + vendor-supported distributions |
| Vendor lock-in worry | Multiple OpenJDK vendors |
| Library breakage on upgrade | Gradual migration tooling (OpenRewrite, jdeps) |
| Namespace migration | `javax` → `jakarta` (Spring Boot 3+, Jakarta EE 9+) |

---

## 2. Language Evolution (Modern Java)

### Topics
- Records, sealed classes, pattern matching (`switch`, records) — R, E, L
- Text blocks, `var`, enhanced `switch` — R, L
- Virtual threads (Java 21+) — R, E, L
- Structured concurrency, scoped values (check version status) — O, E
- Streams, Optional, `CompletableFuture` — R, E, L
- Generics and type erasure — R, E
- Modules (JPMS) — O, E
- Project Valhalla (value classes), Panama (foreign function API), Amber, Loom — O, E
- Verbosity vs explicitness trade-off — R, L

### How Java solves it
| Problem | Java answer |
|---|---|
| Boilerplate-heavy data classes | Records |
| Closed type hierarchies | Sealed classes + pattern matching |
| Thread-per-request cost | Virtual threads |
| Complex async/reactive code | Virtual threads reduce the need for reactive style |
| Native interop without JNI | Foreign Function and Memory API (Panama) |
| Memory overhead of objects | Valhalla value classes (in progress, check status) |

---

## 3. JVM Internals & Runtime Behaviour

### Topics
- JIT (C1/C2), tiered compilation, warm-up — R, E, L
- Garbage collectors: G1, ZGC (generational), Shenandoah, Parallel, Serial — R, E, L
- Heap sizing, GC tuning basics, container-aware JVM — R, E, L
- Memory model, `volatile`, happens-before — O, E
- Class loading, metaspace — O, E
- JFR (Flight Recorder), JMX, heap dumps, thread dumps — R, E, L
- Common production issues: memory leaks, GC pauses, thread starvation, OOM in containers — R, E, L
- Startup time and memory footprint trade-offs — R, E, L

### How Java solves it
| Problem | Java answer |
|---|---|
| Throughput vs latency goals | Choice of collector (G1 balanced, ZGC low pause, Parallel throughput) |
| Peak performance after warm-up | Tiered JIT |
| Production diagnosis | JFR, JMX, `jcmd`, heap/thread dumps |
| Slow startup, big footprint | CRaC, AppCDS, Leyden, GraalVM native image |
| Container memory limits | Container-aware JVM ergonomics |

---

## 4. Frameworks & Application Development

### Topics
- Spring Framework, Spring Boot (current major: 4) — R, E, L
- Dependency injection, auto-configuration, profiles — R, E, L
- Spring MVC vs WebFlux (reactive) — R, E, L
- Quarkus, Micronaut, Helidon (cloud-native alternatives) — R, E, L
- Jakarta EE, MicroProfile — O, E, L
- Spring Data (JPA, MongoDB, Redis) — R, E, L
- Spring Security (OAuth2, JWT, OIDC) — R, E, L
- Spring Cloud (config, gateway, circuit breaker) — R, E, L
- Build and dependency management (BOMs, Maven vs Gradle) — R, L
- Kotlin with Spring — O, L

### How Java solves it
| Problem | Java answer |
|---|---|
| Fast enterprise app delivery | Spring Boot (opinionated defaults, starters) |
| Fast startup, small footprint | Quarkus / Micronaut (build-time processing, native image) |
| High concurrency with simple code | Spring MVC on virtual threads |
| Non-blocking streaming workloads | Spring WebFlux / Reactor |
| Data access | Spring Data, Hibernate/JPA, jOOQ, JDBC |
| Security | Spring Security (OAuth2 resource server, method security) |
| Configuration | Spring Config / externalised config / env |

---

## 5. Microservices & Distributed Systems

### Topics
- Spring Cloud vs Kubernetes-native approaches — R, E, L
- API gateway: Spring Cloud Gateway, Kong — R, E, L
- Resilience: Resilience4j (circuit breaker, retry, bulkhead, rate limiter) — R, E, L
- Messaging: Kafka, RabbitMQ, Spring Cloud Stream — R, E, L
- Service discovery, config management — R, L
- Saga, outbox, idempotency patterns in Java — R, E, L
- gRPC, REST, GraphQL in Java — O, E, L
- Observability: Micrometer, OpenTelemetry — R, E, L
- Distributed tracing and correlation — R, L
- Multi-language landscape: where Java sits vs Go and .NET — R, E, L

### How Java solves it
| Problem | Java answer |
|---|---|
| Fault tolerance | Resilience4j |
| Event streaming | Kafka (Java-native client and ecosystem) |
| Reliable messaging | Outbox via Debezium + Spring |
| Metrics and traces | Micrometer + OpenTelemetry |
| API edge | Spring Cloud Gateway / external gateways |
| Distributed config | Spring Cloud Config / Kubernetes ConfigMaps |

---

## 6. Data Access & Persistence

### Topics
- JDBC, connection pools (HikariCP) — R, E, L
- JPA / Hibernate: entity lifecycle, lazy loading, N+1, caching — R, E, L
- Transactions (`@Transactional`, propagation, isolation) — R, E, L
- jOOQ, MyBatis, Spring JdbcTemplate — O, E, L
- Schema migrations: Flyway, Liquibase — R, L
- NoSQL: MongoDB, Redis, Cassandra clients — O, L
- Optimistic vs pessimistic locking — R, E, L
- Multi-tenancy patterns — O, L

### How Java solves it
| Problem | Java answer |
|---|---|
| ORM | JPA / Hibernate |
| N+1 and lazy loading pitfalls | Fetch joins, entity graphs, projections |
| Transaction management | Declarative `@Transactional` |
| Schema evolution | Flyway / Liquibase |
| Connection management | HikariCP |
| SQL-first control | jOOQ / JdbcTemplate |

---

## 7. Serverless & Cloud-Native Java

### Topics
- Lambda / Azure Functions cold start problem — R, E, L
- AWS Lambda SnapStart — R, E, L
- GraalVM native image: benefits, build cost, reflection limits — R, E, L
- Quarkus / Micronaut / Spring native for serverless — R, E, L
- Containers: JIB, buildpacks, distroless, memory settings — R, E, L
- Kubernetes: probes, resource limits, graceful shutdown — R, L
- Right-sizing JVM in containers — R, E, L
- Cloud SDKs (AWS SDK v2, Azure SDK) — R, L

### How Java solves it
| Problem | Java answer |
|---|---|
| Cold starts | SnapStart, native image, CRaC |
| Image build without Dockerfile | JIB, Spring Boot buildpacks |
| Footprint reduction | Native image, jlink, class data sharing |
| Cloud-managed integration | AWS SDK v2, Azure SDK, Google Cloud client libraries |

---

## 8. Security

### Topics
- OWASP Top 10 in Java apps — R, E, L
- Spring Security, OAuth2/OIDC, JWT — R, E, L
- Deserialisation vulnerabilities, Log4Shell-class supply chain risks — R, E, L
- Dependency scanning (OWASP Dependency-Check, Snyk, Dependabot) — R, E, L
- Secrets management (Vault, Key Vault, Secrets Manager) — R, L
- TLS, keystores, certificates — R, L
- SBOM, signed artefacts — O, E, L
- Security Manager removal (awareness) — O

### How Java solves it
| Problem | Java answer |
|---|---|
| AuthN/AuthZ | Spring Security, Keycloak integration |
| Supply chain | Dependency scanning + SBOM (CycloneDX) |
| Input handling | Bean Validation, parameterised queries |
| Secrets | Vault / cloud secret managers |

---

## 9. Testing, Build & DevOps

### Topics
- JUnit 5, Mockito, AssertJ — R, L
- Spring Boot Test, slices — R, L
- Testcontainers — R, E, L
- Contract testing (Pact) — O, L
- Maven vs Gradle trade-offs — R, E, L
- CI/CD for Java (build caching, layered jars) — R, L
- Static analysis (SonarQube, SpotBugs, Checkstyle) — R, L
- Code coverage (JaCoCo) — R, L
- Observability in production (Actuator) — R, E, L

### How Java solves it
| Problem | Java answer |
|---|---|
| Realistic integration tests | Testcontainers |
| Fast feedback | JUnit 5 + Spring test slices |
| Quality gates | SonarQube, JaCoCo thresholds |
| Production health | Spring Boot Actuator |

---

## 10. Architect Decision Points (where Java earns or loses the choice)

### Topics
- Java vs C#/.NET for enterprise — R, E, L
- Java vs Go for microservices — R, E, L
- Java vs Kotlin on the JVM — R, E, L
- Java vs Node/TypeScript for APIs — R, E, L
- Monolith vs microservices on the JVM — R, E, L
- Legacy modernisation: strangler fig, JVM upgrade, framework migration — R, E, L
- Hiring pool, cost of talent, long-term maintainability — R, E, L
- Cloud cost: footprint and startup vs developer productivity — R, E, L

### How Java solves it
| Question | Java position |
|---|---|
| Long-term enterprise stability | Strongest argument for Java |
| Talent availability | Very large pool |
| Container density and startup | Weaker than Go unless native image / CRaC |
| Developer productivity | Improving (records, virtual threads) but more verbose than Kotlin |
| Ecosystem breadth | Among the broadest (Kafka, Spark, Elasticsearch, Cassandra ecosystems) |

---

## Mental Model (one line each)
- **Strength:** stable, enormous ecosystem, huge talent pool, ideal for long-lived systems
- **Cost:** heavier footprint and slower startup than Go or Rust unless you invest in native image, CRaC or SnapStart
- **Concurrency:** virtual threads let you write blocking code that scales
- **Framework reality:** Spring Boot is the default, Quarkus/Micronaut for startup-sensitive workloads
- **Operations:** JFR, GC choice and container-aware sizing decide production behaviour
- **Risk:** supply chain and dependency hygiene

## Top Interview / Client Conversation Hotspots
1. Why Java for this system vs Go, .NET or Node
2. Virtual threads vs reactive: when each is right
3. Cold start and footprint options: SnapStart, native image, CRaC
4. JVM in containers: memory sizing, GC choice, OOM diagnosis
5. JPA/Hibernate pitfalls: N+1, lazy loading, transaction scope
6. Spring Boot vs Quarkus vs Micronaut
7. Migration strategy across LTS versions and the `javax` → `jakarta` change
8. Resilience patterns and Kafka-based event design
9. Supply chain security and dependency governance
10. Modernising a legacy Java monolith

---

# Cut-Down Strategy (awareness level)

## Tier 1: Know cold (~60%)
1. Release cadence, LTS and migration strategy
2. Virtual threads vs reactive trade-off
3. JVM runtime behaviour: JIT warm-up, GC choice, container sizing
4. Spring Boot architecture and the Quarkus/Micronaut alternative
5. Startup and footprint options (SnapStart, native image, CRaC)
6. JPA/Hibernate pitfalls and transactions
7. Java vs .NET vs Go vs Kotlin decision logic
8. Security and supply chain risks
9. Legacy modernisation approaches

## Tier 2: Working vocabulary (~30%)
- Records, sealed classes, pattern matching
- Resilience4j, Kafka, Micrometer/OpenTelemetry
- Maven vs Gradle, Testcontainers, JUnit 5
- Spring Security / OAuth2
- JFR and basic production diagnosis

## Tier 3: Name recognition only (~10%)
- Valhalla, Panama, Leyden, structured concurrency status
- JPMS, Jakarta EE and MicroProfile specifics
- Helidon, Vert.x, jOOQ, MyBatis

## Skip entirely
- Syntax-level Java, language basics
- Applets, EJB 2.x, legacy JSP/Struts
- Deep JVM bytecode and classloader internals

---

# Awareness Plan (3 weeks, ~45 min/day)

| Week | Focus | Output |
|---|---|---|
| **1** | Platform and runtime: LTS strategy, modern language features, virtual threads, GC choices, container sizing | One-page memo: "Virtual threads vs reactive vs Go goroutines" and "GC choice by workload" |
| **2** | Frameworks, microservices, data: Spring Boot vs Quarkus/Micronaut, Resilience4j, Kafka, JPA pitfalls, security | Sketch a service architecture; list 5 JPA/Spring pitfalls and the fix for each |
| **3** | Serverless, cloud-native, decision points: SnapStart, native image, CRaC, Java vs .NET/Go, modernisation | Decision table "when I would pick Java" and a modernisation approach for a legacy monolith |

## Daily rhythm
- **25 min** read one module
- **10 min** write 3 lines: problem → Java answer → trade-off
- **10 min** compare with the .NET or Go equivalent you already know

## Architect-awareness test
You are ready when you can answer:
1. **When would I pick Java** over my default stack, and why?
2. **What does it cost** (footprint, startup, verbosity) and how do I mitigate it?
3. **What are the top 3 production risks** on the JVM?
4. **How would I modernise** a legacy Java system?