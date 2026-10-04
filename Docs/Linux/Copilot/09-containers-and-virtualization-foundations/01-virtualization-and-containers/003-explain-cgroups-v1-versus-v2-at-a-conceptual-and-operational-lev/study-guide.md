# Explain cgroups v1 versus v2 at a conceptual and operational level: resource accounting, limits, pressure, and delegation.

**Syllabus objective (exact wording):** Explain cgroups v1 versus v2 at a conceptual and operational level: resource accounting, limits, pressure, and delegation.

**Mapping:** `09` → `003` `Explain cgroups v1 versus v2 at a conceptual and operational level: resource accounting, limits, pressure, and delegation.`

## What

cgroup v1 uses multiple controller hierarchies; v2 uses a unified hierarchy with different delegation and controller semantics. Runtime/systemd integration determines effective resource accounting.

## Why

This matters operationally: A monitoring agent reports no memory limit on a v2 host because it reads v1 files; feature-detect `/sys/fs/cgroup` and verify cgroup events. The decision hinges on these mechanics: Runtime/systemd integration determines effective resource accounting.

## How

1. **Establish the relevant boundary:** cgroup v1 uses multiple controller hierarchies; v2 uses a unified hierarchy with different delegation and controller semantics. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Detect mounted hierarchy and process cgroup path, inspect available controllers and runtime delegation; do not translate v1 limit names directly to v2.
3. **Exercise the scenario:** A monitoring agent reports no memory limit on a v2 host because it reads v1 files; feature-detect `/sys/fs/cgroup` and verify cgroup events.
4. **Verify this outcome:** use `stat -fc %T /sys/fs/cgroup` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Runtime/systemd integration determines effective resource accounting.

    **Distro/release distinction:** The running kernel and distribution/runtime determine cgroup v1/v2, delegation, rootless support and default seccomp/LSM profile. Never infer effective limits from config intent alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A monitoring agent reports no memory limit on a v2 host because it reads v1 files; feature-detect `/sys/fs/cgroup` and verify cgroup events. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
stat -fc %T /sys/fs/cgroup
cat /proc/self/cgroup
systemd-cgls --no-pager 2>/dev/null
cat /sys/fs/cgroup/cgroup.controllers 2>/dev/null
```

## Do's and Don'ts

- **Do:** Detect mounted hierarchy and process cgroup path, inspect available controllers and runtime delegation; do not translate v1 limit names directly to v2.
- **Don't:** Do not grant privileged-container access, expose the host runtime socket, or treat namespaces alone as a security boundary.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A monitoring agent reports no memory limit on a v2 host because it reads v1 files; feature-detect `/sys/fs/cgroup` and verify cgroup events. **Operator response:** Detect mounted hierarchy and process cgroup path, inspect available controllers and runtime delegation; do not translate v1 limit names directly to v2. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: cgroup v1 uses multiple controller hierarchies; v2 uses a unified hierarchy with different delegation and controller semantics.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `stat -fc %T /sys/fs/cgroup` and follow the evidence path: Detect mounted hierarchy and process cgroup path, inspect available controllers and runtime delegation; do not translate v1 limit names directly to v2.

**Q: How would you verify or falsify the working diagnosis?**

A: A monitoring agent reports no memory limit on a v2 host because it reads v1 files; feature-detect `/sys/fs/cgroup` and verify cgroup events. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
