# Understand build context, target stages, platforms, build arguments, and provenance metadata.

## What

Build context supplies files; target chooses a stage; platform selects OS and architecture; build arguments parameterize a build; provenance records build claims. Record the commit, context, selected target, platform, arguments, and builder; inspect provenance as evidence, not as a guarantee of trusted inputs.

## Why

Readable tags simplify release operations, while digest pinning trades convenience for exact promotion and rollback identity.

## How

Record context revision, target stage, platform, non-secret arguments, builder version, and provenance policy; inspect generated metadata rather than treating it as proof.

## Features

Build arguments are not secrets. Provenance usefulness depends on trusted generation, source availability, builder settings, and registry support.

## Code snippets (if any)

```sh
docker buildx build --target runtime --platform linux/amd64 --tag app:dev --load .
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Omit target and platform from release records or use provenance as a substitute for trusted inputs.

## Real-life implementation

Release automation records a tag-to-digest mapping and promotes the verified digest through each environment.

## Q&A

- **What is the key concept?** Build context supplies files.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Omit target and platform from release records or use provenance as a substitute for trusted inputs.

**Official reference:** [Docker documentation](https://docs.docker.com/build/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
