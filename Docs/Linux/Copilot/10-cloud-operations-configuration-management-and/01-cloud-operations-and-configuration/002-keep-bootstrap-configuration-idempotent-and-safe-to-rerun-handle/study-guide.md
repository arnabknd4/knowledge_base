# Keep bootstrap configuration idempotent and safe to rerun; handle secrets and metadata-service access deliberately.

**Syllabus objective (exact wording):** Keep bootstrap configuration idempotent and safe to rerun; handle secrets and metadata-service access deliberately.

**Mapping:** `10` → `002` `Keep bootstrap configuration idempotent and safe to rerun; handle secrets and metadata-service access deliberately.`

## What

Bootstrap must converge safely when retried and protect metadata/secrets. User data is often exposed to privileged local users or provider control planes and should not contain durable credentials.

## Why

This matters operationally: A failed first-boot script reruns and creates duplicate users; test two invocations, partial failure and credential redaction before image promotion. The decision hinges on these mechanics: User data is often exposed to privileged local users or provider control planes and should not contain durable credentials.

## How

1. **Establish the relevant boundary:** Bootstrap must converge safely when retried and protect metadata/secrets. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Make each stage idempotent, validate metadata identity, retrieve secrets with narrowly scoped role, and test interruption/retry from a disposable fresh image.
3. **Exercise the scenario:** A failed first-boot script reruns and creates duplicate users; test two invocations, partial failure and credential redaction before image promotion.
4. **Verify this outcome:** use `cloud-init status --long 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** User data is often exposed to privileged local users or provider control planes and should not contain durable credentials.

    **Distro/release distinction:** Cloud-init stages, datasource detection, agents and disk/interface naming differ by provider and image. A custom AMI or Ubuntu cloud image may not behave like a local VM of the same distro. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A failed first-boot script reruns and creates duplicate users; test two invocations, partial failure and credential redaction before image promotion. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
cloud-init status --long 2>/dev/null
systemctl status cloud-final --no-pager 2>/dev/null
grep -iE 'error|failed' /var/log/cloud-init.log 2>/dev/null | tail
```

## Do's and Don'ts

- **Do:** Make each stage idempotent, validate metadata identity, retrieve secrets with narrowly scoped role, and test interruption/retry from a disposable fresh image.
- **Don't:** Do not embed secrets in user data/images or roll untested configuration across a fleet; retain a known-good artifact and canary stop condition.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A failed first-boot script reruns and creates duplicate users; test two invocations, partial failure and credential redaction before image promotion. **Operator response:** Make each stage idempotent, validate metadata identity, retrieve secrets with narrowly scoped role, and test interruption/retry from a disposable fresh image. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Bootstrap must converge safely when retried and protect metadata/secrets.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `cloud-init status --long 2>/dev/null` and follow the evidence path: Make each stage idempotent, validate metadata identity, retrieve secrets with narrowly scoped role, and test interruption/retry from a disposable fresh image.

**Q: How would you verify or falsify the working diagnosis?**

A: A failed first-boot script reruns and creates duplicate users; test two invocations, partial failure and credential redaction before image promotion. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
