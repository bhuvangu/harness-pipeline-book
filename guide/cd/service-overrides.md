# Service overrides

The same service usually needs different settings in different environments —
a local database in dev, a high-availability cluster in prod. Service
overrides change service settings per environment (and optionally per
infrastructure or GitOps cluster) without forking the service.

## What you can override

- **Manifests:** Values YAML, OpenShift Param, Kustomize patches, Helm Repo,
  ECS definitions, and TAS manifests.
- **Configuration files.**
- **Variables.**

Override records target combinations of environment, service,
infrastructure, and cluster. The API types them as `ENV_GLOBAL_OVERRIDE`,
`ENV_SERVICE_OVERRIDE`, `INFRA_GLOBAL_OVERRIDE`, `INFRA_SERVICE_OVERRIDE`,
`CLUSTER_GLOBAL_OVERRIDE`, and `CLUSTER_SERVICE_OVERRIDE` — from "everything
in this environment" down to "this service on this infrastructure."

## Merge behavior

The two behaviors to remember:

- **Values YAML merges by key.** At runtime, Harness merges the service's
  values file with the override's values file. Keys defined in both take the
  override's value; keys unique to either side survive. For example, an
  override with `servicePort: 80` and a service with `replicas: 2` produce a
  merged file containing both.
- **Config files and variables replace wholesale.** They cannot be partially
  overridden — the higher-priority definition completely replaces the lower.

## Limitations

- Runtime inputs are not supported for overrides in multi-service or
  multi-environment stages.
- A Helm Repo override must use the same store type as the service. If the
  service uses HTTP Helm, the override must too.

---
**Sources:** docs/continuous-delivery/x-platform-cd-features/environments/service-overrides.md
(override types, merge examples, limitations);
docs/continuous-delivery/x-platform-cd-features/overrides-v2.md;
corpus/entity_schemas.md (ServiceOverrideResponseV2 type enum);
corpus/path_tree.txt (`/ng/api/serviceOverrides`).
