# Context Budgets, Caching, and Provenance · Architect · R / E / L

> **Exam note:** Product docs support these concepts; exam coverage and any numerical context limits are unverified here.

## 1. In one line
Context management allocates limited model input to relevant evidence while caching repeated prefixes where suitable and preserving where claims came from.

## 2. Problem it solves
- **Without budgeting:** irrelevant history and tool output consume tokens, raise cost/latency, and bury decision-critical evidence.
- **Without provenance:** synthesis and summaries can turn unsupported assumptions into confident claims.

## 3. 30-second context budget
```text
Available context
 - system/task instructions
 - recent conversation needed for continuity
 - retrieved source evidence
 - tool schemas/results
 - output budget
= estimated usage + safety margin
```
Prompt caching can reduce repeated processing for supported cacheable prefixes; it is not a substitute for reducing irrelevant context.

## 4. Mental model
Treat context like a working-set budget: include what changes the decision and preserve an auditable pointer to the evidence.

## 5. Under the hood
1. Inventory instructions, history, retrieved documents, tool definitions/results, and output needs.
2. Estimate token/context use with the appropriate model/API tooling; leave room for response and tool cycles.
3. Retrieve selectively, remove redundant material, and summarize only when the source detail is not needed verbatim.
4. Preserve source IDs, locations, timestamps, and uncertainty through each transformation.
5. Arrange stable repeated prefixes and use prompt caching only where API behavior, cache boundaries, privacy, and workload justify it.
6. Evaluate whether compaction or caching changes answer quality, latency, cost, or data retention.

## 6. Variants and when to use
| Technique | Use when | Trade-off |
|---|---|---|
| Retrieval | Large corpus; only a subset is relevant | Retrieval misses/incorrect ranking must be managed |
| Summarization | Long history must be compacted | Compression can drop qualifiers or exact evidence |
| Prompt caching | Repeated stable prompt prefix in eligible API flow | Cache eligibility/lifetime are API-specific |
| Subagent isolation | Exploration would flood main context | Coordination and output handoff needed |
| Full context | Small, high-recall task where source detail matters | Higher token cost and possible attention dilution |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| Caching a changing or user-sensitive segment carelessly | Stale or improperly reused context | Follow documented cache boundaries and test identity/data isolation |
| Assuming cache changes correctness | Cache affects processing/cost, not evidence quality | Evaluate answer quality independently |
| Summarizing without preserving source links | Claims cannot be checked | Keep citations/record IDs and uncertainty attached |
| Truncating oldest content silently | Important constraints may disappear | Explicitly summarize/anchor invariants and alert on truncation |
| Using “lost-in-the-middle” as a universal rule | Performance depends on task/model/context | Test placement and retrieval strategy on representative examples |

## 8. Performance, memory, and concurrency
- **Performance:** caching may reduce repeated input processing where supported; retrieval/summarization have their own latency and compute costs.
- **Concurrency:** shared cached prefixes must not contain data that crosses user/tenant boundaries.
- **Observability:** monitor input/output tokens, cache read/write metrics where available, truncation/compaction events, retrieval quality, and cost.
- **Testing:** compare full-context vs. retrieved/summarized prompts, including evidence-position and cache-isolation cases.

## 9. Related topics map
- **Prerequisites:** context lifecycle, token concepts, source metadata
- **Siblings:** prompt design, retrieval, subagent delegation, anti-fabrication
- **Downstream:** cost/latency optimization, source-grounded answer, privacy
- **Contrasts:** caching vs. memory; summarization vs. retrieval; token reduction vs. quality
- **Tools/frameworks:** Claude API prompt caching; Claude Code compaction/context tools (specific behavior varies)

## 10. Cross-domain equivalents
| Context strategy | Benefit | Main risk |
|---|---|---|
| Retrieval | Relevant slices | Missed source |
| Summary | Compact history | Lost nuance |
| Cache | Less repeated processing | Wrong boundary/stale assumptions |
| Provenance | Traceable claims | Metadata maintenance |

## 11. Interview lens
- **30-second answer:** I budget context, retrieve only relevant evidence, preserve source identity and uncertainty through summaries, and use caching only for repeated eligible content after checking isolation and current API semantics.
- **Q1 → Does caching improve factual accuracy?** Not by itself; it can improve efficiency for repeated context.
- **Q2 → How do you avoid summaries becoming fabricated truth?** Keep source references, qualifiers, and unknown states, and verify critical claims at use time.
- **Spot the bug:** Cache one shared prefix containing tenant-specific policy/customer details.  
  **Problem:** cross-tenant context risk. **Fix:** isolate cacheable data by correct boundary or exclude sensitive dynamic material.

## 12. Architect lens
- Optimize for quality under cost/latency/privacy constraints—not minimum token count alone.
- Establish a provenance contract from source retrieval through final answer and audit.
- **Version note:** token limits, cache eligibility, duration, and metrics are model/API-specific; verify current docs.

## 13. Revision summary
- Context has a finite budget and relevance matters.
- Retrieval and summaries need quality checks.
- Cache efficiency is not truth or memory.
- Preserve evidence references and tenant boundaries.
- **If you remember only one thing:** Keep enough provenance to re-check every decision-critical claim.

## 14. Coverage self-check
- [ ] Can I account for major context consumers and reserve output room?
- [ ] Can I choose retrieval vs. summary vs. full context?
- [ ] Can I describe caching trade-offs and isolation concerns?
- [ ] Can I preserve evidence and uncertainty through synthesis?

## Sources
- [Claude Code context window](https://code.claude.com/docs/en/context-window)
- [Claude Code prompt caching](https://code.claude.com/docs/en/prompt-caching)
- [Claude API prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
