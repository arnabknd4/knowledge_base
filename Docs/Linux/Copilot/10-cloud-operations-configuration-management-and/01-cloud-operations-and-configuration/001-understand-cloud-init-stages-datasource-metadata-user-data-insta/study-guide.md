# Understand cloud-init stages, datasource/metadata, user data, instance identity, first-boot behavior, and cloud-image customization.

**Syllabus objective (exact wording):** Understand cloud-init stages, datasource/metadata, user data, instance identity, first-boot behavior, and cloud-image customization.

**Mapping:** `10` → `001` `Understand cloud-init stages, datasource/metadata, user data, instance identity, first-boot behavior, and cloud-image customization.`

## What

Cloud-init runs stages against a datasource/metadata source, often with per-instance first-boot semantics. Image and provider determine datasource, module configuration, identity and user-data handling.

## Why

This matters operationally: A cloned image thinks first boot already completed and skips user creation; inspect cached instance identity and build a clean image using vendor guidance. The decision hinges on these mechanics: Image and provider determine datasource, module configuration, identity and user-data handling.

## How

1. **Establish the relevant boundary:** Cloud-init runs stages against a datasource/metadata source, often with per-instance first-boot semantics. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Check cloud-init version/status, datasource and instance ID; inspect logs and stage completion before rerunning modules or altering instance identity.
3. **Exercise the scenario:** A cloned image thinks first boot already completed and skips user creation; inspect cached instance identity and build a clean image using vendor guidance.
4. **Verify this outcome:** use `cloud-init status --long 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Image and provider determine datasource, module configuration, identity and user-data handling.

    **Distro/release distinction:** Cloud-init stages, datasource detection, agents and disk/interface naming differ by provider and image. A custom AMI or Ubuntu cloud image may not behave like a local VM of the same distro. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A cloned image thinks first boot already completed and skips user creation; inspect cached instance identity and build a clean image using vendor guidance. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
cloud-init status --long 2>/dev/null
cloud-init query ds 2>/dev/null
journalctl -u cloud-init -b --no-pager 2>/dev/null
```

## Do's and Don'ts

- **Do:** Check cloud-init version/status, datasource and instance ID; inspect logs and stage completion before rerunning modules or altering instance identity.
- **Don't:** Do not embed secrets in user data/images or roll untested configuration across a fleet; retain a known-good artifact and canary stop condition.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A cloned image thinks first boot already completed and skips user creation; inspect cached instance identity and build a clean image using vendor guidance. **Operator response:** Check cloud-init version/status, datasource and instance ID; inspect logs and stage completion before rerunning modules or altering instance identity. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Cloud-init runs stages against a datasource/metadata source, often with per-instance first-boot semantics.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `cloud-init status --long 2>/dev/null` and follow the evidence path: Check cloud-init version/status, datasource and instance ID; inspect logs and stage completion before rerunning modules or altering instance identity.

**Q: How would you verify or falsify the working diagnosis?**

A: A cloned image thinks first boot already completed and skips user creation; inspect cached instance identity and build a clean image using vendor guidance. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
