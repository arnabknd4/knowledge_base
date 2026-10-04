# Compare RHEL-family systems (RHEL, Rocky Linux, AlmaLinux), Debian/Ubuntu, Amazon Linux, and minimal/container-focused distributions; understand support and compatibility implications.

**Syllabus objective (exact wording):** Compare RHEL-family systems (RHEL, Rocky Linux, AlmaLinux), Debian/Ubuntu, Amazon Linux, and minimal/container-focused distributions; understand support and compatibility implications.

**Mapping:** `01` → `003` `Compare RHEL-family systems (RHEL, Rocky Linux, AlmaLinux), Debian/Ubuntu, Amazon Linux, and minimal/container-focused distributions; understand support and compatibility implications.`

## What

Distribution choice is a support and operations decision, not a family-name equivalence. Compare lifecycle/support owner, kernel policy, certification, package ecosystem, security defaults, image availability and staff capability; derivatives can differ in commercial support.

## Why

This matters operationally: For a regulated service requiring vendor escalation and certified middleware, compare a supported RHEL/Ubuntu LTS/Amazon Linux image with community derivatives and document which party owns fixes. The decision hinges on these mechanics: Compare lifecycle/support owner, kernel policy, certification, package ecosystem, security defaults, image availability and staff capability; derivatives can differ in commercial support.

## How

1. **Establish the relevant boundary:** Distribution choice is a support and operations decision, not a family-name equivalence. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Score the workload against vendor support commitment, required packages/drivers, cloud image, compliance and upgrade window; prototype on the actual release/architecture before standardizing.
3. **Exercise the scenario:** For a regulated service requiring vendor escalation and certified middleware, compare a supported RHEL/Ubuntu LTS/Amazon Linux image with community derivatives and document which party owns fixes.
4. **Verify this outcome:** use `cat /etc/os-release` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Compare lifecycle/support owner, kernel policy, certification, package ecosystem, security defaults, image availability and staff capability; derivatives can differ in commercial support.

    **Distro/release distinction:** RHEL-family kernels may carry vendor backports and ABI/support commitments; Debian/Ubuntu releases package their kernel and user space on their own lifecycle. A distribution combines kernel and user-space components rather than being the kernel alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** For a regulated service requiring vendor escalation and certified middleware, compare a supported RHEL/Ubuntu LTS/Amazon Linux image with community derivatives and document which party owns fixes. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
cat /etc/os-release
uname -m
command -v dnf apt-get apk
```

## Do's and Don'ts

- **Do:** Score the workload against vendor support commitment, required packages/drivers, cloud image, compliance and upgrade window; prototype on the actual release/architecture before standardizing.
- **Don't:** Do not infer support or patch state from a kernel version string, install packages from an untrusted repository, or edit boot configuration without a console and tested recovery path.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

For a regulated service requiring vendor escalation and certified middleware, compare a supported RHEL/Ubuntu LTS/Amazon Linux image with community derivatives and document which party owns fixes. **Operator response:** Score the workload against vendor support commitment, required packages/drivers, cloud image, compliance and upgrade window; prototype on the actual release/architecture before standardizing. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Distribution choice is a support and operations decision, not a family-name equivalence.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `cat /etc/os-release` and follow the evidence path: Score the workload against vendor support commitment, required packages/drivers, cloud image, compliance and upgrade window; prototype on the actual release/architecture before standardizing.

**Q: How would you verify or falsify the working diagnosis?**

A: For a regulated service requiring vendor escalation and certified middleware, compare a supported RHEL/Ubuntu LTS/Amazon Linux image with community derivatives and document which party owns fixes. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
