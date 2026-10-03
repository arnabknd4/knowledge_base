# Quick Revision Template: Coding Topics
**For:** C# · .NET Core / ASP.NET Core · Java · Rust · Go (also works for Python, TypeScript/Node)
**Reading budget:** 2-3 minutes (about 500-700 words plus one short code snippet)
**Goal:** Nothing important is missed. Every note covers the topic itself AND everything connected to it, including how it differs in the other languages you use.

---

## How to use
Send a topic name with a language tag:

- `Topic: async/await | Lang: C#`
- `Topic: Dependency injection lifetimes | Lang: .NET Core`
- `Topic: Virtual threads | Lang: Java`
- `Topic: Ownership and borrowing | Lang: Rust`
- `Topic: Goroutines and channels | Lang: Go`
- `Topic: Concurrency | Lang: Go` (umbrella topic, so Map Mode applies)

The reply follows the skeleton below, in this order, with these exact headings.

---

## Rules that prevent anything being missed

1. **Size check first.**
   - **Leaf topic** (one feature, e.g. `async/await`, generics, `Result`, `defer`) → **Full Mode**.
   - **Umbrella topic** (e.g. Concurrency, Memory management, Collections, Web framework) → **Map Mode**: list every sub-topic with a one-line meaning and a `R/O/E/L` flag, then offer to expand any of them in Full Mode.
2. **Always include a minimal runnable snippet** (5-12 lines). No long code.
3. **Always include "under the hood"** (what the compiler or runtime actually does). This is where interview depth comes from.
4. **Always include top pitfalls with the fix**, not just a list of warnings.
5. **Always fill the Related Topics Map** (section 9) and the **Cross-language equivalents** table (section 10). Both are mandatory.
6. **Always include one performance/memory note** and one **concurrency interaction** note (even if the answer is "none").
7. **Add the language lens** (see bottom). Those lines are mandatory.
8. **End with the Coverage Self-Check.** If a box would be unchecked, fill the gap first.
9. **Flags:** `R` Required · `O` Optional · `E` Exam oriented · `L` Real life use.
10. **Mark version-dependent features** with `(verify version)` instead of guessing.

---

## Output Skeleton (Full Mode)

````markdown
# <Topic>  ·  <Language / Runtime>  ·  <Flags>

## 1. In one line
<≤ 20 words>

## 2. Problem it solves
- Without it:
- With it:

## 3. 30-second snippet
```<lang>
// 5-12 lines, minimal and runnable
```

## 4. Mental model
<One line: what the compiler/runtime does with this>

## 5. Under the hood
1.
2.
3.

## 6. Variants and when to use
| Option | Use when | Trade-off |
|---|---|---|

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|

## 8. Performance, memory and concurrency notes
- Performance / allocation:
- Concurrency interaction (threads, async, locks, goroutines, ownership):
- Observability or testing hook:

## 9. Related Topics Map  (mandatory, all five slots)
- **Prerequisites (learn before):**
- **Siblings (same level, often asked together):**
- **Downstream (builds on this):**
- **Contrasts / alternatives:**
- **Libraries, tools, frameworks:**

## 10. Cross-language equivalents  (mandatory)
| Concept | C# / .NET | Java | Go | Rust | Node/TS |
|---|---|---|---|---|---|

## 11. Interview lens
- **30-second answer:**
- **Q1 →** short answer
- **Q2 →** short answer
- **Q3 →** short answer
- **Spot the bug:** <2-4 line snippet> → problem and fix

## 12. Language lens (mandatory extra lines, see below)

## 13. Revision summary
- 5 bullets, one line each
- **If you remember only one thing:**

## 14. Coverage Self-Check
- [ ] Definition and problem solved
- [ ] Snippet included
- [ ] Under the hood explained
- [ ] Pitfalls with fixes
- [ ] Performance and concurrency note
- [ ] All five related-topic slots filled
- [ ] Cross-language table filled
- [ ] Interview answer and spot-the-bug ready
- [ ] Language lens lines present
````

---

## Map Mode skeleton (for umbrella topics)

```markdown
# <Umbrella topic> · <Language> · Map

## Sub-topic index
| # | Sub-topic | One-line meaning | Flag |
|---|---|---|---|

## How they connect
<Short dependency chain: A → B → C>

## Top 10 interview hotspots
1.
...

## Learn order (fastest path)
1 → 2 → 3 ...

## Next step
Send any sub-topic name for a Full Mode note.
```

---

## Language lenses (mandatory extra lines in section 12)

### C# / .NET Core lens
- **Runtime behaviour:** CLR/JIT/GC implication (allocation, generations, boxing)
- **Async and threading:** `Task`, thread pool, `ConfigureAwait` relevance
- **DI and lifetime:** Transient / Scoped / Singleton impact, if relevant
- **ASP.NET Core placement:** where it sits in the pipeline (middleware, filters, endpoint)
- **EF Core / data impact:** tracking, N+1, transactions, if relevant
- **Version note:** language or runtime version where the feature appeared (verify version)

### Java lens
- **JVM behaviour:** JIT, GC choice, memory model, class loading implication
- **Concurrency model:** platform threads vs virtual threads, `CompletableFuture`, locks
- **Spring / Jakarta placement:** where it sits (bean lifecycle, AOP, transactions), if relevant
- **Startup and footprint:** native image, CRaC, SnapStart relevance
- **Version note:** Java version where the feature became final or preview (verify version)

### Go lens
- **Scheduler behaviour:** goroutines, M:N scheduling, blocking effects
- **Memory:** escape analysis, allocation, GC pause relevance
- **Interfaces and composition:** implicit interfaces, embedding, no inheritance
- **Error handling:** explicit `error` return, wrapping, `errors.Is/As`
- **Concurrency safety:** channels vs mutexes, context cancellation, race detector
- **Version note:** generics and newer stdlib features (verify version)

### Rust lens
- **Ownership impact:** who owns the data, moves vs borrows, lifetimes involved
- **Safety guarantee:** what the compiler proves, and where `unsafe` would be needed
- **Traits and generics:** static vs dynamic dispatch cost
- **Error handling:** `Result` / `Option`, `?`, `thiserror` / `anyhow`
- **Async and ecosystem:** Tokio, `Send`/`Sync` constraints
- **Edition / version note** (verify version)

### Python / TypeScript lens (if used)
- **Runtime behaviour:** GIL / event loop, typing and runtime-check gap
- **Packaging and tooling:** virtual environments, `uv`/`pip`, `npm`/`pnpm`, `tsconfig`
- **Async model:** `asyncio` / Promises, what blocks the loop

---

## Worked example (Full Mode, about 2.5 minutes)

# async/await · C# / .NET · R E L

## 1. In one line
Compiler-generated state machine that lets a method wait for I/O without blocking a thread.

## 2. Problem it solves
- Without it: one thread per waiting request, which exhausts the thread pool and hurts scalability.
- With it: threads are released while waiting and resumed on completion.

## 3. 30-second snippet
```csharp
public async Task<string> GetAsync(HttpClient client, string url, CancellationToken ct)
{
    var body = await client.GetStringAsync(url, ct);   // thread is released here
    return body.Trim();                                // continuation resumes later
}
```

## 4. Mental model
`await` = "pause this method, hand the thread back, resume when the task completes."

## 5. Under the hood
1. Compiler rewrites the method into a state machine (struct in release builds).
2. At `await`, if the task is incomplete, the method registers a continuation and returns an incomplete `Task`.
3. When I/O completes (IOCP on Windows, epoll on Linux), the continuation is scheduled via the captured `SynchronizationContext` or the `TaskScheduler`.
4. Exceptions are stored in the `Task` and rethrown at `await`.
5. No new thread is created for I/O-bound waits.

## 6. Variants and when to use
| Option | Use when | Trade-off |
|---|---|---|
| `Task` / `Task<T>` | Default for async APIs | Heap allocation per call |
| `ValueTask<T>` | Often completes synchronously (caches, buffers) | Must be awaited once, harder to misuse-proof |
| `Task.WhenAll` | Parallel independent I/O | One failure surfaces, others still run |
| `IAsyncEnumerable<T>` | Streaming results | Needs `await foreach` |
| `Task.Run` | CPU-bound work offloaded from a UI thread | Wasteful for I/O on ASP.NET Core |
| `ConfigureAwait(false)` | Library code, avoid context capture | Not needed in ASP.NET Core app code (no sync context) |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| `.Result` / `.Wait()` | Blocks a thread; can deadlock with a sync context; causes thread-pool starvation | `await` all the way up |
| `async void` | Exceptions cannot be awaited and can crash the process | Use `async Task` (except event handlers) |
| Forgetting `await` | Fire-and-forget, lost exceptions | Await or handle explicitly |
| No `CancellationToken` | Work continues after the client leaves | Pass tokens through |
| Sequential awaits in a loop | Needlessly serial I/O | Start tasks, then `Task.WhenAll` |

## 8. Performance, memory and concurrency notes
- Performance / allocation: `Task` allocates; use `ValueTask` only where profiling shows benefit.
- Concurrency interaction: async is not parallelism; it multiplexes waiting on few threads. Shared state still needs synchronisation (`SemaphoreSlim`, not `lock` across `await`).
- Observability hook: `dotnet-counters` for thread-pool queue length and starvation.

## 9. Related Topics Map
- **Prerequisites:** threads and thread pool, delegates, exceptions
- **Siblings:** `Task` Parallel Library, `Parallel.ForEach`, `Channel<T>`, `IAsyncDisposable`
- **Downstream:** ASP.NET Core request handling, `HttpClientFactory`, EF Core async queries, `BackgroundService`
- **Contrasts:** blocking I/O, callbacks/events, reactive streams (Rx)
- **Libraries, tools, frameworks:** Polly, `System.Threading.Channels`, `dotnet-counters`, analyzers for async misuse

## 10. Cross-language equivalents
| Concept | C# / .NET | Java | Go | Rust | Node/TS |
|---|---|---|---|---|---|
| Async I/O model | `async/await` + `Task` | Virtual threads (Java 21+) or `CompletableFuture` | Goroutines + blocking-style code | `async/await` futures + executor (Tokio) | `async/await` + Promise |
| Cancellation | `CancellationToken` | Interruption / structured scopes (verify version) | `context.Context` | Drop future / cancellation tokens | `AbortController` |
| Parallel join | `Task.WhenAll` | `CompletableFuture.allOf` | `sync.WaitGroup` / `errgroup` | `join!` / `try_join!` | `Promise.all` |

## 11. Interview lens
- **30-second answer:** `async/await` compiles to a state machine that releases the thread at each incomplete `await` and resumes via a continuation, so I/O-bound code scales without a thread per request.
- **Q1 → Does `async` create a thread?** No; I/O waits use no thread, continuations run on the pool or captured context.
- **Q2 → Why avoid `.Result`?** Blocks a thread, can deadlock under a sync context, and starves the pool.
- **Q3 → `Task` vs `ValueTask`?** `ValueTask` avoids allocation when the result is often synchronous, with stricter usage rules.
- **Spot the bug:**
  ```csharp
  public string Get() => GetAsync(client, url, default).Result;
  ```
  → Sync-over-async; make the caller async or use a truly synchronous API.

## 12. Language lens (C# / .NET)
- **Runtime behaviour:** state machine allocation, continuations scheduled on the thread pool
- **Async and threading:** `ConfigureAwait(false)` matters mainly in libraries
- **DI and lifetime:** do not capture scoped services in fire-and-forget tasks
- **ASP.NET Core placement:** every middleware, filter and endpoint can be async; honour `HttpContext.RequestAborted`
- **EF Core impact:** use `ToListAsync()` and friends; `DbContext` is not thread-safe
- **Version note:** `ValueTask` and `IAsyncEnumerable` need modern .NET (verify version)

## 13. Revision summary
- `async/await` = compiler state machine plus continuations.
- Releases threads during waits; does not create threads.
- Never block on tasks (`.Result`, `.Wait()`).
- Pass `CancellationToken` everywhere.
- Parallelise independent I/O with `Task.WhenAll`.
- **If you remember only one thing:** async all the way down, never sync over async.

## 14. Coverage Self-Check
- [x] Definition and problem solved
- [x] Snippet included
- [x] Under the hood explained
- [x] Pitfalls with fixes
- [x] Performance and concurrency note
- [x] All five related-topic slots filled
- [x] Cross-language table filled
- [x] Interview answer and spot-the-bug ready
- [x] Language lens lines present