# Monitor CPU, memory, restarts, exit status, disk, network, and health

**Domain:** Observability, reliability, and incident response<br>
**Syllabus objective:** [Monitor CPU, memory, restarts, exit status, disk, network, and health](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Combine host and container resource signals with lifecycle and application telemetry. Track CPU throttling, memory pressure/OOM, restart count, exit code, filesystem capacity, network errors, and health state.

## Why
Failures may arise from host exhaustion, storage pressure, or dependency/network behavior. Resource charts alone can hide restarts, saturation, and user impact.

## How
Define service dashboards and alerts with ownership, baselines, and labels such as digest and instance. Correlate runtime stats with host and application latency/error signals; inspect host and daemon behavior.

## Features
Docker exposes container resource usage through Engine metrics and tooling, but coverage varies by runtime and host. A green resource graph does not prove requests succeed.

## Code snippets (if any)
```sh
docker stats --no-stream api
```

## Do's and Don'ts
Do: alert on sustained symptoms tied to impact. Don’t: page on every restart without context or treat docker stats as historical monitoring.

## Real-life implementation
An alert correlates rising memory, OOM, restarts, and request errors by service and release. The runbook checks host pressure before restart.

## Q&A
- **Q: Does docker stats provide history?** No; export to a time-series system.
- **Q: What does restart count indicate?** A symptom to correlate with exit, host, and application signals.
- **Q: Should every metric page?** No; alert on actionable service conditions.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/engine/containers/runmetrics/)
- [Docker documentation](https://docs.docker.com/engine/containers/resource_constraints/)
