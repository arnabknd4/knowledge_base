# Prioritize reversible, low-risk diagnostic actions before remediation; communicate impact, owners, timeline, and uncertainty.

**Syllabus objective (exact wording):** Prioritize reversible, low-risk diagnostic actions before remediation; communicate impact, owners, timeline, and uncertainty.

**Mapping:** `12` → `002` `Prioritize reversible, low-risk diagnostic actions before remediation; communicate impact, owners, timeline, and uncertainty.`

## What

Reversible low-risk checks generally produce more information per risk than early remediation. Communication should state impact, scope, owners, timeline and uncertainty.

## Why

This matters operationally: A team proposes a fleet restart based on a single timeout; collect connection/queue evidence and test one canary before making a broad change. The decision hinges on these mechanics: Communication should state impact, scope, owners, timeline and uncertainty.

## How

1. **Establish the relevant boundary:** Reversible low-risk checks generally produce more information per risk than early remediation. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Rank next actions by information gained, blast radius and reversibility; get authorization for containment and set a time for the next update.
3. **Exercise the scenario:** A team proposes a fleet restart based on a single timeout; collect connection/queue evidence and test one canary before making a broad change.
4. **Verify this outcome:** use `systemctl status <unit> --no-pager` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Communication should state impact, scope, owners, timeline and uncertainty.

    **Distro/release distinction:** Journal persistence, syslog routing, auditd and diagnostic utilities vary with release and configured retention. Preserve logs through approved, access-controlled incident channels. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A team proposes a fleet restart based on a single timeout; collect connection/queue evidence and test one canary before making a broad change. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
systemctl status <unit> --no-pager
ss -s
journalctl -u <unit> --since '10 min ago' --no-pager
```

## Do's and Don'ts

- **Do:** Rank next actions by information gained, blast radius and reversibility; get authorization for containment and set a time for the next update.
- **Don't:** Do not restart/kill processes or discard logs before assessing transient evidence, write consistency and customer impact.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A team proposes a fleet restart based on a single timeout; collect connection/queue evidence and test one canary before making a broad change. **Operator response:** Rank next actions by information gained, blast radius and reversibility; get authorization for containment and set a time for the next update. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Reversible low-risk checks generally produce more information per risk than early remediation.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemctl status <unit> --no-pager` and follow the evidence path: Rank next actions by information gained, blast radius and reversibility; get authorization for containment and set a time for the next update.

**Q: How would you verify or falsify the working diagnosis?**

A: A team proposes a fleet restart based on a single timeout; collect connection/queue evidence and test one canary before making a broad change. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
