# 08. Observability, troubleshooting, and incident response

Architect-level, objective-mapped guides for this domain. Each checkbox is represented once. See the [source syllabus](../copilot-Networking-syllabus.md).

## Evidence-driven operations

- [Use a layered troubleshooting method: define the failing flow, compare working/non-working cases, and test DNS, address, route, policy, transport, TLS, and application hypotheses.](evidence-driven-operations/065-use-a-layered-troubleshooting-method-define/study-guide.md) — Core; P1; roles D/P/S/A.
- [Use platform-appropriate equivalents of `ping`, `traceroute`/`tracert`, `ipconfig`/`ip`, `route`, `nslookup`/`dig`, socket inspection, and packet capture.](evidence-driven-operations/066-use-platform-appropriate-equivalents-of-ping/study-guide.md) — Core; P1; roles D/P/S/A.
- [Read packet captures sufficiently to identify DNS exchanges, TCP setup/retransmission/reset, TLS handshake errors, HTTP requests, and directionality.](evidence-driven-operations/067-read-packet-captures-sufficiently-to-identif/study-guide.md) — Core; P1; roles D/P/S/A.
- [Correlate application logs and traces with host, firewall, load-balancer, DNS, flow, and cloud-network telemetry using timestamps and request/flow identifiers.](evidence-driven-operations/068-correlate-application-logs-and-traces-with-h/study-guide.md) — Core; P1; roles D/P/S.
- [Understand metrics, logs, flow records, packet capture, SNMP, syslog, and streaming telemetry as complementary signals with different coverage and overhead.](evidence-driven-operations/069-understand-metrics-logs-flow-records-packet/study-guide.md) — Role extension; P2; roles S/P.
- [Separate symptoms from causes, preserve evidence, communicate impact and mitigation, and use a timeline and blameless review after network-related incidents.](evidence-driven-operations/070-separate-symptoms-from-causes-preserve-evide/study-guide.md) — Core; P1; roles D/P/S/A.
- [Define network-related alerts around user-visible symptoms and actionable saturation/error signals; account for false positives and missing telemetry.](evidence-driven-operations/071-define-network-related-alerts-around-user-vi/study-guide.md) — Role extension; P2; roles S/A.
- [Resolve a staged failure such as incorrect DNS, blocked port, missing route, expired certificate, MTU mismatch, or unhealthy backend; document evidence and safe remediation.](evidence-driven-operations/072-resolve-a-staged-failure-such-as-incorrect-d/study-guide.md) — Practical; P1; roles D/P/S/A.

## Operating systems and tools

- [On Linux, inspect interfaces, routes, DNS configuration, listening sockets, firewall state, and packet captures using the host's available tools.](operating-systems-and-tools/073-on-linux-inspect-interfaces-routes-dns-confi/study-guide.md) — Core; P1; roles D/P/S.
- [On Windows, inspect adapter/IP configuration, routes, DNS, listening/connected sockets, firewall rules, and packet evidence using Windows-native tools such as `ipconfig`, `route`, `Get-Net*`, `Test-NetConnection`, and approved capture tooling.](operating-systems-and-tools/074-on-windows-inspect-adapter-ip-configuration/study-guide.md) — Core; P1; roles D/P/S.
- [Understand the difference between host-level, container-level, and cloud control-plane evidence; do not assume a Linux command or network-stack behavior applies to Windows.](operating-systems-and-tools/075-understand-the-difference-between-host-level/study-guide.md) — Core; P1; roles D/P/S.
- [Capture the same simple DNS/HTTPS transaction on a Windows host and a Linux host (or compare their equivalent telemetry); explain which observations are platform-specific.](operating-systems-and-tools/076-capture-the-same-simple-dns-https-transactio/study-guide.md) — Practical; P1; roles D/P/S.
