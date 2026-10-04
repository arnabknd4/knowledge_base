# Interpret load average in context; distinguish runnable work, CPU saturation, I/O wait, and blocked tasks.

**Syllabus objective (exact wording):** Interpret load average in context; distinguish runnable work, CPU saturation, I/O wait, and blocked tasks.

**Mapping:** `05` → `001` `Interpret load average in context; distinguish runnable work, CPU saturation, I/O wait, and blocked tasks.`

## What

Load average represents runnable plus certain uninterruptible tasks over averaging windows; interpret it against CPU count, I/O waits and trends. It is not a percentage of CPU usage.

## Why

This matters operationally: Load rises to 20 on a 32-vCPU database host while CPU is low; inspect blocked tasks and storage latency before resizing CPUs. The decision hinges on these mechanics: It is not a percentage of CPU usage.

## How

1. **Establish the relevant boundary:** Load average represents runnable plus certain uninterruptible tasks over averaging windows; interpret it against CPU count, I/O waits and trends. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Compare runnable queue, blocked tasks, CPU utilization and disk latency over the same interval; identify whether growth is CPU, I/O or lock contention.
3. **Exercise the scenario:** Load rises to 20 on a 32-vCPU database host while CPU is low; inspect blocked tasks and storage latency before resizing CPUs.
4. **Verify this outcome:** use `uptime` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** It is not a percentage of CPU usage.

    **Distro/release distinction:** PSI, perf/eBPF capabilities and sysstat tools depend on kernel config/version and distro packages. Install or enable tooling only through supported package and policy workflows. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Load rises to 20 on a 32-vCPU database host while CPU is low; inspect blocked tasks and storage latency before resizing CPUs. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
uptime
nproc
vmstat 1 5
iostat -xz 1 3 2>/dev/null
```

## Do's and Don'ts

- **Do:** Compare runnable queue, blocked tasks, CPU utilization and disk latency over the same interval; identify whether growth is CPU, I/O or lock contention.
- **Don't:** Do not tune from a single metric snapshot or copy generic sysctl values; profiling and eBPF need bounded scope, authorization and overhead review.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Load rises to 20 on a 32-vCPU database host while CPU is low; inspect blocked tasks and storage latency before resizing CPUs. **Operator response:** Compare runnable queue, blocked tasks, CPU utilization and disk latency over the same interval; identify whether growth is CPU, I/O or lock contention. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Load average represents runnable plus certain uninterruptible tasks over averaging windows; interpret it against CPU count, I/O waits and trends.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `uptime` and follow the evidence path: Compare runnable queue, blocked tasks, CPU utilization and disk latency over the same interval; identify whether growth is CPU, I/O or lock contention.

**Q: How would you verify or falsify the working diagnosis?**

A: Load rises to 20 on a 32-vCPU database host while CPU is low; inspect blocked tasks and storage latency before resizing CPUs. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
