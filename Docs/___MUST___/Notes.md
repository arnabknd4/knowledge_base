# Language Portfolio for an Architect Career (October 2026)

---

## 1. Market Signals

- **Python**: Still dominant (~19% TIOBE July 2026) but slipping.  
- **TypeScript**: Overtook Python/JavaScript on GitHub contributors (Aug 2025).  
- **Rust**: Most admired (Stack Overflow 2025), but adoption is niche.  
- **Enterprise languages**: Java, C#, C++, still strong; PHP declining.  

---

## 2. Recommended Portfolio

| Tier | Languages | Expected Depth |
|------|-----------|----------------|
| **A: Own the trade-offs** | TypeScript, Python, SQL, + one enterprise (C# or Java) | Justify design choices, review code, runtime limits |
| **B: Working architect level** | Go, + the other of C#/Java | Pick for right service, estimate adoption cost |
| **C: Awareness only** | Rust, Kotlin, Mojo/Zig | Know where they fit, when to choose |

**Note**: You already cover .NET, Angular/React, Node, SQL Server, Python, Go. Gaps: Java (awareness) and Rust (Tier C).

---

## 3. Grouping by Domain

| Domain | Primary | Secondary | Watch | Architect’s Decision |
|--------|---------|-----------|-------|----------------------|
| **Full stack** | TypeScript | C#/Java, Python | Kotlin Multiplatform | One language end-to-end vs best-fit per tier |
| **Backend** | Java, C#, Python | Go, TypeScript (Node) | Rust, Kotlin | Team skills vs runtime efficiency |
| **Front end** | TypeScript | – | WebAssembly (Rust) | Framework > language |
| **Microservices** | Java, Go, C# | Python, TypeScript | Rust | Limit service languages (2–3 max) |
| **Serverless** | Python, TypeScript | Go, C#, Java | Rust | Cold-start latency vs ecosystem |
| **Cloud computing** | Python, Go | TypeScript (IaC) | Rust | Terraform DSL vs Pulumi/CDK |
| **AI development** | Python | TypeScript | Rust (infra), Mojo | Python orchestration vs compiled hot paths |

---

## 4. Evidence & Trade-offs

- **Microservices**:  
  - Java 21+ virtual threads remove old performance concerns.  
  - Go popular for lightweight services.  
  - .NET unified runtime (.NET 8/9/10).  
  - **Rule**: Max 2–3 service languages per org.

- **Serverless**:  
  - Python/Node fastest interpreted.  
  - Go/Rust → native binaries.  
  - Java viable with SnapStart/GraalVM.  
  - .NET 10 Native AOT improves Lambda startup.  
  - **Rule**: Benchmark workloads before committing.

- **Cloud computing**:  
  - Python → automation, scripting, AI tooling.  
  - Go → Kubernetes, Terraform, cloud infra.  
  - Pulumi/CDK → TypeScript, Python, Go, C#, Java.  
  - **Trade-off**: Terraform DSL simpler; code IaC more flexible but complex.

- **AI development**:  
  - Python = default for ML/AI SDKs.  
  - TypeScript = AI features in full-stack apps.  
  - Rust = infra (serving runtimes, tokenizers).  
  - Mojo = promising but immature.  
  - **Pattern**: Python front end + Rust/CUDA back end.

---

## 5. Language Decision Matrix

| Language | Wins | Loses | Risk | Verdict |
|----------|------|-------|------|---------|
| **TypeScript** | Full stack, front end, IaC, AI features | CPU-heavy, enterprise libs | Low | Tier A |
| **Python** | AI/ML, automation, serverless glue | Performance, type discipline | Low | Tier A |
| **SQL** | Data modelling, reporting | Not general-purpose | Very low | Tier A |
| **C#/.NET** | Enterprise backends, Azure, Native AOT | Smaller serverless tooling | Low | Tier A/B |
| **Java** | Enterprise, long-lived systems | Verbosity, heavier footprint | Low | Tier A/B |
| **Go** | Microservices, cloud tooling | Less expressive, thin ecosystem | Low | Tier B |
| **Rust** | Infra, latency-critical, safety | Hiring cost, slower delivery | Medium | Tier C |
| **Kotlin** | JVM, Android | Smaller backend share | Low | Tier C |
| **Mojo/Zig** | Systems niches | Immature ecosystems | High | Watch only |
| **PHP/Ruby** | Legacy, CMS | Declining | Medium | Skip |

---

## 6. 12-Month Plan

| Phase | Months | Focus | Architect-Level Output |
|-------|--------|-------|-------------------------|
| **1** | 1–3 | TypeScript + Python discipline; SQL tuning; one enterprise stack | Reference service + runtime trade-off memo |
| **2** | 4–6 | Go for microservices; second enterprise language | Compare Go vs enterprise (cold start, memory, operability) |
| **3** | 7–9 | AI engineering (Python orchestration, TypeScript integration) | RAG + agent reference architecture |
| **4** | 10–12 | Rust awareness; IaC (Terraform vs Pulumi/CDK); governance | One-page language-selection policy |

---

## 7. Selection Heuristic

- Weigh in order:  
  1. Team skills & hiring pool  
  2. Ecosystem & libraries  
  3. Runtime profile (latency, memory, cold start)  
  4. Operability & observability  
  5. Security & supply chain  
  6. Long-term maintainability (10–15 years)

- **Rule**: Adopt a new language only if it beats the incumbent on **≥2 factors**.

---

## Caveats

- Rankings measure different things (search interest, GitHub contributors, developer opinion).  
- Local job-market demand not included → check firms/cities before finalising.  
- Revision-document format can be built for Go, Python, Java next.
