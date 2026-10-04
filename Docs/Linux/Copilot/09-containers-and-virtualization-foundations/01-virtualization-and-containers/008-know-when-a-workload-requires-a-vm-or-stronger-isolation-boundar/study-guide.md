# Know when a workload requires a VM or stronger isolation boundary rather than relying on a container.

**Syllabus objective (exact wording):** Know when a workload requires a VM or stronger isolation boundary rather than relying on a container.

**Mapping:** `09` → `008` `Know when a workload requires a VM or stronger isolation boundary rather than relying on a container.`

## What

A VM or stronger isolation is appropriate when separate kernels, untrusted tenancy, kernel specialization or compliance boundaries exceed container assurance. Choice depends on threat model and residual risk.

## Why

This matters operationally: Untrusted customer plugins execute native code; evaluate separate VM/microVM and control-plane limits instead of relying solely on a restricted container. The decision hinges on these mechanics: Choice depends on threat model and residual risk.

## How

1. **Establish the relevant boundary:** A VM or stronger isolation is appropriate when separate kernels, untrusted tenancy, kernel specialization or compliance boundaries exceed container assurance. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Compare isolation strength, operational overhead, kernel needs, performance, compliance and patch ownership; document shared-kernel residual risk and stronger boundary selection.
3. **Exercise the scenario:** Untrusted customer plugins execute native code; evaluate separate VM/microVM and control-plane limits instead of relying solely on a restricted container.
4. **Verify this outcome:** use `systemd-detect-virt` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Choice depends on threat model and residual risk.

    **Distro/release distinction:** The running kernel and distribution/runtime determine cgroup v1/v2, delegation, rootless support and default seccomp/LSM profile. Never infer effective limits from config intent alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** Untrusted customer plugins execute native code; evaluate separate VM/microVM and control-plane limits instead of relying solely on a restricted container. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
systemd-detect-virt
uname -r
lsns -t user,pid,mnt,net
```

## Do's and Don'ts

- **Do:** Compare isolation strength, operational overhead, kernel needs, performance, compliance and patch ownership; document shared-kernel residual risk and stronger boundary selection.
- **Don't:** Do not grant privileged-container access, expose the host runtime socket, or treat namespaces alone as a security boundary.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

Untrusted customer plugins execute native code; evaluate separate VM/microVM and control-plane limits instead of relying solely on a restricted container. **Operator response:** Compare isolation strength, operational overhead, kernel needs, performance, compliance and patch ownership; document shared-kernel residual risk and stronger boundary selection. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: A VM or stronger isolation is appropriate when separate kernels, untrusted tenancy, kernel specialization or compliance boundaries exceed container assurance.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemd-detect-virt` and follow the evidence path: Compare isolation strength, operational overhead, kernel needs, performance, compliance and patch ownership; document shared-kernel residual risk and stronger boundary selection.

**Q: How would you verify or falsify the working diagnosis?**

A: Untrusted customer plugins execute native code; evaluate separate VM/microVM and control-plane limits instead of relying solely on a restricted container. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
