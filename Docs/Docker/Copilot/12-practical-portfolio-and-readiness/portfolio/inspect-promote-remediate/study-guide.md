# Inspect and promote an image by digest

Portfolio exercise: Demonstrate image inspection, digest-based promotion, vulnerability review, SBOM/provenance capture, and a documented remediation decision.

## What

Tie an inspected image to its immutable digest, component inventory, provenance, and risk decision.

## Why

Tags can move and findings need context; traceable evidence supports promotion and remediation.

## How

Inspect metadata and digest, generate or retrieve SBOM/provenance, review vulnerabilities, record remediation or exception, and promote the same digest. Recheck destination identity.

## Features

SBOM coverage, provenance trust, scan coverage, and verification depend on configured tools.

## Code snippets (if any)

No snippet required: tool and registry commands vary; never include credentials in logs.

## Do's and Don'ts

DO use a disposable environment, state assumptions, capture evidence, and assign follow-up ownership. DON’T use production data or credentials, infer safety from one passing check, or leave temporary resources behind.

## Real-life implementation

Use an authorized sample image. Produce evidence linking source, digest, scan, SBOM/provenance, and a finding decision; state limitations and protect private metadata.

## Q&A

- Why promote by digest? It preserves tested artifact identity.
- Does an SBOM detect vulnerabilities? No; it inventories components.
- Must every finding block release? Apply documented risk policy and record exceptions.

### Official Docker references

- [Official Docker documentation](https://docs.docker.com/build/metadata/attestations/)
- [Official Docker documentation](https://docs.docker.com/scout/)

[Back to domain index](../../index.md) · [Syllabus](../../../copilot-docker-syllabus.md)
