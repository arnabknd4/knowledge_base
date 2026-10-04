# Build runbooks and CI checks for Linux configuration, image baselines, and operational readiness.

**Syllabus objective (exact wording):** Build runbooks and CI checks for Linux configuration, image baselines, and operational readiness.

**Role extension:** DevOps engineer. This checklist outcome extends, rather than duplicates, the shared technical domains.

**Mapping:** `13` → `004` `Build runbooks and CI checks for Linux configuration, image baselines, and operational readiness.`

## What

Runbooks and CI checks should verify configuration syntax, baseline policy and operational readiness before deployment; runbook steps must still work at runtime with least privilege.

## Why

This matters operationally: A CI test catches an invalid systemd unit before image publication, while the runbook verifies the service after boot and shows rollback. The decision hinges on these mechanics: The operator decision is to follow this distinction in the target release and verify the observed behavior: Create CI gates for lint/syntax/security expectations and a peer-tested runbook with preconditions, expected output and rollback; inject a safe failing fixture.

## How

1. **Establish the relevant boundary:** Runbooks and CI checks should verify configuration syntax, baseline policy and operational readiness before deployment; runbook steps must still work at runtime with least privilege. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Create CI gates for lint/syntax/security expectations and a peer-tested runbook with preconditions, expected output and rollback; inject a safe failing fixture.
3. **Exercise the scenario:** A CI test catches an invalid systemd unit before image publication, while the runbook verifies the service after boot and shows rollback.
4. **Verify this outcome:** use `systemd-analyze verify <unit-file>` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The operator decision is to follow this distinction in the target release and verify the observed behavior: Create CI gates for lint/syntax/security expectations and a peer-tested runbook with preconditions, expected output and rollback; inject a safe failing fixture.

    **Distro/release distinction:** A supported RHEL/Ubuntu/Amazon Linux offering and a community-compatible derivative can have different patch escalation and lifecycle commitments; assign ownership for each layer. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A CI test catches an invalid systemd unit before image publication, while the runbook verifies the service after boot and shows rollback. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
systemd-analyze verify <unit-file>
git diff --check
bash -n ./script.sh
```

## Do's and Don'ts

- **Do:** Create CI gates for lint/syntax/security expectations and a peer-tested runbook with preconditions, expected output and rollback; inject a safe failing fixture.
- **Don't:** Do not use production credentials/data in capstones or claim readiness without repeatable evidence, failure handling and rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A CI test catches an invalid systemd unit before image publication, while the runbook verifies the service after boot and shows rollback. **Operator response:** Create CI gates for lint/syntax/security expectations and a peer-tested runbook with preconditions, expected output and rollback; inject a safe failing fixture. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Runbooks and CI checks should verify configuration syntax, baseline policy and operational readiness before deployment; runbook steps must still work at runtime with least privilege.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemd-analyze verify <unit-file>` and follow the evidence path: Create CI gates for lint/syntax/security expectations and a peer-tested runbook with preconditions, expected output and rollback; inject a safe failing fixture.

**Q: How would you verify or falsify the working diagnosis?**

A: A CI test catches an invalid systemd unit before image publication, while the runbook verifies the service after boot and shows rollback. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
