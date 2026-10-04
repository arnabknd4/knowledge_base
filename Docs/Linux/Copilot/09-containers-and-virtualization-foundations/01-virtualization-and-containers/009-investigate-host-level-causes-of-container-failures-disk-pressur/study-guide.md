# Investigate host-level causes of container failures: disk pressure, inode exhaustion, cgroup limits, DNS, routes, clocks, and kernel compatibility (D, S).

**Syllabus objective (exact wording):** Investigate host-level causes of container failures: disk pressure, inode exhaustion, cgroup limits, DNS, routes, clocks, and kernel compatibility (D, S).

**Mapping:** `09` → `009` `Investigate host-level causes of container failures: disk pressure, inode exhaustion, cgroup limits, DNS, routes, clocks, and kernel compatibility (D, S).`

## What

Container failures often originate in host disk/inodes, kernel compatibility, cgroup limits, DNS/routes, clock or storage pressure rather than application code. Evidence must align container and host identities.

## Why

This matters operationally: Many pods on one node fail DNS after resolver config changes; compare node and pod resolver/routing state and recent CNI changes before rebuilding apps. The decision hinges on these mechanics: Evidence must align container and host identities.

## How

1. **Establish the relevant boundary:** Container failures often originate in host disk/inodes, kernel compatibility, cgroup limits, DNS/routes, clock or storage pressure rather than application code. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Correlate container events and cgroup counters with host PSI, filesystem, resolver/route and kernel logs; test from the same namespace before restarting.
3. **Exercise the scenario:** Many pods on one node fail DNS after resolver config changes; compare node and pod resolver/routing state and recent CNI changes before rebuilding apps.
4. **Verify this outcome:** use `df -hT` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Evidence must align container and host identities.

    **Distro/release distinction:** The running kernel and distribution/runtime determine cgroup v1/v2, delegation, rootless support and default seccomp/LSM profile. Never infer effective limits from config intent alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Many pods on one node fail DNS after resolver config changes; compare node and pod resolver/routing state and recent CNI changes before rebuilding apps. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
df -hT
df -i
cat /proc/pressure/{cpu,memory,io} 2>/dev/null
journalctl -k -b --no-pager | tail -60
```

## Do's and Don'ts

- **Do:** Correlate container events and cgroup counters with host PSI, filesystem, resolver/route and kernel logs; test from the same namespace before restarting.
- **Don't:** Do not grant privileged-container access, expose the host runtime socket, or treat namespaces alone as a security boundary.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Many pods on one node fail DNS after resolver config changes; compare node and pod resolver/routing state and recent CNI changes before rebuilding apps. **Operator response:** Correlate container events and cgroup counters with host PSI, filesystem, resolver/route and kernel logs; test from the same namespace before restarting. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Container failures often originate in host disk/inodes, kernel compatibility, cgroup limits, DNS/routes, clock or storage pressure rather than application code.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `df -hT` and follow the evidence path: Correlate container events and cgroup counters with host PSI, filesystem, resolver/route and kernel logs; test from the same namespace before restarting.

**Q: How would you verify or falsify the working diagnosis?**

A: Many pods on one node fail DNS after resolver config changes; compare node and pod resolver/routing state and recent CNI changes before rebuilding apps. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
