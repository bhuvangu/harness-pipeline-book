# Deploying with CD stages

A Deployment stage deploys a service to an environment. It binds three
reusable entities — the service (what you deploy), the environment (where),
and an infrastructure definition (the specific target) — and adds the
execution strategy (rolling, canary, or blue-green) plus a pre-declared
rollback path.

```yaml
- stage:
    name: Rolling Deployment
    identifier: Rolling_Deployment
    type: Deployment
    spec:
      deploymentType: Kubernetes
      service:
        serviceRef: Service_1              # what
      environment:
        environmentRef: Env_1              # where
        infrastructureDefinitions:
          - identifier: Infra_1            # the specific target
      execution:
        steps:
          - step:
              identifier: rolloutDeployment
              type: K8sRollingDeploy
              timeout: 10m
        rollbackSteps:
          - step:
              identifier: rollbackRolloutDeployment
              type: K8sRollingRollback
    failureStrategies:
      - onFailure:
          errors: [AllErrors]
          action:
            type: StageRollback
```

Services and environments are references, not copies. You define them once
and use them from as many pipelines as you need.

## Topics

- [Services](services.md)
- [Environments and infrastructure definitions](environments.md)
- [Service overrides](service-overrides.md)
- [Deployment strategies and rollback](strategies-and-rollback.md)
- [Deployment freeze](deployment-freeze.md)

---
**Sources:** yaml_examples/continuous-delivery__cd-onboarding__new-user__onboarding-path.md.yaml
(example 5, stage YAML);
docs/continuous-delivery/x-platform-cd-features/services/services-overview.md
(reuse across pipelines).
