# Understand host firewalls, SSH policy, disk encryption, secure boot, identity integration, and audit requirements in context.

**Syllabus objective (exact wording):** Understand host firewalls, SSH policy, disk encryption, secure boot, identity integration, and audit requirements in context.

**Mapping:** `08` → `012` `Understand host firewalls, SSH policy, disk encryption, secure boot, identity integration, and audit requirements in context.`

## What

Host firewall, SSH, encryption, secure boot, identity integration and audit controls solve distinct threats and depend on operational context. A control can lock out responders or prevent boot if recovery is ignored.

## Why

This matters operationally: A policy requires encrypted disks but no one tested recovery-key retrieval; verify key escrow and restore procedures before fleet rollout. The decision hinges on these mechanics: A control can lock out responders or prevent boot if recovery is ignored.

## How

1. **Establish the relevant boundary:** Host firewall, SSH, encryption, secure boot, identity integration and audit controls solve distinct threats and depend on operational context. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Document allowed flows and break-glass paths; check current firewall backend, key/encryption recovery custody, support lifecycle and audit evidence before enforcing.
3. **Exercise the scenario:** A policy requires encrypted disks but no one tested recovery-key retrieval; verify key escrow and restore procedures before fleet rollout.
4. **Verify this outcome:** use `nft list ruleset 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** A control can lock out responders or prevent boot if recovery is ignored.

    **Distro/release distinction:** SELinux is central on RHEL-family systems and AppArmor common on Ubuntu; package-signing, audit, Secure Boot and baseline tooling have release-specific procedures. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A policy requires encrypted disks but no one tested recovery-key retrieval; verify key escrow and restore procedures before fleet rollout. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
nft list ruleset 2>/dev/null
sshd -T 2>/dev/null | head
lsblk -f
mokutil --sb-state 2>/dev/null
```

## Do's and Don'ts

- **Do:** Document allowed flows and break-glass paths; check current firewall backend, key/encryption recovery custody, support lifecycle and audit evidence before enforcing.
- **Don't:** Do not disable SELinux/AppArmor, expose private keys/secrets, or run an opaque hardening script as a substitute for policy diagnosis.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A policy requires encrypted disks but no one tested recovery-key retrieval; verify key escrow and restore procedures before fleet rollout. **Operator response:** Document allowed flows and break-glass paths; check current firewall backend, key/encryption recovery custody, support lifecycle and audit evidence before enforcing. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Host firewall, SSH, encryption, secure boot, identity integration and audit controls solve distinct threats and depend on operational context.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `nft list ruleset 2>/dev/null` and follow the evidence path: Document allowed flows and break-glass paths; check current firewall backend, key/encryption recovery custody, support lifecycle and audit evidence before enforcing.

**Q: How would you verify or falsify the working diagnosis?**

A: A policy requires encrypted disks but no one tested recovery-key retrieval; verify key escrow and restore procedures before fleet rollout. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
