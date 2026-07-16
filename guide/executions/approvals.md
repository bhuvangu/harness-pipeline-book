# Approvals

An approval pauses an execution until a person or a ticket system delivers a
verdict. Approvals run as steps — inside CD stages or in dedicated Approval
stages — and each pending gate is an approval instance attached to the
execution.

Approval types: Harness Approval (user groups approve in the Harness UI),
Jira Approval, ServiceNow Approval, and Custom Approval. Instance statuses:
`WAITING`, `APPROVED`, `REJECTED`, `FAILED`, `ABORTED`, `EXPIRED`.

## Harness Approval step

```yaml
- step:
    type: HarnessApproval
    name: Harness Approval Step
    identifier: Harness_Approval_Step
    timeout: 1d                     # instance expires when exceeded
    spec:
      approvalMessage: Test
      includePipelineExecutionHistory: true
      approvers:
        userGroups: [docs]
        minimumCount: 1
        disallowPipelineExecutor: false
      approverInputs:
        - name: foo
          defaultValue: bar
```

Key settings:

- `approvers.userGroups` and `minimumCount` define who approves and how many
  approvals are required.
- `disallowPipelineExecutor` prevents whoever started the run from approving
  it.
- `approverInputs` collects values from the approver that later steps can
  read — for example, a change-ticket number.

While the approval waits, the execution is parked (`TimedWaiting`); when the
`timeout` elapses without a verdict, the instance becomes `EXPIRED` and the
gate does not pass.

A common placement is between deployment phases — for example, between
deploying a new version to the staging slice and switching production
traffic to it in a blue-green stage.

---
**Sources:** corpus/entity_schemas.md (ApprovalInstanceResponse type and
status enums, HarnessApprovalActivity);
docs/continuous-delivery/x-platform-cd-features/cd-steps/approvals/using-harness-approval-steps-in-cd-stages.md
(YAML and placement guidance); corpus/path_tree.txt
(`/pipeline/api/approvals/{approvalInstanceId}/harness/activity`,
`/v1/.../approvals/execution/{execution-id}`).
