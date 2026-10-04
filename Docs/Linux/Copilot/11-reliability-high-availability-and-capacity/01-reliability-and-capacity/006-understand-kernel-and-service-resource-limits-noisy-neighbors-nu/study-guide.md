# Understand kernel and service resource limits, noisy neighbors, NUMA, cgroup controls, and cloud instance sizing.

**Syllabus objective (exact wording):** Understand kernel and service resource limits, noisy neighbors, NUMA, cgroup controls, and cloud instance sizing.

**Mapping:** `11` → `006` `Understand kernel and service resource limits, noisy neighbors, NUMA, cgroup controls, and cloud instance sizing.`

## What

Kernel, systemd, cgroup and cloud instance limits interact; NUMA locality and noisy neighbors change actual capacity. Tune resource boundaries without starving recovery/system work.

## Why

This matters operationally: A container hits CPU quota while the host is idle; inspect cgroup `cpu.max` and scheduler period before resizing the VM. The decision hinges on these mechanics: Tune resource boundaries without starving recovery/system work.

## How

1. **Establish the relevant boundary:** Kernel, systemd, cgroup and cloud instance limits interact; NUMA locality and noisy neighbors change actual capacity. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect effective per-service and cgroup limits alongside host topology/pressure; test under contention and monitor system services and application tails.
3. **Exercise the scenario:** A container hits CPU quota while the host is idle; inspect cgroup `cpu.max` and scheduler period before resizing the VM.
4. **Verify this outcome:** use `lscpu` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Tune resource boundaries without starving recovery/system work.

    **Distro/release distinction:** Pacemaker/Corosync, fencing agents, support contracts and cloud zone/region guarantees are platform-specific; validate the exact supported combination and failure model. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A container hits CPU quota while the host is idle; inspect cgroup `cpu.max` and scheduler period before resizing the VM. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
lscpu
systemctl show <unit> -p CPUQuotaPerSecUSec -p MemoryMax -p TasksMax
cat /proc/<pid>/cgroup
cat /sys/fs/cgroup/cpu.max 2>/dev/null
```

## Do's and Don'ts

- **Do:** Inspect effective per-service and cgroup limits alongside host topology/pressure; test under contention and monitor system services and application tails.
- **Don't:** Do not call a design highly available without testing failover, fencing/state consistency, measured recovery and failure-domain independence.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A container hits CPU quota while the host is idle; inspect cgroup `cpu.max` and scheduler period before resizing the VM. **Operator response:** Inspect effective per-service and cgroup limits alongside host topology/pressure; test under contention and monitor system services and application tails. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Kernel, systemd, cgroup and cloud instance limits interact; NUMA locality and noisy neighbors change actual capacity.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `lscpu` and follow the evidence path: Inspect effective per-service and cgroup limits alongside host topology/pressure; test under contention and monitor system services and application tails.

**Q: How would you verify or falsify the working diagnosis?**

A: A container hits CPU quota while the host is idle; inspect cgroup `cpu.max` and scheduler period before resizing the VM. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
