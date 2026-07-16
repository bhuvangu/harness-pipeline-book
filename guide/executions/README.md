# Managing executions

Every pipeline run creates an execution: a first-class record with its own
identifier (`planExecutionId`), a run counter, an execution graph, and a
status. This section covers how executions move through their lifecycle and
the controls you have over them — aborting, retrying, failure strategies,
and approvals.

The name `planExecutionId` reflects how runs work: Harness compiles your
pipeline YAML into an execution plan — templates resolved, inputs merged,
looping strategies expanded — and then walks that plan as a node graph.

An execution records what started it (`executionTriggerInfo`), the inputs it
ran with, stage-level results, Git details for remote pipelines, and retry
ancestry.

## Topics

- [Execution statuses and the execution graph](statuses-and-graph.md)
- [Failure handling](failure-handling.md)
- [Retrying and rerunning pipelines](retry-and-rerun.md)
- [Approvals](approvals.md)

---
**Sources:** corpus/entity_schemas.md (PipelineExecutionSummary,
ExecutionGraph); corpus/path_tree.txt
(`/pipeline/api/pipelines/execution/...` subtree).
