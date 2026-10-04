# Configure and monitor GitHub-hosted and self-hosted runners

## What
Runner choice determines how workflows execute, how they reach internal services, and how much lifecycle ownership the enterprise has. GitHub-hosted and self-hosted runners are designed for different risks, cost models, and operating assumptions.

## Why
A runner is not just compute; it is a trust boundary. The correct choice depends on workload sensitivity, network access, required tools, and support needs. Choosing poorly can introduce compliance gaps or slow feedback loops.

## How
- Evaluate the workload and required network reachability before choosing a runner type.
- Use GitHub-hosted runners for standard public or ephemeral validation workloads.
- Use self-hosted runners for private networking, custom hardware, and tightly controlled environments.
- Label and monitor runners to route jobs to the right pool and detect stale or unhealthy machines.

## Features
- GitHub-hosted runner simplicity and elastic scale.
- Self-hosted runner control for private access and custom tooling.
- Labels for routing workloads by environment, trust level, or OS.
- Concurrency and monitoring for job queue hygiene and health.

## Do's and Don'ts
- Do: label runners by purpose such as `ci`, `private`, or `prod-deploy`.
- Do: monitor runner health and queue behavior regularly.
- Do: rotate runner credentials and remove stale machines promptly.
- Do: align runner type to workload risk and connectivity requirements.
- Don't: assume all runner types are interchangeable.
- Don't: mix production and development workloads in the same pool unless the risk model supports it.
- Don't: ignore runner labels when troubleshooting job scheduling.
- Don't: overlook stale or unreachable self-hosted runners.

## Real-life implementation
A product team uses GitHub-hosted runners for static analysis, unit tests, and packaging. Production deployment to a private Kubernetes cluster runs on a self-hosted runner pool configured for private networking, internal CA trust, and explicit deployment approvals. The split reduces cost while preserving stricter controls for production execution.

## Q&A
### Q: When should I choose GitHub-hosted runners?
A: When the workload is ephemeral, public or general-purpose, and does not require private network access or custom software beyond the hosted image.

### Q: When is self-hosted execution required?
A: When the workflow needs access to private resources, custom operating environments, or stronger compliance controls than the GitHub-hosted runner image offers.

### Q: Why are labels important?
A: Labels let the workflow target the correct runner pool, reducing accidental use of the wrong environment or trust zone.

### Q: What operational issue should you monitor most closely?
A: Runner health, offline machines, queue delays, and stale registrations that can block or misroute workflows.

## Official docs
- [About GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners)
- [About self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners)
- [Adding self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners)
- [Using labels with self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners)
- [Monitoring and troubleshooting self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)

## Back to syllabus
- [Manage GitHub Actions for the enterprise](../../README.md)
