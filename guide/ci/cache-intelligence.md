# Cache Intelligence

CI environments are ephemeral, so every run pays the cost of downloading
dependencies again. Cache Intelligence caches and restores software
dependencies automatically to speed up builds.

Enable it per stage:

```yaml
- stage:
    type: CI
    spec:
      caching:
        enabled: true
        paths:                      # optional custom cache paths
          - /harness/node_modules
      cloneCodebase: true
```

Cache Intelligence is enabled by default for newly created CI stages.

## Tool detection

Cache Intelligence detects Maven, Gradle, Bazel, Yarn, Go, Node, and .NET
build tools by looking for their dependency files (such as `pom.xml` or
`go.mod`) in the repository root and one directory below it, and caches
each tool's default dependency path. For deeper monorepo layouts,
unsupported tools, or non-default cache locations, set custom `paths`.

## Storage

On Harness Cloud, the cache is stored in Harness-managed storage: all
pipelines in the account share it, each build tool has its own cache key,
retention is 15 days (reset when a cache is updated), and old caches are
evicted automatically when you reach your plan's storage limit.

On self-managed build infrastructure, configure your own object storage —
S3, GCS, Azure Blob, or any S3-compatible store — as the default, with
per-stage overrides available.

---
**Sources:** docs/continuous-integration/use-ci/caching-ci-data/cache-intelligence.md
(all behavior described);
yaml_examples/continuous-integration__use-ci__caching-ci-data__cache-intelligence.md.yaml.
