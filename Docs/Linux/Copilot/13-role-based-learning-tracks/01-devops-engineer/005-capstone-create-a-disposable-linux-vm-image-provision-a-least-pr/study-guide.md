# Capstone: create a disposable Linux VM/image, provision a least-privilege service account and systemd-managed sample service, apply a versioned configuration, emit useful logs/metrics, and demonstrate safe upgrade and rollback.

**Syllabus objective (exact wording):** Capstone: create a disposable Linux VM/image, provision a least-privilege service account and systemd-managed sample service, apply a versioned configuration, emit useful logs/metrics, and demonstrate safe upgrade and rollback.

**Role extension:** DevOps engineer. This checklist outcome extends, rather than duplicates, the shared technical domains.

**Mapping:** `13` → `005` `Capstone: create a disposable Linux VM/image, provision a least-privilege service account and systemd-managed sample service, apply a versioned configuration, emit useful logs/metrics, and demonstrate safe upgrade and rollback.`

## What

The DevOps capstone is a reproducible disposable VM/image with a least-privilege account, systemd service, versioned config, telemetry and safe upgrade/rollback evidence.

## Why

This matters operationally: A reviewer destroys/recreates the lab VM from its recipe and verifies service health and rollback to the previous release. The decision hinges on these mechanics: The operator decision is to follow this distinction in the target release and verify the observed behavior: Submit build recipe, unit/config diff, account privilege proof, observed logs/metrics, upgrade result and rollback result; rebuild from clean input without production credentials.

## How

1. **Establish the relevant boundary:** The DevOps capstone is a reproducible disposable VM/image with a least-privilege account, systemd service, versioned config, telemetry and safe upgrade/rollback evidence. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Submit build recipe, unit/config diff, account privilege proof, observed logs/metrics, upgrade result and rollback result; rebuild from clean input without production credentials.
3. **Exercise the scenario:** A reviewer destroys/recreates the lab VM from its recipe and verifies service health and rollback to the previous release.
4. **Verify this outcome:** use `git diff --check` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The operator decision is to follow this distinction in the target release and verify the observed behavior: Submit build recipe, unit/config diff, account privilege proof, observed logs/metrics, upgrade result and rollback result; rebuild from clean input without production credentials.

    **Distro/release distinction:** A supported RHEL/Ubuntu/Amazon Linux offering and a community-compatible derivative can have different patch escalation and lifecycle commitments; assign ownership for each layer. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A reviewer destroys/recreates the lab VM from its recipe and verifies service health and rollback to the previous release. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
git diff --check
systemctl status <unit> --no-pager
journalctl -u <unit> -b --no-pager
```

## Do's and Don'ts

- **Do:** Submit build recipe, unit/config diff, account privilege proof, observed logs/metrics, upgrade result and rollback result; rebuild from clean input without production credentials.
- **Don't:** Do not use production credentials/data in capstones or claim readiness without repeatable evidence, failure handling and rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A reviewer destroys/recreates the lab VM from its recipe and verifies service health and rollback to the previous release. **Operator response:** Submit build recipe, unit/config diff, account privilege proof, observed logs/metrics, upgrade result and rollback result; rebuild from clean input without production credentials. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: The DevOps capstone is a reproducible disposable VM/image with a least-privilege account, systemd service, versioned config, telemetry and safe upgrade/rollback evidence.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `git diff --check` and follow the evidence path: Submit build recipe, unit/config diff, account privilege proof, observed logs/metrics, upgrade result and rollback result; rebuild from clean input without production credentials.

**Q: How would you verify or falsify the working diagnosis?**

A: A reviewer destroys/recreates the lab VM from its recipe and verifies service health and rollback to the previous release. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
