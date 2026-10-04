# Inspect the relationship between systemd, cgroups, container runtime, and workload resource limits.

**Syllabus objective (exact wording):** Inspect the relationship between systemd, cgroups, container runtime, and workload resource limits.

**Mapping:** `09` → `006` `Inspect the relationship between systemd, cgroups, container runtime, and workload resource limits.`

## What

systemd can own cgroups and delegate subtrees to runtimes; resource limits at unit and workload levels may combine or conflict. Effective cgroup placement matters more than desired YAML.

## Why

This matters operationally: A service-level memory ceiling competes with a runtime container limit; inspect `memory.max` and OOM events from the actual cgroup. The decision hinges on these mechanics: Effective cgroup placement matters more than desired YAML.

## How

1. **Establish the relevant boundary:** systemd can own cgroups and delegate subtrees to runtimes; resource limits at unit and workload levels may combine or conflict. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect systemd unit cgroup properties and the container's actual cgroup path/limits; assign one clear owner per control and verify enforcement under load.
3. **Exercise the scenario:** A service-level memory ceiling competes with a runtime container limit; inspect `memory.max` and OOM events from the actual cgroup.
4. **Verify this outcome:** use `systemd-cgls --no-pager` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Effective cgroup placement matters more than desired YAML.

    **Distro/release distinction:** The running kernel and distribution/runtime determine cgroup v1/v2, delegation, rootless support and default seccomp/LSM profile. Never infer effective limits from config intent alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A service-level memory ceiling competes with a runtime container limit; inspect `memory.max` and OOM events from the actual cgroup. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
systemd-cgls --no-pager
systemctl show <unit> -p ControlGroup -p MemoryMax -p CPUQuotaPerSecUSec
cat /proc/<pid>/cgroup
```

## Do's and Don'ts

- **Do:** Inspect systemd unit cgroup properties and the container's actual cgroup path/limits; assign one clear owner per control and verify enforcement under load.
- **Don't:** Do not grant privileged-container access, expose the host runtime socket, or treat namespaces alone as a security boundary.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A service-level memory ceiling competes with a runtime container limit; inspect `memory.max` and OOM events from the actual cgroup. **Operator response:** Inspect systemd unit cgroup properties and the container's actual cgroup path/limits; assign one clear owner per control and verify enforcement under load. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: systemd can own cgroups and delegate subtrees to runtimes; resource limits at unit and workload levels may combine or conflict.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemd-cgls --no-pager` and follow the evidence path: Inspect systemd unit cgroup properties and the container's actual cgroup path/limits; assign one clear owner per control and verify enforcement under load.

**Q: How would you verify or falsify the working diagnosis?**

A: A service-level memory ceiling competes with a runtime container limit; inspect `memory.max` and OOM events from the actual cgroup. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
