# Reusing configuration with templates

A template is a versioned, reusable definition of a step, stage, or whole
pipeline (plus step group, deployment, monitored service, secret manager,
and artifact source types). Pipelines link to templates instead of copying
their content, so a change to the template can update every pipeline that
uses it.

Templates exist at account, organization, or project scope. Templates can
nest: a step template inside a stage template inside a pipeline template.

## Linking a template

A pipeline uses a template with `templateRef`, supplying values for only the
inputs the template declared:

```yaml
- stage:
    name: deploy_service
    identifier: deploy_service
    template:
      templateRef: Golden_K8s        # org.X / account.X prefixes apply
      templateInputs:
        type: Deployment
        spec:
          services:
            values: <+input>
          environments:
            values: <+input>
```

## Versions and the stable version

A template's identity is its identifier plus a version label. You can amend
an existing version as long as its inputs don't change; any change to the
inputs requires a new version.

Pipelines link to a template in one of two ways:

- **Pin a version label.** Maximum stability; you upgrade manually.
- **Follow the stable version.** When you mark a new version as stable, it
  is automatically picked up by every pipeline linked to stable.

This gives platform teams a rollout lever: publish a new version, validate
it with a pinned early adopter, then move the stable marker to upgrade
everyone at once.

## Scope rules

A template can fix references only to resources at its own scope or higher.
An account-level stage template can fix only account-level services,
environments, connectors, and secrets. Anything that varies per project
should be a runtime input in the template instead — the caller supplies it
at run time from whatever scope their permissions allow.

## Operational contract

Linking means the template's owners can change your pipelines. Plan for the
sharp edges:

- Deleting a template that has active references deletes those references.
- Converting a template input between fixed and runtime does not propagate;
  you must reconcile linked pipelines manually (force-reconcile for nested
  templates).
- Pipelines created from a pipeline template can't add, edit, or delete
  pipeline variables in the UI.
- Pipeline templates don't support chained pipeline stages.

Use a template when many pipelines should share logic and evolve together.
Copy instead when a consumer must diverge freely.

---
**Sources:** docs/platform/templates/template.md (types, versioning, stable
version, scope rules, important notes);
corpus/entity_schemas.md (TemplateResponse entity_type enum, version_label,
stable_template);
yaml_examples/continuous-delivery__cd-onboarding__new-user__cd-pipeline-modeling-overview.md.yaml
(templateRef usage); corpus/path_tree.txt
(`/template/api/templates/updateStableTemplate/...`);
docs/continuous-delivery/x-platform-cd-features/services/services-overview.md
(runtime-input services across scopes).
