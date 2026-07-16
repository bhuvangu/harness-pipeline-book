# CI steps

Build stages provide step types for running scripts, building and pushing
images, managing service dependencies, running tests, and using plugins.

## Run

The general-purpose step: run commands in a container image or directly on
the host machine.

```yaml
- step:
    type: Run
    name: Run pytest
    identifier: Run_pytest
    spec:
      connectorRef: YOUR_IMAGE_REGISTRY_CONNECTOR
      image: python:latest
      shell: Sh
      command: |-
        pip install -r requirements.txt
        pytest -v --cov --junitxml="result.xml"
```

## Build and Push

Build a container image and push it to a registry: Docker Hub, ACR, ECR,
GAR, JFrog, and others. The step authenticates through a registry connector.

## Background

Start long-lived services the stage's other steps depend on, such as a
database or a browser for integration tests. Background services run for
the life of the stage.

## Test

Run tests with Test Intelligence enabled. For more information, see
[Test Intelligence](test-intelligence.md).

## Plugin

Run Drone-style container plugins, including wrappers for GitHub Actions and
Bitrise steps. Plugin capabilities vary by build infrastructure — for
example, Bitrise steps require Harness Cloud. See
[Choosing a build infrastructure](build-infrastructure.md).

## Cache and data-sharing steps

Save and restore caches to S3 or GCS explicitly:

```yaml
- step:
    type: SaveCacheGCS
    identifier: SaveCachetoGCS_1
    spec:
      connectorRef: account.gcp
      bucket: ci_cache
      key: gcs-{{ checksum filePath1 }}
      sourcePaths: [directory1, directory2]
      archiveFormat: Tar
```

For automatic caching, use [Cache Intelligence](cache-intelligence.md)
instead.

## Surfacing artifacts

Build-and-push steps publish images through connectors. To list produced
files on the execution's Artifacts tab, use the
`artifact-metadata-publisher` plugin step. The v1 API also exposes artifacts
per execution
(`/v1/.../pipelines/{pipeline}/executions/{execution}/artifacts`).

Don't confuse this build-output artifact with a CD service's artifact
source, which is the registry coordinates of what you deploy. See
[Services](../cd/services.md).

---
**Sources:** docs/continuous-integration/use-ci/run-step-settings.md (Run
example); docs/continuous-integration/use-ci/prep-ci-pipeline-components.md
(step families);
docs/continuous-integration/use-ci/build-and-upload-artifacts/build-and-push/build-and-push-to-docker-registry.md;
docs/continuous-integration/use-ci/manage-dependencies/background-step-settings.md;
docs/continuous-integration/use-ci/use-drone-plugins/plugin-step-settings-reference.md;
yaml_examples/continuous-integration__use-ci__caching-ci-data__save-cache-in-gcs.md.yaml;
docs/continuous-integration/use-ci/build-and-upload-artifacts/artifacts-tab.md;
corpus/path_tree.txt.
