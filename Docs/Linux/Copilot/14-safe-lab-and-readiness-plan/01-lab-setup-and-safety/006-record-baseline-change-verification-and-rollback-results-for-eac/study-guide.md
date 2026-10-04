# Record baseline, change, verification, and rollback results for each exercise.

**Syllabus objective (exact wording):** Record baseline, change, verification, and rollback results for each exercise.

**Mapping:** `14` → `006` `Record baseline, change, verification, and rollback results for each exercise.`

## What

A useful exercise record captures environment/image, timestamp, baseline, exact change, verification and rollback result. Without these, a success may be accidental and irreproducible.

## Why

This matters operationally: Repeat a systemd unit change from a clean image and compare expected service/log state with the prior run. The decision hinges on these mechanics: Without these, a success may be accidental and irreproducible.

## How

1. **Establish the relevant boundary:** A useful exercise record captures environment/image, timestamp, baseline, exact change, verification and rollback result. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Store the change and test evidence in a versioned lab record; record tool/release versions and clean up synthetic credentials/data after completion.
3. **Exercise the scenario:** Repeat a systemd unit change from a clean image and compare expected service/log state with the prior run.
4. **Verify this outcome:** use `date -Is` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Without these, a success may be accidental and irreproducible.

    **Distro/release distinction:** Console recovery, snapshot tooling, command options and package names vary by release/provider; prove the recovery route on the disposable target before a disruptive exercise. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Repeat a systemd unit change from a clean image and compare expected service/log state with the prior run. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. These examples collect evidence only; they do not authorize the lab action.

```sh
date -Is
cat /etc/os-release
uname -r
git diff --check
```

## Do's and Don'ts

- **Do:** Store the change and test evidence in a versioned lab record; record tool/release versions and clean up synthetic credentials/data after completion.
- **Don't:** Do not use production systems or devices containing needed data as a lab; destructive/disruptive work requires explicit approval, isolation and proven recovery.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Repeat a systemd unit change from a clean image and compare expected service/log state with the prior run. **Operator response:** Store the change and test evidence in a versioned lab record; record tool/release versions and clean up synthetic credentials/data after completion. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: A useful exercise record captures environment/image, timestamp, baseline, exact change, verification and rollback result.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `date -Is` and follow the evidence path: Store the change and test evidence in a versioned lab record; record tool/release versions and clean up synthetic credentials/data after completion.

**Q: How would you verify or falsify the working diagnosis?**

A: Repeat a systemd unit change from a clean image and compare expected service/log state with the prior run. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
