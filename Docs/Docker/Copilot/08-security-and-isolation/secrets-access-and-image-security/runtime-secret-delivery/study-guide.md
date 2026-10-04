# Deliver secrets at runtime without baking them into images or build output

## What
A secret is sensitive runtime data such as a password or token. It should be supplied through a dedicated secret facility or runtime-mounted secret mechanism appropriate to the target.

## Why
Image layers, build arguments, environment inspection, logs, and shell history can expose credentials long after a deployment. Secret separation supports rotation and narrower access.

## How
Keep secret values out of Dockerfiles, `ARG`, `ENV`, committed Compose files, and logs. Grant runtime access only to consuming services, rotate credentials, and validate file permissions and lifecycle.

## Features
BuildKit has dedicated build-secret mounts for build-time needs; they differ from runtime secrets. Compose secret support differs across local and Swarm contexts. Do not assume standalone Engine has Swarm secret semantics.

## Code snippets (if any)
```yaml
services:
  app:
    image: example/app:1.0
    secrets: [db_password]
secrets:
  db_password:
    file: ./secrets/db_password.txt
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A service receives a pre-provisioned runtime secret file from its supported platform, while local development uses a disposable non-production credential. CI masks values and never prints rendered secret contents.

## Q&A
- **Q: Is containerization sufficient isolation?** No. Containers share a kernel; apply layered controls.
- **Q: Where should I start?** Limit daemon, runtime, image, mount, and network trust.
- **Q: How do I verify a control?** Inspect effective settings and test on the target host.

Source: [Official Docker documentation](https://docs.docker.com/compose/how-tos/use-secrets/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
