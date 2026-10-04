# Identify CPU architecture, kernel release, distribution, release lifecycle, and support policy; distinguish upstream kernel version from vendor-maintained kernels.

**Syllabus objective (exact wording):** Identify CPU architecture, kernel release, distribution, release lifecycle, and support policy; distinguish upstream kernel version from vendor-maintained kernels.

**Mapping:** `01` → `002` `Identify CPU architecture, kernel release, distribution, release lifecycle, and support policy; distinguish upstream kernel version from vendor-maintained kernels.`

## What

Architecture, running kernel, distribution release and vendor support lifecycle are separate inventory facts. Vendors can backport fixes, so an upstream-looking version comparison does not establish patch level or support status.

## Why

This matters operationally: A CVE scanner reports an old-looking kernel version on an enterprise host; verify vendor advisories and package release before concluding that it is unpatched. The decision hinges on these mechanics: Vendors can backport fixes, so an upstream-looking version comparison does not establish patch level or support status.

## How

1. **Establish the relevant boundary:** Architecture, running kernel, distribution release and vendor support lifecycle are separate inventory facts. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Capture architecture, kernel and `/etc/os-release`, then check that exact vendor release's lifecycle and errata policy; record the vendor package build as well as the upstream base.
3. **Exercise the scenario:** A CVE scanner reports an old-looking kernel version on an enterprise host; verify vendor advisories and package release before concluding that it is unpatched.
4. **Verify this outcome:** use `uname -m` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Vendors can backport fixes, so an upstream-looking version comparison does not establish patch level or support status.

    **Distro/release distinction:** RHEL-family kernels may carry vendor backports and ABI/support commitments; Debian/Ubuntu releases package their kernel and user space on their own lifecycle. A distribution combines kernel and user-space components rather than being the kernel alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A CVE scanner reports an old-looking kernel version on an enterprise host; verify vendor advisories and package release before concluding that it is unpatched. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
uname -m
uname -r
cat /etc/os-release
rpm -q kernel 2>/dev/null || dpkg-query -W 'linux-image*' 2>/dev/null
```

## Do's and Don'ts

- **Do:** Capture architecture, kernel and `/etc/os-release`, then check that exact vendor release's lifecycle and errata policy; record the vendor package build as well as the upstream base.
- **Don't:** Do not infer support or patch state from a kernel version string, install packages from an untrusted repository, or edit boot configuration without a console and tested recovery path.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A CVE scanner reports an old-looking kernel version on an enterprise host; verify vendor advisories and package release before concluding that it is unpatched. **Operator response:** Capture architecture, kernel and `/etc/os-release`, then check that exact vendor release's lifecycle and errata policy; record the vendor package build as well as the upstream base. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Architecture, running kernel, distribution release and vendor support lifecycle are separate inventory facts.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `uname -m` and follow the evidence path: Capture architecture, kernel and `/etc/os-release`, then check that exact vendor release's lifecycle and errata policy; record the vendor package build as well as the upstream base.

**Q: How would you verify or falsify the working diagnosis?**

A: A CVE scanner reports an old-looking kernel version on an enterprise host; verify vendor advisories and package release before concluding that it is unpatched. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
