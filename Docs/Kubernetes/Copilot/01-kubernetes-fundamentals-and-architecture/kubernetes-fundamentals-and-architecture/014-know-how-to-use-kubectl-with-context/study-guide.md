# Objective 014: Know How To Use Kubectl With Context Switching

## Exact syllabus objective

> Know how to use kubectl with context switching, explain, dry-run, and resource output filters. [Core]

**Syllabus area:** 3.1 Kubernetes fundamentals and architecture<br>
**Role relevance:** Core operators; DevOps; SRE; Platform; Architect<br>
**Study path:** Kubernetes fundamentals and architecture → kubernetes-fundamentals-and-architecture

## What

Resources are versioned API objects identified by group, version, kind, scope, and metadata. kubectl resolves a context and credentials, calls the API, and renders results; it is a client, not the source of truth.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

Explicit API discovery and target checks prevent schema mistakes and accidental writes to the wrong cluster. Client-side success does not establish that admission, scheduling, or runtime will succeed.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Check current context and namespace; discover kinds and served versions; use `explain` and server-side dry-run; review diffs before applying. Use JSONPath/custom-columns for scripts rather than parsing human-formatted output.

**Objective-specific architect checkpoint:** Discover the served resource and scope, confirm the target context, use `kubectl explain`, server-side dry-run and diff, and validate structured output without exposing credentials.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

Contexts; API discovery; schema help; dry-run; declarative apply; output filters; API versioning and deprecation.

**Role lens:** Core operators; DevOps; SRE; Platform; Architect should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```sh
kubectl config current-context
kubectl api-resources
kubectl explain deployment.spec.template.spec
kubectl apply --dry-run=server -f app.yaml
```

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Pin context/namespace in automation, use least-privileged credentials, validate against the target API, and review rendered changes.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Do not expose credentials in shell history or perform destructive writes before checking context. Dry-run is not proof of runtime health.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

A delivery job validates manifests against the target API with a namespace-scoped identity, reviews a diff, then checks rollout status and application health.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: What does `kubectl explain` prove?** Schema documentation, not admission or runtime success. **Q: Why server-side dry-run?** It exercises server validation/admission without persisting the object.

## CKA alignment (separate from the role syllabus)

- **Cluster Architecture, Installation & Configuration** — 25%.

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/reference/kubectl](https://kubernetes.io/docs/reference/kubectl/)
- [kubernetes.io/docs/concepts/overview/kubernetes-api](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
