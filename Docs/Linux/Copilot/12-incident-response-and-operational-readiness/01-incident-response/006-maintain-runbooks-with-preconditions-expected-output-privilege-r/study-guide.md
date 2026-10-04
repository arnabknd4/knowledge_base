# Maintain runbooks with preconditions, expected output, privilege requirements, impact warnings, verification, and rollback.

**Syllabus objective (exact wording):** Maintain runbooks with preconditions, expected output, privilege requirements, impact warnings, verification, and rollback.

**Mapping:** `12` → `006` `Maintain runbooks with preconditions, expected output, privilege requirements, impact warnings, verification, and rollback.`

## What

A runbook is an executable operational contract: preconditions, privileges, expected output, impact, stop condition, verification, escalation and rollback. It must match deployed versions.

## Why

This matters operationally: A database runbook says 'restart service' but omits replica role; add prechecks and an explicit stop condition to prevent restarting the primary incorrectly. The decision hinges on these mechanics: It must match deployed versions.

## How

1. **Establish the relevant boundary:** A runbook is an executable operational contract: preconditions, privileges, expected output, impact, stop condition, verification, escalation and rollback. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Exercise the runbook as a non-author or on-call peer using realistic permissions and a failure case; remove ambiguous steps and stale output.
3. **Exercise the scenario:** A database runbook says 'restart service' but omits replica role; add prechecks and an explicit stop condition to prevent restarting the primary incorrectly.
4. **Verify this outcome:** use `git diff --check` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** It must match deployed versions.

    **Distro/release distinction:** Journal persistence, syslog routing, auditd and diagnostic utilities vary with release and configured retention. Preserve logs through approved, access-controlled incident channels. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A database runbook says 'restart service' but omits replica role; add prechecks and an explicit stop condition to prevent restarting the primary incorrectly. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
git diff --check
systemctl status <unit> --no-pager
journalctl -u <unit> --since '10 min ago' --no-pager
```

## Do's and Don'ts

- **Do:** Exercise the runbook as a non-author or on-call peer using realistic permissions and a failure case; remove ambiguous steps and stale output.
- **Don't:** Do not restart/kill processes or discard logs before assessing transient evidence, write consistency and customer impact.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A database runbook says 'restart service' but omits replica role; add prechecks and an explicit stop condition to prevent restarting the primary incorrectly. **Operator response:** Exercise the runbook as a non-author or on-call peer using realistic permissions and a failure case; remove ambiguous steps and stale output. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: A runbook is an executable operational contract: preconditions, privileges, expected output, impact, stop condition, verification, escalation and rollback.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `git diff --check` and follow the evidence path: Exercise the runbook as a non-author or on-call peer using realistic permissions and a failure case; remove ambiguous steps and stale output.

**Q: How would you verify or falsify the working diagnosis?**

A: A database runbook says 'restart service' but omits replica role; add prechecks and an explicit stop condition to prevent restarting the primary incorrectly. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
