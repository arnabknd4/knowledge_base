# Objective 152: Distinguish Core Kubernetes Apis From Ecosystem

## Exact syllabus objective

> Distinguish core Kubernetes APIs from ecosystem add-ons such as CNI plugins, ingress controllers, service meshes, secret backends, and custom controllers. [Core]

**Syllabus area:** 7) Production nuances and anti-patterns to remember<br>
**Role relevance:** Core operators; DevOps; SRE; Platform; Architect<br>
**Study path:** Production nuances and anti-patterns → production-nuances-and-anti-patterns-to

## What

Core APIs define contracts; distributions and ecosystem controllers implement networking, ingress/gateway, storage, policy, secret integration, runtime, and cloud behavior. Managed-service ownership and optional capability must be verified for the selected version/provider.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

Assuming an API is enforced or a managed service owns all operational work creates gaps. CNI, controller, node, cloud IAM, and backup boundaries are material design inputs.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

For each capability record API, implementation/version, owner, semantics, failure mode, support contract, upgrade path, and test evidence. Check the current CNCF blueprint/version separately for exam preparation.

**Objective-specific architect checkpoint:** Name the installed Ingress/Gateway controller, served API version, owner/route attachment and supported features; an API object alone does not implement TLS or traffic forwarding.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

Core API versus implementation; CNI policy semantics; controller-specific routing; provider shared responsibility; optional runtime controls; extension lifecycle.

**Role lens:** Core operators; DevOps; SRE; Platform; Architect should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```sh
kubectl get networkpolicy -A
kubectl get ingress,gateway,httproute -A
kubectl get csidrivers
```
Discovery does not prove feature enforcement, conformance, or a provider SLA.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Validate implementation documentation and behavior, test policy in-cluster, and revisit boundaries during upgrades.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Do not infer enforcement from API presence or delegate workload security, backup, monitoring, or incident readiness merely because control plane is managed.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

Before tenant onboarding, the platform team verifies CNI policy behavior, Gateway controller ownership, storage snapshot support, and publishes a responsibility matrix.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: Does Kubernetes core provide all add-ons?** No. **Q: Can this library determine CKA scope?** No; verify the current official CNCF blueprint.

## CKA alignment (separate from the role syllabus)

- **Services & Networking** — 20% (adjacent topic).

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
- [kubernetes.io/docs/concepts/services-networking/gateway](https://kubernetes.io/docs/concepts/services-networking/gateway/)
- [kubernetes.io/docs/setup/production-environment](https://kubernetes.io/docs/setup/production-environment/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
