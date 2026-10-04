# 7c. Describe when and how to use verbose logging

## What

Terraform diagnostic logging provides detail for failures not explained by ordinary command output, such as provider protocol errors, API request failures, plugin startup problems, or unexpected internal behavior. `TF_LOG` controls verbosity. Supported levels include `TRACE`, `DEBUG`, `INFO`, `WARN`, and `ERROR`; `TRACE` is most verbose. `TF_LOG_PATH` selects a log-file destination when logging is enabled.

## Why

Targeted diagnostics can help isolate whether a problem is in Terraform core, a provider, or an external interaction. Logs are a troubleshooting aid, not a repair or execution mode. They can be large and reveal resource identifiers, request details, configuration fragments, and values that should be treated as secrets, even if normal CLI output marks them sensitive.

## How

Reproduce the issue with the narrowest useful command and capture logs only for the shortest practical interval. In PowerShell:

```powershell
$env:TF_LOG = "DEBUG"
$env:TF_LOG_PATH = "$PWD\terraform-debug.log"
terraform plan
Remove-Item Env:TF_LOG
Remove-Item Env:TF_LOG_PATH
```

On Unix-like shells, export the variables for the controlled session and unset them afterward. Set `TF_LOG=off` or unset it to disable Terraform logging. `TF_LOG_CORE` and `TF_LOG_PROVIDER` can narrow logging to Terraform core or provider components when supported/appropriate. `TF_LOG=JSON` requests JSON-formatted logs in Terraform versions supporting this special setting; it is a format option, not an ordinary severity level.

Protect the log destination with restrictive permissions, follow retention policy, and sanitize output before sharing. Do not commit logs or publish them in broadly visible CI artifacts. Provider-specific logging controls may be separate. Record Terraform/provider versions, command, relevant sanitized context, then disable logging and retry normally to confirm the failure.

## Features

* `TF_LOG` enables and selects Terraform diagnostic verbosity; `TRACE` is more detailed than `DEBUG`.
* `TF_LOG_PATH` selects a file destination but does not itself enable logging.
* `TF_LOG_CORE` and `TF_LOG_PROVIDER` can scope diagnostics; `TF_LOG=JSON` is supported in Terraform versions with JSON logging.
* Component logs and provider/external-tool logging may have separate controls.

## Do's and Don'ts

**Do**
* Start at the lowest useful verbosity and capture a minimal, reproducible failure.
* Restrict access to log files, redact sensitive details before sharing, and remove them under retention rules.
* Unset or turn off logging after the diagnostic run and retest normally.

**Don't**
* Leave trace logging enabled persistently in production automation.
* Assume sensitive Terraform values or provider request details are automatically redacted.
* Commit logs, expose them in public tickets, or use verbose logging as a substitute for diagnosing the cause.

## Real-life implementation

A controlled staging plan fails with an unexplained provider API error. An operator records the Terraform and provider versions, enables `DEBUG` only for that run, directs output to a restricted local file, and limits the reproduction to the affected workspace. They redact identifiers and credentials before sharing the relevant excerpt with the team, remove the log according to policy, unset both variables, and rerun the plan normally after the provider issue is addressed. Production pipelines are not changed to retain verbose logs.

## Q&A

1. **Which variable enables Terraform diagnostic logging?** `TF_LOG`.
2. **Does setting only `TF_LOG_PATH` necessarily enable logging?** No; set `TF_LOG` to a supported level.
3. **Which is more verbose, `TRACE` or `DEBUG`?** `TRACE`.
4. **Why protect diagnostic logs like secrets?** They may contain sensitive values and operational/API details.

Sources: [Terraform CLI environment variables](https://developer.hashicorp.com/terraform/cli/config/environment-variables), [Terraform debugging](https://developer.hashicorp.com/terraform/internals/debugging).

[Back to the Terraform Associate 004 syllabus](../../../copilot-terraform-syllabus.md)
