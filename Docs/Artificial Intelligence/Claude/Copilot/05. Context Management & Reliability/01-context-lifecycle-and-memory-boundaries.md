# Context Lifecycle and Memory Boundaries · Architect · R / E / L

> **Exam note:** These context concepts are documented product behavior and architecture guidance; exam coverage is unverified.

## 1. In one line
Context is the information supplied to a model for a turn; persistence, memory, and durable workflow state must be designed separately.

## 2. Problem it solves
- **Without lifecycle clarity:** systems assume the model remembers everything, persist the wrong data, or leak unrelated context across tasks.
- **With explicit boundaries:** each turn receives necessary evidence while durable state and access control remain in application systems.

## 3. 30-second lifecycle sketch
```text
Durable application state / source of truth
   -> select relevant evidence + current task state
   -> assemble model context for this turn
   -> optional tool/subagent with scoped context
   -> validate response and persist approved state externally
```

## 4. Mental model
The context window is a working set for inference, not a database, guaranteed memory, or authorization boundary.

## 5. Under the hood
1. Distinguish API message history from Claude Code project instructions, session transcript, auto memory, and subagent context.
2. Know which data is sent to each model/tool and when new turns or sessions start.
3. Select relevant source material and pass minimum necessary context to each worker.
4. Summaries are derived representations; retain links/provenance and confirm critical facts against source-of-truth systems.
5. Persist durable workflow state externally with identity, schema, ownership, version, and retention controls.
6. On resume, rebuild context from validated stored state rather than assuming a previous model context remains intact.

## 6. Variants and when to use
| State mechanism | Use when | Trade-off |
|---|---|---|
| Conversation history | Recent interaction matters to next response | Grows context and may retain irrelevant/sensitive data |
| Project instructions | Stable repository guidance | Broadly loaded context; not durable business state |
| Auto memory | Learned user/project patterns | Fallible and needs review |
| Summarized context | Long history needs compact handoff | Can omit caveats; validate key details |
| Application state store | Workflow must resume reliably | Requires schema, security, and lifecycle design |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| Treating long context as perfect recall | Relevant facts can be missed or displaced | Retrieve/anchor key evidence and test recall-sensitive tasks |
| Treating summary as source of truth | Errors become durable and lose provenance | Store citations/IDs and re-check critical facts |
| Passing entire transcript to every subagent | Costs tokens and leaks irrelevant personal data | Purpose-limit context per assignment |
| Using auto memory for secrets or authoritative state | Memory can be stale and inappropriate to trust | Use secure app storage and reviewed configuration |
| Assuming a resumed workflow retained hidden state | Process/session may not retain all state | Persist explicit checkpoint and reconstruct/validate |

## 8. Performance, memory, and concurrency
- **Context cost:** prompt/history/tool outputs all compete for a bounded window; selective retrieval and summaries help.
- **Concurrency:** subagents have distinct contexts; copy only necessary state and correlate their outputs to task IDs.
- **Privacy:** define which user/project data enters model context, logs, memory, and external tools.
- **Testing:** simulate long sessions, context compaction, missing memory, stale summaries, and cross-user isolation.

## 9. Related topics map
- **Prerequisites:** model requests, sessions, source-of-truth systems
- **Siblings:** delegation, prompt caching, summarization, provenance
- **Downstream:** recovery, privacy, continuity, application persistence
- **Contrasts:** working context vs. durable state; memory vs. evidence
- **Tools/frameworks:** Claude Code memory/context; application persistence/retrieval

## 10. Cross-domain equivalents
| Concept | Example | Reliability implication |
|---|---|---|
| Working set | Current model messages | Bounded and turn-specific |
| Project guidance | `CLAUDE.md` | Context, not authoritative transaction data |
| Learned memory | Auto memory | Can be incomplete or stale |
| Durable state | Database/checkpoint | Must be validated, access-controlled, versioned |

## 11. Interview lens
- **30-second answer:** I separate model working context from durable state, selectively assemble evidence for each task, preserve provenance in summaries, and reconstruct resumed workflows from validated application state.
- **Q1 → Does a larger context window remove the need for retrieval/summarization?** No. Cost, relevance, privacy, and attention remain design concerns.
- **Q2 → What should persist between agent steps?** Explicit workflow state, required identifiers/evidence references, and completion status—not unvalidated model assumptions.
- **Spot the bug:** Store the entire conversation as an authoritative customer profile.  
  **Problem:** conversation may include errors, sensitive excess, and stale claims. **Fix:** extract validated fields with provenance into a controlled data store.

## 12. Architect lens
- Specify context sources, identity scoping, retention, redaction, retrieval, and provenance.
- Define session/resume semantics and safe behavior when checkpoints are missing or stale.
- **Version note:** Claude Code memory loading and context handling can change; check current docs for specific limits and behavior.

## 13. Revision summary
- Context is not persistence.
- Memory is not necessarily authoritative or correct.
- Summaries need provenance and validation.
- Rebuild resumable work from explicit external state.
- **If you remember only one thing:** Keep the source of truth outside the model context.

## 14. Coverage self-check
- [ ] Can I distinguish API history, Claude Code memory, subagent context, and app state?
- [ ] Can I design a privacy-aware context handoff?
- [ ] Can I preserve evidence through summarization?
- [ ] Can I resume safely from a validated checkpoint?

## Sources
- [Claude Code memory](https://code.claude.com/docs/en/memory)
- [Claude Code context window](https://code.claude.com/docs/en/context-window)
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
