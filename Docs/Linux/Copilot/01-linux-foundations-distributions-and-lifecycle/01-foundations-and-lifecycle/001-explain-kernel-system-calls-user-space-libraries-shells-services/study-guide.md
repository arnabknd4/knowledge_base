# Explain kernel, system calls, user space, libraries, shells, services, and the boundary between kernel and distribution.

**Syllabus objective (exact wording):** Explain kernel, system calls, user space, libraries, shells, services, and the boundary between kernel and distribution.

**Mapping:** `01` → `001` `Explain kernel, system calls, user space, libraries, shells, services, and the boundary between kernel and distribution.`

## What

A Linux system call is the controlled user-mode entry into kernel services. Libraries wrap common interfaces; shells and most services run in user space. A distribution integrates a kernel with libraries, tools, policy, packaging and support.

## Why

This matters operationally: On an application that cannot start, inspect its executable and shared-library dependencies before blaming the kernel; compare a working process and package provenance. The decision hinges on these mechanics: Libraries wrap common interfaces; shells and most services run in user space. A distribution integrates a kernel with libraries, tools, policy, packaging and support.

## How

1. **Establish the relevant boundary:** A Linux system call is the controlled user-mode entry into kernel services. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Trace one request from shell/application through a library/system-call boundary and back; distinguish kernel failure from a missing or incompatible user-space dependency.
3. **Exercise the scenario:** On an application that cannot start, inspect its executable and shared-library dependencies before blaming the kernel; compare a working process and package provenance.
4. **Verify this outcome:** use `uname -r` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Libraries wrap common interfaces; shells and most services run in user space. A distribution integrates a kernel with libraries, tools, policy, packaging and support.

    **Distro/release distinction:** RHEL-family kernels may carry vendor backports and ABI/support commitments; Debian/Ubuntu releases package their kernel and user space on their own lifecycle. A distribution combines kernel and user-space components rather than being the kernel alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** On an application that cannot start, inspect its executable and shared-library dependencies before blaming the kernel; compare a working process and package provenance. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
uname -r
getconf GNU_LIBC_VERSION
file /bin/sh
ldd /bin/sh
```

## Do's and Don'ts

- **Do:** Trace one request from shell/application through a library/system-call boundary and back; distinguish kernel failure from a missing or incompatible user-space dependency.
- **Don't:** Do not infer support or patch state from a kernel version string, install packages from an untrusted repository, or edit boot configuration without a console and tested recovery path.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

On an application that cannot start, inspect its executable and shared-library dependencies before blaming the kernel; compare a working process and package provenance. **Operator response:** Trace one request from shell/application through a library/system-call boundary and back; distinguish kernel failure from a missing or incompatible user-space dependency. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: A Linux system call is the controlled user-mode entry into kernel services.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `uname -r` and follow the evidence path: Trace one request from shell/application through a library/system-call boundary and back; distinguish kernel failure from a missing or incompatible user-space dependency.

**Q: How would you verify or falsify the working diagnosis?**

A: On an application that cannot start, inspect its executable and shared-library dependencies before blaming the kernel; compare a working process and package provenance. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
