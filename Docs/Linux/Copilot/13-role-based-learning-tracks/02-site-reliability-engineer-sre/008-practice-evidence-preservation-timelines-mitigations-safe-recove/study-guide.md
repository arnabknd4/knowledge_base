# Practice evidence preservation, timelines, mitigations, safe recovery, and blameless learning.

**Syllabus objective (exact wording):** Practice evidence preservation, timelines, mitigations, safe recovery, and blameless learning.

**Role extension:** Site reliability engineer (SRE). This checklist outcome extends, rather than duplicates, the shared technical domains.

**Mapping:** `13` → `008` `Practice evidence preservation, timelines, mitigations, safe recovery, and blameless learning.`

## What

Evidence preservation includes timelines, host/process state, logs, metrics and deployment context; safe mitigation and recovery are separate from root-cause learning.

## Why

This matters operationally: During a CPU incident, record process/pressure samples and deployment time before scaling; report mitigation outcome separately from root-cause confidence. The decision hinges on these mechanics: The operator decision is to follow this distinction in the target release and verify the observed behavior: Capture minimal authorized evidence before restart, record each action/result and confidence, then validate recovery and make blameless follow-up trackable.

## How

1. **Establish the relevant boundary:** Evidence preservation includes timelines, host/process state, logs, metrics and deployment context; safe mitigation and recovery are separate from root-cause learning. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Capture minimal authorized evidence before restart, record each action/result and confidence, then validate recovery and make blameless follow-up trackable.
3. **Exercise the scenario:** During a CPU incident, record process/pressure samples and deployment time before scaling; report mitigation outcome separately from root-cause confidence.
4. **Verify this outcome:** use `date -u -Is` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** The operator decision is to follow this distinction in the target release and verify the observed behavior: Capture minimal authorized evidence before restart, record each action/result and confidence, then validate recovery and make blameless follow-up trackable.

    **Distro/release distinction:** A supported RHEL/Ubuntu/Amazon Linux offering and a community-compatible derivative can have different patch escalation and lifecycle commitments; assign ownership for each layer. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** During a CPU incident, record process/pressure samples and deployment time before scaling; report mitigation outcome separately from root-cause confidence. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
date -u -Is
ps -eo pid,ppid,stat,%cpu,%mem,comm --sort=-%cpu | head
journalctl -k -b --no-pager | tail -50
```

## Do's and Don'ts

- **Do:** Capture minimal authorized evidence before restart, record each action/result and confidence, then validate recovery and make blameless follow-up trackable.
- **Don't:** Do not use production credentials/data in capstones or claim readiness without repeatable evidence, failure handling and rollback.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

During a CPU incident, record process/pressure samples and deployment time before scaling; report mitigation outcome separately from root-cause confidence. **Operator response:** Capture minimal authorized evidence before restart, record each action/result and confidence, then validate recovery and make blameless follow-up trackable. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Evidence preservation includes timelines, host/process state, logs, metrics and deployment context; safe mitigation and recovery are separate from root-cause learning.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `date -u -Is` and follow the evidence path: Capture minimal authorized evidence before restart, record each action/result and confidence, then validate recovery and make blameless follow-up trackable.

**Q: How would you verify or falsify the working diagnosis?**

A: During a CPU incident, record process/pressure samples and deployment time before scaling; report mitigation outcome separately from root-cause confidence. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux kernel documentation](https://docs.kernel.org/) · [systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
