# Set up Azure Monitor alerting

## What

Azure Monitor alerting consists of alert rules, action groups, and (optionally) alert processing rules. A rule evaluates a metric, log query, activity log event, or service-health condition. An action group defines notifications and automation; an alert processing rule modifies or suppresses notifications during defined schedules or scopes.

## Why

Alerting turns telemetry into actionable operations. A sound design detects user-impacting symptoms, routes them to the right responders, reduces duplicate or noisy notifications, and can invoke safe automation.

## How

Define the failure condition and resource scope, choose the signal type, evaluation window/frequency, threshold and dimensions, and configure severity. Link an action group with the intended email/SMS/push/voice, webhook, ITSM, or automation actions supported for the scenario. Use processing rules for maintenance suppression or routing changes. Test end-to-end delivery and review alert history.

## Features

- Metric alerts are efficient for numeric signals; log alerts support KQL-based conditions; Activity Log alerts detect control-plane events.
- Action groups are reusable and may be invoked by multiple alert rules; permissions and supported actions vary.
- Alert processing rules can suppress or change action groups for matching alerts, including scheduled maintenance windows.
- Dynamic thresholds and stateful behavior are available for supported alert types; check current support and evaluation semantics.
- Exam trap: an action group does not detect a condition, and a processing rule is not a substitute for the alert rule.

## Code snippets (if any)

```bash
az monitor metrics alert create --name "<alert-name>" --resource-group "<resource-group>" --scopes "/subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Compute/virtualMachines/<vm-name>" --condition "avg Percentage CPU > 80" --description "Sustained high CPU" --evaluation-frequency 1m --window-size 5m --severity 2
```

This illustrates a metric alert condition; confirm the metric name/operator syntax and required options against the installed Azure CLI version and target resource type. Associate the required action group separately.

## Do's and Don'ts

- Do alert on actionable symptoms, document the responder/runbook, and test notification paths.
- Do use severity consistently and tune thresholds against a baseline and service objectives.
- Do use processing rules for planned suppression, with explicit scope and expiry.
- Don't suppress alerts indefinitely or rely on an email recipient who is not on-call.
- Don't create a high-volume alert for every individual event when aggregation or a sustained threshold better reflects impact.

## Real-life implementation

For production VMs, combine a sustained CPU alert with availability and application-health signals. Route high-severity events to the on-call channel and lower-severity trends to an operations queue. During an approved patch window, apply a time-bounded processing rule, preserve alert evaluation/history, and confirm suppression is removed when the window ends.

## Q&A

1. **What evaluates the signal?** The alert rule.
2. **What defines email/webhook/automation destinations?** An action group.
3. **How do planned maintenance windows avoid notifications?** Use a scoped, time-bounded alert processing rule.
4. **Is an alert processing rule a detection mechanism?** No; it processes alerts after rules generate them.

References: [Azure Monitor alerts overview](https://learn.microsoft.com/azure/azure-monitor/alerts/alerts-overview), [Metric alerts](https://learn.microsoft.com/azure/azure-monitor/alerts/alerts-metric-overview), [Action groups](https://learn.microsoft.com/azure/azure-monitor/alerts/action-groups), [Alert processing rules](https://learn.microsoft.com/azure/azure-monitor/alerts/alerts-processing-rules).

Syllabus: [copilot-az104-syllabus.md](../../../copilot-az104-syllabus.md).
