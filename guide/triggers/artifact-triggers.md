# Artifact and manifest triggers

Artifact triggers start a pipeline when a new artifact version appears in a
registry — for example, deploying automatically every time a new image is
pushed to Docker Hub. Manifest triggers work the same way for Helm chart
versions.

Unlike webhook triggers, artifact triggers poll. A delegate-run polling job
checks the registry (about once per minute) and fires the trigger when it
collects a genuinely new version. Supported providers include Docker
Registry, ECR, GCR, Google Artifact Registry, ACR, Artifactory, Nexus3,
Amazon S3, Azure Artifacts, Jenkins, Bamboo, GitHub Package Registry, and
custom artifacts.

## Behavior to plan around

- **Existing versions don't fire the trigger.** When you create the trigger,
  Harness collects the tags that already exist but does not start the
  pipeline for them. Only versions pushed afterward fire it.
- **One deployment per polling window by default.** If several artifacts
  arrive in one window, one deployment runs with the last artifact
  collected. A default setting (Execute Triggers With All Collected
  Artifacts or Manifests) switches to one execution per artifact, without
  guaranteed ordering.
- **Don't trigger on floating tags such as `latest`.** The tag's metadata
  doesn't change when the image is re-pushed, so Harness detects nothing
  new and the trigger never fires.
- **Use lexically sortable version tags.** Docker lists tags in lexical
  order, so tags that sort by creation date ensure the most recently pushed
  image is the one deployed.
- **Allow 5–10 minutes after creating or updating a trigger** for the
  polling job to start. Disabling a trigger stops polling; re-enabling
  starts a new polling job.

> **Note**
> This trigger documentation is behind the `CD_TRIGGERS_REFACTOR` feature
> flag in the corpus. See
> [Known issues and open questions](../../api-reference/open-questions.md).

---
**Sources:** docs/platform/triggers/trigger-on-a-new-artifact.md (all
behavior described); corpus/entity_schemas.md (ArtifactTriggerSpec family,
AcrArtifactTriggerSpec connector_ref).
