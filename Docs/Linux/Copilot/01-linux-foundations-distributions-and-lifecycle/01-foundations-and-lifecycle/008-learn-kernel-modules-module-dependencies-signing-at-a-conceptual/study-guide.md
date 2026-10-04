# Learn kernel modules, module dependencies/signing at a conceptual level, and the distinction between loading a module and installing its package (P2).

**Syllabus objective (exact wording):** Learn kernel modules, module dependencies/signing at a conceptual level, and the distinction between loading a module and installing its package (P2).

**Mapping:** `01` → `008` `Learn kernel modules, module dependencies/signing at a conceptual level, and the distinction between loading a module and installing its package (P2).`

## What

Module package installation, module file availability, dependency resolution and current loaded state are different. Kernel ABI, signing policy and Secure Boot can prevent loading even when a module package exists.

## Why

This matters operationally: A network adapter is missing after a kernel update; compare `lspci`/device visibility, installed matching module package, signature status and kernel logs before attempting a reload. The decision hinges on these mechanics: Kernel ABI, signing policy and Secure Boot can prevent loading even when a module package exists.

## How

1. **Establish the relevant boundary:** Module package installation, module file availability, dependency resolution and current loaded state are different. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Check running kernel, module metadata and loaded state; confirm vendor package and signature policy before installation/loading. Treat module unload/load as potentially workload-disruptive.
3. **Exercise the scenario:** A network adapter is missing after a kernel update; compare `lspci`/device visibility, installed matching module package, signature status and kernel logs before attempting a reload.
4. **Verify this outcome:** use `uname -r` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Kernel ABI, signing policy and Secure Boot can prevent loading even when a module package exists.

    **Distro/release distinction:** RHEL-family kernels may carry vendor backports and ABI/support commitments; Debian/Ubuntu releases package their kernel and user space on their own lifecycle. A distribution combines kernel and user-space components rather than being the kernel alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A network adapter is missing after a kernel update; compare `lspci`/device visibility, installed matching module package, signature status and kernel logs before attempting a reload. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
uname -r
lsmod
modinfo <module> 2>/dev/null
journalctl -k -b --no-pager | tail -80
```

## Do's and Don'ts

- **Do:** Check running kernel, module metadata and loaded state; confirm vendor package and signature policy before installation/loading. Treat module unload/load as potentially workload-disruptive.
- **Don't:** Do not infer support or patch state from a kernel version string, install packages from an untrusted repository, or edit boot configuration without a console and tested recovery path.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A network adapter is missing after a kernel update; compare `lspci`/device visibility, installed matching module package, signature status and kernel logs before attempting a reload. **Operator response:** Check running kernel, module metadata and loaded state; confirm vendor package and signature policy before installation/loading. Treat module unload/load as potentially workload-disruptive. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Module package installation, module file availability, dependency resolution and current loaded state are different.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `uname -r` and follow the evidence path: Check running kernel, module metadata and loaded state; confirm vendor package and signature policy before installation/loading. Treat module unload/load as potentially workload-disruptive.

**Q: How would you verify or falsify the working diagnosis?**

A: A network adapter is missing after a kernel update; compare `lspci`/device visibility, installed matching module package, signature status and kernel logs before attempting a reload. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
