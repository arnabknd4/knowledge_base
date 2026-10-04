# Networking Syllabus for DevOps, Platform, SRE, and Architecture

**Status:** Role-oriented learning guide; reviewed against primary sources on October 4, 2026
**Audience:** DevOps engineers, platform engineers, SREs, and solution/infrastructure architects
**Purpose:** Build practical networking fluency for designing, deploying, securing, and operating modern hybrid and cloud-native systems.

> This is an independently assembled learning syllabus, not an official Cisco, cloud-provider, or certification exam blueprint. Priorities are learning guidance, not exam weightings. It builds on the local [Networking syllabus](../Syllabus.md), retaining its useful OSI/TCP-IP, addressing, switching, routing, security, wireless-awareness, design, and operations foundations while adding role-based practice and current cloud-native concerns. Legacy/classful material and vendor-specific command memorization are intentionally de-emphasized.

## How to use this syllabus

- Work through **P1** topics first. P2 and P3 extend depth and specialization.
- Each checkbox is a learning outcome or practical task; check it off when you can explain or demonstrate it without relying on rote definitions.
- Applicability tags identify the roles that benefit most: **DevOps**, **Platform**, **SRE**, and **Architect**. All roles should understand shared P1 fundamentals.
- Use vendor-neutral concepts first, then map them to your employer's cloud, network, operating systems, and tooling.

### Legend

- **Core** — baseline knowledge expected for the role(s) tagged.
- **Role extension** — depth useful for a particular role or environment; not a prerequisite for every learner.
- **Practical** — a lab, design exercise, or operational demonstration.
- **P1 / P2 / P3** — foundational / applied / advanced priority, not a percentage or exam weighting.
- Role abbreviations: **D** = DevOps, **P** = Platform, **S** = SRE, **A** = Architect.

## 1. Network models and performance fundamentals

### Concepts, boundaries, and service objectives

- [ ] **Core · P1 · D/P/S/A** — Explain the OSI and TCP/IP models, encapsulation, and how a real request crosses link, network, transport, and application layers.
- [ ] **Core · P1 · D/P/S/A** — Distinguish LAN, WAN, internet, data-center, virtual, and overlay networks; identify host, subnet, routing, and application boundaries.
- [ ] **Core · P1 · D/P/S/A** — Relate bandwidth, throughput, latency, jitter, loss, MTU, and retransmissions to application behavior and user impact.
- [ ] **Core · P1 · D/P/S/A** — Explain unicast, broadcast, and multicast at a conceptual level; distinguish a collision domain from a broadcast domain.
- [ ] **Role extension · P2 · S/A** — Translate availability, latency, and throughput requirements into measurable network SLOs, error budgets, and service-level dependencies.
- [ ] **Practical · P1 · D/P/S/A** — Trace a browser or service request from name resolution through connection setup, TLS, HTTP exchange, and response; label the responsible layer at each step.

## 2. Addressing, subnetting, and core protocols

### IP addressing and local delivery

- [ ] **Core · P1 · D/P/S/A** — Read and calculate IPv4 CIDR prefixes, subnet ranges, usable addresses, and route aggregation; plan non-overlapping address space for environments and growth.
- [ ] **Core · P1 · D/P/S/A** — Recognize private, public, loopback, link-local, and special-use IPv4 ranges; understand NAT/PAT purpose, trade-offs, and failure modes.
- [ ] **Core · P1 · D/P/S/A** — Explain IPv6 notation, prefix allocation, global and link-local addresses, neighbor discovery, SLAAC/DHCPv6 at a high level, and dual-stack considerations.
- [ ] **Core · P1 · D/P/S/A** — Explain MAC addresses, Ethernet frames, ARP for IPv4, IPv6 Neighbor Discovery, default gateways, and how a host chooses a next hop.
- [ ] **Core · P1 · D/P/S/A** — Interpret ports, sockets, ephemeral ports, and common transport/application protocol relationships.
- [ ] **Role extension · P2 · P/A** — Design IPAM and subnet allocation conventions for multi-environment, multi-account/subscription/project, and Kubernetes address pools.

### Transport, naming, configuration, and application protocols

- [ ] **Core · P1 · D/P/S/A** — Compare TCP and UDP; explain TCP connection establishment/teardown, reliability, retransmission, flow and congestion control, and what packet loss does to throughput.
- [ ] **Core · P1 · D/P/S/A** — Explain DNS resolution, caching/TTL, recursive versus authoritative service, zones, and common A/AAAA/CNAME/NS/PTR/TXT records.
- [ ] **Core · P1 · D/P/S/A** — Explain DHCP address leasing and the role of DNS and time synchronization in reliable service operation.
- [ ] **Core · P1 · D/P/S/A** — Explain HTTP request/response semantics, common status classes, connection reuse, proxies, and the effect of HTTP versions without memorizing wire-level details.
- [ ] **Core · P1 · D/P/S/A** — Describe TLS certificates, trust chains, hostname validation, SNI, certificate expiry/rotation, and the difference between encryption in transit and authorization.
- [ ] **Role extension · P2 · D/P/S** — Understand SSH, NTP, SMTP, and common API/service ports sufficiently to assess dependencies and troubleshoot connectivity.
- [ ] **Role extension · P2 · S/A** — Understand DNS failure patterns such as negative caching, split-horizon answers, stale records, and resolver-path differences.
- [ ] **Practical · P1 · D/P/S/A** — Inspect DNS answers, route/connection state, and an HTTPS certificate for a test endpoint; explain what each observation does and does not prove.

## 3. Switching, routing, and network paths

### LAN and routing fundamentals

- [ ] **Core · P1 · D/P/S/A** — Distinguish switches, routers, firewalls, gateways, access points, proxies, and load balancers by function rather than product name.
- [ ] **Role extension · P2 · A/P** — Explain VLANs, 802.1Q trunks, inter-VLAN routing, spanning-tree purpose, and link aggregation (LACP); know when data-center teams own these layers.
- [ ] **Core · P1 · D/P/S/A** — Read a routing table and explain longest-prefix match, connected/static routes, default routes, next hops, and asymmetric paths.
- [ ] **Role extension · P2 · A/S** — Compare dynamic routing concepts; explain OSPF's intra-domain role and BGP's inter-domain/policy role, autonomous systems, peering, route propagation, and convergence at a conceptual level.
- [ ] **Role extension · P3 · A** — Evaluate BGP policy, route filtering, route leaks, path selection, and failure domains for enterprise or cloud edge designs; do not treat protocol trivia as a substitute for design reasoning.
- [ ] **Role extension · P2 · A** — Recognize where MPLS, SD-WAN, and carrier networks fit in an enterprise WAN; understand service and operational implications without requiring implementation-level expertise.
- [ ] **Practical · P1 · D/P/S/A** — Given a source, destination, and route table, predict the next hop and identify likely boundaries where a packet could be dropped.

## 4. Security, segmentation, and identity-aware access

### Controls and threat-informed design

- [ ] **Core · P1 · D/P/S/A** — Explain stateless/stateful filtering, network ACLs, security groups, host firewalls, proxies, and network firewall policy; distinguish network reachability from application authorization.
- [ ] **Core · P1 · D/P/S/A** — Design least-privilege ingress and egress rules, default-deny boundaries, workload segmentation, management access, and public/private exposure.
- [ ] **Core · P1 · D/P/S/A** — Explain Zero Trust as continuous, identity- and context-aware authorization rather than simply a VPN or product feature.
- [ ] **Core · P1 · D/P/S/A** — Explain TLS/PKI fundamentals, secret and certificate lifecycle, VPN concepts (site-to-site and remote access), and encryption boundaries.
- [ ] **Core · P1 · D/P/S/A** — Recognize DDoS, spoofing, interception, DNS abuse, and lateral movement risks; identify network-level controls and evidence sources.
- [ ] **Role extension · P2 · P/S/A** — Understand network policies, egress controls, private service endpoints, inspection points, and policy enforcement trade-offs in cloud and cluster environments.
- [ ] **Role extension · P2 · A** — Map trust zones and data flows to regulatory or organizational controls; assess blast radius, policy ownership, and exceptions.
- [ ] **Practical · P1 · D/P/S/A** — Review a sample flow matrix and firewall policy; remove unnecessary exposure while preserving required application and operational traffic.

## 5. Load distribution, edge delivery, and availability

- [ ] **Core · P1 · D/P/S/A** — Compare Layer 4 and Layer 7 load balancing, health checks, backend pools, connection draining, session affinity, and TLS termination/pass-through.
- [ ] **Core · P1 · D/P/S/A** — Explain reverse proxies, ingress/gateway layers, DNS-based traffic steering, CDN caching, and Anycast at an operational level.
- [ ] **Role extension · P2 · S/A** — Design multi-zone and multi-region traffic paths; reason about health signals, failover time, state, dependencies, and split-brain risks.
- [ ] **Role extension · P2 · A/S** — Assess active-active versus active-passive designs, redundancy, graceful degradation, failure domains, and tested recovery objectives.
- [ ] **Role extension · P2 · D/S** — Understand MTU/path-MTU discovery, fragmentation, connection limits, NAT port exhaustion, and ephemeral port pressure as possible scaling bottlenecks.
- [ ] **Role extension · P2 · A** — Consider QoS and traffic prioritization where the network is shared or constrained; avoid assuming priority markings are preserved end to end.
- [ ] **Practical · P2 · D/P/S/A** — Model a dependency failure (unhealthy backends, DNS change, or zone loss); describe detection, traffic behavior, user impact, and rollback/recovery.

## 6. Cloud, hybrid, and virtual networking

### Provider-independent design

- [ ] **Core · P1 · D/P/S/A** — Map VPC/VNet and subnet constructs to IP ranges, route tables, gateways, security controls, and regional/zone boundaries.
- [ ] **Core · P1 · D/P/S/A** — Explain internet ingress/egress, NAT, private endpoints/service endpoints, peering, transit/hub-and-spoke, and their routing and security implications.
- [ ] **Role extension · P2 · D/P/S/A** — Compare VPN tunnels and dedicated private connectivity (for example, Direct Connect, ExpressRoute, and Cloud Interconnect); reason about redundancy, routing, throughput, and failover.
- [ ] **Role extension · P2 · A/P** — Plan hybrid DNS, address allocation, overlapping CIDRs, transitive routing, centralized inspection, shared services, and ownership boundaries.
- [ ] **Role extension · P2 · A** — Compare centralized and decentralized network governance; document trade-offs in autonomy, security, operations, scaling, and cost.
- [ ] **Role extension · P2 · D/P** — Review provider-specific equivalents across at least two clouds without assuming service names imply identical behavior or limits.
- [ ] **Role extension · P3 · A/S** — Understand edge connectivity, private service publishing/consumption, multi-cloud transit patterns, and provider-specific routing constraints when the architecture requires them.
- [ ] **Practical · P2 · D/P/S/A** — Draw a cloud/hybrid data-flow diagram that identifies CIDRs, route propagation, trust boundaries, DNS path, egress, and failure domains.

### SDN, overlays, and virtualization

- [ ] **Role extension · P2 · P/A** — Explain control plane versus data plane, SDN intent/policy, underlay versus overlay, and why virtual network abstractions still depend on physical transport.
- [ ] **Role extension · P2 · P/A** — Describe VXLAN and encapsulation conceptually; recognize MTU overhead, troubleshooting visibility, and scale/segmentation benefits.
- [ ] **Role extension · P2 · D/P** — Understand virtual interfaces, network namespaces, bridges, veth pairs, NAT, and packet-filtering hooks at a level useful for tracing container traffic.
- [ ] **Practical · P2 · P/A** — Trace a sample packet through an overlay and name the metadata and observability needed to distinguish overlay, underlay, and policy failures.

## 7. Containers and Kubernetes networking

- [ ] **Core · P1 · D/P/S** — Explain container network namespaces, interfaces, bridge/overlay concepts, port publishing, and how container networking differs from a VM's default network.
- [ ] **Core · P1 · D/P/S** — Explain the Kubernetes network model: Pod-to-Pod, Pod-to-Service, and external-to-Service connectivity; distinguish the Kubernetes API model from its implementation.
- [ ] **Core · P1 · D/P/S** — Explain CNI plugin responsibilities, node/pod/service CIDRs, IPAM, kube-proxy or an alternative service data plane, and cluster DNS.
- [ ] **Core · P1 · D/P/S** — Compare ClusterIP, NodePort, LoadBalancer, Ingress, and Gateway API use cases; understand EndpointSlices and health/readiness effects.
- [ ] **Core · P1 · D/P/S** — Explain NetworkPolicy intent and enforcement dependencies; know that policy behavior depends on the network plugin and configured policy capabilities.
- [ ] **Role extension · P2 · P/S** — Troubleshoot service discovery, pod-to-pod and pod-to-external traffic, DNS, egress, MTU, SNAT, conntrack, and address exhaustion.
- [ ] **Role extension · P2 · P/A** — Plan dual-stack clusters, non-overlapping address pools, multi-cluster connectivity, service exposure, and network-policy governance.
- [ ] **Role extension · P2 · S/A** — Evaluate service-mesh data paths, sidecar or ambient proxying, mTLS, retries, and observability overhead; distinguish mesh behavior from the underlying network.
- [ ] **Role extension · P2 · D/P** — Know that Kubernetes networking details can differ by operating system and implementation; validate CNI, host-network, and policy support for Windows nodes rather than assuming Linux behavior.
- [ ] **Practical · P1 · D/P/S** — Deploy or inspect a small cluster workload; verify name resolution and each connectivity path, then apply a policy and confirm both allowed and denied flows.

## 8. Observability, troubleshooting, and incident response

### Evidence-driven operations

- [ ] **Core · P1 · D/P/S/A** — Use a layered troubleshooting method: define the failing flow, compare working/non-working cases, and test DNS, address, route, policy, transport, TLS, and application hypotheses.
- [ ] **Core · P1 · D/P/S/A** — Use platform-appropriate equivalents of `ping`, `traceroute`/`tracert`, `ipconfig`/`ip`, `route`, `nslookup`/`dig`, socket inspection, and packet capture.
- [ ] **Core · P1 · D/P/S/A** — Read packet captures sufficiently to identify DNS exchanges, TCP setup/retransmission/reset, TLS handshake errors, HTTP requests, and directionality.
- [ ] **Core · P1 · D/P/S** — Correlate application logs and traces with host, firewall, load-balancer, DNS, flow, and cloud-network telemetry using timestamps and request/flow identifiers.
- [ ] **Role extension · P2 · S/P** — Understand metrics, logs, flow records, packet capture, SNMP, syslog, and streaming telemetry as complementary signals with different coverage and overhead.
- [ ] **Core · P1 · D/P/S/A** — Separate symptoms from causes, preserve evidence, communicate impact and mitigation, and use a timeline and blameless review after network-related incidents.
- [ ] **Role extension · P2 · S/A** — Define network-related alerts around user-visible symptoms and actionable saturation/error signals; account for false positives and missing telemetry.
- [ ] **Practical · P1 · D/P/S/A** — Resolve a staged failure such as incorrect DNS, blocked port, missing route, expired certificate, MTU mismatch, or unhealthy backend; document evidence and safe remediation.

### Operating systems and tools

- [ ] **Core · P1 · D/P/S** — On Linux, inspect interfaces, routes, DNS configuration, listening sockets, firewall state, and packet captures using the host's available tools.
- [ ] **Core · P1 · D/P/S** — On Windows, inspect adapter/IP configuration, routes, DNS, listening/connected sockets, firewall rules, and packet evidence using Windows-native tools such as `ipconfig`, `route`, `Get-Net*`, `Test-NetConnection`, and approved capture tooling.
- [ ] **Core · P1 · D/P/S** — Understand the difference between host-level, container-level, and cloud control-plane evidence; do not assume a Linux command or network-stack behavior applies to Windows.
- [ ] **Practical · P1 · D/P/S** — Capture the same simple DNS/HTTPS transaction on a Windows host and a Linux host (or compare their equivalent telemetry); explain which observations are platform-specific.

## 9. Automation, infrastructure as code, and change safety

- [ ] **Core · P1 · D/P/A** — Treat network configuration as versioned, reviewed, repeatable code; understand plan/review/apply, drift, state, and rollback concepts in infrastructure-as-code workflows.
- [ ] **Core · P1 · D/P/S/A** — Automate address plans, route and firewall changes, DNS records, and Kubernetes policies with validation, peer review, least privilege, and auditable change history.
- [ ] **Role extension · P2 · D/P** — Use APIs or vendor-neutral automation patterns to discover and configure network resources; make changes idempotent and safe to rerun.
- [ ] **Role extension · P2 · D/P/S** — Add tests for CIDR overlap, unintended public exposure, route reachability, policy intent, and expected service connectivity.
- [ ] **Role extension · P2 · A/P** — Define ownership, approval boundaries, emergency-change process, and policy guardrails for self-service network provisioning.
- [ ] **Practical · P2 · D/P** — Use IaC or an equivalent declarative workflow to deploy a small isolated network, validate it, make a controlled change, and remove it cleanly.

## 10. Architecture, capacity, cost, and resilience

- [ ] **Core · P1 · D/P/S/A** — Produce a network architecture diagram and data-flow inventory showing workloads, zones, trust boundaries, routes, DNS, ingress/egress, and dependencies.
- [ ] **Core · P1 · D/P/S/A** — Record architecture decisions and trade-offs for address space, segmentation, connectivity, availability, manageability, performance, security, and cost.
- [ ] **Role extension · P2 · A/S** — Calculate capacity needs and headroom for bandwidth, connection counts, NAT ports, addresses, load balancers, DNS, and growth; identify provider quotas and operational limits.
- [ ] **Role extension · P2 · A** — Design high availability and disaster recovery across failure domains; state RTO/RPO assumptions and demonstrate that failover paths have been tested.
- [ ] **Role extension · P2 · D/P/S/A** — Evaluate egress patterns, cross-zone/region transfer, transit, inspection, private endpoints, and logging costs alongside latency, security, and operational consequences.
- [ ] **Role extension · P2 · A/S** — Compare centralized versus distributed controls and shared versus dedicated networks; consider blast radius, failure coupling, and team operating model.
- [ ] **Practical · P2 · D/P/S/A** — Review a design against a checklist of single points of failure, overlapping IP ranges, unbounded egress, hidden dependencies, observability gaps, quota risks, and recovery-test evidence.

## Role-specific emphasis

| Role | Prioritize | Demonstrate readiness |
|---|---|---|
| **DevOps** | P1 foundations, DNS/TCP/TLS, cloud VPC/VNet basics, ingress/egress, IaC, deployment-time connectivity checks, and Linux/Windows host diagnostics. | Can make a safe, reviewed network change for an application deployment and diagnose a failed connection across DNS, route, policy, and TLS layers. |
| **Platform** | DevOps foundations plus cluster networking, IPAM, CNI, service exposure, NetworkPolicy, multi-tenancy, shared connectivity, and self-service guardrails. | Can explain and validate a workload's path through pod, service, cluster, and external network boundaries and provide a secure reusable platform pattern. |
| **SRE** | Transport/DNS behavior, load balancing, failure domains, telemetry, incident response, capacity, resilience, and tested recovery. | Can use evidence to isolate a network-related symptom, assess user impact, mitigate safely, and propose an actionable reliability improvement. |
| **Architect** | Address/routing design, segmentation, hybrid/multi-cloud options, security boundaries, traffic distribution, HA/DR, capacity, cost, and decision records. | Can present a data-flow architecture with explicit assumptions, failure modes, controls, operational ownership, and justified trade-offs. |

## Suggested hands-on sequence and readiness plan

1. **Foundation lab (P1):** Calculate an IPv4/IPv6 address plan; inspect routes and DNS on Windows and Linux; trace a working HTTPS request and explain each layer.
2. **Policy and path lab (P1):** Deploy a small service and client in an isolated environment; test allowed and denied flows; use logs and packet evidence to identify a deliberately introduced failure.
3. **Cloud connectivity lab (P2):** Build a small, disposable VPC/VNet or equivalent with public/private segments, route controls, DNS, and least-privilege security rules. Draw the resulting flow and destroy the environment afterward.
4. **Kubernetes lab (P2):** Deploy two services; validate Pod, Service, DNS, and external paths; add a NetworkPolicy and check its actual enforcement in the chosen CNI.
5. **Resilience exercise (P2):** Simulate an unhealthy backend or zone/dependency loss; record detection, failover behavior, recovery time, and any user-visible failure.
6. **Automation capstone (P2):** Encode a small network and its tests as IaC; review a plan, validate address and exposure rules, apply, verify, and clean up.

**Readiness checkpoint:** For a typical application, independently describe the full request path, subnet and trust boundaries, required routes and DNS, transport/TLS expectations, controls, telemetry, likely failure modes, and a safe validation or recovery approach. For role extension readiness, complete the relevant capstone and explain its trade-offs to a peer.

## Primary references

These references ground the concepts; they are not a prescribed reading order or certification blueprint. Standards are linked directly, and provider documentation illustrates implementations that can differ by service and product.

### Cisco learning reference

- [Cisco CCNA certification overview](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/enterprise/ccna/index.html) — a vendor certification reference for networking, security, and automation fundamentals. This syllabus does not claim to reproduce its exam topics or weighting.

### Internet standards and protocols (IETF RFCs)

- [RFC 9293 — Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034) and [RFC 1035 — Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035)
- [RFC 8200 — Internet Protocol, Version 6 (IPv6) Specification](https://www.rfc-editor.org/rfc/rfc8200)
- [RFC 4271 — A Border Gateway Protocol 4 (BGP-4)](https://www.rfc-editor.org/rfc/rfc4271)
- [RFC 8446 — The Transport Layer Security (TLS) Protocol Version 1.3](https://www.rfc-editor.org/rfc/rfc8446)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)

### Cloud architecture and networking documentation

- [AWS Well-Architected Framework: Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
- [Amazon VPC: What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [Azure Virtual Network overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
- [Google Cloud landing zone: Decide on a network design](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design)

### Kubernetes networking documentation

- [Cluster Networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
- [Services, Load Balancing, and Networking](https://kubernetes.io/docs/concepts/services-networking/)
- [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
