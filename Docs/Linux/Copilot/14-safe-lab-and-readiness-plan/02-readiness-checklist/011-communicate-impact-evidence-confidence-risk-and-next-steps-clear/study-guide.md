# Communicate impact, evidence, confidence, risk, and next steps clearly.

**Syllabus objective (exact wording):** Communicate impact, evidence, confidence, risk, and next steps clearly.

**Mapping:** `14` → `011` `Communicate impact, evidence, confidence, risk, and next steps clearly.`

## What

Clear operational communication separates observed facts, confidence, impact, risk and next action; it names owner and next update rather than presenting guesses as cause.

## Why

This matters operationally: An architect reports partial regional degradation with uncertain dependency cause; state confirmed affected requests and investigation owner without claiming root cause. The decision hinges on these mechanics: The operator decision is to follow this distinction in the target release and verify the observed behavior: Write a short status using impact/scope, evidence, confidence, current risk, mitigation, owner and update time; redact secrets and personal data.

## How

1. **Establish the relevant boundary:** Clear operational communication separates observed facts, confidence, impact, risk and next action; it names owner and next update rather than presenting guesses as cause. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Write a short status using impact/scope, evidence, confidence, current risk, mitigation, owner and update time; redact secrets and personal data.
3. **Exercise the scenario:** An architect reports partial regional degradation with uncertain dependency cause; state confirmed affected requests and investigation owner without claiming root cause.
4. **Verify this outcome:** use `date -u -Is` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The operator decision is to follow this distinction in the target release and verify the observed behavior: Write a short status using impact/scope, evidence, confidence, current risk, mitigation, owner and update time; redact secrets and personal data.

    **Distro/release distinction:** Console recovery, snapshot tooling, command options and package names vary by release/provider; prove the recovery route on the disposable target before a disruptive exercise. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** An architect reports partial regional degradation with uncertain dependency cause; state confirmed affected requests and investigation owner without claiming root cause. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. These examples collect evidence only; they do not authorize the lab action.

```sh
date -u -Is
systemctl status <service> --no-pager
journalctl -u <service> --since '10 min ago' --no-pager
```

## Do's and Don'ts

- **Do:** Write a short status using impact/scope, evidence, confidence, current risk, mitigation, owner and update time; redact secrets and personal data.
- **Don't:** Do not use production systems or devices containing needed data as a lab; destructive/disruptive work requires explicit approval, isolation and proven recovery.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

An architect reports partial regional degradation with uncertain dependency cause; state confirmed affected requests and investigation owner without claiming root cause. **Operator response:** Write a short status using impact/scope, evidence, confidence, current risk, mitigation, owner and update time; redact secrets and personal data. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Clear operational communication separates observed facts, confidence, impact, risk and next action; it names owner and next update rather than presenting guesses as cause.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `date -u -Is` and follow the evidence path: Write a short status using impact/scope, evidence, confidence, current risk, mitigation, owner and update time; redact secrets and personal data.

**Q: How would you verify or falsify the working diagnosis?**

A: An architect reports partial regional degradation with uncertain dependency cause; state confirmed affected requests and investigation owner without claiming root cause. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
