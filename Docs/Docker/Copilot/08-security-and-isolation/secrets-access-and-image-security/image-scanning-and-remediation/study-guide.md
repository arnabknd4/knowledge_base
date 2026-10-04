# Scan images, prioritize vulnerabilities, and rebuild maintained artifacts

## What
Image scanning identifies known vulnerabilities in packages or image contents against a vulnerability database; it does not prove an image is secure.

## Why
Prioritized remediation reduces exposure while avoiding unstructured upgrades that destabilize workloads. Rebuilds ensure patched dependencies reach deployed artifacts.

## How
Scan the exact release digest, triage severity with exploitability and exposure context, set remediation deadlines, rebuild from maintained bases, and verify the replacement artifact before promotion.

## Features
Scanner results depend on database freshness and package metadata. Fixing a source manifest does not change a deployed image until rebuilt and redeployed; document accepted risk and expiry.

## Code snippets (if any)
```console
docker scout cves nginx:alpine
```

## Do's and Don'ts
- **Do:** Verify access, failure behavior, and data lifecycle on the target.
- **Do:** Assign an owner and a measurable verification criterion.
- **Don't:** Assume parsing or startup proves readiness, safety, or suitability.
- **Don't:** Grant broader access or retain data beyond the workload's need.

## Real-life implementation
A critical finding in a public-facing image triggers an emergency rebuild and staged rollout. The team verifies the deployed digest and tracks any incompatible dependency update.

## Q&A
- **Q: Is containerization sufficient isolation?** No. Containers share a kernel; apply layered controls.
- **Q: Where should I start?** Limit daemon, runtime, image, mount, and network trust.
- **Q: How do I verify a control?** Inspect effective settings and test on the target host.

Source: [Official Docker documentation](https://docs.docker.com/scout/). [Syllabus](../../../copilot-docker-syllabus.md) · [Domain index](../../index.md)
