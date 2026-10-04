# Use a consistent triage loop: establish impact and scope; check recent changes; preserve evidence; gather host, service, and dependency signals; form and test hypotheses.

**Syllabus objective (exact wording):** Use a consistent triage loop: establish impact and scope; check recent changes; preserve evidence; gather host, service, and dependency signals; form and test hypotheses.

**Mapping:** `12` → `001` `Use a consistent triage loop: establish impact and scope; check recent changes; preserve evidence; gather host, service, and dependency signals; form and test hypotheses.`

## What

Triage is a repeatable evidence loop: impact/scope, recent changes, preservation, host/service/dependency signals, hypotheses and tests. The timeline and current owner should be explicit.

## Why

This matters operationally: Reports say service is slow only in one zone; segment by client/host/dependency and deployment time before restarting instances. The decision hinges on these mechanics: The timeline and current owner should be explicit.

## How

1. **Establish the relevant boundary:** Triage is a repeatable evidence loop: impact/scope, recent changes, preservation, host/service/dependency signals, hypotheses and tests. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Timestamp observations with timezone/host; state facts versus hypotheses; test one hypothesis with a low-risk observation and update scope as evidence changes.
3. **Exercise the scenario:** Reports say service is slow only in one zone; segment by client/host/dependency and deployment time before restarting instances.
4. **Verify this outcome:** use `date -Is` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The timeline and current owner should be explicit.

    **Distro/release distinction:** Journal persistence, syslog routing, auditd and diagnostic utilities vary with release and configured retention. Preserve logs through approved, access-controlled incident channels. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Reports say service is slow only in one zone; segment by client/host/dependency and deployment time before restarting instances. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
date -Is
uptime
systemctl --failed --no-pager
journalctl -p warning --since '15 min ago' --no-pager
```

## Do's and Don'ts

- **Do:** Timestamp observations with timezone/host; state facts versus hypotheses; test one hypothesis with a low-risk observation and update scope as evidence changes.
- **Don't:** Do not restart/kill processes or discard logs before assessing transient evidence, write consistency and customer impact.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Reports say service is slow only in one zone; segment by client/host/dependency and deployment time before restarting instances. **Operator response:** Timestamp observations with timezone/host; state facts versus hypotheses; test one hypothesis with a low-risk observation and update scope as evidence changes. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Triage is a repeatable evidence loop: impact/scope, recent changes, preservation, host/service/dependency signals, hypotheses and tests.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `date -Is` and follow the evidence path: Timestamp observations with timezone/host; state facts versus hypotheses; test one hypothesis with a low-risk observation and update scope as evidence changes.

**Q: How would you verify or falsify the working diagnosis?**

A: Reports say service is slow only in one zone; segment by client/host/dependency and deployment time before restarting instances. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
