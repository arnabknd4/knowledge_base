# Publish immutable identifiers and capture build metadata, SBOM, and provenance

**Domain:** CI/CD and release engineering<br>
**Syllabus objective:** [Publish immutable identifiers and capture build metadata, SBOM, and provenance](../../../copilot-docker-syllabus.md)<br>
[Domain index](../../index.md)

## What
A release needs stable identity and evidence about its build. Publish a human-friendly version for navigation, but deploy by digest; generate an SBOM and provenance linked to the exact artifact.

## Why
Tags can be mutable. Digest identity supports promotion; metadata helps vulnerability triage, dependency analysis, and supply-chain policy decisions.

## How
Push the candidate, resolve its manifest digest, generate SBOM/provenance in the trusted build, and retain source revision, builder identity, scan results, and policy decision. Verify evidence before release.

## Features
Buildx can generate SBOM and provenance attestations. Their presence alone does not prove trust; define trust roots, verification policy, and protected publishing.

## Code snippets (if any)
```sh
docker buildx build --push --tag registry.example/app:1.4.0 --sbom=true --provenance=mode=max .
```

## Do's and Don'ts
Do: retain digest-linked evidence and verify signer/builder policy. Don’t: infer integrity from a tag or treat metadata as automatically verified.

## Real-life implementation
A release record links source commit to builder run, digest, scan and attestations, then deployment. Admission rejects missing or untrusted evidence.

## Q&A
- **Q: Why deploy by digest?** It selects exact content.
- **Q: Does an SBOM prove safety?** No; it describes components.
- **Q: Is provenance self-authenticating?** No; verify issuer, builder, signature, and source under policy.

### Official Docker documentation
- [Docker documentation](https://docs.docker.com/build/metadata/attestations/)
- [Docker documentation](https://docs.docker.com/build/metadata/attestations/sbom/)
- [Docker documentation](https://docs.docker.com/build/metadata/attestations/slsa-provenance/)
