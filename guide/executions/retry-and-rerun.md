# Retrying and rerunning pipelines

After a run ends, you have two distinct ways to run it again. Retry resumes
a failed execution from the point of failure with the same inputs. Rerun
starts a fresh execution using the previous run's inputs.

| | Retry | Rerun |
|---|---|---|
| What runs | The failed portion of the same execution | A new execution from the start |
| Inputs | Identical | Same as previous run |
| Precondition | `canRetry` is true | `canReExecute` is true |
| v1 endpoint | `.../pipelines/{pipeline}/execute/retry/{execution-id}` | `.../pipelines/{pipeline}/execute/rerun/{execution-id}` |

Use retry when the failure was environmental — a flaky connection, an
infrastructure hiccup — and the completed stages are still valid. Use rerun
when you want a clean run of the whole pipeline. To change input values,
start a normal new run instead.

The execution summary tracks retry ancestry (`retryExecutionMetadata`,
`isRetriedExecution`, `showRetryHistory`), so you can trace a chain of
retries in the execution history.

Both operations also have selective-stage forms, which run a subset of
stages (`.../execute/stages`, `.../execute/rerun/{execution-id}/stages`).

---
**Sources:** corpus/path_tree.txt (retry, rerun, canRetry, stage-selective
endpoints); corpus/entity_schemas.md (PipelineExecutionSummary retry
fields, canRetry/canReExecute).
