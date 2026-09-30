# Networking: Architect-Level Prerequisite Topics

**Legend:** R = Required | O = Optional | E = Exam-oriented | L = Real-life use

---

## Tier 1: Foundations
| Topic | Flag |
|---|---|
| Network types (LAN, WAN, MAN, PAN) | R, E |
| Topologies (star, mesh, hybrid) | R, E |
| Client-server vs peer-to-peer | R, E |
| OSI model (7 layers) | R, E, L |
| TCP/IP model (4 layers) | R, E, L |
| Encapsulation / decapsulation (PDU: frame, packet, segment) | R, E |
| Bandwidth, throughput, latency, jitter, packet loss | R, L |

## Tier 2: Addressing & Core Protocols
| Topic | Flag |
|---|---|
| MAC address | R, E |
| IPv4 addressing (classes, private vs public) | R, E, L |
| Subnet mask, CIDR notation | R, E, L |
| Subnetting and VLSM | R, E, L |
| IPv6 basics | R, E |
| NAT / PAT | R, E, L |
| Ports and sockets | R, E, L |
| TCP vs UDP | R, E, L |
| TCP 3-way handshake, flow control | R, E |
| ARP | R, E, L |
| ICMP (ping, traceroute) | R, L |
| DHCP | R, E, L |
| DNS (records: A, AAAA, CNAME, MX, TXT, NS) | R, E, L |
| HTTP/HTTPS, TLS basics | R, E, L |
| Other protocols (SSH, FTP/SFTP, SMTP, NTP) | O, E |

## Tier 3: Devices & Switching
| Topic | Flag |
|---|---|
| Hub, switch, router, modem, access point | R, E |
| Layer 2 vs Layer 3 switch | R, E, L |
| MAC table, broadcast domain, collision domain | R, E |
| VLANs, trunking (802.1Q) | R, E, L |
| Spanning Tree Protocol (STP) | E, O |
| Link aggregation (LACP) | O, E |
| Gateway, default route | R, L |
| Firewall, proxy, load balancer | R, L |

## Tier 4: Routing
| Topic | Flag |
|---|---|
| Routing table, static vs dynamic routing | R, E, L |
| Inter-VLAN routing | R, E, L |
| OSPF | E, O |
| BGP (concepts only) | R for architects, E, L |
| Autonomous System (AS) | R, E |
| EIGRP, RIP | O |

## Tier 5: Security
| Topic | Flag |
|---|---|
| CIA triad | R, E |
| Firewall types (stateless, stateful, NGFW) | R, E, L |
| ACLs | R, E, L |
| VPN (site-to-site, remote access, IPsec) | R, E, L |
| Zero Trust basics | R, L |
| Segmentation, DMZ | R, E, L |
| IDS/IPS | R, E |
| Common attacks (DDoS, spoofing, MITM) | R, E |
| PKI, certificates | R, E, L |

## Tier 6: Wireless
| Topic | Flag |
|---|---|
| Wi-Fi standards (802.11 a/b/g/n/ac/ax) | O, E |
| SSID, channels, bands (2.4/5/6 GHz) | O, L |
| WPA2/WPA3 | R, E, L |
| Cellular (4G/5G) concepts | O |

## Tier 7: Architect-Level Design
| Topic | Flag |
|---|---|
| Three-tier architecture (core, distribution, access) | R, E |
| Spine-leaf architecture | R, E, L |
| High availability, redundancy, failover | R, L |
| Load balancing (L4 vs L7) | R, E, L |
| CDN, Anycast | R, L |
| SD-WAN | R, L |
| SDN, network virtualization (VXLAN, overlay/underlay) | R, E, L |
| Cloud networking (VPC/VNet, subnets, peering, transit gateway) | R, E, L |
| Hybrid connectivity (Direct Connect, ExpressRoute) | R, E, L |
| Service mesh, ingress, container networking | R for cloud-native, L |
| QoS | O, E |
| Capacity planning, SLAs | R, L |

## Tier 8: Operations & Troubleshooting
| Topic | Flag |
|---|---|
| Troubleshooting methodology (layer by layer) | R, E, L |
| Tools: ping, traceroute, nslookup/dig, netstat, tcpdump, Wireshark | R, L |
| Monitoring (SNMP, NetFlow, syslog) | O, L |
| Network automation (Ansible, Terraform basics) | O, L |

---

## Jargon to Skip for Now
- Token Ring, FDDI, ATM, Frame Relay, X.25, IPX/SPX
- Detailed CSMA/CD mechanics
- Legacy classful routing internals
- Vendor-specific CLI syntax (Cisco IOS commands)
- Deep MPLS internals