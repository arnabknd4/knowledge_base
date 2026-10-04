# Distinguish mutable host administration from container/image and fleet management; know when each pattern is appropriate.

**Syllabus objective (exact wording):** Distinguish mutable host administration from container/image and fleet management; know when each pattern is appropriate.

**Mapping:** `10` → `006` `Distinguish mutable host administration from container/image and fleet management; know when each pattern is appropriate.`

## What

Mutable host administration can be appropriate for long-lived specialized systems; image/container/fleet replacement favors consistency. The decision turns on state, repair model, scale and downtime tolerance.

## Why

This matters operationally: A stateful legacy appliance cannot yet be replaced immutably; add audited config automation and staged migration while isolating its mutable data. The decision hinges on these mechanics: The decision turns on state, repair model, scale and downtime tolerance.

## How

1. **Establish the relevant boundary:** Mutable host administration can be appropriate for long-lived specialized systems; image/container/fleet replacement favors consistency. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Document where state lives, how changes are captured, how drift is found, how quickly hosts can be replaced, and who owns emergency changes.
3. **Exercise the scenario:** A stateful legacy appliance cannot yet be replaced immutably; add audited config automation and staged migration while isolating its mutable data.
4. **Verify this outcome:** use `git status --short` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The decision turns on state, repair model, scale and downtime tolerance.

    **Distro/release distinction:** Cloud-init stages, datasource detection, agents and disk/interface naming differ by provider and image. A custom AMI or Ubuntu cloud image may not behave like a local VM of the same distro. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A stateful legacy appliance cannot yet be replaced immutably; add audited config automation and staged migration while isolating its mutable data. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
git status --short
systemctl --failed --no-pager
cloud-init status --long 2>/dev/null
```

## Do's and Don'ts

- **Do:** Document where state lives, how changes are captured, how drift is found, how quickly hosts can be replaced, and who owns emergency changes.
- **Don't:** Do not embed secrets in user data/images or roll untested configuration across a fleet; retain a known-good artifact and canary stop condition.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A stateful legacy appliance cannot yet be replaced immutably; add audited config automation and staged migration while isolating its mutable data. **Operator response:** Document where state lives, how changes are captured, how drift is found, how quickly hosts can be replaced, and who owns emergency changes. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Mutable host administration can be appropriate for long-lived specialized systems; image/container/fleet replacement favors consistency.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `git status --short` and follow the evidence path: Document where state lives, how changes are captured, how drift is found, how quickly hosts can be replaced, and who owns emergency changes.

**Q: How would you verify or falsify the working diagnosis?**

A: A stateful legacy appliance cannot yet be replaced immutably; add audited config automation and staged migration while isolating its mutable data. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
