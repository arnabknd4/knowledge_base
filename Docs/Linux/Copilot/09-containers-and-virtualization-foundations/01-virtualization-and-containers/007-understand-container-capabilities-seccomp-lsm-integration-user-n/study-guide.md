# Understand container capabilities, seccomp, LSM integration, user namespaces, mounts, secrets, and image provenance.

**Syllabus objective (exact wording):** Understand container capabilities, seccomp, LSM integration, user namespaces, mounts, secrets, and image provenance.

**Mapping:** `09` → `007` `Understand container capabilities, seccomp, LSM integration, user namespaces, mounts, secrets, and image provenance.`

## What

Capabilities, seccomp, LSM labels, user namespaces, mounts, secret injection and image provenance are independent controls. A broad privilege flag can defeat several safeguards at once.

## Why

This matters operationally: A build container needs compiler access but not host Docker socket; remove that socket mount and test build output with unprivileged identity. The decision hinges on these mechanics: A broad privilege flag can defeat several safeguards at once.

## How

1. **Establish the relevant boundary:** Capabilities, seccomp, LSM labels, user namespaces, mounts, secret injection and image provenance are independent controls. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Review effective runtime settings and process status; remove unneeded capabilities, block host-sensitive mounts and verify secrets are not embedded in image layers.
3. **Exercise the scenario:** A build container needs compiler access but not host Docker socket; remove that socket mount and test build output with unprivileged identity.
4. **Verify this outcome:** use `grep -E '^(Cap|Seccomp|NoNewPrivs)' /proc/<pid>/status` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** A broad privilege flag can defeat several safeguards at once.

    **Distro/release distinction:** The running kernel and distribution/runtime determine cgroup v1/v2, delegation, rootless support and default seccomp/LSM profile. Never infer effective limits from config intent alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A build container needs compiler access but not host Docker socket; remove that socket mount and test build output with unprivileged identity. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
grep -E '^(Cap|Seccomp|NoNewPrivs)' /proc/<pid>/status
findmnt
podman inspect <container> 2>/dev/null
```

## Do's and Don'ts

- **Do:** Review effective runtime settings and process status; remove unneeded capabilities, block host-sensitive mounts and verify secrets are not embedded in image layers.
- **Don't:** Do not grant privileged-container access, expose the host runtime socket, or treat namespaces alone as a security boundary.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A build container needs compiler access but not host Docker socket; remove that socket mount and test build output with unprivileged identity. **Operator response:** Review effective runtime settings and process status; remove unneeded capabilities, block host-sensitive mounts and verify secrets are not embedded in image layers. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Capabilities, seccomp, LSM labels, user namespaces, mounts, secret injection and image provenance are independent controls.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `grep -E '^(Cap|Seccomp|NoNewPrivs)' /proc/<pid>/status` and follow the evidence path: Review effective runtime settings and process status; remove unneeded capabilities, block host-sensitive mounts and verify secrets are not embedded in image layers.

**Q: How would you verify or falsify the working diagnosis?**

A: A build container needs compiler access but not host Docker socket; remove that socket mount and test build output with unprivileged identity. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
