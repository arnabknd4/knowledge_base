# Identify architecture-dependent and cloud-image differences that affect boot, devices, firmware, and package availability (A).

**Syllabus objective (exact wording):** Identify architecture-dependent and cloud-image differences that affect boot, devices, firmware, and package availability (A).

**Mapping:** `01` → `009` `Identify architecture-dependent and cloud-image differences that affect boot, devices, firmware, and package availability (A).`

## What

Cloud images vary by CPU architecture, firmware mode, device naming, metadata, included agents and available packages. Architecture compatibility must be proven across image, kernel, boot path, drivers and application dependencies.

## Why

This matters operationally: A service image boots on x86 but fails on ARM due to an unavailable binary dependency; validate multi-architecture artifacts and cloud-device setup before fleet promotion. The decision hinges on these mechanics: Architecture compatibility must be proven across image, kernel, boot path, drivers and application dependencies.

## How

1. **Establish the relevant boundary:** Cloud images vary by CPU architecture, firmware mode, device naming, metadata, included agents and available packages. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Build a matrix of image ID, architecture, boot mode, device interface, package sources and cloud-init behavior; test a clean instance of each production shape.
3. **Exercise the scenario:** A service image boots on x86 but fails on ARM due to an unavailable binary dependency; validate multi-architecture artifacts and cloud-device setup before fleet promotion.
4. **Verify this outcome:** use `uname -m` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Architecture compatibility must be proven across image, kernel, boot path, drivers and application dependencies.

    **Distro/release distinction:** RHEL-family kernels may carry vendor backports and ABI/support commitments; Debian/Ubuntu releases package their kernel and user space on their own lifecycle. A distribution combines kernel and user-space components rather than being the kernel alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A service image boots on x86 but fails on ARM due to an unavailable binary dependency; validate multi-architecture artifacts and cloud-device setup before fleet promotion. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
uname -m
cat /etc/os-release
cloud-init status --long 2>/dev/null
lsblk -o NAME,TYPE,SIZE,SERIAL
```

## Do's and Don'ts

- **Do:** Build a matrix of image ID, architecture, boot mode, device interface, package sources and cloud-init behavior; test a clean instance of each production shape.
- **Don't:** Do not infer support or patch state from a kernel version string, install packages from an untrusted repository, or edit boot configuration without a console and tested recovery path.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A service image boots on x86 but fails on ARM due to an unavailable binary dependency; validate multi-architecture artifacts and cloud-device setup before fleet promotion. **Operator response:** Build a matrix of image ID, architecture, boot mode, device interface, package sources and cloud-init behavior; test a clean instance of each production shape. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Cloud images vary by CPU architecture, firmware mode, device naming, metadata, included agents and available packages.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `uname -m` and follow the evidence path: Build a matrix of image ID, architecture, boot mode, device interface, package sources and cloud-init behavior; test a clean instance of each production shape.

**Q: How would you verify or falsify the working diagnosis?**

A: A service image boots on x86 but fails on ARM due to an unavailable binary dependency; validate multi-architecture artifacts and cloud-device setup before fleet promotion. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
