# Objective study guide

> Architect study guide · Registry operations

## What

**Syllabus objective:** Avoid secrets in command history, source, pipeline logs, and image layers.

## Why

Registry choices determine who publishes or retrieves artifacts and whether a known-good release remains available for recovery.

## How

Credentials must not enter shell history, source, logs, build arguments, metadata, or image layers; revoke suspected leaks. Record an owner, test behavior, and define a recovery step.

## Features

- Identify the security boundary, reliability target, operational owner, and evidence.
- Balance availability and rollback retention against cost, mutable names, and overly broad write permissions.

## Code snippets (if any)

```text
No snippet needed: use supported credential helpers or secret integration; never embed credentials in arguments or build instructions.
```

Placeholders only; test in a disposable environment.

## Do's and Don'ts

- **Do:** Verify the target and effective state; preserve evidence and assign an owner.
- **Don't:** Assume defaults or command success prove the outcome; bypass neither access controls nor rollback planning.

## Real-life implementation

Apply this to a real service in staging: name the owner, expected evidence, failure mode, and fallback. Exercise the procedure before making it a release or operations standard.

## Q&A

Self-check prompts (not claims about an official Docker exam):

**Q: What is the key operational practice?**
**A:** Credentials must not enter shell history, source, logs, build arguments, metadata, or image layers; revoke suspected leaks.

**Q: Which trade-off should be explicit?**
**A:** Balance availability and rollback retention against cost, mutable names, and overly broad write permissions.

**Q: What confirms implementation?**
**A:** Repeatable evidence, an owner, and a recovery action.

## References

- [Syllabus objective](../../../copilot-docker-syllabus.md)
- [Domain index](../../index.md)
- [Official Docker documentation](https://docs.docker.com/build/building/secrets/)
