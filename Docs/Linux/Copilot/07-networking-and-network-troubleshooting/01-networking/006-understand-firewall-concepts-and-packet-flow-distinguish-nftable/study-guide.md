# Understand firewall concepts and packet flow; distinguish nftables, firewalld, and UFW interfaces, plus legacy iptables compatibility.

**Syllabus objective (exact wording):** Understand firewall concepts and packet flow; distinguish nftables, firewalld, and UFW interfaces, plus legacy iptables compatibility.

**Mapping:** `07` → `006` `Understand firewall concepts and packet flow; distinguish nftables, firewalld, and UFW interfaces, plus legacy iptables compatibility.`

## What

nftables is the kernel packet-filter framework; firewalld/UFW provide policy management and may use nftables or compatibility backends. Packet path, namespace, state and rule ordering determine outcome.

## Why

This matters operationally: A host firewall reports active but a container port is still reachable; inspect published-port forwarding and nftables chain path, not only UFW status. The decision hinges on these mechanics: Packet path, namespace, state and rule ordering determine outcome.

## How

1. **Establish the relevant boundary:** nftables is the kernel packet-filter framework; firewalld/UFW provide policy management and may use nftables or compatibility backends. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Identify active ruleset and frontend, then trace interface, hook, direction, conntrack state and namespace. Save current policy and out-of-band access before any lab-only rule experiment.
3. **Exercise the scenario:** A host firewall reports active but a container port is still reachable; inspect published-port forwarding and nftables chain path, not only UFW status.
4. **Verify this outcome:** use `nft list ruleset 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Packet path, namespace, state and rule ordering determine outcome.

    **Distro/release distinction:** NetworkManager is common on RHEL; Ubuntu may use Netplan with NetworkManager or systemd-networkd. firewalld/UFW are frontends, while nftables is the kernel rules framework. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A host firewall reports active but a container port is still reachable; inspect published-port forwarding and nftables chain path, not only UFW status. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
nft list ruleset 2>/dev/null
firewall-cmd --state 2>/dev/null
ufw status verbose 2>/dev/null
```

## Do's and Don'ts

- **Do:** Identify active ruleset and frontend, then trace interface, hook, direction, conntrack state and namespace. Save current policy and out-of-band access before any lab-only rule experiment.
- **Don't:** Do not flush/change routes, firewall, resolver or interface settings on a remote host without out-of-band access and a tested rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A host firewall reports active but a container port is still reachable; inspect published-port forwarding and nftables chain path, not only UFW status. **Operator response:** Identify active ruleset and frontend, then trace interface, hook, direction, conntrack state and namespace. Save current policy and out-of-band access before any lab-only rule experiment. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: nftables is the kernel packet-filter framework; firewalld/UFW provide policy management and may use nftables or compatibility backends.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `nft list ruleset 2>/dev/null` and follow the evidence path: Identify active ruleset and frontend, then trace interface, hook, direction, conntrack state and namespace. Save current policy and out-of-band access before any lab-only rule experiment.

**Q: How would you verify or falsify the working diagnosis?**

A: A host firewall reports active but a container port is still reachable; inspect published-port forwarding and nftables chain path, not only UFW status. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
