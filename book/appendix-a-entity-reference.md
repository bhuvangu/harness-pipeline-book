# Appendix A. Entity reference

This appendix is the precise backing for the narrative chapters, in the spirit
of an AWS API Reference behind a User Guide. Each entity section follows the
same template:

- **Definition** — what it is, in one or two sentences.
- **Scopes** — where the entity can live (Account / Org / Project).
- **Identity** — identifier vs. name, uniqueness scope, regex quoted verbatim
  from `corpus/entity_schemas.md`.
- **Owns / Owned by** — composition edges, with URL-nesting and doc evidence.
- **References** — association edges (things it points at but does not own).
- **YAML** — a minimal annotated example, cited.
- **API surface** — both generations where present: v1 beta
  (`/v1/orgs/{org}/...`) and legacy NextGen (`/ng/api/...`,
  `/pipeline/api/...`, `/template/api/...`). One entity, two views; paths from
  `corpus/path_tree.txt` / `corpus/openapi_pipeline.yaml`.
- **Lifecycle** — states, where evidenced.
- **Gotchas** — sharp edges a new engineer should know.

Claims marked **INFERRED** are the author's inference from structure, not a
direct doc/spec statement.

Shared identity rules (quoted from `entity_schemas.md` unless noted):

- The canonical **identifier** regex, used by Pipeline, Input Set, Template,
  Connector: `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$` (max length 128). Identifiers
  are immutable after creation (docs/platform/pipelines/add-a-stage.md:
  "once the stage is saved, the **Id** becomes immutable").
- The canonical **name** regex: `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`. Names are
  mutable ("You can change the **Name** at any time, but you can't change the
  **Id**", same doc).
- Uniqueness is per scope container: an identifier must be unique within the
  account/org/project it lives in; the same identifier can exist at different
  scopes, which is why cross-scope references need `org.` / `account.`
  prefixes (see Chapter 1). **INFERRED** from the reference-prefix design in
  docs/continuous-delivery/x-platform-cd-features/environments/create-environment-groups.md.

---

## A.1 Account

- **Definition.** The root scope of everything in Harness. Every resource
  belongs to exactly one account; account-scope resources are shared downward.
- **Scopes.** Is the top of the scope hierarchy; not itself scoped.
- **Identity.** `accountIdentifier` / `accountId` appears as a field on nearly
  every response schema (e.g. `entity_schemas.md`: `FreezeResponse.accountId`
  required; `ConnectorInfoDTO.accountIdentifier`).
- **Owns.** Organizations, and account-scope instances of Connector, Secret,
  Template, Variable, Service, Environment, Delegate, Freeze
  (evidence per entity below).
- **References.** —
- **API surface.** The account is addressed via query/path params rather than
  a CRUD resource in this corpus: `/ng/api/accounts/{accountIdentifier}/immutable-delegate-enabled`
  (path_tree.txt); every `/ng/api/...` list call takes `accountIdentifier`.
- **Gotchas.** Account-scope resources are referenced from lower scopes with
  the `account.` prefix, e.g. `connectorRef: account.Harness_DockerHub`
  (docs/continuous-delivery/x-platform-cd-features/services/services-overview.md YAML).

## A.2 Organization

- **Definition.** A grouping scope under Account, typically a business unit
  or product line; owns Projects and org-scope shared resources.
- **Scopes.** Child of Account.
- **Identity.** Referenced as `orgIdentifier` (legacy NG APIs) or `org` (v1
  APIs). On the v1 `Connector` schema, `org` has pattern
  `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$` (`entity_schemas.md`: Connector).
- **Owns.** Projects (`/v1/orgs/{org}/projects/{project}/...`, path_tree.txt);
  org-scope Connectors (`/v1/orgs/{org}/connectors`), Environments
  (`/v1/orgs/{org}/environments`), Templates, GitX webhooks
  (`/v1/orgs/{org}/gitx-webhooks`).
- **References.** —
- **API surface.** v1: `/v1/orgs/{org}` subtree (path_tree.txt). Legacy NG org
  CRUD is outside the filtered corpus; org identity appears as the
  `orgIdentifier` parameter on virtually every `/ng/api/...` call.
- **Gotchas.** Org-scope resources are referenced from projects with the
  `org.` prefix, e.g. `connectorRef: org.bitnami`
  (docs/continuous-delivery/x-platform-cd-features/services/services-overview.md).

## A.3 Project

- **Definition.** The working scope where day-to-day pipeline work happens.
  Pipelines, Input Sets, and Triggers exist only at project scope in this
  corpus; most other resources can also live here.
- **Scopes.** Child of Organization.
- **Identity.** `projectIdentifier` (legacy NG) / `project` (v1; pattern
  `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$` on the v1 Connector schema,
  `entity_schemas.md`).
- **Owns.** Pipelines, Input Sets, Triggers, and project-scope Services,
  Environments, Connectors, Secrets, Templates, Variables, Delegates,
  Freezes. Evidence: the `/v1/orgs/{org}/projects/{project}/...` subtree
  (pipelines, input-sets, secrets, connectors, environments, approvals —
  path_tree.txt).
- **References.** —
- **API surface.** v1: `/v1/orgs/{org}/projects/{project}` subtree.
- **Gotchas.** Pipelines have *only* project-level endpoints in both API
  generations (`/v1/orgs/{org}/projects/{project}/pipelines`,
  `/pipeline/api/pipelines?...projectIdentifier=`) — unlike Services and
  Environments, there is no account/org-level pipeline. **INFERRED** from
  the absence of such paths in path_tree.txt.

## A.4 Pipeline

- **Definition.** The YAML-defined workflow entity; the aggregate root of
  Pipeline > Stage > Step. "Harness pipeline YAML lets you model your release
  process declaratively" (docs/platform/pipelines/harness-yaml-quickstart.md).
- **Scopes.** Project only (see A.3 gotcha).
- **Identity.** `identifier` pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`,
  maxLen 128; `name` pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; both required
  along with `pipeline_yaml` (`entity_schemas.md`: PipelineCreateRequestBody).
  Unique within its project. **INFERRED** (uniqueness) from identifier-based
  addressing `/pipelines/{pipeline}`.
- **Owns.** Stages (inline YAML children — `pipeline.stages[]`,
  harness-yaml-quickstart.md "Basic pipeline structure"); its Executions
  (`/v1/.../pipelines/{pipeline}/executions/{execution}/artifacts`); its Input
  Sets (InputSetResponse has `pipelineIdentifier`, `entity_schemas.md`); its
  Triggers (`NGTriggerResponse.targetIdentifier` is the pipeline;
  trigger YAML nests `pipelineIdentifier`, yaml_examples/platform__pipelines__harness-yaml-quickstart.md.yaml example 18).
- **References.** Codebase connector (`properties.ci.codebase.connectorRef`,
  docs/continuous-integration/use-ci/codebase-configuration/create-and-configure-a-codebase.md);
  Templates via `template.templateRef` at stage/step level; Git repo when
  stored remotely (`git_details`, PipelineCreateRequestBody).
- **YAML.** Minimal skeleton (docs/platform/pipelines/harness-yaml-quickstart.md):

  ```yaml
  pipeline:
    name: YAML Example        # mutable display name
    identifier: YAML_Example  # immutable, unique in project
    projectIdentifier: default
    orgIdentifier: default
    tags: {}
    stages:
      - stage: ...            # owned children, see A.5
    variables: []             # pipeline-scope variables, see A.31
  ```

- **API surface.**

  | Operation | v1 beta | legacy NG |
  |---|---|---|
  | CRUD | `/v1/orgs/{org}/projects/{project}/pipelines[/{pipeline}]` | `/pipeline/api/pipelines[/{pipelineIdentifier}]`, `/pipeline/api/pipelines/v2` |
  | Run | `.../pipelines/{pipeline}/execute` (+ `/stages`, `/rerun/{execution-id}`, `/retry/{execution-id}`) | `/pipeline/api/pipeline/execute/...` (execution subtree, A.8) |
  | Inputs schema | `.../pipelines/{pipeline}/inputs` | `/pipeline/api/inputSets/template` |
  | Import from Git | `.../pipelines/{pipeline}/import` | `/pipeline/api/pipelines/import/{pipelineIdentifier}` |
  | Validate | `.../pipelines/validate/{uuid}` | — |

  (all from path_tree.txt)

- **Lifecycle.** Stored inline or in Git: `storeType` enum `INLINE, REMOTE,
  INLINE_HC` (`entity_schemas.md`: PipelineExecutionSummary). No draft/publish
  states in evidence.
- **Gotchas.** A minimum configuration is required before the pipeline can
  even be saved (harness-yaml-quickstart.md). Git-stored ("remote") pipelines
  are still Harness entities — Git is a storage backend selected per entity,
  not a different entity type.

## A.5 Stage

- **Definition.** "A stage is a part of a pipeline that contains the logic to
  perform a major segment of a larger workflow" (docs/platform/pipelines/add-a-stage.md).
  The stage type determines its settings and step catalog.
- **Scopes.** Not independently scoped — exists only inside a Pipeline (or a
  Stage Template).
- **Identity.** `identifier` unique within the pipeline; auto-generated from
  the name and **immutable once saved**; name mutable (add-a-stage.md,
  "Stage names").
- **Owned by.** Pipeline (`pipeline.stages[]` YAML nesting,
  harness-yaml-quickstart.md).
- **Owns.** Steps and step groups (`spec.execution.steps[]`); stage
  variables; per-type components: CI stages own codebase-clone behavior,
  infrastructure/runtime and caching config
  (yaml_examples/continuous-integration__use-ci__caching-ci-data__cache-intelligence.md.yaml
  example 2); Deployment stages own service/environment bindings.
- **References.** Delegate selectors; Templates (`template.templateRef` in a
  stage — yaml_examples/continuous-delivery__cd-onboarding__new-user__cd-pipeline-modeling-overview.md.yaml
  example 1); for CD: Service, Environment, Infrastructure Definition.
- **Stage types.** Build (CI), Deploy (CD), Approval, Feature Flag, Security
  Tests, Pipeline (chained pipeline), Custom, Dynamic
  (docs/platform/pipelines/add-a-stage.md).
- **YAML.** (harness-yaml-quickstart.md "Basic stage structure")

  ```yaml
  - stage:
      identifier: deploy_service  # immutable once saved
      name: deploy service
      type: Deployment            # determines spec shape and step catalog
      spec:
        execution:
          steps: [...]
      variables: [...]
      when: ...                   # conditional execution
      failureStrategies: [...]
  ```

- **API surface.** No standalone stage CRUD; stages travel inside pipeline
  YAML. Execution-side views exist: selective stage execution
  (`/v1/.../pipelines/{pipeline}/execute/stages`,
  `.../execute/stages-execution-list`; schema `StageExecutionResponseBody`).
- **Gotchas.** Stage variables are visible pipeline-wide: reference in-stage
  as `<+stage.variables.NAME>`, from other stages as
  `<+pipeline.stages.STAGE_ID.variables.NAME>` (add-a-stage.md). Stage
  variable YAML documents `type: String ## String or Secret`
  (add-a-stage.md) — contrast with the account/org/project Variable entity,
  whose API enum is `String` only (A.31, Appendix D#7).

## A.6 Step

- **Definition.** The atomic unit of work inside a stage; typed, with the
  catalog determined by the stage type (Run, ShellScript, HarnessApproval,
  K8sApply, Plugin, and so on).
- **Scopes.** Inside a stage (or a Step Template).
- **Identity.** `identifier` + `name` per step, unique within the stage.
  **INFERRED** (uniqueness scope) from expression addressing
  `<+pipeline.stages.STAGE_ID...>`.
- **Owned by.** Stage (`spec.execution.steps[]`), optionally via a Step Group.
- **References.** Connectors (`spec.connectorRef` on Run/Plugin/cache steps —
  yaml_examples/continuous-integration__use-ci__caching-ci-data__save-cache-in-gcs.md.yaml),
  Secrets via expressions (`<+secrets.getValue("secretfile")>`,
  yaml_examples/platform__secrets__add-use-text-secrets.md.yaml), Templates,
  Delegate selectors (docs/platform/delegates/delegate-concepts/delegate-overview.md,
  "You can select a delegate in each pipeline step").
- **YAML.** (yaml_examples/platform__secrets__add-use-text-secrets.md.yaml)

  ```yaml
  - step:
      type: Run                 # step type from the stage's catalog
      name: Run_1
      identifier: Run_1
      spec:
        shell: Sh
        command: |
          echo $SECRET | base64 --decode > decoded.txt
        envVariables:
          SECRET: <+secrets.getValue("secretfile")>  # secret reference
  ```

- **API surface.** None standalone; steps exist inside pipeline/template YAML
  and as nodes in the execution graph (`ExecutionGraph.nodeMap`,
  `entity_schemas.md`).
- **Gotchas.** Every step has a `timeout` and can carry its own failure
  strategy and conditional execution
  (docs/platform/pipelines/failure-handling/define-a-failure-strategy-on-stages-and-steps.md).

## A.7 Step Group

- **Definition.** A named grouping of steps inside a stage that shares
  settings; in CD it can be containerized so its steps run in a shared
  container environment
  (docs/continuous-delivery/x-platform-cd-features/cd-steps/containerized-steps/containerized-step-groups.md).
- **Scopes.** Inside a stage; also available as a Template type
  (docs/platform/templates/create-a-stepgroup-template.md).
- **Identity.** `identifier` within the stage.
- **Owned by.** Stage. **Owns.** Steps.
- **YAML.** (yaml_examples/continuous-delivery__cd-infrastructure__aws-cdk__cdk-image-build.md.yaml, example 1)

  ```yaml
  stepGroup:
    privileged: true
    name: k8s-step-group
    sharedPaths:        # settings shared by all member steps
      - /var/run
      - /var/lib/docker
  ```

- **API surface.** None standalone (YAML-embedded).
- **Gotchas.** Step groups can nest `parallel:` blocks of steps
  (yaml_examples/continuous-delivery__cd-onboarding__new-user__cd-pipeline-modeling-overview.md.yaml).

## A.8 Execution

- **Definition.** One run of a pipeline: a plan (`planExecutionId`), a node
  graph, per-node statuses, and summary metadata. The runtime counterpart of
  the Pipeline entity.
- **Scopes.** Project (lives under its pipeline). `PipelineExecutionSummary`
  requires `orgIdentifier`, `projectIdentifier` (`entity_schemas.md`).
- **Identity.** `planExecutionId` (system-generated); plus a human
  `runSequence` counter (PipelineExecutionSummary).
- **Owned by.** Pipeline
  (`/v1/.../pipelines/{pipeline}/executions/{execution}/artifacts`,
  path_tree.txt). **Owns.** Its execution graph nodes
  (`ExecutionGraph.rootNodeId`, `nodeMap`, `nodeAdjacencyListMap` —
  `entity_schemas.md`) and execution-scoped notes/annotations
  (`/pipeline/api/pipelines/execution/{planExecutionId}/notes`).
- **References.** The trigger or user that started it
  (`executionTriggerInfo`), the input set values used
  (`/pipeline/api/pipelines/execution/{planExecutionId}/inputsetV2`), Git
  details for remote pipelines (`gitDetails`, `storeType`).
- **Statuses.** Quoted from `entity_schemas.md` (PipelineExecutionSummary
  `status` enum): `Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed,
  Errored, IgnoreFailed, NotStarted, Expired, Aborted, Discontinuing, Queued`.
- **API surface.**

  | Operation | v1 beta | legacy NG |
  |---|---|---|
  | Start | `.../pipelines/{pipeline}/execute` | (execution created via pipeline run APIs) |
  | Rerun / retry | `.../execute/rerun/{execution-id}`, `.../execute/retry/{execution-id}` | `/pipeline/api/pipelines/execution/canRetry/{planExecutionId}` |
  | Detail | — | `/pipeline/api/pipelines/execution/v2/{planExecutionId}` |
  | Graph | — | `.../execution/getExecutionGraph/{planExecutionId}`, `.../subGraph/{planExecutionId}/{nodeExecutionId}` |
  | List/summary | — | `.../execution/summary`, `.../execution/summary/outline` |
  | Queue management | — | `/pipeline/api/pipelines/queue-management/queued-pipelines`, `.../bulk-abort` |

  (path_tree.txt)

- **Lifecycle.** Queued → Running → terminal (Success is displayed in
  execution history; the summary enum above captures waiting/terminal
  states). Executions can be queued by resource constraints, concurrency
  limits, or pipeline locks; aborting a queued execution removes it
  permanently ("There is no way to resume it")
  (docs/platform/pipelines/executions-and-logs/executions-management.md).
- **Gotchas.** `canRetry` / `canReExecute` are explicit response fields —
  retry (resume from failed stage) and rerun (fresh run) are different
  operations with different v1 endpoints. Executions aborted by a freeze
  window get the distinct status label "Aborted By Freeze"
  (docs/continuous-delivery/manage-deployments/deployment-freeze.md).

## A.9 Input Set

- **Definition.** "Input sets are collections of runtime input values for a
  pipeline" — saved arguments for the pipeline-as-function
  (docs/platform/pipelines/input-sets.md).
- **Scopes.** Project, always bound to one pipeline
  (`InputSetResponse.pipelineIdentifier`, `entity_schemas.md`).
- **Identity.** `identifier` pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`,
  maxLen 128; `name` pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; required with
  `input_set_yaml` (`entity_schemas.md`: InputSetCreateRequestBody).
- **Owned by.** Pipeline (nested `pipeline.identifier` in its YAML;
  input-set endpoints require `pipelineIdentifier`).
- **References.** Git repo when remote (`git_details`).
- **YAML.** (yaml_examples/platform__pipelines__harness-yaml-quickstart.md.yaml, example 20)

  ```yaml
  inputSet:
    name: My Input Set 1
    identifier: My_Input_Set
    orgIdentifier: default
    projectIdentifier: CD_Examples
    pipeline:                      # mirrors the target pipeline's shape,
      identifier: YAML             # containing ONLY the <+input> fields
      stages:
        - stage:
            identifier: Deploy
            type: Deployment
            spec:
              infrastructure:
                infrastructureDefinition:
                  type: KubernetesDirect
                  spec:
                    connectorRef: Kubernetes_Quickstart
                    namespace: default
  ```

- **API surface.**

  | Operation | v1 beta | legacy NG |
  |---|---|---|
  | CRUD | `/v1/orgs/{org}/projects/{project}/input-sets[/{input-set}]` | `/pipeline/api/inputSets[/{inputSetIdentifier}]` |
  | Merge | `.../input-sets/merge` | `/pipeline/api/inputSets/merge` |
  | Runtime-input template | — | `/pipeline/api/inputSets/template` |
  | Import / Git | `.../input-sets/{input-set}/import`, `/git-metadata`, `/move-config` | `.../{inputSetIdentifier}/update-git-metadata` |

  (path_tree.txt)

- **Lifecycle.** `isOutdated` flags an input set whose pipeline has changed
  underneath it (`entity_schemas.md`: InputSetResponse).
- **Gotchas.** Only settings whose pipeline value is `<+input>` can appear in
  an input set (input-sets.md). If the pipeline's runtime inputs change, the
  input set can silently go stale — hence `isOutdated`. With triggers you can
  use an input set *or* inline runtime values, not both (input-sets.md).

## A.10 Overlay Input Set

- **Definition.** An ordered composition of input sets: "Overlays are groups
  of input sets, which enable you to pull runtime inputs from multiple input
  sets" (docs/platform/pipelines/input-sets.md).
- **Scopes.** Project, bound to one pipeline.
- **Identity.** Same identifier rules as Input Set; the API distinguishes the
  two by `inputSetType` enum `INPUT_SET, OVERLAY_INPUT_SET`
  (`entity_schemas.md`).
- **Owned by.** Pipeline. **References.** Its member Input Sets, by
  identifier, in priority order.
- **YAML.** (yaml_examples/platform__pipelines__harness-yaml-quickstart.md.yaml, example 22)

  ```yaml
  overlayInputSet:
    name: My Overlay Set
    identifier: My_Overlay_Set
    orgIdentifier: default
    projectIdentifier: CD_Examples
    pipelineIdentifier: YAML
    inputSetReferences:   # resolved in order; later sets win
      - My_Input_Set
      - My_Input_Set_2
  ```

- **API surface.** legacy NG: `/pipeline/api/inputSets/overlay[/{inputSetIdentifier}]`
  (path_tree.txt). No overlay-specific v1 path appears in the corpus
  (Appendix D#9).
- **Gotchas.** "The setting's final value is the value assigned in the last
  input set to be resolved" (input-sets.md, "Priority in overlays") — last
  writer wins, and later sets also fill fields earlier sets left empty.

## A.11 Trigger

- **Definition.** A rule attached to a pipeline that starts an execution when
  an event occurs — a Git webhook event, a schedule, or a new artifact/
  manifest version. Type enum: `Webhook, Artifact, Manifest, Scheduled,
  MultiRegionArtifact, SystemEvent` (`entity_schemas.md`: NGTriggerResponse).
- **Scopes.** Project, bound to one pipeline
  (`NGTriggerResponse.targetIdentifier`).
- **Identity.** `identifier` + `name`; unique per pipeline. **INFERRED**
  (uniqueness) from `/pipeline/api/triggers/{triggerIdentifier}` addressing
  plus required `targetIdentifier` query context.
- **Owned by.** Pipeline (trigger YAML carries `pipelineIdentifier`;
  yaml_examples/platform__pipelines__harness-yaml-quickstart.md.yaml example 18).
- **References.** Code-repo Connector (webhook triggers require one for all
  Git providers except Custom and Harness Code —
  docs/platform/triggers/triggering-pipelines.md); an Input Set or inline
  runtime values; artifact-source connectors for Artifact triggers
  (`connector_ref` on `AcrArtifactTriggerSpec`, `entity_schemas.md`).
- **YAML.** Webhook (custom) skeleton
  (yaml_examples/platform__pipelines__harness-yaml-quickstart.md.yaml, example 18)
  and a cron source
  (yaml_examples/platform__triggers__schedule-pipelines-using-cron-triggers.md.yaml):

  ```yaml
  trigger:
    name: nightly
    identifier: nightly
    enabled: true
    orgIdentifier: default
    projectIdentifier: default
    pipelineIdentifier: my_pipe   # the owning pipeline
    source:
      type: Scheduled
      spec:
        type: Cron
        spec:
          expression: 0/5 * * * *
          type: UNIX
          timezone: America/New_York
  ```

- **API surface.** legacy NG: `/pipeline/api/triggers`,
  `.../triggers/{triggerIdentifier}[/details|/eventHistory]`,
  `.../triggers/catalog`, `.../eventHistory/...` (path_tree.txt). No v1
  trigger CRUD path in the corpus (Appendix D#9).
- **Lifecycle.** `enabled` flag; webhook `registrationStatus` enum
  `SUCCESS, FAILED, ERROR, TIMEOUT, UNAVAILABLE`
  (`entity_schemas.md`: NGTriggerDetailsResponseDTO).
- **Gotchas.** All triggers in an account share one webhook URL
  (`.../webhook?accountIdentifier=...`), so conditions must be written to
  select only your events (triggering-pipelines.md). Conditions are
  `AND`-ed; use a JEXL condition for `OR` logic (same doc). During a freeze,
  trigger invocations of frozen pipelines are rejected
  (deployment-freeze.md). If the pipeline's runtime inputs change, update the
  trigger's inputs or executions fail (`isPipelineInputOutdated` field;
  triggering-pipelines.md).

## A.12 Webhook

- **Definition.** The HTTP-facing half of event-driven triggering: the
  registered endpoint in Harness plus the webhook definition in the Git
  provider. Distinct from the Trigger, which holds the matching rules and
  pipeline binding.
- **Scopes.** Webhook registrations exist per Git provider repo; GitX
  webhooks exist at account/org/project (`/v1/gitx-webhooks`,
  `/v1/orgs/{org}/gitx-webhooks`,
  `/v1/orgs/{org}/projects/{project}/gitx-webhooks` — path_tree.txt).
- **Identity.** Per-provider spec schemas: `GithubWebhookTriggerSpec`
  (`repo_name`, `connector_ref`, event enum `PullRequest, Push, IssueComment,
  Release`), plus Gitlab/Bitbucket/AzureRepo/AwsCodeCommit/Custom/Harness
  variants (`entity_schemas.md`).
- **Owned by.** Conceptually the account (shared URL); Git-provider webhooks
  belong to the repo. **References.** Connector for registration.
- **API surface.** legacy NG: `/pipeline/api/webhook/custom[/v2]`,
  `/pipeline/api/webhook/custom/{webhookToken}/v3`, `/ng/api/webhook`;
  v1: gitx-webhook subtree (path_tree.txt).
- **Gotchas.** Harness auto-registers webhooks in supported providers; if
  auto-registration fails or the trigger is Custom, you copy the URL and
  register it manually (triggering-pipelines.md).

## A.13 Approval

- **Definition.** A gate that pauses execution for a human or ticket-system
  verdict. Runs as an Approval *step* (inside CD stages or Approval stages);
  each pending gate is an Approval Instance. Types: `HarnessApproval,
  JiraApproval, CustomApproval, ServiceNowApproval`
  (`entity_schemas.md`: ApprovalInstanceResponse).
- **Scopes.** Lives inside pipeline YAML; instances live under executions.
- **Identity.** Approval instance `id` (system-generated), required with
  `type`, `status`, `details` (ApprovalInstanceResponse).
- **Owned by.** Execution (instances); Stage (the step definition).
- **References.** Harness User Groups as approvers
  (`approvers.userGroups`), approver inputs.
- **Statuses.** `WAITING, APPROVED, REJECTED, FAILED, ABORTED, EXPIRED`
  (ApprovalInstanceResponse); per-activity actions `APPROVE, REJECT`
  (`entity_schemas.md`: HarnessApprovalActivity).
- **YAML.** (docs/continuous-delivery/x-platform-cd-features/cd-steps/approvals/using-harness-approval-steps-in-cd-stages.md)

  ```yaml
  - step:
      type: HarnessApproval
      name: Harness Approval Step
      identifier: Harness_Approval_Step
      timeout: 1d                     # EXPIRED when exceeded
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

- **API surface.** v1: `/v1/orgs/{org}/projects/{project}/approvals/execution/{execution-id}`;
  legacy NG: `/pipeline/api/approvals/{approvalInstanceId}/harness/activity`
  (path_tree.txt).
- **Gotchas.** Approvers can set variables consumed by later steps
  (using-harness-approval-steps-in-cd-stages.md). The `Approval` schema under
  `/gateway/lw/...` in the schema digest is Cloud Cost autostopping, not
  pipeline approvals — a keyword-filter false friend (Appendix D#4).

## A.14 Deployment Freeze

- **Definition.** A time-windowed rule that blocks CD deployments for chosen
  orgs/projects/services/environments: "A freeze window is defined using one
  or more rules and a schedule"
  (docs/continuous-delivery/manage-deployments/deployment-freeze.md).
- **Scopes.** Account, Org, or Project (`freezeScope` enum
  `account, org, project, unknown` — `entity_schemas.md`: FreezeResponse).
- **Identity.** `identifier` + `name` required with `accountId`, `yaml`
  (FreezeResponse).
- **Owned by.** Its scope container. **References.** The org/project/
  service/environment entities selected by its rules.
- **Type / status.** `type` enum `GLOBAL, MANUAL`; `status` enum
  `Enabled, Disabled` (FreezeResponse).
- **YAML.** (yaml_examples/continuous-delivery__manage-deployments__deployment-freeze.md.yaml)

  ```yaml
  freeze:
    name: example
    identifier: example
    entityConfigs:
      - name: myapp freeze
        entities:
          - type: Org
            filterType: All
          - type: Service
            filterType: All
          - type: EnvType
            filterType: All
    status: Disabled
    windows:
      - timeZone: America/Los_Angeles
        startTime: 2023-07-03 10:08 AM
        endTime: 2023-07-05 10:38 AM
  ```

- **API surface.** legacy NG only in this corpus: `/ng/api/freeze`,
  `.../freeze/list`, `.../freeze/{freezeIdentifier}`,
  `.../freeze/manageGlobalFreeze`, `.../freeze/getGlobalFreeze`,
  `.../freeze/updateFreezeStatus`, `.../freeze/getFrozenExecutionDetails`
  (path_tree.txt).
- **Lifecycle.** Enabled/Disabled; enabled windows cannot be edited — disable
  first (deployment-freeze.md, "Important notes").
- **Gotchas.** Freeze applies to CD stages only; CI stages in the same
  pipeline keep running. A running pipeline finishes its current stage, then
  freezes ("Aborted By Freeze"). Account admins always bypass. Custom
  webhook triggers can override a freeze if their API key has the override
  permission (deployment-freeze.md).

## A.15 Build Infrastructure

- **Definition.** Where a CI stage's steps run: Harness Cloud (Harness-managed
  machines), a self-managed Kubernetes cluster (each stage executes in a
  pod), self-managed AWS/GCP/Azure VMs, or a local Docker runner
  (docs/continuous-integration/use-ci/set-up-build-infrastructure/which-build-infrastructure-is-right-for-me.md).
- **Scopes.** Configured per CI stage (`stage.spec.platform` + `runtime` or
  `infrastructure`); not a standalone CRUD entity.
- **Owned by.** CI Stage. **References.** Kubernetes connector + namespace
  (cluster infra), delegate (self-managed paths).
- **YAML.** Harness Cloud runtime
  (yaml_examples/continuous-integration__use-ci__caching-ci-data__cache-intelligence.md.yaml, example 2):

  ```yaml
  - stage:
      type: CI
      spec:
        platform:
          os: Linux
          arch: Amd64
        runtime:
          type: Cloud    # Harness Cloud; K8s uses infrastructure: KubernetesDirect
          spec: {}
  ```

- **Platform support.** Linux amd64/arm64 everywhere; macOS arm64 only on
  Harness Cloud (recommended) or local runner; Windows amd64 everywhere,
  Windows arm64 nowhere (which-build-infrastructure-is-right-for-me.md,
  support matrix).
- **Gotchas.** Feature availability varies by infrastructure — e.g. Build
  Intelligence is Cloud/K8s Linux only; delegate selectors are "not
  applicable" on Harness Cloud and unsupported on VM infra (same doc's
  feature matrix). New CI features generally land on Harness Cloud first.

## A.16 Codebase

- **Definition.** A CI pipeline's configured Git repository: connector +
  repo + clone behavior. "When you add a Build stage to a CI pipeline, you
  specify where your build code is stored. This becomes the pipeline's
  _default codebase_"
  (docs/continuous-integration/use-ci/codebase-configuration/create-and-configure-a-codebase.md).
- **Scopes.** Property of a Pipeline (`pipeline.properties.ci.codebase`).
- **Owned by.** Pipeline. **References.** Code-repo Connector
  (`connectorRef`) or Harness Code repo (`repoName`).
- **YAML.** (create-and-configure-a-codebase.md)

  ```yaml
  pipeline:
    ...
    properties:
      ci:
        codebase:
          connectorRef: YOUR_CODEBASE_CONNECTOR_ID
          build: <+input>     # branch / tag / PR chosen at runtime
  ```

- **API surface.** None standalone; embedded in pipeline YAML.
- **Gotchas.** Each Build stage clones the default codebase unless
  `cloneCodebase: false` (same doc). Webhook triggers require the pipeline to
  have a default codebase to listen on (triggering-pipelines.md). Built-in
  codebase variables (`<+codebase.*>`) describe the resolved clone
  (docs/continuous-integration/use-ci/codebase-configuration/built-in-cie-codebase-variables-reference.md).

## A.17 CI Step catalog

- **Definition.** The CI-specific step types that populate Build stages. The
  step catalog groups: build & push / upload & download artifacts, run tests,
  manage dependencies (Background steps), share & cache data, run scripts
  (Run step), and plugins
  (docs/continuous-integration/use-ci/prep-ci-pipeline-components.md, "Steps").
  Modeled here as kinds of Step (A.6), not separate entities.
- **Key types.**
  - **Run** — execute scripts in a container or on the host
    (docs/continuous-integration/use-ci/run-step-settings.md).
  - **Build and Push** — build an image and push to a registry (Docker, ACR,
    ECR, GAR, JFrog…) (docs/continuous-integration/use-ci/build-and-upload-artifacts/build-and-push/build-and-push-to-docker-registry.md).
  - **Background** — long-lived service dependencies for the stage (databases,
    emulators) (docs/continuous-integration/use-ci/manage-dependencies/background-step-settings.md).
  - **Plugin** — Drone-style container plugins, incl. GitHub Actions/Bitrise
    wrappers (docs/continuous-integration/use-ci/use-drone-plugins/plugin-step-settings-reference.md).
  - **Test (Run Tests)** — test execution with Test Intelligence (A.18)
    (docs/continuous-integration/use-ci/run-tests/ti-overview.md).
- **YAML.** Cache steps as an example of the family shape
  (yaml_examples/continuous-integration__use-ci__caching-ci-data__save-cache-in-gcs.md.yaml):

  ```yaml
  - step:
      type: SaveCacheGCS
      name: Save Cache to GCS_1
      identifier: SaveCachetoGCS_1
      spec:
        connectorRef: account.gcp   # account-scope connector reference
        bucket: ci_cache
        key: gcs-{{ checksum filePath1 }}
        sourcePaths: [directory1, directory2]
        archiveFormat: Tar
  ```

- **Gotchas.** Plugin behavior differs by infrastructure (host-machine plugin
  runs are Harness Cloud only; Bitrise steps are Harness Cloud only) —
  which-build-infrastructure-is-right-for-me.md feature matrix.

## A.18 Test Intelligence

- **Definition.** "Harness Test Intelligence (TI) improves unit test time by
  running only the unit tests required to confirm the quality of the code
  changes that triggered the build"
  (docs/continuous-integration/use-ci/run-tests/ti-overview.md).
- **Scopes.** A capability of the Test step in CI stages, backed by a
  Harness-side TI service; not a CRUD entity.
- **How it selects.** Changed code (via Git), changed tests, new tests; files
  like `build.gradle`/`pom.xml` can trigger full runs (ti-overview.md).
- **Architecture.** TI service (call graphs, commit graphs) + Test Runner
  Agent (on build infra) + Test step (ti-overview.md, "Test Intelligence
  architecture").
- **References.** Codebase (commit/PR data), webhook trigger events —
  the Git trigger must include Synchronize and merge/close events for TI's
  call graph to stay correct (ti-overview.md).
- **Gotchas.** Unit tests only; supported for Python, Java, Ruby, C#, Kotlin,
  Scala (JS/Kotest in beta — Appendix D#10). To ignore files, add
  `.ticonfig.yaml` to the codebase (ti-overview.md).

## A.19 Cache Intelligence

- **Definition.** Automatic dependency caching for CI: "Harness automatically
  caches and restores software dependencies to speed up your builds"
  (docs/continuous-integration/use-ci/caching-ci-data/cache-intelligence.md).
- **Scopes.** Per CI stage (`stage.spec.caching.enabled: true`).
- **Owned by.** CI Stage. **References.** On self-managed infrastructure, a
  default object-storage config (S3/GCS/Azure Blob); on Harness Cloud,
  Harness-managed storage (cache-intelligence.md, "Cache storage").
- **YAML.** (yaml_examples/continuous-integration__use-ci__caching-ci-data__cache-intelligence.md.yaml, example 1)

  ```yaml
  - stage:
      type: CI
      spec:
        caching:
          enabled: true
          paths:
            - /harness/node_modules   # custom cache path
        cloneCodebase: true
  ```

- **Lifecycle.** On Harness Cloud: 15-day retention window, reset on cache
  update; old caches auto-evicted at the storage limit
  (cache-intelligence.md).
- **Gotchas.** Detects build tools (Maven, Gradle, Bazel, Yarn, Go, .NET…)
  only at repo root and one directory deep; deeper layouts need custom paths
  (cache-intelligence.md, "Supported tools and paths"). Enabled by default
  for newly created CI stages.

## A.20 Artifact (build output)

- **Definition.** The image or file a CI stage produces and pushes (via Build
  and Push / upload steps), surfaced on the execution's **Artifacts** tab
  (docs/continuous-integration/use-ci/build-and-upload-artifacts/artifacts-tab.md).
- **Scopes.** Belongs to an Execution (viewable per build).
- **Owned by.** Execution — `/v1/orgs/{org}/projects/{project}/pipelines/{pipeline}/executions/{execution}/artifacts`
  (path_tree.txt). **References.** Registry/storage connectors used to push.
- **YAML.** Publishing metadata to the Artifacts tab uses the
  `artifact-metadata-publisher` plugin
  (yaml_examples/continuous-integration__use-ci__build-and-upload-artifacts__artifacts-tab.md.yaml, example 1):

  ```yaml
  - step:
      type: Plugin
      name: publish artifact metadata
      identifier: publish_artifact_metadata
      spec:
        connectorRef: YOUR_IMAGE_REGISTRY_CONNECTOR
        image: plugins/artifact-metadata-publisher
        settings:
          file_urls: https://domain.com/path/to/artifact
  ```

- **Gotchas.** Do not confuse with the CD *artifact source* (part of a
  Service definition, A.21) or the Artifact Registry module (out of scope,
  Ch 1).

## A.21 Service

- **Definition.** "A Harness service represents what you're deploying." Each
  service contains a **Service Definition**: artifacts, manifests,
  config files, and service variables
  (docs/continuous-delivery/x-platform-cd-features/services/services-overview.md).
- **Scopes.** Account, Org, or Project ("You can create services from: an
  account, an organization, within a pipeline, outside a pipeline", same doc).
- **Identity.** `identifier`, `name`; `ServiceRequest` carries
  `orgIdentifier`/`projectIdentifier` + `yaml` (`entity_schemas.md`).
- **Owned by.** Its scope container. **Owns.** Its Service Definition
  (manifests, artifact sources, variables — YAML-embedded).
- **References.** Connectors for manifest stores and artifact registries,
  across scopes: `connectorRef: account.Harness_DockerHub`, `org.bitnami`
  (services-overview.md YAML samples).
- **YAML.** (docs/continuous-delivery/x-platform-cd-features/services/services-overview.md, account-level sample)

  ```yaml
  service:
    name: nginx
    identifier: nginx
    serviceDefinition:
      type: Kubernetes
      spec:
        manifests:
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
        artifacts:
          primary:
            primaryArtifactRef: <+input>
            sources:
              - identifier: harness dockerhub
                type: DockerRegistry
                spec:
                  connectorRef: account.Harness_DockerHub
                  imagePath: library/nginx
                  tag: <+input>
  ```

- **API surface.**

  | Operation | v1 beta | legacy NG |
  |---|---|---|
  | CRUD | `/v1/orgs/{org}/projects/{project}/services[/{service}]` (+ org- and account-level `/v1/services`) | `/ng/api/servicesV2[/{serviceIdentifier}]`, `.../upsert`, `.../batch` |
  | Import / Git | — | `.../servicesV2/import`, `.../move-config/{serviceIdentifier}`, `.../update-git-metadata` |

  (path_tree.txt)

- **Gotchas.** An account-level service can only reference account-level
  connectors: "These services are global and cannot have dependencies at a
  lower hierarchy level" (services-overview.md). Account-level stage
  templates can reference only account-level services (same doc).

## A.22 Environment

- **Definition.** "A Harness environment represents where you are deploying
  your application", categorized prod or non-prod; it holds infrastructure
  definitions, environment variables, and service overrides
  (docs/continuous-delivery/x-platform-cd-features/environments/environment-overview.md).
- **Scopes.** Account, Org, or Project (same doc, "Creating environments").
- **Identity.** `identifier`, `name`; `type` required, enum
  `PreProduction, Production` (`entity_schemas.md`: EnvironmentRequest).
- **Owned by.** Scope container. **Owns.** Infrastructure Definitions
  (URL nesting: `/v1/environments/{environment}/infrastructures/{infrastructure-definition}`,
  path_tree.txt; `InfrastructureRequest.environmentRef`), environment
  variables, and environment-level override configuration.
- **References.** Referenced by pipelines (`environmentRef`), Environment
  Groups, Service Overrides, Freeze rules.
- **YAML.** (environment-overview.md, account-level sample)

  ```yaml
  environment:
    name: dev
    identifier: dev
    type: PreProduction        # enum: PreProduction | Production
    variables:
      - name: port
        type: String
        value: "8080"
      - name: namespace
        type: String
        value: <+service.name>-dev   # expressions allowed in env vars
  ```

- **API surface.**

  | Operation | v1 beta | legacy NG |
  |---|---|---|
  | CRUD | `/v1/environments`, `/v1/orgs/{org}/environments`, `/v1/orgs/{org}/projects/{project}/environments[/{environment}]` | `/ng/api/environmentsV2[/{environmentIdentifier}]`, `.../upsert` |
  | Infra children | `.../environments/{environment}/infrastructures[/{infrastructure-definition}]` | (see A.23) |
  | Overrides (legacy) | — | `/ng/api/environmentsV2/serviceOverrides` |

  (path_tree.txt)

- **Gotchas.** The env `type` drives freeze rules (`EnvType` filter,
  deployment-freeze.md YAML) and prod/non-prod behavior in dashboards. The
  three v1 path families (account/org/project) are the same entity at three
  scopes — don't model them separately.

## A.23 Infrastructure Definition

- **Definition.** The concrete deployment target inside an environment —
  "the specific VM, Kubernetes cluster, or target infrastructure where you
  plan to deploy your application" (environment-overview.md).
- **Scopes.** Lives under an Environment at any scope.
- **Identity.** `identifier`, `name`; `yaml` required; `type` enum:
  `KubernetesDirect, KubernetesGcp, KubernetesAzure, Pdc, SshWinRmAzure,
  ServerlessAwsLambda, AzureWebApp, AzureFunction, SshWinRmAws,
  CustomDeployment, ECS, Elastigroup`; response adds `deploymentType` enum
  `Kubernetes, NativeHelm, Ssh, WinRm, ServerlessAwsLambda, AzureWebApp,
  AzureFunction, CustomDeployment, ECS, Elastigroup, TAS, Asg`
  (`entity_schemas.md`: InfrastructureRequest / InfrastructureResponseDTO).
- **Owned by.** Environment (`environmentRef` field + URL nesting
  `/v1/environments/{environment}/infrastructures/...`, path_tree.txt).
- **References.** Cloud/cluster Connector (`spec.connectorRef`).
- **YAML.** (environment-overview.md, account-level sample)

  ```yaml
  infrastructureDefinition:
    name: dev-k8s
    identifier: dev
    environmentRef: dev            # owning environment
    deploymentType: Kubernetes
    type: KubernetesDirect
    spec:
      connectorRef: account.Harness_Kubernetes_Cluster
      namespace: <+service.name>-dev
      releaseName: release-<+INFRA_KEY_SHORT_ID>
    allowSimultaneousDeployments: false
  ```

- **API surface.** v1: nested under environments (above). legacy NG:
  infrastructure CRUD exists under `/ng/api/infrastructures` in the full API;
  in this corpus the legacy evidence is the `InfrastructureRequest/ResponseDTO`
  schemas (`entity_schemas.md`). The `/api/infrastructures` paths in
  path_tree.txt belong to another module (IACM/armory-style executor) —
  keyword over-inclusion, see Appendix D#4.
- **Gotchas.** `allowSimultaneousDeployments` gates concurrent deploys into
  the same infra. Infrastructure can be scoped to specific services
  (docs/continuous-delivery/x-platform-cd-features/environments/scope-infra-to-services.md).

## A.24 Environment Group

- **Definition.** A named collection of environments for bulk selection in
  pipelines and governance
  (docs/continuous-delivery/x-platform-cd-features/environments/create-environment-groups.md).
- **Scopes.** Account, Org, or Project; members can come from higher scopes.
- **Identity.** `identifier` pattern `^[a-zA-Z_][0-9a-zA-Z_]{0,127}$` (note:
  no `$` allowed, unlike pipeline identifiers); `yaml` required
  (`entity_schemas.md`: EnvironmentGroupRequest).
- **Owned by.** Scope container. **References.** Environments by identifier,
  with scope prefixes.
- **YAML.** (create-environment-groups.md; also
  yaml_examples/continuous-delivery__x-platform-cd-features__environments__create-environment-groups.md.yaml)

  ```yaml
  environmentGroup:
    name: demoEnvGroup
    identifier: demoEnvGroup
    orgIdentifier: default
    projectIdentifier: CD_Docs
    envIdentifiers:
      - test                              # project scope: no prefix
      - org.testE                         # org scope
      - account.CDCNGAuto_EnvNg59wFkWCjQQ # account scope
  ```

- **API surface.** legacy NG only in corpus: `/ng/api/environmentGroup`,
  `.../environmentGroup/list`, `.../environmentGroup/{envGroupIdentifier}`
  (path_tree.txt).
- **Gotchas.** The `envIdentifiers` list is the canonical, doc-stated example
  of cross-scope reference prefixes (create-environment-groups.md) — the same
  syntax used for connectors, services, templates.

## A.25 Service Override

- **Definition.** Values that replace parts of a service's configuration when
  it deploys into a particular environment (or infra/cluster): "To enable the
  same service to use different environment settings, DevOps teams can
  override service settings for each environment"
  (docs/continuous-delivery/x-platform-cd-features/environments/service-overrides.md).
- **Scopes.** Account, Org, or Project (overrides-v2 exposes them under
  Project/Org/Account settings — service-overrides.md).
- **Identity.** `identifier` plus targeting fields `environmentRef`,
  `serviceRef`, `infraIdentifier`, `clusterIdentifier`; `type` enum:
  `ENV_GLOBAL_OVERRIDE, ENV_SERVICE_OVERRIDE, INFRA_GLOBAL_OVERRIDE,
  INFRA_SERVICE_OVERRIDE, CLUSTER_GLOBAL_OVERRIDE, CLUSTER_SERVICE_OVERRIDE`
  (`entity_schemas.md`: ServiceOverrideResponseV2).
- **Owned by.** Historically nested under Environment
  (`/ng/api/environmentsV2/serviceOverrides`); v2 is a standalone resource
  (`/ng/api/serviceOverrides`). **References.** Environment, Service,
  optionally Infrastructure Definition / GitOps cluster.
- **What can be overridden.** Manifests (Values YAML, OpenShift Param,
  Kustomize, Helm Repo, ECS/TAS types), config files, variables
  (service-overrides.md, "Override types").
- **Merge semantics.** Values YAML merges name-by-name (higher priority wins
  per key); config files and variables replace wholesale
  (service-overrides.md).
- **API surface.** legacy NG: `/ng/api/serviceOverrides[/{identifier}]`,
  `.../move-config`, `.../update-git-metadata`;
  `/ng/api/environmentsV2/serviceOverrides` (v1-era of the feature)
  (path_tree.txt). No v1-beta path in corpus.
- **Gotchas.** Runtime inputs are not supported for overrides in
  multi-service/multi-environment setups (service-overrides.md,
  "Limitations"). Helm Repo overrides must keep the same store type as the
  service.

## A.26 Connector

- **Definition.** A typed, reusable credential-plus-endpoint object for an
  external system (Git providers, cloud platforms, registries, K8s clusters,
  ticketing, monitoring). Created in YAML like other entities
  (docs/platform/connectors/create-a-connector-using-yaml.md).
- **Scopes.** Account, Org, or Project (`org`/`project` optional fields on
  the v1 `Connector` schema).
- **Identity.** `identifier` pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`,
  maxLen 128; `name` pattern `^[0-9a-zA-Z-_ ]{0,127}$`; `spec` required and
  typed (`entity_schemas.md`: Connector).
- **Owned by.** Scope container. **References.** Secrets (credentials fields
  inside `spec`), Delegates (connectors execute through delegates —
  delegate-overview.md: "Connectors are used for all third-party
  connections").
- **YAML.** (yaml_examples/platform__pipelines__harness-yaml-quickstart.md.yaml, example 23)

  ```yaml
  connector:
    name: my-cluster
    identifier: my_cluster
    orgIdentifier: default
    projectIdentifier: default
    type: K8sCluster          # connector type
    spec:                     # shape depends on type
      credential: ...
  ```

- **API surface.**

  | Operation | v1 beta | legacy NG |
  |---|---|---|
  | CRUD | `/v1/connectors`, `/v1/orgs/{org}/connectors`, `/v1/orgs/{org}/projects/{project}/connectors[/{connector}]` | `/ng/api/connectors[/{identifier}]`, `.../listV2` |
  | Test | `.../connectors/{connector}/test-connection` | `.../connectors/testConnection/{identifier}`, `.../testGitRepoConnection/{identifier}` |
  | Catalog | — | `/ng/api/connectors/catalogue` |

  (path_tree.txt)

- **Gotchas.** Referenced everywhere as `connectorRef` with scope prefixes
  (`account.gcp`, `org.bitnami`). A connector at account scope is the way to
  share credentials across all projects — but entities at account scope can
  only use account-scope connectors (services-overview.md).

## A.27 Secret

- **Definition.** A managed sensitive value — text, file, or SSH credential —
  stored encrypted and referenced from YAML by expression
  (docs/platform/secrets/add-use-text-secrets.md).
- **Scopes.** Account, Org, or Project (v1 `Secret` schema has optional
  `org`, `project`).
- **Identity.** `identifier` pattern `^[a-zA-Z_][0-9a-zA-Z_$-]{0,127}$`
  (note: hyphen allowed — unlike Pipeline/Connector identifiers), maxLen 128;
  `name` pattern `^[0-9a-zA-Z-_ ]{0,127}$`; `spec` required
  (`entity_schemas.md`: Secret; see Appendix D#6).
- **Owned by.** Scope container. **References.** Its Secret Manager
  (storage backend).
- **Usage.** `<+secrets.getValue("secretfile")>` in step env/commands
  (yaml_examples/platform__secrets__add-use-text-secrets.md.yaml); scope
  prefixes apply: `<+secrets.getValue("account.mysecret")>` (implied by the
  OPA example in docs/platform/variables-and-expressions/runtime-inputs.md).
- **API surface.**

  | Operation | v1 beta | legacy NG |
  |---|---|---|
  | CRUD | `/v1/orgs/{org}/projects/{project}/secrets[/{secret}]` | `/ng/api/v2/secrets[/{identifier}]`, `.../files`, `.../yaml` |
  | Validate | `.../secrets/validate-secret-ref` | `/ng/api/v2/secrets/validate` |

  (path_tree.txt)

- **Lifecycle.** `draft` flag on SecretResponse (`entity_schemas.md`).
- **Gotchas.** Secret values used as runtime input are visible to anyone who
  can run the pipeline — the docs recommend OPA policies to block
  `<+secrets.getValue` in runtime input (runtime-inputs.md, warning note).
  Harness sanitizes secrets out of logs
  (docs/platform/secrets/secrets-management/secrets-and-log-sanitization.md).

## A.28 Secret Manager

- **Definition.** The backend that stores/encrypts secrets. Built-in default:
  "Google Cloud Key Management Service is the default Secret Manager in
  Harness and is named Harness Secret Manager Google KMS"; alternatives
  include AWS KMS, HashiCorp Vault, Azure Key Vault, GCP Secrets Manager,
  AWS Secrets Manager, custom
  (docs/platform/secrets/secrets-management/harness-secret-manager-overview.md).
- **Scopes.** Configured like connectors at any scope. **INFERRED** from its
  configuration docs living alongside connector setup
  (docs/platform/secrets/secrets-management/add-an-aws-kms-secrets-manager.md etc.)
  and the `SecretManager` template type (`entity_schemas.md`:
  TemplateResponse `entity_type` enum).
- **Owns.** The stored secret material. **Referenced by.** Secrets.
- **Key architectural fact.** "Harness Manager does not have access to your
  key management system, and only the Harness Delegate, which sits in your
  private network, has access to it" — decryption happens on the delegate
  (harness-secret-manager-overview.md).
- **KMS vs third-party.** KMS options store only the key (secrets encrypted
  in Harness DB via envelope encryption); third-party managers store keys and
  secrets, Harness keeps only a reference (same doc).
- **Gotchas.** KMS key rotation is unsupported — losing the old key version
  loses the secrets (same doc, warning). Secret cache TTL is 30 minutes
  (except Vault). Secrets Manager configs can themselves be templated
  (docs/platform/templates/create-a-secret-manager-template.md).

## A.29 Delegate

- **Definition.** "Harness Delegate is a service you run in your local
  network or VPC to connect your artifacts, infrastructure, collaboration,
  verification, and other providers with Harness Manager... The delegate
  performs all operations, including deployment and integration"
  (docs/platform/delegates/delegate-concepts/delegate-overview.md).
- **Scopes.** Account, Org, or Project ("You can view a list of your
  delegates at the account, project, and org level", same doc;
  `DelegateGroupDTO` has `orgIdentifier`/`projectIdentifier`).
- **Identity.** `name` + `identifier` on the delegate group; `size` enum
  `LAPTOP, SMALL, MEDIUM, LARGE, CCM_SMALL`
  (`entity_schemas.md`: DelegateGroupDTO / DelegateSetupDetails).
- **Owned by.** Scope container. **References.** Delegate Token for
  registration (`tokenName`, DelegateSetupDetails;
  docs/platform/delegates/secure-delegates/secure-delegates-with-tokens.md).
- **Communication.** Outbound-only HTTPS/WSS to Harness Manager; heartbeats
  every minute; task data does not flow over the WebSocket channel
  (delegate-overview.md).
- **Task assignment.** Selector tags → heartbeat liveness → capability check
  against the target system (delegate-overview.md, "How Harness Manager picks
  delegates").
- **API surface.** legacy NG: `/ng/api/delegate-setup/listDelegates`,
  `.../delegate-setup/delegate/{delegateIdentifier}`,
  `/ng/api/delegate-group-tags/...`, `/ng/api/delegate-token-ng`,
  `/ng/api/download-delegates/{docker|kubernetes}` (path_tree.txt). No v1
  path in corpus.
- **Lifecycle.** Registration → Connected/Not Connected (heartbeat) →
  expiration by image version; auto-upgrade supported
  (delegate-overview.md, Delegates list page fields).
- **Gotchas.** If you pin specific delegates via selectors and they can't do
  the task, Harness does not fall back to others (delegate-overview.md).
  Harness Cloud build infra needs no delegate — that's the point of it
  (which-build-infrastructure-is-right-for-me.md).

## A.30 Template

- **Definition.** A versioned, reusable definition of a Step, Stage, Pipeline
  (and more) that pipelines link to instead of copying
  (docs/platform/templates/template.md).
- **Scopes.** Account, Org, or Project; `scope` enum
  `org, project, account, unknown` (`entity_schemas.md`: TemplateResponse).
- **Identity.** `identifier` pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`,
  maxLen 128, **plus** `version_label` — identity is (identifier, version);
  `entity_type` enum `Step, Stage, Pipeline, CustomDeployment,
  MonitoredService, SecretManager`; `stable_template` boolean
  (`entity_schemas.md`: TemplateResponse / TemplateCreateRequestBody).
  Docs additionally list Step Group and Artifact Source template types
  (template.md; see Appendix D#8).
- **Owned by.** Scope container. **Referenced by.** Pipelines/stages/steps
  via `template.templateRef` + `templateInputs`
  (yaml_examples/continuous-delivery__cd-onboarding__new-user__cd-pipeline-modeling-overview.md.yaml).
- **YAML (usage site).**

  ```yaml
  - stage:
      name: deploy_service
      identifier: deploy_service
      template:
        templateRef: Golden_K8s     # scope prefixes apply: org. / account.
        templateInputs:             # the template's declared <+input> slots
          type: Deployment
          spec:
            services:
              values: <+input>
  ```

- **API surface.**

  | Operation | v1 beta | legacy NG |
  |---|---|---|
  | CRUD | (template v1 endpoints not in corpus) | `/template/api/templates`, `.../update/{templateIdentifier}/{versionLabel}` |
  | Stable version | — | `.../updateStableTemplate/{templateIdentifier}/{versionLabel}` |
  | Inputs | — | `.../templateInputs/{templateIdentifier}` |
  | Resolve | — | `/template/api/templates/v2/applyTemplates`, `/template/api/refresh-template/refreshed-yaml` |

  (path_tree.txt)

- **Lifecycle.** Multiple versions; one may be marked **stable**: "When you
  mark a new version of the template as stable, it is automatically picked up"
  by pipelines linked to the stable version (template.md, "Stable version").
  New inputs require a new version.
- **Gotchas.** Deleting a template with active references deletes the
  references (template.md, "Important notes"). Changing fixed↔runtime inputs
  does not propagate — you must reconcile linked pipelines. A template can
  only fix-reference resources at its own scope or higher (template.md,
  "Referencing objects within a scope"). Pipeline templates with chained
  pipeline stages are unsupported.

## A.31 Variable

- **Definition.** A named value defined at account, org, or project scope (or
  inline on pipelines/stages/services/environments), read via expressions
  (docs/platform/variables-and-expressions/add-a-variable.md).
- **Scopes.** Account, Org, Project (entity form); pipeline/stage/service/
  environment (inline form).
- **Identity.** `identifier`, `name`, `type` required; `type` enum: `String`
  (`entity_schemas.md`: VariableDTO). Docs show stage variables with
  `type: String ## String or Secret` (add-a-stage.md) — see Appendix D#7.
- **Owned by.** Scope container (or owning pipeline/stage for inline).
- **Reference syntax.** (add-a-variable.md)

  | Scope | Expression |
  |---|---|
  | Account | `<+variable.account.VAR_NAME>` |
  | Org | `<+variable.org.VAR_NAME>` |
  | Project | `<+variable.VAR_NAME>` |
  | Pipeline | `<+pipeline.variables.VAR_NAME>` |
  | Stage (same stage) | `<+stage.variables.VAR_NAME>` |
  | Stage (other stage) | `<+pipeline.stages.STAGE_ID.variables.VAR_NAME>` |

- **API surface.** legacy NG: `/ng/api/variables[/{identifier}]`,
  `.../variables/list` (path_tree.txt). (The `/v1/backstage-env-variables`
  paths are the IDP module — keyword noise, Appendix D#4.)
- **Gotchas.** Higher-scope variables are visible to all lower scopes
  (add-a-variable.md). Stage variables can be overridden by later stages.

---

*End of Appendix A. Relationship edges asserted here are diagrammed and
re-verified in Appendix B; unresolved doc/spec tensions are catalogued in
Appendix D.*

