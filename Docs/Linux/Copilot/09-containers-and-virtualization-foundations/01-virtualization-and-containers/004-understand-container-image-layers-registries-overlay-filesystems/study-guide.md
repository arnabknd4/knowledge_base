# Understand container image layers, registries, overlay filesystems, rootless operation, runtime interfaces, and OCI concepts.

**Syllabus objective (exact wording):** Understand container image layers, registries, overlay filesystems, rootless operation, runtime interfaces, and OCI concepts.

**Mapping:** `09` → `004` `Understand container image layers, registries, overlay filesystems, rootless operation, runtime interfaces, and OCI concepts.`

## What

Container images are layered OCI artifacts fetched from registries; overlay filesystems combine immutable layers with a writable layer. Rootless operation changes UID mapping and available features.

## Why

This matters operationally: A container loses uploaded files when replaced because data lived in its writable layer; move durable data to managed storage and verify ownership mapping. The decision hinges on these mechanics: Rootless operation changes UID mapping and available features.

## How

1. **Establish the relevant boundary:** Container images are layered OCI artifacts fetched from registries; overlay filesystems combine immutable layers with a writable layer. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Pin and verify image digest/provenance, inspect storage driver and writable-layer usage, run rootless where compatible and externalize durable state.
3. **Exercise the scenario:** A container loses uploaded files when replaced because data lived in its writable layer; move durable data to managed storage and verify ownership mapping.
4. **Verify this outcome:** use `podman image inspect <image> 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Rootless operation changes UID mapping and available features.

    **Distro/release distinction:** The running kernel and distribution/runtime determine cgroup v1/v2, delegation, rootless support and default seccomp/LSM profile. Never infer effective limits from config intent alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A container loses uploaded files when replaced because data lived in its writable layer; move durable data to managed storage and verify ownership mapping. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
podman image inspect <image> 2>/dev/null
docker image inspect <image> 2>/dev/null
findmnt -t overlay
df -hT
```

## Do's and Don'ts

- **Do:** Pin and verify image digest/provenance, inspect storage driver and writable-layer usage, run rootless where compatible and externalize durable state.
- **Don't:** Do not grant privileged-container access, expose the host runtime socket, or treat namespaces alone as a security boundary.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A container loses uploaded files when replaced because data lived in its writable layer; move durable data to managed storage and verify ownership mapping. **Operator response:** Pin and verify image digest/provenance, inspect storage driver and writable-layer usage, run rootless where compatible and externalize durable state. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Container images are layered OCI artifacts fetched from registries; overlay filesystems combine immutable layers with a writable layer.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `podman image inspect <image> 2>/dev/null` and follow the evidence path: Pin and verify image digest/provenance, inspect storage driver and writable-layer usage, run rootless where compatible and externalize durable state.

**Q: How would you verify or falsify the working diagnosis?**

A: A container loses uploaded files when replaced because data lived in its writable layer; move durable data to managed storage and verify ownership mapping. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
