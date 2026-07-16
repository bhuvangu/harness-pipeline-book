# Deployment strategies and rollback

Harness provides the standard deployment strategies as stage execution
patterns. Your choice trades speed against risk and determines what rollback
costs.

## Rolling

Nodes in one environment are replaced with the new version one by one, or in
batches defined by a window size.

Use rolling when you want a balance of speed and safety without extra
infrastructure. A common pattern is a rolling deployment to a QA environment
as the stage before a canary deployment to production. The application and
database must tolerate old and new versions running side by side during the
roll.

## Blue-green

Two identical environments run at the same time with different versions.
You verify the new version on the staging side, then flip traffic at the
load balancer, and decommission the old side when you're confident.

Use blue-green when you need zero downtime and want to verify in a full
production environment. Rollback is nearly instant — flip traffic back. The
cost is running and maintaining a duplicate environment.

## Canary

The new version is rolled out in small phases — for example 2%, 10%, 25%,
50%, 100% — with verification gating each phase. This is currently the most
common way to deploy applications to production: lowest risk, testing with
real users, and cheap, fast rollback.

For Kubernetes, Harness runs canary in two phases: phase 1 deploys canary
instances alongside production and then deletes them; phase 2 performs a
rolling update of the production workload.

## Gates

Approval steps and stages before or between phases give you gated CD;
omitting them is "no-gate CD." Harness supports both. For more information,
see [Approvals](../executions/approvals.md).

## Rollback

Rollback in a Deployment stage is pre-declared. The stage's
`execution.rollbackSteps` contain the mirror-image steps (such as
`K8sRollingRollback`), and a failure strategy of `StageRollback` routes
failures into them:

```yaml
execution:
  steps:
    - step:
        type: K8sRollingDeploy
        ...
  rollbackSteps:
    - step:
        type: K8sRollingRollback
        ...
failureStrategies:
  - onFailure:
      errors: [AllErrors]
      action:
        type: StageRollback
```

Rollback restores the stage to its state before execution; how it does so
depends on the deployment type. Rollback is a stage-level concept — there is
no per-step rollback action. To trigger rollback on a running stage
manually, mark the stage as failed rather than aborting the pipeline. See
[Failure handling](../executions/failure-handling.md).

---
**Sources:** docs/continuous-delivery/manage-deployments/deployment-concepts.md
(all three strategies, pros/cons, Kubernetes canary phases, gates);
yaml_examples/continuous-delivery__cd-onboarding__new-user__onboarding-path.md.yaml
(rollbackSteps YAML);
docs/platform/pipelines/failure-handling/define-a-failure-strategy-on-stages-and-steps.md
(StageRollback action, no step rollback).
