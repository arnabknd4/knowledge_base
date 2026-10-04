# Understand virtual memory, page cache, reclaim, swap, overcommit, OOM behavior, NUMA basics, and container memory limits.

**Syllabus objective (exact wording):** Understand virtual memory, page cache, reclaim, swap, overcommit, OOM behavior, NUMA basics, and container memory limits.

**Mapping:** `05` → `002` `Understand virtual memory, page cache, reclaim, swap, overcommit, OOM behavior, NUMA basics, and container memory limits.`

## What

Virtual memory includes resident pages, reclaimable cache, swap and overcommit; cgroup limits may OOM a container while host memory remains available. NUMA placement affects locality.

## Why

This matters operationally: One container restarts with OOMKilled on a host with free memory; inspect its memory.max/events and workload peak rather than host `free` alone. The decision hinges on these mechanics: NUMA placement affects locality.

## How

1. **Establish the relevant boundary:** Virtual memory includes resident pages, reclaimable cache, swap and overcommit; cgroup limits may OOM a container while host memory remains available. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Correlate `MemAvailable`, swap-in/out, PSI, kernel OOM events and cgroup `memory.events`; distinguish reclaim from sustained allocation pressure.
3. **Exercise the scenario:** One container restarts with OOMKilled on a host with free memory; inspect its memory.max/events and workload peak rather than host `free` alone.
4. **Verify this outcome:** use `free -h` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** NUMA placement affects locality.

    **Distro/release distinction:** PSI, perf/eBPF capabilities and sysstat tools depend on kernel config/version and distro packages. Install or enable tooling only through supported package and policy workflows. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** One container restarts with OOMKilled on a host with free memory; inspect its memory.max/events and workload peak rather than host `free` alone. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
free -h
cat /proc/pressure/memory 2>/dev/null
cat /sys/fs/cgroup/memory.events 2>/dev/null
journalctl -k -b --no-pager | grep -i oom
```

## Do's and Don'ts

- **Do:** Correlate `MemAvailable`, swap-in/out, PSI, kernel OOM events and cgroup `memory.events`; distinguish reclaim from sustained allocation pressure.
- **Don't:** Do not tune from a single metric snapshot or copy generic sysctl values; profiling and eBPF need bounded scope, authorization and overhead review.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

One container restarts with OOMKilled on a host with free memory; inspect its memory.max/events and workload peak rather than host `free` alone. **Operator response:** Correlate `MemAvailable`, swap-in/out, PSI, kernel OOM events and cgroup `memory.events`; distinguish reclaim from sustained allocation pressure. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Virtual memory includes resident pages, reclaimable cache, swap and overcommit; cgroup limits may OOM a container while host memory remains available.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `free -h` and follow the evidence path: Correlate `MemAvailable`, swap-in/out, PSI, kernel OOM events and cgroup `memory.events`; distinguish reclaim from sustained allocation pressure.

**Q: How would you verify or falsify the working diagnosis?**

A: One container restarts with OOMKilled on a host with free memory; inspect its memory.max/events and workload peak rather than host `free` alone. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
