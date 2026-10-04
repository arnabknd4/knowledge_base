# Engineering Workflow and CI · Architect · R / E / L

> **Exam note:** This workflow is grounded in Claude Code documentation; exam coverage and exact CLI flags are unverified.

## 1. In one line
An effective coding-agent workflow makes exploration, planning, edits, verification, and human review observable and appropriately gated.

## 2. Problem it solves
- **Without a workflow:** the agent may edit before understanding, miss tests, or produce changes that appear complete but are unverified.
- **With an explicit workflow:** changes are scoped, reviewable, tested, and integrated under normal engineering controls.

## 3. 30-second workflow
```text
Issue + acceptance criteria
 -> inspect repository/context
 -> propose plan for material or risky changes
 -> edit in small reviewable steps
 -> run targeted checks and inspect diff
 -> report verified results + remaining risks
 -> human review / merge / deploy through existing gates
```

## 4. Mental model
Claude Code is an agentic development interface, not a replacement for the repository's build, test, review, and release controls.

## 5. Under the hood
1. Provide task goal, constraints, acceptance criteria, and commands.
2. Let the agent gather relevant repository context rather than guessing architecture.
3. Use planning for broad/uncertain work; keep a direct path for small, reversible edits.
4. Inspect every diff and run the smallest checks that cover the change, escalating to broader suites as appropriate.
5. In CI, use non-interactive execution and machine-readable output only after validating current CLI semantics, exit codes, permissions, and failure reporting.
6. Preserve human review and protected branch/release policies for consequential changes.

## 6. Variants and when to use
| Workflow | Use when | Trade-off |
|---|---|---|
| Direct edit | Small, clear, low-risk task | Fast; requires still verifying result |
| Plan then edit | Broad changes, uncertain scope, multiple files | Better alignment; plan adds time |
| Agent-assisted CI check | Repeatable review or bounded automated task | Scales; must constrain access and output |
| Human-in-loop PR | Shared or high-impact change | Review cost; preserves accountable approval |

## 7. Pitfalls and fixes
| Pitfall | Why it bites | Fix |
|---|---|---|
| Relying on a generated plan without checking implementation | Plans can omit constraints or tests | Review diff and verify acceptance criteria |
| Running broad write-capable CI agent with production secrets | Prompt compromise or tool misuse could expose secrets | Use least-privilege ephemeral credentials and isolated runners |
| Parsing human prose as CI protocol | Output format is unstable | Use documented machine output, schema/exit code checks |
| Treating green tests as proof of correctness | Tests can miss requirements/regressions | Include acceptance checks, review diff, and risk-based evaluation |
| Automating merge/deploy by default | Error impact exceeds task boundary | Preserve protected approvals and deterministic gates |

## 8. Performance, memory, and concurrency
- **Performance:** target checks first; scale to full suite when change scope or risk warrants it.
- **Concurrency:** parallel read-only analysis may help, but concurrent edits or shared worktrees need isolation and conflict handling.
- **Observability:** preserve task ID, tool/command outcomes, changed files, test outputs, and final disposition while protecting secrets.
- **Testing:** exercise CI with denied permissions, timeout, malformed JSON/output, failed tests, and no-op diff.

## 9. Related topics map
- **Prerequisites:** Claude Code instructions, tools, permissions, task acceptance criteria
- **Siblings:** skills, hooks, subagents, context management
- **Downstream:** pull request, release, deployment, audit
- **Contrasts:** blind auto-commit, prompt-only CI control, unreviewed generated patch
- **Tools/frameworks:** Claude Code CLI/IDE; repository CI and test framework

## 10. Cross-domain equivalents
| Software lifecycle | Agent workflow |
|---|---|
| Requirements | Prompt + acceptance criteria |
| Developer investigation | Context gathering |
| Implementation | Tool-mediated edits |
| Build/test/review | Verification and human review |
| Release policy | CI permissions and protected gates |

## 11. Interview lens
- **30-second answer:** I use Claude Code to accelerate investigation and implementation, but retain repository-native tests, diff review, least-privilege CI, and protected merge/deploy controls.
- **Q1 → When is plan mode useful?** When scope, dependencies, or risk justify an explicit approach before edits; not for every trivial change.
- **Q2 → How do you make CI output reliable?** Pin documented invocation behavior, validate exit status and machine-readable shape, constrain permissions, and fail visibly on parse/test errors.
- **Spot the bug:** CI runs a coding agent with a release token and accepts `"all tests pass"` from its final text.  
  **Problem:** excessive credential and self-reported verification. **Fix:** run independent test steps with scoped credentials; gate release separately.

## 12. Architect lens
- Integrate with existing CI identity, sandboxing, artifacts, approval, and audit controls.
- Verify current command flags/output format against the official CLI reference; do not preserve stale snippets as policy.
- **Version note:** Claude Code CLI options and non-interactive behavior are version-sensitive.

## 13. Revision summary
- Gather context before edits.
- Plan proportional to task uncertainty and risk.
- Review diffs and verify outcomes independently.
- Keep CI credentials and release gates least-privileged.
- **If you remember only one thing:** Agent-produced changes still need ordinary engineering verification.

## 14. Coverage self-check
- [ ] Can I choose direct vs. plan-first workflow?
- [ ] Can I define acceptance criteria and verification?
- [ ] Can I secure agent use in CI?
- [ ] Can I avoid relying on unverified CLI options or model self-report?

## Sources
- [Claude Code common workflows](https://code.claude.com/docs/en/common-workflows)
- [Claude Code overview](https://code.claude.com/docs/en/overview)
- [Claude Code feature overview](https://code.claude.com/docs/en/features-overview)
