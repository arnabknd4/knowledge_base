# Domain 5 — Networking

Objective-level study guides for Docker networking models, application connectivity, and multi-host operations.

## Guides

### Docker network models

- [Understand bridge, host, none, overlay, macvlan, and ipvlan drivers and their appropriate use cases](docker-network-models/network-driver-models/study-guide.md)
- [Distinguish the default bridge from user-defined bridge networks, including service-name DNS behavior](docker-network-models/default-vs-user-defined-bridge/study-guide.md)
- [Attach and detach containers from networks and inspect network configuration](docker-network-models/attach-detach-inspect/study-guide.md)
- [Understand container interfaces, IP addressing, routing, DNS, NAT, firewall interaction, and port publishing](docker-network-models/network-packet-path/study-guide.md)
- [Distinguish a Dockerfile EXPOSE declaration from runtime port publishing (-p)](docker-network-models/expose-vs-publish/study-guide.md)
### Application and multi-host connectivity

- [Connect services by stable service names rather than hard-coded container IP addresses](application-and-multi-host-connectivity/service-name-discovery/study-guide.md)
- [Design least-exposure ingress: publish only required ports and place dependent services on appropriate networks](application-and-multi-host-connectivity/least-exposure-ingress/study-guide.md)
- [Understand outbound connectivity, host-to-container access, container-to-host access, and cross-network communication](application-and-multi-host-connectivity/network-connectivity-directions/study-guide.md)
- [Troubleshoot name resolution, connection refusal, port collisions, routing, firewall rules, and MTU-related failures](application-and-multi-host-connectivity/network-troubleshooting/study-guide.md)
- [Understand overlay networking prerequisites and the operational/security implications of cross-host container networking](application-and-multi-host-connectivity/overlay-prerequisites/study-guide.md)
- [Plan service discovery and ingress/load balancing separately from container networking](application-and-multi-host-connectivity/discovery-vs-ingress/study-guide.md)

**Syllabus:** [Docker syllabus](../copilot-docker-syllabus.md)
