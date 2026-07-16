# Variables

Variables are named values you define once and reference by expression.
You can define them as standalone resources at account, organization, or
project scope, or inline on pipelines, stages, services, and environments.

Higher-scope variables are visible to all lower scopes. Service and
environment variables are available in the stages that use those services
and environments. Stage variables are available across the pipeline, and
later stages can override their values.

## Reference syntax

| Defined at | Expression |
|---|---|
| Account | `<+variable.account.VAR_NAME>` |
| Organization | `<+variable.org.VAR_NAME>` |
| Project | `<+variable.VAR_NAME>` |
| Pipeline | `<+pipeline.variables.VAR_NAME>` |
| Stage (same stage) | `<+stage.variables.VAR_NAME>` |
| Stage (from another stage) | `<+pipeline.stages.STAGE_ID.variables.VAR_NAME>` |

## Defining variables

Inline stage variables:

```yaml
- stage:
    variables:
      - name: VAR_NAME
        type: String     # docs show String or Secret for stage variables
        value: 90
```

Variable values can themselves be fixed values, runtime inputs, or
expressions — so a variable can also serve as a declared parameter.

> **Note**
> The standalone variable entity's API declares only the `String` type,
> while the stage-variable documentation shows String or Secret. See
> [Known issues and open questions](../reference/open-questions.md).

---
**Sources:** docs/platform/variables-and-expressions/add-a-variable.md
(scopes, visibility, reference table);
docs/platform/pipelines/add-a-stage.md (stage variable YAML, overriding);
corpus/entity_schemas.md (VariableDTO type enum);
corpus/path_tree.txt (`/ng/api/variables`).
