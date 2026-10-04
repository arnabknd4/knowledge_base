# Use security baselines such as CIS or applicable organizational/regulatory baselines as review inputs, not blindly applied scripts.

**Syllabus objective (exact wording):** Use security baselines such as CIS or applicable organizational/regulatory baselines as review inputs, not blindly applied scripts.

**Mapping:** `08` → `011` `Use security baselines such as CIS or applicable organizational/regulatory baselines as review inputs, not blindly applied scripts.`

## What

CIS and regulatory baselines are control catalogs, not universal safe scripts. Applicability, compensating controls, exceptions and workload impact need review and evidence.

## Why

This matters operationally: A benchmark disables a legacy protocol required by a vendor; isolate the exception, restrict its exposure and document a migration deadline rather than silently ignoring the finding. The decision hinges on these mechanics: Applicability, compensating controls, exceptions and workload impact need review and evidence.

## How

1. **Establish the relevant boundary:** CIS and regulatory baselines are control catalogs, not universal safe scripts. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Map each relevant control to policy owner, evidence and test; pilot selected changes on representative images and record exceptions with rationale/expiry.
3. **Exercise the scenario:** A benchmark disables a legacy protocol required by a vendor; isolate the exception, restrict its exposure and document a migration deadline rather than silently ignoring the finding.
4. **Verify this outcome:** use `oscap info <profile-or-content> 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Applicability, compensating controls, exceptions and workload impact need review and evidence.

    **Distro/release distinction:** SELinux is central on RHEL-family systems and AppArmor common on Ubuntu; package-signing, audit, Secure Boot and baseline tooling have release-specific procedures. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A benchmark disables a legacy protocol required by a vendor; isolate the exception, restrict its exposure and document a migration deadline rather than silently ignoring the finding. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing. Packet capture or security/audit output requires authorization and controlled handling.

```sh
oscap info <profile-or-content> 2>/dev/null
auditctl -s 2>/dev/null
cat /etc/os-release
```

## Do's and Don'ts

- **Do:** Map each relevant control to policy owner, evidence and test; pilot selected changes on representative images and record exceptions with rationale/expiry.
- **Don't:** Do not disable SELinux/AppArmor, expose private keys/secrets, or run an opaque hardening script as a substitute for policy diagnosis.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A benchmark disables a legacy protocol required by a vendor; isolate the exception, restrict its exposure and document a migration deadline rather than silently ignoring the finding. **Operator response:** Map each relevant control to policy owner, evidence and test; pilot selected changes on representative images and record exceptions with rationale/expiry. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: CIS and regulatory baselines are control catalogs, not universal safe scripts.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `oscap info <profile-or-content> 2>/dev/null` and follow the evidence path: Map each relevant control to policy owner, evidence and test; pilot selected changes on representative images and record exceptions with rationale/expiry.

**Q: How would you verify or falsify the working diagnosis?**

A: A benchmark disables a legacy protocol required by a vendor; isolate the exception, restrict its exposure and document a migration deadline rather than silently ignoring the finding. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
