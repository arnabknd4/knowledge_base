# Configure organizational use policies

## What
Organizational use policies define what automation is allowed, which actions are trusted, and how the enterprise enforces a consistent governance model across repositories. They are the enterprise control plane for GitHub Actions usage.

## Why
Without a policy model, teams choose security and workflow behavior independently, creating drift, hidden trust issues, and uneven compliance. Enterprise policy creates a common security baseline while allowing controlled flexibility where needed.

## How
- Set action allowlists and denylists to control which workflows and actions can be used.
- Require review for unverified actions and differentiate them from verified or internal actions.
- Apply policies at the enterprise or organization level, and use repo and environment controls for exceptions.
- Review policy drift regularly and make exceptions traceable and time-bound when needed.

## Features
- Allowlist and denylist enforcement for actions and repositories.
- Verified vs. unverified action decision-making.
- Policy application at enterprise or organization scope.
- Exception handling and a documented review workflow.

## Do's and Don'ts
- Do: treat policy as an operating model, not a one-time configuration.
- Do: maintain a central catalog of approved actions and action owners.
- Do: pair policy with repository and environment protections.
- Do: use required reviewers for any policy exception or new internal action.
- Don't: assume a verified action is automatically safe.
- Don't: treat enterprise policy as a replacement for environment protections.
- Don't: leave approval lists stale or unowned.
- Don't: apply a broad allowlist without a clear exception model.

## Real-life implementation
An enterprise blocks unverified actions by default and allows only GitHub-owned, vendor-supported, or reviewed internal actions. Production repositories rely on the organization policy plus environment approvals, while dev repos remain slightly more flexible under explicit platform oversight.

## Q&A
### Q: What is the difference between policy and repository settings?
A: Policy sets the enterprise default and trust model; repository settings apply additional local controls within that boundary.

### Q: Why use both allowlists and required reviews?
A: They balance governance with enablement: the enterprise can support innovation while still preventing unsafe or unvetted automation.

### Q: How should exceptions be handled?
A: Exceptions should be documented, owner-assigned, time-bound when possible, and reviewed against the same compliance and security standards as approved assets.

### Q: What happens if an action is later identified as risky?
A: The org can block or remove it from the allowlist, notifying consumers and reducing supply-chain exposure quickly.

## Official docs
- [Enforcing GitHub Actions policies for your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-github-actions-policies-for-your-enterprise)
- [Disabling or limiting GitHub Actions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization)
- [About GitHub Marketplace actions](https://docs.github.com/en/actions/using-workflows/using-github-marketplace-actions)
- [Using actions securely](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)

## Back to syllabus
- [Manage GitHub Actions for the enterprise](../../README.md)
