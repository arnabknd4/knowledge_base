# Compare package formats and tools: RPM/DNF and `rpm`; DEB/APT and `dpkg`; repositories, signing, metadata, dependency resolution, pinning/version locks, and package provenance.

**Syllabus objective (exact wording):** Compare package formats and tools: RPM/DNF and `rpm`; DEB/APT and `dpkg`; repositories, signing, metadata, dependency resolution, pinning/version locks, and package provenance.

**Mapping:** `01` → `004` `Compare package formats and tools: RPM/DNF and `rpm`; DEB/APT and `dpkg`; repositories, signing, metadata, dependency resolution, pinning/version locks, and package provenance.`

## What

RPM/DEB are package formats; DNF/APT resolve repository metadata and dependencies, while rpm/dpkg query or manipulate local package state. Trust roots, signing, pinning and lifecycle are repository policy decisions—not merely install syntax.

## Why

This matters operationally: An urgent library update appears unavailable: establish whether the host has stale metadata, wrong repository/release, a pin, or an unsupported package before adding an untrusted source. The decision hinges on these mechanics: Trust roots, signing, pinning and lifecycle are repository policy decisions—not merely install syntax.

## How

1. **Establish the relevant boundary:** RPM/DEB are package formats; DNF/APT resolve repository metadata and dependencies, while rpm/dpkg query or manipulate local package state. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect package ownership and enabled sources first; verify repository signing and release compatibility. Use the distribution's supported package manager, then pin only with an explicit update/exception process.
3. **Exercise the scenario:** An urgent library update appears unavailable: establish whether the host has stale metadata, wrong repository/release, a pin, or an unsupported package before adding an untrusted source.
4. **Verify this outcome:** use `rpm -qf /bin/sh 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Trust roots, signing, pinning and lifecycle are repository policy decisions—not merely install syntax.

    **Distro/release distinction:** RHEL-family kernels may carry vendor backports and ABI/support commitments; Debian/Ubuntu releases package their kernel and user space on their own lifecycle. A distribution combines kernel and user-space components rather than being the kernel alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** An urgent library update appears unavailable: establish whether the host has stale metadata, wrong repository/release, a pin, or an unsupported package before adding an untrusted source. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
rpm -qf /bin/sh 2>/dev/null
dpkg-query -S /bin/sh 2>/dev/null
dnf repolist 2>/dev/null
apt-cache policy bash 2>/dev/null
```

## Do's and Don'ts

- **Do:** Inspect package ownership and enabled sources first; verify repository signing and release compatibility. Use the distribution's supported package manager, then pin only with an explicit update/exception process.
- **Don't:** Do not infer support or patch state from a kernel version string, install packages from an untrusted repository, or edit boot configuration without a console and tested recovery path.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

An urgent library update appears unavailable: establish whether the host has stale metadata, wrong repository/release, a pin, or an unsupported package before adding an untrusted source. **Operator response:** Inspect package ownership and enabled sources first; verify repository signing and release compatibility. Use the distribution's supported package manager, then pin only with an explicit update/exception process. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: RPM/DEB are package formats; DNF/APT resolve repository metadata and dependencies, while rpm/dpkg query or manipulate local package state.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `rpm -qf /bin/sh 2>/dev/null` and follow the evidence path: Inspect package ownership and enabled sources first; verify repository signing and release compatibility. Use the distribution's supported package manager, then pin only with an explicit update/exception process.

**Q: How would you verify or falsify the working diagnosis?**

A: An urgent library update appears unavailable: establish whether the host has stale metadata, wrong repository/release, a pin, or an unsupported package before adding an untrusted source. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
