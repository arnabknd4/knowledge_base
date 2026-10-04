# Understand swap purpose and behavior; use workload and memory evidence when evaluating swap configuration.

**Syllabus objective (exact wording):** Understand swap purpose and behavior; use workload and memory evidence when evaluating swap configuration.

**Mapping:** `06` → `008` `Understand swap purpose and behavior; use workload and memory evidence when evaluating swap configuration.`

## What

Swap supplies a backing/pressure mechanism and may support hibernation; performance depends on device and workload. Swappiness is not a direct memory limit and universal sizing rules are unsafe.

## Why

This matters operationally: A latency-critical service stalls under swap thrash despite no OOM; quantify major faults and swap I/O before changing memory/capacity policy. The decision hinges on these mechanics: Swappiness is not a direct memory limit and universal sizing rules are unsafe.

## How

1. **Establish the relevant boundary:** Swap supplies a backing/pressure mechanism and may support hibernation; performance depends on device and workload. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Correlate swap-in/out, memory PSI, OOMs, workload latency and hibernation requirements; compare policy with vendor defaults before resizing.
3. **Exercise the scenario:** A latency-critical service stalls under swap thrash despite no OOM; quantify major faults and swap I/O before changing memory/capacity policy.
4. **Verify this outcome:** use `swapon --show` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Swappiness is not a direct memory limit and universal sizing rules are unsafe.

    **Distro/release distinction:** RHEL storage guidance commonly covers XFS/LVM; Debian/Ubuntu deployments may use ext4 or other layouts. Filesystem grow/repair tooling and cloud-volume contracts differ; verify exact support. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A latency-critical service stalls under swap thrash despite no OOM; quantify major faults and swap I/O before changing memory/capacity policy. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
swapon --show
free -h
vmstat 1 5
cat /proc/pressure/memory 2>/dev/null
```

## Do's and Don'ts

- **Do:** Correlate swap-in/out, memory PSI, OOMs, workload latency and hibernation requirements; compare policy with vendor defaults before resizing.
- **Don't:** Do not partition, format, repair, resize, alter RAID/LVM or delete data outside an isolated lab and separately approved change with verified backups.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A latency-critical service stalls under swap thrash despite no OOM; quantify major faults and swap I/O before changing memory/capacity policy. **Operator response:** Correlate swap-in/out, memory PSI, OOMs, workload latency and hibernation requirements; compare policy with vendor defaults before resizing. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Swap supplies a backing/pressure mechanism and may support hibernation; performance depends on device and workload.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `swapon --show` and follow the evidence path: Correlate swap-in/out, memory PSI, OOMs, workload latency and hibernation requirements; compare policy with vendor defaults before resizing.

**Q: How would you verify or falsify the working diagnosis?**

A: A latency-critical service stalls under swap thrash despite no OOM; quantify major faults and swap I/O before changing memory/capacity policy. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
