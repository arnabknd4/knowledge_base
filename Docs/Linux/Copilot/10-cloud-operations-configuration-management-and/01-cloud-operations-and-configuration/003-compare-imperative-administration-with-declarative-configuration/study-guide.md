# Compare imperative administration with declarative configuration management; understand desired state, drift detection, inventory, and convergence.

**Syllabus objective (exact wording):** Compare imperative administration with declarative configuration management; understand desired state, drift detection, inventory, and convergence.

**Mapping:** `10` → `003` `Compare imperative administration with declarative configuration management; understand desired state, drift detection, inventory, and convergence.`

## What

Imperative administration performs an action; declarative management describes desired state and detects/converges drift. Neither removes need for idempotence, ownership or review.

## Why

This matters operationally: An operator manually opens a firewall port that automation closes nightly; define ownership, update desired state and audit drift before repeating the fix. The decision hinges on these mechanics: Neither removes need for idempotence, ownership or review.

## How

1. **Establish the relevant boundary:** Imperative administration performs an action; declarative management describes desired state and detects/converges drift. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Choose declarative convergence for repeatable fleet settings; reserve imperative changes for bounded response and reconcile them back to the source of truth.
3. **Exercise the scenario:** An operator manually opens a firewall port that automation closes nightly; define ownership, update desired state and audit drift before repeating the fix.
4. **Verify this outcome:** use `git diff --check` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Neither removes need for idempotence, ownership or review.

    **Distro/release distinction:** Cloud-init stages, datasource detection, agents and disk/interface naming differ by provider and image. A custom AMI or Ubuntu cloud image may not behave like a local VM of the same distro. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** An operator manually opens a firewall port that automation closes nightly; define ownership, update desired state and audit drift before repeating the fix. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
git diff --check
ansible-playbook --check --diff site.yml 2>/dev/null
systemctl is-enabled <unit>
```

## Do's and Don'ts

- **Do:** Choose declarative convergence for repeatable fleet settings; reserve imperative changes for bounded response and reconcile them back to the source of truth.
- **Don't:** Do not embed secrets in user data/images or roll untested configuration across a fleet; retain a known-good artifact and canary stop condition.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

An operator manually opens a firewall port that automation closes nightly; define ownership, update desired state and audit drift before repeating the fix. **Operator response:** Choose declarative convergence for repeatable fleet settings; reserve imperative changes for bounded response and reconcile them back to the source of truth. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Imperative administration performs an action; declarative management describes desired state and detects/converges drift.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `git diff --check` and follow the evidence path: Choose declarative convergence for repeatable fleet settings; reserve imperative changes for bounded response and reconcile them back to the source of truth.

**Q: How would you verify or falsify the working diagnosis?**

A: An operator manually opens a firewall port that automation closes nightly; define ownership, update desired state and audit drift before repeating the fix. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
