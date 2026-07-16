# Connectors

A connector packages the endpoint and credentials for one external system:
a Git provider, a cloud platform, a Kubernetes cluster, an artifact
registry, or a ticketing or monitoring system. Pipelines, services,
infrastructure definitions, triggers, and codebases all reference connectors
by identifier in `connectorRef` fields.

```yaml
connector:
  name: my-cluster
  identifier: my_cluster
  orgIdentifier: default
  projectIdentifier: default
  type: K8sCluster        # the type determines the spec shape
  spec:
    credential: ...
```

Connectors exist at account, organization, or project scope. References
from lower scopes use the standard prefixes: `connectorRef: account.gcp`,
`connectorRef: org.bitnami`. An account-scope connector is how you share
credentials with every project — but remember that account-scope entities
can only use account-scope connectors. For more information, see
[Scopes](../concepts/scopes.md).

Connector operations execute through delegates, which is why a connector's
reachability depends on delegate placement. Both API generations provide a
test-connection operation to verify a connector
(`/v1/.../connectors/{connector}/test-connection`,
`/ng/api/connectors/testConnection/{identifier}`).

The connector's credential fields reference secrets rather than embedding
values. For more information, see
[Secrets and secret managers](secrets.md).

---
**Sources:** docs/platform/connectors/create-a-connector-using-yaml.md;
yaml_examples/platform__pipelines__harness-yaml-quickstart.md.yaml
(example 23); corpus/entity_schemas.md (Connector identity patterns);
corpus/path_tree.txt (CRUD and test-connection endpoints);
docs/platform/delegates/delegate-concepts/delegate-overview.md
("Connectors are used for all third-party connections");
docs/continuous-delivery/x-platform-cd-features/services/services-overview.md
(scope prefix examples, account-scope restriction).
