# Python for DevOps + SRE: Prerequisite Topics (Architect Level)

**Legend:** R = Required | O = Optional | E = Exam oriented | L = Real-life use

---

## 1. Python Core Language
- Data types (int, str, list, dict, set, tuple): R, E, L
- Variables, operators, type casting: R, E
- Conditionals and loops: R, E, L
- Functions (args, kwargs, return values): R, E, L
- Scope (LEGB): R, E
- Comprehensions (list/dict/set): R, E, L
- Lambda, map, filter: O, E
- Modules and packages: R, E, L
- Exception handling (try/except/finally): R, E, L
- Context managers (`with`): R, E, L
- Iterators and generators: R, E, L
- Decorators: R, E, L
- Closures: O, E
- Type hints: R, L
- Dataclasses: O, L
- Async/await (asyncio): O, L
- Multithreading vs multiprocessing vs GIL: R, E, L
- Logging module: R, E, L

## 2. OOP and Design
- Classes and objects: R, E, L
- Inheritance and composition: R, E
- Dunder methods: O, E
- SOLID principles: R, E
- Design patterns (Factory, Singleton, Strategy, Observer): O, E
- Idempotency: R, E, L
- Immutability: O, E

## 3. Environment and Packaging
- Virtual environments (venv): R, E, L
- pip and requirements.txt: R, E, L
- pyproject.toml: R, L
- Poetry / pipx / uv: O, L
- Dependency pinning and lock files: R, L
- Python version management (pyenv): O, L
- Building wheels / publishing packages: O, L

## 4. File, OS and System Automation
- File I/O: R, E, L
- pathlib / os / shutil: R, E, L
- subprocess: R, E, L
- Environment variables: R, E, L
- Argument parsing (argparse, click, typer): R, L
- Signal handling: O, L
- Regex: R, E, L
- Parsing formats (JSON, YAML, TOML, CSV, XML): R, E, L
- Scheduling (cron, schedule libs): O, L

## 5. Networking and APIs
- HTTP basics (methods, status codes, headers): R, E, L
- requests / httpx: R, L
- REST API consumption: R, E, L
- Authentication (API keys, tokens, OAuth2, JWT): R, E, L
- Retries, timeouts, backoff: R, E, L
- Pagination and rate limiting: R, L
- Sockets: O, E
- SSH automation (paramiko, fabric): O, L
- Webhooks: R, L
- Web frameworks (Flask, FastAPI): O, L

## 6. Cloud and Infra Automation
- boto3 (AWS SDK): R, E, L
- Azure SDK / GCP SDK: O, L
- Kubernetes Python client: O, L
- Docker SDK: O, L
- Ansible modules in Python: O, L
- Terraform CDK / Pulumi: O, L
- Secrets handling (env, vault, secrets manager): R, E, L

## 7. Data Handling for Ops
- JSON/YAML manipulation: R, E, L
- Templating (Jinja2): R, L
- pandas basics: O, L
- Log parsing: R, L
- Text processing: R, L
- Database access (sqlite3, SQLAlchemy, psycopg): O, L

## 8. Testing and Quality
- pytest: R, E, L
- Unit vs integration vs e2e tests: R, E
- Mocking (unittest.mock): R, E, L
- Fixtures: R, L
- Code coverage: O, E, L
- Linting and formatting (ruff, flake8, black): R, L
- Static typing (mypy): O, L
- Pre-commit hooks: O, L
- TDD: O, E

## 9. DevOps Integration
- Git basics with Python (GitPython): O, L
- CI/CD scripting (GitHub Actions, Jenkins): R, E, L
- Containerizing Python apps (Dockerfile): R, E, L
- Configuration management: R, E
- Infrastructure as Code concepts: R, E
- Python in pipelines: R, L

## 10. SRE Specific
- Observability (logs, metrics, traces): R, E, L
- Prometheus client library: O, L
- OpenTelemetry: O, E, L
- Health checks / readiness probes: R, E, L
- SLI, SLO, SLA, error budgets: R, E, L
- Alerting scripts: R, L
- Incident automation and runbooks: R, E, L
- Chaos engineering scripts: O, E
- Capacity and performance testing (Locust): O, L
- Profiling (cProfile, memory profiling): O, L
- Concurrency for scale (queues, workers, Celery): O, E, L
- Graceful shutdown and failure handling: R, E, L

## 11. Security
- Input validation: R, E
- Secrets management: R, E, L
- Dependency scanning (pip-audit, Bandit): R, E, L
- Least privilege (IAM with scripts): R, E, L
- Supply chain security: O, E
- TLS/SSL handling: O, E, L

## 12. Architect-Level Concepts
- Script vs tool vs service vs library (when to use what): R, E
- Automation maturity and toil reduction: R, E
- Scalability and reliability patterns (retry, circuit breaker, bulkhead): R, E
- Event-driven automation: O, E, L
- Monorepo vs polyrepo for ops code: O, E
- Python vs Go vs Bash (trade-offs): R, E
- Packaging and distribution strategy: O, E
- Documentation and docstrings: R, L