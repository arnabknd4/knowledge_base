# Control log volume, retention, sensitive fields, and access

**Domain:** Observability, reliability, and incident response<br>
**Syllabus objective:** [Control log volume, retention, sensitive fields, and access](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Logging is a governed data pipeline. Define useful events, volume bounds, retention, redaction, access, and response to destination failure.

## Why
Uncontrolled logs consume disk, obscure signals, expose sensitive data, and create compliance risks. Retention also affects investigation and legal obligations.

## How
Set severity and sampling, driver limits/rotation, central retention tiers, auditing, and redaction tests. Alert on queue, disk, and ingestion saturation; define safe behavior during collector outage.

## Features
Docker driver options bound local behavior, but delivery and rotation differ by driver. Central retention and application redaction remain necessary.

## Code snippets (if any)
```sh
docker run --log-opt max-size=10m --log-opt max-file=3 registry.example/api:release
```

## Do's and Don'ts
Do: minimize sensitive fields and test redaction. Don’t: rely on default retention, assume local rotation governs central storage, or disable logging blindly.

## Real-life implementation
A service uses structured logs, restricts debug verbosity to approved windows, rotates local fallback logs, and retains security events longer under restricted access.

## Q&A
- **Q: Does rotation equal retention?** No; configure local and central policies separately.
- **Q: Can logs include user data?** Minimize and protect only necessary approved data.
- **Q: What if logs fill disk?** Bound buffers and restore collection using a runbook.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/engine/logging/configure/)
- [Docker documentation](https://docs.docker.com/engine/logging/drivers/)
