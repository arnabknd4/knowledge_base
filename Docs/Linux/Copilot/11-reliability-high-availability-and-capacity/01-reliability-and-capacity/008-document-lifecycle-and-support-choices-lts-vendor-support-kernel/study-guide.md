# Document lifecycle and support choices: LTS/vendor support, kernel cadence, upgrade windows, package repositories, and compatibility.

**Syllabus objective (exact wording):** Document lifecycle and support choices: LTS/vendor support, kernel cadence, upgrade windows, package repositories, and compatibility.

**Mapping:** `11` → `008` `Document lifecycle and support choices: LTS/vendor support, kernel cadence, upgrade windows, package repositories, and compatibility.`

## What

Support choices include vendor LTS windows, kernel cadence, repositories, upgrades and compatibility. EOL platforms accumulate risk even if currently stable.

## Why

This matters operationally: An appliance depends on an unsupported kernel driver; document exception owner/mitigation and test replacement path before the vendor window closes. The decision hinges on these mechanics: EOL platforms accumulate risk even if currently stable.

## How

1. **Establish the relevant boundary:** Support choices include vendor LTS windows, kernel cadence, repositories, upgrades and compatibility. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Maintain inventory with lifecycle dates, support owner, upgrade target, kernel/driver constraints and tested migration route; alert before support expiry.
3. **Exercise the scenario:** An appliance depends on an unsupported kernel driver; document exception owner/mitigation and test replacement path before the vendor window closes.
4. **Verify this outcome:** use `cat /etc/os-release` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** EOL platforms accumulate risk even if currently stable.

    **Distro/release distinction:** Pacemaker/Corosync, fencing agents, support contracts and cloud zone/region guarantees are platform-specific; validate the exact supported combination and failure model. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** An appliance depends on an unsupported kernel driver; document exception owner/mitigation and test replacement path before the vendor window closes. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
cat /etc/os-release
uname -r
rpm -q kernel 2>/dev/null
apt-cache policy linux-image-generic 2>/dev/null
```

## Do's and Don'ts

- **Do:** Maintain inventory with lifecycle dates, support owner, upgrade target, kernel/driver constraints and tested migration route; alert before support expiry.
- **Don't:** Do not call a design highly available without testing failover, fencing/state consistency, measured recovery and failure-domain independence.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

An appliance depends on an unsupported kernel driver; document exception owner/mitigation and test replacement path before the vendor window closes. **Operator response:** Maintain inventory with lifecycle dates, support owner, upgrade target, kernel/driver constraints and tested migration route; alert before support expiry. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Support choices include vendor LTS windows, kernel cadence, repositories, upgrades and compatibility.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `cat /etc/os-release` and follow the evidence path: Maintain inventory with lifecycle dates, support owner, upgrade target, kernel/driver constraints and tested migration route; alert before support expiry.

**Q: How would you verify or falsify the working diagnosis?**

A: An appliance depends on an unsupported kernel driver; document exception owner/mitigation and test replacement path before the vendor window closes. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
