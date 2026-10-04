# Understand immutable image workflows, golden images, image pipelines, signed/provenance-aware artifacts, and replacement rather than ad hoc repair.

**Syllabus objective (exact wording):** Understand immutable image workflows, golden images, image pipelines, signed/provenance-aware artifacts, and replacement rather than ad hoc repair.

**Mapping:** `10` → `005` `Understand immutable image workflows, golden images, image pipelines, signed/provenance-aware artifacts, and replacement rather than ad hoc repair.`

## What

Immutable workflows produce versioned images from controlled inputs, validate and sign/provenance-track them, then replace instances. Golden-image contents must not include runtime secrets or mutable state.

## Why

This matters operationally: A security fix is applied by image rebuild; verify the resulting digest, SBOM/provenance, boot/agent checks and rollback to previous image. The decision hinges on these mechanics: Golden-image contents must not include runtime secrets or mutable state.

## How

1. **Establish the relevant boundary:** Immutable workflows produce versioned images from controlled inputs, validate and sign/provenance-track them, then replace instances. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Rebuild from a clean base, scan/test package and policy baseline, record digest/provenance, and exercise replacement/rollback while state remains external.
3. **Exercise the scenario:** A security fix is applied by image rebuild; verify the resulting digest, SBOM/provenance, boot/agent checks and rollback to previous image.
4. **Verify this outcome:** use `sha256sum <image-artifact>` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Golden-image contents must not include runtime secrets or mutable state.

    **Distro/release distinction:** Cloud-init stages, datasource detection, agents and disk/interface naming differ by provider and image. A custom AMI or Ubuntu cloud image may not behave like a local VM of the same distro. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A security fix is applied by image rebuild; verify the resulting digest, SBOM/provenance, boot/agent checks and rollback to previous image. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
sha256sum <image-artifact>
cosign verify <image-reference> 2>/dev/null
cat /etc/os-release
```

## Do's and Don'ts

- **Do:** Rebuild from a clean base, scan/test package and policy baseline, record digest/provenance, and exercise replacement/rollback while state remains external.
- **Don't:** Do not embed secrets in user data/images or roll untested configuration across a fleet; retain a known-good artifact and canary stop condition.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A security fix is applied by image rebuild; verify the resulting digest, SBOM/provenance, boot/agent checks and rollback to previous image. **Operator response:** Rebuild from a clean base, scan/test package and policy baseline, record digest/provenance, and exercise replacement/rollback while state remains external. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Immutable workflows produce versioned images from controlled inputs, validate and sign/provenance-track them, then replace instances.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `sha256sum <image-artifact>` and follow the evidence path: Rebuild from a clean base, scan/test package and policy baseline, record digest/provenance, and exercise replacement/rollback while state remains external.

**Q: How would you verify or falsify the working diagnosis?**

A: A security fix is applied by image rebuild; verify the resulting digest, SBOM/provenance, boot/agent checks and rollback to previous image. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
