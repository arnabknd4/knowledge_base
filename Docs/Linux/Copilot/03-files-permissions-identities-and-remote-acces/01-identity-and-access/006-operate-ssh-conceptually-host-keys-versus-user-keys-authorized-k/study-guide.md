# Operate SSH conceptually: host keys versus user keys, authorized keys, agent forwarding risk, configuration precedence, known-host verification, bastions, and tunnels.

**Syllabus objective (exact wording):** Operate SSH conceptually: host keys versus user keys, authorized keys, agent forwarding risk, configuration precedence, known-host verification, bastions, and tunnels.

**Mapping:** `03` → `006` `Operate SSH conceptually: host keys versus user keys, authorized keys, agent forwarding risk, configuration precedence, known-host verification, bastions, and tunnels.`

## What

SSH host keys authenticate the server to the client; user keys authenticate the client to the server. `known_hosts`, `authorized_keys`, agent forwarding, bastions and tunnels each have distinct trust and exposure implications.

## Why

This matters operationally: A changed host key after rebuild may be legitimate or interception; verify through the provider console/owner before updating known_hosts rather than disabling checking. The decision hinges on these mechanics: `known_hosts`, `authorized_keys`, agent forwarding, bastions and tunnels each have distinct trust and exposure implications.

## How

1. **Establish the relevant boundary:** SSH host keys authenticate the server to the client; user keys authenticate the client to the server. Confirm the target release and actual service/process context before selecting the check.
2. **Apply the operator method:** Verify the presented host-key fingerprint through a trusted channel, inspect effective client settings, and use narrowly scoped forwarding/tunnels only where required.
3. **Exercise the scenario:** A changed host key after rebuild may be legitimate or interception; verify through the provider console/owner before updating known_hosts rather than disabling checking.
4. **Verify this outcome:** use `ssh -G <host> | head -30` first, then the remaining checks as needed. The specific success/failure discriminator is the behavior described in the technical explanation above; record what the observation proves and what it does not.
5. **Choose a response:** change only the layer the evidence implicates. If the result disagrees with the working hypothesis, stop and test the adjacent layer rather than applying a familiar fix.

## Features

**Technical mechanics:** `known_hosts`, `authorized_keys`, agent forwarding, bastions and tunnels each have distinct trust and exposure implications.

    **Distro/release distinction:** RHEL-family commonly enforces SELinux, while Ubuntu commonly enables AppArmor; both still use DAC. PAM/NSS/SSSD and OpenSSH defaults depend on release and identity integration. Verify the active package, service, kernel feature or policy source on the target image before relying on a distro default.

**Failure mode to recognize:** A changed host key after rebuild may be legitimate or interception; verify through the provider console/owner before updating known_hosts rather than disabling checking. The common diagnostic error is to act on a neighboring layer before establishing the boundary named in this objective.

## Code snippets (if any)

Inspection/validation examples; replace angle-bracket placeholders with a reviewed target. Options and tool availability vary by release; review output for secrets before sharing.

```sh
ssh -G <host> | head -30
ssh-keygen -F <host>
ssh -vvv <host> 2>&1 | tail -30
```

## Do's and Don'ts

- **Do:** Verify the presented host-key fingerprint through a trusted channel, inspect effective client settings, and use narrowly scoped forwarding/tunnels only where required.
- **Don't:** Do not use broad recursive permission changes, disable host-key checking, or directly edit identity databases to bypass an access failure.
- **Lab-only:** destructive or disruptive operations mentioned by this objective must be tested only on disposable systems unless a separately approved production change includes verified backup, impact review and rollback.

## Real life implementation

A changed host key after rebuild may be legitimate or interception; verify through the provider console/owner before updating known_hosts rather than disabling checking. **Operator response:** Verify the presented host-key fingerprint through a trusted channel, inspect effective client settings, and use narrowly scoped forwarding/tunnels only where required. **Evidence to retain:** capture the affected release/context, the relevant command output, and the service/data/policy result that discriminates this failure from the adjacent layer. If the result requires a disruptive change, test the exact procedure in a disposable lab and retain its rollback evidence.

## Q&A

**Q: What technical distinction changes the decision for this objective?**

A: SSH host keys authenticate the server to the client; user keys authenticate the client to the server.

**Q: In this scenario, what should be inspected before intervention?**

A: Start with `ssh -G <host> | head -30` and follow the evidence path: Verify the presented host-key fingerprint through a trusted channel, inspect effective client settings, and use narrowly scoped forwarding/tunnels only where required.

**Q: How would you verify or falsify the working diagnosis?**

A: A changed host key after rebuild may be legitimate or interception; verify through the provider console/owner before updating known_hosts rather than disabling checking. Use the checks shown above to confirm the affected boundary; if the observation disagrees with the hypothesis, investigate the adjacent layer rather than applying the assumed fix.

## References

[Linux man-pages project](https://www.kernel.org/doc/man-pages/) · [RHEL 9 documentation index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9) · [Ubuntu Server documentation](https://ubuntu.com/server/docs) · [Syllabus and full role/lab context](../../../copilot-Linux-syllabus.md)
