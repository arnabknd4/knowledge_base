# Use `.dockerignore` to exclude credentials, local artifacts, VCS metadata, and unnecessary build context.

## What

The build context is the set of files available to the builder; .dockerignore excludes matching files before transfer and prevents accidental COPY access. Ignore files before transfer; this reduces context size and avoids accidental access to local secrets, but does not remove data from existing image layers.

## Why

Keeping credentials out of artifacts limits exposure through image distribution, layer history, build caches, and logs.

## How

Add exclusions for VCS metadata, credentials, local dependencies, and build output; review COPY instructions and build from a clean checkout.

## Features

Context hygiene improves build speed and reduces exposure to local credentials or artifacts. Ignore rules do not remove files already committed in prior image layers.

## Code snippets (if any)

```sh
docker build --progress=plain --tag app:dev .
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Send the entire workstation tree to a remote builder or assume ignore rules erase secrets already present in old layers.

## Real-life implementation

CI supplies a short-lived credential only to the required step and scans build outputs for accidental disclosure.

## Q&A

- **What is the key concept?** The build context is the set of files available to the builder.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Send the entire workstation tree to a remote builder or assume ignore rules erase secrets already present in old layers.

**Official reference:** [Docker documentation](https://docs.docker.com/build/concepts/dockerfile/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
