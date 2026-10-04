# Plan backups around recovery-point and recovery-time objectives; include off-host/immutable copies, encryption, retention, and restore testing.

**Syllabus objective (exact wording):** Plan backups around recovery-point and recovery-time objectives; include off-host/immutable copies, encryption, retention, and restore testing.

**Mapping:** `06` → `011` `Plan backups around recovery-point and recovery-time objectives; include off-host/immutable copies, encryption, retention, and restore testing.`

## What

Backup design converts RPO/RTO into copy frequency, retention, off-host/immutable isolation, encryption, throughput and restore ownership. A completed job is not proof that data is recoverable.

## Why

This matters operationally: A ransomware exercise requires a clean recovery copy; prove credentials are separate, retention is immutable and a restore completes within agreed RTO. The decision hinges on these mechanics: A completed job is not proof that data is recoverable.

## How

1. **Establish the relevant boundary:** Backup design converts RPO/RTO into copy frequency, retention, off-host/immutable isolation, encryption, throughput and restore ownership. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Restore representative data into an isolated target; validate integrity/application consistency, start/end criteria, measured duration and data point against objectives.
3. **Exercise the scenario:** A ransomware exercise requires a clean recovery copy; prove credentials are separate, retention is immutable and a restore completes within agreed RTO.
4. **Verify this outcome:** use `restic snapshots 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** A completed job is not proof that data is recoverable.

    **Distro/release distinction:** RHEL storage guidance commonly covers XFS/LVM; Debian/Ubuntu deployments may use ext4 or other layouts. Filesystem grow/repair tooling and cloud-volume contracts differ; verify exact support. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A ransomware exercise requires a clean recovery copy; prove credentials are separate, retention is immutable and a restore completes within agreed RTO. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
restic snapshots 2>/dev/null
borg list <repo> 2>/dev/null
sha256sum <test-artifact>
```

## Do's and Don'ts

- **Do:** Restore representative data into an isolated target; validate integrity/application consistency, start/end criteria, measured duration and data point against objectives.
- **Don't:** Do not partition, format, repair, resize, alter RAID/LVM or delete data outside an isolated lab and separately approved change with verified backups.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A ransomware exercise requires a clean recovery copy; prove credentials are separate, retention is immutable and a restore completes within agreed RTO. **Operator response:** Restore representative data into an isolated target; validate integrity/application consistency, start/end criteria, measured duration and data point against objectives. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Backup design converts RPO/RTO into copy frequency, retention, off-host/immutable isolation, encryption, throughput and restore ownership.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `restic snapshots 2>/dev/null` and follow the evidence path: Restore representative data into an isolated target; validate integrity/application consistency, start/end criteria, measured duration and data point against objectives.

**Q: How would you verify or falsify the working diagnosis?**

A: A ransomware exercise requires a clean recovery copy; prove credentials are separate, retention is immutable and a restore completes within agreed RTO. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
