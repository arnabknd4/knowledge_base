# Extending Claude Code Safely · Architect · R / E / L

> **Exam note:** The features are documented Claude Code capabilities; whether a specific option is tested is unverified.

## 1. In one line
Extend Claude Code with the smallest appropriate mechanism: reusable knowledge, isolated work, external capabilities, or deterministic automation.

## 2. Problem it solves
- **Without deliberate extension choices:** teams overconfigure, duplicate instructions, expose excessive capabilities, or rely on prompts for enforcement.
- **With clear boundaries:** each mechanism has a focused role and auditable permission surface.

## 3. 30-second selection guide
```text
Always-needed project fact?     -> CLAUDE.md
Reusable procedure/reference?   -> Skill
Separate research/task context? -> Subagent
External system capability?    -> MCP server
Must run at lifecycle event?   -> Hook
Must allow/deny an action?      -> Permission/runtime policy
Share a bundled setup?          -> Plugin (if appropriate)
```

## 4. Mental model
Extensions plug into different parts of the agent workflow; they are complementary, not interchangeable.

## 5. Under the hood
1. Define the desired behavior and its trigger before choosing a mechanism.
2. Keep skills focused and invocable/discoverable only as appropriate.
3. Delegate research or specialized work to subagents when isolation or bounded tool access helps.
4. Connect MCP servers only for required external capabilities; scope the available tools and credentials.
5. Use hooks for deterministic lifecycle automation and permissions for runtime action gates.
6. Review, test, and version control extension configuration; determine which user/project scope applies.

## 6. Variants and when to use
| Feature | Primary purpose | Architect trade-off |
|---|---|---|
| Skill | Reusable instructions/workflow | Model-invoked content still needs testing and access review |
| Subagent | Isolated specialized work | Separate context and cost; integration/permission design required |
| Hook | Deterministic lifecycle-triggered command or action | Timing and failure semantics are product-specific |
| MCP | External systems/tools | Adds a network/process trust and availability boundary |
| Plugin | Package/distribute extensions | Easier reuse; supply-chain and version governance matter |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| Using a hook for every judgment call | Deterministic checks are poor substitutes for nuanced policy review | Use prompt/agent evaluation for judgment, hard policy for invariant gates |
| Giving subagents all parent capabilities by default | Expands blast radius and hides scope | Grant only needed tools and explicitly review inherited permissions |
| Installing an MCP server without reviewing it | Adds executable or remote capability | Verify source, auth, data flow, permissions, and update policy |
| Creating a skill for a one-off prompt | Adds unnecessary configuration | Keep transient work in the task prompt |
| Assuming plugins or skills enforce security | They primarily package/instruct behavior | Keep security controls in permissions and service boundaries |

## 8. Performance, memory, and concurrency
- **Context:** skills and subagents can reduce always-loaded content or isolate noisy work.
- **Latency/cost:** hooks, subagents, and external calls add work; measure the whole task, not only model turn count.
- **Concurrency:** extension setup can be shared across team sessions; define ownership and avoid conflicting configuration edits.
- **Testing:** validate hook timing/failure behavior, MCP server access, skill triggering, subagent scope, and plugin update path.

## 9. Related topics map
- **Prerequisites:** Claude Code instruction scope, agent loop, permissions
- **Siblings:** context management, CI workflows, MCP security
- **Downstream:** team standards, automation, operations
- **Contrasts:** all-in-one prompt, broad hook script, unrestricted MCP connection
- **Tools/frameworks:** Claude Code skills, subagents, hooks, MCP, plugins

## 10. Cross-domain equivalents
| Need | Preferred mechanism | Avoid conflating with |
|---|---|---|
| Reusable procedure | Skill | Persistent instruction |
| Isolated execution | Subagent | Simple prompt template |
| External capability | MCP | Prompt text saying data is available |
| Deterministic automation | Hook | Model-selected tool call |
| Enforce access | Permission/runtime policy | Skill or CLAUDE.md |

## 11. Interview lens
- **30-second answer:** I map requirement to trigger and control: instructions for durable context, skills for reusable procedures, subagents for isolated work, MCP for external systems, hooks for deterministic lifecycle events, and permissions for access enforcement.
- **Q1 → Hook or skill for formatting?** A skill can describe a formatting workflow; a hook is appropriate when formatting must run deterministically at a defined event.
- **Q2 → MCP or prompt context for current Jira state?** MCP or another authorized integration is needed to retrieve live state; a prompt cannot make stale text current.
- **Spot the bug:** A deployment skill says “ask before deploy,” and the CI credential is unrestricted.  
  **Problem:** the credential can still deploy without a reliable gate. **Fix:** enforce approval/authorization where deployment executes.

## 12. Architect lens
- Inventory extension capabilities and owners; scope who can configure/install them.
- Apply least privilege, version pinning/review, audit, and secret management.
- **Version note:** feature names, plugin behavior, skills frontmatter, and hook semantics can change.

## 13. Revision summary
- Choose extensions based on the job and trigger.
- Skills, subagents, hooks, and MCP solve different problems.
- Permissions enforce actions; prompts guide them.
- Review extension provenance and scope.
- **If you remember only one thing:** Select the mechanism by its runtime role, not by whichever feature sounds most agentic.

## 14. Coverage self-check
- [ ] Can I choose the right Claude Code extension for a requirement?
- [ ] Can I state permissions and trust implications for that extension?
- [ ] Can I test trigger, scope, timing, and failure behavior?
- [ ] Can I explain where an actual security gate lives?

## Sources
- [Claude Code feature overview](https://code.claude.com/docs/en/features-overview)
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code hooks](https://code.claude.com/docs/en/hooks-guide)
- [Claude Code MCP](https://code.claude.com/docs/en/mcp)
