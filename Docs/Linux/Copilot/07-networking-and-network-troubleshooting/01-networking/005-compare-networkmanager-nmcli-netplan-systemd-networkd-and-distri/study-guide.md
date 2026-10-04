# Compare NetworkManager/nmcli, Netplan, systemd-networkd, and distribution-specific network configuration; avoid assuming one control plane everywhere.

**Syllabus objective (exact wording):** Compare NetworkManager/nmcli, Netplan, systemd-networkd, and distribution-specific network configuration; avoid assuming one control plane everywhere.

**Mapping:** `07` → `005` `Compare NetworkManager/nmcli, Netplan, systemd-networkd, and distribution-specific network configuration; avoid assuming one control plane everywhere.`

## What

NetworkManager/nmcli, Netplan, systemd-networkd and cloud-init may be control planes or frontends; generated backend files can be overwritten. Determine active renderer on that exact release/image.

## Why

This matters operationally: An Ubuntu image's manual networkd edit disappears at reboot because Netplan owns generation; update Netplan and test with its rollback safeguards. The decision hinges on these mechanics: Determine active renderer on that exact release/image.

## How

1. **Establish the relevant boundary:** NetworkManager/nmcli, Netplan, systemd-networkd and cloud-init may be control planes or frontends; generated backend files can be overwritten. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect running managers and their source configuration; check Netplan renderer where present and use the owning tool's validation/rollback process.
3. **Exercise the scenario:** An Ubuntu image's manual networkd edit disappears at reboot because Netplan owns generation; update Netplan and test with its rollback safeguards.
4. **Verify this outcome:** use `systemctl is-active NetworkManager systemd-networkd 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Determine active renderer on that exact release/image.

    **Distro/release distinction:** NetworkManager is common on RHEL; Ubuntu may use Netplan with NetworkManager or systemd-networkd. firewalld/UFW are frontends, while nftables is the kernel rules framework. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** An Ubuntu image's manual networkd edit disappears at reboot because Netplan owns generation; update Netplan and test with its rollback safeguards. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
systemctl is-active NetworkManager systemd-networkd 2>/dev/null
nmcli device status 2>/dev/null
netplan get 2>/dev/null
```

## Do's and Don'ts

- **Do:** Inspect running managers and their source configuration; check Netplan renderer where present and use the owning tool's validation/rollback process.
- **Don't:** Do not flush/change routes, firewall, resolver or interface settings on a remote host without out-of-band access and a tested rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

An Ubuntu image's manual networkd edit disappears at reboot because Netplan owns generation; update Netplan and test with its rollback safeguards. **Operator response:** Inspect running managers and their source configuration; check Netplan renderer where present and use the owning tool's validation/rollback process. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: NetworkManager/nmcli, Netplan, systemd-networkd and cloud-init may be control planes or frontends; generated backend files can be overwritten.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemctl is-active NetworkManager systemd-networkd 2>/dev/null` and follow the evidence path: Inspect running managers and their source configuration; check Netplan renderer where present and use the owning tool's validation/rollback process.

**Q: How would you verify or falsify the working diagnosis?**

A: An Ubuntu image's manual networkd edit disappears at reboot because Netplan owns generation; update Netplan and test with its rollback safeguards. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
