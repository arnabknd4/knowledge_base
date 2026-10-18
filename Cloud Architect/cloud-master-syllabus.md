---
title: "Cloud Architect Supplement (companion to master-syllabus)"
subtitle: "Experienced .NET Lead (12+ years, Kolkata market) to Cloud Architect on Azure and AWS. Topic IDs 58.01 to 58.11"
---

## PART 1: AUDIT RESULT AND HOW THIS FILE FITS

Verdict: the cloud-architect path is already about 90% covered. This file is deliberately small. It adds 11 topics for real gaps, a capstone definition, a path-specific cut list, a batch order and a certification sequence. After this file the planning is closed (freeze rule, Part 8).

Already covered (do not duplicate):

- Azure: master D12 (12.01 to 12.16), compute choice 8.11, Azure SQL 4.07, Cosmos DB 4.09.
- AWS: master D22 (22.01 to 22.14), including .NET workloads and migration (22.10) and the Azure, AWS and GCP mapping sheet (22.14).
- Containers and Kubernetes: D08. IaC and pipelines: D07 (Terraform 7.07, Azure DevOps 7.03, OIDC in pipelines 7.08).
- Messaging, caching, resilience, observability, security: D05, D06, 3.04, D13, D14.
- Migration and modernization: 12.09, 9.03, 22.10, leadership 53.06 and 53.07.
- Cloud-adjacent AI: ai-master-syllabus D31, D32, D34, D35.
- Enterprise cloud topics: ea-master-syllabus 43.01 to 43.04.

What was left out (the gaps this file fills):

- No definition of the cloud capstone, although master Part 1 relies on one. Skills come from building it (58.02).
- Serverless and event-driven architecture on cloud: only Functions triggers appear (58.03).
- Cloud network design at scale: IP planning, hybrid DNS, private endpoint DNS pitfalls, egress (58.04). Most real network incidents live here.
- Hybrid identity and Windows workloads: Kerberos, AD, SQL and Windows licensing. This is the real blocker for legacy .NET Framework migrations (58.05).
- Choosing data services by access pattern, and moving data at scale (58.06).
- Kubernetes platform engineering and GitOps: only optional awareness topics existed (58.07).
- Guardrails as code: policy, account vending, drift, CSPM (58.08).
- Resilience engineering and DR drills as practice, not theory (58.09).
- Cloud limits, quotas and capacity engineering (58.10).
- Cloud scenario drills and interview scenarios (58.11).
- The cloud-architect role and decision frame (58.01).

The cloud architect mindset (read once a quarter):

- Managed first: run less. Self-host only with a reason you can write in one line.
- Cost is a non-functional requirement. Every design has a unit cost you can state.
- Failure is normal. Know the blast radius of a zone, a region, a subscription, a pipeline and a credential.
- Identity is the first perimeter, network the second.
- If it is not code (IaC, policy, pipeline), it did not happen and will drift.
- Limits and SLAs drive design. Know quotas before you commit to a design.
- Two clouds, one model: learn the concept first, then the Azure and AWS product names.
- Operations is part of the architecture: if you cannot say who gets paged, the design is not done.
- Services change monthly. Anything not verified in the last quarter is marked (verify).

Rules (same as master-syllabus, with these additions):

- Same tags, same three-pass method, same gap-list rule, same loop, same note-size rule.
- Phase tags in this file: P1 = start once master Phase 1 has begun. P2 = after the named master batch. P3 = after master Phase 2 core.
- Every FULL note ends with a lab on the Azure or AWS free tier, using a budget alert set first and a clean-up step (terraform destroy or resource group delete). Labs that cost money need a stated cap.
- Cloud topics always name the Azure and AWS equivalent of each concept.
- The cloud capstone (58.02) is the practice vehicle. Each batch adds one slice to it.

## PART 2: NOTE TEMPLATE AND INSTRUCTION ADDENDUM

Use the master Part 2 template with these changes for IDs 58.01 to 58.11:

- Section 4: for each concept add the Azure and AWS equivalent in one clause and the limit or default worth memorizing (verify).
- Section 5: add one line starting "Cloud architect lens:" saying what a client, a security team and a finance team ask about it.
- Section 6: a cloud situation with region, zone or account layout and a rough cost note. Include the trade-off and when NOT to use it.
- Section 10: mini lab on the free tier, budget alert first, clean-up last. Add the slice of the capstone (58.02) the lab contributes to.

To add to the consolidated instructions in ea-master-syllabus Part 3: add "58.01 to 58.11 in cloud-master-syllabus" to the list of ranges, and add this bullet under Range changes:

- IDs 58.01 to 58.11 (cloud): in section 4 give the Azure and AWS equivalent of each concept and one limit or default to memorize; in section 5 add a line starting Cloud architect lens:; section 6 includes region or account layout and a rough cost note; section 10 is a free-tier lab with a budget alert first and a clean-up step.

Also add cloud-master-syllabus to the Project documents.

## PART 3: CLOUD MASTER SYLLABUS

How to read a line: tick box, topic ID and title, tags, then the concepts to cover, then Links to topics already covered. Everything listed is in scope. Anything not listed is out of scope for now. Link IDs: master 1.01 to 24.03, AI 25.01 to 38.04, EA 39.01 to 48.02, leadership 50.01 to 57.04.

## D58 CLOUD ARCHITECT SUPPLEMENT

☐ **58.01 Cloud architect role and decision frame** [P1 R L K] workload vs platform vs enterprise cloud architect; deliverables (high-level design, landing zone design, Well-Architected review, DR plan, cost model, migration plan, ADRs); service selection criteria (managed vs self-managed, PaaS first, lock-in vs velocity, reversibility, team skill); region and zone selection (latency, residency, service availability, price, paired regions); cost as a design input; the cloud architect in services firms, product firms and GCCs; first 90 days on a cloud program; what interviews test. Links: 50.01, 12.10, 22.11

☐ **58.02 Cloud capstone: landing zone and reference workload** [P2 R L] scope: Azure landing zone built with Terraform (management groups, subscriptions, policy, hub-spoke network, private endpoints); a reference workload (.NET API, SQL, Service Bus, Redis) on Container Apps or AKS; pipeline with OIDC to Azure; observability with SLO alerts; Key Vault and managed identity everywhere; a measured regional failover drill (real RTO and RPO); cost dashboard with budgets and tags; one slice mirrored on AWS (the API on ECS Fargate or Lambda with RDS) deployed from the same pipeline; ADRs, a Well-Architected review, runbooks and a postmortem of one deliberate failure. Milestones M1 to M6, one per batch. About 100 hours over a year, each lab capped and torn down with destroy. Links: 17.02, 7.07, 12.16, 22.09

☐ **58.03 Serverless and event-driven architecture on cloud** [P2 R E L] Azure Functions hosting plans, Lambda, Container Apps jobs; triggers and bindings; scaling behaviour and concurrency limits; cold starts and mitigation; durable orchestration (Durable Functions, Step Functions); idempotency and retries on triggers; queue-based load leveling and fan-out; webhooks and scheduled jobs; cost model and break-even against always-on compute; limits to memorize (timeouts, payload, concurrency; verify); observability and local testing; .NET isolated worker model (verify); when serverless is the wrong choice. Links: 3.05, 6.04, 12.04, 22.04, 22.06

☐ **58.04 Cloud network design at scale** [P2 R E L] IP address planning and IPAM; overlapping CIDR problems; hub-spoke vs Transit Gateway vs Virtual WAN decision; hybrid DNS resolution and private endpoint DNS pitfalls (private zones, conditional forwarders, resolvers); egress control and inspection; multi-region connectivity; private access to PaaS and SaaS; connectivity to branch offices and data centres (VPN, ExpressRoute, Direct Connect); flow logs, Network Watcher and Reachability Analyzer; a network troubleshooting playbook (DNS first, then routes, then NSG or security group, then firewall). Links: 12.03, 22.03, 43.02, 16.04

☐ **58.05 Hybrid identity and Windows workloads on cloud** [P2 R L K] AD DS on cloud VMs vs Entra Domain Services vs AWS Managed AD; Entra Connect and Cloud Sync; Kerberos and NTLM constraints for legacy .NET Framework apps; gMSA; Windows authentication in App Service and containers; SQL Server on VM vs Managed Instance vs RDS (verify limits); Windows Server and SQL licensing in cloud (Azure Hybrid Benefit, license mobility; verify); IIS lift-and-shift gotchas (machine keys, session state, local file shares, scheduled tasks, COM and GAC dependencies); coexistence while migrating in waves. Links: 12.02, 12.09, 16.02, 22.10, 8.11

☐ **58.06 Cloud data services selection and data migration** [P2 R E L] choosing relational, NoSQL, cache, search, queue-backed and analytics services by access pattern and consistency need on Azure and AWS; HA and DR options per service; online vs offline migration (DMS, replication, BACPAC, Data Box and Snowball; verify); bandwidth and transfer-time math; cutover and validation plan; egress and inter-region cost; backup and restore at scale; residency constraints. Links: 4.07, 4.09, 22.05, 40.03, 12.09

☐ **58.07 Kubernetes platform engineering and GitOps** [P3 R E L] cluster lifecycle as code; GitOps with Argo CD or Flux and the pull model; multi-tenancy (namespaces, quotas, RBAC, network policy); policy as code in the cluster (Gatekeeper or Kyverno, Azure Policy for Kubernetes); Pod Security Standards and admission control; service mesh decision criteria (when not to); ingress strategy; multi-cluster and fleet management; AKS vs EKS comparison; autoscaling stack (HPA, KEDA, Karpenter awareness; verify); upgrade and node image patching routine; platform as a product. Links: 7.10, 8.08, 8.12, 53.08

☐ **58.08 Cloud governance and guardrails as code** [P3 R E L] preventive, detective and corrective controls; Azure Policy, AWS SCPs and Config rules; subscription and account vending; Terraform landing zone modules (Azure Verified Modules, Control Tower awareness; verify); drift detection and remediation; exception process and expiry; compliance reporting; CSPM and CNAPP (Defender for Cloud, Security Hub and others; verify); tag enforcement; IaC pipeline guardrails (Checkov, OPA and Conftest); break-glass design. Links: 12.06, 12.16, 22.01, 7.07, 14.05, 43.04

☐ **58.09 Cloud resilience engineering and DR drills** [P3 R E L] failure modes by scope (instance, zone, region, control plane, identity, DNS, pipeline); dependency mapping and blast radius; DR runbooks; game days and fault injection (Azure Chaos Studio, AWS Fault Injection Service; verify); backup restore testing; quota and capacity in the failover region; control-plane vs data-plane dependencies; multi-region data challenges; DNS and traffic-manager failover timings; measuring real RTO and RPO; lessons from public cloud outages (verify). Links: 11.04, 12.11, 13.08

☐ **58.10 Performance, capacity and quota engineering** [P3 R L] sizing and right-sizing; service quotas and limits as design inputs; throttling behaviour; autoscale design (metrics, cooldown, scale-in safety); tail latency across zones; cloud-side load testing and test-environment cost; reserved capacity and commitment planning; GPU and scarce-capacity awareness; a limits checklist per service for Azure and AWS (verify). Links: 13.07, 12.12, 22.04

☐ **58.11 Cloud architect case drills and interview scenarios** [P3 R L] eight drills answered in Azure and AWS terms: landing zone for 20 teams; migrating 200 .NET Framework apps; regional DR for a payments system; multi-tenant AKS platform; cutting a cloud bill by 30 percent; securing a lift-and-shift; zero-downtime database migration; connecting branch offices and a data centre. Method each time: requirements, constraints, options, decision, diagram, cost, risks, operations, how you would explain it to a client. Includes a whiteboard template and a 45-minute plan. Links: 11.05, 11.06, 17.04, 12.15


TOTALS: 11 topics, all required (full notes, about 11 printed pages). Required by phase: Phase 1 has 1, Phase 2 has 5, Phase 3 has 5. Optional: none. Printed total is about 11 pages, roughly 6 sheets printed on both sides.

## PART 4: STUDY ORDER (INTERLEAVED WITH THE MASTER BATCHES)

Each batch is added after the master batch named. Send cloud IDs in a separate chat message from the technical IDs. Each batch adds one capstone slice (58.02).

- CL-B1 (after master Batch 4, AZ-104 core): 58.01, 58.04, 58.02. M1: landing zone skeleton and hub-spoke network in Terraform.
- CL-B2 (after master Batch 6): 58.05, 58.06. M2: reference workload with managed identity and Key Vault.
- CL-B3 (after master Batch 9): 58.03, 58.07, 58.10. M3: container platform, pipeline with OIDC, autoscale tests.
- CL-B4 (after master Batch 10): 58.08. M4: policy, tags, budgets, drift check in the pipeline.
- CL-B5 (after master Batch 15): 58.09, 58.11, plus pull forward 12.15 and 12.16 from master Batch 17. M5: failover drill with measured RTO and RPO. M6: AWS slice, ADRs, Well-Architected review, postmortem.

Order dependencies: 58.04 after 12.03. 58.05 after 12.09 if possible (otherwise in the same batch). 58.07 after 8.04 to 8.09. 58.08 after 12.06 and 7.07. 58.09 after 12.11. 58.11 after 12.10.

Write now rather than after Phase 3 (they were optional): 12.17 (Azure Arc and hybrid awareness) and 53.08 (platform engineering), both as short notes, in CL-B3.

Practice log: every FULL note gets one lab result and one capstone commit. Log each in leadership Part L6 form. Once a quarter, pick two and write them as portfolio entries (17.02).

## PART 5: CUTTING THE LOAD FOR THE CLOUD PATH

For a cloud architect target, the other three files contain notes you can defer until a job asks. Keep everything not listed. Counts below are required notes only.

Defer from the EA file (22 notes): D39 (39.01 to 39.05), D44 (44.01 to 44.06), 45.01, 46.01, D47 (47.01, 47.02, 47.04), D48 (48.01, 48.02), 40.01, 40.02, 40.04, 41.03. Keep 40.03, 41.01, 41.02, 42.01 to 42.05 and 43.01 to 43.04 (12 notes).

Defer from the AI file (14 notes): 25.02, 31.09, 32.06, 32.07, 32.09, 33.04, 33.05, 36.05, 36.06, 36.07, 37.03, 37.04, 38.03, 38.04. Keep the rest, since cloud architects must design AI on cloud. Take at B: 31.03, 31.04, 31.06, 32.02, 32.03, 32.04, 33.02.

Defer from the master file (11 notes): 2.03, 2.04, 2.05, 2.06, 4.06, 15.07, 18.01, 18.02, 18.03, 18.04, 22.13.

Leadership file: keep all 44, they are short and drive promotion.

Arithmetic: 302 required notes across the four files, plus 11 here, minus 47 deferred, is about 266 required notes. At 6 a month that is about 44 months. The seven B notes save a few more hours. This is still long, so rely on the batches: after CL-B3 and master Batch 10 you already have a credible cloud-architect profile for interviews, and everything later raises your level.

Deferred notes are not deleted. Take them when a job asks, or switch paths: if you move to the EA path, the EA file's own cut list applies instead.

## PART 6: CERTIFICATION SEQUENCE (ALL VERIFY)

Pick at most four. Check each skills outline and prerequisites on Microsoft Learn, AWS and CNCF before booking.

- 1. AZ-104 (master Batch 4, notes 12.13). First, because everything else assumes it.
- 2. AWS Solutions Architect Associate (22.12). After master Batch 6A, to prove the second cloud.
- 3. AZ-305 (12.15, pulled forward to CL-B5). The architect-level credential for the target role.
- 4. One of: AZ-400 (12.14) for pipeline-heavy roles, CKA for Kubernetes-heavy roles, Terraform Associate for IaC-heavy roles, AZ-500 for security-heavy roles. Choose from the market check below, not from habit.
- Only when a job asks: AWS Solutions Architect Professional (22.13), GCP Professional Cloud Architect (23.01 first), CKAD, AZ-204.
- Renewals: Microsoft associate and expert certifications renew by a free online assessment (verify); AWS certifications renew every three years (verify). Put the dates in your calendar when you pass.

## PART 7: CLOUD MARKET CHECK AND SELF-ASSESSMENT

I did not search the job market for this file. Run this check and let your own numbers change the plan.

Quarterly cloud market check (30 minutes, add to the 24.03, AI and EA routines):

- Sites: Naukri, LinkedIn Jobs, Indeed. Location Kolkata, then Remote India. Experience filter 10 to 15 years. Record the date.
- Searches: "cloud architect", "azure solution architect", "aws solutions architect", "devops architect", "platform engineer", "cloud migration architect", "kubernetes architect".
- For each: result count, then the top 20 postings. Tally must-haves: cloud (Azure, AWS, GCP), IaC (Terraform, Bicep, CloudFormation), Kubernetes, certifications asked, migration, FinOps, security, language (C#, Java, Python), employer type (GCC, services firm, product firm, consulting firm).
- Compare ratios between queries, not absolute counts. Log one table per quarter.

Rules for changing the plan:

- GCP appears in more than a third of the postings you want: write 23.01, then take a GCP associate-level path.
- Kubernetes appears in more than half: move 58.07 before 58.03 and add the CKA to Part 6 as the fourth certification.
- AWS is a must-have more than twice as often as Azure: move the AWS notes 22.03 to 22.09 into Phase 2 and move the SAA exam ahead of AZ-305.
- Terraform is a must-have more often than Bicep: keep Terraform as the capstone language (it already is) and drop Bicep to awareness.
- Python is a must-have in more than half: promote 16.05 first, then 20.01.

Quarterly cloud self-assessment (30 minutes, 1 to 5 scale as in leadership Part L7):

- Score D07 CI/CD and IaC, D08 containers and Kubernetes, D12 Azure, D22 AWS, D13 observability, D14 security, D16 foundations (Linux, networking, scripting) and D58 cloud supplement.
- Target before applying for cloud architect roles: no domain below 3; D12, D22, D08 and D58 at 4.
- Pick the two lowest scores and bring them forward in the next batch.

## PART 8: WRAP-UP

This is the last supplement. The planning is closed under the freeze rule in ea-master-syllabus Part 9: no new syllabus files until 18 October 2027, missing concepts go on gap lists, and the plan changes only through the quarterly checks.

Final map of the five documents: master-syllabus (technology, languages, AWS), ai-master-syllabus (AI), leadership-syllabus (renumbered D50 to D57), ea-master-syllabus (enterprise path), cloud-master-syllabus (this file). The same Project holds all five and one instruction block.

Success measure for the cloud path: a working capstone with a measured failover drill, AZ-104 and AZ-305 passed, one AWS credential, and one production cloud decision you led and can describe with numbers.

Filing: same print settings as master Part 6. Word file for this domain: D58-cloud-architect-supplement. Keep capstone artifacts (diagrams, ADRs, review, runbooks, postmortem) in their own binder section next to the practice log.
