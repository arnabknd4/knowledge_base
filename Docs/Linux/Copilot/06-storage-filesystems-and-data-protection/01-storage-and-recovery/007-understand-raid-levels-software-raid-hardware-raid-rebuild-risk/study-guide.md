# Understand RAID levels, software RAID, hardware RAID, rebuild risk, and why RAID is not a backup.

**Syllabus objective (exact wording):** Understand RAID levels, software RAID, hardware RAID, rebuild risk, and why RAID is not a backup.

**Mapping:** `06` → `007` `Understand RAID levels, software RAID, hardware RAID, rebuild risk, and why RAID is not a backup.`

## What

RAID trades capacity/performance for tolerance of specified device failures; rebuilds increase load and degraded-array risk. It does not protect against deletion, corruption, ransomware or site loss.

## Why

This matters operationally: A degraded mirror during peak I/O needs a risk assessment before replacing a member; confirm backup integrity and vendor/controller replacement procedure first. The decision hinges on these mechanics: It does not protect against deletion, corruption, ransomware or site loss.

## How

1. **Establish the relevant boundary:** RAID trades capacity/performance for tolerance of specified device failures; rebuilds increase load and degraded-array risk. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Identify RAID level, member health, spare/rebuild behavior and controller dependency; ensure independent backup and monitor rebuild completion.
3. **Exercise the scenario:** A degraded mirror during peak I/O needs a risk assessment before replacing a member; confirm backup integrity and vendor/controller replacement procedure first.
4. **Verify this outcome:** use `cat /proc/mdstat` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** It does not protect against deletion, corruption, ransomware or site loss.

    **Distro/release distinction:** RHEL storage guidance commonly covers XFS/LVM; Debian/Ubuntu deployments may use ext4 or other layouts. Filesystem grow/repair tooling and cloud-volume contracts differ; verify exact support. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A degraded mirror during peak I/O needs a risk assessment before replacing a member; confirm backup integrity and vendor/controller replacement procedure first. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
cat /proc/mdstat
mdadm --detail /dev/mdX 2>/dev/null
lsblk -f
```

## Do's and Don'ts

- **Do:** Identify RAID level, member health, spare/rebuild behavior and controller dependency; ensure independent backup and monitor rebuild completion.
- **Don't:** Do not partition, format, repair, resize, alter RAID/LVM or delete data outside an isolated lab and separately approved change with verified backups.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A degraded mirror during peak I/O needs a risk assessment before replacing a member; confirm backup integrity and vendor/controller replacement procedure first. **Operator response:** Identify RAID level, member health, spare/rebuild behavior and controller dependency; ensure independent backup and monitor rebuild completion. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: RAID trades capacity/performance for tolerance of specified device failures; rebuilds increase load and degraded-array risk.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `cat /proc/mdstat` and follow the evidence path: Identify RAID level, member health, spare/rebuild behavior and controller dependency; ensure independent backup and monitor rebuild completion.

**Q: How would you verify or falsify the working diagnosis?**

A: A degraded mirror during peak I/O needs a risk assessment before replacing a member; confirm backup integrity and vendor/controller replacement procedure first. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
