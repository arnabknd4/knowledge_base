# Instructions, Memory, and Scoped Rules · Architect · R / E / L

> **Exam note:** Claude Code configuration is product-grounded; exam coverage is not verified.

## 1. In one line
Claude Code instruction and memory files provide scoped context to guide behavior; they are not substitutes for enforced permissions or policy.

## 2. Problem it solves
- **Without organized instructions:** teams repeatedly explain project conventions, commands, and architecture context.
- **With scoped instructions:** persistent facts load at an appropriate scope, while specialized rules can be separated from always-needed context.

## 3. 30-second scope sketch
```text
Organization policy -> user preferences -> project instructions
                                      -> path-specific rules / local context
Skills: reusable procedures loaded when relevant
Permissions/hooks: separate mechanisms for controlling/enforcing actions
```
This is a conceptual map, not a guaranteed precedence diagram. Loading and merge behavior must be checked in current documentation.

## 4. Mental model
Instruction files are context the model is asked to follow; access controls and deterministic hooks are controls the runtime can enforce.

## 5. Under the hood
1. Claude Code loads applicable project/user/managed guidance according to documented locations and scope.
2. `CLAUDE.md` holds concise instructions and project facts; `AGENTS.md` may also be supported in documented circumstances.
3. `.claude/rules/` supports modular or path-specific rules; imports can include reusable instruction content.
4. Auto memory is a separate mechanism for learned notes; it should be reviewed for correctness and sensitivity.
5. A separate permission or hook mechanism is needed when an action must be blocked regardless of model interpretation.

## 6. Variants and when to use
| Mechanism | Use when | Trade-off |
|---|---|---|
| Project `CLAUDE.md` | Stable conventions, commands, architecture facts | Loads broadly; keep concise |
| User/managed instruction | Personal preference or organization-wide direction | Scope may be too broad for project-only rules |
| `.claude/rules/` | Modular or path-relevant guidance | More files and matching behavior to maintain |
| Skill | Reusable procedure or reference material used on demand | Invocation/description must make appropriate use discoverable |
| Permission/hook | Action needs enforceable restriction or deterministic event behavior | Configuration and testing required |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| Putting a long manual in root instructions | Consumes context and dilutes high-priority guidance | Keep only durable facts; move procedures/references to skills/rules |
| Assuming hierarchy works like CSS overrides | Behavior may not match the metaphor | Verify documented loading and conflicts; avoid unsupported precedence assumptions |
| Treating `CLAUDE.md` as authorization | The model may not follow instructions | Enforce action permissions in settings/runtime/service |
| Storing secrets or private environment values | Instructions may be loaded, copied, or logged | Use secret stores/environment injection; never commit credentials |
| Letting auto memory become unreviewed policy | Learned notes can be stale or wrong | Review, scope, and correct memory; use explicit policy controls |

## 8. Performance, memory, and concurrency
- **Context:** every always-loaded instruction competes with task evidence; move infrequent details to on-demand mechanisms.
- **Performance:** concise, relevant context reduces avoidable reading and ambiguity.
- **Concurrency:** shared project guidance should be version controlled and reviewed like code; local/private instructions must not silently override team safety policy.
- **Testing:** start a clean session and verify which files loaded; test a path-specific rule against matching and nonmatching files.

## 9. Related topics map
- **Prerequisites:** Claude Code project scope and context lifecycle
- **Siblings:** skills, hooks, permissions, MCP, subagents
- **Downstream:** repeatable workflows, policy compliance, context management
- **Contrasts:** prompt text vs. deterministic enforcement; memory vs. source of truth
- **Tools/frameworks:** `CLAUDE.md`, `AGENTS.md`, `.claude/rules/`, skills, settings

## 10. Cross-domain equivalents
| Need | Claude Code mechanism | Architect caution |
|---|---|---|
| Persistent project facts | `CLAUDE.md` | Context, not hard enforcement |
| Path-specific guidance | `.claude/rules/` | Validate matching and load scope |
| Repeated procedure | Skill | Not the same as a permission boundary |
| Block risky action | Permissions/hooks | Confirm exact enforcement point |

## 11. Interview lens
- **30-second answer:** I keep durable project facts concise in instructions, put conditional procedures in skills or scoped rules, and use runtime permissions/hooks for actions that must be enforced.
- **Q1 → Should all documentation go into `CLAUDE.md`?** No. Keep always-needed context small; put procedures/reference material in on-demand or scoped files.
- **Q2 → Can path-scoped guidance stop an unauthorized write?** Not reliably as a security control; use an enforced permission boundary.
- **Spot the bug:** “The agent cannot deploy because `CLAUDE.md` says not to.”  
  **Problem:** guidance is not an authorization check. **Fix:** disable or gate deployment at the execution layer and verify the control.

## 12. Architect lens
- Document ownership, scope, loading, review, and data classification for instruction files.
- Treat generated memory as fallible context; keep system-of-record data elsewhere.
- **Version note:** supported file locations, imports, precedence, and memory behavior evolve; verify current Claude Code docs.

## 13. Revision summary
- Instructions provide context and guidance.
- Rules can modularize or scope guidance.
- Skills carry reusable on-demand procedures.
- Permissions/hooks enforce separate runtime behavior.
- **If you remember only one thing:** Do not confuse “the model was told not to” with “the system prevents it.”

## 14. Coverage self-check
- [ ] Can I choose between instructions, scoped rules, skills, permissions, and hooks?
- [ ] Can I explain context cost and why to keep global guidance concise?
- [ ] Can I avoid unsupported inheritance/override assumptions?
- [ ] Can I prove an action restriction is enforced?

## Sources
- [Claude Code memory](https://code.claude.com/docs/en/memory)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code hooks](https://code.claude.com/docs/en/hooks-guide)
