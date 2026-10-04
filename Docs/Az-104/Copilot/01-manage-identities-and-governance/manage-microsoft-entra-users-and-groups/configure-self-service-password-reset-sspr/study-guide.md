# Configure self-service password reset (SSPR)

Syllabus: [Domain 1 — Manage Azure identities and governance](../../../copilot-az104-syllabus.md#1-manage-azure-identities-and-governance-20-25)

## What

Configure Microsoft Entra self-service password reset so eligible users can verify their identity and reset or unlock an account without help-desk intervention. Configuration includes user scope, authentication methods and their required count, registration, notifications, and on-premises password writeback where hybrid scenarios require it.

## Why

SSPR reduces service-desk load and improves recovery time, but it is an authentication control and must balance usability with assurance. The allowed reset methods, verification strength, and user population should align with organizational risk. Hybrid password writeback adds a dependency on synchronization configuration and on-premises connectivity.

## How

In the portal, open **Microsoft Entra ID > Password reset** and configure the target scope (selected users/groups or all), authentication methods, registration, notifications, and any writeback settings. Test using a pilot account, verify the user's registered methods, and test the actual reset flow. Microsoft Graph supports configuration automation; Azure CLI is not the primary complete interface for SSPR policy. For hybrid writeback, validate the synchronization agent and permissions with the official deployment guidance.

## Features

- SSPR can be scoped rather than enabled tenant-wide immediately.
- The required number of methods and selected method combinations affect usability and assurance; available methods can depend on licensing and tenant policy.
- Password writeback synchronizes cloud reset changes to an on-premises directory when configured and supported.
- **Exam trap:** configuring SSPR does not automatically ensure users have registered valid methods, nor does it imply password writeback is active.

**Microsoft Learn:** [Enable self-service password reset](https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-sspr); [Password writeback overview](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-writeback)

## Code snippets (if any)

No snippet required. SSPR policy and writeback settings are tenant-level security configuration; use the portal for a controlled pilot or the current Microsoft Graph documentation for automation rather than a brittle tenant-specific script.

## Do's and Don'ts

- Do stage rollout, communicate registration requirements, and monitor reset failures.
- Do verify authentication methods meet policy and separately test hybrid writeback.
- Don't select weak recovery methods merely to simplify adoption.
- Don't assume every user is in scope or writeback is enabled just because the policy is configured.

## Real-life implementation

A hybrid organization enables SSPR for an IT pilot group first, requires approved verification methods, and publishes enrollment instructions. It tests a cloud-only account and a synchronized account separately; the latter confirms the reset reaches the on-premises source. After reviewing help-desk data and security approval, rollout expands in controlled waves.

## Q&A

**Q: What does SSPR reduce?**
A: Dependence on the service desk for eligible user password resets.

**Q: Why start with a selected group?**
A: It limits blast radius and allows authentication-method and user-experience testing.

**Q: Does cloud SSPR automatically update on-premises passwords?**
A: No. Password writeback must be supported and configured for the hybrid environment.

**Q: What common issue blocks a user's reset even after enablement?**
A: The user may be out of scope or may not have registered the required verification methods.
