---
title: "Master Syllabus, Note Template and AI Prompt"
subtitle: "Experienced .NET Lead (12+ years, Kolkata market) to .NET Architect to Cloud Architect"
---

## PART 1: HOW TO USE THIS DOCUMENT

Purpose: stop deciding and stop collecting. Part 4 lists every topic and concept already chosen for you. Part 2 is the fixed note format. Part 3 is the one-time setup that makes the prompt reusable. You only repeat one loop: send the next topic IDs, read, print, recall.

The loop for each topic:

- Take the next two or three topic IDs from Part 5 (study order).
- Send the IDs to your Claude Project chat (one-time setup in Part 3). Get one note per ID.
- Skim for obvious errors. For exam topics, check the note once against the Microsoft Learn page for that service (15 minutes). Write (verify) beside anything doubtful.
- Paste the notes into the domain Word file (one file per domain, example: D01-dotnet-platform.docx). Do not rewrite or reformat.
- Print in batches of 8 to 10 notes. Tick the box in Part 4 when the note is printed and you have recalled it once from memory on paper.

Rules that protect your time and eyes:

- A concept that is not in the topic line is not needed yet. Write it on the gap list (one A4 page per domain, by hand). Once a month, take all gap lists to the AI in one session. Never browse for extra sources.
- AI notes are drafts. They can be wrong on versions, limits and service names. Anything that changes fast is tagged (verify). Check Microsoft Learn for exam facts.
- One note per topic. Do not make parallel notes from different sources.
- Generate notes in one screen session per batch (about 1 hour). The rest of the week is paper: read, handwrite the recall box, revise with index cards.
- Pace: about 6 notes a month (roughly 12 hours). The remaining time goes to labs, the capstone project and certification exams. Notes do not replace hands-on work.

Tags used in Part 4:

- P1, P2, P3, P4: phase in which to write the note (P1 first).
- R = required for job readiness. O = optional, do after P3 or when a job asks for it.
- E = relevant to Azure certification exams. L = used in real projects.
- K = you probably know most of this from 12 years of work. Generate the note, read once, fill only the gaps. Do not spend extra time.
- (verify) = names, versions or limits that change often. Check the official page.

Note size rule: R topics get a FULL note (one printed page). O topics get a SHORT note (half a page).

Scale (honest numbers): see the totals at the end of Part 4. At 6 notes a month, the R notes alone take about two years, which fits the long plan. You do not need all of them to start applying. Batches 1 to 6 (Phase 1) plus the capstone project and AZ-104 are enough to begin interviews.

## PART 2: NOTE TEMPLATE (VERSION 2, BUILT FOR TOPICS THAT ARE NEW TO YOU)

You do not need to say which topics are new. The tags in the topic line decide the depth.

- No K tag: treat the topic as new to you. Plain words first, then the technical meaning. Define every term when it first appears. Connect it to something you already know from the legacy .NET Framework world. Include a mini lab.
- K tag: skip the basics. Cover gaps, what changed in modern .NET and Azure, and interview depth. No lab unless it is a gap.
- R tag: FULL note, about 700 words, one printed page. O tag: SHORT note, about 300 words, half a page.

FULL NOTE sections (your 9-section template plus three additions: Before you read, Mini lab, Legacy equivalent line):

1. What is it: two or three lines in plain words, then one line starting "Legacy equivalent:" that says what this replaces or resembles in .NET Framework projects.

2. Why needed: the problem it solves and what breaks without it.

3. Before you read: two to four prerequisite ideas, one line each. Skipped for K topics.

4. Features and core concepts: every concept in the topic line. For each: the plain meaning in one short line, then why it matters. Add the one command, code or setting worth memorizing (maximum 6 lines).

5. Core focus (exam and interview): what is asked most, plus defaults and limits to remember.

6. Real-world use case: one project scenario in .NET and Azure terms: situation, choice made, trade-off, and when NOT to use it.

7. Interview lens: four questions with two-line answers.

8. Common mistakes: how each shows up in production, and the fix.

9. Mental model: one picture in words or a tiny text diagram.

10. Mini lab: one exercise of 20 to 40 minutes with exact steps and the result you should see. Use local tools or the Azure free tier and end with a clean-up step. Skipped for K and O topics.

11. Revision summary: five to eight one-line facts to recall from memory.

SHORT NOTE: sections 1, 4, 6 and 11 only.

How a new topic becomes a skill (three passes, about 3 hours in total):

- Pass 1, paper, day 1: read the printed note, close it, then handwrite the recall box under it: "In my own words: ... / I would use it when: ... / I would avoid it when: ..."
- Pass 2, screen, within 3 days: do the mini lab once. Keep labs inside your two weekly screen sessions (Wednesday and Saturday), not on other days.
- Pass 3, use, within 2 weeks: use the topic in the capstone project or in your current work, even in a small way, and answer the four interview questions aloud without looking.
- Revise on day 3, day 10 and day 30 using only the revision summary.

## PART 3: ONE-TIME SETUP, SO YOU NEVER RETYPE THE PROMPT

Where the prompt lives. Do this once:

- Option 1 (best): open your Claude Project "Long term career goal", open Project instructions, and paste the text between the two markers below. Make sure this syllabus is in the Project documents under the name master-syllabus. From then on you type only the topic IDs.
- Option 2: Claude memory. A short version of this template is saved in this Project's memory, so it also applies without the pasted text. Pasted instructions are the safer one, because they are always loaded.
- Option 3 (no Project): paste the same text at the start of a new chat, then send the ID and its topic line from Part 4.

Daily use: send one ID, or up to three IDs in one message (example: 1.03 1.04 1.05). Start a new chat for each batch, because long chats are slower and use more of your allowance.

What this saves: you never retype the prompt and you never paste topic lines. The instructions are still read by the AI every time, but they are short (about 340 words).

START OF INSTRUCTIONS

You are my senior architect mentor and teacher. I am Arnab, a .NET tech lead with 12 years in legacy .NET Framework (MVC, Entity Framework, SQL Server, jQuery, TypeScript, GitLab CI), moving to modern .NET, Azure, microservices and then architect roles, in the Kolkata and remote India job market.

When I send one or more topic IDs (example: 1.03), find each topic line in the project document master-syllabus and write one study note per ID. If an ID is not found, ask me to paste the line. Cover every concept in the topic line and add nothing unrelated.

Depth comes from the tags in the topic line. No K tag means the topic is new to me: plain words first, then the technical meaning, define every term when it first appears, and include the mini lab. K tag means skip the basics and focus on gaps, what changed in modern .NET and Azure, and interview depth. R tag means a FULL note of about 700 words. O tag means a SHORT note of about 300 words with sections 1, 4, 6 and 11 only.

Headings, exactly: 1 What is it (end with one line starting Legacy equivalent:), 2 Why needed, 3 Before you read (two to four prerequisites, one line each), 4 Features and core concepts (each concept: plain meaning, then why it matters), 5 Core focus (exam and interview), 6 Real-world use case (include the trade-off and when not to use it), 7 Interview lens (four questions with two-line answers), 8 Common mistakes, 9 Mental model, 10 Mini lab (20 to 40 minutes, exact steps, expected result, clean-up step, local tools or Azure free tier), 11 Revision summary (five to eight one-line facts).

Style: plain text only, no tables, emojis, bold or decoration. Dash bullets. Short sentences. No introductions or conclusions. Do not invent facts, limits or prices. Write (verify) next to any version, service name or limit that may have changed. Include code or commands only if worth memorizing, maximum 6 lines. Separate notes with a line of dashes.

END OF INSTRUCTIONS

## PART 4: MASTER SYLLABUS

How to read a line: tick box, topic ID and title, tags, then the concepts to cover. Everything listed is in scope. Anything not listed is out of scope for now.

## D01 .NET PLATFORM AND C\#

☐ **1.01 Runtime and SDK basics** [P1 R L] CLR, JIT, BCL; .NET Framework vs .NET vs .NET Standard; LTS vs STS releases (current LTS, verify); target frameworks; SDK-style csproj; NuGet and versioning; global.json; multi-targeting; side-by-side installs; framework-dependent vs self-contained; ReadyToRun, trimming, native AOT awareness

☐ **1.02 Hosting and startup** [P1 R L] Program.cs; WebApplicationBuilder; generic host; Kestrel; reverse proxy (IIS, Nginx, YARP); environments; launchSettings; forwarded headers; ports and URLs; hosted lifetime and graceful shutdown

☐ **1.03 Dependency injection** [P1 R E L] lifetimes (singleton, scoped, transient); registration patterns; constructor injection; captive dependency; scope validation; keyed services; factory registration; service locator anti-pattern; decorating services; testing with DI

☐ **1.04 Configuration, options and secrets** [P1 R L] sources and precedence (appsettings, environment variables, command line, user secrets, Key Vault); IOptions, IOptionsSnapshot, IOptionsMonitor; validation on start; per-environment config; twelve-factor config; Azure App Configuration; feature flags (FeatureManagement)

☐ **1.05 Middleware and request pipeline** [P1 R L] ordering; Use, Run, Map; custom middleware; exception handling; endpoint routing; filters vs middleware; CORS; compression; rate limiting; HTTPS redirection and HSTS; request buffering

☐ **1.06 Logging and diagnostics** [P1 R L] ILogger and levels; structured logging (Serilog); scopes; correlation IDs; sinks; sampling; dotnet-counters, dotnet-trace, dotnet-dump; health checks endpoints

☐ **1.07 Async and concurrency** [P1 R L] Task and async/await state machine; sync-over-async deadlocks; ConfigureAwait; CancellationToken; ValueTask; Task.WhenAll; concurrency vs parallelism; Channels; SemaphoreSlim; lock; Interlocked; ConcurrentDictionary; thread pool starvation; IAsyncEnumerable

☐ **1.08 Modern C# language** [P1 R L] records; init and required; pattern matching; switch expressions; nullable reference types; primary constructors; collection expressions; tuples and deconstruction; generics and constraints; delegates, events, lambdas; LINQ (deferred execution, IEnumerable vs IQueryable); exception best practices

☐ **1.09 Memory and performance** [P2 R L] value vs reference types; stack and heap; boxing; GC generations; LOH; IDisposable and IAsyncDisposable; Span and Memory; ArrayPool; string allocations; BenchmarkDotNet; profiling (dotnet-trace, PerfView); common leaks (events, statics, HttpClient misuse)

☐ **1.10 HTTP client and serialization** [P1 R L] HttpClient lifetime and socket exhaustion; IHttpClientFactory; typed clients; delegating handlers; resilience handlers (Polly); timeouts; System.Text.Json options; source-generated serialization; Newtonsoft migration

☐ **1.11 Testing in .NET** [P1 R L] xUnit; mocking (Moq, NSubstitute); arrange-act-assert; test doubles; WebApplicationFactory; Testcontainers; database test strategies; test data builders; coverage as a signal; snapshot and contract tests; test pyramid; flaky tests

☐ **1.12 Migrating legacy .NET Framework apps** [P1 R L] assessment (APIs, dependencies, analyzers); .NET Upgrade Assistant; in-place vs strangler (YARP) vs rewrite; System.Web replacements; Web.config to appsettings; Global.asax to middleware; EF6 to EF Core; WCF to CoreWCF, gRPC or REST; Windows-only APIs; session and auth state; side-by-side hosting; rollback plan

☐ **1.13 Advanced .NET** [P3 O] source generators; Roslyn analyzers; reflection and attributes; expression trees; native AOT; P/Invoke; minimal API tuning; .NET Aspire (verify)


## D02 FRONT END

☐ **2.01 JavaScript fundamentals** [P1 R L K] scope, closures, this; prototypes; ES modules; event loop; promises and async; fetch; destructuring; immutability; array methods; error handling; cookies, localStorage, sessionStorage; same-origin policy

☐ **2.02 TypeScript** [P1 R L K] types vs interfaces; generics; unions and intersections; narrowing and type guards; utility types; strict mode; tsconfig; declaration files; mapped and conditional types basics

☐ **2.03 Browser and web fundamentals** [P2 R L] DOM; critical rendering path; reflow and repaint; browser HTTP caching; service workers awareness; CORS; CSP; cookie flags (HttpOnly, Secure, SameSite); DevTools network and performance panels

☐ **2.04 Angular core (primary framework)** [P2 R L] components and templates; standalone components; change detection (default, OnPush, signals); DI in Angular; routing (lazy loading, guards, resolvers); forms (template-driven vs reactive, validation); HttpClient and interceptors; RxJS (map, switchMap, mergeMap, debounceTime, takeUntil, async pipe); state (signals, services, NgRx awareness); testing (unit, Playwright end-to-end); Angular CLI and builds; performance (lazy load, trackBy, bundle analysis); SSR awareness

☐ **2.05 Front-end security and authentication** [P2 R L] OIDC authorization code with PKCE; MSAL for Angular; token storage (memory vs cookie); refresh tokens; XSS prevention; CSRF; CORS configuration in ASP.NET Core; CSP; BFF pattern for SPAs; route guards are not real authorization

☐ **2.06 Front-end architecture for a lead** [P3 R L] feature folder structure; shared libraries; monorepo (Nx) awareness; API client generation from OpenAPI; error handling and telemetry (Application Insights JS); feature flags; environment config; CI for front end (lint, test, build, audit); dependency upgrade policy; design systems; accessibility (WCAG basics); i18n

☐ **2.07 React quick comparison** [P3 O] components; hooks (useState, useEffect, useMemo, useCallback); context; router; React Query and Redux Toolkit; Next.js awareness

☐ **2.08 Blazor, micro-frontends, PWA** [P4 O] Blazor Server vs WebAssembly; module federation; SSR and SSG; PWA basics


## D03 BACK END AND API DESIGN

☐ **3.01 REST API design** [P1 R L] resources and URIs; verb semantics; status codes; idempotency; PUT vs PATCH; pagination (offset vs cursor); filtering and sorting; versioning (URL, header); ETags and concurrency; content negotiation; long-running operations (202 and status); rate limits; maturity model

☐ **3.02 ASP.NET Core Web API implementation** [P1 R L] controllers vs minimal APIs; model binding; validation (DataAnnotations, FluentValidation); filters; ProblemDetails; global exception handling (IExceptionHandler); API versioning library; OpenAPI generation (built-in, Swashbuckle, NSwag); DTO vs entity; mapping libraries pros and cons; output caching

☐ **3.03 Authentication and authorization** [P1 R E L] OAuth 2.0 grants; OIDC; JWT structure and validation; scopes vs roles vs claims; policy-based and resource-based authorization; Entra ID app registrations (app roles, scopes, consent); managed identity; client credentials; on-behalf-of flow; token lifetime, refresh, revocation; ASP.NET Core Identity basics; Entra External ID (verify)

☐ **3.04 Resilience** [P2 R L] timeouts; retry with exponential backoff and jitter; circuit breaker; bulkhead; fallback; rate limiting and load shedding; idempotency keys; deduplication; graceful degradation; health checks (liveness, readiness, startup); graceful shutdown

☐ **3.05 Background processing** [P2 R L] BackgroundService and IHostedService; worker services; queue plus worker pattern; Hangfire and Quartz; scheduled jobs; outbox processors; idempotent jobs; concurrency control; Azure Functions timer and queue triggers; Durable Functions awareness

☐ **3.06 gRPC and real-time** [P3 O] protobuf; unary and streaming; deadlines; gRPC vs REST; gRPC-Web; SignalR; WebSockets; server-sent events; GraphQL awareness

☐ **3.07 API contracts and governance** [P2 R L] OpenAPI-first design; naming and error standards; versioning policy; breaking vs non-breaking changes; consumer-driven contracts (Pact); API Management basics (policies, products, JWT validation, caching, throttling)

☐ **3.08 API security** [P2 R L] OWASP API Top 10; input validation; mass assignment; broken object-level authorization; rate limiting; security headers; secrets handling; SQL injection; SSRF; file upload risks; logging without personal data


## D04 DATABASES AND DATA ACCESS

☐ **4.01 SQL Server internals and indexing** [P2 R L K] pages and extents; clustered vs heap; B-tree and nonclustered indexes; covering and included columns; filtered indexes; statistics; execution plans (scan, seek, lookup, join types); parameter sniffing; plan cache; missing index DMVs; Query Store; tempdb

☐ **4.02 T-SQL for leads** [P2 R L K] joins; window functions; CTEs; set-based vs row-by-row; stored procedures vs inline SQL; temp tables vs table variables; MERGE pitfalls; pagination; JSON support; SARGability; dynamic SQL and injection; bulk operations

☐ **4.03 Transactions, isolation and locking** [P2 R E L K] ACID; isolation levels; read committed snapshot; snapshot isolation; lock types and escalation; deadlocks; blocking diagnosis; optimistic vs pessimistic concurrency; distributed transactions and why to avoid them; retry on deadlock

☐ **4.04 Schema design and data modeling** [P2 R L K] normalization and denormalization trade-offs; keys (natural vs surrogate; GUID vs identity vs sequential GUID); constraints; data types; temporal tables; soft delete; audit columns; multi-tenancy models (shared schema, schema per tenant, database per tenant); partitioning; archiving

☐ **4.05 EF Core** [P1 R L] DbContext lifetime; tracking vs no-tracking; loading strategies; N+1; projections; compiled queries; raw SQL; global filters; concurrency tokens; migrations (scripts, bundles); owned types; value converters; ExecuteUpdate and ExecuteDelete; split queries; interceptors; EF6 vs EF Core differences

☐ **4.06 Dapper, ADO.NET and data access patterns** [P2 R L] Dapper basics; when to prefer it over EF; connection pooling; parameterization; repository and unit of work critique; CQRS read side; specification and query objects; SqlBulkCopy

☐ **4.07 Azure SQL, high availability and disaster recovery** [P1 R E L] deployment options (SQL Database, Managed Instance, SQL on VM); DTU vs vCore; serverless; elastic pools; Hyperscale awareness; backups (point-in-time, long-term retention); geo-replication; failover groups; RPO and RTO; Always On awareness; security (TDE, Always Encrypted, private endpoint, Entra auth); monitoring; migration tools (DMS, DMA, BACPAC)

☐ **4.08 Safe schema change and zero-downtime releases** [P2 R L] expand and contract; backward-compatible migrations; online index operations; data backfill; dual write; feature-flagged cutover; database version control (EF migrations, DACPAC, DbUp, Flyway); database CI; rollback strategy

☐ **4.09 NoSQL and Cosmos DB** [P2 R E L] document, key-value, column and graph types; CAP implications; Cosmos DB (partition key design, request units, consistency levels, change feed, indexing policy, TTL); MongoDB basics (documents, indexes, aggregation, replica set); Table and Blob storage basics; modeling for access patterns; when NoSQL is wrong

☐ **4.10 Analytics and search** [P4 O] OLTP vs OLAP; star schema; ETL vs ELT; Azure Data Factory, Synapse, Fabric awareness; data lake; Elasticsearch and Azure AI Search basics; change data capture


## D05 CACHING

☐ **5.01 Caching fundamentals** [P1 R L] hit ratio and latency; cache-aside, read-through, write-through, write-behind, refresh-ahead; TTL and sliding expiry; invalidation strategies; versioned keys; stampede, penetration and avalanche; negative caching; consistency trade-offs; what not to cache; key design; serialization cost; eviction (LRU, LFU)

☐ **5.02 Caching APIs in .NET** [P1 R L] IMemoryCache (size limits, expiration, eviction callbacks); IDistributedCache; HybridCache (verify); output caching; response caching; two-level cache (local plus distributed); multi-instance consistency issues

☐ **5.03 Redis** [P1 R E L] data structures (string, hash, list, set, sorted set, stream); TTL; eviction policies; persistence (RDB, AOF); replication; clustering and sharding; Sentinel awareness; Azure Cache for Redis and Azure Managed Redis (verify); StackExchange.Redis multiplexer; pipelining; pub/sub; distributed locks and their risks; rate limiting; session storage; big key problems; monitoring (latency, memory, evictions)

☐ **5.04 HTTP and edge caching** [P2 R L] Cache-Control; ETag and If-None-Match; Last-Modified; Vary; max-age and s-maxage; fingerprinted assets; CDN (Azure Front Door, CDN); purge; caching authenticated content risks; reverse-proxy caching awareness

☐ **5.05 Advanced caching** [P3 O] Redis streams; Lua scripts; bloom filters; client-side caching; cache warming; multi-region caches


## D06 MESSAGING AND EVENT-DRIVEN DESIGN

☐ **6.01 Messaging fundamentals** [P1 R L] sync vs async; queue vs topic vs stream; point-to-point vs publish-subscribe; message vs event vs command; delivery semantics (at-most-once, at-least-once, exactly-once myth); ordering; partitions; competing consumers; backpressure; poison messages and dead-letter queues; retry and backoff; TTL; message size; schema versioning; idempotent consumers; claim-check pattern

☐ **6.02 Azure Service Bus** [P1 R E L] queues; topics and subscriptions; filters and rules; sessions; peek-lock vs receive-and-delete; lock duration and renewal; dead-letter queue; scheduled messages; duplicate detection; transactions; Standard vs Premium; managed identity access; .NET SDK processor; monitoring; geo-disaster recovery

☐ **6.03 Event-driven patterns** [P2 R L] outbox and inbox; transactional messaging; saga (orchestration vs choreography); process manager; event notification vs event-carried state transfer; CQRS read-model projections; eventual consistency in the UI; compensating actions; replay; schema registry; event versioning; testing async flows

☐ **6.04 Event Grid and Event Hubs** [P2 R E L] Event Grid (topics, filtering, retry, system events); Event Hubs (partitions, consumer groups, checkpointing, capture); choosing between Service Bus, Event Grid, Event Hubs and Storage Queues

☐ **6.05 Kafka and RabbitMQ concepts** [P3 R L] broker vs log; topics, partitions, offsets, consumer groups; retention and compaction; exchanges and bindings; acknowledgements; ordering guarantees; throughput trade-offs; Kafka Connect awareness; Event Hubs Kafka endpoint; MassTransit, NServiceBus, Wolverine abstractions

☐ **6.06 Workflow engines** [P3 O] Durable Functions; Logic Apps; Temporal awareness; Azure Functions triggers and bindings


## D07 CI/CD AND DEVOPS

☐ **7.01 Git mastery** [P1 R L K] object model; merge vs rebase; cherry-pick; bisect; reflog; stash; tags; hooks; conflict resolution; history rewriting rules; monorepo vs polyrepo; commit conventions; signed commits

☐ **7.02 Branching and release strategies** [P1 R L] trunk-based; GitFlow; GitHub Flow; release and hotfix branches; pull request policies (reviews, required checks, CODEOWNERS); semantic versioning; changelogs; feature flags; environment promotion

☐ **7.03 Azure DevOps** [P1 R E L] organization and project structure; YAML pipelines (triggers, stages, jobs, steps, templates, parameters, variables, variable groups, conditions); agents and pools (hosted vs self-hosted); service connections; environments, approvals and checks; Azure Artifacts feeds; pipeline artifacts; test reporting; Boards (work items, sprints); permissions

☐ **7.04 GitLab CI and GitHub Actions mapping** [P1 R L] GitLab concepts (stages, jobs, rules, runners, artifacts, cache, environments) mapped to Azure Pipelines and GitHub Actions (workflows, actions, runners, reusable workflows, matrix, secrets, OIDC to Azure, environments, caching); migration approach; GH-200 blueprint (verify status)

☐ **7.05 Build, test and scan stages** [P2 R L] restore, build, test, publish for .NET; test reports and coverage; static analysis (SonarQube); SAST; dependency scanning (Dependabot, NuGet audit); secret scanning; container scanning (Trivy, Defender for Cloud); SBOM; quality gates; build caching; artifact versioning; signing

☐ **7.06 Deployment strategies** [P2 R L] blue-green; canary; rolling; recreate; feature-flag releases; App Service slot swaps; traffic shifting; smoke tests; automated rollback; database changes in pipelines; per-environment config; approvals; zero-downtime deployment

☐ **7.07 Infrastructure as code and Terraform** [P1 R E L] IaC principles; Terraform (providers, resources, state, azurerm backend, locking, modules, variables, outputs, locals, workspaces, plan and apply, drift, import, lifecycle, testing with terraform test, tflint, checkov); Bicep and ARM basics and comparison; secrets in IaC; CI for IaC; naming and tagging conventions; Azure Verified Modules awareness

☐ **7.08 Secrets and identity in pipelines** [P2 R L] Key Vault references; managed identity; workload identity federation (OIDC); least-privilege service principals; secret rotation; no secrets in repositories; variable masking; protected branches and environments; pipeline permission hardening

☐ **7.09 Delivery metrics and engineering practice** [P3 R L] DORA metrics; lead time; change failure rate; MTTR; flow metrics; pull request size and review standards; definition of done; inner source; documentation as code

☐ **7.10 GitOps, Ansible, Jenkins awareness** [P4 O] Argo CD and Flux; pull vs push deployment; Ansible (inventory, playbooks, idempotency); Jenkins (pipeline as code, agents); policy as code (OPA, Azure Policy); drift detection


## D08 DOCKER AND KUBERNETES

☐ **8.01 Container fundamentals** [P1 R E L] containers vs VMs; namespaces and cgroups; images and layers; registries; tags vs digests; Dockerfile instructions (FROM, COPY, RUN, ENTRYPOINT vs CMD, ENV, ARG, EXPOSE, USER, HEALTHCHECK); multi-stage builds for .NET; layer caching; .dockerignore; non-root user; image size; BuildKit

☐ **8.02 Docker runtime and local development** [P1 R L] run, exec, logs, inspect; volumes and bind mounts; bridge and host networks; port mapping; environment and secrets; Docker Compose (services, healthchecks, networks, volumes, profiles); debugging containers in Visual Studio and VS Code; local dependencies (SQL Server, Redis, Azurite, emulators)

☐ **8.03 Registry and supply chain** [P1 R E L] Azure Container Registry (SKUs, tasks, geo-replication, private link, managed identity pull); tagging strategy (semver plus git SHA, avoid latest); vulnerability scanning; image signing; SBOM; base image patching; retention policies

☐ **8.04 Kubernetes architecture** [P2 R E L] control plane (API server, etcd, scheduler, controller manager); nodes (kubelet, kube-proxy, runtime); declarative model and reconciliation; namespaces; labels and selectors; kubectl and contexts; manifests; Kustomize

☐ **8.05 Workloads and configuration** [P2 R E L] Pod lifecycle; Deployments and ReplicaSets; rolling update and rollback; StatefulSet; DaemonSet; Job and CronJob; ConfigMap; Secret and the limits of base64; init containers; sidecars; probes (liveness, readiness, startup); requests and limits; QoS classes; PodDisruptionBudget; graceful termination

☐ **8.06 Networking and exposure** [P2 R E L] Services (ClusterIP, NodePort, LoadBalancer); cluster DNS; Ingress and controllers; Gateway API awareness; NetworkPolicy; TLS and cert-manager; AKS networking (kubenet, Azure CNI, overlay); internal vs external load balancers

☐ **8.07 Storage and scaling** [P2 R E L] PV, PVC, StorageClass, CSI; Azure Disk vs Azure Files; HPA; VPA; KEDA (Service Bus scaling); cluster autoscaler; node pools (system, user, spot); affinity, taints and tolerations, topology spread; capacity planning

☐ **8.08 AKS operations** [P2 R E L] cluster and node pool creation; upgrades (channels, surge); managed identity and workload identity; Entra integration and RBAC; ACR integration; monitoring (Container Insights, managed Prometheus and Grafana); ingress options; Defender; policy; cost control; private clusters; SLA tiers

☐ **8.09 Kubernetes troubleshooting** [P2 R L] describe, logs, events, exec, port-forward, top; CrashLoopBackOff; ImagePullBackOff; OOMKilled; Pending pods; failing probes; DNS and service issues; config errors; node NotReady; stuck rollouts; ephemeral debug containers; runbook habit

☐ **8.10 Helm and deployment tooling** [P3 R L] charts (templates, values, helpers); releases, upgrades, rollbacks; OCI chart repositories; Kustomize overlays; Helm in pipelines; secrets handling (CSI Secrets Store, External Secrets)

☐ **8.11 Choosing compute** [P1 R E L] App Service vs Container Apps vs AKS vs Functions vs VMs; decision criteria (control, operations load, scaling, cost, team skill); Container Apps (revisions, KEDA scaling, ingress, jobs, Dapr awareness); App Service containers; migration paths from IIS-hosted monoliths; Windows containers for legacy .NET Framework

☐ **8.12 Advanced Kubernetes** [P4 O] RBAC details; Pod Security Standards; admission controllers; operators and CRDs; service mesh (Istio, Linkerd); Dapr; multi-cluster; CKA and CKAD skills


## D09 MICROSERVICES AND DISTRIBUTED ARCHITECTURE

☐ **9.01 Architectural styles and when to split** [P2 R L] monolith; modular monolith; SOA; microservices; serverless; benefits and costs; team size and independent deployment as the real drivers; Conway's law; signs of a distributed monolith; fallacies of distributed computing; latency and consistency costs

☐ **9.02 Decomposition and strategic DDD** [P2 R L] bounded contexts; ubiquitous language; context maps (shared kernel, customer-supplier, conformist, anti-corruption layer); core, supporting and generic subdomains; event storming; aggregate boundaries; service granularity; data ownership; team alignment

☐ **9.03 Strangler fig and legacy modernization** [P1 R L] seams; incremental extraction; facade and proxy (YARP, API Management); anti-corruption layer; branch by abstraction; parallel run; data synchronization (change data capture, risks of dual writes); migration sequencing; measuring progress; rollback; handling organizational change

☐ **9.04 Service communication** [P2 R L] REST vs gRPC vs messaging; availability math of synchronous call chains; timeouts and retries; service discovery; load balancing; API versioning; BFF; gateway aggregation; async request-reply; orchestration vs choreography; backward compatibility

☐ **9.05 Data management in microservices** [P2 R L] database per service; shared database anti-pattern; data duplication and read models; API composition; CQRS; outbox; change data capture (Debezium awareness); saga; alternatives to distributed transactions; reporting across services; reference data sharing

☐ **9.06 Operating microservices** [P2 R L] independent CI/CD; versioning; config and secrets per service; service templates and golden paths; distributed tracing; SLOs per service; dependency management; on-call ownership; platform team; cost allocation; feature flags

☐ **9.07 Testing microservices** [P3 R L] adapted test pyramid; unit, component, contract, integration, end-to-end; consumer-driven contracts (Pact); test doubles for external services (WireMock); testing in production (canary, synthetic checks); chaos testing awareness; test environment strategy; test data

☐ **9.08 Anti-patterns and failure modes** [P2 R L] distributed monolith; nano-services; chatty services; shared database; cascading failures; retry storms; tight coupling through shared libraries; unclear ownership; versioning problems; big-bang rewrite; resume-driven design; mitigations

☐ **9.09 Cloud design patterns on Azure** [P3 R E L] retry; circuit breaker; bulkhead; throttling; queue-based load leveling; competing consumers; priority queue; claim check; sidecar; ambassador; gateway offloading, routing, aggregation; valet key; cache-aside; leader election; sharding; CQRS; event sourcing; compensating transaction; saga; health endpoint monitoring; deployment stamps; geode

☐ **9.10 Dapr, service mesh, event sourcing in practice** [P4 O] Dapr building blocks; mesh trade-offs; event sourcing costs and tooling; .NET Aspire (verify)


## D10 DESIGN PATTERNS AND SOFTWARE ARCHITECTURE

☐ **10.01 Design principles** [P2 R L K] SOLID with .NET examples; DRY; KISS; YAGNI; separation of concerns; composition over inheritance; Law of Demeter; coupling and cohesion; cyclomatic complexity; fail fast; immutability

☐ **10.02 Creational patterns** [P2 R L K] Factory Method; Abstract Factory; Builder; Singleton (DI-managed); Prototype; .NET examples (IHttpClientFactory, ILoggerFactory)

☐ **10.03 Structural patterns** [P2 R L K] Adapter; Decorator (DI decoration); Facade; Proxy; Composite; Bridge; Flyweight awareness; .NET examples (middleware, streams)

☐ **10.04 Behavioral patterns** [P2 R L K] Strategy; Observer; Command; Chain of Responsibility (middleware); Template Method; State; Mediator (library licensing changes, verify); Iterator; Visitor awareness; Memento

☐ **10.05 Enterprise and data patterns** [P2 R L] Repository; Unit of Work; Specification; Active Record vs Data Mapper; DTO; service layer; domain model vs transaction script; CQRS; anti-corruption layer; Result pattern; Null Object; Options pattern

☐ **10.06 Architecture styles** [P3 R L] layered and N-tier; clean, onion and hexagonal; vertical slice; modular monolith structure; event-driven; microkernel and plugin; pipe and filter; choosing by quality attributes; .NET solution structure and the dependency rule; architecture tests (NetArchTest)

☐ **10.07 Tactical DDD** [P3 R L] entities; value objects; aggregates and invariants; aggregate roots; repositories per aggregate; domain events; domain services; factories; ubiquitous language in code; anemic vs rich models; transaction boundaries; eventual consistency between aggregates

☐ **10.08 Refactoring and legacy code** [P3 R L] code smells; refactoring catalog; characterization tests; seams; Boy Scout rule; technical debt quadrant; measuring complexity, coupling and churn; static analysis; safe refactoring with tests and IDE tools; code review practices; recording refactor decisions

☐ **10.09 Event sourcing, advanced CQRS, functional style** [P4 O] event store basics; projections; snapshots; functional patterns in C#; reactive programming


## D11 SYSTEM DESIGN

☐ **11.01 Requirements and estimation** [P2 R L] functional vs non-functional; quality attributes (availability, latency, throughput, consistency, durability, scalability, security, cost, operability); SLIs and SLOs; back-of-envelope math (QPS, storage, bandwidth, latency numbers); read-write ratio; peak vs average

☐ **11.02 Scalability building blocks** [P2 R L] vertical vs horizontal; stateless services; load balancing (L4, L7, algorithms); reverse proxy; CDN; DNS routing; autoscaling; connection pooling; queue-based load leveling; rate limiting (token bucket, leaky bucket, sliding window); backpressure

☐ **11.03 Data scaling** [P3 R L] replication (leader-follower, multi-leader, leaderless); replica lag; sharding strategies (hash, range, directory); consistent hashing; hot partitions; secondary indexes; CAP and PACELC; consistency models (strong, eventual, causal, read-your-writes); quorum; cross-shard transactions

☐ **11.04 Reliability and availability** [P3 R L] redundancy; failover (active-active, active-passive); health checks; multi-zone and multi-region; RPO and RTO; backup and restore tests; graceful degradation; bulkheads; retry budgets; cascading failure prevention; composite SLA math; DR tiers (backup-restore, pilot light, warm standby, active-active)

☐ **11.05 Practice set 1** [P3 R L] URL shortener; rate limiter; notification service; file upload and storage; unique ID generator; key-value store; pastebin; web crawler. Method each time: requirements, API, data model, high-level design, deep dive, bottlenecks, trade-offs

☐ **11.06 Practice set 2** [P3 R L] chat; news feed; e-commerce checkout and orders; payment processing (idempotency, reconciliation); job scheduler; logging and metrics pipeline; search autocomplete; booking with inventory (double booking); multi-tenant SaaS; audit log; report generation

☐ **11.07 Design communication** [P3 R L] whiteboard structure; clarifying questions; articulating trade-offs; diagram conventions; estimation narrative; 45-minute time boxing; common mistakes; justifying decisions; running a design review

☐ **11.08 Advanced system design** [P4 O] consensus (Raft, Paxos awareness); leader election; distributed locks; CRDTs; LSM trees vs B-trees; bloom filters; geo-distribution; stream processing; lambda and kappa architectures


## D12 AZURE CLOUD

☐ **12.01 Azure fundamentals** [P1 R E L] tenants; management groups; subscriptions; resource groups; resource providers; regions, availability zones, paired regions; ARM; locks; tags; quotas; pricing models; SLAs; portal, CLI, PowerShell, Cloud Shell; Resource Graph; naming conventions

☐ **12.02 Identity and access** [P1 R E L] Entra ID tenants, users, groups; app registrations vs enterprise apps; service principals; managed identities (system vs user-assigned); Azure RBAC (roles, scopes, assignments, custom roles); Entra roles vs Azure roles; Conditional Access; MFA; PIM; access reviews; B2B guests; SSO (SAML, OIDC); hybrid identity awareness

☐ **12.03 Networking** [P1 R E L] VNets and subnets; address planning; NSGs and ASGs; user-defined routes; peering; VPN Gateway; ExpressRoute; Virtual WAN awareness; hub-spoke; Azure Firewall; Azure DNS and private DNS zones; Private Endpoint vs Service Endpoint; Load Balancer; Application Gateway and WAF; Front Door; Traffic Manager; Bastion; NAT Gateway; Network Watcher

☐ **12.04 Compute** [P1 R E L] VMs (sizes, disks, availability zones, scale sets, images); App Service (plans, slots, scaling, VNet integration, custom domains and TLS); Azure Functions (hosting plans, triggers and bindings); Container Apps; AKS; choosing compute; cost levers (reservations, savings plans, spot, hybrid benefit)

☐ **12.05 Storage** [P1 R E L] account types and redundancy (LRS, ZRS, GRS, GZRS); blob tiers and lifecycle; Azure Files; queues and tables; managed disks; SAS, stored access policies, Entra authentication; immutability; soft delete; failover; private endpoints; Data Lake Gen2; AzCopy; Azurite locally

☐ **12.06 Governance basics** [P1 R E L] Azure Policy (definitions, initiatives, effects, remediation); management groups; tagging strategy; locks; Defender for Cloud overview; Cost Management, budgets and alerts; Advisor; cloud adoption framework stages

☐ **12.07 Monitoring and operations** [P1 R E L] Azure Monitor (metrics, logs, alerts, action groups, autoscale); Log Analytics and KQL basics; Application Insights (distributed tracing, availability tests, sampling); diagnostic settings; workbooks; Service Health and Resource Health; Azure Backup and Site Recovery; Update Manager; Automation runbooks awareness

☐ **12.08 Security services** [P2 R E L] Key Vault (secrets, keys, certificates; RBAC vs access policies; soft delete and purge protection; App Service references); managed HSM awareness; Defender for Cloud plans; NSG, WAF, Firewall; DDoS; encryption (at rest, in transit, customer-managed keys); Sentinel awareness; security baselines; secure score

☐ **12.09 Migration to Azure** [P1 R E L] the six Rs (rehost, refactor, rearchitect, rebuild, replace, retire or retain); Azure Migrate (discovery, assessment, migration); App Service Migration Assistant; Database Migration Service; Site Recovery; cutover planning; dependency mapping; business case and TCO; migration waves; hybrid connectivity; legacy .NET Framework on App Service, VMs and Windows containers

☐ **12.10 Well-Architected Framework and architecture design** [P3 R E L] five pillars and their trade-offs; workload assessment; reliability patterns (zones, regions); cost optimization; operational excellence; performance efficiency; reference architectures (Azure Architecture Center); architecture styles (N-tier, web-queue-worker, microservices, event-driven)

☐ **12.11 High availability, DR and business continuity** [P3 R E L] zones vs regions; SLA math; backup strategies; Site Recovery; geo-replication per service; Traffic Manager and Front Door failover; RPO and RTO design; DR drills; multi-region data (Cosmos DB multi-write, SQL failover groups); runbooks

☐ **12.12 Cost management and FinOps** [P2 R L] pricing calculator; TCO; tags and cost allocation; budgets; reservations and savings plans; right-sizing; autoscale; dev-test pricing; auto-shutdown; storage tiering; egress costs; FinOps framework (inform, optimize, operate); anomaly alerts; showback and chargeback

☐ **12.13 AZ-104 blueprint and exam strategy** [P1 R E] skills outline domains (identity and governance; storage; compute; virtual networking; monitoring and backup) as currently published (verify); labs per domain; practice assessments; time management; yearly renewal assessment

☐ **12.14 AZ-400 blueprint and exam strategy** [P3 R E] domains (processes and communications; source control strategy; build and release pipelines; security and compliance plan; instrumentation strategy) as currently published (verify); prerequisite check on Microsoft Learn; labs; renewal

☐ **12.15 AZ-305 blueprint and design drills** [P4 R E] domains (identity, governance and monitoring; data storage; business continuity; infrastructure) as currently published (verify); service-choice comparison sheets (storage, databases, compute, messaging, networking, identity); case-study reasoning; cost and SLA trade-offs

☐ **12.16 Landing zones and enterprise-scale design** [P4 R E L] Azure landing zone concepts; management group hierarchy; subscription design; hub-spoke and Virtual WAN; shared services; policy at scale; identity and connectivity subscriptions; platform vs workload teams; Cloud Adoption Framework phases

☐ **12.17 Other clouds and hybrid** [P4 O] AWS and GCP service mapping; Azure Arc; Azure Local (verify); multi-cloud strategy; edge

☐ **12.18 Optional certification blueprints** [P4 O E] AZ-500; Terraform Associate (verify current version); GH-200 (verify status); CKA and CKAD; AI-200 (verify)


## D13 OBSERVABILITY AND RELIABILITY

☐ **13.01 Observability fundamentals** [P2 R L] logs, metrics, traces; correlation and trace IDs; W3C trace context; structured logs; log levels and cost; sampling; cardinality; RED and USE methods; golden signals; business metrics

☐ **13.02 OpenTelemetry in .NET** [P2 R L] traces, metrics and logs APIs (ActivitySource, Meter); auto-instrumentation; exporters (OTLP, Azure Monitor); collector; propagation across HTTP and messaging; baggage; resource attributes; semantic conventions

☐ **13.03 Azure observability stack** [P1 R E L] Application Insights SDK vs OpenTelemetry distro; KQL queries; workbooks; alerts (metric, log, smart); action groups; availability tests; Container Insights; managed Prometheus and Grafana; dashboards; retention and cost; application map

☐ **13.04 Prometheus and Grafana basics** [P3 R L] scraping model; metric types (counter, gauge, histogram); PromQL basics; Alertmanager; Grafana dashboards; exporters; ELK and Loki awareness

☐ **13.05 Alerting and dashboards** [P2 R L] symptom vs cause alerts; alert fatigue; severity; runbooks; escalation; dashboard design (overview, drill-down); SLO burn-rate alerts; synthetic monitoring; paging policy

☐ **13.06 SRE fundamentals** [P2 R L] SLI, SLO, SLA; error budgets; toil; release gating by budget; availability nines table; incident management (roles, severity, communication, timeline); blameless postmortem template; on-call practices; change management; production readiness reviews

☐ **13.07 Performance and load testing** [P3 R L] baselines; load, stress, soak and spike tests; k6, JMeter, Azure Load Testing; bottleneck analysis (CPU, memory, IO, database, locks, thread pool); production profiling (dotnet-trace, Application Insights profiler); percentile latency (p95, p99); Little's law basics

☐ **13.08 Chaos and resilience testing** [P4 O] Azure Chaos Studio; game days; capacity modeling; observability cost control


## D14 SECURITY

☐ **14.01 Secure coding in .NET** [P2 R L] OWASP Top 10 mapped to .NET (injection, broken access control, cryptographic failures, insecure design, misconfiguration, vulnerable components, authentication failures, integrity failures, logging failures, SSRF); parameterized queries; output encoding; anti-forgery tokens; Data Protection API; input validation; deserialization risks; file upload safety

☐ **14.02 Cryptography and data protection** [P2 R L] symmetric vs asymmetric; hashing vs encryption vs signing; password hashing (PBKDF2, Argon2, bcrypt); salts; TLS versions, certificates and chains; mTLS; key management and rotation; envelope encryption; encryption at rest, in transit, in use; certificate lifecycle; personal data handling; tokenization; masking

☐ **14.03 Secrets and least privilege** [P2 R L] secret sprawl; Key Vault patterns; managed identities; workload identity; least-privilege RBAC; just-in-time access; rotation; secret scanning; break-glass accounts; service principal hygiene

☐ **14.04 Threat modeling and secure design** [P3 R L] STRIDE; data flow diagrams; trust boundaries; attack surface; abuse cases; security requirements; defense in depth; zero trust principles (verify explicitly, least privilege, assume breach); secure SDLC; design review checklist

☐ **14.05 Supply chain and DevSecOps** [P3 R L] dependency scanning; SBOM; signed artifacts and images; pinned versions; private feeds; pipeline hardening; SAST, DAST, IAST; container and IaC scanning (Checkov); policy as code; vulnerability management SLAs; secure build agents

☐ **14.06 Cloud security** [P3 R E L] shared responsibility; Defender for Cloud; network security (private endpoints, NSG, WAF, DDoS); identity security (Conditional Access, PIM); data security (customer-managed keys, TDE, purge protection); security logging (Activity log, Sentinel awareness); incident response basics; Microsoft cloud security benchmark

☐ **14.07 Compliance and privacy** [P3 R L] GDPR basics; India DPDP Act awareness (verify); data residency; audit logging; retention; right to erasure impact on design; PCI-DSS, HIPAA, SOC 2, ISO 27001 awareness; privacy by design; data classification

☐ **14.08 Advanced security** [P4 O] zero trust architecture; SIEM and SOAR; penetration testing process; red and blue teams; WAF tuning


## D15 LEADERSHIP AND ARCHITECTURE PRACTICE

☐ **15.01 Architecture documentation** [P1 R L] ADRs (context, options, decision, consequences, status); C4 model levels; sequence and deployment diagrams; arc42 awareness; runbooks; diagrams as code (Mermaid, Structurizr, PlantUML); lightweight RFC process

☐ **15.02 Trade-off analysis** [P2 R L] quality attribute scenarios; utility trees; ATAM awareness; weighted decision matrices; cost, risk, time and team skill; build vs buy; reversible vs irreversible decisions; risk register; spike and proof-of-concept method; fitness functions; evolutionary architecture

☐ **15.03 Non-functional requirements and reviews** [P3 R L] NFR catalog (performance, availability, security, scalability, maintainability, observability, compliance, cost); measurable targets; architecture review checklist; design review process; production readiness review; architecture governance; technology radar; guardrails vs control

☐ **15.04 Technical leadership** [P2 R L] estimation (story points, T-shirt sizes, three-point); planning and scope negotiation; risk management; delegation; mentoring and growing leads; code review culture; onboarding; technical roadmap; tech debt budget; client stakeholder management; offshore team coordination

☐ **15.05 Communication and influence** [P2 R L] explaining to non-technical audiences; writing proposals and RFCs; executive summaries; cost and risk framing; presenting designs; handling objections; building consensus; influencing without authority; conflict resolution; status reporting; decision logs

☐ **15.06 Agile and delivery management** [P3 R L] Scrum and Kanban; backlog refinement; sprint planning; definition of ready and done; cycle time and velocity; release planning; SAFe awareness; risk and issue tracking; client SLAs; change requests; time-and-material vs fixed price

☐ **15.07 Enterprise architecture foundations** [P4 R E L] EA domains (business, data, application, technology); TOGAF ADM phases; architecture principles; capability maps; roadmaps; architecture repository; governance boards; ArchiMate awareness; TOGAF Foundation and Practitioner syllabus (verify current version); enterprise vs solution vs technical architect roles

☐ **15.08 AI-assisted engineering** [P3 O] using coding assistants safely; prompt patterns for review, tests and documentation; data privacy rules; checking for hallucinations; AI in the SDLC; RAG and agent architecture awareness; Azure OpenAI and Foundry awareness (verify)


## D16 FOUNDATIONS: LINUX, WINDOWS, NETWORKING, SCRIPTING

☐ **16.01 Linux essentials** [P1 R E L] filesystem hierarchy; permissions and ownership; users, groups, sudo; processes and signals; systemd and journalctl; package managers; cron and timers; disks, LVM, mounts; SSH (keys, config, tunnels); logs in /var/log; resource tools (top, vmstat, iostat, free, df, du, lsof, ss); text tools (grep, sed, awk, find, xargs, tail); environment variables; tar; SELinux awareness

☐ **16.02 Windows Server and IIS** [P1 R L K] IIS architecture (sites, app pools, bindings); app pool identity; web.config; logging and failed request tracing; performance counters; Event Viewer; PowerShell basics; services and scheduled tasks; certificates; Active Directory and Group Policy awareness

☐ **16.03 Shell, Bash and PowerShell scripting** [P1 R L] variables and quoting; conditionals and loops; functions; exit codes; set -euo pipefail; pipes and redirection; argument parsing; trap; idempotent scripts; jq and curl; ShellCheck; PowerShell objects and pipeline; modules; Az module for Azure automation

☐ **16.04 Networking fundamentals** [P1 R E L] OSI and TCP/IP; IP addressing; CIDR and subnetting; routing; NAT; DNS (records, resolution, TTL); DHCP; TCP handshake, flow and congestion control; UDP; HTTP/1.1, 2, 3; TLS handshake; L4 and L7 load balancers; proxies; firewalls; VPN; latency, bandwidth, MTU; tools (ping, traceroute, dig, curl -v, ss, tcpdump, Wireshark, openssl s_client)

☐ **16.05 Python for automation** [P2 O] venv and pip; files, JSON, YAML; requests; subprocess; argparse; logging; exceptions; Azure SDK and CLI scripting; basic tests

☐ **16.06 Go awareness for DevOps tooling** [P4 O] why Kubernetes and Terraform tooling is written in Go; reading simple Go; building a small CLI


## D17 CAREER AND INTERVIEW TOOLKIT

☐ **17.01 Story bank** [P1 R L] eight to ten STAR stories with numbers: introducing the queue system; building the GitLab pipeline; persuading a client; a production incident; a conflict; a failure and what changed; mentoring; an estimation miss; a design decision; delivery under pressure

☐ **17.02 Project portfolio write-ups** [P1 R L] capstone README; architecture diagram; ADRs; postmortem; cost estimate; what I would change; describing lab vs production work honestly

☐ **17.03 Resume and profile** [P1 R L] lead-level resume structure; keyword mapping to postings (Azure DevOps, microservices, Terraform, AKS); quantified achievements; LinkedIn headline and summary; GitHub profile; recruiter outreach messages; referrals

☐ **17.04 Interview preparation map** [P2 R L] rounds: .NET deep dive, SQL, system design, cloud scenario, pipeline design, behavioral, managerial (team, estimation, conflict), architect (trade-offs), client-facing; mock interview schedule; question bank per domain

☐ **17.05 Offer and negotiation** [P2 R L] CTC structure (fixed, variable, PF, gratuity, stock); in-hand vs CTC calculation; notice period and buyout; counter-offers; comparing offers (total pay, growth, role content); background verification awareness; negotiation scripts


TOTALS: 152 topics. 133 are required (full notes, about 133 printed pages) and 19 are optional (short notes, about 10 pages). Required by phase: Phase 1 has 51, Phase 2 has 54, Phase 3 has 25, Phase 4 has 3. Optional by phase: 1 in Phase 2, 6 in Phase 3, 12 in Phase 4. Printed total is about 150 pages, roughly 75 sheets printed on both sides.

## PART 5: STUDY ORDER (BATCHES OF ABOUT 8 NOTES)

Work in this order. One batch is roughly one to one and a half months at your pace. Start the capstone project during Batch 2 and apply what you write about in each batch inside the project.

Phase 1 (build credibility, apply from about Batch 5 or 6):

- Batch 1: 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08
- Batch 2: 1.10, 1.11, 1.12, 4.05, 3.01, 3.02, 3.03, 9.03
- Batch 3: 16.01, 16.04, 8.01, 8.02, 8.03, 8.11, 7.01, 7.02
- Batch 4 (AZ-104 core): 12.01, 12.02, 12.03, 12.04, 12.05, 12.06, 12.07, 12.13
- Batch 5 (capstone support): 7.03, 7.04, 7.07, 5.01, 5.02, 5.03, 6.01, 6.02, 13.03
- Batch 6: 4.07, 12.09, 15.01, 16.02, 16.03, 2.01, 2.02, 17.01, 17.02, 17.03

Phase 2 (lead in the cloud era):

- Batch 7: 3.04, 3.05, 3.07, 3.08, 4.01, 4.02, 4.03, 4.04
- Batch 8: 4.06, 4.08, 4.09, 5.04, 6.03, 6.04, 7.05, 7.06
- Batch 9: 7.08, 8.04, 8.05, 8.06, 8.07, 8.08, 8.09, 13.01
- Batch 10: 13.02, 13.05, 13.06, 14.01, 14.02, 14.03, 12.08, 12.12
- Batch 11: 2.03, 2.04, 2.05, 9.01, 9.02, 9.04, 9.05, 9.06
- Batch 12: 9.08, 10.01, 10.02, 10.03, 10.04, 10.05, 11.01, 11.02
- Batch 13: 1.09, 15.02, 15.04, 15.05, 17.04, 17.05, and 16.05 (optional, skip if short of time)

Phase 3 (.NET architect):

- Batch 14: 10.06, 10.07, 10.08, 11.03, 11.04, 11.05, 11.06, 11.07
- Batch 15: 9.07, 9.09, 6.05, 8.10, 12.10, 12.11, 15.03, 15.06
- Batch 16 (AZ-400 block): 7.09, 12.14, 14.04, 14.05, 14.06, 14.07, 13.04, 13.07, 2.06

Phase 4 (cloud architect):

- Batch 17: 12.15, 12.16, 15.07

Optional notes (write only when a target job asks, or after Batch 16): 1.13, 2.07, 2.08, 3.06, 4.10, 5.05, 6.06, 7.10, 8.12, 9.10, 10.09, 11.08, 12.17, 12.18, 13.08, 14.08, 15.08, 16.06.

Fast-pass reminder: topics tagged K (2.01, 2.02, 4.01 to 4.04, 7.01, 10.01 to 10.04, 16.02) should take about one hour each. Generate, read once, mark the gaps.

## PART 6: PRINT SETTINGS (TO KEEP THE PAGE COUNT LOW)

- Word: Narrow margins (0.5 inch), font Arial or Calibri 10 pt, single line spacing, 0 pt space after paragraphs, headings the same size as body text but plain bold.
- Print on both sides, black and white, draft quality. Do not print two pages on one sheet (the text becomes too small to read).
- One Word file per domain: D01-dotnet-platform, D02-frontend, D03-backend-api, D04-databases, D05-caching, D06-messaging, D07-cicd-devops, D08-containers-k8s, D09-microservices, D10-patterns-architecture, D11-system-design, D12-azure, D13-observability-sre, D14-security, D15-leadership-architecture, D16-foundations, D17-career.
- Punch and file each domain in its own section of your binder. Put the printed Part 4 line at the front of each section as the tick list.
- If your eyes are strained, export the Word file to PDF and read it on an e-ink reader instead of printing, and keep the handwritten recall box on paper.
