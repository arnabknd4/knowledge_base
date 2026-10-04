# Make a reviewed, reversible change and verify both intended effect and absence of regressions.

**Syllabus objective (exact wording):** Make a reviewed, reversible change and verify both intended effect and absence of regressions.

**Mapping:** `14` → `009` `Make a reviewed, reversible change and verify both intended effect and absence of regressions.`

## What

A reviewed reversible change has an owner, narrow diff, precheck, acceptance test, rollback and regression check. Validation includes intended effect and absence of side effects.

## Why

This matters operationally: Update a service resource limit on one disposable canary, compare latency and restart behavior, then restore prior configuration and verify health. The decision hinges on these mechanics: Validation includes intended effect and absence of side effects.

## How

1. **Establish the relevant boundary:** A reviewed reversible change has an owner, narrow diff, precheck, acceptance test, rollback and regression check. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Have a peer review target and rollback, apply to a canary, check service/security signals and exercise rollback before declaring completion.
3. **Exercise the scenario:** Update a service resource limit on one disposable canary, compare latency and restart behavior, then restore prior configuration and verify health.
4. **Verify this outcome:** use `git diff --check` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Validation includes intended effect and absence of side effects.

    **Distro/release distinction:** Console recovery, snapshot tooling, command options and package names vary by release/provider; prove the recovery route on the disposable target before a disruptive exercise. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Update a service resource limit on one disposable canary, compare latency and restart behavior, then restore prior configuration and verify health. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. These examples collect evidence only; they do not authorize the lab action.

```sh
git diff --check
systemctl show <unit> -p MemoryMax -p CPUQuotaPerSecUSec
systemctl is-active <unit>
```

## Do's and Don'ts

- **Do:** Have a peer review target and rollback, apply to a canary, check service/security signals and exercise rollback before declaring completion.
- **Don't:** Do not use production systems or devices containing needed data as a lab; destructive/disruptive work requires explicit approval, isolation and proven recovery.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Update a service resource limit on one disposable canary, compare latency and restart behavior, then restore prior configuration and verify health. **Operator response:** Have a peer review target and rollback, apply to a canary, check service/security signals and exercise rollback before declaring completion. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: A reviewed reversible change has an owner, narrow diff, precheck, acceptance test, rollback and regression check.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `git diff --check` and follow the evidence path: Have a peer review target and rollback, apply to a canary, check service/security signals and exercise rollback before declaring completion.

**Q: How would you verify or falsify the working diagnosis?**

A: Update a service resource limit on one disposable canary, compare latency and restart behavior, then restore prior configuration and verify health. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
