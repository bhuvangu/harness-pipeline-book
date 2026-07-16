# Failure handling

Failure handling in Harness is declared, not improvised. Steps, step groups,
and stages accept failure strategies — rules that map error conditions to
actions. Separately, you can interrupt a running execution by aborting it or
marking parts of it as failed.

## Failure strategies

```yaml
failureStrategies:
  - onFailure:
      errors: [AllErrors]
      action:
        type: Retry
        spec:
          retryCount: 2
          retryIntervals: [10s]
          onRetryFailure:
            action:
              type: StageRollback
```

Available actions: Manual Intervention, Mark as Success, Ignore Failure,
Retry Step, Retry Step Group, Abort, Rollback Stage, Rollback Step Group,
and Mark As Failure.

- **Retry** takes a count, intervals, and a post-retry-failure action, and
  can be gated by a JEXL condition.
- **Ignore Failure** lets the stage continue; the step shows as "success
  (failure ignored)" and rollback is not triggered.
- **Manual Intervention** pauses the execution and lets a user choose an
  action (Mark as Success, Ignore Failure, Retry, Abort, or Rollback
  Stage), with a timeout and a post-timeout fallback action.
- **Rollback Stage** rolls the stage back to its state before execution.
  There is no per-step rollback action — rollback is a stage-level concept.
  For CD rollback specifics, see
  [Deployment strategies and rollback](../cd/strategies-and-rollback.md).

## Aborting an execution

When you abort a pipeline, it finishes the current task and then stops with
status `Aborted`. Harness does not clean up resources created during the
run, such as pods. Treat abort as a last resort, because skipping
end-of-pipeline cleanup can leave infrastructure in an unresolved state.

## Marking a stage as failed

To stop a stage and still get cleanup, mark it as failed instead of
aborting. Marking as failed routes through the failure-strategy machinery,
so a configured rollback runs and the workspace is reverted.

---
**Sources:** docs/platform/pipelines/failure-handling/define-a-failure-strategy-on-stages-and-steps.md
(action table, retry settings, manual intervention, no step rollback);
docs/platform/pipelines/failure-handling/abort-pipeline.md (abort semantics,
mark-as-failed tip); docs/platform/pipelines/failure-handling/mark-as-failed.md.
