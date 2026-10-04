# Relate host-level signals to user-visible symptoms, SLOs, error budgets, capacity forecasts, and alert quality.

**Syllabus objective (exact wording):** Relate host-level signals to user-visible symptoms, SLOs, error budgets, capacity forecasts, and alert quality.

**Role extension:** Site reliability engineer (SRE). This checklist outcome extends, rather than duplicates, the shared technical domains.

**Mapping:** `13` → `007` `Relate host-level signals to user-visible symptoms, SLOs, error budgets, capacity forecasts, and alert quality.`

## What

Host metrics become SRE signals only when related to user-visible symptoms, SLO/error budget, capacity forecast and alert actionability. Noisy host threshold pages without service context waste response.

## Why

This matters operationally: A disk latency signal is tied to database p99 and error budget; alert only when the service impact is actionable and include affected volume/instance. The decision hinges on these mechanics: Noisy host threshold pages without service context waste response.

## How

1. **Establish the relevant boundary:** Host metrics become SRE signals only when related to user-visible symptoms, SLO/error budget, capacity forecast and alert actionability. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Select leading and lagging signals; define alert scope, threshold window, runbook action and suppression/ownership, then test against an incident or replay.
3. **Exercise the scenario:** A disk latency signal is tied to database p99 and error budget; alert only when the service impact is actionable and include affected volume/instance.
4. **Verify this outcome:** use `iostat -xz 1 3 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Noisy host threshold pages without service context waste response.

    **Distro/release distinction:** A supported RHEL/Ubuntu/Amazon Linux offering and a community-compatible derivative can have different patch escalation and lifecycle commitments; assign ownership for each layer. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A disk latency signal is tied to database p99 and error budget; alert only when the service impact is actionable and include affected volume/instance. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
iostat -xz 1 3 2>/dev/null
systemctl status <service> --no-pager
date -Is
```

## Do's and Don'ts

- **Do:** Select leading and lagging signals; define alert scope, threshold window, runbook action and suppression/ownership, then test against an incident or replay.
- **Don't:** Do not use production credentials/data in capstones or claim readiness without repeatable evidence, failure handling and rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A disk latency signal is tied to database p99 and error budget; alert only when the service impact is actionable and include affected volume/instance. **Operator response:** Select leading and lagging signals; define alert scope, threshold window, runbook action and suppression/ownership, then test against an incident or replay. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Host metrics become SRE signals only when related to user-visible symptoms, SLO/error budget, capacity forecast and alert actionability.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `iostat -xz 1 3 2>/dev/null` and follow the evidence path: Select leading and lagging signals; define alert scope, threshold window, runbook action and suppression/ownership, then test against an incident or replay.

**Q: How would you verify or falsify the working diagnosis?**

A: A disk latency signal is tied to database p99 and error budget; alert only when the service impact is actionable and include affected volume/instance. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
