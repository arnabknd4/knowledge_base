# Diagnose boot failures using console access, previous-boot logs, rescue modes, initramfs, and known-good kernel selection.

**Syllabus objective (exact wording):** Diagnose boot failures using console access, previous-boot logs, rescue modes, initramfs, and known-good kernel selection.

**Mapping:** `04` → `009` `Diagnose boot failures using console access, previous-boot logs, rescue modes, initramfs, and known-good kernel selection.`

## What

Boot diagnosis follows firmware/bootloader → kernel/initramfs → root mount → PID 1 → units. Console access and previous-boot logs can distinguish phases; recovery options are release-specific.

## Why

This matters operationally: A kernel update leaves a VM at dracut/initramfs prompt; confirm root device and included storage driver rather than repeatedly selecting the failing default entry. The decision hinges on these mechanics: Console access and previous-boot logs can distinguish phases; recovery options are release-specific.

## How

1. **Establish the relevant boundary:** Boot diagnosis follows firmware/bootloader → kernel/initramfs → root mount → PID 1 → units. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Capture console errors and boot ID; test a known-good kernel/rescue path only with console and rollback. Check root UUID, initramfs drivers and recent boot configuration changes.
3. **Exercise the scenario:** A kernel update leaves a VM at dracut/initramfs prompt; confirm root device and included storage driver rather than repeatedly selecting the failing default entry.
4. **Verify this outcome:** use `journalctl -b -1 -p warning --no-pager` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Console access and previous-boot logs can distinguish phases; recovery options are release-specific.

    **Distro/release distinction:** Current RHEL and Debian/Ubuntu releases commonly use systemd, but unit files, packaged defaults, journal persistence and legacy SysV compatibility differ. Read the installed merged unit. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A kernel update leaves a VM at dracut/initramfs prompt; confirm root device and included storage driver rather than repeatedly selecting the failing default entry. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
journalctl -b -1 -p warning --no-pager
journalctl -k -b --no-pager
lsblk -f
cat /proc/cmdline
```

## Do's and Don'ts

- **Do:** Capture console errors and boot ID; test a known-good kernel/rescue path only with console and rollback. Check root UUID, initramfs drivers and recent boot configuration changes.
- **Don't:** Do not force-kill or reboot before preserving relevant process and boot evidence; do not assume restart and reload have the same semantics.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A kernel update leaves a VM at dracut/initramfs prompt; confirm root device and included storage driver rather than repeatedly selecting the failing default entry. **Operator response:** Capture console errors and boot ID; test a known-good kernel/rescue path only with console and rollback. Check root UUID, initramfs drivers and recent boot configuration changes. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Boot diagnosis follows firmware/bootloader → kernel/initramfs → root mount → PID 1 → units.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `journalctl -b -1 -p warning --no-pager` and follow the evidence path: Capture console errors and boot ID; test a known-good kernel/rescue path only with console and rollback. Check root UUID, initramfs drivers and recent boot configuration changes.

**Q: How would you verify or falsify the working diagnosis?**

A: A kernel update leaves a VM at dracut/initramfs prompt; confirm root device and included storage driver rather than repeatedly selecting the failing default entry. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
