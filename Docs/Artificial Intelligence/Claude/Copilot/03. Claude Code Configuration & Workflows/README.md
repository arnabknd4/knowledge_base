# Domain 3 · Claude Code Configuration & Workflows

**Study status:** Strong alignment with public Claude Code documentation; exam coverage and weight are unverified.

## Topic sequence

| # | Topic | Architect outcome |
|---|---|---|
| 1 | [Instructions, memory, and scoped rules](./01-instructions-memory-and-scoped-rules.md) | Put guidance in the right scope and understand its limits. |
| 2 | [Extending Claude Code safely](./02-extending-claude-code-safely.md) | Choose skills, hooks, subagents, MCP, and settings appropriately. |
| 3 | [Engineering workflow and CI](./03-engineering-workflow-and-ci.md) | Plan, edit, verify, and automate with reviewable controls. |

## Design lens

Use persistent instructions for concise project context, skills for reusable workflows, hooks for deterministic event-triggered automation, permissions for action boundaries, and MCP for external capabilities. Check the current CLI reference before relying on flags in automation.

## Quick oral drill

A team wants Claude Code to follow repository conventions, run a formatter after edits, and never deploy without approval. Which mechanisms address each requirement—and which do not?
