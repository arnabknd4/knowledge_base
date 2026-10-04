# Claude Architect Foundations: Syllabus Alignment Audit

**Audit date:** 2026-10-04
**Status:** Provisional study map; official exam alignment is **not verified**.

## Finding

The five areas below are a reasonable curriculum for learning to design with Claude Code, the Claude API, agents, and MCP. The subjects are supported by Anthropic's public product documentation. However, I could not verify a public, first-party exam blueprint that confirms this exam title, these five domains, their weights, or the individual objectives. Product documentation establishes that a feature exists; it does **not** establish that the exam tests it.

Use this file as a product-document-aligned study map, not as an official exam syllabus. Treat all exam-specific weights, question counts, scenarios, fees, pass marks, renewal periods, and predictions about likely questions as **unverified** unless you can match them to an official exam guide.

## Domain-by-domain alignment

### 1. Agentic Architecture & Orchestration

**Product-document alignment: Strong. Exam alignment: Unverified.**

- Understand the agentic loop as gathering context, taking action, and verifying results; expect the loop to adapt and allow human interruption.
- Know when a single agent is sufficient and when delegation is useful. Understand subagents' isolated context, scoped tools/permissions, delegation inputs, and summarized results.
- Compare sequential and parallel work, coordinator/worker patterns, task decomposition, and the trade-offs in context use, latency, cost, and failure handling.
- Handle tool-use cycles, including tool-call/result handoff and completion/stop reasons. Do not treat every agent loop as the same fixed `observe → think → act → respond` sequence.
- Cover human approval or escalation, interrupted work, bounded retries, recovery, and verification of consequential actions.
- Distinguish Claude Code subagents, Claude Agent SDK capabilities, and application-level orchestration; similarly named features do not necessarily share APIs or lifecycle semantics.
- For SDK-specific notes, verify event names and behavior against the versioned SDK documentation. Avoid presenting one hook name such as `PostToolUse` as a universal Agent SDK hook.

### 2. Tool Design & MCP Integration

**Product-document alignment: Strong. Exam alignment: Unverified.**

- Design tool names, input schemas, descriptions, examples, clear boundaries, and useful high-signal results. Explain when a tool should and should not be called.
- Know the Claude API tool-use round trip: Claude returns a tool call, the client executes client-side tools and returns a tool result; distinguish these from Anthropic-hosted server tools.
- Understand tool selection and tool-use controls, structured errors, and how the application should handle failed calls and untrusted results.
- Cover MCP's client/server model and its tools, resources, and prompts. Understand the transport, authentication, configuration, consent, and trust boundaries relevant to the client being used.
- Apply least privilege, authorization, secret handling, input validation, and human approval to tools that can access data or cause side effects.
- Keep MCP concepts distinct from Claude API tools and Claude Code's built-in tools. `Read`, `Write`, `Edit`, `Bash`, `Grep`, and `Glob` are Claude Code tool names, not a universal tool set for every Claude integration.

### 3. Claude Code Configuration & Workflows

**Product-document alignment: Strong. Exam alignment: Unverified.**

- Cover `CLAUDE.md` instruction scopes, `AGENTS.md` where relevant, imports, `.claude/rules/`, and the distinction between guidance and enforced controls.
- Cover settings and permission scopes, plan/permission modes, hooks, MCP servers, subagents, skills, and plugins; choose the smallest extension that meets a workflow need.
- Treat custom commands as part of the current skills model: current Claude Code documentation says custom commands have been merged into skills, while existing command files remain compatible.
- Include practical explore → plan → edit/act → verify workflows, review of diffs, test execution, and recovery from failed commands or incorrect changes.
- Cover non-interactive/CI use and output handling only against the current Claude Code CLI reference. Flags and output formats can change; do not memorize options without a versioned source.
- Do not describe instruction files as a security boundary: use permissions, hooks, or other deterministic controls for actions that must be enforced.

### 4. Prompt Engineering & Structured Output

**Product-document alignment: Strong. Exam alignment: Unverified.**

- Start with explicit success criteria and evaluations; improve prompts based on measured failures rather than relying on prompt folklore.
- Cover clear, direct instructions; relevant examples; XML structuring where useful; role/context; prompt chaining; and thinking features according to current model/API documentation.
- For tool use, understand tool descriptions, schemas, tool choice, and strict input validation where supported.
- For JSON outputs, understand schema constraints, parsing/SDK helpers, and how to handle refusals, truncation, and application-level semantic validation. Schema-conforming output is not proof that the content is factually correct.
- Use bounded validation/retry loops with explicit stop conditions and human review where necessary.
- The Message Batches API is an asynchronous bulk-processing API. It is a valid API capability, but its inclusion in this exam is **not verified** and it is not itself a prompting technique.

### 5. Context Management & Reliability

**Product-document alignment: Strong. Exam alignment: Unverified.**

- Distinguish Claude API context from Claude Code session context, project instructions, auto memory, and subagent context. Understand what persists, what is reloaded, and what is summarized or isolated.
- Cover context-window budgeting, selective context loading, compaction/summarization, prompt caching, and the trade-offs between retaining detail and reducing context.
- Preserve provenance: keep source evidence and uncertainty visible when summarizing or combining information; do not let a summary silently turn an assumption into a fact.
- Design reliability around bounded retries, timeouts, tool/API errors, idempotency for side effects, checkpoints or recovery where appropriate, and verification of final results.
- Add observability and evaluation: record useful inputs, tool actions, outcomes, and errors while respecting privacy and data-retention requirements.
- Use confidence estimates as routing signals only when calibrated and validated; do not present model confidence as a guarantee of correctness.
- Human escalation, permissions, and safety controls overlap with the other domains and should be taught as cross-cutting practices rather than exclusive topics in this domain.

## Claims to keep flagged in the existing study notes

- **Domain percentages (27%, 18%, 20%, 20%, 15%):** no first-party exam blueprint located to verify these weights.
- **Exam logistics and scenario bank in `Exam-Syllabus.md`:** number of items, duration, proctoring, pass score, fee, validity, and named scenarios are unverified from first-party sources.
- **Exact few-shot counts (for example, “2–4 pairs” or diminishing returns after “5+”):** do not present as a universal Anthropic rule; test examples against the task and current model.
- **“Chain-of-thought prompting”:** revise to current, documented thinking/prompting guidance. Do not assume hidden reasoning should be requested or exposed.
- **“Lost-in-the-middle” as an exam objective, Message Batches as an exam objective, and anti-fabrication schema patterns:** plausible study subjects or techniques, but exam inclusion is not verified by a public blueprint.
- **CLAUDE.md hierarchy claims:** the official docs describe instruction loading and scope; do not assume CSS-like override semantics unless a specific rule is documented. Keep enforceable security controls separate from prompt instructions.
- **Standards mappings (such as ISO 42001 or NIST AI RMF):** these may be useful external study context, but they do not establish exam coverage.

## Public first-party references checked

These references support product-feature alignment only, not exam coverage:

- [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works) — agentic loop, tools, context gathering, action, and verification.
- [Claude Code feature overview](https://code.claude.com/docs/en/features-overview) — choosing among CLAUDE.md, skills, subagents, hooks, MCP, and plugins.
- [Claude Code memory](https://code.claude.com/docs/en/memory) — instruction files, scopes, rules, and auto memory.
- [Claude Code skills](https://code.claude.com/docs/en/skills) — skills, command compatibility, and invocation.
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents) — isolated contexts, tools, permissions, and delegation.
- [Claude Code hooks](https://code.claude.com/docs/en/hooks-guide) — lifecycle hooks and deterministic automation.
- [Claude Code context window](https://code.claude.com/docs/en/context-window) — context loading and compaction concepts.
- [Claude API tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) and [tool definitions](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) — tool execution flow, schemas, descriptions, and controls.
- [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) — schema-constrained JSON and strict tool use.
- [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) — success criteria, evaluation, and prompting resources.
- [Message Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing) — asynchronous bulk processing.
- [MCP introduction](https://modelcontextprotocol.io/introduction) — MCP purpose and core concepts.

## Recommendation

Keep the five folders as a practical learning structure, with the coverage additions and caveats above. The architect-level lessons and capstone are in [Copilot/](./Copilot/README.md). Until an official exam blueprint is available, label the map and exam-specific notes **provisional / not verified**, and do not use the percentages or exam logistics as planning facts.
