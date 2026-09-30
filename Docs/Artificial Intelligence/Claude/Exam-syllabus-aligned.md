## 🧩 Domain 1: Agentic Architecture & Orchestration (27%)
- Agentic loop: lifecycle (observe → think → act → respond), stop_reason handling
- Coordinator–subagent orchestration: hub‑and‑spoke, parallel vs sequential agents
- Task decomposition: prompt chaining vs dynamic decomposition
- Human handoff patterns: escalation, ambiguity resolution
- Agent SDK hooks: PostToolUse, tool‑call interception, enforcement handoff
- Session state: --resume, fork_session
- Reliability patterns: retries, checkpointing, reversible actions, human‑in‑the‑loop interrupts

## 🛠️ Domain 2: Tool Design & MCP Integration (18%)
- Tool interface design: schema, naming conventions, description writing
- MCP components: server, client, resources, tools, prompts
- Error handling: structured error responses (isError), MCP error propagation
- Tool distribution: across agents, tool_choice parameter
- Integration configs: .mcp.json vs ~/.claude.json
- Built‑in tools: Read, Write, Edit, Bash, Grep, Glob
- Security: authentication, authorization, guardrails for MCP servers

## 💻 Domain 3: Claude Code Configuration & Workflows (20%)
- CLAUDE.md hierarchy: inheritance, @import, .claude/rules/
- Slash commands & skills: custom commands, context (fork, allowed‑tools, argument‑hint)
- Path rules: glob‑scoped conventions
- Plan mode vs direct execution
- Iterative refinement techniques
- CI/CD integration: non‑interactive mode (-p), --output-format json, --json-schema
- Agentic coding workflow: file system and terminal interaction

## ✍️ Domain 4: Prompt Engineering & Structured Output (20%)
- Explicit criteria: flag, skip, severity; reduce false positives
- Few‑shot prompting: sweet spot 2–4 pairs, diminishing returns after 5+
- Chain‑of‑thought prompting
- Role assignment in prompts
- Structured output: JSON schemas, tool_use anchoring
- Validation retry: feedback loops, retry caps, failure handling
- Message Batches API: batch processing, efficiency gains
- Multi‑pass review: iterative evaluation, error reduction
- Anti‑fabrication schemas: nullable fields, citation‑required answers

## 📂 Domain 5: Context Management & Reliability (15%)
- Context preservation: progressive summarization, lost‑in‑the‑middle effects
- Escalation & ambiguity resolution
- Error propagation: multi‑agent systems
- Confidence scoring & human review workflows
- Information provenance: multi‑source synthesis
- Token management: estimation, caching strategies, compaction
- Conversation reliability: multi‑turn state management