# Verify image provenance and signatures according to organizational policy

## What
Provenance describes how an image was built; signatures bind an identity to an artifact or its metadata. Verification evaluates those claims against an explicit trust policy.

## Why
A known registry location or tag alone does not establish who built an artifact or whether it corresponds to reviewed source.

## How
Define trusted builders and identities, preserve attestations with immutable image digests, enforce verification before deployment, and document exceptions and key or identity rotation.

## Features
Verification tooling and policy depend on the supply-chain system in use; Docker Scout attestation commands are experimental. Listing metadata does not itself verify signer trust or prove the source and build were safe.

## Code snippets (if any)
```console
docker scout attestation list --predicate-type https://slsa.dev/provenance/v1 example/app:1.0
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
Before promotion, CI verifies the expected builder identity and source revision for an image digest. A missing or invalid attestation blocks release and creates an auditable exception path.

## Q&A
- **Q: Is containerization sufficient isolation?** No. Containers share a kernel; apply layered controls.
- **Q: Where should I start?** Limit daemon, runtime, image, mount, and network trust.
- **Q: How do I verify a control?** Inspect effective settings and test on the target host.

Source: [Official Docker documentation](https://docs.docker.com/reference/cli/docker/scout/attestation/list/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
