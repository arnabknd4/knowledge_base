# Objective 052: Know Coredns And How Cluster Dns Enables Stable

## Exact syllabus objective

> Know CoreDNS and how cluster DNS enables stable internal service discovery. [Core]

**Syllabus area:** 3.5 Services, networking, DNS, Ingress, Gateway, and CNI<br>
**Role relevance:** Core operators; DevOps; SRE; Platform; Architect<br>
**Study path:** Services, networking, DNS, Ingress, Gateway, and CNI → services-networking-dns-ingress-gateway-and

## What

Cluster DNS publishes service-discovery records and uses configured forwarding/search behavior. CoreDNS is common, but installation and configuration vary by distribution. Name resolution and packet reachability are separate steps.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

Applications may fail at DNS before routing is involved. Search paths, caching, upstream resolvers, and query saturation are operational dependencies.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Test a service FQDN from the caller's namespace; compare DNS answer to Service/EndpointSlice state; inspect DNS Pod health, policy, and forwarding using approved diagnostics.

**Objective-specific architect checkpoint:** Test FQDN resolution from the caller namespace, then separately verify Service selectors, EndpointSlices, routing, and policy; a DNS answer is not proof of reachability.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

Service and Pod records; namespace search paths; cluster DNS Service; upstream forwarding/caching; distribution-specific configuration.

**Role lens:** Core operators; DevOps; SRE; Platform; Architect should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```sh
kubectl get svc,endpointslices -n app
kubectl get pods -n kube-system -o wide
# In an approved diagnostic Pod: nslookup api.app.svc.cluster.local
```
Use sanctioned tools; do not install utilities into production workloads.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Monitor DNS latency/errors, query saturation and forwarding, and test from the actual caller context.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Do not infer a DNS failure from every connection error or modify CoreDNS without checking provider ownership.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

For a failed service call, SRE checks name resolution, EndpointSlices, TCP reachability, and policy as separate hops to locate the break.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: Does successful resolution prove reachability?** No; routing and policy still apply. **Q: Is CoreDNS guaranteed?** No; verify the cluster's implementation.

## CKA alignment (separate from the role syllabus)

- **Services & Networking** — 20%.

Topic-level study aid to the CKA domains and weights quoted by the syllabus, not a claim that every library objective is an exam item. Verify the current CNCF blueprint, domain wording, and version before planning certification study.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/services-networking/dns-pod-service](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
- [kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution](https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
