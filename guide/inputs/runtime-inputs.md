# Runtime inputs and expressions

Most settings in a pipeline accept a fixed value, a runtime input, or an
expression. You choose per setting.

## Fixed values

Fixed values are defined when you configure the setting and don't change at
runtime. Use them for settings that define the pipeline's identity, such as
the codebase connector.

## Runtime inputs

A runtime input is the placeholder `<+input>`. It marks a value you'll
provide when the pipeline runs:

```yaml
- step:
    identifier: Run_1
    type: Run
    spec:
      shell: <+input>
      command: <+input>
```

Almost any setting can be a runtime input, including variables, artifacts,
connectors, environments, infrastructures, services, secrets, and looping
strategies.

You can constrain runtime inputs with allowed values and defaults:

```yaml
value: <+input>.allowedValues(P0,P1,NA)
value: <+input>.default("main")
```

The set of `<+input>` fields is effectively the pipeline's signature. When
you change it, saved callers go stale: input sets are flagged `isOutdated`,
and triggers are flagged `isPipelineInputOutdated`. Update input sets and
trigger inputs whenever you change a pipeline's runtime inputs — a trigger
with a missing input value fails the run.

## Expressions

Expressions reference values from the pipeline's live context and are
resolved during execution:

- `<+pipeline.variables.NAME>`, `<+stage.variables.NAME>` — variables
- `<+secrets.getValue("token")>` — secrets
- `<+service.name>`, `<+env.name>` — the resolved service and environment
- `<+trigger.payload.pull_request.number>` — trigger event data

Expressions also work inside files fetched at runtime. For example, a
Kubernetes `values.yaml` can contain `<+stage.variables.NAME>`, and Harness
substitutes the value during execution.

> **Note**
> Runtime input values are visible to anyone with permission to run the
> pipeline. Passing secret expressions through runtime input can expose
> secret values. The documentation recommends OPA policies that block
> `<+secrets.getValue` in runtime input.

---
**Sources:** docs/platform/variables-and-expressions/runtime-inputs.md
(value types, security note); docs/platform/pipelines/input-sets.md
(what can be runtime input, YAML example);
docs/platform/pipelines/add-a-stage.md (values.yaml substitution);
yaml_examples/continuous-delivery__cd-onboarding__new-user__cd-pipeline-modeling-overview.md.yaml
(allowedValues, default); corpus/entity_schemas.md (InputSetResponse.isOutdated,
NGTriggerDetailsResponseDTO.isPipelineInputOutdated);
docs/platform/triggers/triggering-pipelines.md (trigger input staleness).
