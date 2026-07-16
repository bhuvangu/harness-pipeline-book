# Execution statuses and the execution graph

## Statuses

The execution summary reports one of the following statuses (quoted from the
API schema): `Running`, `AsyncWaiting`, `TaskWaiting`, `TimedWaiting`,
`Failed`, `Errored`, `IgnoreFailed`, `NotStarted`, `Expired`, `Aborted`,
`Discontinuing`, `Queued`.

How to read them:

| Status group | Meaning |
|---|---|
| `AsyncWaiting`, `TaskWaiting`, `TimedWaiting` | The engine is parked: on an async callback, a delegate task, or a timer. Approvals and manual interventions park executions this way. |
| `Queued` | Admitted but not started. See "Queued executions" below. |
| `Discontinuing` | An abort in progress. Aborts finish the current task first, so they are not instantaneous. |
| `Failed` vs `Errored` | Your workload failed, versus the system couldn't execute it. |
| `IgnoreFailed` | A failure converted to success by an Ignore failure strategy. |
| `Expired` | A deadline passed, such as an approval timeout. |

> **Note**
> The schema's status enum contains no `Success` value, although the UI and
> docs clearly show successful runs. This looks like a truncation in the
> schema digest. See
> [Known issues and open questions](../reference/open-questions.md).

## The execution graph

The runtime structure of a run is an explicit graph with a root node, a node
map, and an adjacency list. Nodes correspond to the pipeline structure you
wrote — stages, step groups, steps — plus runtime expansions such as matrix
iterations.

You can fetch the whole graph
(`/pipeline/api/pipelines/execution/getExecutionGraph/{planExecutionId}`) or
drill into one node's subgraph. This is the API view behind the execution
details page.

## Queued executions

Executions can wait before starting for three reasons: the pipeline has
resource constraints, the maximum concurrent executions limit is reached, or
the pipeline is waiting on a lock held by another pipeline. Queue positions
are calculated account-wide.

An Executions Management page lists queued executions and supports single
and bulk abort. Aborting a queued execution removes it permanently — you
must trigger the pipeline again to run it. (Feature-flagged; see
[Known issues and open questions](../reference/open-questions.md).)

---
**Sources:** corpus/entity_schemas.md (PipelineExecutionSummary status enum
quoted verbatim; ExecutionGraph);
docs/platform/pipelines/executions-and-logs/executions-management.md
(queue reasons, abort behavior); corpus/path_tree.txt (graph and
queue-management endpoints);
docs/platform/pipelines/failure-handling/define-a-failure-strategy-on-stages-and-steps.md
(paused state during manual intervention, "success (failure ignored)").
