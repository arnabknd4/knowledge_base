Arnab, we’ll approach this as a structured learning programme for the Claude Certified Architect Foundation exam, with one objective beyond passing: developing the judgement needed to design and operate production-grade systems using Claude.

We will move steadily. Each topic will build on the previous one, and we will not skip foundational concepts simply to cover material faster. We will also stay within the exam scope rather than drifting into unrelated AI or software architecture topics.

### How we will learn

1\. Understand the concept

Learn what a capability does, why it exists, when to use it, and what problem it solves.

2\. Connect it to architecture

Examine component interactions, data flow, failure modes, security boundaries, and design trade-offs where relevant to the exam.

3\. Apply it to a realistic scenario

Work through practical architecture decisions instead of memorising definitions.

4\. Test your understanding

Answer exam-style questions, explain your reasoning, identify misconceptions, and revisit weak areas.

### Our exam roadmap

The current Anthropic Partner Academy page identifies five exam domains. We will allocate study time according to their relative importance.

01

Agentic Architecture & Orchestration

### 27%

02

Claude Code Configuration & Workflows

### 20%

03

Prompt Engineering & Structured Output

### 20%

04

Tool Design & MCP Integration

### 18%

05

Context Management & Reliability

### 15%

Domain weights are from the published certification information.

### Lesson 1 — Think like a Claude architect

Before writing code or configuring an agent, you need to understand the architectural problem you are solving.

A Claude-based system is not necessarily an agent. It may be a single model call, a deterministic workflow containing model calls, or an agent that selects tools and performs multiple steps.

Consider this example: a company wants to build a customer-support assistant that answers questions about orders and can cancel an order when authorised.

There are three possible designs.

Design A

Single model call

The application sends the customer's question to Claude and returns the response. Suitable for explanations, classification, and other tasks that do not require the model to execute external actions.

Design B

Deterministic workflow

Application code retrieves the order, checks its status, applies business rules, and uses Claude to explain the outcome. Suitable when the process and decision sequence are known in advance.

Design C

Agentic workflow

Claude determines which available tools to use, interprets their results, and decides whether another step is necessary. Suitable when the next action depends on intermediate results or the user's request.

The critical architectural principle is this: use the least complex design that satisfies the requirements.

An agent is not automatically better than a deterministic workflow. Additional autonomy introduces more execution paths, opportunities for errors, latency, and cost. Even when Claude chooses the next action, the application must enforce authorisation and business invariants.

For example, Claude may decide that an order should be cancelled, but the application must independently verify that the customer is authorised to cancel it and that the order remains cancellable. A model's decision is not an authorisation boundary.

### Check your understanding

Let's begin with an exam-style question. This is an original practice question, not an official exam item.

QUESTION 1 · ARCHITECTURE SELECTION

An organisation wants a Claude-based system to process employee expense claims. The process is fixed: validate required fields, check the expense policy, calculate the reimbursement limit, and produce a decision report. The application must follow the same sequence for every claim.

Which architecture is the best starting point?

A. A multi-agent architecture in which several agents independently review each claim.

B. A deterministic workflow that uses Claude only where language understanding or generation is needed.

C. A fully autonomous agent that chooses the validation sequence for each claim.

D. A single Claude prompt that handles every step without application-level validation.

Submit answer

### Correct.

A fixed sequence is best represented by a deterministic workflow. Claude can handle unstructured receipt descriptions or generate explanations, while application code enforces required fields, policy rules, calculations, and validation.

Continue lesson

Take your time with this first question. The objective is to understand why one architecture is appropriate, not merely to identify the correct option.

One practical note: the certification syllabus can change. We will use the [official Anthropic Partner Academy certification page](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification?utm_source=chatgpt.com) as our scope reference and keep our lessons tied to its published objectives.
