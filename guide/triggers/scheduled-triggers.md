# Scheduled triggers

Scheduled triggers start a pipeline on a cron schedule. Use them for
nightly builds, periodic deployments, and recurring housekeeping pipelines.

```yaml
source:
  type: Scheduled
  spec:
    type: Cron
    spec:
      expression: 0/5 * * * *
      type: UNIX
      timezone: America/New_York
```

Set the `timezone` explicitly. Schedules defined without thinking about time
zones are a common source of drift when teams span regions.

A scheduled trigger supplies pipeline input the same way other triggers do:
an input set or inline values. For more information, see
[Starting pipelines with triggers](README.md).

---
**Sources:** yaml_examples/platform__triggers__schedule-pipelines-using-cron-triggers.md.yaml
(YAML example); corpus/entity_schemas.md (ScheduledTriggerSpec,
CronScheduledTriggerSpec);
docs/platform/triggers/schedule-pipelines-using-cron-triggers.md.
