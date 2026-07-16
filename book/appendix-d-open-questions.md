# Appendix D. Open questions

The week-one question list: ambiguities, doc-vs-spec conflicts, beta flags,
and corpus limitations found while writing this book. Each entry says what
we observed, why it matters, and what to ask a colleague (or verify against
a live account).

## D.1 Corpus vs. prompt path count

Observed: the task brief says the filtered OpenAPI spec has 476 paths; the
corpus contains 474 (`openapi_pipeline.yaml`; `path_tree.txt` has 475 lines).
Impact: none identified — no entity lacked API evidence. Ask: were two paths
pruned after the brief was written?

## D.2 No live API phase

`HARNESS_API_KEY` was not set, so the optional live-exploration phase was
skipped entirely. Everything the live phase would have answered remains
open: real execution-graph node shapes and status values in practice, which
response fields are actually populated, how `org.`/`account.` references
appear in production YAML at scale, and whether v1 beta and `/ng/api`
really return the same object shaped differently.

## D.3 Execution status: where is `Success`?

The `PipelineExecutionSummary.status` enum (`entity_schemas.md`) lists
`Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored,
IgnoreFailed, NotStarted, Expired, Aborted, Discontinuing, Queued` — no
`Success`/`Succeeded` value, though docs speak of successful stages and
"Aborted By Freeze" (deployment-freeze.md) also isn't in the enum. Likely
the digest truncated the enum or success is represented elsewhere. Verify
against a live execution before building anything on this enum.

## D.4 Keyword over-inclusion in the schema digest and path tree

Confirmed false friends in the corpus (ignore them when modeling
pipelines):

- `Approval` schema under `/gateway/lw/...` → Cloud Cost autostopping, not
  pipeline approvals (the real ones: `ApprovalInstanceResponse`,
  `HarnessApprovalActivity`).
- `ServiceV2` schema (cloud_account_id, idle_time_mins) → CCM autostopping,
  not the CD Service (`ServiceRequest`/`ServiceResponseDTO`).
- `/api/infrastructures/...` and `/api/environments/...` root paths →
  non-pipeline module (armory/IACM-style), not CD Infrastructure
  Definitions.
- `/v1/backstage-env-variables` → IDP module, not the Variable entity.
- `/cv/api/monitored-service/...` → Service Reliability module.
- `docs/continuous-delivery/armory/**` → legacy Armory/Spinnaker KB
  articles; excluded from citations.

## D.5 GitX docs absent from the corpus

The `platform/git-experience` docs subtree is not in `corpus/docs/`, so all
Git-backed-storage claims rest on spec fields (`storeType: INLINE, REMOTE,
INLINE_HC`, `git_details`) plus mentions in pipeline/input-set/trigger docs.
Open: branch-selection semantics for referenced entities, conflict handling,
bidirectional sync behavior. Also unexplained: what exactly `INLINE_HC`
means (the enum value appears only in PipelineExecutionSummary).

## D.6 Identifier regex inconsistencies (spec-internal)

- Secret identifiers allow `-`: `^[a-zA-Z_][0-9a-zA-Z_$-]{0,127}$` vs the
  canonical `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$` (Pipeline/Template/Connector).
- Environment Group identifiers disallow `$`:
  `^[a-zA-Z_][0-9a-zA-Z_]{0,127}$`.
- Connector `org`/`project` fields are patterned like *names*
  (`^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$` — allows spaces!) though they hold
  identifiers.

Ask: are these deliberate per-entity rules or spec drift? (The connector
org/project one smells like a spec bug — an org identifier with a space
seems unaddressable elsewhere.)

## D.7 Variable types: String-only API vs richer docs

`VariableDTO.type` enum is `String` only (`entity_schemas.md`), while stage
variable YAML documents `type: String ## String or Secret`
(docs/platform/pipelines/add-a-stage.md). Interpretation adopted in this
book: the account/org/project Variable *entity* is String-only; inline
pipeline/stage variables support Secret. Verify whether Number/Secret entity
variables exist behind flags or newer APIs.

## D.8 Template type lists disagree

Docs list template types: Step, Step Group, Stage, Pipeline, Deployment,
Monitored Service, Secrets Manager, Artifact Source
(docs/platform/templates/template.md). The API enum has: `Step, Stage,
Pipeline, CustomDeployment, MonitoredService, SecretManager`
(`entity_schemas.md`: TemplateResponse) — no Step Group or Artifact Source,
and "Deployment" maps to `CustomDeployment`. Ask which surface lags which.

## D.9 v1-beta API coverage is uneven

In the corpus, v1 (`/v1/...`) covers pipelines, input sets, executions,
services, environments + infrastructure, connectors, secrets, approvals,
gitx-webhooks — but **not** triggers, templates, freeze, delegates,
environment groups, service overrides, or overlay-specific input-set
operations (all `/pipeline/api`, `/template/api`, `/ng/api` only). Treat as
migration-in-progress; do not read entity boundaries off v1 coverage.

## D.10 Feature flags observed (beta surface area)

Features documented but gated the day this corpus froze — check your
account's flags before relying on them:

| Flag | Feature | Source |
|---|---|---|
| `PIPE_QUEUED_PIPELINE_OBSERVABILITY` | Executions Management (queue page) | executions-management.md |
| `PIE_INPUTSET_RBAC_PERMISSIONS` (+ `CDS_INPUT_SET_MIGRATION`) | Input set access control | input-sets.md |
| `CD_TRIGGERS_REFACTOR` | Artifact trigger doc's described behavior | trigger-on-a-new-artifact.md |
| `CDS_MANUAL_INTERVENTION_CUSTOM_ACTIONS` | Restrict manual-intervention actions | define-a-failure-strategy-on-stages-and-steps.md |
| `CDS_PIPELINE_ABORT_RBAC_PERMISSION` | Separate Abort permission | abort-pipeline.md |
| `CI_GIT_CLONE_CONTAINERLESS` | Host-side clone in VM/cloud infra | create-and-configure-a-codebase.md |
| `CI_ENABLE_MULTIPART` | >5 GB cache blobs multi-part upload | cache-intelligence.md |
| Test Intelligence JS (Jest) / Kotest | TI language support in beta | ti-overview.md |

## D.11 Trigger v2 endpoints, undocumented split

`/pipeline/api/triggers/v2` and `.../triggers/{triggerIdentifier}/v2` exist
alongside the unversioned trigger endpoints, plus a `yamlVersion` field on
NGTriggerResponse (path_tree.txt; entity_schemas.md). Nothing in the
corpus's docs explains the v2/yamlVersion split. Ask: is there a trigger
YAML v1→v2 migration underway, and which should new triggers use?

## D.12 Environment "type" vocabulary mismatch (minor)

Docs say environments are categorized "prod or non-prod"
(environment-overview.md); the API enum is `PreProduction, Production`
(EnvironmentRequest). Same concept, two vocabularies; the freeze YAML uses a
third (`EnvType` filter). Cosmetic, but worth knowing when querying.

## D.13 Where is stage-level CRUD for CD steps' rollback state?

Failure-strategy docs state rollback semantics "depend on the type of build
or deployment" (define-a-failure-strategy-on-stages-and-steps.md) but the
corpus doesn't document what state K8s rollback restores when multiple
releases share a namespace, or how `releaseName: release-<+INFRA_KEY_SHORT_ID>`
(environment-overview.md) interacts with rollback history. Ask the CD team
or test in a sandbox.

## D.14 Aggregate org/project APIs not in corpus

Org/Project CRUD endpoints (e.g. `/ng/api/organizations`,
`/ng/api/projects`) did not survive the pipeline-relevance filter; the scope
hierarchy is evidenced indirectly (path nesting, schema fields). No modeling
impact, but Appendix A.1–A.3 cite structure rather than CRUD docs.
