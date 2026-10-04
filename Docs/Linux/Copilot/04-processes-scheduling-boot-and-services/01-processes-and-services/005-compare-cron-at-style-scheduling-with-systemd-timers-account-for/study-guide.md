# Compare cron/at-style scheduling with systemd timers; account for environment, missed runs, concurrency, and logging.

**Syllabus objective (exact wording):** Compare cron/at-style scheduling with systemd timers; account for environment, missed runs, concurrency, and logging.

**Mapping:** `04` → `005` `Compare cron/at-style scheduling with systemd timers; account for environment, missed runs, concurrency, and logging.`

## What

Cron/at jobs and systemd timers differ in environment, calendar/timezone, missed-run handling, concurrency, logging and unit dependencies. Neither automatically guarantees exactly-once execution.

## Why

This matters operationally: A daily maintenance job overlaps a previous long run after reboot; use a lock/idempotent operation and decide whether a persistent timer should catch up. The decision hinges on these mechanics: Neither automatically guarantees exactly-once execution.

## How

1. **Establish the relevant boundary:** Cron/at jobs and systemd timers differ in environment, calendar/timezone, missed-run handling, concurrency, logging and unit dependencies. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect schedule, timezone, working directory, environment, lock/concurrency behavior and last-run logs; define idempotency if a missed or repeated run is possible.
3. **Exercise the scenario:** A daily maintenance job overlaps a previous long run after reboot; use a lock/idempotent operation and decide whether a persistent timer should catch up.
4. **Verify this outcome:** use `systemctl list-timers --all --no-pager` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Neither automatically guarantees exactly-once execution.

    **Distro/release distinction:** Current RHEL and Debian/Ubuntu releases commonly use systemd, but unit files, packaged defaults, journal persistence and legacy SysV compatibility differ. Read the installed merged unit. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A daily maintenance job overlaps a previous long run after reboot; use a lock/idempotent operation and decide whether a persistent timer should catch up. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
systemctl list-timers --all --no-pager
systemctl cat <timer> <service>
crontab -l
```

## Do's and Don'ts

- **Do:** Inspect schedule, timezone, working directory, environment, lock/concurrency behavior and last-run logs; define idempotency if a missed or repeated run is possible.
- **Don't:** Do not force-kill or reboot before preserving relevant process and boot evidence; do not assume restart and reload have the same semantics.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A daily maintenance job overlaps a previous long run after reboot; use a lock/idempotent operation and decide whether a persistent timer should catch up. **Operator response:** Inspect schedule, timezone, working directory, environment, lock/concurrency behavior and last-run logs; define idempotency if a missed or repeated run is possible. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Cron/at jobs and systemd timers differ in environment, calendar/timezone, missed-run handling, concurrency, logging and unit dependencies.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemctl list-timers --all --no-pager` and follow the evidence path: Inspect schedule, timezone, working directory, environment, lock/concurrency behavior and last-run logs; define idempotency if a missed or repeated run is possible.

**Q: How would you verify or falsify the working diagnosis?**

A: A daily maintenance job overlaps a previous long run after reboot; use a lock/idempotent operation and decide whether a persistent timer should catch up. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
