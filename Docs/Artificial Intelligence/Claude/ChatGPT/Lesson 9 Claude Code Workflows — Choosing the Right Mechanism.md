Lesson 12: Claude Code Workflows — Choosing the Right Mechanism

The objective of this lesson is to distinguish Claude Code's configuration and workflow mechanisms and select the right one for a given requirement.

The key principle is use instructions to guide behaviour, reusable capabilities to standardise tasks, delegation to divide work, hooks to automate lifecycle events, and permissions to control access.

We will study each mechanism, then apply the distinctions to exam-style scenarios.

1. Persistent instructions: CLAUDE.md

Claude Code can use CLAUDE.md files to obtain instructions about a project or working environment.

Typical contents include:

- Project architecture and module boundaries.
- Coding conventions.
- Relevant build and test commands.
- Repository-specific requirements.
- Constraints that should guide future coding tasks.

For example, a project might require Claude Code to follow existing service-layer boundaries, run relevant tests after making changes, and avoid modifying database migrations without a clear reason.

These instructions reduce the need to repeat the same guidance in every request.

When to use it: When Claude Code needs persistent guidance about how work should be performed in a project.

Important limitation: Instructions guide the model; they do not guarantee compliance. They are not a substitute for permissions or technical safeguards.

2. Skills: reusable knowledge and workflows

A skill packages instructions, domain knowledge, or a repeatable procedure that Claude Code can use when appropriate.

For example, a team may repeatedly ask Claude Code to review pull requests against the same checklist. Instead of including that checklist in every request, the team can create a reusable skill.

Skills are useful for:

- Standardising recurring tasks.
- Packaging project-specific procedures.
- Providing domain knowledge when needed.
- Reducing repeated prompting.

When to use it: When a task procedure or body of knowledge should be reusable.

A skill is not the same as a hook. A skill provides instructions that Claude can apply; a hook triggers configured automation at a particular event.

Official reference: [Claude Code — Extend Claude Code](https://code.claude.com/docs/en/features-overview?utm_source=chatgpt.com)

3. Subagents: delegate bounded tasks

A subagent is a specialised worker that performs a task using its own context and returns results to the main agent.

Suppose Claude Code needs to investigate a defect in a large repository. The main agent might delegate separate tasks to investigate:

- The relevant service implementation.
- Related tests.
- Potential security implications.

The main agent then reviews the findings and decides what to do next.

Subagents can help when tasks are independent, require specialised instructions, or involve extensive investigation that would otherwise fill the main conversation's context.

However, delegation adds overhead. It may increase total model calls and token consumption, and findings may conflict or require verification.

When to use it: When bounded delegation or context isolation provides a meaningful benefit.

Do not assume every multi-step coding task needs subagents. A straightforward code change may be easier to complete with a single agent.

4. Hooks: automate lifecycle events

Hooks allow configured actions to run at particular points in Claude Code's lifecycle.

Examples include:

- Running a linter after a file is edited.
- Recording information when a session starts or ends.
- Blocking a prohibited operation before it executes.
- Running a configured validation command at a relevant event.

The defining characteristic is that a hook is associated with a specified event rather than relying solely on Claude to remember an instruction.

Consider a requirement:

> Every time Claude Code attempts to modify a protected configuration file, the operation must be checked against a restriction.



A prompt saying “do not modify this file” provides guidance. A suitably configured enforcement mechanism can provide a technical safeguard.

When to use it: When an action must happen consistently at a defined workflow event.

Hooks can implement important controls, but their effectiveness depends on the actual configuration, event handling, and execution environment. Permissions and other safeguards may also be required.

Official reference: [Claude Code — Hooks](https://code.claude.com/docs/en/hooks?utm_source=chatgpt.com)

5. Permissions: control what Claude Code can do

Permissions govern the tools and operations Claude Code is allowed to use and when approval is required.

For example, a development environment might permit reading source files and running approved tests while requiring additional approval for destructive operations.

This is fundamentally different from giving Claude instructions about what it should do.

Mechanism	Primary responsibility

CLAUDE.md	Persistent instructions and project conventions
Skills	Reusable procedures and knowledge
Subagents	Delegated work and isolated task context
Hooks	Event-triggered actions and checks
Permissions	Controls over tool use and approval


Production principle: Apply least privilege. Give Claude Code only the access necessary for its intended task, and apply stronger controls to sensitive operations.

Official reference: [Claude Code — Permissions](https://code.claude.com/docs/en/permissions?utm_source=chatgpt.com)


---

6. Put the mechanisms together

Consider a team building a payment service. It wants Claude Code to follow architecture conventions, review changes consistently, investigate defects efficiently, and prevent unauthorised operations.

A suitable design could combine these mechanisms:

1. CLAUDE.md: Explain the repository architecture, coding conventions, and required test commands.
2. Skill: Provide a reusable payment-code review checklist.
3. Subagent: Delegate a bounded security review when the change warrants it.
4. Hook: Run a configured validation check at the relevant lifecycle event.
5. Permissions: Restrict access to sensitive tools and require approval where appropriate.

Each mechanism has a distinct responsibility. Combining them is useful when the requirements justify it; configuring every mechanism for every project is unnecessary.

One important distinction: a subagent's findings do not automatically become authoritative, and a successful hook does not prove that the entire change is correct. The workflow still needs appropriate verification.


---

Lesson 12: Assessment

Choose the single best answer for each question. The scenarios are designed to test the differences between mechanisms, not just their definitions.

Question 1 — Repeated instructions

A development team repeatedly asks Claude Code to review API changes against the same detailed checklist. The checklist needs to be reusable across multiple sessions.

What is the best fit?

A. Put the entire checklist in every user prompt.

B. Create a reusable skill containing the review procedure.

C. Create a hook that automatically approves every API change.

D. Create a subagent that permanently stores the checklist in conversation history.

Question 2 — Reliable enforcement

A team has a rule that a particular destructive command must never execute in its development environment.

Which approach provides the strongest enforcement?

A. Add a sentence to CLAUDE.md asking Claude not to execute the command.

B. Ask Claude to confirm that it understands the restriction.

C. Configure appropriate technical restrictions, such as permission rules or a hook that reliably blocks the prohibited operation, and verify that the restriction covers the relevant execution paths.

D. Create a skill explaining why destructive commands are dangerous.

Question 3 — Context isolation

Claude Code must investigate a large repository. The main conversation needs only a concise summary of the investigation, not every intermediate search result.

Which approach is most appropriate?

A. Ask the main agent to include every file in its context.

B. Delegate the bounded investigation to a subagent and have it return relevant findings.

C. Move the entire investigation procedure into CLAUDE.md.

D. Use a hook to summarise every source file before each model request.

Question 4 — Automatic checks

A team requires a configured validation command to run after Claude Code edits a source file.

Which mechanism is the most direct fit?

A. A skill that tells Claude it should remember to run the command.

B. A subagent that periodically checks whether files have changed.

C. A suitably configured hook associated with the relevant file-edit event.

D. A project instruction that describes the command but does not configure any automation.

Question 5 — Selecting mechanisms

A team needs shared project conventions, a reusable release checklist, and restricted access to production-deployment tools.

Which combination best matches those requirements?

A. Use CLAUDE.md for conventions, a skill for the release checklist, and permission controls for deployment access.

B. Use a skill for all three because skills can replace permissions.

C. Use a subagent for conventions, a hook for the checklist, and CLAUDE.md to grant tool access.

D. Use CLAUDE.md for all three because persistent instructions guarantee enforcement.

Question 6 — Avoiding unnecessary complexity

A developer asks Claude Code to make a small, well-defined change to a single function and run its unit tests. There are no special delegation or automation requirements.

What is the most appropriate starting point?

A. Create a coordinator and multiple subagents before inspecting the code.

B. Build a custom skill, several hooks, and an MCP server before making the change.

C. Use a straightforward Claude Code workflow, following existing project instructions and the relevant test process.

D. Give Claude unrestricted permissions so it can complete the task without interruption.


---

Reply with your answers in this format: 1B, 2C, 3B, 4C, 5A, 6C

I will grade your answers, explain the reasoning behind any mistakes, and use the results to determine whether we should proceed to a mixed-domain mock exam or reinforce this domain first.