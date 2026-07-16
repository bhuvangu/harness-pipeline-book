# Starting pipelines with triggers

A trigger starts a pipeline when an event occurs: a Git webhook event, a
schedule, or a new artifact or manifest version in a registry. The trigger
decides whether the event matters using conditions, then starts the
pipeline with a specific set of runtime input values.

A trigger belongs to one pipeline and is enabled or disabled independently
of it. Trigger types are Webhook, Artifact, Manifest, Scheduled,
MultiRegionArtifact, and SystemEvent.

```yaml
trigger:
  name: nightly
  identifier: nightly
  enabled: true
  orgIdentifier: default
  projectIdentifier: default
  pipelineIdentifier: my_pipeline
  source:
    type: Scheduled            # or Webhook | Artifact | Manifest
    spec: ...
```

## Supplying pipeline input

A trigger provides the pipeline's runtime inputs from an input set or from
inline values, but not both at the same time. To override individual values
on top of an input set, use the trigger's override-YAML configuration.
Event data is available through expressions such as
`<+trigger.payload.pull_request.number>`.

When you change a pipeline's runtime inputs, update its triggers' inputs as
well. A trigger missing a required input value causes the run to fail, and
the API flags the trigger as `isPipelineInputOutdated`.

## Triggers and deployment freezes

While a freeze window is active, trigger invocations of frozen pipelines are
rejected. Custom webhook triggers can override a freeze if their API key has
the freeze-override permission. For more information, see
[Deployment freeze](../cd/deployment-freeze.md).

## Topics

- [Webhook triggers](webhook-triggers.md)
- [Scheduled triggers](scheduled-triggers.md)
- [Artifact and manifest triggers](artifact-triggers.md)

---
**Sources:** corpus/entity_schemas.md (NGTriggerResponse type enum,
NGTriggerDetailsResponseDTO); yaml_examples/platform__pipelines__harness-yaml-quickstart.md.yaml
(example 18); docs/platform/triggers/triggering-pipelines.md (input rules);
docs/continuous-delivery/manage-deployments/deployment-freeze.md
(trigger rejection during freeze).
