# 6b — Describe state locking

## What

State locking coordinates Terraform operations that might write state. A locking-capable backend acquires a lock so another operation cannot concurrently mutate the same state. This protects the integrity of Terraform's address-to-object mapping and guards against conflicting or lost state updates; it does not lock cloud resources or prevent external infrastructure changes.

Terraform automatically locks when the configured backend supports locking and the operation requires it. Support and semantics depend on the backend. The local backend can use local filesystem locking, but that is not a cross-machine coordination service. Locking is scoped to a state; separate states/workspaces can operate independently.

## Why

Concurrent state writers can overwrite updates or corrupt the relationship between configuration and infrastructure. Locking provides safe serialization for that state, while pipeline coordination, backend availability, and permissions remain operational requirements.

## How

If a lock is already held, Terraform ordinarily stops and reports lock information. Use `-lock-timeout` to wait for a lock; do not bypass it simply because an operation is taking time.

```shell
terraform plan -lock-timeout=5m
terraform apply -lock-timeout=5m
```

`-lock=false` disables locking for that command and is generally unsafe unless exclusive control of that state is positively established. `terraform force-unlock LOCK_ID` removes a lock, but does not stop the process that acquired it or undo changes. Use it only after verifying that the operation is dead, the lock is genuinely stale, and the lock ID/backend/state match the abandoned run. `-force` suppresses confirmation; it does not reduce the risk.

## Features

- Automatic lock acquisition applies to state-writing operations when supported.
- `-lock-timeout` waits for lock availability.
- `-lock=false` disables a safety mechanism for a command.
- `force-unlock` removes a lock only; it does not terminate an operation or repair state.
- Backend capability, lock-service permissions, and operational availability matter.

## Do's and Don'ts

**Do**
- Serialize deployment pipelines per state and coordinate operators.
- Wait or diagnose contention before taking action; use a reasonable lock timeout.
- Before force-unlocking, verify no operation is running and confirm the exact lock ID and state.
- Restrict permissions to administer state and locks, and monitor abandoned runs.

**Don't**
- Force-unlock a slow, live, or unknown operation.
- Assume every backend supports locking or that locking protects infrastructure from out-of-band edits.
- Use `-lock=false` as a routine way to make a pipeline proceed.
- Assume force-unlock rolls back work, terminates the lock holder, or repairs a state file.

## Real-life implementation

In production, configure a backend with documented locking behavior and permissions, and serialize CI/CD applies for each state/workspace while allowing independent states to proceed. Set a lock timeout appropriate to expected plan/apply duration and provide operators with run ownership, logs, and escalation steps. For an abandoned lock, investigate the runner and backend first; confirm the process has ended and that no writer can resume before force-unlocking the matching lock ID. Afterwards inspect state and run a fresh plan before allowing another apply.

## Q&A

1. **What does a state lock protect?** Concurrent state writes, not cloud resources from external changes.
2. **Does every backend support locking?** No. It depends on backend capabilities.
3. **What should be checked before `force-unlock`?** Confirm the operation is no longer running, the lock is stale, and the ID belongs to the correct state.
4. **What does `-lock-timeout` do?** Waits for a lock to become available instead of disabling locking.

**Official references:**

- [State locking](https://developer.hashicorp.com/terraform/language/state/locking)
- [Force-unlock command](https://developer.hashicorp.com/terraform/cli/commands/force-unlock)

[Back to the Terraform Associate syllabus](../../../copilot-terraform-syllabus.md)
