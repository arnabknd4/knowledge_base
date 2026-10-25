### Lesson 6: Claude Code Configuration and Workflows

Before moving into the mock exam, we need to cover the remaining domain in our learning sequence: Claude Code configuration and workflows.

The focus is on how Claude Code is configured for a project, how instructions are applied consistently, and how developers organise repeatable coding workflows. We will keep this tied to the certification objectives rather than branching into unrelated software-engineering topics.

The key architectural distinction is that configuration establishes the working environment and constraints; workflow design determines how the work is carried out.

### 1\. `CLAUDE.md`: persistent project instructions

Claude Code can read `CLAUDE.md` files to obtain project instructions. These can describe the architecture, coding conventions, test commands, and important development constraints.

For example:

```markdown
# Project instructions

## Architecture
- Keep business logic in the service layer.
- Follow the existing module boundaries.

## Testing
- Run the relevant unit tests after changing code.
- Add regression tests for bug fixes.

## Constraints
- Do not modify database migrations without explaining why.
- Never include credentials in source code.
```

The purpose is to avoid repeating the same instructions in every request.

Claude Code supports different instruction scopes. The main distinction to remember is:

* Project instructions: shared conventions that belong with the repository.

* Personal instructions: preferences that apply to an individual's work across projects.

* More local instructions: rules relevant to a particular part of a codebase.

Keep instructions concise, specific, and maintained. A large, contradictory `CLAUDE.md` can make the intended workflow less clear. Also, instructions guide Claude; they do not replace tool permissions or enforcement in the surrounding environment.

### 2\. Configuration and permissions

Claude Code configuration controls aspects of its behaviour, including which tools can be used and when approval is required.

Suppose a developer asks Claude Code to fix a bug. Reading source files and running a permitted test may be acceptable without additional approval in a configured environment. Deleting production data or executing a destructive shell command requires a different level of control.

A sound configuration follows least privilege: grant only the access needed for the task, and use approval controls for sensitive operations.

Do not confuse instructions with permissions:

| Mechanism                | Responsibility                                       |
| ------------------------ | ---------------------------------------------------- |
| CLAUDE.md                | Project guidance and conventions                     |
| Permission configuration | Controls over tool use and approval                  |
| Hooks                    | Run configured actions at specified lifecycle events |
| Skills                   | Reusable task-specific instructions and workflows    |

A sentence in `CLAUDE.md` saying “never delete files” is not equivalent to a technical permission control that blocks deletion.

### 3\. Skills, subagents, and hooks

These capabilities solve different workflow problems.

Skills — reusable expertise or procedures

A skill can package instructions for a recurring task, such as reviewing a pull request against a team's checklist. It can be reused rather than rewritten in every prompt.

Subagents — delegated work

A subagent can focus on a bounded task, such as reviewing a module or investigating a particular defect. Delegation is useful when a task benefits from separation of responsibilities, but it adds coordination overhead.

Hooks — lifecycle-triggered automation

Hooks run configured commands or actions at specified points in a workflow. They are useful for repeatable checks or enforcement tasks that should not depend solely on the model remembering an instruction.

For example, a code-change workflow might use a project instruction file to explain the architecture, a skill to provide the team's review procedure, a subagent to inspect security implications, and a hook to run a configured check.

The important exam skill is recognising which mechanism fits the requirement, rather than choosing the most elaborate one.

### 4\. Make coding workflows repeatable

Consider a team that wants Claude Code to fix defects consistently.

A reasonable workflow is:

* Understand the issue and inspect the relevant code.

* Identify the likely cause and propose an approach.

* Make a bounded code change.

* Run relevant tests and inspect the diff.

* Report what changed, which checks passed, and what remains unresolved.

For a small, well-defined bug, a single agent may be sufficient. For a complex change, a planning step or specialised review may be useful. A team may also use automation in its CI workflow to trigger a review or coding task.

In non-interactive use, CLI options such as `--max-turns` can limit agentic iterations, while output-format options can make results easier for scripts to consume. These controls help make automated workflows more predictable.

Automation should not mean unrestricted execution. Limit repository access and credentials, review changes before merging, and ensure the workflow has appropriate timeouts and failure handling.

### 5\. Exam practice

A development team wants Claude Code to follow shared coding conventions, use a reusable pull-request review procedure, and automatically run a required check at a particular workflow event.

Which mapping is most appropriate?

A. Put everything in the user's prompt for every session.

B. Use `CLAUDE.md` for shared project instructions, a skill for the reusable review procedure, and a hook for the event-triggered check.

C. Use a subagent for all three requirements because subagents can replace project configuration and automation.

D. Use permission settings to store coding conventions and the review checklist.

Check answer

### Correct.

Project instructions, reusable procedures, and lifecycle-triggered automation have distinct responsibilities. Choosing the right mechanism reduces repetition and makes the workflow more predictable.

### Lesson 6 summary

Remember the distinctions:

* `CLAUDE.md` provides persistent project guidance.

* Permission configuration controls tool access and approvals.

* Skills package reusable task procedures.

* Subagents delegate bounded work.

* Hooks trigger configured automation at workflow events.

* Repeatable workflows should include verification, bounded execution, and appropriate review.

The five exam domains have now each received an introductory lesson. Next, we should move into scenario-based revision, where you will have to choose an architecture or configuration, explain the trade-offs, and identify unsafe alternatives. This is more useful than memorising definitions alone.
