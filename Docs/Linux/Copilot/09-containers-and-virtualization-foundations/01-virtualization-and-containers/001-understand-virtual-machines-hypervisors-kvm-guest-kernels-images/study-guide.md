# Understand virtual machines, hypervisors, KVM, guest kernels, images, and the host/guest responsibility boundary.

**Syllabus objective (exact wording):** Understand virtual machines, hypervisors, KVM, guest kernels, images, and the host/guest responsibility boundary.

**Mapping:** `09` → `001` `Understand virtual machines, hypervisors, KVM, guest kernels, images, and the host/guest responsibility boundary.`

## What

A VM virtualizes devices and runs its own guest kernel; the hypervisor/provider owns the host boundary and host maintenance. Guest images and agents remain operator responsibilities depending on service model.

## Why

This matters operationally: An instance has a guest filesystem outage although provider volume is healthy; inspect guest block/mount and kernel logs before escalating as hypervisor fault. The decision hinges on these mechanics: Guest images and agents remain operator responsibilities depending on service model.

## How

1. **Establish the relevant boundary:** A VM virtualizes devices and runs its own guest kernel; the hypervisor/provider owns the host boundary and host maintenance. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Record the provider responsibility split, guest kernel/image lifecycle, virtual device drivers and agent health; distinguish guest memory pressure from host contention.
3. **Exercise the scenario:** An instance has a guest filesystem outage although provider volume is healthy; inspect guest block/mount and kernel logs before escalating as hypervisor fault.
4. **Verify this outcome:** use `systemd-detect-virt` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Guest images and agents remain operator responsibilities depending on service model.

    **Distro/release distinction:** The running kernel and distribution/runtime determine cgroup v1/v2, delegation, rootless support and default seccomp/LSM profile. Never infer effective limits from config intent alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** An instance has a guest filesystem outage although provider volume is healthy; inspect guest block/mount and kernel logs before escalating as hypervisor fault. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
systemd-detect-virt
uname -r
lsblk -f
journalctl -k -b --no-pager | tail -50
```

## Do's and Don'ts

- **Do:** Record the provider responsibility split, guest kernel/image lifecycle, virtual device drivers and agent health; distinguish guest memory pressure from host contention.
- **Don't:** Do not grant privileged-container access, expose the host runtime socket, or treat namespaces alone as a security boundary.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

An instance has a guest filesystem outage although provider volume is healthy; inspect guest block/mount and kernel logs before escalating as hypervisor fault. **Operator response:** Record the provider responsibility split, guest kernel/image lifecycle, virtual device drivers and agent health; distinguish guest memory pressure from host contention. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: A VM virtualizes devices and runs its own guest kernel; the hypervisor/provider owns the host boundary and host maintenance.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemd-detect-virt` and follow the evidence path: Record the provider responsibility split, guest kernel/image lifecycle, virtual device drivers and agent health; distinguish guest memory pressure from host contention.

**Q: How would you verify or falsify the working diagnosis?**

A: An instance has a guest filesystem outage although provider volume is healthy; inspect guest block/mount and kernel logs before escalating as hypervisor fault. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
