# GH-200 study guide: mitigate script injection

## What

Script injection occurs when attacker-controlled data is interpreted as shell syntax or otherwise changes a command's behavior. Workflow expressions are evaluated before the generated script is run, so directly inserting an issue title, PR branch name, comment, commit message, or dispatch input into `run:` can turn data into code.

Objective link: [GH-200 syllabus — implement security best practices](../../../../copilot-github-syllabus.md#implement-security-best-practices).

## Why

An attacker may craft an untrusted value that changes commands, reads workspace contents, or abuses the job's token and secrets. Risk grows when a workflow has write permissions, cloud access, or runs privileged operations. Shell quoting helps but is not a complete defense against unsafe parsing, option injection, path traversal, or unsafe use of `eval`.

## How

- Avoid expression interpolation of untrusted values directly into `run:` script source.
- Pass values through an environment variable, then validate against the expected format and use quoted variable expansion.
- Use an allowlist when the value has a constrained domain; reject invalid values rather than trying to strip dangerous characters.
- Use parameterized APIs/actions where possible, avoid `eval`, and keep permissions and secrets minimal.
- Treat values sent to actions, filenames, and generated config as untrusted too; validate for the target context.

```yaml
steps:
  - name: Validate and use dispatch input
    env:
      IMAGE_TAG: ${{ inputs.image_tag }}
    shell: bash
    run: |
      if [[ ! "$IMAGE_TAG" =~ ^[A-Za-z0-9._-]+$ ]]; then
        echo "Invalid image tag" >&2
        exit 1
      fi
      printf 'Using tag: %s\n' "$IMAGE_TAG"
```

The environment-variable boundary prevents the expression from rewriting the script source; the allowlist validates the intended tag syntax. Keep the value quoted when used later.

## Features

- **Expression timing:** `${{ }}` is expanded before the runner invokes the shell; shell quoting cannot undo unsafe source interpolation.
- **Environment boundary:** pass untrusted values as environment data rather than embedding them into script text.
- **Validation and context-aware encoding:** enforce allowed formats and use APIs/escaping appropriate to the consumer.
- **Least privilege:** reduced token permissions and secret exposure limit impact if a vulnerability remains.

## Do's and Don'ts

**Do**
- Review every context expression used in a `run:` block, especially PR and issue fields.
- Validate structured inputs before using them as refs, paths, tags, or command arguments.
- Quote shell variables and use safe APIs instead of constructing shell command strings.
- Keep untrusted-event jobs read-only and separate them from privileged deployment jobs.

**Don't**
- Write `run: echo "${{ github.event.pull_request.title }}"` or interpolate user data directly into command source.
- Assume that moving input into `env:` alone validates it or makes every later use safe.
- Use `eval`, concatenate commands from user-controlled strings, or rely on blacklist-only sanitization.
- Expose secrets or write tokens to workflows that process untrusted contributions unless a carefully isolated design requires it.

## Real-life implementation

A pull-request workflow reports a title in a check summary. It passes the title through an environment variable, treats it as plain text, and never uses it to build a command. A separate deployment workflow runs only from a protected branch and has production credentials. This prevents a malicious PR title from becoming shell syntax and ensures the reporting job cannot deploy even if its data handling has a defect.

## Q&A

**Q: Why can direct `${{ ... }}` interpolation in `run:` be dangerous?**

A: Expression expansion happens before shell execution, so untrusted text can alter the generated script.

**Q: Does using `env:` eliminate injection risk?**

A: It avoids inserting data into script source, but the value still needs safe quoting, validation, and context-aware handling.

**Q: Is quoting sufficient for every input?**

A: No. Quoting addresses shell word splitting and metacharacters in many cases, but it does not validate semantic formats, prevent all option/path issues, or make `eval` safe.

**Q: Why reduce `GITHUB_TOKEN` permissions in an input-processing job?**

A: If input handling is exploitable, least privilege limits the actions an attacker can perform with the compromised job.

### References

- [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [Workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Using GitHub Actions environment variables](https://docs.github.com/en/actions/learn-github-actions/variables)
