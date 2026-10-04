# 07. Containers and Kubernetes networking

Architect-level, objective-mapped guides for this domain. Each checkbox is represented once. See the [source syllabus](../copilot-Networking-syllabus.md).

## Container and Kubernetes networking

- [Explain container network namespaces, interfaces, bridge/overlay concepts, port publishing, and how container networking differs from a VM's default network.](container-and-kubernetes-networking/055-explain-container-network-namespaces-interfa/study-guide.md) — Core; P1; roles D/P/S.
- [Explain the Kubernetes network model: Pod-to-Pod, Pod-to-Service, and external-to-Service connectivity; distinguish the Kubernetes API model from its implementation.](container-and-kubernetes-networking/056-explain-the-kubernetes-network-model-pod-to/study-guide.md) — Core; P1; roles D/P/S.
- [Explain CNI plugin responsibilities, node/pod/service CIDRs, IPAM, kube-proxy or an alternative service data plane, and cluster DNS.](container-and-kubernetes-networking/057-explain-cni-plugin-responsibilities-node-pod/study-guide.md) — Core; P1; roles D/P/S.
- [Compare ClusterIP, NodePort, LoadBalancer, Ingress, and Gateway API use cases; understand EndpointSlices and health/readiness effects.](container-and-kubernetes-networking/058-compare-clusterip-nodeport-loadbalancer-ingr/study-guide.md) — Core; P1; roles D/P/S.
- [Explain NetworkPolicy intent and enforcement dependencies; know that policy behavior depends on the network plugin and configured policy capabilities.](container-and-kubernetes-networking/059-explain-networkpolicy-intent-and-enforcement/study-guide.md) — Core; P1; roles D/P/S.
- [Troubleshoot service discovery, pod-to-pod and pod-to-external traffic, DNS, egress, MTU, SNAT, conntrack, and address exhaustion.](container-and-kubernetes-networking/060-troubleshoot-service-discovery-pod-to-pod-an/study-guide.md) — Role extension; P2; roles P/S.
- [Plan dual-stack clusters, non-overlapping address pools, multi-cluster connectivity, service exposure, and network-policy governance.](container-and-kubernetes-networking/061-plan-dual-stack-clusters-non-overlapping-add/study-guide.md) — Role extension; P2; roles P/A.
- [Evaluate service-mesh data paths, sidecar or ambient proxying, mTLS, retries, and observability overhead; distinguish mesh behavior from the underlying network.](container-and-kubernetes-networking/062-evaluate-service-mesh-data-paths-sidecar-or/study-guide.md) — Role extension; P2; roles S/A.
- [Know that Kubernetes networking details can differ by operating system and implementation; validate CNI, host-network, and policy support for Windows nodes rather than assuming Linux behavior.](container-and-kubernetes-networking/063-know-that-kubernetes-networking-details-can/study-guide.md) — Role extension; P2; roles D/P.
- [Deploy or inspect a small cluster workload; verify name resolution and each connectivity path, then apply a policy and confirm both allowed and denied flows.](container-and-kubernetes-networking/064-deploy-or-inspect-a-small-cluster-workload-v/study-guide.md) — Practical; P1; roles D/P/S.
