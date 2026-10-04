# Understand volume ownership/permissions, mount propagation, host-path coupling, and data lifecycle

## What

Mounted data retains filesystem ownership and mode semantics. Container UID/GID may differ from host files; bind mounts expose host paths, and propagation shares nested mount events. Lifecycle includes migration, retention, deletion, and recovery.

## Why

State the tradeoff and assign operational ownership.

## How

Use a deliberate non-root identity, provision ownership, and test as the deployed user. Prefer read-only consumer mounts. Treat propagation as advanced host coupling, only for required nested mounts.

## Features

UID/GID numbers, ACLs, SELinux labels, user namespaces, and Desktop file sharing affect behavior.

## Code snippets (if any)

```bash
docker run --rm --user 10001:10001 --mount type=volume,src=app-data,dst=/data alpine:3.20 sh -c 'id; test -w /data'
```

## Do's and Don'ts

- **Do:** document expected UID/GID, access mode, migration owner, and deletion approval; test with production-like identity.
- **Don't:** solve permission errors by running privileged or recursively making sensitive host directories world-writable.

## Real-life implementation

A service starts as UID 10001, a provisioning job sets only its data directory ownership, and read-only replicas mount data read-only when the storage/application model allows.

## Q&A

- **Q: Why can a mount be unwritable?** The process UID/GID, host ownership, ACL, label, or driver policy may not grant access.
- **Q: What is mount propagation for?** Sharing nested mount/unmount events across mount namespaces in specific host-integrated designs.
- **Q: Should recursive chmod be the default fix?** No; identify the exact identity and grant the minimum required access.

**Docs:** [Docker](https://docs.docker.com/engine/storage/)

**Local:** [Syllabus](../../../copilot-docker-syllabus.md) · [Index](../../index.md)
