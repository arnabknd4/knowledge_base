# Describe BIOS/UEFI, firmware, bootloader (commonly GRUB), kernel and initramfs, root filesystem handoff, and PID 1.

**Syllabus objective (exact wording):** Describe BIOS/UEFI, firmware, bootloader (commonly GRUB), kernel and initramfs, root filesystem handoff, and PID 1.

**Mapping:** `01` → `006` `Describe BIOS/UEFI, firmware, bootloader (commonly GRUB), kernel and initramfs, root filesystem handoff, and PID 1.`

## What

UEFI/BIOS initializes hardware and selects a boot path; a bootloader loads a kernel and initramfs, which discovers/mounts root and hands control to PID 1. Firmware mode, boot entries and initramfs contents determine recovery options.

## Why

This matters operationally: A VM drops to an initramfs emergency shell after a volume UUID changes; distinguish root discovery from systemd/service startup and use console recovery rather than repeated remote reboot. The decision hinges on these mechanics: Firmware mode, boot entries and initramfs contents determine recovery options.

## How

1. **Establish the relevant boundary:** UEFI/BIOS initializes hardware and selects a boot path; a bootloader loads a kernel and initramfs, which discovers/mounts root and hands control to PID 1. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Read current boot mode, boot entries and kernel command line; map the root device and initramfs dependencies. Before changing entries, confirm console access and a known-good alternative kernel.
3. **Exercise the scenario:** A VM drops to an initramfs emergency shell after a volume UUID changes; distinguish root discovery from systemd/service startup and use console recovery rather than repeated remote reboot.
4. **Verify this outcome:** use `test -d /sys/firmware/efi && echo UEFI || echo BIOS` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Firmware mode, boot entries and initramfs contents determine recovery options.

    **Distro/release distinction:** RHEL-family kernels may carry vendor backports and ABI/support commitments; Debian/Ubuntu releases package their kernel and user space on their own lifecycle. A distribution combines kernel and user-space components rather than being the kernel alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A VM drops to an initramfs emergency shell after a volume UUID changes; distinguish root discovery from systemd/service startup and use console recovery rather than repeated remote reboot. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
test -d /sys/firmware/efi && echo UEFI || echo BIOS
cat /proc/cmdline
lsblk -f
bootctl status 2>/dev/null
```

## Do's and Don'ts

- **Do:** Read current boot mode, boot entries and kernel command line; map the root device and initramfs dependencies. Before changing entries, confirm console access and a known-good alternative kernel.
- **Don't:** Do not infer support or patch state from a kernel version string, install packages from an untrusted repository, or edit boot configuration without a console and tested recovery path.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A VM drops to an initramfs emergency shell after a volume UUID changes; distinguish root discovery from systemd/service startup and use console recovery rather than repeated remote reboot. **Operator response:** Read current boot mode, boot entries and kernel command line; map the root device and initramfs dependencies. Before changing entries, confirm console access and a known-good alternative kernel. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: UEFI/BIOS initializes hardware and selects a boot path; a bootloader loads a kernel and initramfs, which discovers/mounts root and hands control to PID 1.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `test -d /sys/firmware/efi && echo UEFI || echo BIOS` and follow the evidence path: Read current boot mode, boot entries and kernel command line; map the root device and initramfs dependencies. Before changing entries, confirm console access and a known-good alternative kernel.

**Q: How would you verify or falsify the working diagnosis?**

A: A VM drops to an initramfs emergency shell after a volume UUID changes; distinguish root discovery from systemd/service startup and use console recovery rather than repeated remote reboot. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
