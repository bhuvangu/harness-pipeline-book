# Environments and infrastructure definitions

An environment represents where you deploy — a logical target such as dev,
QA, or prod, categorized as `PreProduction` or `Production`. The physical
targets are the environment's infrastructure definitions: each one names a
specific cluster and namespace, VM group, or other target. An environment
can contain many infrastructure definitions; when a pipeline selects an
environment, it also picks which infrastructure definition to use.

For example, a `prod` environment might contain five infrastructure
definitions for the five Kubernetes clusters that make up production.

## Environment YAML

```yaml
environment:
  name: dev
  identifier: dev
  type: PreProduction        # PreProduction | Production
  variables:                 # environment-wide variables
    - name: port
      type: String
      value: "8080"
    - name: namespace
      type: String
      value: <+service.name>-dev
```

Environment variables are available to the pipelines, manifests, and steps
that deploy into the environment.

## Infrastructure definition YAML

```yaml
infrastructureDefinition:
  name: dev-k8s
  identifier: dev
  environmentRef: dev              # the owning environment
  deploymentType: Kubernetes
  type: KubernetesDirect
  spec:
    connectorRef: account.Harness_Kubernetes_Cluster
    namespace: <+service.name>-dev
    releaseName: release-<+INFRA_KEY_SHORT_ID>
  allowSimultaneousDeployments: false
```

`allowSimultaneousDeployments` controls whether multiple deployments can run
into this infrastructure at the same time. Infrastructure types include
KubernetesDirect, KubernetesGcp, KubernetesAzure, Pdc, SshWinRmAws,
SshWinRmAzure, ServerlessAwsLambda, AzureWebApp, AzureFunction, ECS,
Elastigroup, and CustomDeployment.

You can also scope an infrastructure definition to specific services, so
only those services can deploy into it.

## Environment groups

An environment group is a named collection of environments for bulk
selection. Members can come from any scope, using the standard prefixes:

```yaml
environmentGroup:
  name: demoEnvGroup
  identifier: demoEnvGroup
  orgIdentifier: default
  projectIdentifier: CD_Docs
  envIdentifiers:
    - test                              # project scope
    - org.testE                         # organization scope
    - account.CDCNGAuto_EnvNg59wFkWCjQQ # account scope
```

## Scopes

Like services, environments and their infrastructure definitions can be
created at account, organization, or project scope. When you create one at
account scope, omit the `orgIdentifier` and `projectIdentifier` fields.

---
**Sources:** docs/continuous-delivery/x-platform-cd-features/environments/environment-overview.md
(definitions, YAML samples, multiple infra definitions, API note);
corpus/entity_schemas.md (EnvironmentRequest type enum,
InfrastructureRequest type enum); corpus/path_tree.txt
(`/v1/environments/{environment}/infrastructures/...` nesting);
docs/continuous-delivery/x-platform-cd-features/environments/scope-infra-to-services.md;
docs/continuous-delivery/x-platform-cd-features/environments/create-environment-groups.md.
