# Authenticate to registries with short-lived or tightly scoped credentials

**Domain:** CI/CD and release engineering<br>
**Syllabus objective:** [Authenticate to registries with short-lived or tightly scoped credentials](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
Registry credentials let a pipeline read or publish images. Prefer workload identity or short-lived credentials; otherwise use dedicated, revocable credentials limited to the required repository and actions.

## Why
CI logs, artifacts, or compromised dependencies can expose credentials. Excess scope turns a build compromise into broad image or account access.

## How
Separate pull from publish credentials, store them in the CI secret facility, mask output, limit job permissions and lifetime, and authenticate only just before registry operations. Rotate and audit access.

## Features
Docker credential helpers and docker login --password-stdin avoid placing a token in command-line arguments. Masking does not replace access controls.

## Code snippets (if any)
```sh
printf "%s" "$REGISTRY_TOKEN" | docker login registry.example --username "$REGISTRY_USER" --password-stdin
```

## Do's and Don'ts
Do: use scoped, revocable credentials and never echo them. Don’t: commit secrets, put them in Dockerfile ARG/ENV, persist credentials in artifacts, or share deploy credentials with PR jobs.

## Real-life implementation
A release identity can push to one repository but cannot administer the registry. PR checks have pull-only access; deployment uses a separate identity.

## Q&A
- **Q: Is masking enough?** No; also scope access and lifetime.
- **Q: Why separate read/write?** Limit damage from compromised test jobs.
- **Q: What improves with password-stdin?** It avoids process arguments, but storage must still be secure.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/reference/cli/docker/login/)
- [Docker documentation](https://docs.docker.com/docker-hub/access-tokens/)
