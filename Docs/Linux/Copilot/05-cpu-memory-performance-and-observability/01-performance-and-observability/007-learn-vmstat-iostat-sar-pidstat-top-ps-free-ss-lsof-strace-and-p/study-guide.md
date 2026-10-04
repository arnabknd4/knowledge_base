# Learn `vmstat`, `iostat`, `sar`, `pidstat`, `top`/`ps`, `free`, `ss`, `lsof`, `strace`, and `perf` at a diagnostic level (P1).

**Syllabus objective (exact wording):** Learn `vmstat`, `iostat`, `sar`, `pidstat`, `top`/`ps`, `free`, `ss`, `lsof`, `strace`, and `perf` at a diagnostic level (P1).

**Mapping:** `05` → `007` `Learn `vmstat`, `iostat`, `sar`, `pidstat`, `top`/`ps`, `free`, `ss`, `lsof`, `strace`, and `perf` at a diagnostic level (P1).`

## What

vmstat/iostat/sar/pidstat/top/ps/free/ss/lsof/strace/perf differ in overhead, privilege and observation point. First samples may be averages since boot; verify documentation and live-process effect.

## Why

This matters operationally: A file-descriptor leak hypothesis is tested with a bounded `lsof` count and `/proc/PID/fd` trend before tracing syscall behavior. The decision hinges on these mechanics: First samples may be averages since boot; verify documentation and live-process effect.

## How

1. **Establish the relevant boundary:** vmstat/iostat/sar/pidstat/top/ps/free/ss/lsof/strace/perf differ in overhead, privilege and observation point. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Choose the tool from the hypothesis; sample briefly, avoid broad tracing on a loaded host, and obtain approval before attaching profilers or tracing sensitive processes.
3. **Exercise the scenario:** A file-descriptor leak hypothesis is tested with a bounded `lsof` count and `/proc/PID/fd` trend before tracing syscall behavior.
4. **Verify this outcome:** use `vmstat 1 3` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** First samples may be averages since boot; verify documentation and live-process effect.

    **Distro/release distinction:** PSI, perf/eBPF capabilities and sysstat tools depend on kernel config/version and distro packages. Install or enable tooling only through supported package and policy workflows. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A file-descriptor leak hypothesis is tested with a bounded `lsof` count and `/proc/PID/fd` trend before tracing syscall behavior. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
vmstat 1 3
iostat -xz 1 3 2>/dev/null
pidstat 1 3 2>/dev/null
perf --version 2>/dev/null
```

## Do's and Don'ts

- **Do:** Choose the tool from the hypothesis; sample briefly, avoid broad tracing on a loaded host, and obtain approval before attaching profilers or tracing sensitive processes.
- **Don't:** Do not tune from a single metric snapshot or copy generic sysctl values; profiling and eBPF need bounded scope, authorization and overhead review.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A file-descriptor leak hypothesis is tested with a bounded `lsof` count and `/proc/PID/fd` trend before tracing syscall behavior. **Operator response:** Choose the tool from the hypothesis; sample briefly, avoid broad tracing on a loaded host, and obtain approval before attaching profilers or tracing sensitive processes. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: vmstat/iostat/sar/pidstat/top/ps/free/ss/lsof/strace/perf differ in overhead, privilege and observation point.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `vmstat 1 3` and follow the evidence path: Choose the tool from the hypothesis; sample briefly, avoid broad tracing on a loaded host, and obtain approval before attaching profilers or tracing sensitive processes.

**Q: How would you verify or falsify the working diagnosis?**

A: A file-descriptor leak hypothesis is tested with a bounded `lsof` count and `/proc/PID/fd` trend before tracing syscall behavior. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
