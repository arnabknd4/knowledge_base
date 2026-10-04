# CI/CD and release engineering

[Parent index](../README.md) · [Docker syllabus](../copilot-docker-syllabus.md)

Objective-level study guides:

## Build and test pipelines

- [Build in CI with a controlled builder and versioned context](./build-and-test-pipelines/controlled-builder-versioned-context/study-guide.md)
- [Test the built artifact at unit, integration, and image levels](./build-and-test-pipelines/test-built-artifact/study-guide.md)
- [Use build cache without letting untrusted builds poison trusted release caches](./build-and-test-pipelines/safe-build-cache/study-guide.md)
- [Authenticate to registries with short-lived or tightly scoped credentials](./build-and-test-pipelines/registry-authentication/study-guide.md)
- [Publish immutable identifiers and capture build metadata, SBOM, and provenance](./build-and-test-pipelines/immutable-release-metadata/study-guide.md)
- [Separate pull-request validation from privileged release and deployment workflows](./build-and-test-pipelines/separate-validation-release-workflows/study-guide.md)

## Release promotion and rollback

- [Test rollback and recovery; account for data and schema changes](./release-promotion-and-rollback/test-rollback-and-recovery/study-guide.md)
- [Promote a tested image through environments by digest](./release-promotion-and-rollback/promote-tested-digest/study-guide.md)
- [Define approvals, policy checks, sequencing, health validation, and rollback criteria](./release-promotion-and-rollback/release-approval-sequencing-health-rollback/study-guide.md)
- [Maintain traceability from source revision to build, digest, evidence, and deployment](./release-promotion-and-rollback/traceable-release-chain/study-guide.md)
- [Define retention, cleanup, and incident response for compromised or vulnerable images](./release-promotion-and-rollback/image-retention-compromise-response/study-guide.md)
