# Read service state and journal logs; correlate boot ID, timestamps, unit dependencies, and recent configuration changes.

**Syllabus objective (exact wording):** Read service state and journal logs; correlate boot ID, timestamps, unit dependencies, and recent configuration changes.

**Mapping:** `04` → `007` `Read service state and journal logs; correlate boot ID, timestamps, unit dependencies, and recent configuration changes.`

## What

Journal records need host, boot ID, timestamp and unit context; persistent journal availability depends on configuration and distro defaults. Correlate transitions rather than reading only the current status summary.

## Why

This matters operationally: A failure vanishes after restart; inspect previous-boot messages and identify the first causal error rather than treating the last cascade as root cause. The decision hinges on these mechanics: Correlate transitions rather than reading only the current status summary.

## How

1. **Establish the relevant boundary:** Journal records need host, boot ID, timestamp and unit context; persistent journal availability depends on configuration and distro defaults. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Query a bounded time and boot, include kernel/unit messages, and compare with deployment timestamps. Preserve incident records before rotation or reboot.
3. **Exercise the scenario:** A failure vanishes after restart; inspect previous-boot messages and identify the first causal error rather than treating the last cascade as root cause.
4. **Verify this outcome:** use `journalctl -u <unit> -b --no-pager` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Correlate transitions rather than reading only the current status summary.

    **Distro/release distinction:** Current RHEL and Debian/Ubuntu releases commonly use systemd, but unit files, packaged defaults, journal persistence and legacy SysV compatibility differ. Read the installed merged unit. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A failure vanishes after restart; inspect previous-boot messages and identify the first causal error rather than treating the last cascade as root cause. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
journalctl -u <unit> -b --no-pager
journalctl -k -b -1 --no-pager
journalctl --list-boots
```

## Do's and Don'ts

- **Do:** Query a bounded time and boot, include kernel/unit messages, and compare with deployment timestamps. Preserve incident records before rotation or reboot.
- **Don't:** Do not force-kill or reboot before preserving relevant process and boot evidence; do not assume restart and reload have the same semantics.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A failure vanishes after restart; inspect previous-boot messages and identify the first causal error rather than treating the last cascade as root cause. **Operator response:** Query a bounded time and boot, include kernel/unit messages, and compare with deployment timestamps. Preserve incident records before rotation or reboot. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Journal records need host, boot ID, timestamp and unit context; persistent journal availability depends on configuration and distro defaults.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `journalctl -u <unit> -b --no-pager` and follow the evidence path: Query a bounded time and boot, include kernel/unit messages, and compare with deployment timestamps. Preserve incident records before rotation or reboot.

**Q: How would you verify or falsify the working diagnosis?**

A: A failure vanishes after restart; inspect previous-boot messages and identify the first causal error rather than treating the last cascade as root cause. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
