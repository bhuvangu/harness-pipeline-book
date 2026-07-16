# What is the Harness pipeline offering?

Harness pipelines are the CI/CD core of the Harness platform. You define a
pipeline as YAML, and Harness runs it: CI stages build and test your code on
managed or self-managed infrastructure, and CD stages deploy your services to
your environments using rolling, canary, or blue-green strategies.

You can start pipelines manually, on a schedule, from Git webhook events, or
when a new artifact version appears in a registry. Every run is recorded as
an execution that you can inspect, retry, or roll back.

The pipeline offering is one part of the Harness platform. Adjacent modules —
GitOps, Feature Flags, Security Testing Orchestration, Chaos Engineering,
Cloud Cost Management, Internal Developer Portal, Code Repository, and
others — are not covered in this guide, although two of them appear as
pipeline stage types (Feature Flag and Security Tests).

## How this guide is organized

Concept pages explain how pipelines work. Task-oriented pages cover
configuring inputs, starting pipelines, and managing runs. The CI and CD
sections cover the two stage families in depth. The Reference section holds
the precise, per-entity definitions that back every other page.

All content is derived from a frozen documentation and API corpus
(`../corpus/`, frozen 2026-07-16). Each page lists its sources at the
bottom. Statements marked INFERRED are the author's inference from
structure rather than a direct statement in the sources.

## Topics

- [Pipeline concepts](concepts/README.md)
  - [Scopes: account, organization, and project](concepts/scopes.md)
  - [Identifiers and names](concepts/identifiers.md)
  - [Pipeline structure: stages and steps](concepts/pipeline-structure.md)
  - [YAML and Git-backed storage](concepts/yaml-and-storage.md)
  - [The two API generations](concepts/api-generations.md)
- [Configuring pipeline inputs](inputs/README.md)
  - [Runtime inputs and expressions](inputs/runtime-inputs.md)
  - [Input sets and overlays](inputs/input-sets.md)
  - [Variables](inputs/variables.md)
- [Starting pipelines with triggers](triggers/README.md)
  - [Webhook triggers](triggers/webhook-triggers.md)
  - [Scheduled triggers](triggers/scheduled-triggers.md)
  - [Artifact and manifest triggers](triggers/artifact-triggers.md)
- [Managing executions](executions/README.md)
  - [Execution statuses and the execution graph](executions/statuses-and-graph.md)
  - [Failure handling](executions/failure-handling.md)
  - [Retrying and rerunning pipelines](executions/retry-and-rerun.md)
  - [Approvals](executions/approvals.md)
- [Building with CI stages](ci/README.md)
  - [Choosing a build infrastructure](ci/build-infrastructure.md)
  - [Configuring the codebase](ci/codebase.md)
  - [CI steps](ci/ci-steps.md)
  - [Test Intelligence](ci/test-intelligence.md)
  - [Cache Intelligence](ci/cache-intelligence.md)
- [Deploying with CD stages](cd/README.md)
  - [Services](cd/services.md)
  - [Environments and infrastructure definitions](cd/environments.md)
  - [Service overrides](cd/service-overrides.md)
  - [Deployment strategies and rollback](cd/strategies-and-rollback.md)
  - [Deployment freeze](cd/deployment-freeze.md)
- [Connecting to your infrastructure](connect/README.md)
  - [Delegates](connect/delegates.md)
  - [Connectors](connect/connectors.md)
  - [Secrets and secret managers](connect/secrets.md)
- [Reusing configuration with templates](reuse/templates.md)
- [Walkthroughs](walkthroughs/README.md)
  - [Life of a build](walkthroughs/life-of-a-build.md)
  - [Life of a deployment](walkthroughs/life-of-a-deployment.md)
## Companion document

Precise per-entity definitions, API tables, diagrams, and the glossary live
in a separate document, the
[API & Entity Reference](../api-reference/README.md) — the same split AWS
uses between a service's User Guide and its API Reference.
