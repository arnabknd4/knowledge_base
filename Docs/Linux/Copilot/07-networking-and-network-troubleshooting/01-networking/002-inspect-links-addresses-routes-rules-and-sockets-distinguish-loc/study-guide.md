# Inspect links, addresses, routes, rules, and sockets; distinguish local, routed, and name-resolution failures.

**Syllabus objective (exact wording):** Inspect links, addresses, routes, rules, and sockets; distinguish local, routed, and name-resolution failures.

**Mapping:** `07` → `002` `Inspect links, addresses, routes, rules, and sockets; distinguish local, routed, and name-resolution failures.`

## What

The active kernel network state may differ from desired config. `ip` inspects links/addresses/routes/rules; `ss` shows sockets. Test in the workload's namespace when containers are involved.

## Why

This matters operationally: A service listens on loopback only; `ss -lntp` identifies bind address and port before firewall or DNS is changed. The decision hinges on these mechanics: `ip` inspects links/addresses/routes/rules; `ss` shows sockets. Test in the workload's namespace when containers are involved.

## How

1. **Establish the relevant boundary:** The active kernel network state may differ from desired config. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Locate the failure boundary: link/address, route, neighbor, socket/listener or resolver; compare host and process namespace before changing configuration.
3. **Exercise the scenario:** A service listens on loopback only; `ss -lntp` identifies bind address and port before firewall or DNS is changed.
4. **Verify this outcome:** use `ip -brief address` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** `ip` inspects links/addresses/routes/rules; `ss` shows sockets. Test in the workload's namespace when containers are involved.

    **Distro/release distinction:** NetworkManager is common on RHEL; Ubuntu may use Netplan with NetworkManager or systemd-networkd. firewalld/UFW are frontends, while nftables is the kernel rules framework. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A service listens on loopback only; `ss -lntp` identifies bind address and port before firewall or DNS is changed. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
ip -brief address
ip route show table all
ip rule
ss -lntup
```

## Do's and Don'ts

- **Do:** Locate the failure boundary: link/address, route, neighbor, socket/listener or resolver; compare host and process namespace before changing configuration.
- **Don't:** Do not flush/change routes, firewall, resolver or interface settings on a remote host without out-of-band access and a tested rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A service listens on loopback only; `ss -lntp` identifies bind address and port before firewall or DNS is changed. **Operator response:** Locate the failure boundary: link/address, route, neighbor, socket/listener or resolver; compare host and process namespace before changing configuration. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: The active kernel network state may differ from desired config.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `ip -brief address` and follow the evidence path: Locate the failure boundary: link/address, route, neighbor, socket/listener or resolver; compare host and process namespace before changing configuration.

**Q: How would you verify or falsify the working diagnosis?**

A: A service listens on loopback only; `ss -lntp` identifies bind address and port before firewall or DNS is changed. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
