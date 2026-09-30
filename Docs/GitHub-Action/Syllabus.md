# GitHub Actions: Prerequisites & Core Topics (Architect Level)

**Legend:** R = Required | O = Optional | E = Exam-oriented | L = Real-life use

## 1. Git & GitHub Basics
- Git fundamentals (commit, branch, merge, rebase, tags): **R, E, L**
- Branching strategies (trunk-based, GitFlow, GitHub Flow): **R, E, L**
- Pull requests & code review: **R, E, L**
- Forks vs. clones: **O, E**
- Git hooks: **O, L**
- Monorepo vs. polyrepo: **O, L**

## 2. GitHub Platform Essentials
- Repositories (public/private/internal): **R, E**
- Organizations, teams, roles & permissions: **R, E, L**
- GitHub Apps vs. OAuth Apps: **R, E, L**
- Personal Access Tokens (classic vs. fine-grained): **R, E, L**
- GITHUB_TOKEN & its permissions: **R, E, L**
- Branch protection rules / Rulesets: **R, E, L**
- CODEOWNERS: **R, E, L**
- GitHub Environments & deployment protection rules: **R, E, L**
- Secrets & Variables (repo / environment / org level): **R, E, L**
- GitHub Packages & Container Registry (GHCR): **O, E, L**
- GitHub Enterprise (Cloud vs. Server): **O, E, L**

## 3. YAML & Config Basics
- YAML syntax (maps, lists, multi-line strings, anchors): **R, E, L**
- JSON basics: **O, L**
- Expressions & contexts (`github`, `env`, `secrets`, `matrix`, `needs`): **R, E, L**
- Functions (`contains`, `format`, `hashFiles`, `success`, `failure`): **R, E, L**

## 4. CI/CD Concepts
- CI vs. Continuous Delivery vs. Continuous Deployment: **R, E**
- Pipeline stages (build, test, scan, package, deploy): **R, E, L**
- Artifacts & caching: **R, E, L**
- Deployment strategies (blue-green, canary, rolling): **R, E, L**
- Release management & versioning (SemVer): **R, E, L**
- GitOps: **O, L**
- Infrastructure as Code (Terraform basics): **O, L**

## 5. Linux, Shell & Scripting
- Linux command line basics: **R, L**
- Bash scripting: **R, L**
- PowerShell (Windows runners): **O, L**
- Environment variables & exit codes: **R, E, L**

## 6. Containers & Runtime
- Docker basics (image, container, Dockerfile, registry): **R, E, L**
- Docker Compose: **O, L**
- Kubernetes basics: **O, L**
- Service containers in workflows: **O, E, L**

## 7. Security & Identity
- Secrets management concepts: **R, E, L**
- OIDC (OpenID Connect) for cloud authentication: **R, E, L**
- Least privilege principle: **R, E, L**
- Dependabot: **R, E, L**
- CodeQL & code scanning: **R, E, L**
- Secret scanning & push protection: **R, E, L**
- Supply chain security (SBOM, artifact attestations, SLSA): **O, E, L**
- Pinning actions to SHA: **R, E, L**
- Third-party action risk: **R, L**

## 8. Testing & Quality
- Unit, integration, and e2e testing concepts: **R, L**
- Linting & static analysis: **O, L**
- Code coverage reporting: **O, L**
- Test matrix strategy: **R, E, L**

## 9. Cloud Basics
- One cloud platform (AWS / Azure / GCP) fundamentals: **R, L**
- IAM roles & trust policies: **R, E, L**
- Container registries (ECR / ACR / GCR): **O, L**

## 10. Networking Basics
- HTTP/HTTPS & REST APIs: **R, E, L**
- Webhooks: **R, E, L**
- DNS, firewalls, IP allowlists (self-hosted runners): **O, L**

## 11. Core GitHub Actions Terms (know before deep dive)
- Workflow, Event, Job, Step, Action, Runner: **R, E**
- Triggers (`push`, `pull_request`, `schedule`, `workflow_dispatch`, `workflow_call`, `repository_dispatch`): **R, E, L**
- Filters (branches, paths, tags): **R, E, L**
- GitHub-hosted vs. self-hosted runners: **R, E, L**
- Runner groups & labels: **O, E, L**
- Larger runners & ARC (Actions Runner Controller): **O, L**
- Matrix builds: **R, E, L**
- `needs` & job dependencies: **R, E, L**
- Conditional execution (`if`): **R, E, L**
- Concurrency & cancel-in-progress: **R, E, L**
- Reusable workflows: **R, E, L**
- Composite actions: **R, E, L**
- JavaScript / Docker custom actions: **O, E, L**
- Starter workflows & organization templates: **O, E**
- Workflow commands & `GITHUB_ENV` / `GITHUB_OUTPUT`: **R, E, L**
- Job summaries & annotations: **O, L**
- Marketplace & action versioning: **R, E, L**
- Debugging (step debug logging, re-run, act): **O, L**
- Usage limits, billing, and retention policies: **O, E, L**
- Audit log & Actions policies: **O, E, L**

## 12. Architect-Level Additions
- Enterprise-wide governance of Actions (allowed actions, policies): **R, E, L**
- Multi-environment promotion patterns: **R, E, L**
- Monorepo pipeline design: **O, L**
- Cost optimization & runner scaling: **O, L**
- Migration from Jenkins / GitLab CI / Azure DevOps: **O, L**
- Observability of pipelines (metrics, DORA): **O, L**