# Understand eBPF-based observability and its kernel, privilege, tooling, and production-safety constraints (P2).

**Syllabus objective (exact wording):** Understand eBPF-based observability and its kernel, privilege, tooling, and production-safety constraints (P2).

**Mapping:** `05` → `008` `Understand eBPF-based observability and its kernel, privilege, tooling, and production-safety constraints (P2).`

## What

eBPF observability depends on kernel features, BTF/configuration, verifier acceptance, privilege/capabilities, tooling version and probe overhead. Probes can expose sensitive process/network data.

## Why

This matters operationally: A team wants syscall latency histograms on a production node; validate a maintained tool on a canary kernel and measure overhead before fleet deployment. The decision hinges on these mechanics: Probes can expose sensitive process/network data.

## How

1. **Establish the relevant boundary:** eBPF observability depends on kernel features, BTF/configuration, verifier acceptance, privilege/capabilities, tooling version and probe overhead. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Confirm kernel/tool support, inspect the exact program/source, use bounded aggregation and duration, and define detach/overhead/privacy controls before production use.
3. **Exercise the scenario:** A team wants syscall latency histograms on a production node; validate a maintained tool on a canary kernel and measure overhead before fleet deployment.
4. **Verify this outcome:** use `uname -r` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Probes can expose sensitive process/network data.

    **Distro/release distinction:** PSI, perf/eBPF capabilities and sysstat tools depend on kernel config/version and distro packages. Install or enable tooling only through supported package and policy workflows. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A team wants syscall latency histograms on a production node; validate a maintained tool on a canary kernel and measure overhead before fleet deployment. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
uname -r
test -r /sys/kernel/btf/vmlinux && echo BTF-present
bpftool feature probe 2>/dev/null | head
```

## Do's and Don'ts

- **Do:** Confirm kernel/tool support, inspect the exact program/source, use bounded aggregation and duration, and define detach/overhead/privacy controls before production use.
- **Don't:** Do not tune from a single metric snapshot or copy generic sysctl values; profiling and eBPF need bounded scope, authorization and overhead review.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A team wants syscall latency histograms on a production node; validate a maintained tool on a canary kernel and measure overhead before fleet deployment. **Operator response:** Confirm kernel/tool support, inspect the exact program/source, use bounded aggregation and duration, and define detach/overhead/privacy controls before production use. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: eBPF observability depends on kernel features, BTF/configuration, verifier acceptance, privilege/capabilities, tooling version and probe overhead.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `uname -r` and follow the evidence path: Confirm kernel/tool support, inspect the exact program/source, use bounded aggregation and duration, and define detach/overhead/privacy controls before production use.

**Q: How would you verify or falsify the working diagnosis?**

A: A team wants syscall latency histograms on a production node; validate a maintained tool on a canary kernel and measure overhead before fleet deployment. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
