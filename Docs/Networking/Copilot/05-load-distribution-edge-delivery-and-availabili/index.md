# 05. Load distribution, edge delivery, and availability

Architect-level, objective-mapped guides for this domain. Each checkbox is represented once. See the [source syllabus](../copilot-Networking-syllabus.md).

## Load balancing and edge availability

- [Compare Layer 4 and Layer 7 load balancing, health checks, backend pools, connection draining, session affinity, and TLS termination/pass-through.](load-balancing-and-edge-availability/036-compare-layer-4-and-layer-7-load-balancing-h/study-guide.md) — Core; P1; roles D/P/S/A.
- [Explain reverse proxies, ingress/gateway layers, DNS-based traffic steering, CDN caching, and Anycast at an operational level.](load-balancing-and-edge-availability/037-explain-reverse-proxies-ingress-gateway-laye/study-guide.md) — Core; P1; roles D/P/S/A.
- [Design multi-zone and multi-region traffic paths; reason about health signals, failover time, state, dependencies, and split-brain risks.](load-balancing-and-edge-availability/038-design-multi-zone-and-multi-region-traffic-p/study-guide.md) — Role extension; P2; roles S/A.
- [Assess active-active versus active-passive designs, redundancy, graceful degradation, failure domains, and tested recovery objectives.](load-balancing-and-edge-availability/039-assess-active-active-versus-active-passive-d/study-guide.md) — Role extension; P2; roles A/S.
- [Understand MTU/path-MTU discovery, fragmentation, connection limits, NAT port exhaustion, and ephemeral port pressure as possible scaling bottlenecks.](load-balancing-and-edge-availability/040-understand-mtu-path-mtu-discovery-fragmentat/study-guide.md) — Role extension; P2; roles D/S.
- [Consider QoS and traffic prioritization where the network is shared or constrained; avoid assuming priority markings are preserved end to end.](load-balancing-and-edge-availability/041-consider-qos-and-traffic-prioritization-wher/study-guide.md) — Role extension; P2; roles A.
- [Model a dependency failure (unhealthy backends, DNS change, or zone loss); describe detection, traffic behavior, user impact, and rollback/recovery.](load-balancing-and-edge-availability/042-model-a-dependency-failure-unhealthy-backend/study-guide.md) — Practical; P2; roles D/P/S/A.
