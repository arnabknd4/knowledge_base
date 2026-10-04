# 02. Addressing, subnetting, and core protocols

Architect-level, objective-mapped guides for this domain. Each checkbox is represented once. See the [source syllabus](../copilot-Networking-syllabus.md).

## IP addressing and local delivery

- [Read and calculate IPv4 CIDR prefixes, subnet ranges, usable addresses, and route aggregation; plan non-overlapping address space for environments and growth.](ip-addressing-and-local-delivery/007-read-and-calculate-ipv4-cidr-prefixes-subnet/study-guide.md) — Core; P1; roles D/P/S/A.
- [Recognize private, public, loopback, link-local, and special-use IPv4 ranges; understand NAT/PAT purpose, trade-offs, and failure modes.](ip-addressing-and-local-delivery/008-recognize-private-public-loopback-link-local/study-guide.md) — Core; P1; roles D/P/S/A.
- [Explain IPv6 notation, prefix allocation, global and link-local addresses, neighbor discovery, SLAAC/DHCPv6 at a high level, and dual-stack considerations.](ip-addressing-and-local-delivery/009-explain-ipv6-notation-prefix-allocation-glob/study-guide.md) — Core; P1; roles D/P/S/A.
- [Explain MAC addresses, Ethernet frames, ARP for IPv4, IPv6 Neighbor Discovery, default gateways, and how a host chooses a next hop.](ip-addressing-and-local-delivery/010-explain-mac-addresses-ethernet-frames-arp-fo/study-guide.md) — Core; P1; roles D/P/S/A.
- [Interpret ports, sockets, ephemeral ports, and common transport/application protocol relationships.](ip-addressing-and-local-delivery/011-interpret-ports-sockets-ephemeral-ports-and/study-guide.md) — Core; P1; roles D/P/S/A.
- [Design IPAM and subnet allocation conventions for multi-environment, multi-account/subscription/project, and Kubernetes address pools.](ip-addressing-and-local-delivery/012-design-ipam-and-subnet-allocation-convention/study-guide.md) — Role extension; P2; roles P/A.

## Transport, naming, configuration, and application protocols

- [Compare TCP and UDP; explain TCP connection establishment/teardown, reliability, retransmission, flow and congestion control, and what packet loss does to throughput.](transport-naming-configuration-and-applica/013-compare-tcp-and-udp-explain-tcp-connection-e/study-guide.md) — Core; P1; roles D/P/S/A.
- [Explain DNS resolution, caching/TTL, recursive versus authoritative service, zones, and common A/AAAA/CNAME/NS/PTR/TXT records.](transport-naming-configuration-and-applica/014-explain-dns-resolution-caching-ttl-recursive/study-guide.md) — Core; P1; roles D/P/S/A.
- [Explain DHCP address leasing and the role of DNS and time synchronization in reliable service operation.](transport-naming-configuration-and-applica/015-explain-dhcp-address-leasing-and-the-role-of/study-guide.md) — Core; P1; roles D/P/S/A.
- [Explain HTTP request/response semantics, common status classes, connection reuse, proxies, and the effect of HTTP versions without memorizing wire-level details.](transport-naming-configuration-and-applica/016-explain-http-request-response-semantics-comm/study-guide.md) — Core; P1; roles D/P/S/A.
- [Describe TLS certificates, trust chains, hostname validation, SNI, certificate expiry/rotation, and the difference between encryption in transit and authorization.](transport-naming-configuration-and-applica/017-describe-tls-certificates-trust-chains-hostn/study-guide.md) — Core; P1; roles D/P/S/A.
- [Understand SSH, NTP, SMTP, and common API/service ports sufficiently to assess dependencies and troubleshoot connectivity.](transport-naming-configuration-and-applica/018-understand-ssh-ntp-smtp-and-common-api-servi/study-guide.md) — Role extension; P2; roles D/P/S.
- [Understand DNS failure patterns such as negative caching, split-horizon answers, stale records, and resolver-path differences.](transport-naming-configuration-and-applica/019-understand-dns-failure-patterns-such-as-nega/study-guide.md) — Role extension; P2; roles S/A.
- [Inspect DNS answers, route/connection state, and an HTTPS certificate for a test endpoint; explain what each observation does and does not prove.](transport-naming-configuration-and-applica/020-inspect-dns-answers-route-connection-state-a/study-guide.md) — Practical; P1; roles D/P/S/A.
