# Services

A service represents what you're deploying — a microservice or another
workload. Each service contains a service definition that specifies its
manifests, artifacts, configuration files, and service-specific variables.

You can create services at account, organization, or project scope, and
inside or outside a pipeline. A service created in a pipeline is added to
the Services list automatically, and you can reference the same service from
any number of pipelines.

## Service definition

For a Kubernetes service, the definition has two main parts:

```yaml
service:
  name: nginx
  identifier: nginx
  serviceDefinition:
    type: Kubernetes
    spec:
      manifests:                    # where the manifests live
        - manifest:
            identifier: nginx-base
            type: K8sManifest
            spec:
              store:
                type: Github
                spec:
                  connectorRef: account.Harness_K8sManifest
                  paths: [cdng/]
                  branch: main
      artifacts:                    # what image to deploy
        primary:
          primaryArtifactRef: <+input>
          sources:
            - identifier: harness dockerhub
              type: DockerRegistry
              spec:
                connectorRef: account.Harness_DockerHub
                imagePath: library/nginx
                tag: <+input>       # version chosen per run or by a trigger
```

Setting the artifact `tag` to `<+input>` is the standard pattern: the
version to deploy arrives at run time, from the Run form, an input set, or
an artifact trigger.

## Scope rules

An account-level service can only reference account-level connectors for its
manifests and artifacts. Account-level services are global and cannot depend
on resources at a lower scope. Similarly, an account-level stage template
can reference only account-level services; when a stage takes its service as
a runtime input, you can pass a service from any scope your permissions
allow.

---
**Sources:** docs/continuous-delivery/x-platform-cd-features/services/services-overview.md
(definition, scopes, YAML sample, scope restrictions);
docs/continuous-delivery/x-platform-cd-features/services/create-services.md;
corpus/entity_schemas.md (ServiceRequest); corpus/path_tree.txt
(`/ng/api/servicesV2`, `/v1/.../services`).
