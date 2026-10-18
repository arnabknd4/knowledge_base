---
title: "AI Master Syllabus, Note Template and AI Prompt"
subtitle: "Companion to master-syllabus. Experienced .NET Lead (12+ years, Kolkata market) to AI-capable .NET Architect, Cloud Architect and AI Governance-ready Architect. Topic IDs 25.01 to 38.04"
---

## PART 1: HOW TO USE THIS DOCUMENT

Purpose: same as master-syllabus. Stop deciding, stop collecting. Part 4 lists every AI topic and concept already chosen for you. Part 2 is the fixed note format. Part 3 is the one-time setup. Part 5 is the AI study order. Part 6 tells you where each AI batch fits against your master-syllabus batches, so you can align the two plans yourself.

How this file relates to master-syllabus:

- This file continues the numbering. Master-syllabus uses IDs 1.01 to 24.03. This file uses 25.01 to 38.04. No ID exists in both files, so the same Project prompt works for both.
- Same topic-line format, same tags, same three-pass method, same gap-list rule, same note size rule. Read Part 1 and Part 2 of master-syllabus for the full rules; only the differences are written here.
- The master-syllabus Part 7 says no AI topics were added because you were not targeting the AI market then. This file is the opt-in AI track. Nothing in master-syllabus is deleted. Part 6 lists the few master lines that this file supersedes.

The loop for each topic is unchanged: take the next two or three IDs from Part 5, send them to your Claude Project chat, skim for errors, paste the notes into the domain Word file, print, recall. Tick the box in Part 4 after you have recalled it once from memory on paper.

Rules that matter more for AI topics:

- AI products, model names, versions, limits, prices and exam outlines change every few weeks. Anything that may have changed is tagged (verify). Check the official page: Microsoft Learn for Azure and Foundry, the AWS documentation and exam guides for AWS, Anthropic documentation and Anthropic Academy for Claude.
- Notes are drafts. A model writing notes about models can be wrong about models. Never paste a version number, limit or price from a note into a resume or a client document without checking the official page.
- Labs that call a paid model API need a spending cap set first (budget alert, quota or key limit) and a clean-up step at the end (delete deployments, indexes and agents).
- A concept that is not in the topic line goes on the gap list (one A4 page per domain, by hand). Once a month, take all gap lists to the AI in one session. Never browse for extra sources.
- Pace: about 6 notes a month. Notes do not replace building. The AI capstone (38.02) is where this track becomes a skill.

Tags used in Part 4 (same as master-syllabus, with these meanings for this file):

- P1, P2, P3, P4: phase inside this AI track. P1 is vocabulary, prompting, tools and first builds. P2 is core build skills (retrieval, agents, evaluation, cloud AI, security, governance basics). P3 is architect depth. P4 is specialist or exam depth.
- R = required. O = optional, write only when a target job asks or after Phase 3.
- E = relevant to an AI certification exam: Microsoft AI-900 or AI-901 and AI-103, AWS AIF-C01 and AIP-C01, Claude Certified Architect Foundations. L = used in real projects.
- K = you probably know most of this from 12 years of work (resilience, gateways, networking, identity). Generate the note, read once, fill only the gaps.
- (verify) = names, versions, limits or dates that change often. Check the official page.

Note size rule: R topics get a FULL note (one printed page). O topics get a SHORT note (half a page).

Scale (honest numbers): see the totals at the end of Part 4. This track alone has 70 required notes, about 12 months at 6 notes a month. Together with the 155 required notes in master-syllabus that is 225 required notes, about three years at 6 notes a month. You do not need all of it to start interviewing for AI-capable architect roles. Phase 1 plus Phase 2 (42 required notes) plus the capstone is the AI core.

Language note: AI job postings mostly name Python. The notes in this file show the .NET way first (Microsoft.Extensions.AI, Microsoft Agent Framework, the C# MCP SDK) and mention Python only where it is the common choice. Python for automation (16.05 in master-syllabus) is the minimum. See the rule in Part 7 for promoting 20.01 to required.

## PART 2: NOTE TEMPLATE (SAME AS MASTER-SYLLABUS VERSION 2, WITH FOUR AI ADDITIONS)

Use the master-syllabus Part 2 template unchanged: the same 11 sections, the same K, R and O depth rules, the same three-pass method. Four additions for AI topics, applied by the prompt in Part 3:

- Section 4 (features and core concepts): for each concept, add the failure mode in one clause (how it goes wrong in production).
- Section 5 (core focus): add one line starting "Risk and evaluation:" that says how you would test it and what could go wrong for users.
- Section 6 (real-world use case): state the risk tier in one word (low, medium or high) and the fallback when the AI part fails.
- Section 10 (mini lab): set a spending cap first. Use local tools, the Azure free tier, the AWS free tier or a small capped API budget. End with a clean-up step.

If you prefer your own AI_Note_Format template for these topics, replace only the "Headings, exactly" line in the Part 3 instructions with its section names. Topic lines and tags work with either format.

## PART 3: ONE-TIME SETUP (REPLACES THE MASTER-SYLLABUS INSTRUCTIONS)

Do this once:

- Open your Claude Project "Long term career goal", open Project instructions, and replace the earlier pasted instructions with the text between the two markers below. It works for both files.
- Make sure both documents are in the Project documents under the names master-syllabus and ai-master-syllabus.
- Daily use is unchanged: send one ID, or up to three IDs (example: 26.03 26.04 28.01). Start a new chat for each batch.

START OF INSTRUCTIONS

You are my senior architect mentor and teacher. I am Arnab, a .NET tech lead with 12 years in legacy .NET Framework (MVC, Entity Framework, SQL Server, jQuery, TypeScript, GitLab CI), moving to modern .NET, Azure and AWS, microservices, AI engineering and then architect roles, in the Kolkata and remote India job market.

When I send one or more topic IDs (example: 1.03 or 28.01), find each topic line in the project document master-syllabus (IDs 1.01 to 24.03) or ai-master-syllabus (IDs 25.01 to 38.04) and write one study note per ID. If an ID is not found, ask me to paste the line. Cover every concept in the topic line and add nothing unrelated.

Depth comes from the tags in the topic line. No K tag means the topic is new to me: plain words first, then the technical meaning, define every term when it first appears, and include the mini lab. K tag means skip the basics and focus on gaps, what changed in modern .NET and cloud, and interview depth. R tag means a FULL note of about 700 words. O tag means a SHORT note of about 300 words with sections 1, 4, 6 and 11 only.

Headings, exactly: 1 What is it (end with one line starting Legacy equivalent:), 2 Why needed, 3 Before you read (two to four prerequisites, one line each), 4 Features and core concepts (each concept: plain meaning, then why it matters), 5 Core focus (exam and interview; for AI topics add a line starting Risk and evaluation:), 6 Real-world use case (include the trade-off, when not to use it, and for AI topics the risk tier and the fallback when the AI part fails), 7 Interview lens (four questions with two-line answers), 8 Common mistakes, 9 Mental model, 10 Mini lab (20 to 40 minutes, exact steps, expected result, clean-up step, local tools, free tier or a capped API budget), 11 Revision summary (five to eight one-line facts). For AWS, Java and AI topics, name the Azure or .NET equivalent of each concept. For AI topics show the .NET way first and mention Python only where it is the common choice.

Style: plain text only, no tables, emojis, bold or decoration. Dash bullets. Short sentences. No introductions or conclusions. Do not invent facts, limits, prices, model names or exam details. AI products change monthly, so write (verify) next to any version, service name, model name, limit or date that may have changed. Include code or commands only if worth memorizing, maximum 6 lines. Separate notes with a line of dashes.

END OF INSTRUCTIONS

## PART 4: AI MASTER SYLLABUS

How to read a line: tick box, topic ID and title, tags, then the concepts to cover. Everything listed is in scope. Anything not listed is out of scope for now.

## D25 AI AND MACHINE LEARNING FUNDAMENTALS

☐ **25.01 AI, ML and data science vocabulary** [P1 R E L] AI vs ML vs deep learning vs generative AI; supervised, unsupervised, self-supervised and reinforcement learning; training vs inference; features and labels; train, validation and test splits; overfitting and underfitting; bias-variance trade-off; data leakage; metrics (accuracy, precision, recall, F1, ROC-AUC, RMSE, confusion matrix); baselines; when not to use ML (rules, SQL, search); ML project lifecycle; build vs buy vs configure

☐ **25.02 Classical ML for architects** [P2 R E L] regression and classification; decision trees, random forest, gradient boosting; clustering; anomaly detection; recommenders; time-series forecasting; feature engineering; pipelines (scikit-learn awareness); ML.NET awareness; AutoML; interpretability (feature importance, SHAP awareness); when classical ML beats an LLM (tabular data, cost, latency, determinism)

☐ **25.03 Deep learning and transformer basics** [P1 R E L] neurons, layers, loss and gradient descent at concept level; embeddings; attention; transformer encoder and decoder; tokens; parameters; pretraining, fine-tuning and alignment (RLHF, preference tuning); scaling and compute; reasoning models (verify); diffusion models awareness; multimodal models; training cost vs inference cost; why models hallucinate

☐ **25.04 Data for AI** [P2 R L] data quality dimensions; labeling and annotation; lineage and provenance; PII in training data and prompts; train-serve skew; data drift vs concept drift; lakehouse and feature store awareness; vector data; synthetic data and its risks; data contracts; ownership and access control for AI data; dataset versioning

☐ **25.05 Math and statistics minimum for architects** [P3 O] vectors, dot product and cosine similarity; probability and distributions; sampling and confidence intervals; correlation vs causation; A/B test basics; statistical significance; entropy and perplexity awareness; reading evaluation charts honestly


## D26 LLM FOUNDATIONS AND PROMPTING

☐ **26.01 LLM mechanics and vocabulary** [P1 R E L] tokens and tokenization; context window; temperature, top-p and top-k; max output tokens; stop sequences; system, user and assistant roles; determinism and seeds; hallucination and grounding; knowledge cutoff; reasoning or thinking modes (verify); multimodal input; streaming; latency (time to first token, tokens per second); input vs output token pricing; prompt caching; batch inference; open-weight vs hosted models; licensing basics

☐ **26.02 Model landscape and selection** [P2 R L] model families and providers (Anthropic Claude, OpenAI, Google Gemini, Meta Llama, Mistral and others; verify current lineup); large vs small models; the cost, latency and quality triangle; benchmarks and their limits; model cards; availability by platform (Foundry, Bedrock, Vertex; verify); data residency; routing and cascading; model lifecycle and deprecation; vendor lock-in; evaluating candidates on your own data

☐ **26.03 Prompt engineering** [P1 R E L] structure (role, task, context, constraints, output format); clear and direct instructions; few-shot examples; delimiters and XML tags; reasoning guidance; decomposition and prompt chaining; system prompt design; templating; positive vs negative instructions; prompt versioning and review; prompt injection awareness; differences between models; common failure patterns

☐ **26.04 Structured output and tool calling** [P1 R E L] JSON-schema-constrained output; the function and tool calling flow; parallel tool calls; schema design; validation and retry loops; error results from tools; refusals and partial output; mapping to .NET types and System.Text.Json schemas; idempotent tool design; batch processing of structured extraction; output repair

☐ **26.05 Context engineering and memory** [P2 R E L] context budgeting; context rot and long-context limits; ordering and placement of information; summarization and compaction; retrieval vs stuffing; prompt caching strategy; conversation state storage; long-term memory stores; scratchpads and notes files; context isolation with subagents; token counting; cost and latency effects

☐ **26.06 Fine-tuning and model adaptation** [P3 O E] prompting vs RAG vs fine-tuning decision; supervised fine-tuning; parameter-efficient methods (LoRA awareness); distillation; preference tuning awareness; dataset requirements and quality; evaluating before and after; hosted fine-tuning on Foundry and Bedrock (verify); cost and maintenance burden; when fine-tuning is the wrong answer

☐ **26.07 Multimodal, speech and vision** [P4 O] image and document understanding; OCR and layout analysis; speech to text and text to speech; real-time voice APIs; image generation awareness; video awareness; accessibility uses; cost and latency differences


## D27 RETRIEVAL AND KNOWLEDGE SYSTEMS (RAG)

☐ **27.01 Embeddings and vector search** [P2 R E L] what embeddings represent; dimensions and embedding models; similarity measures (cosine, dot product, Euclidean); approximate nearest neighbour (HNSW, IVF, DiskANN awareness); vector stores (Azure AI Search, Azure Cosmos DB, PostgreSQL pgvector, OpenSearch, Redis; verify); hybrid search (keyword plus vector); reranking; metadata filters; index size and cost; embedding model versioning and re-embedding

☐ **27.02 RAG pipeline design** [P2 R E L] ingestion (parse, clean, chunk); chunking strategies and overlap; metadata design; retrieval; query rewriting; reranking; context assembly; citations and grounding; freshness and incremental indexing; security trimming by user permissions; multi-tenant isolation; failure modes (missed retrieval, wrong chunk, stale data, over-trust); when RAG is not needed

☐ **27.03 Advanced retrieval and knowledge graphs** [P3 O] agentic and multi-hop retrieval; GraphRAG and knowledge graphs; text-to-SQL and structured data; long context vs RAG; retrieval caching; query routing; evaluation of retrieval quality; multimodal retrieval


## D28 AGENTS AND AGENTIC ARCHITECTURE

☐ **28.01 Agent fundamentals** [P1 R E L] workflow vs agent; the agentic loop (reason, act, observe); stop conditions; tool use; planning and reflection; autonomy levels; when to use an agent and when a deterministic workflow is better; cost, latency and reliability trade-offs; typical enterprise agent use cases; failure modes

☐ **28.02 Workflow patterns** [P2 R E L] prompt chaining; routing; parallelization; orchestrator and workers; evaluator and optimizer; state machines; durable execution (Durable Functions, Step Functions, Temporal awareness); human-in-the-loop approval; checkpoint and resume; idempotency; timeouts

☐ **28.03 Multi-agent orchestration** [P2 R E L] coordinator and subagent pattern; handoffs; shared vs isolated context; task decomposition; parallel subagents; result aggregation; error propagation across agents; loop guards and budgets; hooks; agent-to-agent protocol awareness; when multi-agent is the wrong choice

☐ **28.04 Agent reliability and escalation** [P3 R E L] guardrails and validation; retries and fallbacks; step, token and cost budgets; escalation to humans; confidence and abstention; deterministic fallbacks; state persistence and replay; handling tool failures; observability of agent runs; preventing context loss in long runs; reliability testing

☐ **28.05 Agent frameworks and SDKs** [P2 R L] Microsoft.Extensions.AI abstractions; Microsoft Agent Framework 1.0 (reported GA in April 2026; verify); Semantic Kernel in maintenance mode and migration (verify); AutoGen lineage; LangGraph; Claude Agent SDK; OpenAI Agents SDK awareness; Foundry Agent Service; Amazon Bedrock AgentCore and Strands awareness (verify); framework selection criteria; avoiding lock-in

☐ **28.06 Coding agents and AI-assisted engineering** [P1 R E L] using coding agents safely (supersedes 15.08 in master-syllabus); Claude Code and GitHub Copilot agent modes; instruction files (CLAUDE.md, Copilot instructions); plan mode vs direct execution; reviewing generated code; test-first with agents; permission and sandbox settings; secrets and repository-access risks; CI use; cost control; team policies; measuring productivity honestly


## D29 TOOLS, MCP AND INTEGRATION

☐ **29.01 Tool design** [P1 R E L] tool names and descriptions a model can choose between reliably; input schemas; granularity; side effects and confirmation; idempotency; structured error responses; result size and pagination; least-privilege scopes; number of tools and selection accuracy; testing tools in isolation

☐ **29.02 Model Context Protocol** [P1 R E L] host, client and server roles; primitives (tools, resources, prompts); transports (stdio, streamable HTTP); capability negotiation; sampling, roots and elicitation; authorization (OAuth-based; verify); configuration scopes (project vs user); registries; versioning and spec changes (verify); security considerations

☐ **29.03 Building MCP servers and clients in .NET** [P2 R L] C# MCP SDK (verify); ASP.NET Core hosting; stdio vs HTTP; wrapping existing REST APIs; Entra ID authentication; testing with an inspector; deployment on Container Apps or AKS; observability; versioning; API Management in front of MCP servers (verify)

☐ **29.04 Agent interoperability protocols** [P4 O] Agent2Agent (A2A) awareness; OpenAPI-to-tool conversion; agent UI protocol awareness; computer-use and browser agents; agent registries; standards governance (verify)

☐ **29.05 Integrating AI into enterprise systems** [P3 R L K] AI behind existing APIs; async job pattern for long LLM calls; queue-based inference; 429 and quota handling; retries with jitter; circuit breaker for model endpoints; AI gateway (token limits, load balancing across deployments, semantic caching); multi-region failover; streaming through gateways (server-sent events); webhooks and callbacks


## D30 EVALUATION AND QUALITY

☐ **30.01 Evaluation fundamentals** [P2 R E L] why evals come before features; golden datasets; offline vs online evaluation; metrics (exact match, F1, groundedness, relevance, faithfulness, toxicity); LLM-as-judge and its biases; human review; non-determinism and sample size; regression suites in CI; eval-driven development

☐ **30.02 RAG and agent evaluation** [P3 R E L] retrieval metrics (recall at k, MRR, nDCG); answer faithfulness and citation accuracy; tool-call accuracy; trajectory evaluation; task success rate; cost and latency per task; Foundry evaluators, Ragas and promptfoo awareness (verify); building a dataset from production logs

☐ **30.03 Testing AI applications in .NET** [P3 R L] Microsoft.Extensions.AI.Evaluation (verify); fakes and record-replay for model responses; contract tests on tool schemas; snapshot tests; CI quality gates; canary prompts; shadow traffic; A/B testing of prompts and models

☐ **30.04 Safety and adversarial testing** [P3 R E L] red-teaming method; prompt-injection and jailbreak test sets; PyRIT awareness; content-safety evaluation; bias and fairness testing; abuse monitoring; release criteria for AI features


## D31 AI ON AZURE (MICROSOFT FOUNDRY)

☐ **31.01 Microsoft Foundry platform** [P2 R E L] Foundry resources and projects (formerly Azure AI Foundry; verify current naming); model catalog; deployment types (standard, global, provisioned throughput, batch); quotas and tokens per minute; regions and model availability; Azure OpenAI vs Foundry Models; authentication (Entra ID and managed identity vs keys); SDKs; cost levers

☐ **31.02 Azure AI Search and RAG on Azure** [P2 R E L] index design; vector and hybrid search; semantic ranker; integrated vectorization; indexers and skillsets; security trimming; agentic retrieval (verify); private endpoints; replicas and partitions; cost; alternatives (Cosmos DB vector, pgvector, Azure SQL vector; verify)

☐ **31.03 Foundry Agent Service** [P3 R E L] agents and tools; built-in tools (file search, code interpreter, Azure AI Search, web grounding, MCP; verify); connected agents; threads and runs concepts (verify current API); identity and permissions; tracing; publishing and versioning

☐ **31.04 Azure AI services** [P3 R E] Document Intelligence; Language; Vision; Speech; Translator; Content Safety (prompt shields, groundedness detection); prebuilt service vs LLM decision; typical fundamentals-exam scenarios

☐ **31.05 .NET AI development on Azure** [P2 R L] Microsoft.Extensions.AI (IChatClient, IEmbeddingGenerator, middleware for caching, telemetry and function invocation); Azure OpenAI and OpenAI .NET SDKs; DI registration; streaming; structured output; function calling; resilience for 429; token counting; Aspire AI integrations awareness (verify)

☐ **31.06 Azure AI gateway, networking and operations** [P3 R E L K] API Management AI gateway policies (token limits, token metrics, semantic cache, backend pools); private endpoints; RBAC roles for model access; Key Vault; diagnostic logs; Application Insights generative AI tracing; quota management; tagging and cost management; landing zone for AI awareness

☐ **31.07 Azure Machine Learning and MLOps** [P4 O E] workspace, jobs and endpoints (managed online and batch); model registry; pipelines; MLflow; feature store awareness; responsible AI dashboard awareness; AI-300 awareness (verify)

☐ **31.08 AI fundamentals exam blueprint (AI-900 or AI-901)** [P1 R E] check which fundamentals exam is current (verify); domains as currently published; AI workloads and considerations; ML principles; vision, language, speech and generative AI workloads; responsible AI principles; labs; practice assessments

☐ **31.09 AI-103 blueprint and strategy** [P3 R E] Azure AI App and Agent Developer Associate, which replaces AI-102 (reported AI-102 retirement 30 June 2026; verify date and skills outline); prerequisites; domains as currently published; labs per domain; practice assessments; renewal

☐ **31.10 Other Microsoft AI and data blueprints** [P4 O E] AI-200 Azure AI Cloud Developer Associate; AI-300 MLOps Engineer Associate; DP-800 SQL AI Developer Associate; SC-500 Cloud and AI Security Engineer Associate (all verify status, dates and skills outlines)


## D32 AI ON AWS

☐ **32.01 Amazon Bedrock core** [P2 R E L] model access and catalog; Converse API vs InvokeModel; on-demand, provisioned throughput and batch (verify); cross-region inference; pricing and quotas; IAM permissions; VPC endpoints; invocation logging; streaming; mapping to Foundry concepts

☐ **32.02 Bedrock Knowledge Bases and RAG on AWS** [P3 R E L] knowledge bases; data sources; chunking options; vector stores (OpenSearch Serverless, Aurora pgvector, S3 vectors; verify); retrieval APIs; reranking; metadata filtering; guardrail integration; structured data retrieval; mapping to Azure AI Search

☐ **32.03 Bedrock Agents and AgentCore** [P3 R E L] agents and action groups; Lambda tools; attaching knowledge bases; multi-agent collaboration; AgentCore runtime, memory, gateway, identity and observability (verify); Strands Agents SDK awareness (verify); MCP on AWS awareness; mapping to Foundry Agent Service

☐ **32.04 Bedrock Guardrails and AI safety on AWS** [P3 R E L] content filters; denied topics; word filters; sensitive information filters (PII); contextual grounding checks; prompt-attack filter; automated reasoning checks (verify); ApplyGuardrail API; model evaluation; mapping to Azure Content Safety

☐ **32.05 SageMaker AI and ML on AWS** [P4 O E] SageMaker studio, training jobs, endpoints, pipelines and model registry; JumpStart; Model Monitor; Clarify; MLOps practices; MLA-C01 awareness (verify)

☐ **32.06 AWS AI services** [P3 R E] Textract; Comprehend; Rekognition; Transcribe; Polly; Translate; Lex; Kendra; Amazon Q awareness (verify naming); prebuilt service vs LLM decision

☐ **32.07 .NET and generative AI on AWS** [P3 R L] AWS SDK for .NET with the Bedrock runtime; Microsoft.Extensions.AI with Bedrock (verify package); Lambda with .NET calling Bedrock; API Gateway and streaming; Step Functions orchestrating model calls; IAM roles and secrets; comparison with 31.05

☐ **32.08 AWS AI Practitioner blueprint (AIF-C01)** [P2 R E] domains as currently published (reported weights: AI and ML fundamentals 20%, generative AI fundamentals 24%, applications of foundation models 28%, responsible AI 14%, security, compliance and governance 14%; verify against the current exam guide); format and passing score (verify); labs; practice assessments

☐ **32.09 AWS Generative AI Developer Professional blueprint (AIP-C01)** [P4 R E] domains as published by AWS (foundation model integration, data management and compliance 31%; implementation and integration 26%; AI safety, security and governance 20%; operational efficiency and optimization 12%; testing, validation and troubleshooting 11%; verify); recommended experience; format and passing score (verify); labs; practice assessments


## D33 CLAUDE AND ANTHROPIC PLATFORM

☐ **33.01 Claude API essentials** [P1 R E L] Messages API; system prompts; content blocks; streaming; the tool use loop; stop reasons; token counting; prompt caching; batch processing; extended thinking (verify); files and citations awareness; rate limits and retries; model selection (verify lineup); Claude on Bedrock, Foundry and Vertex availability (verify); .NET access options (verify)

☐ **33.02 Claude Agent SDK and agentic loops** [P2 R E L] the agent loop in the SDK; subagents; hooks; permission modes; sessions; MCP integration; custom tools; deployment patterns; cost controls; failure handling

☐ **33.03 Claude Code configuration and workflows** [P1 R E L] CLAUDE.md hierarchy (user, project, directory); settings scopes; skills and slash commands; subagents; hooks; plan mode vs direct execution; permission modes; MCP configuration scopes; headless use in CI; GitHub integration; team conventions (verify current features)

☐ **33.04 Claude Certified Architect Foundations blueprint** [P3 R E] domains and weights (agentic architecture and orchestration 27%; Claude Code configuration and workflows 20%; prompt engineering and structured output 20%; tool design and MCP integration 18%; context management and reliability 15%); 60 scenario-based questions in 120 minutes, passing score 720 of 1000 (verify); six scenario types; prerequisites; build-a-small-agent practice plan; map of each domain to topics in this file (Part 7)

☐ **33.05 Provider comparison and portability** [P3 R L] differences between providers in tool calling, structured output, caching and limits; abstraction through Microsoft.Extensions.AI; LiteLLM-style gateways awareness; portability tests; fallback providers; vendor risk; contract and data-use terms awareness


## D34 LLMOPS, PLATFORM AND OPERATIONS

☐ **34.01 LLMOps lifecycle** [P2 R L] prompt and configuration as code; model version pinning; release strategies (canary, shadow, A/B); evaluation gates in CI/CD; rollback; feature flags for AI features; dataset versioning; environments with separate quotas; handling model deprecations

☐ **34.02 Observability for AI** [P2 R E L] generative AI tracing and OpenTelemetry GenAI conventions (verify); spans for model calls, tools and retrieval; token and cost metrics; latency (time to first token); quality signals and user feedback; prompt and response logging with redaction; sampling; drift detection; alerting; tooling awareness (Application Insights, Foundry tracing, Langfuse)

☐ **34.03 Cost, latency and capacity** [P2 R L] token economics; prompt, semantic and response caching; model routing and cascading; batching; truncation and summarization; streaming for user experience; provisioned throughput vs pay-as-you-go; quota planning; per-tenant and per-user rate limits; budgets and kill switches; unit cost per task; FinOps for AI (links to 12.12)

☐ **34.04 Inference and self-hosting** [P4 O] self-hosting open-weight models (vLLM, Ollama, TGI awareness); GPU basics (memory, quantization, batching); GPU node pools on AKS; KServe awareness; ONNX Runtime and local inference from .NET (verify); small language models; edge deployment; when self-hosting beats an API

☐ **34.05 AI platform engineering** [P3 R L] reference architecture for an enterprise AI platform: gateway, prompt registry, evaluation service, vector store service, guardrail service, model catalog governance; golden paths; multi-tenancy; chargeback; landing zone for AI; centre of excellence (links to 9.06)

☐ **34.06 MLOps essentials** [P4 O E] MLflow; model registry; CI/CD for models; drift monitoring and retraining triggers; feature store; batch vs online inference; shadow deployment; mapping Azure ML to SageMaker


## D35 AI SECURITY AND SAFETY

☐ **35.01 LLM application threats** [P2 R E L] OWASP Top 10 for LLM applications (verify current version); direct and indirect prompt injection; jailbreaks; sensitive information disclosure; insecure output handling; excessive agency; supply chain (models, plugins, MCP servers); system prompt leakage; vector and embedding weaknesses; denial of wallet; MITRE ATLAS awareness

☐ **35.02 Agent and tool security** [P2 R E L] least privilege for tools; identity for agents (managed identity, on-behalf-of, scoped tokens); confused deputy; human approval gates; sandboxing code execution; network egress control; no secrets in prompts; MCP server trust and authentication; tool poisoning; the risk of combining private data, untrusted input and outbound channels; audit trails; kill switch

☐ **35.03 Guardrails and content safety** [P3 R E L] input and output filtering; Azure AI Content Safety (prompt shields, groundedness); Bedrock Guardrails; PII detection and redaction; topic restrictions; refusal design; layered defense; latency cost; false positives; jailbreak monitoring

☐ **35.04 Data protection for AI** [P3 R E L] data classification before prompting; PII handling; tenant isolation in RAG (security trimming, per-tenant indexes); retention and zero-data-retention terms; provider data-use terms; residency; logging with redaction; encryption; right to erasure in vector stores and logs; DPDP Act mapping (links to 14.07; verify)

☐ **35.05 AI red teaming and incident response** [P4 O] AI incident taxonomy; response runbook; rollback and disablement; disclosure; bug bounty awareness; PyRIT and garak awareness; links to 30.04


## D36 RESPONSIBLE AI, GOVERNANCE AND ASSURANCE

☐ **36.01 Responsible AI principles and practice** [P1 R E L] fairness, reliability and safety, privacy and security, inclusiveness, transparency, accountability (Microsoft principles); AWS responsible AI dimensions awareness (verify); harms taxonomy; human oversight; model cards and system cards; impact assessment; explainability awareness; bias measurement; user disclosure of AI use

☐ **36.02 NIST AI Risk Management Framework** [P2 R E L] Govern, Map, Measure and Manage functions; trustworthiness characteristics; the Generative AI Profile (NIST AI 600-1; verify); playbook use; mapping to the SDLC; AI risk register; mapping to cloud governance and Well-Architected reviews

☐ **36.03 ISO/IEC 42001 and related standards** [P2 R E L] AI management system structure and clauses; Annex A controls; plan-do-check-act; certification process; ISO/IEC 23894 AI risk management; ISO/IEC 22989 terminology awareness; integration with ISO 27001; AI policy and roles; audit evidence

☐ **36.04 EU AI Act** [P2 R E L] risk tiers (unacceptable, high, limited, minimal); general-purpose AI obligations; provider vs deployer; high-risk requirements (risk management, data governance, technical documentation, logging, transparency, human oversight, accuracy and robustness); conformity assessment; timelines and any amendments (verify); penalties; reach over non-EU delivery teams

☐ **36.05 India and other regulation** [P3 R L] India AI governance guidelines (verify current); DPDP Act and Rules (verify); MeitY advisories (verify); sector regulators such as RBI and SEBI (verify); US state laws, UK, Singapore and OECD principles awareness; copyright and IP in training data and outputs awareness; contract clauses for AI vendors

☐ **36.06 AI governance operating model** [P3 R L] AI policy; use-case intake and risk tiering; AI inventory; approval gates (design, pre-production, post-release); roles (AI council, product owner, risk, legal); third-party AI risk and vendor assessment; monitoring and audit; incident reporting; training and awareness; shadow AI; mapping AWS Well-Architected generative AI guidance and cloud adoption frameworks to NIST AI RMF, ISO 42001 and the EU AI Act

☐ **36.07 AI assurance and audit** [P3 R L] assurance engagement structure; control design and testing; evidence collection; independent validation; model risk management awareness; SOC 2 and ISO audits with AI in scope; readiness assessments and maturity models; consulting deliverables (gap assessment, control mapping, policy pack, roadmap); reporting findings to leadership


## D37 AI ARCHITECTURE AND SOLUTION DESIGN

☐ **37.01 AI solution architecture patterns** [P2 R L] reference architectures (chat with enterprise data, document processing, embedded copilot, agentic workflow automation, classification and extraction at scale, summarization, code assistance); choosing between LLM, classical ML and rules; AI non-functional requirements (quality, latency, cost, safety, explainability, auditability); capability maps; build vs buy vs configure

☐ **37.02 Designing AI features into .NET and microservice systems** [P2 R L] AI as a separate service with a contract; anti-corruption layer around model providers; async patterns; outbox with AI jobs; idempotency and non-determinism; caching; non-AI fallback paths; prompts as versioned configuration; multi-tenancy; UX patterns (streaming, citations, feedback, undo); human-in-the-loop interfaces (links to 9.x, 6.x, 3.04)

☐ **37.03 AI system design practice** [P3 R L] enterprise chatbot with RAG and security trimming; support-ticket triage agent; document extraction at scale; code-review bot in CI; contract analysis; claims processing; multi-tenant knowledge assistant; text-to-SQL analytics assistant. Method each time: requirements and risk tier, architecture, evaluation plan, safety, cost estimate, rollout

☐ **37.04 AI decisions, estimation and business case** [P3 R L] ADRs for model choice and RAG vs fine-tuning; cost model (tokens times volume); ROI and business case; the pilot-to-production gap; success metrics; proof-of-concept design with exit criteria; AI risk register; vendor evaluation; stakeholder communication (links to 15.02, 15.05)

☐ **37.05 Data and knowledge architecture for AI** [P3 R L] lakehouse for AI; data products; metadata catalog and lineage (Purview awareness); vector store strategy; knowledge freshness; master data; ownership; access-control propagation; synthetic data; data contracts; Fabric awareness (verify)

☐ **37.06 Emerging AI architecture topics** [P4 O] long-running agents; agent identity; memory architectures; voice agents; computer-use agents; on-device models; AI-native application patterns; reasoning-model cost behaviour (verify)


## D38 AI CAREER, CAPSTONE AND INTERVIEW TOOLKIT

☐ **38.01 AI career positioning** [P1 R L] role map (AI engineer, generative AI solutions architect, agentic AI engineer, MLOps engineer, AI governance and risk consultant, AI assurance); the AI market check routine (Part 7); skills gap log; positioning as .NET plus AI architect; honest description of lab vs production work

☐ **38.02 AI capstone project** [P2 R L] scope: a .NET enterprise assistant with retrieval on Azure AI Search, tool calls to internal APIs through a C# MCP server, an agent workflow with human approval, evaluations in CI, guardrails, tracing and a cost dashboard, plus a governance pack (risk tier, model card, NIST AI RMF mapping, threat model); milestones; README; ADRs; postmortem (links to 17.02)

☐ **38.03 AI interview preparation map** [P3 R L] rounds (LLM fundamentals, RAG design, agent design, evaluation, security, governance, AI system design, cost, behavioural with AI stories); question bank per domain; mock interview schedule; AI story bank (extends 17.01)

☐ **38.04 AI stakeholder communication** [P3 R L] explaining AI limits to executives; setting expectations on hallucination and accuracy; ROI storytelling; adoption and change management; client discovery workshops; team AI-use policy; responsible disclosure to customers


TOTALS: 82 topics. 70 are required (full notes, about 70 printed pages) and 12 are optional (short notes, about 6 pages). Required by phase: Phase 1 has 14, Phase 2 has 28, Phase 3 has 27, Phase 4 has 1. Optional by phase: 0 in Phase 1, 0 in Phase 2, 3 in Phase 3, 9 in Phase 4. Printed total is about 76 pages, roughly 38 sheets printed on both sides.

## PART 5: STUDY ORDER (BATCHES OF ABOUT 8 NOTES)

Work in this order inside the AI track. Part 6 shows where each batch fits against master-syllabus. Start the AI capstone (38.02) when you reach AI-B6 and build what each later batch teaches inside it.

Phase 1 (vocabulary, prompting, tools, first builds):

- Batch AI-B1: 25.01, 25.03, 26.01, 26.03, 26.04, 33.01, 36.01, 31.08
- Batch AI-B2: 28.01, 28.06, 29.01, 29.02, 33.03, 38.01

Phase 2 (core build skills):

- Batch AI-B3 (retrieval on Azure): 25.04, 26.02, 26.05, 27.01, 27.02, 31.01, 31.02, 31.05
- Batch AI-B4 (agents and tools in code): 25.02, 28.02, 28.03, 28.05, 29.03, 33.02, 30.01
- Batch AI-B5 (AWS, operations, security): 32.01, 32.08, 34.01, 34.02, 34.03, 35.01, 35.02, 37.01
- Batch AI-B6 (governance and design, capstone start): 36.02, 36.03, 36.04, 37.02, 38.02

Phase 3 (AI architect):

- Batch AI-B7 (reliability, evaluation, protection): 28.04, 29.05, 30.02, 30.03, 30.04, 35.03, 35.04
- Batch AI-B8 (Azure depth and AI-103): 31.03, 31.04, 31.06, 31.09, 34.05
- Batch AI-B9 (AWS depth): 32.02, 32.03, 32.04, 32.06, 32.07, 33.05
- Batch AI-B10 (governance, assurance, design practice, Claude exam): 33.04, 36.05, 36.06, 36.07, 37.03, 37.04, 37.05, 38.03, 38.04

Phase 4 (certification depth):

- Batch AI-B11: 32.09

Optional notes (write only when a target job asks, or after Batch AI-B10): 25.05, 26.06, 26.07, 27.03, 29.04, 31.07, 31.10, 32.05, 34.04, 34.06, 35.05, 37.06.

Fast-pass reminder: topics tagged K (29.05, 31.06) should take about one hour each. Generate, read once, mark the gaps.

## PART 6: ALIGNMENT WITH MASTER-SYLLABUS

Earliest start for each AI batch (all master topics listed must already be noted and recalled):

- AI-B1: no prerequisites. Can start at any time.
- AI-B2: after master Batch 3 (needs 7.01, 7.02, 16.01).
- AI-B3: after master Batch 5 (needs 12.01 to 12.07, 5.01 to 5.03, 3.03).
- AI-B4: after master Batch 8 (needs 3.04, 3.05, 6.01 to 6.04).
- AI-B5: after master Batches 6A and 10 (needs 22.01 to 22.05, 13.01 to 13.03, 14.01 to 14.03, 12.08, 12.12).
- AI-B6: after master Batch 13 (needs 15.02, 15.05, 14.01, 9.01 to 9.06).
- AI-B7: after master Batch 16 (needs 9.07, 13.05, 13.06, 14.04 to 14.07).
- AI-B8: after master Batch 15 (needs 12.10, 12.11, 9.06).
- AI-B9: after master Batch 15A (needs 22.06 to 22.11).
- AI-B10: after master Batch 16 (needs 14.04, 14.07, 15.03, 15.06).
- AI-B11: after master Batch 17A (needs 22.13).

One possible interleave that respects all of the above (change it freely):

- Master Batches 1 to 6, then AI-B1.
- Master Batches 6A and 7, then AI-B2.
- Master Batch 8, then AI-B3.
- Master Batches 9 and 10, then AI-B4.
- Master Batches 11, 12 and 13, then AI-B5 and AI-B6.
- Master Batches 14, 14A, 15 and 15A, then AI-B8 and AI-B9.
- Master Batch 16, then AI-B7 and AI-B10.
- Master Batches 17 and 17A, then AI-B11.

Lines in master-syllabus that this file supersedes or extends (apply when you start the AI track; nothing else in master-syllabus changes):

- 15.08 AI-assisted engineering: superseded by 28.06. Keep or delete the master line.
- 12.18 mentions AI-200 as an optional blueprint: covered by 31.09 and 31.10.
- 17.01 story bank: AI stories are added in 38.03.
- 17.03 resume keywords: add Foundry, Bedrock, RAG, MCP, agents and evals only after the matching notes and the capstone are done.
- 24.03 market tracking routine: the AI queries in Part 7 are added to the same quarterly 30-minute check.
- 16.05 Python for automation stays required. 20.01 Python backend stays optional unless the rule in Part 7 applies.
- Master Part 3 instructions: replaced once by the Part 3 text in this file.

## PART 7: MARKET BASIS, CERTIFICATION MAPS AND RE-CHECK ROUTINE

Market check date: 18 October 2026. Data quality warning: I found no reliable Kolkata-only AI job counts. The figures below are India-wide and come from HR and recruiter reports, so treat them as direction only.

What the check found:

- A CIEL HR report (reported by Outlook Business on 8 September 2026, covering March 2024 to May 2026 postings) puts India demand growth for agentic AI engineers at 260% year on year, generative AI solutions architects at 120%, AI product owners at 120%, LLM engineers at 86.5% and MLOps engineers at 82.2%. Growth rates from a small base look large; the report also names generative AI, cloud, cybersecurity and data engineering as priority skills and puts market skill gaps at 38% to 61%.
- Earlier hiring reports (Quess, Taggd, Adecco) said AI, cloud and cybersecurity carry the salary and hiring premium in 2026, and one named AI governance as a premium area. That is why D36 is a full domain.
- The same reports say hiring is concentrated in Tier-1 cities and global capability centres. Kolkata has fewer postings, so the remote and GCC routes matter for AI roles.
- Tooling reported by one developer blog: Microsoft Agent Framework 1.0 reached general availability on 3 April 2026, and Semantic Kernel is in maintenance mode. Verify on Microsoft Learn before building the capstone on either.
- Certifications: one source reports AI-102 retired on 30 June 2026 and was replaced by AI-103 (Azure AI App and Agent Developer Associate), with AI-200, AI-300, DP-800 and SC-500 planned for 2026 (planned dates, not confirmed). AWS publishes AIP-C01 domain weights. Anthropic publishes the Claude Certified Architect Foundations exam. All exam facts are tagged (verify).

Certification maps (which topics prepare which exam; check each official outline once):

- Claude Certified Architect Foundations: agentic architecture and orchestration (27%) is 28.01, 28.02, 28.03, 28.04, 28.05 and 33.02. Claude Code configuration and workflows (20%) is 28.06 and 33.03. Prompt engineering and structured output (20%) is 26.03 and 26.04. Tool design and MCP integration (18%) is 29.01, 29.02 and 29.03. Context management and reliability (15%) is 26.05 and 28.04. Blueprint and strategy note: 33.04.
- AWS AIF-C01: AI and ML fundamentals is 25.01 to 25.04. Generative AI fundamentals is 25.03 and 26.01. Applications of foundation models is 26.02 to 26.05, 27.01, 27.02 and 32.01. Responsible AI is 36.01. Security, compliance and governance is 35.01, 36.02 to 36.04. Blueprint note: 32.08.
- AWS AIP-C01: foundation model integration, data management and compliance is 32.01, 32.02, 27.01, 27.02 and 35.04. Implementation and integration is 32.03, 32.07, 29.05 and 28.x. AI safety, security and governance is 32.04, 35.x and 36.x. Operational efficiency is 34.03. Testing, validation and troubleshooting is 30.x and 34.02. Blueprint note: 32.09.
- Microsoft AI-900 or AI-901: 25.01, 25.03, 26.01, 31.04, 36.01. Blueprint note: 31.08.
- Microsoft AI-103: 31.01 to 31.06, 27.x, 28.x, 30.x, 35.03. Skills outline not verified; blueprint note: 31.09.

Quarterly AI market check (30 minutes, add to the 24.03 routine):

- Sites: Naukri, LinkedIn Jobs, Indeed. Location Kolkata, then Remote India. Experience filter 10 to 15 years. Record the date.
- Searches: "generative AI solution architect", "AI architect", "agentic AI engineer", "LLM engineer", "MLOps engineer", "AI governance", "responsible AI consultant", "AI assurance", "AI platform engineer".
- For each: result count, then read the top 20 postings and tally must-haves: language (Python vs C# vs Java), cloud (Azure vs AWS vs GCP), frameworks (LangChain, LangGraph, Semantic Kernel, Agent Framework), vector stores, certification asks, employer type (service firm, GCC, product, assurance or consulting firm).
- Compare ratios between queries, not absolute counts. Log one table per quarter: date, query, count, must-have tally, notes.

Rules for changing the plan (apply from your own numbers):

- Python is a must-have in more than half of the top 20 postings for your target roles: promote 20.01 to required and move it before AI-B4.
- Governance, assurance or risk roles dominate the postings you want: move 36.05 to 36.07 into Phase 2 and add 36.02 to 36.04 to AI-B2.
- AWS is a must-have more often than Azure by more than 2 times: move 32.02 to 32.04 and 32.07 into Phase 2.
- Postings ask for fine-tuning or self-hosting regularly: promote 26.06 and 34.04 to required Phase 3.

Sources used:

- CIEL HR report coverage, Outlook Business: https://www.outlookbusiness.com/news/demand-for-agentic-ai-talent-rises-260-as-enterprises-embrace-ai-report
- Quess hiring report coverage: https://oga-prod.angelone.in/news/economy/india-s-it-job-market-grows-by-16-in-2025-quess-corp
- Taggd IT hiring trends: https://taggd.in/blogs/it-hiring-trends/
- AWS AIP-C01 exam page: https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html
- AWS AIF-C01 guide summary (page last updated October 2024): https://tutorialsdojo.com/aws-certified-ai-practitioner-aif-c01-exam-guide/
- Microsoft AI certification changes (secondary source): https://www.whizlabs.com/blog/microsofts-next-generation-ai-certifications/
- Microsoft Agent Framework vs Semantic Kernel (developer blog): https://startdebugging.net/2026/06/microsoft-agent-framework-vs-semantic-kernel-for-a-greenfield-net-agent/
- Claude Certified Architect Foundations summary (secondary source): https://www.cloudthat.com/resources/blog/inside-claude-certified-architect-foundations-what-anthropics-new-exam-actually-measures

## PART 8: PRINT SETTINGS

Same as master-syllabus Part 6 (Word narrow margins, Arial or Calibri 10 pt, print both sides in black and white, no two pages per sheet, binder section per domain, handwritten recall boxes, e-ink PDF option). One Word file per domain: D25-ai-ml-fundamentals, D26-llm-prompting, D27-retrieval-rag, D28-agents, D29-tools-mcp, D30-evaluation, D31-ai-azure, D32-ai-aws, D33-claude-anthropic, D34-llmops, D35-ai-security, D36-responsible-ai-governance, D37-ai-architecture, D38-ai-career.
