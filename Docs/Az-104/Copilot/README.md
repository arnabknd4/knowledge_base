# AZ-104 Architect-Level Study Library

This library expands the [official AZ-104 syllabus](./copilot-az104-syllabus.md) into objective-level learning material. Each domain contains topic folders, each topic contains a folder per published skill, and each skill folder contains its `study-guide.md`.

## Exam domains

1. [Manage Azure identities and governance](./01-manage-identities-and-governance/index.md)
2. [Implement and manage storage](./02-implement-and-manage-storage/index.md)
3. [Deploy and manage Azure compute resources](./03-deploy-and-manage-compute-resources/index.md)
4. [Implement and manage virtual networking](./04-implement-and-manage-virtual-networking/index.md)
5. [Monitor and maintain Azure resources](./05-monitor-and-maintain-azure-resources/index.md)

## Study method

For each skill, learn the service's responsibility and control plane, then reason about when to choose it, its identity and network boundaries, its availability and recovery behavior, and its cost/operational trade-offs. Practice both portal operations and CLI/PowerShell or ARM/Bicep equivalents. Use a disposable subscription or sandbox for hands-on work; never test destructive operations against production.

Use the Q&A to retrieve concepts without notes, then revisit missed objectives in the official [AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104). Review Microsoft's current practice assessment and exam sandbox before scheduling because skill objectives can change.

Code snippets are illustrative learning examples. Verify current commands, API versions, permissions, regional availability, quotas, and pricing against Microsoft Learn and the target subscription before adapting them.
