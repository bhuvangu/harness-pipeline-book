# Configuring the codebase

When you add the first Build stage to a pipeline, you specify where your
code is stored. This becomes the pipeline's default codebase, and each Build
stage clones it into the build environment before running steps.

The codebase is pipeline-level configuration:

```yaml
pipeline:
  ...
  properties:
    ci:
      codebase:
        connectorRef: YOUR_CODEBASE_CONNECTOR_ID
        build: <+input>     # branch, tag, or PR chosen at run time or by a trigger
```

For repositories in the Harness Code Repository module, use `repoName`
instead of a connector.

## To configure the default codebase

1. In the Pipeline Studio, select **Add Stage**, and then select **Build**.
2. Enter a stage name and make sure **Clone Codebase** is enabled.
3. Configure the codebase connection: select **Harness Code Repository**
   and a repo, or select **Third-party Git provider**, a code repository
   connector, and the repository name.
4. Select **Set Up Stage**.

To change the connector or other settings later, select **Codebase** in the
Pipeline Studio's right-side panel, or edit the `codebase` section in YAML.

## Controlling cloning

- To skip the automatic clone in a stage, set `cloneCodebase: false` in the
  stage spec. Do this when a stage doesn't need the source, or when you need
  custom clone behavior.
- A pipeline can clone additional repositories beyond the default codebase.
- Clone enhancements are available on the codebase and the Git Clone step:
  Git LFS, fetch tags, sparse checkout, submodules, a custom clone path, and
  pre-fetch commands.

## Why the codebase matters beyond cloning

- Webhook triggers require the pipeline to have a default codebase to listen
  on. See [Webhook triggers](../triggers/webhook-triggers.md).
- The resolved clone is described to your steps through built-in
  `<+codebase.*>` variables, such as the branch, commit, and PR number.
- Test Intelligence reads the codebase's commit and PR data to select tests.
  See [Test Intelligence](test-intelligence.md).

---
**Sources:** docs/continuous-integration/use-ci/codebase-configuration/create-and-configure-a-codebase.md
(default codebase, YAML, cloneCodebase, clone enhancements);
docs/platform/triggers/triggering-pipelines.md (trigger requires default
codebase); docs/continuous-integration/use-ci/codebase-configuration/built-in-cie-codebase-variables-reference.md.
