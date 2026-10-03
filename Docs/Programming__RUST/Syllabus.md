# Rust: Architect Awareness Guide (Tier C)

**Flags:** `R` Required · `O` Optional · `E` Exam oriented · `L` Real life use
**Level:** Awareness. You will not be writing Rust daily. Goal: know where Rust fits, when a team is right to choose it, what it costs, and how to evaluate a Rust proposal in a design review.
**Per module:** Topics (flagged) → How Rust solves it
**Baseline:** current stable Rust (2024 edition). Verify ecosystem maturity (async runtimes, web frameworks, cloud SDK coverage) against the libraries your project needs.

---

## 1. Positioning & Business Case

### Topics
- What Rust is for: systems-level performance with memory safety, no garbage collector — R, E, L
- Most admired language in Stack Overflow's survey for nine consecutive years; admiration is not the same as hiring pool — R, E, L
- Where Rust is adopted: infrastructure, security-sensitive code, AI inference tooling, WebAssembly, CLI tools — R, E, L
- Memory-safety argument (a large share of serious vulnerabilities in C/C++ code are memory-safety bugs) — R, E, L
- Rust vs C/C++ vs Go vs Java vs C# decision logic — R, E, L
- Talent market: smaller pool, higher salary premium, longer onboarding — R, E, L
- Governance: Rust Foundation, editions, release cadence (six weeks) — O, E

### How Rust solves it
| Problem | Rust answer |
|---|---|
| Memory bugs in systems code (use-after-free, data races) | Ownership and borrowing checked at compile time |
| GC pauses and runtime overhead | No garbage collector, no runtime |
| Performance vs safety trade-off | Zero-cost abstractions with safety guarantees |
| Safe incremental adoption | FFI with C, bindings for Python/Node/.NET, WebAssembly targets |

---

## 2. Core Language Model

### Topics
- Ownership, move semantics, borrowing, lifetimes — R, E, L
- Why the borrow checker causes the learning curve — R, E, L
- Enums, pattern matching, `Option` and `Result` (no null, no exceptions) — R, E, L
- Traits and generics (static dispatch) vs trait objects (dynamic dispatch) — R, E, L
- Error handling with `Result`, `?` operator, `thiserror` / `anyhow` — R, E, L
- Immutability by default, `mut`, interior mutability (`RefCell`, `Mutex`) — O, E
- Smart pointers (`Box`, `Rc`, `Arc`) — O, E
- Macros (declarative and procedural) — O, E
- `unsafe`: what it permits, why it is contained — R, E, L
- Compile times and binary size as real costs — R, E, L

### How Rust solves it
| Problem | Rust answer |
|---|---|
| Null reference errors | `Option<T>` |
| Unchecked exceptions | `Result<T, E>` forces explicit handling |
| Data races | Ownership rules + `Send` / `Sync` traits |
| Polymorphism without runtime cost | Generics (monomorphisation), traits |
| Escape hatch for low-level work | `unsafe` blocks, auditable and localised |

---

## 3. Concurrency & Async

### Topics
- "Fearless concurrency": compile-time data-race prevention — R, E, L
- Threads, channels, `Arc<Mutex<T>>` — O, E, L
- Async/await model, futures, executor-based runtimes — R, E, L
- Tokio (dominant async runtime), async-std (declining) — R, E, L
- Function colouring and async ecosystem complexity — R, E, L
- Rayon for data parallelism — O, L
- Comparison with Go goroutines and Java virtual threads — R, E, L
- Cancellation, backpressure, structured concurrency patterns — O, E

### How Rust solves it
| Problem | Rust answer |
|---|---|
| Shared-state bugs in concurrent code | Compiler rejects data races |
| High-concurrency I/O services | Tokio + async/await |
| CPU-parallel workloads | Rayon, threads |
| Message passing | Channels (`std::sync::mpsc`, `crossbeam`, `tokio::sync`) |

---

## 4. Ecosystem & Tooling

### Topics
- Cargo: build, dependency management, workspaces, features — R, E, L
- crates.io, semantic versioning, `Cargo.lock` — R, E, L
- `rustup`, toolchains, editions, MSRV — R, L
- Clippy, rustfmt, rust-analyzer — R, L
- `cargo audit`, `cargo deny`, supply chain hygiene — R, E, L
- Cross-compilation, static linking (musl) — R, E, L
- Small, dependency-free container images (scratch/distroless) — R, E, L
- Compile-time performance: incremental builds, `sccache`, mold linker — O, L
- Cargo praised as a major reason for adoption (most admired cloud dev tool in the survey) — R, E

### How Rust solves it
| Problem | Rust answer |
|---|---|
| Reproducible builds | `Cargo.lock`, workspaces |
| Code quality | Clippy, rustfmt, strict compiler |
| Dependency vulnerabilities | `cargo audit` / `cargo deny` + RustSec advisory DB |
| Deploy anywhere | Single static binary, cross-compilation targets |

---

## 5. Web, API & Service Development

### Topics
- Frameworks: Axum (Tokio-aligned, current favourite), Actix Web, Rocket — R, E, L
- Serde (serialisation) — R, E, L
- gRPC with Tonic — R, E, L
- HTTP clients: reqwest, hyper — O, L
- Database access: sqlx (compile-time checked queries), Diesel, SeaORM — R, E, L
- Auth, JWT, OAuth2 crates — O, L
- Observability: `tracing`, `tracing-subscriber`, OpenTelemetry — R, E, L
- OpenAPI generation (utoipa) — O, L
- Ecosystem maturity vs Java/.NET (fewer enterprise libraries) — R, E, L

### How Rust solves it
| Problem | Rust answer |
|---|---|
| High-throughput low-latency API | Axum / Actix on Tokio |
| Typed JSON handling | Serde |
| Typed SQL | sqlx compile-time query checks |
| RPC between services | Tonic (gRPC) |
| Structured telemetry | `tracing` + OpenTelemetry exporters |

---

## 6. Cloud, Serverless & Microservices

### Topics
- AWS Lambda with Rust via `cargo-lambda` (custom runtime; cold starts in roughly 10-30 ms in vendor benchmarks) — R, E, L
- Azure Functions, Cloud Run, containers with Rust binaries — O, L
- Tiny container images and fast autoscaling — R, E, L
- Memory and cost efficiency per request — R, E, L
- Cloud SDK coverage: AWS SDK for Rust (GA), Azure SDK for Rust (verify maturity) — R, E, L
- When Go is the safer microservice choice vs Rust — R, E, L
- Kubernetes operators and controllers: `kube-rs` — O, E
- Proxies and data planes (Linkerd2-proxy, Pingora, Envoy-adjacent tools) — O, E

### How Rust solves it
| Problem | Rust answer |
|---|---|
| Cold starts and memory in serverless | Native binary, tiny footprint |
| Cost per request at scale | Low CPU and memory use |
| Networking-heavy infrastructure | Async I/O + memory safety |
| Kubernetes-native tools | `kube-rs`, `k8s-openapi` |

---

## 7. AI & Data Infrastructure

### Topics
- Rust's role: inference runtimes, tokenizers, vector databases, embedded inference — not model training — R, E, L
- Examples: Hugging Face tokenizers, Candle, Polars, `uv` (Python package manager written in Rust) — R, E, L
- Python front end, Rust back end pattern (PyO3, maturin) — R, E, L
- Python orchestration with Rust hot paths vs full rewrites — R, E, L
- "Use an existing serving stack (e.g. vLLM) before rewriting in Rust" cost-of-engineering argument — R, E, L
- WebAssembly for in-browser and edge inference — O, E
- Data engineering: Polars, DataFusion, Arrow — O, E, L

### How Rust solves it
| Problem | Rust answer |
|---|---|
| Python performance bottleneck | Rust extension via PyO3 |
| Fast tokenisation / data processing | Rust-native libraries wrapped for Python |
| Low-latency, low-footprint inference | Candle, ONNX Runtime bindings, llama.cpp-style cores |
| Safe edge deployment | Compile to WebAssembly or small native binaries |

---

## 8. Security & Reliability

### Topics
- Memory safety as security control (government and industry guidance favouring memory-safe languages) — R, E, L
- What Rust does not prevent: logic bugs, `unsafe` misuse, dependency risk — R, E, L
- Supply chain: crates.io trust model, typosquatting, `cargo vet` — R, E, L
- Panics vs error handling, abort strategy — O, E
- Fuzzing (`cargo-fuzz`), Miri for undefined behaviour — O, E
- Rust in OS and platform code (Linux kernel, Android, Windows components) — R, E, L

### How Rust solves it
| Problem | Rust answer |
|---|---|
| Memory-safety vulnerabilities | Safe Rust prevents them by construction |
| Auditing risky code | `unsafe` boundaries are explicit and grep-able |
| Dependency trust | `cargo audit`, `cargo deny`, `cargo vet` |

---

## 9. Testing, Build & DevOps

### Topics
- Built-in testing (unit tests, doc tests, integration tests) — R, L
- Property testing (proptest), benchmarking (Criterion) — O, L
- CI caching for slow builds — R, L
- Docker multi-stage builds, static binaries — R, E, L
- Cross-platform release pipelines — O, L
- Observability and production profiling (flamegraph, tokio-console) — O, L

### How Rust solves it
| Problem | Rust answer |
|---|---|
| Test culture | Tests ship with the toolchain |
| Slow CI | `sccache`, cargo caching, incremental builds |
| Minimal runtime images | Static binary on scratch/distroless |

---

## 10. Architect Decision Points

### Topics
- When to choose Rust: latency-critical paths, memory-constrained or embedded targets, security-sensitive components, shared core compiled to many platforms — R, E, L
- When not to choose Rust: CRUD-heavy line-of-business apps, fast prototyping, teams without Rust experience, ecosystem-gap domains — R, E, L
- Rust vs Go (productivity and hiring vs performance and safety) — R, E, L
- Rust vs Java/C# (ecosystem and talent vs footprint and predictability) — R, E, L
- Incremental adoption: rewrite one hot path or one sidecar, not the whole system — R, E, L
- Cost model: slower delivery, steeper onboarding, higher salaries, lower infrastructure bill — R, E, L
- Business risk rating: medium — R, E, L

### How Rust solves it
| Question | Rust position |
|---|---|
| Throughput per dollar | Best in class |
| Time to first feature | Slower than Go, Java, C#, Python, TypeScript |
| Hiring | Smaller pool, premium pay |
| Safety guarantees | Strongest among mainstream languages |
| Enterprise library coverage | Thinner than Java/.NET |

---

## Mental Model (one line each)
- **Core bargain:** pay in compile-time effort to get memory safety and speed without a garbage collector
- **Where it wins:** hot paths, infrastructure, tooling, edge, and anything that must be small, fast and safe
- **Where it loses:** time-to-market, hiring, and broad enterprise library coverage
- **Adoption pattern:** start with a sidecar, a library or a Python extension, not a full rewrite
- **AI stack reality:** Python on top, Rust or CUDA underneath
- **Risk:** talent scarcity and ecosystem gaps matter more than language quality

## Top Interview / Client Conversation Hotspots
1. When would you choose Rust over Go (or Java/C#), and when not
2. Ownership and borrowing explained in business terms: what bug classes disappear
3. What Rust does not protect against
4. Rust for serverless: cold starts, cost, tooling gaps
5. Rust in the AI stack: PyO3 extensions, tokenizers, inference runtimes
6. Incremental adoption strategy for a Java/.NET/Python estate
7. Hiring and onboarding cost model
8. Async Rust complexity and the Tokio ecosystem
9. Supply chain security for crates
10. Compile times and CI impact

---

# Cut-Down Strategy (Tier C awareness)

## Tier 1: Know cold (~60%)
1. Positioning: where Rust wins and loses
2. Ownership and borrowing in business terms
3. Decision logic vs Go, Java, C#, C++
4. Serverless and container footprint advantages
5. AI infrastructure role and the Python + Rust pattern
6. Incremental adoption strategy
7. Cost model: hiring, onboarding, build times

## Tier 2: Working vocabulary (~30%)
- Tokio, Axum, Serde, sqlx, Tonic
- Cargo, workspaces, `cargo audit` / `cargo deny`
- `Result` / `Option` error model
- PyO3 and WebAssembly integration
- Security claims and limits of `unsafe`

## Tier 3: Name recognition only (~10%)
- Lifetimes in depth, trait objects, macros
- Embedded Rust, `no_std`, kernel-level Rust
- Polars, DataFusion, Candle internals
- Miri, fuzzing tooling

## Skip entirely
- Syntax-level tutorials
- Writing production Rust code
- Deep async runtime internals

---

# Awareness Plan (2 weeks, ~45 min/day)

| Week | Focus | Output |
|---|---|---|
| **1** | Positioning, ownership/borrowing in business terms, error model, concurrency and async overview, ecosystem and tooling | One-page memo: "What bug classes Rust removes and what it does not" and "Rust vs Go vs Java decision table" |
| **2** | Serverless and cloud footprint, AI infrastructure pattern (PyO3), security and supply chain, adoption strategy | Decision document: "Where I would introduce Rust in a Java/.NET/Python estate, and the cost model" |

## Optional hands-on (1 to 2 hours total, not required)
- Run a "hello world" Axum service and containerise it to see the image size
- Build a tiny PyO3 function and call it from Python to see the integration model

## Daily rhythm
- **25 min** read one module
- **10 min** write 3 lines: problem → Rust answer → trade-off
- **10 min** compare with the Go or Java equivalent

## Architect-awareness test
You are ready when you can answer:
1. **When would I recommend Rust** to a client, and when would I talk them out of it?
2. **What does it cost** in hiring, delivery speed and build time?
3. **What safety guarantees** are real, and what is marketing?
4. **How would I introduce it** incrementally into an existing estate?