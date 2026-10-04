# Manage runner groups and troubleshoot runner issues

## What
Runner groups create a governance boundary for self-hosted runners, and they let platform teams decide which repositories or workloads can use each pool. Proper group design and troubleshooting keep production jobs reliable and isolated.

## Why
As runner pools grow, job contention, stale machines, and permission drift become operational problems. Without clear groups and a troubleshooting playbook, failures can cascade across many repositories and teams.

## How
- Organize runners into groups based on trust zone or workload type, such as public CI, internal private, or production deployment.
- Use labels to split runners by OS, region, hardware, or service requirements.
- Monitor queue health, offline status, and job logs as part of a repeatable troubleshooting flow.
- Review group access regularly and remove stale runners or permissions that are no longer required.

## Features
- Runner groups for access control and organizational boundaries.
- Labels for job routing and capacity management.
- Health and queue monitoring for job stability.
- Standard troubleshooting steps across connectivity, permissions, and service state.

## Do's and Don'ts
- Do: assign clear ownership for each runner group.
- Do: keep runner groups aligned with trust boundaries and deployment risk.
- Do: use labels to route jobs to correct hardware or OS pools.
- Do: treat stale registrations and queue backlogs as a lifecycle issue.
- Don't: confuse runner groups with labels; they serve different controls.
- Don't: place production and development workloads into one pool without explicit risk review.
- Don't: ignore permission errors when a runner appears offline or inaccessible.
- Don't: leave a failing runner in the production pool without triage.

## Real-life implementation
An enterprise creates three runner groups: `public-ci`, `private-internal`, and `prod-deploy`. Public CI is open to a subset of repos; internal private runners are limited to controlled workloads; production deploy runners require environment protection and explicit repository access. This reduces incident blast radius and improves operational clarity.

## Q&A
### Q: Why are runner groups and labels both needed?
A: Groups control who can use a runner pool; labels tell jobs which runners are appropriate for a given environment or capability set.

### Q: What is the first step when a self-hosted runner fails a job?
A: Check runner status, logs, service health, and whether the job was routed to the correct pool and permissions model.

### Q: How do you keep production workloads safe?
A: By isolating them in dedicated groups, using explicit labels, and reviewing repository access and environment protection rules regularly.

### Q: What operational metrics matter most?
A: Offline runner count, queue time, failed job patterns, and stale or unauthorized registrations.

## Official docs
- [About self-hosted runner groups](https://docs.github.com/en/actions/hosting-your-own-runners/managing-runners/about-self-hosted-runner-groups)
- [Managing self-hosted runners for an organization](https://docs.github.com/en/actions/hosting-your-own-runners/managing-runners/managing-self-hosted-runners-for-an-organization)
- [Monitoring and troubleshooting self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)
- [Using labels with self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners)

## Back to syllabus
- [Manage GitHub Actions for the enterprise](../../README.md)
