# Quick Revision Template: Theory Topics
**For:** System Design · Operating Systems · AI (also works for networking, distributed systems, security, cloud)
**Reading budget:** 2-3 minutes (about 500-700 words)
**Goal:** Nothing important is missed. Every note covers the topic itself AND everything connected to it.

---

## How to use
Send a topic name, optionally with a domain tag:

- `Topic: Paging and virtual memory | Domain: OS`
- `Topic: Consistent hashing | Domain: System Design`
- `Topic: RAG | Domain: AI`
- `Topic: Operating System | Domain: OS` (umbrella topic, so Map Mode applies)

The reply follows the skeleton below, in this order, with these exact headings.

---

## Rules that prevent anything being missed

1. **Size check first.**
   - **Leaf topic** (one concept, e.g. TLB, CAP theorem, embeddings) → use **Full Mode**.
   - **Umbrella topic** (e.g. Operating System, System Design, AI, Distributed Systems) → use **Map Mode**: list every sub-topic with a one-line meaning and a `R/O/E/L` flag, grouped by module. Then offer to expand any sub-topic in Full Mode.
2. **Always fill the Related Topics Map** (section 8). It is mandatory and has five fixed slots, so connected topics cannot be skipped.
3. **Always include the opposite or alternative** of the topic (what you would pick instead and why).
4. **Always include one failure mode** with its production symptom.
5. **Always include at least one number or rule of thumb** (limit, latency order of magnitude, complexity, ratio).
6. **Add the domain lens** (see bottom). Those extra lines are mandatory for the domain.
7. **End with the Coverage Self-Check.** If any box would be unchecked, fill the gap before sending.
8. **Flags:** `R` Required · `O` Optional · `E` Exam oriented · `L` Real life use.
9. **Be honest about version-dependent or uncertain items.** Mark them `(verify)` instead of guessing.

---

## Output Skeleton (Full Mode)

```markdown
# <Topic>  ·  <Domain>  ·  <Flags>

## 1. In one line
<≤ 20 words: what it is>

## 2. Why it exists
- Problem it solves:
- What goes wrong without it:

## 3. Mental model
<One analogy or one-line flow, e.g. A → B → C>

## 4. Key concepts (the 80%)
| Term | Meaning (≤ 1 line) | Flag |
|---|---|---|

## 5. How it works
1.
2.
3.
(numbered flow, lifecycle, or components)

## 6. Types / variants and trade-offs
| Option | Use when | Trade-off |
|---|---|---|

**Decision rule:** Use it when … Avoid it when … Prefer <alternative> when …

## 7. Failure modes and symptoms
| What breaks | Symptom you will see | Fix / mitigation |
|---|---|---|

## 8. Related Topics Map  (mandatory, all five slots)
- **Prerequisites (learn before):**
- **Siblings (same level, often asked together):**
- **Downstream (builds on this):**
- **Contrasts / alternatives (the opposite idea):**
- **Real systems and tools (where it lives):**

## 9. Numbers and rules of thumb
-

## 10. Interview lens
- **30-second answer:**
- **Q1 →** short answer
- **Q2 →** short answer
- **Q3 →** short answer
- **Common mistakes / misconceptions:**

## 11. Domain lens (mandatory extra lines, see below)

## 12. Revision summary
- 5 bullets, one line each
- **If you remember only one thing:**

## 13. Coverage Self-Check
- [ ] Definition and purpose
- [ ] How it works
- [ ] Types and trade-offs, including the alternative
- [ ] Failure mode with symptom
- [ ] All five related-topic slots filled
- [ ] At least one number or rule of thumb
- [ ] Domain lens lines present
- [ ] Interview answer ready
```

---

## Map Mode skeleton (for umbrella topics)

```markdown
# <Umbrella topic> · Map

## Module index
| # | Module | One-line meaning | Sub-topics (flagged) |
|---|---|---|---|

## Dependencies between modules
<Which modules depend on which, as a short list or arrow chain>

## Top 10 interview hotspots
1.
...

## Learn order (fastest path)
1 → 2 → 3 ...

## Next step
Send any sub-topic name for a Full Mode note.
```

---

## Domain lenses (mandatory extra lines in section 11)

### System Design lens
- **Scale:** what changes at 10x and 100x load
- **Consistency vs availability:** where this sits (CAP/PACELC), and what it gives up
- **Bottleneck and capacity:** the first thing that saturates
- **Data and state:** where state lives, how it is partitioned or replicated
- **Reliability:** timeout, retry, idempotency, back-pressure implications
- **Cost and operability:** what it costs to run and observe
- **Security:** the main attack or trust-boundary concern

### Operating Systems lens
- **Resource touched:** CPU, memory, disk, or network
- **Cost model:** syscall, context switch, page fault, or copy cost
- **Linux tool or file to inspect it:** e.g. `vmstat`, `strace`, `/proc`, `perf` (verify exact tool for the topic)
- **Container and cloud impact:** namespaces, cgroup limits, Kubernetes behaviour
- **Production symptom:** what an on-call engineer sees

### AI lens
- **Data:** inputs, quality, privacy, provenance
- **Model or method:** what is learned or retrieved, and its limits
- **Evaluation:** how you know it works (metrics, test sets, human review)
- **Failure modes:** hallucination, bias, drift, prompt injection, over-reliance
- **Governance and risk:** applicable controls and frameworks (NIST AI RMF, ISO/IEC 42001, EU AI Act where relevant), accountability, human oversight
- **Cost and latency:** tokens, compute, caching, batching
- **Security:** data leakage, model abuse, supply chain

---

## Worked example (Full Mode, about 2.5 minutes)

# Virtual Memory and Paging · OS · R E L

## 1. In one line
OS abstraction giving each process a private address space, mapped to physical RAM (or disk) in fixed-size pages.

## 2. Why it exists
- Problem it solves: isolation between processes, running programs larger than RAM, simple programming model, less fragmentation.
- What goes wrong without it: processes can corrupt each other, memory must be contiguous, no overcommit or sharing.

## 3. Mental model
Virtual page → (MMU + page table, cached by TLB) → physical frame. A missing mapping triggers a page fault and the OS fixes it.

## 4. Key concepts (the 80%)
| Term | Meaning | Flag |
|---|---|---|
| Page / frame | Fixed-size unit of virtual / physical memory (commonly 4 KB) | R E |
| Page table | Per-process map of virtual pages to frames (multi-level on 64-bit) | R E |
| TLB | Small cache of recent translations | R E L |
| Page fault (minor / major) | Minor: mapping fixed in memory. Major: data read from disk | R E L |
| Demand paging | Pages loaded only when first touched | R E |
| Copy-on-write | Shared pages copied only on write (cheap `fork`) | R E L |
| Swap / thrashing | Disk-backed overflow / constant faulting, no useful work | R E L |
| Huge pages | Larger pages to reduce TLB misses | O E L |

## 5. How it works
1. CPU issues a virtual address.
2. TLB hit → physical address, done.
3. TLB miss → page table walk.
4. Page not present → page fault → OS finds or evicts a frame (replacement policy), reads from disk if needed.
5. Page table updated, instruction retried.

## 6. Types / variants and trade-offs
| Option | Use when | Trade-off |
|---|---|---|
| Paging | General purpose | Page-table memory, TLB misses |
| Segmentation | Legacy / protection schemes | External fragmentation |
| LRU / Clock replacement | Eviction under pressure | LRU is costly to track exactly, Clock approximates it |
| Huge pages | Large heaps, databases | Less flexible, can add latency or fragmentation (verify per workload) |

**Decision rule:** Keep latency-sensitive services off swap. Use huge pages only after measuring TLB pressure.

## 7. Failure modes and symptoms
| What breaks | Symptom | Fix |
|---|---|---|
| Thrashing | High major faults, high I/O wait, latency collapse | Add RAM, reduce working set, limit concurrency |
| OOM kill | Process or container disappears | Right-size limits, find leaks, tune heap |
| Memory overcommit surprise | Works until load, then kills | Set limits and alerts |

## 8. Related Topics Map
- **Prerequisites:** address space, MMU, CPU cache, process basics
- **Siblings:** page cache, `mmap`, memory allocators, shared memory
- **Downstream:** cgroup memory limits, container OOM, JVM/Node heap sizing, NUMA
- **Contrasts:** segmentation, direct physical addressing, unikernels
- **Real systems and tools:** Linux kernel, `vmstat`, `/proc/meminfo`, `perf`, `free`

## 9. Numbers and rules of thumb
- Typical page size 4 KB; 64-bit x86 commonly uses 4-level page tables.
- Order of magnitude latency: RAM about 100 ns, NVMe about 100 µs, spinning disk about milliseconds. A major fault costs orders of magnitude more than a RAM access.

## 10. Interview lens
- **30-second answer:** Virtual memory gives each process an isolated address space translated by the MMU through page tables; the TLB caches translations; page faults let the OS load pages on demand and evict others when RAM is short.
- **Q1 → Minor vs major fault?** Minor needs no disk read, major does.
- **Q2 → Why is `fork` cheap?** Copy-on-write shares pages until written.
- **Q3 → What is thrashing?** Working set exceeds RAM, so the system spends its time swapping.
- **Common mistakes:** confusing virtual memory with swap; assuming "free" memory is wasted (page cache uses it).

## 11. Domain lens (OS)
- **Resource touched:** memory (and disk when swapping)
- **Cost model:** TLB miss, page fault, disk read
- **Inspect with:** `vmstat` (si/so), `/proc/meminfo`, `perf` page-fault events
- **Container impact:** cgroup limit triggers OOM kill even if the host has spare RAM
- **Production symptom:** latency spikes with high iowait, or sudden container restarts

## 12. Revision summary
- Virtual memory = isolation plus more address space than RAM.
- Translation path: TLB → page table → fault handler.
- Minor fault cheap, major fault expensive.
- Copy-on-write makes `fork` and sharing efficient.
- Thrashing and OOM are the two production failures.
- **If you remember only one thing:** keep the working set inside RAM, because a major fault is orders of magnitude slower than a memory access.

## 13. Coverage Self-Check
- [x] Definition and purpose
- [x] How it works
- [x] Types and trade-offs, including the alternative
- [x] Failure mode with symptom
- [x] All five related-topic slots filled
- [x] Number or rule of thumb
- [x] Domain lens lines present
- [x] Interview answer ready