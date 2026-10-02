# Node.js: Architect + Developer Revision Guide

**Flags:** `R` Required · `O` Optional · `E` Exam oriented · `L` Real life use
**Per module:** Topics (flagged) → How Node.js solves it
**Baseline:** current LTS Node.js, TypeScript-first backend work. Verify version-specific features (built-in test runner, `--watch`, permission model, native `fetch`) against the LTS you target.

---

## 1. Runtime & Internals

### Topics
- V8 engine, JIT, event loop, libuv, thread pool — R, E, L
- Single-threaded model, non-blocking I/O — R, E, L
- Event loop phases (timers, pending, poll, check, close) — R, E
- `process.nextTick` vs `setImmediate` vs `Promise` microtasks — R, E
- Call stack, heap, garbage collection — R, E
- Node.js vs browser runtime — R, E
- CPU-bound vs I/O-bound workloads — R, E, L
- LTS vs Current releases, version managers (nvm, fnm) — R, L
- `process` object, signals, exit codes — R, L
- Globals: `fetch`, `AbortController`, `structuredClone` — O, L

### How Node.js solves it
| Problem | Node.js answer |
|---|---|
| Handle many concurrent connections cheaply | Event loop + non-blocking I/O (libuv) |
| Fast JS execution | V8 JIT compilation |
| Blocking file/DNS/crypto work | libuv thread pool |
| Deferred execution control | `nextTick`, microtasks, `setImmediate` |
| Version management | LTS channel + nvm / fnm |
| Graceful stop | `process.on('SIGTERM')` handlers |

---

## 2. JavaScript / TypeScript Essentials

### Topics
- Closures, scope, `this`, prototypes — R, E
- Promises, `async/await`, error propagation — R, E, L
- `Promise.all`, `allSettled`, `race`, `any` — R, E, L
- ES modules vs CommonJS (`import` vs `require`) — R, E, L
- Destructuring, spread, optional chaining — R
- Generators, iterators, async iterators — O, E
- Classes, inheritance, mixins — R
- TypeScript: types, generics, utility types, strict mode — R, E, L
- Immutability, pure functions — R, L

### How Node.js solves it
| Problem | Node.js answer |
|---|---|
| Async code readability | Native `async/await` |
| Module organisation | ESM + CommonJS interop, `package.json` `type` field |
| Type safety | TypeScript with `tsc`, `tsx`, `ts-node` |
| Parallel async tasks | `Promise.all` / `allSettled` |
| Streaming data iteration | Async iterators (`for await`) |

---

## 3. Core Modules

### Topics
- `fs` (callbacks, promises, streams) — R, E, L
- `path`, `os`, `url`, `util` — R, L
- `events` (`EventEmitter`) — R, E, L
- `http` / `https` modules — R, E
- `crypto` (hashing, HMAC, random, encryption) — R, E, L
- `stream` (Readable, Writable, Duplex, Transform, pipeline) — R, E, L
- `buffer` — R, E
- `child_process` (spawn, exec, fork) — R, E, L
- `worker_threads` — R, E, L
- `cluster` module — R, E, L
- `zlib`, `net`, `dns` — O
- `readline`, `process.stdin` — O
- `node:test`, `assert` — O, L

### How Node.js solves it
| Problem | Node.js answer |
|---|---|
| Large file handling | Streams + `pipeline` (backpressure handled) |
| Event-driven design | `EventEmitter` |
| Use all CPU cores | `cluster` / PM2 / container replicas |
| CPU-heavy work | `worker_threads` |
| Run external programs | `child_process` |
| Hashing / signing | `crypto` module |
| Binary data | `Buffer` |

---

## 4. Asynchronous Patterns & Concurrency

### Topics
- Callback hell → Promises → async/await evolution — R, E
- Error handling in async code, unhandled rejections — R, E, L
- Backpressure in streams — R, E, L
- Concurrency control (p-limit, queues) — R, L
- `AbortController`, timeouts, cancellation — R, L
- `AsyncLocalStorage` (request context) — R, E, L
- Race conditions, idempotency — R, E, L
- Avoiding event-loop blocking — R, E, L
- Event loop lag measurement — O, L

### How Node.js solves it
| Problem | Node.js answer |
|---|---|
| Cancel slow operations | `AbortController` + `AbortSignal.timeout` |
| Per-request context (trace ID) | `AsyncLocalStorage` |
| Limit parallel work | p-limit / queue libraries / BullMQ |
| Memory-safe streaming | `stream.pipeline` + backpressure |
| Crash on unhandled errors | `process.on('unhandledRejection')` + restart policy |

---

## 5. Web Frameworks & API Development

### Topics
- Express: routing, middleware, error middleware — R, E, L
- Fastify (schemas, plugins, hooks, performance) — R, E, L
- NestJS (modules, controllers, providers, DI, guards, pipes) — R, E, L
- Koa, Hapi (awareness) — O
- REST design, status codes, idempotency, versioning — R, E, L
- Request validation (Zod, Joi, class-validator, Ajv) — R, E, L
- Pagination, filtering, sorting — R, L
- OpenAPI / Swagger — R, L
- GraphQL (Apollo, Mercurius) — O, E, L
- gRPC — O, E, L
- WebSockets (ws, Socket.IO), SSE — O, E, L
- File upload (multer, streaming) — R, L
- Rate limiting, CORS, helmet — R, E, L
- Centralised error handling — R, E, L

### How Node.js solves it
| Problem | Node.js answer |
|---|---|
| Build REST APIs fast | Express / Fastify / NestJS |
| Structured large backends | NestJS (modular, DI, decorators) |
| Input validation | Zod / Joi / Fastify JSON schema |
| API docs | `swagger-ui-express`, `@nestjs/swagger`, Fastify swagger |
| Real-time push | Socket.IO / `ws` / SSE |
| Security headers | `helmet`, `cors` |
| Abuse protection | `express-rate-limit`, `@fastify/rate-limit` |

---

## 6. Databases & Data Access

### Topics
- SQL drivers: `pg`, `mysql2`, `mssql` — R, L
- ORMs/query builders: Prisma, TypeORM, Sequelize, Drizzle, Knex — R, E, L
- MongoDB: native driver, Mongoose — R, E, L
- Connection pooling — R, E, L
- Transactions — R, E, L
- Migrations — R, L
- N+1 and query optimisation — R, E, L
- Redis (caching, sessions, queues) — R, L
- Repository pattern, data mapper vs active record — R, E
- Schema validation at boundary — R, L

### How Node.js solves it
| Problem | Node.js answer |
|---|---|
| Relational access | Prisma / TypeORM / Knex / Drizzle |
| Document access | Mongoose / MongoDB driver |
| Connection reuse | Driver-level pools (`pg.Pool`) |
| Schema evolution | Prisma Migrate / Knex migrations / TypeORM migrations |
| Caching | `ioredis` / `redis` client |

---

## 7. Security

### Topics
- AuthN vs AuthZ — R, E
- JWT, refresh tokens, session cookies — R, E, L
- OAuth2 / OIDC (Passport, openid-client, Auth0 SDKs) — R, E, L
- Password hashing (bcrypt, argon2) — R, E, L
- OWASP Top 10 for Node (injection, XSS, SSRF, prototype pollution) — R, E, L
- Input sanitisation, parameterised queries — R, E, L
- Secrets management (env vars, vaults) — R, L
- `helmet`, CORS, CSRF protection — R, E, L
- Dependency risk: `npm audit`, lockfiles, supply chain — R, E, L
- RBAC / ABAC / policy checks — R, E, L
- Rate limiting, brute-force protection — R, L
- Node permission model — O

### How Node.js solves it
| Problem | Node.js answer |
|---|---|
| Authentication | Passport.js, `jsonwebtoken` / `jose`, OIDC libraries |
| Password storage | `bcrypt` / `argon2` |
| HTTP hardening | `helmet`, `cors`, CSRF middleware |
| Supply chain | `npm audit`, `npm ci`, lockfile, Dependabot / Snyk |
| Secret handling | Env vars + Key Vault / Secrets Manager / Vault |

---

## 8. Architecture & Design Patterns

### Topics
- Layered architecture (controller → service → repository) — R, E, L
- Clean / Hexagonal architecture — R, E, L
- Modular monolith vs microservices — R, E, L
- Dependency injection (NestJS, awilix, tsyringe) — R, E, L
- CQRS, event-driven design, event sourcing — O, E, L
- Domain-driven design basics — R, E, L
- API Gateway, BFF — R, L
- Saga, outbox, idempotency — R, E, L
- 12-factor app — R, E, L
- Monorepo (Nx, Turborepo, pnpm workspaces) — O, L
- Design patterns: Factory, Strategy, Observer, Singleton — R, E

### How Node.js solves it
| Problem | Node.js answer |
|---|---|
| Structure and DI | NestJS modules + providers |
| Event-driven decoupling | `EventEmitter`, brokers (RabbitMQ, Kafka, SQS) |
| Gateway | Fastify / Express gateway, Kong, KrakenD in front |
| Monorepos | Nx / Turborepo / pnpm workspaces |
| Config discipline | `dotenv` / `@nestjs/config` / `env-var` + validation |

---

## 9. Messaging & Background Processing

### Topics
- Job queues: BullMQ (Redis), Agenda — R, E, L
- Message brokers: RabbitMQ, Kafka, SQS, Service Bus — R, E, L
- Pub/sub, at-least-once, dead-letter queues — R, E, L
- Cron / scheduling (`node-cron`, BullMQ repeatable) — R, L
- Retry, exponential backoff, idempotency — R, E, L
- Event streaming vs queueing — R, E
- Serverless workers (Lambda, Functions) — O, L

### How Node.js solves it
| Problem | Node.js answer |
|---|---|
| Background jobs | BullMQ + Redis |
| Broker integration | `amqplib`, `kafkajs`, cloud SDKs |
| Scheduled jobs | `node-cron`, BullMQ repeatables, cloud schedulers |
| Reliability | Retry + DLQ + idempotency keys |

---

## 10. Performance & Scalability

### Topics
- Never block the event loop — R, E, L
- Clustering, PM2, horizontal scaling — R, E, L
- Caching strategies (in-memory, Redis, HTTP cache) — R, E, L
- Profiling: `--inspect`, clinic.js, `0x`, flamegraphs — O, L
- Memory leaks: heap snapshots, common causes — R, E, L
- Streaming vs buffering responses — R, E, L
- Load testing (autocannon, k6, Artillery) — O, L
- Compression, keep-alive, HTTP/2 — O, L
- Database query tuning, indexes — R, L
- Stateless services, sticky sessions — R, E

### How Node.js solves it
| Problem | Node.js answer |
|---|---|
| Use multi-core | `cluster`, PM2, container replicas |
| CPU spikes | `worker_threads`, offload to queue |
| Memory issues | Heap snapshots (Chrome DevTools), `--max-old-space-size` |
| Benchmark | `autocannon`, k6 |
| Faster frameworks | Fastify, schema-based serialisation |

---

## 11. Observability

### Topics
- Structured logging (pino, winston) — R, L
- Log levels, correlation IDs — R, L
- Metrics (Prometheus, `prom-client`) — R, L
- Distributed tracing (OpenTelemetry) — R, L
- Health and readiness endpoints — R, L
- Error tracking (Sentry, App Insights) — R, L
- Diagnostics: `node --inspect`, `diagnostics_channel` — O

### How Node.js solves it
| Problem | Node.js answer |
|---|---|
| Fast structured logs | pino |
| Metrics | `prom-client` |
| Tracing | OpenTelemetry Node SDK (auto-instrumentation) |
| Request correlation | `AsyncLocalStorage` + logger bindings |
| Error alerts | Sentry / App Insights SDKs |

---

## 12. Testing

### Topics
- Unit testing: Jest, Vitest, Mocha, `node:test` — R, L
- Mocks, stubs, spies — R, L
- HTTP/API testing: Supertest — R, L
- Integration testing with Testcontainers — R, L
- Contract testing (Pact) — O
- TDD, test pyramid — R, E
- Coverage (c8, Istanbul) — R, L
- E2E (Playwright) — O
- Load testing — O, L

### How Node.js solves it
| Problem | Node.js answer |
|---|---|
| Fast unit tests | Jest / Vitest / `node:test` |
| API-level tests | Supertest |
| Real dependencies | Testcontainers for Node |
| Isolation | Dependency injection + mocks |

---

## 13. DevOps & Deployment

### Topics
- Docker (multi-stage, slim/alpine/distroless, non-root user) — R, E, L
- Kubernetes basics (probes, HPA, graceful shutdown) — R, L
- CI/CD (lint, test, build, scan, deploy) — R, L
- Package managers: npm, pnpm, yarn; lockfiles, `npm ci` — R, E, L
- Environment config, secrets — R, L
- Serverless (Lambda, Azure Functions) — O, L
- Process managers (PM2) vs container orchestration — R, E
- Zero-downtime deploys — R, L
- Build tooling: `tsc`, esbuild, SWC, tsup — O, L

### How Node.js solves it
| Problem | Node.js answer |
|---|---|
| Small secure images | Multi-stage Dockerfile + `node:lts-slim` / distroless |
| Reproducible installs | `npm ci` + lockfile |
| Graceful shutdown in K8s | SIGTERM handler: stop accepting, drain, close pools |
| Serverless | Lambda / Azure Functions Node runtimes |
| Fast TS builds | esbuild / SWC / tsup |

---

## 14. Cross-Cutting Concerns

### Topics
- Config management and validation — R, L
- Global error handling (operational vs programmer errors) — R, E, L
- Graceful shutdown — R, E, L
- Validation strategy — R, L
- Internationalisation — O
- Feature flags — O, L
- Date/time handling (UTC, Luxon, date-fns) — R, L
- Pagination and API contracts — R, L

### How Node.js solves it
| Problem | Node.js answer |
|---|---|
| Consistent errors | Central error middleware / NestJS exception filters |
| Config safety | Schema-validated env at startup |
| Clean shutdown | Signal handlers + `server.close()` + pool teardown |
| Time bugs | UTC storage, Luxon / date-fns |

---

## Mental Model (one line each)
- **Request flow:** Client → Reverse proxy → Node process → Middleware → Route handler → Service → DB/Cache/Queue
- **Concurrency:** one thread runs JS, I/O happens off-thread, never block the loop
- **Scale out:** more processes/containers, not bigger threads
- **CPU work:** workers or queues, never inline
- **Streams everywhere:** process data in chunks, respect backpressure
- **Config in env:** 12-factor, validated at boot
- **Fail safe:** timeouts, retries, idempotency, graceful shutdown

## Top Interview Hotspots
1. Event loop phases, `nextTick` vs microtasks vs `setImmediate`
2. Why Node scales for I/O but struggles with CPU work, and the fixes
3. Streams, backpressure, `pipeline`
4. `cluster` vs `worker_threads` vs `child_process`
5. Async error handling and unhandled rejections
6. Express vs Fastify vs NestJS trade-offs
7. Authentication flow (JWT, refresh, OIDC) and security hardening
8. Memory leaks: causes and how to diagnose
9. Microservice patterns in Node (queues, saga, outbox)
10. Docker and K8s deployment with graceful shutdown

---

# Cut-Down Strategy

## Tier 1: Master in depth (~60% of effort)
1. Event loop, async model, libuv, microtasks
2. Promises/async patterns and error handling
3. Streams, Buffers, backpressure
4. Express + Fastify + NestJS fundamentals (pick one deep, know the other two)
5. REST API design, validation, centralised errors
6. Auth: JWT, OIDC, password hashing, OWASP basics
7. DB access: ORM/driver, pooling, transactions
8. Scaling: cluster, workers, stateless design
9. Layered/Clean architecture, DI, 12-factor
10. Observability: logging, metrics, tracing

## Tier 2: Working knowledge (~30%)
- BullMQ / brokers (RabbitMQ, Kafka)
- Redis caching
- Testing (Jest/Vitest, Supertest, Testcontainers)
- Docker + K8s deployment, graceful shutdown
- WebSockets / SSE
- OpenAPI, rate limiting, helmet
- Monorepo tooling

## Tier 3: Awareness only (~10%)
- GraphQL, gRPC
- Serverless runtimes
- Deep V8 internals, native addons (N-API)
- Event sourcing
- Node permission model, SEA (single executable apps)

## Drop for now
- Legacy callback-only patterns beyond interview awareness
- Obscure core modules (`dgram`, `tls` internals)
- Framework-specific edge APIs you won't use

---

# Steady 6-Week Plan

*Assumes ~1 to 1.5 hrs/day. With less time, stretch to 8-9 weeks, same order. Do not skip Tier 1.*

| Week | Focus | Output |
|---|---|---|
| **1** | Event loop, async patterns, core modules (`fs`, `events`, `stream`) | Demo that proves loop phases order; file processor using streams with backpressure |
| **2** | TypeScript setup, Express/Fastify API, validation, error handling | REST API with Zod validation, central error handler, OpenAPI docs |
| **3** | NestJS structure, DI, database access (ORM + pooling + transactions) | Same API in NestJS with Prisma/TypeORM; transaction example |
| **4** | Security: JWT, refresh tokens, OIDC, password hashing, helmet, rate limit | Secured API with RBAC guard; dependency audit in CI |
| **5** | Scaling + messaging: cluster/workers, Redis cache, BullMQ, outbox idea | CPU-heavy task moved to worker; background job with retry + DLQ |
| **6** | Observability, testing, Docker/K8s, CI/CD + interview revision | pino + OpenTelemetry; Supertest + Testcontainers tests; multi-stage image with graceful shutdown; mock interviews on Top 10 |

## Daily rhythm
- **30 min** concept (one module)
- **45 min** hands-on (implement in the sample project)
- **15 min** revision (5 lines: problem → Node answer → trade-off)

## Weekly checkpoints
- **Day 6:** Revise using Mental Model + Top Interview Hotspots
- **Day 7:** Explain 3 topics aloud as in an interview (why this, trade-offs, alternatives)

## Architect-standard test for every Tier 1 topic
You are ready when you can answer all four:
1. **What problem** does it solve?
2. **How** does Node.js implement it?
3. **Trade-offs** and failure modes?
4. **When would you NOT use it?**