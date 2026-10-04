# Distinguish containerd, CRI-O, runc, and higher-level orchestration responsibilities.

**Syllabus objective (exact wording):** Distinguish containerd, CRI-O, runc, and higher-level orchestration responsibilities.

**Mapping:** `09` → `005` `Distinguish containerd, CRI-O, runc, and higher-level orchestration responsibilities.`

## What

containerd and CRI-O are runtimes/CRI implementations; runc is an OCI low-level runtime; orchestration schedules and reconciles workloads. Debug by identifying the failed layer and logs.

## Why

This matters operationally: A Kubernetes pod cannot start because CRI socket is unavailable; inspect kubelet and runtime services before modifying container image or application config. The decision hinges on these mechanics: Debug by identifying the failed layer and logs.

## How

1. **Establish the relevant boundary:** containerd and CRI-O are runtimes/CRI implementations; runc is an OCI low-level runtime; orchestration schedules and reconciles workloads. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Trace request from orchestrator to CRI endpoint, runtime service, OCI process and kernel; collect component versions and timestamps before changing runtime configuration.
3. **Exercise the scenario:** A Kubernetes pod cannot start because CRI socket is unavailable; inspect kubelet and runtime services before modifying container image or application config.
4. **Verify this outcome:** use `systemctl status containerd crio kubelet --no-pager 2>/dev/null` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Debug by identifying the failed layer and logs.

    **Distro/release distinction:** The running kernel and distribution/runtime determine cgroup v1/v2, delegation, rootless support and default seccomp/LSM profile. Never infer effective limits from config intent alone. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A Kubernetes pod cannot start because CRI socket is unavailable; inspect kubelet and runtime services before modifying container image or application config. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
systemctl status containerd crio kubelet --no-pager 2>/dev/null
crictl info 2>/dev/null
runc --version 2>/dev/null
```

## Do's and Don'ts

- **Do:** Trace request from orchestrator to CRI endpoint, runtime service, OCI process and kernel; collect component versions and timestamps before changing runtime configuration.
- **Don't:** Do not grant privileged-container access, expose the host runtime socket, or treat namespaces alone as a security boundary.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A Kubernetes pod cannot start because CRI socket is unavailable; inspect kubelet and runtime services before modifying container image or application config. **Operator response:** Trace request from orchestrator to CRI endpoint, runtime service, OCI process and kernel; collect component versions and timestamps before changing runtime configuration. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: containerd and CRI-O are runtimes/CRI implementations; runc is an OCI low-level runtime; orchestration schedules and reconciles workloads.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `systemctl status containerd crio kubelet --no-pager 2>/dev/null` and follow the evidence path: Trace request from orchestrator to CRI endpoint, runtime service, OCI process and kernel; collect component versions and timestamps before changing runtime configuration.

**Q: How would you verify or falsify the working diagnosis?**

A: A Kubernetes pod cannot start because CRI socket is unavailable; inspect kubelet and runtime services before modifying container image or application config. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
