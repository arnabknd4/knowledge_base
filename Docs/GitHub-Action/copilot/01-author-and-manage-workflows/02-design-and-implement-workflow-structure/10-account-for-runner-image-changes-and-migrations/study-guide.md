# Objective: Account for runner image changes and migrations (the study guide calls out Ubuntu 20.04 deprecation and the Windows Server 2025 migration for `windows-latest`).

## What

Runner images are part of the execution platform contract. A hosted runner image update can alter the default toolchain, package versions, and installed software. Treat it like any other infrastructure dependency that requires migration planning.

## Why

- `ubuntu-latest` is convenient but less predictable over time.
- Pinned images provide stability but require deliberate maintenance.
- OS-specific scripts often break during runner image migrations because default tools and paths change.

## How

Select a supported runner label, explicitly provision critical tools, and validate candidate image changes before release-critical use.

```yaml
jobs:
  linux:
    runs-on: ubuntu-22.04
  windows:
    runs-on: windows-2022
```

## Features

GitHub-hosted runner labels point to maintained images whose included software and underlying OS versions change. A `-latest` label is a moving target, not a permanent image snapshot.

**Official references**

- [GitHub-hosted runner images](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#preinstalled-software)
- [Runner images and software](https://github.com/actions/runner-images)
- [GitHub Actions release notes](https://github.blog/changelog/label/github-actions/)

- [Back to topic objectives](../README.md)
- [Back to Author and manage workflows](../../README.md)
- [GH-200 syllabus](../../../../copilot-github-syllabus.md)

## Do's and Don'ts

**Do**

- Review GitHub-hosted runner release notes before broad changes.
- Keep shell and package-install commands resilient to image changes.
- Avoid assumptions about tool availability or default shell behavior across images.

**Don't**

- Don't assume a `latest` tag is stable and immutable.
- Don't overlook that image migrations often break scripts that rely on old versions or paths.
- Don't treat runner technology updates as purely a developer convenience, not a compatibility risk.

## Real-life implementation

Treat image updates as a dependency migration. Test workflow changes on candidate images, remove assumptions about undocumented preinstalls and paths, and use a specific supported label temporarily when stability warrants it.

## Q&A

**Q: Are your workflows pinned to an image version where stability matters?**

**A:** Use a specific supported runner label when reproducibility requires it, while planning upgrades; remember a label still does not freeze every installed tool version.

**Q: Would a runner image update silently break your install scripts or PATH assumptions?**

**A:** It can. Avoid relying on incidental preinstalled tools or fixed paths, and explicitly install or verify required tool versions.

**Q: Do you have a test path for migrations before relying on the latest image behavior?**

**A:** Exercise candidate images in a branch or non-critical workflow, compare logs and tool versions, and migrate before a label transition affects release-critical jobs.
