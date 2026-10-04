# Recognize rescue/emergency boot paths, kernel command-line parameters, initramfs purpose, and recovery considerations (P1).

**Syllabus objective (exact wording):** Recognize rescue/emergency boot paths, kernel command-line parameters, initramfs purpose, and recovery considerations (P1).

**Mapping:** `01` → `007` `Recognize rescue/emergency boot paths, kernel command-line parameters, initramfs purpose, and recovery considerations (P1).`

## What

Rescue targets mount and start fewer resources than normal operation; emergency shells may have even less environment and access. Kernel command-line options and initramfs tools are boot-chain/release specific.

## Why

This matters operationally: A fstab error blocks normal boot; use the provider console and documented rescue path, preserve the failing entry, then validate mount syntax and reboot only after a recovery route is proven. The decision hinges on these mechanics: Kernel command-line options and initramfs tools are boot-chain/release specific.

## How

1. **Establish the relevant boundary:** Rescue targets mount and start fewer resources than normal operation; emergency shells may have even less environment and access. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Document console credentials, encryption keys, root-device dependencies and recovery steps; identify the target distribution's rescue/emergency semantics before testing a boot parameter.
3. **Exercise the scenario:** A fstab error blocks normal boot; use the provider console and documented rescue path, preserve the failing entry, then validate mount syntax and reboot only after a recovery route is proven.
4. **Verify this outcome:** use `systemctl get-default` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Kernel command-line options and initramfs tools are boot-chain/release specific.

    **Distro/release distinction:** RHEL-family kernels may carry vendor backports and ABI/support commitments; Debian/Ubuntu releases package their kernel and user space on their own lifecycle. A distribution combines kernel and user-space components rather than being the kernel alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A fstab error blocks normal boot; use the provider console and documented rescue path, preserve the failing entry, then validate mount syntax and reboot only after a recovery route is proven. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
systemctl get-default
cat /proc/cmdline
journalctl -b -p err --no-pager
systemctl list-units --failed --no-pager
```

## Do's and Don'ts

- **Do:** Document console credentials, encryption keys, root-device dependencies and recovery steps; identify the target distribution's rescue/emergency semantics before testing a boot parameter.
- **Don't:** Do not infer support or patch state from a kernel version string, install packages from an untrusted repository, or edit boot configuration without a console and tested recovery path.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A fstab error blocks normal boot; use the provider console and documented rescue path, preserve the failing entry, then validate mount syntax and reboot only after a recovery route is proven. **Operator response:** Document console credentials, encryption keys, root-device dependencies and recovery steps; identify the target distribution's rescue/emergency semantics before testing a boot parameter. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Rescue targets mount and start fewer resources than normal operation; emergency shells may have even less environment and access.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemctl get-default` and follow the evidence path: Document console credentials, encryption keys, root-device dependencies and recovery steps; identify the target distribution's rescue/emergency semantics before testing a boot parameter.

**Q: How would you verify or falsify the working diagnosis?**

A: A fstab error blocks normal boot; use the provider console and documented rescue path, preserve the failing entry, then validate mount syntax and reboot only after a recovery route is proven. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
