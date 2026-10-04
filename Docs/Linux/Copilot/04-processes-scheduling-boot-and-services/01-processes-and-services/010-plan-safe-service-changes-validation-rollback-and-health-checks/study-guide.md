# Plan safe service changes, validation, rollback, and health checks before deployment (D, S).

**Syllabus objective (exact wording):** Plan safe service changes, validation, rollback, and health checks before deployment (D, S).

**Mapping:** `04` → `010` `Plan safe service changes, validation, rollback, and health checks before deployment (D, S).`

## What

A safe service change has prechecks, config validation, a bounded rollout, health checks, observable success criteria and rollback. Reload is not always equivalent to restart and may not apply every change.

## Why

This matters operationally: A new worker limit passes syntax checks but degrades queue latency; deploy to a canary and compare error/latency metrics before widening rollout. The decision hinges on these mechanics: Reload is not always equivalent to restart and may not apply every change.

## How

1. **Establish the relevant boundary:** A safe service change has prechecks, config validation, a bounded rollout, health checks, observable success criteria and rollback. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Classify whether config supports reload, validate syntax, apply to one canary, confirm readiness/dependencies, and define stop/rollback criteria before fleet promotion.
3. **Exercise the scenario:** A new worker limit passes syntax checks but degrades queue latency; deploy to a canary and compare error/latency metrics before widening rollout.
4. **Verify this outcome:** use `systemctl is-active <unit>` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Reload is not always equivalent to restart and may not apply every change.

    **Distro/release distinction:** Current RHEL and Debian/Ubuntu releases commonly use systemd, but unit files, packaged defaults, journal persistence and legacy SysV compatibility differ. Read the installed merged unit. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A new worker limit passes syntax checks but degrades queue latency; deploy to a canary and compare error/latency metrics before widening rollout. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
systemctl is-active <unit>
systemctl show <unit> -p CanReload -p ExecReload
journalctl -u <unit> --since '10 min ago' --no-pager
```

## Do's and Don'ts

- **Do:** Classify whether config supports reload, validate syntax, apply to one canary, confirm readiness/dependencies, and define stop/rollback criteria before fleet promotion.
- **Don't:** Do not force-kill or reboot before preserving relevant process and boot evidence; do not assume restart and reload have the same semantics.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A new worker limit passes syntax checks but degrades queue latency; deploy to a canary and compare error/latency metrics before widening rollout. **Operator response:** Classify whether config supports reload, validate syntax, apply to one canary, confirm readiness/dependencies, and define stop/rollback criteria before fleet promotion. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: A safe service change has prechecks, config validation, a bounded rollout, health checks, observable success criteria and rollback.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemctl is-active <unit>` and follow the evidence path: Classify whether config supports reload, validate syntax, apply to one canary, confirm readiness/dependencies, and define stop/rollback criteria before fleet promotion.

**Q: How would you verify or falsify the working diagnosis?**

A: A new worker limit passes syntax checks but degrades queue latency; deploy to a canary and compare error/latency metrics before widening rollout. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
