# Objective: Use service containers (`services:`) for dependent services such as databases and queues; configure ports, health checks, and container options.

## What

Service containers let a workflow run dependent systems locally, which is extremely useful for realistic integration tests without additional infrastructure.

## Why

- Service containers are fast and cheap for CI but may not match the full production topology.
- Health checks reduce flaky startup timing but add complexity.
- Local dependencies speed up tests but must be chosen carefully for real risk coverage.

## How

Declare each dependency under `services`, set a deterministic image and health behavior, and map ports according to whether the job runs on the host or in a container.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: postgres
        ports:
          - 5432:5432
        options: >-
          --health-cmd="pg_isready -U postgres"
          --health-interval=10s
          --health-timeout=5s
          --health-retries=5
```

## Features

A service container supplies a job-scoped dependency such as a database or queue. Networking differs by whether the job itself runs in a container or directly on the runner host.

**Official references**

- [About service containers](https://docs.github.com/en/actions/using-jobs/about-service-containers)
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Limit exposed ports and set credentials explicitly.
- Prefer health checks to naive `sleep` waiting.
- Use clean, deterministic service state so tests are repeatable.

**Don't**

- Don't forget to consider service readiness before the app starts.
- Don't assume local service containers perfectly mirror production.
- Don't use ports or dependency names without confirming the runtime configuration.

## Real-life implementation

Make service versions, ports, credentials, and readiness behavior predictable. Health checks and deterministic test data reduce flakes; service containers are test dependencies, not a substitute for production infrastructure.

## Q&A

**Q: Would your app reach the service at the expected hostname and port?**

**A:** A containerized job can usually address the service by its service label; a host-run job should use the mapped host port, commonly through `localhost`.

**Q: What happens if the dependency is still starting up when the job begins?**

**A:** The test may race and fail. Configure a health check or explicit readiness retry instead of assuming container start means the service is ready.

**Q: Are the service settings deterministic enough to avoid random or flaky test results?**

**A:** Pin a suitable service image and define ports, health checks, and test credentials/data explicitly; avoid relying on mutable defaults.
