# .NET Core: Architect + Developer Revision Guide

**Flags:** `R` Required · `O` Optional · `E` Exam oriented · `L` Real life use
**Per module:** Topics (flagged) → How .NET Core solves it

---

## 1. Platform & Runtime

### Topics
- CLR, JIT, AOT (Native AOT) — R, E
- .NET SDK vs Runtime vs ASP.NET Core Runtime — R, E
- .NET Standard vs .NET Framework vs .NET (5+) — R, E
- LTS vs STS releases — R, L
- Assemblies, NuGet, target frameworks (TFM) — R, L
- Garbage Collection (generations, LOH, workstation vs server GC) — R, E, L
- Stack vs heap, value vs reference types, boxing/unboxing — R, E
- Span<T>, Memory<T>, ArrayPool — O, L
- Cross-platform, self-contained vs framework-dependent publish — R, L
- Single-file publish, ReadyToRun, trimming — O, L

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| Run anywhere (Linux, Windows, containers) | Cross-platform runtime, `dotnet publish -r <rid>` |
| Fast startup, small footprint | ReadyToRun, Native AOT, trimming |
| Automatic memory management | Generational GC, Server vs Workstation GC |
| Zero-copy, low-allocation processing | `Span<T>`, `Memory<T>`, `ArrayPool<T>` |
| Dependency packaging | NuGet, Central Package Management |
| Version strategy | LTS for production, STS for experiments |

---

## 2. C# Language Essentials

### Topics
- OOP: SOLID, abstraction, polymorphism, interfaces vs abstract classes — R, E
- Generics, constraints, variance — R, E
- Delegates, events, Func/Action/Predicate — R, E
- Lambdas, LINQ (deferred vs immediate execution) — R, E, L
- async/await, Task, ValueTask, ConfigureAwait — R, E, L
- Records, init-only, pattern matching, nullable reference types — R, L
- Extension methods, partial classes, attributes — R
- IDisposable, using, finalizers — R, E
- Reflection, source generators — O
- Collections: List, Dictionary, HashSet, Concurrent, Immutable — R, E
- Exception handling patterns — R, L
- Threading: Thread, ThreadPool, lock, SemaphoreSlim, Interlocked — R, E, L
- Parallel, PLINQ, Channels — O, L

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| Non-blocking I/O | `async/await`, `Task`, `ValueTask` |
| Data querying | LINQ (`IEnumerable` vs `IQueryable`) |
| Immutable DTOs | `record`, `init`, `required` |
| Null safety | Nullable reference types |
| Producer/consumer | `System.Threading.Channels` |
| Thread safety | `lock`, `SemaphoreSlim`, `ConcurrentDictionary`, `Interlocked` |
| Resource cleanup | `IDisposable`, `IAsyncDisposable`, `using` |

---

## 3. ASP.NET Core Fundamentals

### Topics
- Hosting model: Host, WebApplication, Kestrel, IIS, reverse proxy — R, E, L
- Program.cs, minimal hosting model — R, E
- Middleware pipeline (order, Use/Run/Map) — R, E, L
- Request lifecycle — R, E
- Routing: conventional vs attribute, endpoint routing — R, E
- Configuration: appsettings, env vars, User Secrets, Options pattern (IOptions, IOptionsSnapshot, IOptionsMonitor) — R, E, L
- Environments (Dev/Staging/Prod) — R, L
- Logging: ILogger, providers, Serilog, structured logging — R, L
- Static files, CORS, HTTPS, HSTS — R, L
- Model binding, validation (DataAnnotations, FluentValidation) — R, E, L
- Filters: Authorization, Resource, Action, Exception, Result — R, E, L
- Content negotiation, formatters, ProblemDetails — R, L
- Health checks — R, L
- Rate limiting, response caching, output caching, response compression — O, L

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| Web server | Kestrel (behind Nginx / IIS / YARP) |
| Cross-cutting request logic | Middleware pipeline (`app.Use`) |
| Per-endpoint logic | Filters (Action, Exception, Authorization) |
| Settings per environment | `appsettings.{Env}.json`, env vars, Options pattern |
| Strongly typed config | `IOptions`, `IOptionsSnapshot`, `IOptionsMonitor` |
| Logging | `ILogger<T>` + Serilog / OpenTelemetry providers |
| Input validation | Data annotations, `IValidatableObject`, FluentValidation |
| Liveness / readiness | `AddHealthChecks()`, `MapHealthChecks()` |
| Abuse protection | Built-in `RateLimiter` middleware |
| Standard errors | `ProblemDetails`, `IExceptionHandler` |

---

## 4. Dependency Injection

### Topics
- Service lifetimes: Transient, Scoped, Singleton — R, E, L
- Captive dependency problem — R, E, L
- Registration patterns, Keyed services — R, E
- Constructor injection vs others — R
- Scope per request, scope in background services — R, L
- Open generics, decorator pattern — O, L
- Third-party containers (Autofac) — O

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| Loose coupling | Built-in `IServiceCollection` container |
| Object lifetime control | `AddTransient / AddScoped / AddSingleton` |
| Multiple implementations | Keyed services, `IEnumerable<T>` injection |
| Scoped work outside requests | `IServiceScopeFactory` |
| Cross-cutting wrapping | Decorators (Scrutor) |
| Config binding | `services.Configure<T>()` |

---

## 5. API Development

### Topics
- Controllers vs Minimal APIs — R, E, L
- REST principles, HTTP verbs, status codes, idempotency — R, E, L
- API versioning — R, L
- Swagger / OpenAPI — R, L
- Pagination, filtering, sorting — R, L
- gRPC — O, E, L
- GraphQL (HotChocolate) — O
- SignalR / WebSockets — O, E, L
- Minimal API filters, endpoint groups — O, E
- HttpClient, IHttpClientFactory, typed clients — R, E, L
- Resilience: Polly, retry, circuit breaker, timeout, bulkhead — R, L

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| Build REST APIs | Controllers or Minimal APIs |
| Contract docs | Swashbuckle / built-in OpenAPI |
| Evolve APIs | `Asp.Versioning` |
| Service-to-service calls | `IHttpClientFactory`, typed clients |
| Fault tolerance | `Microsoft.Extensions.Http.Resilience` / Polly |
| High-performance RPC | gRPC (`Grpc.AspNetCore`) |
| Real-time push | SignalR |
| Edge routing | YARP reverse proxy |

---

## 6. Data Access

### Topics
- EF Core: DbContext lifetime, tracking vs no-tracking — R, E, L
- Migrations, code-first vs database-first — R, E, L
- Relationships, loading (eager, lazy, explicit) — R, E, L
- N+1 problem, Include, projection — R, E, L
- Concurrency (RowVersion, optimistic) — R, E, L
- Transactions, Unit of Work — R, L
- Query filters, global filters, soft delete — O, L
- Compiled queries, split queries, bulk operations — O, L
- Dapper / ADO.NET — R, L
- Repository pattern: when and when not — R, E, L
- Multiple DB providers, NoSQL (MongoDB, Cosmos DB) — O, L
- Connection pooling — R, L

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| ORM | EF Core (`DbContext` = Unit of Work + Repository) |
| Schema evolution | EF Migrations |
| Read performance | `AsNoTracking`, projection (`Select`), compiled queries |
| N+1 | `Include`, `AsSplitQuery`, projection |
| Concurrent updates | `[Timestamp]` / `IsConcurrencyToken` |
| Raw speed | Dapper, ADO.NET |
| Soft delete / multi-tenant | Global query filters |
| Atomic multi-step | `BeginTransaction`, implicit transaction in `SaveChanges` |
| Bulk operations | `ExecuteUpdate`, `ExecuteDelete` |

---

## 7. Security

### Topics
- Authentication vs authorization — R, E
- JWT, Bearer tokens, refresh tokens — R, E, L
- OAuth2, OpenID Connect flows — R, E, L
- ASP.NET Core Identity — R, E, L
- Cookie auth vs token auth — R, E
- Policy-based, role-based, claims-based authorization — R, E, L
- Azure AD / Entra ID, Microsoft Identity Platform — R, L
- Data Protection API — O, E
- OWASP Top 10, CSRF, XSS, SQL injection, CORS — R, E, L
- Secrets management (Key Vault, User Secrets) — R, L
- API key, mTLS — O

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| Authentication | `AddAuthentication().AddJwtBearer()`, Cookies, OIDC |
| User store | ASP.NET Core Identity |
| Authorization | `[Authorize]`, policies, requirements, handlers |
| External IdP | Microsoft.Identity.Web (Entra ID) |
| Secrets | User Secrets (dev), Key Vault (prod) |
| CSRF | Antiforgery middleware |
| App data encryption | Data Protection API |
| CORS | `AddCors()` policies |

---

## 8. Architecture & Design Patterns

### Topics
- Clean Architecture, Onion, Hexagonal — R, E, L
- N-Tier vs layered vs modular monolith — R, E, L
- Microservices vs monolith trade-offs — R, E, L
- DDD: entities, value objects, aggregates, bounded context, domain events — R, E, L
- CQRS, MediatR, Event Sourcing — R, E, L
- Vertical Slice architecture — O, L
- GoF patterns (Factory, Strategy, Decorator, Observer, Singleton) — R, E
- Specification, Result, Mediator, Outbox patterns — O, L
- API Gateway (YARP, Ocelot), BFF — R, L
- Saga, distributed transactions, eventual consistency — R, E, L
- Idempotency, retry safety — R, L
- Strangler fig, anti-corruption layer — O, L

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| Layer separation | Solution/project structure (Domain, Application, Infrastructure, API) |
| CQRS | MediatR or hand-rolled handlers |
| Domain events | `INotification` / EF `SaveChanges` interception |
| Gateway | YARP, Ocelot |
| Distributed workflows | MassTransit Sagas, NServiceBus |
| Reliable messaging | Outbox pattern (MassTransit / EF Core outbox) |
| Cross-service orchestration | .NET Aspire, Dapr |
| Mapping | Mapperly, AutoMapper |

---

## 9. Messaging & Background Processing

### Topics
- IHostedService, BackgroundService — R, E, L
- Worker Services — R, L
- Message brokers: RabbitMQ, Azure Service Bus, Kafka — R, L
- MassTransit / NServiceBus — O, L
- Hangfire / Quartz.NET — O, L
- Pub/sub, queues, dead-letter, at-least-once delivery — R, E, L

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| Long-running tasks | `BackgroundService`, `IHostedService` |
| Dedicated worker | Worker Service template |
| Scheduling | Hangfire, Quartz.NET |
| Messaging | Azure Service Bus SDK, RabbitMQ.Client, Confluent.Kafka, MassTransit |
| Graceful shutdown | `IHostApplicationLifetime`, `CancellationToken` |
| In-process queue | `Channel<T>` |

---

## 10. Caching

### Topics
- IMemoryCache, IDistributedCache — R, E, L
- Redis — R, L
- Cache-aside, write-through, invalidation, expiry — R, E, L
- HybridCache — O, L
- Response / output caching — O, L

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| Single-node cache | `IMemoryCache` |
| Multi-node cache | `IDistributedCache` (Redis, SQL Server) |
| Stampede protection + L1/L2 | `HybridCache` |
| HTTP-level caching | Response caching, Output caching |

---

## 11. Performance & Scalability

### Topics
- Async all the way, avoid blocking (`.Result` / `.Wait`) — R, E, L
- Thread pool starvation — R, E, L
- Profiling: dotnet-trace, dotnet-counters, dotnet-dump, BenchmarkDotNet — O, L
- Allocation reduction, pooling, streaming — O, L
- Horizontal scaling, stateless design, sticky sessions — R, L
- Load balancing, health probes — R, L

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| Thread starvation | Async I/O everywhere, no `.Result` |
| Diagnosing | `dotnet-counters`, `dotnet-trace`, `dotnet-dump`, PerfView |
| Micro-benchmarks | BenchmarkDotNet |
| Bandwidth | Response compression, streaming (`IAsyncEnumerable`) |
| Stateless scaling | Distributed cache + external session/state |
| Request throttling | Rate limiter, concurrency limiter |

---

## 12. Observability

### Topics
- Logging, metrics, tracing (three pillars) — R, E, L
- OpenTelemetry — R, L
- Application Insights, Prometheus, Grafana, ELK/Seq — O, L
- Correlation IDs, distributed tracing — R, L

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| Logs | `ILogger` + Serilog / Seq / ELK |
| Metrics | `System.Diagnostics.Metrics`, `Meter` |
| Traces | `ActivitySource`, `Activity` (W3C trace context) |
| Unified export | OpenTelemetry .NET SDK |
| Cloud APM | Application Insights |
| Correlation | `TraceId` auto-propagation via `HttpClient` |

---

## 13. Testing

### Topics
- Unit testing: xUnit, NUnit, MSTest — R, L
- Mocking: Moq, NSubstitute — R, L
- Integration testing: WebApplicationFactory, Testcontainers — R, L
- TDD, test pyramid — R, E
- Contract testing, load testing — O, L
- Code coverage, mutation testing — O

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| Unit | xUnit + Moq / NSubstitute |
| API integration | `WebApplicationFactory<T>` |
| Real dependencies | Testcontainers for .NET |
| DB test isolation | SQLite / Testcontainers (EF InMemory is limited) |
| Assertions | FluentAssertions / Shouldly |
| Coverage | Coverlet |

---

## 14. DevOps & Deployment

### Topics
- Docker, multi-stage builds, container images for .NET — R, E, L
- Kubernetes basics (Deployments, Services, Ingress, probes) — R, L
- CI/CD (Azure DevOps, GitHub Actions) — R, L
- Azure App Service, AKS, Azure Functions, Container Apps — R, L
- Config per environment, feature flags — R, L
- Blue/green, canary deployments — O, L
- .NET Aspire — O, L

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| Containerise | Official `mcr.microsoft.com/dotnet/*` images, multi-stage Dockerfile, `dotnet publish /t:PublishContainer` |
| K8s readiness | Health check endpoints, graceful shutdown |
| Cloud hosting | App Service, AKS, Container Apps, Azure Functions |
| Local multi-service dev | .NET Aspire AppHost |
| CI/CD | `dotnet restore / build / test / publish` in Azure DevOps or GitHub Actions |
| Feature flags | `Microsoft.FeatureManagement` |

---

## 15. UI Layer Awareness

### Topics
- MVC, Razor Pages — R, E
- Blazor (Server, WASM, Hybrid) — O, E
- Web API + SPA (Angular/React) integration — R, L
- Static hosting, CORS, auth with SPA — R, L

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| Server-rendered | MVC, Razor Pages |
| C# in browser | Blazor Server / WASM / Hybrid |
| SPA backend | Web API + CORS + JWT/BFF |
| SPA hosting | `UseStaticFiles`, SPA fallback, YARP |

---

## 16. Cross-Cutting Concerns

### Topics
- Global exception handling (middleware, IExceptionHandler) — R, E, L
- Validation strategy — R, L
- Auditing, multi-tenancy — O, L
- Localization, globalization — O
- Feature flags, configuration reload — O, L
- Mapping (AutoMapper, Mapperly, manual) — R, L

### How .NET Core solves it
| Problem | .NET answer |
|---|---|
| Global errors | `IExceptionHandler`, `UseExceptionHandler`, ProblemDetails |
| Validation | Filters / endpoint filters / pipeline behaviors |
| Auditing | EF `SaveChangesInterceptor` |
| Multi-tenancy | Global query filters + tenant middleware |
| Localization | `IStringLocalizer`, `RequestLocalization` |

---

## Mental Model (one line each)
- **Request flow:** Client → Kestrel → Middleware → Routing → Filters → Controller/Endpoint → Service → Repository/DbContext → DB
- **Everything is DI:** services registered in Program.cs, resolved per scope
- **Config flows in:** appsettings → env vars → secrets → Options
- **Async end to end:** never block threads
- **Layers depend inward:** Domain at the centre, infrastructure at the edge
- **Distributed means failure:** retry, timeout, circuit breaker, idempotency, observability

## Top Interview Hotspots
1. Middleware order and the request pipeline
2. DI lifetimes and captive dependency
3. async/await internals and deadlocks
4. EF Core performance (N+1, tracking, concurrency)
5. JWT / OAuth2 / OIDC flow
6. Clean Architecture, CQRS, DDD trade-offs
7. Microservices communication, saga, outbox
8. GC, memory leaks, thread pool starvation
9. Minimal API vs Controllers
10. Docker / K8s deployment of .NET apps

---

# Cut-Down Strategy

## Tier 1: Master in depth (~60% of effort)
1. Middleware pipeline + request lifecycle
2. DI lifetimes + captive dependency
3. async/await + thread pool + GC
4. EF Core (tracking, N+1, concurrency, transactions)
5. AuthN/AuthZ (JWT, OAuth2/OIDC, policies)
6. Clean Architecture + DDD basics + CQRS
7. Minimal APIs vs Controllers, filters, ProblemDetails
8. Resilience (HttpClientFactory + Polly), health checks
9. Observability (OpenTelemetry, logging, tracing)
10. Microservices communication: sync vs async, outbox, saga

## Tier 2: Working knowledge (~30%)
- Caching (Memory, Redis, HybridCache)
- Background services, messaging basics (Service Bus / RabbitMQ)
- Testing (xUnit, WebApplicationFactory, Testcontainers)
- Docker + K8s deployment of .NET apps
- Options pattern, config, secrets
- API versioning, OpenAPI, gRPC overview
- YARP / API Gateway

## Tier 3: Awareness only (~10%)
- Blazor, SignalR, GraphQL
- Native AOT, Span/Memory internals
- Hangfire / Quartz, NServiceBus
- Aspire, Dapr, event sourcing
- Localization, multi-tenancy, mutation testing

## Drop for now
- Deep C# reflection and source generators
- Advanced profiling (PerfView deep dives)
- Custom formatters, middleware internals beyond basics
- Framework-era topics (WCF, Web Forms, classic ASP.NET)

---

# Steady 6-Week Plan

*Assumes ~1 to 1.5 hrs/day. With less time, stretch to 8-9 weeks, same order. Do not skip Tier 1.*

| Week | Focus | Output |
|---|---|---|
| **1** | Runtime, C# async, GC, DI, middleware pipeline | One-page notes on request lifecycle + DI lifetimes; small API with custom middleware and scoped/singleton demo |
| **2** | API layer: Minimal API/Controllers, filters, validation, ProblemDetails, config/Options, logging | API with versioning, global exception handler, Options-bound config, Serilog |
| **3** | EF Core + Dapper, transactions, concurrency, caching | EF Core with migrations, fix a deliberate N+1, optimistic concurrency, Redis/HybridCache |
| **4** | Security: JWT, OIDC with Entra ID, policies, secrets, OWASP | Secure the API with JWT + policy-based auth; Key Vault / User Secrets |
| **5** | Architecture: Clean Architecture, DDD, CQRS/MediatR, resilience, messaging, outbox, saga | Refactor into 4 layers + CQRS; one async flow via Service Bus/RabbitMQ with outbox |
| **6** | Observability, testing, Docker/K8s, CI/CD, interview revision | OpenTelemetry tracing, Testcontainers integration tests, containerise + pipeline; mock interviews on Top 10 |

## Daily rhythm
- **30 min** concept (one module)
- **45 min** hands-on (implement in the sample project)
- **15 min** revision (5 lines: problem → .NET answer → trade-off)

## Weekly checkpoints
- **Day 6:** Revise using Mental Model + Top Interview Hotspots
- **Day 7:** Explain 3 topics aloud as in an interview (why this, trade-offs, alternatives)

## Architect-standard test for every Tier 1 topic
You are ready when you can answer all four:
1. **What problem** does it solve?
2. **How** does .NET implement it?
3. **Trade-offs** and failure modes?
4. **When would you NOT use it?**