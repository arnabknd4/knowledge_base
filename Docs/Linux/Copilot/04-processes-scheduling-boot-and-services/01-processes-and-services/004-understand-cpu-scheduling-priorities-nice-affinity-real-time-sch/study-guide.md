# Understand CPU scheduling, priorities/nice, affinity, real-time scheduling at a conceptual level, and workload impact (P1).

**Syllabus objective (exact wording):** Understand CPU scheduling, priorities/nice, affinity, real-time scheduling at a conceptual level, and workload impact (P1).

**Mapping:** `04` → `004` `Understand CPU scheduling, priorities/nice, affinity, real-time scheduling at a conceptual level, and workload impact (P1).`

## What

Nice values influence fair scheduling priority; affinity restricts where threads run, and real-time policies can starve ordinary work if misused. Privilege and kernel policy constrain changes.

## Why

This matters operationally: A latency-sensitive worker competes with batch jobs; test affinity/nice in an isolated load test and measure tail latency plus system responsiveness. The decision hinges on these mechanics: Privilege and kernel policy constrain changes.

## How

1. **Establish the relevant boundary:** Nice values influence fair scheduling priority; affinity restricts where threads run, and real-time policies can starve ordinary work if misused. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Measure run queue, per-thread CPU, and latency first; use a bounded benchmark and verify system services retain CPU before evaluating scheduling changes.
3. **Exercise the scenario:** A latency-sensitive worker competes with batch jobs; test affinity/nice in an isolated load test and measure tail latency plus system responsiveness.
4. **Verify this outcome:** use `ps -eLo pid,tid,cls,rtprio,ni,psr,pcpu,comm` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Privilege and kernel policy constrain changes.

    **Distro/release distinction:** Current RHEL and Debian/Ubuntu releases commonly use systemd, but unit files, packaged defaults, journal persistence and legacy SysV compatibility differ. Read the installed merged unit. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A latency-sensitive worker competes with batch jobs; test affinity/nice in an isolated load test and measure tail latency plus system responsiveness. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
ps -eLo pid,tid,cls,rtprio,ni,psr,pcpu,comm
taskset -pc <pid>
chrt -p <pid>
```

## Do's and Don'ts

- **Do:** Measure run queue, per-thread CPU, and latency first; use a bounded benchmark and verify system services retain CPU before evaluating scheduling changes.
- **Don't:** Do not force-kill or reboot before preserving relevant process and boot evidence; do not assume restart and reload have the same semantics.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A latency-sensitive worker competes with batch jobs; test affinity/nice in an isolated load test and measure tail latency plus system responsiveness. **Operator response:** Measure run queue, per-thread CPU, and latency first; use a bounded benchmark and verify system services retain CPU before evaluating scheduling changes. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Nice values influence fair scheduling priority; affinity restricts where threads run, and real-time policies can starve ordinary work if misused.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `ps -eLo pid,tid,cls,rtprio,ni,psr,pcpu,comm` and follow the evidence path: Measure run queue, per-thread CPU, and latency first; use a bounded benchmark and verify system services retain CPU before evaluating scheduling changes.

**Q: How would you verify or falsify the working diagnosis?**

A: A latency-sensitive worker competes with batch jobs; test affinity/nice in an isolated load test and measure tail latency plus system responsiveness. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
