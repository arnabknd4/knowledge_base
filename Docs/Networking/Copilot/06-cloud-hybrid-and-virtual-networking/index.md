# 06. Cloud, hybrid, and virtual networking

Architect-level, objective-mapped guides for this domain. Each checkbox is represented once. See the [source syllabus](../copilot-Networking-syllabus.md).

## Provider-independent design

- [Map VPC/VNet and subnet constructs to IP ranges, route tables, gateways, security controls, and regional/zone boundaries.](provider-independent-design/043-map-vpc-vnet-and-subnet-constructs-to-ip-ran/study-guide.md) — Core; P1; roles D/P/S/A.
- [Explain internet ingress/egress, NAT, private endpoints/service endpoints, peering, transit/hub-and-spoke, and their routing and security implications.](provider-independent-design/044-explain-internet-ingress-egress-nat-private/study-guide.md) — Core; P1; roles D/P/S/A.
- [Compare VPN tunnels and dedicated private connectivity (for example, Direct Connect, ExpressRoute, and Cloud Interconnect); reason about redundancy, routing, throughput, and failover.](provider-independent-design/045-compare-vpn-tunnels-and-dedicated-private-co/study-guide.md) — Role extension; P2; roles D/P/S/A.
- [Plan hybrid DNS, address allocation, overlapping CIDRs, transitive routing, centralized inspection, shared services, and ownership boundaries.](provider-independent-design/046-plan-hybrid-dns-address-allocation-overlappi/study-guide.md) — Role extension; P2; roles A/P.
- [Compare centralized and decentralized network governance; document trade-offs in autonomy, security, operations, scaling, and cost.](provider-independent-design/047-compare-centralized-and-decentralized-networ/study-guide.md) — Role extension; P2; roles A.
- [Review provider-specific equivalents across at least two clouds without assuming service names imply identical behavior or limits.](provider-independent-design/048-review-provider-specific-equivalents-across/study-guide.md) — Role extension; P2; roles D/P.
- [Understand edge connectivity, private service publishing/consumption, multi-cloud transit patterns, and provider-specific routing constraints when the architecture requires them.](provider-independent-design/049-understand-edge-connectivity-private-service/study-guide.md) — Role extension; P3; roles A/S.
- [Draw a cloud/hybrid data-flow diagram that identifies CIDRs, route propagation, trust boundaries, DNS path, egress, and failure domains.](provider-independent-design/050-draw-a-cloud-hybrid-data-flow-diagram-that-i/study-guide.md) — Practical; P2; roles D/P/S/A.

## SDN, overlays, and virtualization

- [Explain control plane versus data plane, SDN intent/policy, underlay versus overlay, and why virtual network abstractions still depend on physical transport.](sdn-overlays-and-virtualization/051-explain-control-plane-versus-data-plane-sdn/study-guide.md) — Role extension; P2; roles P/A.
- [Describe VXLAN and encapsulation conceptually; recognize MTU overhead, troubleshooting visibility, and scale/segmentation benefits.](sdn-overlays-and-virtualization/052-describe-vxlan-and-encapsulation-conceptuall/study-guide.md) — Role extension; P2; roles P/A.
- [Understand virtual interfaces, network namespaces, bridges, veth pairs, NAT, and packet-filtering hooks at a level useful for tracing container traffic.](sdn-overlays-and-virtualization/053-understand-virtual-interfaces-network-namesp/study-guide.md) — Role extension; P2; roles D/P.
- [Trace a sample packet through an overlay and name the metadata and observability needed to distinguish overlay, underlay, and policy failures.](sdn-overlays-and-virtualization/054-trace-a-sample-packet-through-an-overlay-and/study-guide.md) — Practical; P2; roles P/A.
