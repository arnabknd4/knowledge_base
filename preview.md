---
title: "Domain 1: .NET Platform and C#"
date: 2026-10-11
role_focus: ".NET Full Stack / Architect / Cloud Architect"
tags: [dotnet, backend, runtime, csharp, migration, testing]
---

# Domain 1: .NET Platform and C#

## Topic 1.1: Modern .NET Runtime
The modern .NET runtime (currently .NET 8 LTS, verify version) replaces the legacy .NET Framework.  
It is cross‑platform, faster, and supports side‑by‑side installs.  
The hosting model is minimal, using `Program.cs` and `WebApplicationBuilder` instead of `Global.asax` and `Web.config`.

Dependency Injection is central, with lifetimes (singleton, scoped, transient).  
Configuration uses the `IOptions` pattern with environment‑specific settings and secrets.  
Middleware defines request pipelines, ordering, and exception handling.  
Logging abstractions (`ILogger`) provide structured logging and correlation IDs.

---

## Topic 1.2: Modern C# Language Features
Async/await and the Task model are critical for concurrency.  
LINQ enables expressive queries but requires awareness of deferred execution and allocations.  
Records, pattern matching, nullable reference types, and init‑only properties are part of modern code review.  
Generics, delegates, events, and extension methods are assumed knowledge in design discussions.  
Memory and GC concepts (Span<T>, IDisposable, generations, LOH) are needed for performance troubleshooting.  
Concurrency primitives (locks, SemaphoreSlim, channels, thread‑safe collections) are essential for robust systems.

---

## Topic 1.3: Migrating Legacy .NET Framework Apps
Migration strategies include in‑place upgrade, strangler pattern, or rewrite.  
Tools like .NET Upgrade Assistant, API analyzers, and compatibility shims help.  
Reverse proxy (YARP) can migrate page by page.  
EF6 to EF Core differences and System.Web to ASP.NET Core mappings are essential.  
Risk planning involves feature flags, parallel runs, and rollback strategies to ensure safe modernization.

---

## Topic 1.4: Testing in .NET
Unit testing frameworks include xUnit and NUnit, with mocking libraries like Moq or NSubstitute.  
Integration testing uses WebApplicationFactory, test databases, and Testcontainers.  
A mature test strategy balances unit, integration, and end‑to‑end tests.  
Coverage is treated as a signal, not a goal.  
Testing maturity demonstrates engineering credibility in interviews and real projects.
