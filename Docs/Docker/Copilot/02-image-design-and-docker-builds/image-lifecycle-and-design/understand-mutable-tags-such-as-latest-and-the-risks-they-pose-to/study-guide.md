# Understand mutable tags such as `latest` and the risks they pose to rollback and repeatable deployment.

## What

A tag is a mutable registry name; latest has no built-in promise of recency or stability. A digest identifies exact content for repeatable promotion and rollback. Tags can move, including latest, which has no inherent freshness or stability guarantee. Deploy by digest when exact artifact identity is required.

## Why

Readable tags simplify release operations, while digest pinning trades convenience for exact promotion and rollback identity.

## How

Use explicit release tags for discovery, enforce registry immutability where appropriate, and deploy by a recorded digest for exact rollback.

## Features

Release tags aid discovery, while digest references pin content. Multi-platform tags may resolve to an image index with platform-specific manifests.

## Code snippets (if any)

```sh
docker image inspect alpine:3.21 --format "{{index .RepoDigests 0}}"
```

## Do's and Don'ts

**Do**
- Use least privilege; keep secrets and persistent data out of image layers.

**Don't**
- Use latest as a promotion or rollback identifier.

## Real-life implementation

Release automation records a tag-to-digest mapping and promotes the verified digest through each environment.

## Q&A

- **What is the key concept?** A tag is a mutable registry name.
- **How should I validate it?** Follow the practical steps above and inspect behavior on the target platform.
- **What must I avoid?** Use latest as a promotion or rollback identifier.

**Official reference:** [Docker documentation](https://docs.docker.com/build/building/best-practices/)

[Back to syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
