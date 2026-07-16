# YAML and Git-backed storage

Everything you can configure in the Harness UI, you can also represent in
YAML. Pipelines, connectors, triggers, input sets, services, environments,
and freeze windows each have a YAML form whose top-level key names the
entity type (`pipeline:`, `connector:`, `trigger:`, and so on). The create
APIs accept the YAML as a string field, such as `pipeline_yaml`.

## Value types

Most settings accept one of three value forms:

- **Fixed values** are decided when you design the pipeline and don't change
  at runtime.
- **Runtime inputs** use the placeholder `<+input>`. You supply the value
  when the pipeline runs.
- **Expressions** such as `<+stage.variables.NAME>` or
  `<+secrets.getValue("somesecret")>` are resolved during execution.

Almost any setting can use any of the three forms. This is what lets one
pipeline serve many scenarios. For more information, see
[Runtime inputs and expressions](../inputs/runtime-inputs.md).

## Inline and remote storage

Each pipeline, input set, and template is stored either inside Harness
(inline) or in your Git repository (remote). The API exposes this as the
`storeType` field, with values `INLINE`, `REMOTE`, and `INLINE_HC`, together
with `gitDetails` and the connector used to reach the repository.

A remote pipeline behaves like any other pipeline. Git stores the YAML text;
the entity itself — its identifier, executions, triggers, and input sets —
lives in Harness. The APIs include dedicated operations for the Git
lifecycle: importing from Git, reading Git metadata, and moving an entity
between inline and remote storage.

Triggers can select which Git branch or tag to load a remote pipeline from
at execution time using the `pipelineBranchName` and `inputSetBranchName`
properties, including a `$tag:v1.0.0` syntax for tag-based release flows.

> **Note**
> The dedicated Git Experience documentation subtree is not part of this
> guide's corpus. Storage behavior described here rests on the API fields
> and on the pipeline, input-set, and trigger documentation. See
> [Known issues and open questions](../reference/open-questions.md).

---
**Sources:** docs/platform/pipelines/harness-yaml-quickstart.md ("Everything
you can do in the Visual editor, you can also represent in YAML");
docs/platform/variables-and-expressions/runtime-inputs.md (three value
forms); corpus/entity_schemas.md (PipelineExecutionSummary `storeType`
enum, `gitDetails`); corpus/path_tree.txt (import, git-metadata,
move-config endpoints); docs/platform/triggers/triggering-pipelines.md
(branch/tag selection in triggers).
