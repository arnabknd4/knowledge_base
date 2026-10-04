# Explain namespaces for PID, mount, network, user, UTS, and IPC isolation; understand that namespaces alone do not provide complete security.

**Syllabus objective (exact wording):** Explain namespaces for PID, mount, network, user, UTS, and IPC isolation; understand that namespaces alone do not provide complete security.

**Mapping:** `09` → `002` `Explain namespaces for PID, mount, network, user, UTS, and IPC isolation; understand that namespaces alone do not provide complete security.`

## What

PID, mount, network, user, UTS and IPC namespaces isolate different views, not all authority. User namespaces map identities; privileged host mounts and kernel attack surface remain shared.

## Why

This matters operationally: A process has a separate PID namespace but can see host files through a bind mount; check `findmnt` and user mapping instead of declaring it isolated. The decision hinges on these mechanics: User namespaces map identities; privileged host mounts and kernel attack surface remain shared.

## How

1. **Establish the relevant boundary:** PID, mount, network, user, UTS and IPC namespaces isolate different views, not all authority. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Inspect namespace links and process capabilities/mounts; test each boundary relevant to threat model and combine namespace isolation with seccomp, LSM and least privilege.
3. **Exercise the scenario:** A process has a separate PID namespace but can see host files through a bind mount; check `findmnt` and user mapping instead of declaring it isolated.
4. **Verify this outcome:** use `lsns -p <pid>` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** User namespaces map identities; privileged host mounts and kernel attack surface remain shared.

    **Distro/release distinction:** The running kernel and distribution/runtime determine cgroup v1/v2, delegation, rootless support and default seccomp/LSM profile. Never infer effective limits from config intent alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A process has a separate PID namespace but can see host files through a bind mount; check `findmnt` and user mapping instead of declaring it isolated. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
lsns -p <pid>
readlink /proc/<pid>/ns/{pid,mnt,net,user,ipc,uts}
findmnt
grep '^Cap' /proc/<pid>/status
```

## Do's and Don'ts

- **Do:** Inspect namespace links and process capabilities/mounts; test each boundary relevant to threat model and combine namespace isolation with seccomp, LSM and least privilege.
- **Don't:** Do not grant privileged-container access, expose the host runtime socket, or treat namespaces alone as a security boundary.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A process has a separate PID namespace but can see host files through a bind mount; check `findmnt` and user mapping instead of declaring it isolated. **Operator response:** Inspect namespace links and process capabilities/mounts; test each boundary relevant to threat model and combine namespace isolation with seccomp, LSM and least privilege. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: PID, mount, network, user, UTS and IPC namespaces isolate different views, not all authority.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `lsns -p <pid>` and follow the evidence path: Inspect namespace links and process capabilities/mounts; test each boundary relevant to threat model and combine namespace isolation with seccomp, LSM and least privilege.

**Q: How would you verify or falsify the working diagnosis?**

A: A process has a separate PID namespace but can see host files through a bind mount; check `findmnt` and user mapping instead of declaring it isolated. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
