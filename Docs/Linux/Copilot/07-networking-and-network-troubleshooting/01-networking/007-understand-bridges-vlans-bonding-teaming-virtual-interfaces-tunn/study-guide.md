# Understand bridges, VLANs, bonding/teaming, virtual interfaces, tunnels, and overlay networks (P1).

**Syllabus objective (exact wording):** Understand bridges, VLANs, bonding/teaming, virtual interfaces, tunnels, and overlay networks (P1).

**Mapping:** `07` → `007` `Understand bridges, VLANs, bonding/teaming, virtual interfaces, tunnels, and overlay networks (P1).`

## What

Bridges connect L2 segments; VLANs tag traffic; bonding/teaming aggregate links; tunnels/overlays add encapsulation and MTU constraints. Configuration and driver support are distro/device dependent.

## Why

This matters operationally: An overlay service loses packets above a threshold; calculate encapsulation overhead and verify physical underlay MTU plus endpoint configuration. The decision hinges on these mechanics: Configuration and driver support are distro/device dependent.

## How

1. **Establish the relevant boundary:** Bridges connect L2 segments; VLANs tag traffic; bonding/teaming aggregate links; tunnels/overlays add encapsulation and MTU constraints. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Map physical and virtual interfaces, bridge/VLAN membership, bond state, tunnel endpoint and effective MTUs before diagnosing a multi-hop path.
3. **Exercise the scenario:** An overlay service loses packets above a threshold; calculate encapsulation overhead and verify physical underlay MTU plus endpoint configuration.
4. **Verify this outcome:** use `ip -d link show` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Configuration and driver support are distro/device dependent.

    **Distro/release distinction:** NetworkManager is common on RHEL; Ubuntu may use Netplan with NetworkManager or systemd-networkd. firewalld/UFW are frontends, while nftables is the kernel rules framework. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** An overlay service loses packets above a threshold; calculate encapsulation overhead and verify physical underlay MTU plus endpoint configuration. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
ip -d link show
bridge link 2>/dev/null
cat /proc/net/bonding/* 2>/dev/null
ip route
```

## Do's and Don'ts

- **Do:** Map physical and virtual interfaces, bridge/VLAN membership, bond state, tunnel endpoint and effective MTUs before diagnosing a multi-hop path.
- **Don't:** Do not flush/change routes, firewall, resolver or interface settings on a remote host without out-of-band access and a tested rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

An overlay service loses packets above a threshold; calculate encapsulation overhead and verify physical underlay MTU plus endpoint configuration. **Operator response:** Map physical and virtual interfaces, bridge/VLAN membership, bond state, tunnel endpoint and effective MTUs before diagnosing a multi-hop path. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Bridges connect L2 segments; VLANs tag traffic; bonding/teaming aggregate links; tunnels/overlays add encapsulation and MTU constraints.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `ip -d link show` and follow the evidence path: Map physical and virtual interfaces, bridge/VLAN membership, bond state, tunnel endpoint and effective MTUs before diagnosing a multi-hop path.

**Q: How would you verify or falsify the working diagnosis?**

A: An overlay service loses packets above a threshold; calculate encapsulation overhead and verify physical underlay MTU plus endpoint configuration. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
