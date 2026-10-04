# GH-200 study guide: enforce action-usage policies

## What

Action-usage policies determine which actions, reusable workflows, and local actions repositories may run. Organization and enterprise settings can allow all actions, allow selected actions, or disable actions; restrictions can also require full-length commit SHAs. Repository policy is subject to the higher-level organization or enterprise policy. Policies can include actions from specified owners, selected repositories, and GitHub-authored actions; policy capabilities depend on plan and administrative scope.

Objective link: [GH-200 syllabus — implement security best practices](../../../../copilot-github-syllabus.md#implement-security-best-practices).

## Why

An unreviewed action executes code in the workflow's security context. It may read accessible workspace data, use granted tokens or secrets, and communicate externally. Central policy reduces inconsistent trust decisions and limits supply-chain exposure, but does not make an allowed action safe or replace review and pinning.

## How

- Set the narrowest practical allow policy at the organization or enterprise level, then make repository-level settings stricter where needed.
- Explicitly review exceptions and update policy when workflows add dependencies; policy settings do not retroactively audit the safety of existing workflows.
- Require full-SHA references where supported and pair allowlists with an action review/upgrade process.
- Distinguish an allowlist from an execution-time human approval: GitHub's available controls vary by policy scope and plan. Do not assume a universal per-use “required reviewer for unverified actions” switch; enforce review through applicable rules, governance, and change controls.
- If unverified-action use requires review, protect workflow changes with CODEOWNERS/branch protection or another documented approval process. Workflow-run approval settings are separate and do not certify an action's safety.
- Validate policy behavior with a test repository before rollout, and communicate which actions and reusable workflows are permitted.

## Features

- **Allow/deny controls:** restrict which sources can be used; exact choices and inheritance behavior depend on enterprise and organization settings.
- **SHA requirements:** policy may require actions to be pinned to full-length SHAs.
- **Governance scope:** enterprise and organization controls provide broad defaults; repository administrators may have narrower controls only where higher-level settings permit them.
- **Review gates:** repository rules can require designated reviewers for workflow changes that introduce unverified actions; run-approval controls should not be confused with action verification.
- **Operational exception path:** documented owners, reasons, review dates, and removal criteria make exceptions auditable.

## Do's and Don'ts

**Do**
- Keep the approved set small, explain its trust basis, and review it periodically.
- Test policy changes on representative workflows and communicate blocked dependencies before enforcement.
- Track exceptions and include an owner, expiration/review date, and compensating controls.
- Combine policy with immutable references, least-privilege token permissions, and workflow review.

**Don't**
- Assume Marketplace listing, popularity, or an owner allowlist certifies an action's code.
- Treat a denylist as complete protection; new repositories, aliases, or unreviewed permitted sources can still introduce risk.
- Assume a repository setting can override a stricter organization or enterprise rule.
- Imply policy checks will approve every use manually or inspect action behavior for vulnerabilities.

## Real-life implementation

An organization limits production repositories to a small set of reviewed actions and reusable workflows, requires full-SHA references where its policy supports that requirement, and tests the restriction in a pilot repository. A deployment workflow that adopts a new action first requests a documented exception; security reviews the exact source and commit, then either approves an appropriately scoped exception or adds the dependency to the approved set. This prevents a compromised or newly introduced dependency from being accepted merely because a workflow author can reference it.

## Q&A

**Q: Does an allowlisted action become safe by policy?**

A: No. The policy permits its use; teams must still assess ownership, code, permissions, release changes, and the exact referenced revision.

**Q: Can a repository loosen an organization-wide restriction?**

A: No. More-specific settings cannot override stricter inherited enterprise or organization controls.

**Q: Does an action allowlist replace full-SHA pinning?**

A: No. An allowlist controls eligible sources; a full SHA fixes the code revision used for a run. Both reduce different risks.

**Q: Should every organization block all actions?**

A: Not necessarily. A narrow approved set is stronger, but must balance supply-chain risk against the effort of reviewing and maintaining dependencies.

### References

- [About GitHub Actions policy](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization)
- [Restricting GitHub Actions](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization)
- [Allowing specific actions to run](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#allowing-specific-actions-to-run)
