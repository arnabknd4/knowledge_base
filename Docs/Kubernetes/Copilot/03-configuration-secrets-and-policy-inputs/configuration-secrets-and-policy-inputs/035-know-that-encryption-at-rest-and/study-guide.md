# Objective 035: Know That Encryption At Rest And Secret

## Exact syllabus objective

> Know that encryption at rest and secret protection are separate concerns from application-level secret handling. [Architect]

**Syllabus area:** 3.3 Configuration, Secrets, and policy inputs<br>
**Role relevance:** Architect; platform leadership; SRE<br>
**Study path:** Configuration, Secrets, and policy inputs → configuration-secrets-and-policy-inputs

## What

Authentication identifies a caller; authorization decides permitted API actions; admission validates or mutates objects. RBAC, workload identity, Pod security, network controls, image provenance, and audit each address different risks.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

Namespaces and Secret objects are not sufficient security in isolation. Overbroad permissions, privileged workloads, weak provenance, untested policies, and unclear cloud identity boundaries can compound into cluster compromise.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Threat-model identities and boundaries; use least-privilege RBAC; enforce Pod Security Standards/admission; control artifacts; audit changes; test deny and break-glass paths. Treat runtime controls and secret backends as implementation-specific.

**Objective-specific architect checkpoint:** Review API-data encryption, key custody, key rotation/recovery, backups, and application-level secret handling as distinct controls.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

Authentication providers; Roles/ClusterRoles and bindings; service accounts; admission; Pod Security; audit; runtime and supply-chain ecosystem controls.

**Role lens:** Architect; platform leadership; SRE should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata: {name: pod-reader, namespace: app}
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
```
Bind only to intended identities; review effective access before applying.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Scope permissions, protect secrets and backups, use policy tests and audit retention, and define provider/customer responsibility boundaries.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Do not grant workloads cluster-admin or rely on base64, namespace names, or image tags alone as security controls.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

Tenant onboarding provisions scoped identity, quotas, Pod Security, image policy, and default-deny network rules only after confirming CNI enforcement.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: Is admission the same as authorization?** No; admission validates/mutates an authorized request. **Q: Does RBAC isolate network traffic?** No.

## CKA alignment (separate from the role syllabus)

- **Adjacent: Workloads & Scheduling (15%) / Cluster Architecture, Installation & Configuration (25%)** — not a separate domain in the cited list.

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/security](https://kubernetes.io/docs/concepts/security/)
- [kubernetes.io/docs/reference/access-authn-authz/rbac](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [kubernetes.io/docs/reference/access-authn-authz/admission-controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)
- [kubernetes.io/docs/concepts/security/pod-security-standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
