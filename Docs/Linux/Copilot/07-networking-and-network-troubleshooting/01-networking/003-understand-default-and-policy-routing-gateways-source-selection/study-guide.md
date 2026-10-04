# Understand default and policy routing, gateways, source selection, forwarding, NAT, and asymmetric routing.

**Syllabus objective (exact wording):** Understand default and policy routing, gateways, source selection, forwarding, NAT, and asymmetric routing.

**Mapping:** `07` → `003` `Understand default and policy routing, gateways, source selection, forwarding, NAT, and asymmetric routing.`

## What

Policy routing selects tables using rules and source attributes; forwarding/NAT and return paths must agree. Asymmetric routing and reverse-path filtering can reject valid incoming traffic.

## Why

This matters operationally: A dual-homed host sends replies out the wrong interface; inspect `ip rule` and route lookup from the selected source rather than adding a broad default route. The decision hinges on these mechanics: Asymmetric routing and reverse-path filtering can reject valid incoming traffic.

## How

1. **Establish the relevant boundary:** Policy routing selects tables using rules and source attributes; forwarding/NAT and return paths must agree. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect all routing rules/tables, source addresses, forwarding and both directions; capture a bounded flow trace only if needed.
3. **Exercise the scenario:** A dual-homed host sends replies out the wrong interface; inspect `ip rule` and route lookup from the selected source rather than adding a broad default route.
4. **Verify this outcome:** use `ip rule show` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Asymmetric routing and reverse-path filtering can reject valid incoming traffic.

    **Distro/release distinction:** NetworkManager is common on RHEL; Ubuntu may use Netplan with NetworkManager or systemd-networkd. firewalld/UFW are frontends, while nftables is the kernel rules framework. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A dual-homed host sends replies out the wrong interface; inspect `ip rule` and route lookup from the selected source rather than adding a broad default route. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
ip rule show
ip route show table all
ip route get <destination> from <source>
sysctl net.ipv4.ip_forward
```

## Do's and Don'ts

- **Do:** Inspect all routing rules/tables, source addresses, forwarding and both directions; capture a bounded flow trace only if needed.
- **Don't:** Do not flush/change routes, firewall, resolver or interface settings on a remote host without out-of-band access and a tested rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A dual-homed host sends replies out the wrong interface; inspect `ip rule` and route lookup from the selected source rather than adding a broad default route. **Operator response:** Inspect all routing rules/tables, source addresses, forwarding and both directions; capture a bounded flow trace only if needed. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Policy routing selects tables using rules and source attributes; forwarding/NAT and return paths must agree.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `ip rule show` and follow the evidence path: Inspect all routing rules/tables, source addresses, forwarding and both directions; capture a bounded flow trace only if needed.

**Q: How would you verify or falsify the working diagnosis?**

A: A dual-homed host sends replies out the wrong interface; inspect `ip rule` and route lookup from the selected source rather than adding a broad default route. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
