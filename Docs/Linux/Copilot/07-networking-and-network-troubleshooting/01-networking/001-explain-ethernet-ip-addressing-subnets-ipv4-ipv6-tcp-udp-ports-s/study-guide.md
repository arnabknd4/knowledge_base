# Explain Ethernet, IP addressing/subnets, IPv4/IPv6, TCP/UDP, ports, sockets, ARP/neighbor discovery, MTU, and path MTU.

**Syllabus objective (exact wording):** Explain Ethernet, IP addressing/subnets, IPv4/IPv6, TCP/UDP, ports, sockets, ARP/neighbor discovery, MTU, and path MTU.

**Mapping:** `07` → `001` `Explain Ethernet, IP addressing/subnets, IPv4/IPv6, TCP/UDP, ports, sockets, ARP/neighbor discovery, MTU, and path MTU.`

## What

Ethernet/link, IPv4/IPv6 addressing, TCP/UDP ports, sockets, neighbor discovery and MTU define different path stages. Path MTU discovery failure can allow small packets but black-hole larger traffic.

## Why

This matters operationally: TLS connects but large responses stall through a tunnel; investigate PMTU/fragmentation rather than repeatedly restarting DNS or the application. The decision hinges on these mechanics: Path MTU discovery failure can allow small packets but black-hole larger traffic.

## How

1. **Establish the relevant boundary:** Ethernet/link, IPv4/IPv6 addressing, TCP/UDP ports, sockets, neighbor discovery and MTU define different path stages. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Capture interface/address, route, neighbor and socket evidence; test both families and payload sizes only within authorization; compare configured MTU end to end.
3. **Exercise the scenario:** TLS connects but large responses stall through a tunnel; investigate PMTU/fragmentation rather than repeatedly restarting DNS or the application.
4. **Verify this outcome:** use `ip -brief link` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Path MTU discovery failure can allow small packets but black-hole larger traffic.

    **Distro/release distinction:** NetworkManager is common on RHEL; Ubuntu may use Netplan with NetworkManager or systemd-networkd. firewalld/UFW are frontends, while nftables is the kernel rules framework. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** TLS connects but large responses stall through a tunnel; investigate PMTU/fragmentation rather than repeatedly restarting DNS or the application. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
ip -brief link
ip -brief address
ip neigh
ip route
ss -s
```

## Do's and Don'ts

- **Do:** Capture interface/address, route, neighbor and socket evidence; test both families and payload sizes only within authorization; compare configured MTU end to end.
- **Don't:** Do not flush/change routes, firewall, resolver or interface settings on a remote host without out-of-band access and a tested rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

TLS connects but large responses stall through a tunnel; investigate PMTU/fragmentation rather than repeatedly restarting DNS or the application. **Operator response:** Capture interface/address, route, neighbor and socket evidence; test both families and payload sizes only within authorization; compare configured MTU end to end. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Ethernet/link, IPv4/IPv6 addressing, TCP/UDP ports, sockets, neighbor discovery and MTU define different path stages.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `ip -brief link` and follow the evidence path: Capture interface/address, route, neighbor and socket evidence; test both families and payload sizes only within authorization; compare configured MTU end to end.

**Q: How would you verify or falsify the working diagnosis?**

A: TLS connects but large responses stall through a tunnel; investigate PMTU/fragmentation rather than repeatedly restarting DNS or the application. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
