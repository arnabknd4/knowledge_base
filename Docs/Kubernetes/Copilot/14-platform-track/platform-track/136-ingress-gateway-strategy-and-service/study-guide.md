# Objective 136: Ingress Gateway Strategy And Service Exposure

## Exact syllabus objective

> Ingress/Gateway strategy and service exposure policy [Platform]

**Syllabus area:** 4.3 Platform track<br>
**Role relevance:** Platform; security; developer-experience teams<br>
**Study path:** Platform track → platform-track

## What

Kubernetes defines a Pod networking contract; actual routing, IPAM, encapsulation, policy enforcement, and service forwarding come from chosen implementations. CNI is an integration boundary, not a single universal data plane.

Apply this operating model to the exact objective above. Separate Kubernetes API behavior from the selected distribution, controller, CNI/CSI driver, runtime, and cloud-provider implementation.

## Why

NetworkPolicy enforcement varies by CNI and configuration. Design must state address allocation, routing, MTU, egress, policy, failure modes, and cloud-network interaction.

For architecture decisions, record assumptions, failure domains, control owners, durability, and service outcomes—not only feature names.

## How

Map Pod, Service, node, and external paths; identify the CNI and supported capabilities; validate routes and MTU; test DNS, service forwarding, and policy from representative namespaces/nodes.

**Objective-specific architect checkpoint:** Name the installed Ingress/Gateway controller, served API version, owner/route attachment and supported features; an API object alone does not implement TLS or traffic forwarding.

**Safe practice:** begin with read-only discovery in a disposable/lab cluster. Confirm `kubectl config current-context` and namespace before a write; use an authorized change window and environment-specific procedure for production.

## Features

Pod IP allocation; cluster routing; CNI lifecycle; Service virtual-IP forwarding; optional eBPF/proxy alternatives; implementation-specific network policy.

**Role lens:** Platform; security; developer-experience teams should explain the trade-off, show operational evidence, and state the ownership boundary—not merely name an API.

## Code snippets (if any)

```sh
kubectl get pods -A -o wide
kubectl get svc,endpointslices -A
kubectl get networkpolicy -A
```
An API object does not prove the selected CNI enforces its semantics.

Examples are illustrative. Substitute approved images, versions, namespaces, identities, and plugin settings; inspect rendered changes before applying.

## Do's and Don'ts

**Do**
- Record CNI/version, policy semantics, IP capacity, MTU, upgrade plan, and provider boundaries. Test the actual dataplane.
- Validate behavior and failure recovery on the actual distribution and plugin/controller versions.

**Don't**
- Do not assume every plugin implements NetworkPolicy equally or that kube-proxy always provides service forwarding.
- Do not copy a lab mutation to production without authorization, review, and a recovery plan.

## Real life implementation

The design review verifies the selected CNI implements required policy, tests it across node pools, and reserves Pod CIDR/routing capacity with the cloud team.

**Acceptance evidence:** a reviewed design/runbook, observed healthy state, tested failure or rollback path, and named owner. For managed clusters, verify the provider contract; managed control planes do not automatically transfer application, policy, identity, monitoring, data-protection, capacity, or incident responsibilities.

## Q&A

**Q: Is CNI itself the cluster network?** It is an integration/plugin ecosystem; actual behavior depends on implementation. **Q: Does policy YAML guarantee isolation?** Only if the deployed network implementation enforces it.

## CKA alignment (separate from the role syllabus)

- **Services & Networking** — 20% (adjacent topic).

A role-track label is not an official CKA domain. The adjacent mapping is topic-level only; verify the current CNCF blueprint and version.

Official certification reference: [CNCF CKA](https://www.cncf.io/training/certification/cka/). Verify its current blueprint and version before exam preparation.

## Official references

- [kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
- [kubernetes.io/docs/concepts/services-networking/network-policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [kubernetes.io/docs/concepts/services-networking](https://kubernetes.io/docs/concepts/services-networking/)

[Domain index](../../index.md) · [Source syllabus](../../../copilot-Kubernetes-syllabus.md)
