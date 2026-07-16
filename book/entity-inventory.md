# Entity Inventory (Checkpoint 2 — for review)

Scope: the Harness pipeline offering (CI + CD) plus its direct dependencies.
**31 entities**, within the 25–35 target. Each line: entity, one-liner, primary
evidence (doc path / API path / schema name from `corpus/`).

Corpus verification: all six corpus pieces present and readable. Counts:
1,278 docs in `doc_index.csv` (prompt said ~1,280 ✓), 1,381 schemas in
`entity_schemas.md` ✓, 359 files / 1,582 YAML blocks in `yaml_examples/` ✓,
474 paths in `openapi_pipeline.yaml` vs 476 claimed (Δ2, logged for
Appendix D). `HARNESS_API_KEY` is **not set** → live phase skipped (Appendix D).

## A. Scope hierarchy (3)

| # | Entity | One-liner | Evidence |
|---|--------|-----------|----------|
| 1 | **Account** | Root scope; every resource lives in exactly one account; account-scope resources referenced as `account.<id>`. | `entity_schemas.md` (`accountIdentifier` on most schemas); paths `/ng/api/accounts/{accountIdentifier}/...` in `path_tree.txt` |
| 2 | **Organization** | Grouping scope under Account; org-scope resources referenced as `org.<id>`. | `path_tree.txt` `/v1/orgs/{org}/...`; `entity_schemas.md` (`orgIdentifier`) |
| 3 | **Project** | Working scope under Organization where pipelines usually live. | `path_tree.txt` `/v1/orgs/{org}/projects/{project}/...`; docs/continuous-delivery/gitops/gitops-entities/projects/manage-projects.md (adjacent-module analog) |

## B. The pipeline aggregate (5)

| # | Entity | One-liner | Evidence |
|---|--------|-----------|----------|
| 4 | **Pipeline** | The YAML-defined workflow; root of the Pipeline > Stage > Step aggregate; inline or Git-backed (GitX). | docs/platform/pipelines/harness-yaml-quickstart.md; `/v1/orgs/{org}/projects/{project}/pipelines` + `/pipeline/api/pipelines`; schema `PipelineCreateRequestBody` |
| 5 | **Stage** | Typed unit of work inside a pipeline (CI, Deployment, Approval, Custom…); owns steps and (per type) infrastructure. | docs/platform/pipelines/add-a-stage.md; schema `StageExecutionResponseBody` |
| 6 | **Step** | Atomic action inside a stage; type catalog differs by stage type. | docs/continuous-delivery/x-platform-cd-features/cd-steps/containerized-steps/run-step.md; yaml_examples (step blocks throughout) |
| 7 | **Step Group** | Named grouping of steps sharing settings/containers; can be containerized in CD. | docs/continuous-delivery/x-platform-cd-features/cd-steps/containerized-steps/containerized-step-groups.md |
| 8 | **Execution** | A run of a pipeline: plan + node graph + statuses; supports interrupts, retry, rerun. | docs/platform/pipelines/executions-and-logs/executions-management.md; `/pipeline/api/pipelines/execution/{planExecutionId}`, `getExecutionGraph/{planExecutionId}`; schema `ExecutionGraph` |

## C. Parameterization and events (4)

| # | Entity | One-liner | Evidence |
|---|--------|-----------|----------|
| 9 | **Input Set** | Saved values for a pipeline's runtime inputs — "saved arguments" to the pipeline-as-function. | docs/platform/pipelines/input-sets.md; `/v1/orgs/{org}/projects/{project}/input-sets`, `/pipeline/api/inputSets`; schema enum `INPUT_SET` |
| 10 | **Overlay Input Set** | Ordered composition of input sets; later sets override earlier. | docs/platform/pipelines/input-sets.md; schema enum `inputSetType: INPUT_SET, OVERLAY_INPUT_SET` |
| 11 | **Trigger** | Rule that starts a pipeline on an event: webhook, cron/scheduled, or new-artifact; binds payload to runtime inputs. | docs/platform/triggers/triggering-pipelines.md, trigger-on-a-new-artifact.md, schedule-pipelines-using-cron-triggers.md; `/pipeline/api/triggers`; schema `NGTriggerDetailsResponseDTO` |
| 12 | **Webhook** | The registered HTTP endpoint / Git-provider event source behind webhook triggers. | docs/platform/triggers/trigger-deployments-using-custom-triggers.md; schemas `GithubWebhookSpec`-family (`entity_schemas.md`) |

## D. Control gates (2)

| # | Entity | One-liner | Evidence |
|---|--------|-----------|----------|
| 13 | **Approval** | Human or ticket-system gate (Harness UI, Jira, ServiceNow) as step/stage; pauses execution until verdict. | docs/continuous-delivery/x-platform-cd-features/cd-steps/approvals/using-harness-approval-steps-in-cd-stages.md; schemas `Approval*` |
| 14 | **Deployment Freeze** | Time-windowed rule blocking deployments at a chosen scope. | docs/continuous-delivery/manage-deployments/deployment-freeze.md; `/ng/api/freeze`; schema `FreezeDetailedResponse` |

## E. CI-side entities (6)

| # | Entity | One-liner | Evidence |
|---|--------|-----------|----------|
| 15 | **Build Infrastructure** | Where CI stage steps run: Harness Cloud, Kubernetes, VM, Docker, local. | docs/continuous-integration/use-ci/set-up-build-infrastructure/which-build-infrastructure-is-right-for-me.md, harness-ci.md |
| 16 | **Codebase** | The CI stage's configured Git repo: connector + repo + clone behavior; source of built-in codebase variables. | docs/continuous-integration/use-ci/codebase-configuration/* (e.g. built-in-cie-codebase-variables-reference.md) |
| 17 | **CI Step catalog** | The CI-specific step types: Run, Build and Push, Background, Plugin, Run Tests. Modeled as kinds of Step (#6), inventoried once. | docs/continuous-integration/use-ci/build-and-upload-artifacts/build-and-push/build-and-push-to-docker-registry.md; run-step docs; yaml_examples CI files |
| 18 | **Test Intelligence** | Selective test execution for Run Tests steps based on code changes. | docs/continuous-integration/use-ci/run-tests/ti-overview.md |
| 19 | **Cache Intelligence** | Managed dependency caching for CI stages. | docs/continuous-integration/use-ci/caching-ci-data/cache-intelligence.md |
| 20 | **Artifact (build output)** | Image/file produced and pushed by CI; surfaced on the Artifacts tab. | docs/continuous-integration/use-ci/build-and-upload-artifacts/artifacts-tab.md |

## F. CD-side entities (5)

| # | Entity | One-liner | Evidence |
|---|--------|-----------|----------|
| 21 | **Service** | What you deploy: manifest + artifact definition, reusable across pipelines. | docs/continuous-delivery/x-platform-cd-features/services/create-services.md; `/ng/api/servicesV2`, `/v1/.../services`; schema `ServiceRequest` |
| 22 | **Environment** | Where you deploy (logical target, e.g. prod/pre-prod); owns infrastructure definitions and overrides. | docs/continuous-delivery/x-platform-cd-features/environments/environment-overview.md; `/ng/api/environmentsV2`, `/v1/environments`; schema `EnvironmentRequest` |
| 23 | **Infrastructure Definition** | Concrete target inside an environment (cluster/namespace, VM group…); child of Environment by URL nesting. | `/v1/environments/{environment}/infrastructures/{infrastructure-definition}` (`path_tree.txt`); schema `InfrastructureRequest`; docs/continuous-delivery/x-platform-cd-features/environments/scope-infra-to-services.md |
| 24 | **Environment Group** | Named collection of environments for bulk targeting. | docs/continuous-delivery/x-platform-cd-features/environments/create-environment-groups.md; `/ng/api/environmentGroup`; schema `EnvironmentGroupResponse` |
| 25 | **Service Override** | Per environment(-group)/service value overrides (variables, manifests, config files). | docs/continuous-delivery/x-platform-cd-features/environments/service-overrides.md, overrides-v2.md; `/ng/api/serviceOverrides` |

## G. Dependencies — concise treatment (6)

| # | Entity | One-liner | Evidence |
|---|--------|-----------|----------|
| 26 | **Connector** | Typed credential+endpoint object for external systems (Git, cloud, registries, K8s). | docs/platform/connectors/* (32 docs); `/ng/api/connectors`, `/v1/connectors`; schema `ConnectorInfoDTO` |
| 27 | **Secret** | Managed sensitive value (text, file, SSH) referenced from YAML. | docs/platform/secrets/add-use-text-secrets.md; `/ng/api/v2/secrets`; schema `SecretRequest` |
| 28 | **Secret Manager** | Backend that stores secrets (built-in, KMS, Vault, GCP SM…), itself configured as a connector. | docs/platform/secrets/secrets-management/add-an-aws-kms-secrets-manager.md et al. |
| 29 | **Delegate** | Customer-side worker process that executes tasks and reaches private infrastructure. | docs/platform/delegates/delegate-concepts/delegate-overview.md; `/ng/api/delegate-group-tags/...`; schema `DelegateGroupDTO` |
| 30 | **Template** | Versioned reusable definition for step/stage/pipeline (and more); stable-version semantics. | docs/continuous-delivery/x-platform-cd-features/templates/create-a-remote-pipeline-template.md; docs/platform/templates/*; schema `TemplateCreateRequestBody` |
| 31 | **Variable** | Named value at account/org/project or pipeline/stage scope, read via expressions. | docs/platform/variables-and-expressions/add-a-variable.md; schema `VariableDTO` |

## Deliberately NOT separate entities (mechanisms, covered in chapters)

- **Deployment strategies** (rolling/canary/blue-green) and **Rollback** — behavior of CD stages, Ch 7. INFERRED classification.
- **Runtime inputs & expressions** — parameterization mechanics, Ch 3.
- **GitX (Git-backed config)** — a storage property of Pipeline/InputSet/Template, Ch 1.
- **Failure strategies, looping/matrix, barriers** — execution semantics, Ch 5 (docs/platform/pipelines/failure-handling/*, looping-strategies/*).
- **Delegate Token** — Delegate detail, Ch 8.
- Adjacent modules named once in Ch 1 and excluded: GitOps, RBAC internals, CCM, Feature Flags, STO, Chaos, IDP, SEI, Code Repository, Artifact Registry internals, Database DevOps. The corpus contains Armory/Spinnaker KB articles (docs/continuous-delivery/armory/*) — legacy acquisition content; treated as noise, noted for Appendix D.

## Early Appendix D seeds

1. Prompt says 476 spec paths; corpus has 474 (`path_tree.txt` 475 lines incl. trailing). Δ2, no impact identified yet.
2. `HARNESS_API_KEY` absent → no live samples; real execution-graph status values must come from docs/spec enums only.
3. Both API generations confirmed present (`/v1/orgs/...` and `/ng/api/...`, `/pipeline/api/...`) — each entity will get a dual API table, modeled once.
4. `entity_schemas.md` over-includes non-pipeline schemas (SLO, monitored-service, IACM, cost/`gateway/lw` approvals) per keyword filtering — will be ignored; e.g. the `Approval` schema under `/gateway/lw/...` is Cloud Cost governance, NOT pipeline approvals. Pipeline approvals live in step YAML + `/pipeline/api` paths.
