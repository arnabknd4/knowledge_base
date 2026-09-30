# Shell + Bash: Prerequisite Topics (DevOps + SRE + Architect Level)

**Flags:** R = Required | O = Optional | E = Exam-oriented | L = Real-life use

---

## 1. Foundations (Linux and Shell Basics)
- Shell vs Terminal vs Console: R, E
- Shell types (sh, bash, zsh, dash): R, E, L
- Bash vs POSIX sh: R, E, L
- Login vs non-login shell: R, E
- Interactive vs non-interactive shell: R, E, L
- Shell startup files (.bashrc, .bash_profile, .profile, /etc/profile): R, E, L
- Linux filesystem hierarchy (FHS): R, E, L
- Absolute vs relative paths: R, L
- Users, groups, UID/GID: R, E, L
- File permissions (rwx, octal, umask): R, E, L
- Special permissions (SUID, SGID, sticky bit): R, E, L
- Ownership (chown, chmod, chgrp): R, L
- Processes (PID, PPID, parent/child): R, E, L
- Foreground vs background processes: R, E, L
- Signals (SIGTERM, SIGKILL, SIGHUP, SIGINT): R, E, L
- Exit codes / exit status: R, E, L

## 2. Core Shell Features
- Command structure (command, options, arguments): R, L
- Built-in vs external commands: R, E
- Command types (type, which, alias, function): R, E, L
- Aliases: O, L
- Command history and history expansion: O, L
- Tab completion: O, L
- Command substitution: R, E, L
- Brace expansion: R, E, L
- Tilde expansion: O, E
- Wildcards / globbing (*, ?, []): R, E, L
- Extended globbing (extglob, globstar): O, E
- Quoting (single, double, escape, $'...'): R, E, L
- Order of shell expansions: R, E
- Word splitting: R, E, L
- Command separators (;, &&, ||, &): R, E, L
- Grouping (subshell `()` vs `{}`): R, E, L

## 3. Variables and Data
- Variables (declaration, assignment, scope): R, E, L
- Environment variables vs shell variables: R, E, L
- export, readonly, unset: R, E, L
- Special variables ($?, $$, $!, $0, $@, $*, $#, $1...): R, E, L
- Important built-in variables (PATH, HOME, PWD, IFS, PS1, SHELL): R, E, L
- Parameter expansion (default, substring, replace, trim): R, E, L
- Arrays (indexed): R, E, L
- Associative arrays: O, E
- Arithmetic (`$(( ))`, let, expr): R, E, L
- Here-string and here-document: R, E, L
- Variable scope (global, local): R, E, L
- Declare attributes (declare -i, -r, -a, -A, -x): O, E

## 4. Input, Output and Redirection
- stdin, stdout, stderr and file descriptors: R, E, L
- Redirection (>, >>, <, 2>, &>, 2>&1): R, E, L
- Pipes: R, E, L
- Named pipes (FIFO): O, E
- Process substitution (`<()`, `>()`): O, E, L
- tee: R, L
- /dev/null, /dev/zero, /dev/urandom: R, E, L
- read (input, prompts, options): R, E, L
- printf vs echo: R, E, L
- xargs: R, L
- Custom file descriptors (exec 3>): O, E

## 5. Control Flow and Logic
- if / elif / else: R, E, L
- Test operators (`[ ]`, `[[ ]]`, test): R, E, L
- `[ ]` vs `[[ ]]` differences: R, E
- File, string and numeric tests: R, E, L
- Logical operators (&&, ||, !): R, E, L
- case statements: R, E, L
- for loops (list and C-style): R, E, L
- while and until loops: R, E, L
- select loops: O
- break and continue: R, E
- Reading files line by line safely: R, E, L
- Short-circuit evaluation: R, E, L

## 6. Functions and Script Structure
- Functions (define, call, return): R, E, L
- Function arguments and return values: R, E, L
- Local variables in functions: R, E, L
- Recursion: O
- Shebang (#!/bin/bash vs #!/usr/bin/env bash): R, E, L
- Making scripts executable: R, L
- source vs `.` vs execute: R, E, L
- Script arguments and getopts: R, E, L
- Sourcing libraries / modular scripts: R, L
- Idempotent script design: R, L
- Script portability (bash vs POSIX): R, E, L

## 7. Text Processing Toolkit
- grep (basic, extended, PCRE): R, E, L
- Regular expressions (BRE vs ERE): R, E, L
- sed: R, E, L
- awk: R, E, L
- cut, sort, uniq, wc: R, E, L
- tr: R, E, L
- head, tail (including tail -f): R, L
- find: R, E, L
- locate / updatedb: O
- diff, comm, cmp: O, E
- jq (JSON): R, L
- yq (YAML): O, L
- column, paste, join: O
- Log parsing pipelines: R, L

## 8. Error Handling and Debugging
- set -e (errexit): R, E, L
- set -u (nounset): R, E, L
- set -o pipefail: R, E, L
- Strict mode (`set -euo pipefail`): R, E, L
- set -x (xtrace) and bash -x: R, E, L
- PS4 for trace formatting: O
- trap (EXIT, ERR, INT, TERM): R, E, L
- Cleanup patterns (temp files, locks): R, L
- Custom error/logging functions: R, L
- ShellCheck (linting): R, L
- Common pitfalls (unquoted vars, word splitting, globbing): R, E, L
- Return codes best practice: R, E, L

## 9. Process and Job Management
- Job control (&, jobs, fg, bg): R, E, L
- nohup, disown, setsid: R, E, L
- wait: R, E
- ps, top, htop, pgrep, pkill: R, L
- kill, killall: R, E, L
- nice, renice: O, E
- Subshells and environment inheritance: R, E, L
- Zombie and orphan processes: E
- Daemonizing basics: O, E
- timeout command: R, L

## 10. Scheduling and Automation
- cron (syntax, crontab): R, E, L
- at and batch: O, E
- systemd timers: R, L
- systemd services basics: R, E, L
- Running scripts as services: R, L
- Lock files / flock (prevent overlap): R, L
- Cron environment pitfalls: R, E, L

## 11. Networking and Remote Operations
- curl and wget: R, L
- ssh, scp, rsync: R, L
- SSH keys and ssh-agent: R, L
- SSH config file: O, L
- Port and connectivity checks (nc, ss, netstat): R, L
- dig, nslookup, host: R, L
- Remote command execution (ssh heredocs, loops over hosts): R, L
- tmux / screen: O, L
- Parallel execution (xargs -P, GNU parallel): O, L

## 12. System, Storage and Logs
- Disk and filesystem (df, du, lsblk, mount): R, L
- Log files (/var/log, journalctl): R, L
- logrotate: O, L
- tar, gzip, zip: R, L
- Package managers (apt, yum/dnf): R, L
- lsof, strace: O, L
- /proc and /sys basics: O, E
- Resource checks (free, vmstat, iostat, uptime): R, L
- Environment and locale (LANG, LC_ALL): O, E

## 13. Security and Safe Scripting
- Least privilege (sudo, sudoers basics): R, E, L
- Secrets handling (no hardcoded secrets, env vs files): R, L
- Input validation and sanitization: R, E, L
- Command injection risks: R, E, L
- Safe temp files (mktemp): R, E, L
- umask and file permissions in scripts: R, E, L
- PATH hijacking: O, E
- Audit and logging of script actions: O, L
- Checksums and signature verification (sha256sum, gpg): O, L

## 14. DevOps, SRE and Architect Layer
- Shell in CI/CD pipelines (Jenkins, GitLab CI, GitHub Actions): R, L
- Shell in Docker (ENTRYPOINT, CMD, entrypoint scripts): R, E, L
- kubectl scripting and one-liners: R, L
- Shell with cloud CLIs (aws, gcloud, az): R, L
- Bash vs Python/Ansible: when to use which: R, E, L
- Health checks and probe scripts: R, L
- Incident response one-liners: R, L
- Automation toil reduction (SRE principle): R, E, L
- Idempotency and repeatability: R, E, L
- Script testing (bats, shunit2): O, L
- Script versioning and code review: R, L
- Style guide (Google Shell Style Guide): O, E, L
- Bash 3 vs 4 vs 5 differences (macOS vs Linux): O, E, L
- Shell anti-patterns and when not to script: R, E, L

---

## Suggested Study Order
1 → 2 → 3 → 4 → 5 → 6 → 8 → 7 → 9 → 10 → 11 → 12 → 13 → 14