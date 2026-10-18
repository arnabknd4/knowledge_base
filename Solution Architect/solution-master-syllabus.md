---
title: "Solution Architect Supplement (companion to master-syllabus)"
subtitle: "Experienced .NET Lead (12+ years, Kolkata market) to Solution Architect. Topic IDs 59.01 to 59.06"
---

## PART 1: AUDIT RESULT AND HOW THIS FILE FITS

Verdict: the solution architect path is already about 90% covered. It is the hub between the lead role and both the cloud and enterprise paths, so most of its skills sit in files you already have. This file is deliberately small: 6 topics, a route through the older files, a batch order, and a certification sequence.

Where the solution architect job is already covered (do not duplicate):

- Requirements and business analysis: leadership 54.03, master 11.01.
- Documentation and decisions: 15.01 (ADRs, C4), 15.02 (trade-offs), 53.02 (decision process), cloud 58.01 (deliverables).
- Integration and packaged applications: ea 41.01, 41.02, 41.03.
- Presales, RFPs and estimates: leadership 54.04, 52.01, 54.05, 54.06, ea 44.04.
- Architecture styles, microservices, data and security design: D09, D10, D04, D14 (14.04 threat modeling).
- Migration and modernization: 9.03, 12.09, 53.06, cloud 58.06.
- Stakeholders, client skills and communication: 54.01, 54.02, 55.01 to 55.05.
- Interview and career: 17.04, 57.03.

What was left out (the gaps this file fills):

- The solution design document itself and the options paper. 15.01 teaches ADRs and diagrams; no topic teaches how to assemble a full solution design, trace requirements to components, and recommend one option out of three (59.01).
- A catalog of recurring solution building blocks (notifications, documents, search, workflow, payments, reporting) and the build, buy or configure decision for each (59.02).
- Solution-level quality: acceptance criteria, NFR test plan, UAT, operational acceptance (59.03).
- Case drills for business systems. 11.05 and 11.06 are internet-scale system design, 58.11 is cloud, 48.02 is enterprise. None covers a portal, a workflow system or an ERP integration (59.04).
- A capstone that turns a client brief into a complete solution pack (59.05).
- Optional: web, mobile and omnichannel patterns (59.06).

The solution architect mindset (read once a quarter):

- Start from the business outcome and constraints, not from the technology you like.
- Offer options, not answers: two or three options, criteria, a recommendation, and what would change it.
- Cover the whole solution: people, process, data, integration, security, operations and transition, not only the application.
- Say what is out of scope. Write assumptions down, because an unwritten assumption is an unmanaged risk.
- Everything traces: requirement to decision to component to test.
- Estimate in ranges with assumptions. Cost and time are requirements too.
- Be the translator: the same design explained to the sponsor, the delivery team and operations.
- Stay hands-on enough to be believed. Review code and read the pipeline.
- Leave a decision trail the next architect can follow.

Rules (same as master-syllabus, with these additions):

- Same tags, same three-pass method, same gap-list rule, same loop, same note-size rule.
- Phase tags in this file: P1 = start once master Phase 1 is done. P2 = after the master batch named. P3 = after master Phase 2 core.
- Every FULL note ends with a Practice exercise (30 to 60 minutes) that produces one artifact for the fictional client in 59.05. Keep artifacts in the capstone folder.
- IDs 59.01 to 59.06 clash with nothing. Link IDs: master 1.01 to 24.03, AI 25.01 to 38.04, EA 39.01 to 48.02, leadership 50.01 to 57.04, cloud 58.01 to 58.11.
- I did not search the job market for this file. Run the check in Part 7 and let your own numbers change the plan.

## PART 2: NOTE TEMPLATE AND INSTRUCTION ADDENDUM

Use the master Part 2 template with these changes for IDs 59.01 to 59.06:

- Section 4: for each concept give the plain meaning, why it matters, and one template or checklist (example: a document outline, a scoring sheet, a test-plan table). No code.
- Section 5: add one line starting "Solution architect lens:" saying what the client sponsor, the delivery team and operations each ask about it.
- Section 6: a client project with requirements, constraints, the options considered, the one chosen and why, and a rough cost and time note. Include when NOT to apply it.
- Section 10 becomes Practice exercise: produce one artifact for the fictional client in 59.05. Give exact steps, the result you should have, and what to log. Skipped for O topics.

The consolidated instruction block in ea-master-syllabus Part 3 already carries the 59.01 to 59.06 range and this bullet (use the re-delivered EA file):

- IDs 59.01 to 59.06 (solution): in section 4 give one template or checklist per concept, no code; in section 5 add a line starting Solution architect lens:; section 6 is a client project with the options considered and a rough cost and time note; section 10 is a Practice exercise producing one artifact for the fictional client.

Also add solution-master-syllabus to the Project documents.

## PART 3: SOLUTION MASTER SYLLABUS

How to read a line: tick box, topic ID and title, tags, then the concepts to cover, then Links to topics already covered. Everything listed is in scope. Anything not listed is out of scope for now.

## D59 SOLUTION ARCHITECT SUPPLEMENT

☐ **59.01 Solution design document and options analysis** [P1 R L] reading a client brief or RFP for hidden constraints; solution design document structure (context and scope, business drivers, requirements and constraints, assumptions, architecture views for context, containers, deployment, data, integration and security, NFR mapping, options considered, decision and rationale, risks and dependencies, out of scope, cost and effort summary, transition and rollout, open items); HLD vs LLD and who reads each; the options paper (two or three options, criteria, weighted scoring, recommendation, reversibility); requirement-to-component traceability matrix; context diagram conventions; one-page summary on top of the detail; versioning and sign-off; a design document review checklist. Links: 15.01, 15.02, 54.03, 58.01

☐ **59.02 Solution building blocks and build, buy or configure** [P2 R L] a catalog of recurring components and the decision for each: authentication and SSO, notifications (email, SMS, push; deliverability, templates, opt-out), documents and files (storage, virus scan, preview, e-signature), search, scheduling and batch jobs, workflow and approvals, reporting and dashboards, payments and billing, audit trail, rules engines, third-party data APIs (address, KYC, maps), CMS; criteria for build vs buy vs configure; third-party API risk (rate limits, SLA, cost per call, data residency, exit); vendor selection scorecard; licensing traps (per user, per API call, per environment); estimating integration effort. Links: 24.01, 41.03, 54.06, 11.06

☐ **59.03 Solution quality, acceptance and operational readiness** [P3 R L] quality strategy mapped to the solution's risks; acceptance criteria written as testable statements; NFR test plan (performance, security, DR, accessibility); UAT planning and sign-off; defect severity and triage with the client; data migration validation and reconciliation; operational acceptance (runbooks, monitoring, alerts, support model, restore proof, DR drill); release readiness review; hypercare exit criteria; who signs what; traceability back to requirements. Links: 1.11, 9.07, 52.04, 52.06

☐ **59.04 Solution architecture case drills for business systems** [P3 R L] eight drills: a B2B customer portal integrated with ERP and CRM; a claims or case-management system with workflow and documents; online onboarding with KYC and e-signature; order-to-cash across ERP, e-commerce and a warehouse; cutover of a legacy .NET Framework system; replacing an in-house HR or CRM system with SaaS (SSO and integration); a reporting platform consolidating five systems; a customer notification platform. Method each time: brief, requirements and constraints, options, recommendation, diagram, NFR table, integration map, estimate range, risks and assumptions, delivery plan, how you would present it in 15 minutes. Links: 11.05, 11.06, 58.11, 48.02, 41.01

☐ **59.05 Solution capstone: client brief to solution pack** [P2 R L] scope: write or pick a fictional client brief (mid-size Indian company, business problem, budget, deadline, existing systems). Produce: requirements summary and traceability, context diagram, options paper, solution design document using 59.01, integration map, security and NFR mapping, estimate with range and assumptions, delivery plan and team shape, risk register, quality and acceptance plan from 59.03, cost view, and a 15-minute client presentation. You may reuse the reference workload from the cloud capstone (58.02) as the build-side proof, so one build supports two portfolio pieces. About 40 to 50 hours over six months, one piece per batch. Milestones: S1 brief, requirements, context diagram and options paper draft; S2 design document, building-block decisions and NFR and security mapping; S3 estimate, delivery plan, risk register, quality plan and presentation. Links: 17.02, 58.02, 54.04, 52.01

☐ **59.06 Web, mobile and omnichannel solution patterns** [P3 O L] web vs mobile vs PWA decision; native vs cross-platform; backend for frontend for mobile; offline and sync; push notifications; deep links; app store release and versioning; mobile security (storage, device attestation awareness); API design for mobile; accessibility and localization; analytics and feature flags. Links: 2.05, 2.08, 41.06, 3.02


TOTALS: 6 topics. 5 are required (full notes, about 5 printed pages) and 1 is optional (short note, about half a page). Required by phase: Phase 1 has 1, Phase 2 has 2, Phase 3 has 2. Optional: 1 in Phase 3. Printed total is about 6 pages, roughly 3 sheets printed on both sides.

## PART 4: STUDY ORDER (INTERLEAVED WITH THE MASTER BATCHES)

Each batch is added after the master batch named. Send solution IDs in a separate chat message from the technical IDs. Each batch adds one capstone milestone (59.05).

Links: IDs after "Links:" tell the AI which concepts not to repeat. They are not always prerequisites. The real prerequisites are in the order dependencies below.

- SA-B1 (after master Batch 6, which gives you 15.01 and the career notes 17.01 to 17.03): 59.01, 59.05. S1: brief, requirements, context diagram, options paper draft.
- SA-B2 (after master Batch 13, which gives you 15.02): 59.02. S2: design document, building-block decisions, NFR and security mapping.
- SA-B3 (after master Batch 15, which gives you 54.04 and 9.07): 59.03, 59.04, and optionally 59.06. S3: estimate, delivery plan, risk register, quality plan, presentation.

Order dependencies: 59.01 after 15.01. 59.05 after 59.01. 59.02 after 15.02. 59.03 after 1.11 and 9.07. 59.04 after 11.06, 54.04 and 41.01.

Practice log: every FULL note gets one artifact in the capstone folder. Log each in leadership Part L6 form. Once a quarter, pick two and write them as portfolio entries (17.02), in generic form without client details.

## PART 5: SOLUTION ARCHITECT ROUTE (WHAT TO TAKE FULL, SHORT OR LATER)

A solution architect needs breadth across the whole delivery, depth in design, integration and communication, and less depth in infrastructure operations. This route was computed by script from the topic tags of the four older files. Every ID was checked to exist and to be a required topic.

- A = full note (about 700 words) with the lab or practice exercise.
- B = short note (add B after the ID, about 300 words, sections 1, 4, 6 and 11).
- D = defer until a job asks.

Counts: of the 302 required notes in the four older files, 72 are A, 121 are B and 109 are D. Add the 5 required notes in this file (all A). Note-equivalents (a B counts as half): 72 + 60.5 + 5 = 137.5. At 6 a month that is about 23 months.

A (full notes):

- D01: 1.12
- D03: 3.01, 3.03, 3.07
- D04: 4.04, 4.07
- D06: 6.01, 6.02, 6.03
- D08: 8.11
- D09: 9.01 to 9.06, 9.08, 9.09
- D10: 10.05, 10.06, 10.07
- D11: 11.01 to 11.07
- D12: 12.01, 12.02, 12.04, 12.09, 12.10, 12.11, 12.12, 12.15
- D14: 14.04, 14.07
- D15: 15.01 to 15.06
- D17: 17.01 to 17.05
- D22: 22.14
- D24: 24.01, 24.03
- D41: 41.01, 41.02, 41.03
- D45: 45.01
- D50: 50.01
- D52: 52.01, 52.03
- D53: 53.01, 53.02, 53.05
- D54: 54.01 to 54.06
- D55: 55.01, 55.02, 55.03
- D57: 57.03

B (short notes):

- D01: 1.01 to 1.08, 1.10, 1.11
- D02: 2.03 to 2.06
- D03: 3.02, 3.04, 3.05, 3.08
- D04: 4.01 to 4.03, 4.05, 4.08, 4.09
- D05: 5.01 to 5.04
- D06: 6.04, 6.05
- D07: 7.01 to 7.09
- D09: 9.07
- D10: 10.01 to 10.04, 10.08
- D12: 12.03, 12.05 to 12.08, 12.13, 12.16
- D13: 13.01, 13.05, 13.06
- D14: 14.01 to 14.03, 14.05, 14.06
- D15: 15.07
- D16: 16.04
- D22: 22.01 to 22.05, 22.10 to 22.12
- D24: 24.02
- AI (design features into solutions): 25.01, 25.03, 26.01, 26.03, 27.02, 28.01, 31.01, 35.01, 36.01, 37.01, 37.02, 37.04
- EA: 39.01, 39.02, 40.01 to 40.03, 42.01, 42.02, 42.04, 42.05, 43.04, 44.01, 44.04, 44.05, 44.06, 46.01
- Leadership: 50.02, 50.03, 50.04, 51.01, 51.02, 51.05, 51.06, 51.07, 52.02, 52.04, 52.05, 52.06, 53.03, 53.04, 53.06, 53.07, 55.04, 55.05, 56.01, 56.02, 56.04, 56.06, 57.01

D (defer; 109 required notes, and the ranges below also sweep in a few optional AI topics, 29.04, 32.05 and 34.04, which are deferred too):

- Master: 1.09, 2.01, 2.02, 4.06, 8.01 to 8.10, 12.14, 13.02, 13.03, 13.04, 13.07, 16.01 to 16.03, 18.01 to 18.04, 22.06 to 22.09, 22.13
- AI: 25.02, 25.04, 26.02, 26.04, 26.05, 27.01, 28.02 to 28.06, 29.01 to 29.05, 30.01 to 30.04, 31.02 to 31.06, 31.08, 31.09, 32.01 to 32.09, 33.01 to 33.05, 34.01 to 34.05, 35.02 to 35.04, 36.02 to 36.07, 37.03, 37.05, 38.01 to 38.04
- EA: 39.03 to 39.05, 40.04, 42.03, 43.01 to 43.03, 44.02, 44.03, 47.01, 47.02, 47.04, 48.01, 48.02
- Leadership: 51.03, 51.04, 51.08, 52.07, 56.03

Rules:

- If a target posting names a deferred topic (for example Kubernetes, observability or a specific AI pattern), take that note then, at A.
- If you also follow the cloud route (cloud-master-syllabus Part 5B), take the better tier of the two for each topic: A beats B beats D. Defer a topic only when both routes defer it.
- The 5 notes in this file and the capstone are never deferred. They are the proof.

## PART 6: CERTIFICATION SEQUENCE (ALL VERIFY)

Pick at most three. Check each skills outline and prerequisites on Microsoft Learn, AWS and Open Group before booking.

- 1. AZ-104 (master 12.13). It teaches the platform that your designs sit on.
- 2. AZ-305 (12.15). The design-level credential, and it matches the solution architect job directly. Write 12.15 after master Batch 15.
- 3. One of: AWS Solutions Architect Associate (22.12) if postings ask for AWS; TOGAF Foundation (15.07) if you are heading toward the enterprise path; a product credential (for example Salesforce, SAP or Dynamics) only if your target employer builds on that product.
- Renewals: Microsoft associate and expert certifications renew by a free online assessment (verify). Put the dates in your calendar when you pass.

## PART 7: SOLUTION ARCHITECT MARKET CHECK AND SELF-ASSESSMENT

I did not search the job market for this file. Run this check and let your own numbers change the plan.

Quarterly check (30 minutes, add to the 24.03, AI, EA and cloud routines):

- Sites: Naukri, LinkedIn Jobs, Indeed. Location Kolkata, then Remote India. Experience filter 10 to 15 years. Record the date.
- Searches: "solution architect", "technical solution architect", ".net solution architect", "azure solution architect", "integration architect", "presales solution architect".
- For each: result count, then the top 20 postings. Tally must-haves: presales vs delivery role, industry, cloud (Azure, AWS, GCP), integration products (MuleSoft, Boomi, Azure Integration Services), packaged platforms (SAP, Salesforce, Dynamics), certifications asked, language (C#, Java, Python), employer type (GCC, services firm, product firm, consulting firm).
- Compare ratios between queries, not absolute counts. Log one table per quarter.

Rules for changing the plan:

- Presales is the main role in the postings you want: move 54.04 and 59.04 earlier, and take the client-skills notes (54.02, 55.01) before the technical B notes.
- SAP, Salesforce or Dynamics appears in more than a third: add a product awareness note when a job asks, and move 41.03 ahead of 41.01.
- AWS is a must-have more than twice as often as Azure: move 22.01 to 22.05 from B to A and put the SAA exam ahead of AZ-305.
- One industry dominates: write 45.01 first and take that industry's EA domain note (45.02 to 45.07) at full depth.
- Kubernetes or observability appears in more than half: pull 8.04 to 8.09 and 13.02, 13.03 out of D, or switch to the cloud route.

Quarterly self-assessment (30 minutes, 1 to 5 scale as in leadership Part L7):

- Score D09 microservices, D11 system design, D15 architecture practice, D41 integration, D54 stakeholders and business, D55 communication, D59 this file.
- Target before applying for solution architect roles: no domain below 3; D15, D54 and D59 at 4.
- Pick the two lowest scores and bring them forward in the next batch.

## PART 8: WRAP-UP

This is the last supplement. The planning is closed under the freeze rule in ea-master-syllabus Part 9: no new syllabus files until 18 October 2027, missing concepts go on gap lists, and the plan changes only through the quarterly checks.

The path is one line with branches: tech lead, then solution architect, then either cloud architect or enterprise architect. The solution architect route in Part 5 is the trunk. The cloud route (cloud-master-syllabus Part 5B) and the EA file's topics are branches you take on top of it, so you do not need to decide between them now.

Final map of the six documents: master-syllabus (technology, languages, AWS), ai-master-syllabus (AI), leadership-syllabus (renumbered D50 to D57), ea-master-syllabus (enterprise path, and the one instruction block), cloud-master-syllabus (D58), solution-master-syllabus (this file, D59). The same Project holds all six.

Success measure for the solution architect path: a finished capstone pack (options paper, design document, estimate, risk register, presentation), AZ-104 and AZ-305 passed, one real solution you led end to end that you can describe with the options you rejected and the estimate against the actual, and the ability to present any solution in 15 minutes.

Filing: same print settings as master Part 6. Word file for this domain: D59-solution-architect-supplement. Keep capstone artifacts in their own binder section next to the practice log.
