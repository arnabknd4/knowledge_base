# Use disposable VMs, snapshots, or isolated cloud accounts with no production credentials or sensitive data.

**Syllabus objective (exact wording):** Use disposable VMs, snapshots, or isolated cloud accounts with no production credentials or sensitive data.

**Mapping:** `14` → `001` `Use disposable VMs, snapshots, or isolated cloud accounts with no production credentials or sensitive data.`

## What

Disposable VMs, snapshots or isolated cloud accounts keep lab mistakes away from production data and credentials. Isolation also needs cost limits, network boundaries and cleanup ownership.

## Why

This matters operationally: Practice fstab recovery in a snapshot-backed VM with blocked production routes and a cleanup ticket. The decision hinges on these mechanics: Isolation also needs cost limits, network boundaries and cleanup ownership.

## How

1. **Establish the relevant boundary:** Disposable VMs, snapshots or isolated cloud accounts keep lab mistakes away from production data and credentials. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Create an isolated account/VM with synthetic data and no production identity; verify snapshot/restore and destroy/cleanup procedure before experiment.
3. **Exercise the scenario:** Practice fstab recovery in a snapshot-backed VM with blocked production routes and a cleanup ticket.
4. **Verify this outcome:** use `systemd-detect-virt` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Isolation also needs cost limits, network boundaries and cleanup ownership.

    **Distro/release distinction:** Console recovery, snapshot tooling, command options and package names vary by release/provider; prove the recovery route on the disposable target before a disruptive exercise. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Practice fstab recovery in a snapshot-backed VM with blocked production routes and a cleanup ticket. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. These examples collect evidence only; they do not authorize the lab action.

```sh
systemd-detect-virt
cloud-init status --long 2>/dev/null
git status --short
```

## Do's and Don'ts

- **Do:** Create an isolated account/VM with synthetic data and no production identity; verify snapshot/restore and destroy/cleanup procedure before experiment.
- **Don't:** Do not use production systems or devices containing needed data as a lab; destructive/disruptive work requires explicit approval, isolation and proven recovery.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Practice fstab recovery in a snapshot-backed VM with blocked production routes and a cleanup ticket. **Operator response:** Create an isolated account/VM with synthetic data and no production identity; verify snapshot/restore and destroy/cleanup procedure before experiment. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Disposable VMs, snapshots or isolated cloud accounts keep lab mistakes away from production data and credentials.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemd-detect-virt` and follow the evidence path: Create an isolated account/VM with synthetic data and no production identity; verify snapshot/restore and destroy/cleanup procedure before experiment.

**Q: How would you verify or falsify the working diagnosis?**

A: Practice fstab recovery in a snapshot-backed VM with blocked production routes and a cleanup ticket. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
