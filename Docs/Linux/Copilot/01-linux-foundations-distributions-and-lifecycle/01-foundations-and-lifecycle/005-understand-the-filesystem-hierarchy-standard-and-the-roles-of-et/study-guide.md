# Understand the Filesystem Hierarchy Standard and the roles of `/etc`, `/var`, `/usr`, `/opt`, `/home`, `/run`, `/proc`, `/sys`, and `/dev`.

**Syllabus objective (exact wording):** Understand the Filesystem Hierarchy Standard and the roles of `/etc`, `/var`, `/usr`, `/opt`, `/home`, `/run`, `/proc`, `/sys`, and `/dev`.

**Mapping:** `01` → `005` `Understand the Filesystem Hierarchy Standard and the roles of `/etc`, `/var`, `/usr`, `/opt`, `/home`, `/run`, `/proc`, `/sys`, and `/dev`.`

## What

FHS separates configuration (`/etc`), variable state (`/var`), vendor software (`/usr`), optional locally managed software (`/opt`), home data (`/home`), volatile runtime (`/run`) and kernel/device interfaces (`/proc`, `/sys`, `/dev`). Mount layouts may vary.

## Why

This matters operationally: A service works until reboot because its generated socket or state was written beneath an ephemeral path; map path ownership and persistence before moving data. The decision hinges on these mechanics: Mount layouts may vary.

## How

1. **Establish the relevant boundary:** FHS separates configuration (`/etc`), variable state (`/var`), vendor software (`/usr`), optional locally managed software (`/opt`), home data (`/home`), volatile runtime (`/run`) and kernel/device interfaces (`/proc`, `/sys`, `/dev`). Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Locate a service's config, durable state, logs/cache, executable and runtime socket; determine which path is persistent, packaged, generated or ephemeral before backup or migration.
3. **Exercise the scenario:** A service works until reboot because its generated socket or state was written beneath an ephemeral path; map path ownership and persistence before moving data.
4. **Verify this outcome:** use `findmnt` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Mount layouts may vary.

    **Distro/release distinction:** RHEL-family kernels may carry vendor backports and ABI/support commitments; Debian/Ubuntu releases package their kernel and user space on their own lifecycle. A distribution combines kernel and user-space components rather than being the kernel alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A service works until reboot because its generated socket or state was written beneath an ephemeral path; map path ownership and persistence before moving data. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
findmnt
ls -ld /etc /var /usr /opt /home /run /proc /sys /dev
systemctl show <unit> -p FragmentPath -p StateDirectory -p RuntimeDirectory
```

## Do's and Don'ts

- **Do:** Locate a service's config, durable state, logs/cache, executable and runtime socket; determine which path is persistent, packaged, generated or ephemeral before backup or migration.
- **Don't:** Do not infer support or patch state from a kernel version string, install packages from an untrusted repository, or edit boot configuration without a console and tested recovery path.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A service works until reboot because its generated socket or state was written beneath an ephemeral path; map path ownership and persistence before moving data. **Operator response:** Locate a service's config, durable state, logs/cache, executable and runtime socket; determine which path is persistent, packaged, generated or ephemeral before backup or migration. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: FHS separates configuration (`/etc`), variable state (`/var`), vendor software (`/usr`), optional locally managed software (`/opt`), home data (`/home`), volatile runtime (`/run`) and kernel/device interfaces (`/proc`, `/sys`, `/dev`).

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `findmnt` and follow the evidence path: Locate a service's config, durable state, logs/cache, executable and runtime socket; determine which path is persistent, packaged, generated or ephemeral before backup or migration.

**Q: How would you verify or falsify the working diagnosis?**

A: A service works until reboot because its generated socket or state was written beneath an ephemeral path; map path ownership and persistence before moving data. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
