# Chapter 9. Reuse: templates and versioning

Every mechanism so far reuses *values* (variables, input sets) or *entities*
(services, connectors). Templates reuse *structure*: a step, stage, or whole
pipeline defined once, versioned, and linked from many places. This chapter
is about when linking beats copying — and the operational contract that
versioning imposes.

## 9.1 What a template is

"Harness' templates allow you to design reusable content, logic, and
parameters... Instead of creating pipelines from scratch each time, Harness
lets you select from pre-built templates and link them to your pipelines"
(docs/platform/templates/template.md). Template types: Step, Step Group,
Stage, Pipeline, Deployment, Monitored Service, Secrets Manager, Artifact
Source (template.md; the API's `entity_type` enum currently lists
`Step, Stage, Pipeline, CustomDeployment, MonitoredService, SecretManager` —
a doc/spec delta logged in Appendix D#8).

A template is a scoped entity like any other — account, org, or project
(template.md, "Templates scopes") — with one extra identity dimension:

> **Identity = (identifier, version label).**
> `identifier` follows the canonical regex
> `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; each version has a `version_label`, and
> exactly one version can be flagged `stable_template`
> (corpus/entity_schemas.md: TemplateResponse, TemplateCreateRequestBody).

Templates can nest: "you can link a step template to a stage template and
link the stage template to a pipeline template" (template.md).

## 9.2 Linking: templateRef + templateInputs

A pipeline uses a template by reference, supplying only the inputs the
template declared as `<+input>`:

```yaml
- stage:
    name: deploy_service
    identifier: deploy_service
    template:
      templateRef: Golden_K8s        # scope prefixes apply: org.X, account.X
      templateInputs:                # ONLY the declared runtime inputs
        type: Deployment
        spec:
          services:
            values: <+input>
          environments:
            values: <+input>
```

(yaml_examples/continuous-delivery__cd-onboarding__new-user__cd-pipeline-modeling-overview.md.yaml)

This is Chapter 3's function model one level up: a template is a function
*definition*; `templateInputs` is its parameter list; every linked pipeline
is a call site. The platform resolves the composite YAML on demand
(`/template/api/templates/v2/applyTemplates`,
`/template/api/refresh-template/refreshed-yaml` — corpus/path_tree.txt).

## 9.3 Versioning and the stable pointer

"Versioning a template enables you to create a new template without
modifying the existing one... You can make changes to the same version of
the template, as long as the template's inputs remain unaltered. You must
create a new version of the template for any changes in the inputs"
(template.md). In other words: *the input signature is the version
boundary* — same rule that made input sets go stale in Chapter 3.5.

Consumers choose their coupling (template.md, "Stable version"):

- **Pin a version label** — maximal stability, manual upgrades.
- **Follow stable** — "when you mark a new version of the template as
  stable, it is automatically picked up to link to the pipeline."

The stable flip is a first-class API operation:
`/template/api/templates/updateStableTemplate/{templateIdentifier}/{versionLabel}`
(path_tree.txt). This gives platform teams a deployment lever: publish
v3, bake it with pinned early adopters, then move the `stable` pointer and
every stable-following pipeline upgrades at once.

With Git Experience, versions can live on different branches or repos; set
branch/repo context before switching versions (template.md, "Versioning with
Git Experience").

## 9.4 Scope rules for what a template may reference

A template can only *fix* references to resources at its own scope or higher:
"if you create an account-level stage deploy template, the service, the
environment, the infrastructure definition, the connectors, and the secrets
referenced in its steps must be defined at the account level"; and "you
cannot reference objects downwards in the hierarchy" (template.md,
"Referencing objects within a scope"). Project-level templates may reference
org and account resources — the usual upward-only visibility from Chapter 1.

The practical consequence: **account-level golden templates take
project-specific things as runtime inputs**, not fixed values. A service that
varies per project can't be fixed in the account template — but it *can*
arrive via `<+input>` at run time, chosen from any scope the runner's RBAC
allows (services-overview.md note on stage templates + runtime-input
services).

## 9.5 Template vs copy: the operational contract

Choosing linking over copying buys central change control and costs
coordination discipline. The corpus is explicit about the sharp edges
(template.md, "Important notes"):

- **Deletion cascades to references.** "When you delete an existing template
  with active pipeline references, Harness deletes the references."
- **Input-type flips don't propagate.** Converting a template input between
  runtime and fixed leaves linked pipelines stale; you reconcile manually
  (and for nested templates, may need force-reconcile).
- **Pipelines created from pipeline templates** can't add/edit/delete
  pipeline variables in the UI.
- **Chained-pipeline stages** can't live in pipeline templates.

When *should* you copy? When the consumer must diverge freely and you don't
want the upstream team's changes landing in their pipeline. When should you
template? "Share common logic without duplicating it on multiple pipelines...
Add or remove a change in one file rather than a lot of stages" (template.md,
"Why should you use templates?"). A rule of thumb consistent with the docs:
governance and golden paths → template + stable pointer; one-off variation →
copy, or a template input.

## Walkthrough: a golden deploy stage for forty teams

The pattern from the CD modeling guide's "golden pipeline"
(yaml_examples/continuous-delivery__cd-onboarding__new-user__cd-pipeline-modeling-overview.md.yaml):

1. Platform team publishes account-scope stage template `Golden_K8s`,
   version `v1`, marked stable. Inside it: the canonical step sequence
   (pre-requisite step group → K8sApply → post-deploy checks), with
   services/environments/conditions declared as `<+input>` (9.4: they vary
   per project, so they can't be fixed at account scope).
2. Each team's pipeline links `templateRef: Golden_K8s` and supplies
   `templateInputs` — nothing else. Their diff surface is arguments, not
   logic.
3. Platform team ships `v2` (adds a mandatory policy step, same inputs) —
   because the signature didn't change, they *could* amend `v1`; they cut
   `v2` anyway for auditability, bake it with one pinned team, then
   `updateStableTemplate` to move everyone (9.3).
4. `v3` adds a new required input — a signature change, so a new version is
   mandatory (9.3), and every consuming pipeline must be reconciled to
   supply the new input before it runs cleanly (9.5).

> ### Mental model
>
> A template is a versioned function published at a scope: `templateRef` is
> the call, `templateInputs` the arguments, and the input signature defines
> where one version ends and the next begins. The `stable` label is a
> movable pointer — platform teams deploy standards by moving it, consumers
> choose between pinning (stability) and following (freshness). Linking
> means the upstream team can change your pipeline; that's the feature, and
> the reconciliation duties are the price.

### Check your understanding

1. Why does adding a new `<+input>` to a template force a new version, while
   editing a step's command doesn't? *(§9.3: the input signature is the
   version boundary — callers break otherwise.)*
2. An account-level stage template needs a Git connector for manifests.
   What are your two compliant options? *(§9.4: an account-scope connector
   fixed in the template, or a `<+input>` connector supplied per run.)*
3. What happens to forty pipelines when the platform team deletes the
   template they link? *(§9.5: the references are deleted with it —
   coordinate or deprecate instead.)*
4. Your team wants yesterday's behavior forever; the platform team keeps
   improving the template. Reconcile both. *(§9.3: pin the version label;
   the platform team moves `stable` for everyone else.)*
