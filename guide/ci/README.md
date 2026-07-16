# Building with CI stages

A CI (Build) stage builds and tests code and produces artifacts. Configuring
one comes down to three decisions: where the steps run (build
infrastructure), what code they run against (the codebase), and what work
they do (the steps). Harness adds two accelerators — Test Intelligence for
test selection and Cache Intelligence for dependency caching.

A key property of CI stages: all steps in a stage share one machine. On
Harness Cloud each stage runs on a fresh, ephemeral VM that terminates when
the stage completes; on a Kubernetes build infrastructure each stage runs in
a pod. Steps share the machine's filesystem, which is how they pass files to
each other. Use the stage's `sharedPaths` setting for locations outside the
default workspace.

```yaml
- stage:
    name: Build
    identifier: Build
    type: CI
    spec:
      cloneCodebase: true
      caching:
        enabled: true
      platform:
        os: Linux
        arch: Amd64
      runtime:
        type: Cloud        # Harness Cloud build infrastructure
        spec: {}
      execution:
        steps: [...]
```

## Topics

- [Choosing a build infrastructure](build-infrastructure.md)
- [Configuring the codebase](codebase.md)
- [CI steps](ci-steps.md)
- [Test Intelligence](test-intelligence.md)
- [Cache Intelligence](cache-intelligence.md)

---
**Sources:** docs/continuous-integration/use-ci/set-up-build-infrastructure/use-harness-cloud-build-infrastructure.md
(ephemeral VM per stage, shared filesystem);
docs/continuous-integration/use-ci/set-up-build-infrastructure/which-build-infrastructure-is-right-for-me.md
(K8s: stage per pod); yaml_examples/continuous-integration__use-ci__caching-ci-data__cache-intelligence.md.yaml
(stage YAML).
