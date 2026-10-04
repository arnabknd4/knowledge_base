# Claude Certified Architect – Foundations (CCAR-F): Study Map

> **Verification warning (2026-10-04):** This document's exam identity, format, question count, duration, scenario list, pass score, price, validity period, domain names, and domain weights have not been verified against a first-party Anthropic exam blueprint. Treat them as unverified notes, not official exam facts. See [Exam-syllabus-aligned.md](./Exam-syllabus-aligned.md) for the product-document alignment audit and sources.

## Exam Snapshot
- 60 items (multiple-choice and multiple-response), 120 minutes, proctored
- 4 scenarios presented at random from a bank of 6
- Pass mark: scaled 720 on a 100–1,000 scale
- Valid for 12 months; fee $125 USD
- Core tech tested: Claude Code, Claude Agent SDK, Claude API, MCP

## The 6 Scenarios
1. Customer Support Resolution Agent
2. Code Generation with Claude Code
3. Multi-Agent Research System
4. Developer Productivity with Claude
5. Claude Code for CI/CD
6. Structured Data Extraction

## Domain 1: Agentic Architecture & Orchestration (27%)
- Agentic loop and stop_reason handling
- Coordinator–subagent (hub-and-spoke) orchestration
- Subagent spawning, Task tool, and explicit context passing
- Workflow enforcement and human handoff patterns
- Agent SDK hooks (PostToolUse, tool-call interception)
- Task decomposition: prompt chaining vs dynamic decomposition
- Session state: --resume and fork_session

## Domain 2: Tool Design & MCP Integration (18%)
- Tool descriptions and boundaries
- Structured error responses for MCP tools (isError)
- Tool distribution across agents and tool_choice
- MCP server integration (.mcp.json vs ~/.claude.json, MCP resources)
- Built-in tools: Read, Write, Edit, Bash, Grep, Glob

## Domain 3: Claude Code Configuration & Workflows (20%)
- CLAUDE.md hierarchy, @import, and .claude/rules/
- Custom slash commands and skills (context: fork, allowed-tools, argument-hint)
- Path-specific rules (glob-scoped conventions)
- Plan mode vs direct execution
- Iterative refinement techniques
- Claude Code in CI/CD (-p, --output-format json, --json-schema)

## Domain 4: Prompt Engineering & Structured Output (20%)
- Explicit criteria and false-positive reduction
- Few-shot prompting
- Structured output via tool_use and JSON schemas
- Validation, retry, and feedback loops
- Message Batches API
- Multi-instance and multi-pass review

## Domain 5: Context Management & Reliability (15%)
- Preserving critical information across long conversations
- Escalation and ambiguity resolution
- Error propagation in multi-agent systems
- Context management in large codebase exploration
- Human review workflows and confidence calibration
- Information provenance in multi-source synthesis

## Explicitly Out of Scope
- Fine-tuning, model internals, Constitutional AI/RLHF
- API auth, billing, rate limits, pricing calculations
- Hosting/deploying MCP servers
- Computer use, vision, streaming API
- Specific cloud provider configurations
- Embeddings and vector databases