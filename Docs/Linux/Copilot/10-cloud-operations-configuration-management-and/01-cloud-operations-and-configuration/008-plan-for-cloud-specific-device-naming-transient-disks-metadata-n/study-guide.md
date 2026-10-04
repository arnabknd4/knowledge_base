# Plan for cloud-specific device naming, transient disks, metadata, network interfaces, and provider-managed agents.

**Syllabus objective (exact wording):** Plan for cloud-specific device naming, transient disks, metadata, network interfaces, and provider-managed agents.

**Mapping:** `10` → `008` `Plan for cloud-specific device naming, transient disks, metadata, network interfaces, and provider-managed agents.`

## What

Cloud device names, transient disks, metadata, interfaces and provider agents vary by image/instance generation. Guest names may not map predictably to provider volume identity.

## Why

This matters operationally: An instance replacement loses `/dev/nvme1n1` data thought persistent; verify provider volume attachment and serial mapping before mounting or storing state. The decision hinges on these mechanics: Guest names may not map predictably to provider volume identity.

## How

1. **Establish the relevant boundary:** Cloud device names, transient disks, metadata, interfaces and provider agents vary by image/instance generation. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Resolve device serial/ID and metadata without exposing secrets; test ephemeral disk loss, interface naming and agent startup on each selected image shape.
3. **Exercise the scenario:** An instance replacement loses `/dev/nvme1n1` data thought persistent; verify provider volume attachment and serial mapping before mounting or storing state.
4. **Verify this outcome:** use `lsblk -o NAME,TYPE,SIZE,SERIAL,FSTYPE,MOUNTPOINTS` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** Guest names may not map predictably to provider volume identity.

    **Distro/release distinction:** Cloud-init stages, datasource detection, agents and disk/interface naming differ by provider and image. A custom AMI or Ubuntu cloud image may not behave like a local VM of the same distro. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** An instance replacement loses `/dev/nvme1n1` data thought persistent; verify provider volume attachment and serial mapping before mounting or storing state. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
lsblk -o NAME,TYPE,SIZE,SERIAL,FSTYPE,MOUNTPOINTS
ip -brief address
systemctl --failed --no-pager
cloud-init status --long 2>/dev/null
```

## Do's and Don'ts

- **Do:** Resolve device serial/ID and metadata without exposing secrets; test ephemeral disk loss, interface naming and agent startup on each selected image shape.
- **Don't:** Do not embed secrets in user data/images or roll untested configuration across a fleet; retain a known-good artifact and canary stop condition.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

An instance replacement loses `/dev/nvme1n1` data thought persistent; verify provider volume attachment and serial mapping before mounting or storing state. **Operator response:** Resolve device serial/ID and metadata without exposing secrets; test ephemeral disk loss, interface naming and agent startup on each selected image shape. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: Cloud device names, transient disks, metadata, interfaces and provider agents vary by image/instance generation.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `lsblk -o NAME,TYPE,SIZE,SERIAL,FSTYPE,MOUNTPOINTS` and follow the evidence path: Resolve device serial/ID and metadata without exposing secrets; test ephemeral disk loss, interface naming and agent startup on each selected image shape.

**Q: How would you verify or falsify the working diagnosis?**

A: An instance replacement loses `/dev/nvme1n1` data thought persistent; verify provider volume attachment and serial mapping before mounting or storing state. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[systemd manual index](https://www.freedesktop.org/software/systemd/man/latest/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
