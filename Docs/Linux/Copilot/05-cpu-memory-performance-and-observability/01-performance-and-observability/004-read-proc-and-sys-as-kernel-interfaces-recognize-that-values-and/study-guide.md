# Read `/proc` and `/sys` as kernel interfaces; recognize that values and available files vary by kernel and configuration.

**Syllabus objective (exact wording):** Read `/proc` and `/sys` as kernel interfaces; recognize that values and available files vary by kernel and configuration.

**Mapping:** `05` → `004` `Read `/proc` and `/sys` as kernel interfaces; recognize that values and available files vary by kernel and configuration.`

## What

Procfs/sysfs expose kernel-generated process and device interfaces; files and semantics vary with kernel configuration and namespaces. These are not universally stable application APIs.

## Why

This matters operationally: A monitoring agent assumes a PSI file exists on every kernel; feature-detect it and emit an explicit unsupported state rather than a false zero. The decision hinges on these mechanics: These are not universally stable application APIs.

## How

1. **Establish the relevant boundary:** Procfs/sysfs expose kernel-generated process and device interfaces; files and semantics vary with kernel configuration and namespaces. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Read documented counters for the running kernel, confirm units and namespace scope, and tolerate absent files/features in scripts.
3. **Exercise the scenario:** A monitoring agent assumes a PSI file exists on every kernel; feature-detect it and emit an explicit unsupported state rather than a false zero.
4. **Verify this outcome:** use `uname -r` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** These are not universally stable application APIs.

    **Distro/release distinction:** PSI, perf/eBPF capabilities and sysstat tools depend on kernel config/version and distro packages. Install or enable tooling only through supported package and policy workflows. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A monitoring agent assumes a PSI file exists on every kernel; feature-detect it and emit an explicit unsupported state rather than a false zero. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
uname -r
cat /proc/pressure/io 2>/dev/null
grep . /proc/meminfo | head
find /sys -maxdepth 2 -type f -name '*state' 2>/dev/null | head
```

## Do's and Don'ts

- **Do:** Read documented counters for the running kernel, confirm units and namespace scope, and tolerate absent files/features in scripts.
- **Don't:** Do not tune from a single metric snapshot or copy generic sysctl values; profiling and eBPF need bounded scope, authorization and overhead review.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A monitoring agent assumes a PSI file exists on every kernel; feature-detect it and emit an explicit unsupported state rather than a false zero. **Operator response:** Read documented counters for the running kernel, confirm units and namespace scope, and tolerate absent files/features in scripts. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Procfs/sysfs expose kernel-generated process and device interfaces; files and semantics vary with kernel configuration and namespaces.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `uname -r` and follow the evidence path: Read documented counters for the running kernel, confirm units and namespace scope, and tolerate absent files/features in scripts.

**Q: How would you verify or falsify the working diagnosis?**

A: A monitoring agent assumes a PSI file exists on every kernel; feature-detect it and emit an explicit unsupported state rather than a false zero. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
