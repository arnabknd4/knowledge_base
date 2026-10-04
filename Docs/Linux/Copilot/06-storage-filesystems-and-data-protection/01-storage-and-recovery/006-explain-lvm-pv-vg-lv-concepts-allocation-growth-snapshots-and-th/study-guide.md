# Explain LVM PV/VG/LV concepts, allocation, growth, snapshots, and the distinction between growing a block layer and growing a filesystem.

**Syllabus objective (exact wording):** Explain LVM PV/VG/LV concepts, allocation, growth, snapshots, and the distinction between growing a block layer and growing a filesystem.

**Mapping:** `06` → `006` `Explain LVM PV/VG/LV concepts, allocation, growth, snapshots, and the distinction between growing a block layer and growing a filesystem.`

## What

LVM separates physical volumes, volume groups and logical volumes; snapshots consume pool capacity. Growing a block layer and expanding a filesystem are distinct steps with filesystem-specific rules.

## Why

This matters operationally: A database volume is short of space; confirm VG free capacity and filesystem growth support before proposing a maintenance window and rollback. The decision hinges on these mechanics: Growing a block layer and expanding a filesystem are distinct steps with filesystem-specific rules.

## How

1. **Establish the relevant boundary:** LVM separates physical volumes, volume groups and logical volumes; snapshots consume pool capacity. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect PV/VG/LV free extents and filesystem type first; plan each layer's supported growth sequence and monitor snapshot space. Treat all mutation commands as lab-only in these guides.
3. **Exercise the scenario:** A database volume is short of space; confirm VG free capacity and filesystem growth support before proposing a maintenance window and rollback.
4. **Verify this outcome:** use `pvs` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Growing a block layer and expanding a filesystem are distinct steps with filesystem-specific rules.

    **Distro/release distinction:** RHEL storage guidance commonly covers XFS/LVM; Debian/Ubuntu deployments may use ext4 or other layouts. Filesystem grow/repair tooling and cloud-volume contracts differ; verify exact support. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A database volume is short of space; confirm VG free capacity and filesystem growth support before proposing a maintenance window and rollback. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
pvs
vgs
lvs -a -o +devices
df -hT
```

## Do's and Don'ts

- **Do:** Inspect PV/VG/LV free extents and filesystem type first; plan each layer's supported growth sequence and monitor snapshot space. Treat all mutation commands as lab-only in these guides.
- **Don't:** Do not partition, format, repair, resize, alter RAID/LVM or delete data outside an isolated lab and separately approved change with verified backups.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A database volume is short of space; confirm VG free capacity and filesystem growth support before proposing a maintenance window and rollback. **Operator response:** Inspect PV/VG/LV free extents and filesystem type first; plan each layer's supported growth sequence and monitor snapshot space. Treat all mutation commands as lab-only in these guides. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: LVM separates physical volumes, volume groups and logical volumes; snapshots consume pool capacity.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `pvs` and follow the evidence path: Inspect PV/VG/LV free extents and filesystem type first; plan each layer's supported growth sequence and monitor snapshot space. Treat all mutation commands as lab-only in these guides.

**Q: How would you verify or falsify the working diagnosis?**

A: A database volume is short of space; confirm VG free capacity and filesystem growth support before proposing a maintenance window and rollback. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
