# The Harness Pipeline Book

A domain-model book teaching the Harness pipeline offering (CI + CD) to an
experienced engineer joining the company. Written in the spirit of AWS
documentation: **User Guide chapters** that teach concepts and mental models,
backed by an **entity reference** with precise definitions, identity rules,
API tables, and citations.

Every factual claim cites its source in the frozen corpus (`../corpus/`):
doc paths under `docs/`, spec paths/schemas from `openapi_pipeline.yaml` /
`entity_schemas.md` / `path_tree.txt`, and example files from
`yaml_examples/`. Inferences are labeled INFERRED. The corpus froze
2026-07-16; no live API access was used (see Appendix D.2).

## How to read this book

- **New to Harness?** Read chapters 1–5 in order (the platform core), then
  chapter 6 or 7 depending on whether you land on CI or CD, then 8–10.
- **In a hurry?** Chapter 10 is the whole model as two narratives; each
  chapter ends with a *Mental model* box you can read standalone.
- **Looking something up?** Appendix A (entity reference), B (relationship
  diagrams), C (glossary), D (open questions / known ambiguities).

## Contents

| Chapter | What it teaches |
|---|---|
| [1. The resource model](01-resource-model.md) | Scopes, identifier vs name, YAML as the native form, inline vs Git storage, two API generations, adjacent modules |
| [2. The pipeline aggregate](02-pipeline-aggregate.md) | Pipeline > Stage > Step; stage types; YAML anatomy |
| [3. Parameterization](03-parameterization.md) | Runtime inputs, expressions, variables, input sets and overlays — pipeline as a function |
| [4. Triggers and events](04-triggers-and-events.md) | Webhook / cron / artifact triggers; conditions; payload binding |
| [5. Execution](05-execution.md) | The execution entity, plan and graph, statuses, queue, interrupts, failure strategies, retry vs rerun, approvals |
| [6. CI stages](06-ci-stages.md) | Build infrastructure trade-offs, codebase, CI step catalog, Test & Cache Intelligence, artifacts |
| [7. CD stages](07-cd-stages.md) | The Service / Environment / Infrastructure Definition triad, overrides, strategies, freeze, rollback |
| [8. The connectivity layer](08-connectivity-layer.md) | Delegates, connectors, secrets, secret managers — how SaaS reaches your infrastructure |
| [9. Reuse](09-reuse.md) | Templates, versioning, the stable pointer, template vs copy |
| [10. Life of a build, life of a deployment](10-life-of-a-pipeline.md) | Two end-to-end narratives naming all 31 entities |

| Appendix | Contents |
|---|---|
| [A. Entity reference](appendix-a-entity-reference.md) | Per-entity: definition, scopes, identity (quoted regexes), owns/owned-by, references, YAML, dual API tables, lifecycle, gotchas |
| [B. Relationship diagrams](appendix-b-relationships.md) | Scope hierarchy + ER diagrams, with a 28-row edge evidence table |
| [C. Glossary](appendix-c-glossary.md) | Harness term → definition → nearest industry equivalent |
| [D. Open questions](appendix-d-open-questions.md) | Doc-vs-spec conflicts, beta flags, corpus gaps — the week-one question list |

Working artifact: [entity-inventory.md](entity-inventory.md) — the reviewed
checkpoint-2 inventory this book was built from.
