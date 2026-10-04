# Control interpolation, environment files, profiles, project names, and overrides

## What
Compose resolves variables, environment files, profiles, project names, and merged Compose files to form the effective application model.

## Why
Explicit configuration layering supports different developer and CI needs without building environment-specific images. Predictable project naming also avoids resource collisions on shared hosts.

## How
Use interpolation for non-secret settings, inspect the resolved model with `docker compose config`, select optional services with profiles, and specify project identity deliberately. Keep override files small and review merge results.

## Features
An unset interpolation variable may become empty or produce a warning depending on expression form. `env_file` supplies container environment; it is not a secure secret store. Merge and profile behavior should be tested with the installed Compose version.

## Code snippets (if any)
```console
docker compose --project-name sample --profile debug config
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A developer enables a mail catcher profile locally, while CI uses a distinct project name and a test override. The pipeline validates the rendered configuration before creating resources.

## Q&A
- **Q: How do I validate it?** Render the model, then smoke-test the target implementation.
- **Q: What does Compose not provide?** Multi-host scheduling or cluster-level failover.
- **Q: How can I limit surprises?** Pin supported versions and rehearse failure and recovery.

Source: [Official Docker documentation](https://docs.docker.com/compose/how-tos/environment-variables/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
