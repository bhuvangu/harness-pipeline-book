# The two API generations

Harness exposes the same entities through two REST surfaces. Treat them as
two views of one domain: a pipeline created through one generation is the
same entity when listed through the other.

| | v1 beta | Legacy NextGen |
|---|---|---|
| Shape | Resource-oriented; scope in the path | RPC-style; scope in query parameters |
| Example | `/v1/orgs/{org}/projects/{project}/pipelines/{pipeline}` | `/pipeline/api/pipelines/{pipelineIdentifier}?accountIdentifier=...` |
| Naming | kebab-case (`input-sets`) | camelCase (`inputSets`) |

In the corpus, v1 covers pipelines, input sets, executions, services,
environments and their infrastructure definitions, connectors, secrets, and
approvals. Triggers, templates, freeze windows, delegates, environment
groups, and service overrides appear only on the legacy surface
(`/pipeline/api`, `/template/api`, `/ng/api`). Uneven v1 coverage is a
migration in progress, not an entity boundary.

## URL nesting as ownership evidence

In the v1 generation, path nesting mirrors ownership. For example,
`/v1/environments/{environment}/infrastructures/{infrastructure-definition}`
shows that an infrastructure definition belongs to an environment. The
[Relationship diagrams](../reference/relationships.md) reference uses this
technique, together with documentation statements, to justify every edge in
the entity model.

---
**Sources:** corpus/path_tree.txt (all paths and coverage);
corpus/openapi_pipeline.yaml (spec of record);
docs/continuous-delivery/x-platform-cd-features/environments/environment-overview.md
(environment owns infrastructure definitions).
