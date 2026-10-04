# Objective 030: Know The Difference Between Environment

## Exact syllabus objective

> Know the difference between environment variables and mounted files. [Core]

**Syllabus area:** 3.3 Configuration, Secrets, and policy inputs<br>
**Role relevance:** Core operators; DevOps; SRE; Platform; Architect<br>
**Study path:** Configuration, Secrets, and policy inputs → configuration-secrets-and-policy-inputs

## What

ConfigMaps carry non-confidential configuration. Secret resources carry sensitive values, but protection depends on API authorization, encryption-at-rest configuration, delivery, and provider safeguards. Environment and mounted-file injection have different update behavior.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

Secret and configuration lifecycles differ. A Secret object alone is not a complete secrets-management system; sensitive values require least privilege, rotation, auditability, and controlled propagation.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Separate confidential and ordinary values; scope service-account access; choose env/file injection deliberately; plan how changes trigger reload or rollout. Use approved external-secret integrations where centralized rotation or external KMS-backed storage is required.

**Objective-specific architect checkpoint:** Choose env versus mounted-file delivery based on reload and exposure behavior; separate non-secret config, least-privileged credentials, at-rest protection, rotation, and external-store ownership.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

Namespaced ConfigMap/Secret APIs; data keys and mounts; imagePullSecrets; projected service-account credentials; updates that may require application reload.

**Role lens:** Core operators; DevOps; SRE; Platform; Architect should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```yaml
apiVersion: v1
kind: ConfigMap
metadata: {name: app-config, namespace: app}
data:
  LOG_LEVEL: info
```
Never commit live credentials; configure Secret delivery separately.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Enable appropriate encryption at rest, protect backups, audit reads, restrict RBAC, rotate credentials, and prevent values entering logs.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Base64 is encoding, not encryption. Do not mount every secret into every Pod or assume environment variables refresh in a running process.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

A platform injects ordinary settings from a ConfigMap and syncs credentials from an approved vault integration. Rotation triggers a controlled rollout; old credentials are revoked after verification.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: Are Secret values encrypted by base64?** No. **Q: Do ConfigMap environment variables refresh automatically?** No; reload or recreate according to the application and injection method.

## CKA alignment (separate from the role syllabus)

- **Adjacent: Workloads & Scheduling (15%) / Cluster Architecture, Installation & Configuration (25%)** — not a separate domain in the cited list.

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/configuration/configmap](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [kubernetes.io/docs/concepts/configuration/secret](https://kubernetes.io/docs/concepts/configuration/secret/)
- [kubernetes.io/docs/concepts/security/secrets-good-practices](https://kubernetes.io/docs/concepts/security/secrets-good-practices/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
