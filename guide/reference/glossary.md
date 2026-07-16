# Glossary

Harness term → definition → nearest industry equivalent. Definitions compress the guide pages and the
[Entity reference](entity-reference.md); equivalents are the author's
mapping (treat as orientation, not identity).

| Harness term | Definition | Nearest industry equivalent |
|---|---|---|
| **Account** | Root scope owning all orgs, projects, and resources | AWS Organization root / GitHub Enterprise account |
| **Organization** | Grouping scope under account | AWS OU / GitHub organization |
| **Project** | Working scope holding pipelines and their callers | GitLab project group / Azure DevOps project |
| **Pipeline** | YAML-defined workflow; aggregate of stages and steps | Jenkins pipeline / GitHub Actions workflow |
| **Stage** | Typed major segment of a pipeline (Build, Deploy, Approval…) | GitLab stage / Actions job (typed) |
| **Step** | Atomic action in a stage | Actions step / Jenkins sh block |
| **Step Group** | Steps sharing settings/containers, can run parallel | Actions composite step / Tekton task grouping |
| **Execution** | One run of a pipeline: plan + node graph + statuses | Build/run instance (Jenkins build, Actions run) |
| **planExecutionId** | System id of an execution's compiled plan | Run id |
| **Runtime input (`<+input>`)** | Declared parameter filled at run time | Workflow input / parameterized build param |
| **Expression (`<+...>`)** | Value resolved from live pipeline context | `${{ }}` contexts in Actions / Jenkins env vars |
| **Input Set** | Saved values for a pipeline's runtime inputs | Saved parameter preset (no exact mainstream equivalent) |
| **Overlay Input Set** | Ordered, last-wins composition of input sets | Layered config files (base + override) |
| **Trigger** | Rule starting a pipeline on webhook/cron/artifact events | Actions `on:` block / Jenkins trigger |
| **Webhook (shared endpoint)** | One account-wide URL receiving all Git events | Provider webhook endpoint |
| **Artifact trigger** | Polling-based trigger on new registry versions | Registry webhook + deploy automation |
| **Approval** | Human/ticket gate pausing execution | Actions environment approval / ServiceNow change gate |
| **Deployment Freeze** | Scheduled window blocking CD deployments per scope/rules | Change moratorium / blackout window |
| **Build Infrastructure** | Where CI stage steps run: Cloud VM, K8s pod, VMs, local | Hosted vs self-hosted runners |
| **Harness Cloud** | Harness-managed ephemeral build VMs | GitHub-hosted runners |
| **Codebase** | Pipeline-level Git repo config cloned by CI stages | Checkout config / SCM definition |
| **Test Intelligence (TI)** | Diff-based unit-test selection | Predictive test selection (e.g. Bazel/TIA-style) |
| **Cache Intelligence** | Automatic dependency cache save/restore | actions/cache with auto-detection |
| **Artifact (CI)** | Build output pushed to a registry / listed on Artifacts tab | Build artifact |
| **Service** | What you deploy: manifests + artifact sources + variables | Helm release definition / Spinnaker application-ish |
| **Service Definition** | The manifest/artifact/variable payload inside a Service | Chart + values + image coordinates |
| **Environment** | Where you deploy; PreProduction or Production | Deploy environment (Actions environments) |
| **Infrastructure Definition** | Concrete target in an environment (cluster+namespace…) | Kubernetes context/namespace binding |
| **Environment Group** | Named set of environments for bulk targeting | Environment tier grouping |
| **Service Override** | Per env(-service/-infra) config replacing service settings | Per-env values files / kustomize overlays |
| **Rolling / Canary / Blue-Green** | Stage execution strategies | Same industry terms |
| **Rollback steps** | Pre-declared mirror steps run on StageRollback | Automated rollback hooks |
| **Connector** | Typed credentials + endpoint for an external system | Jenkins credential+endpoint config / Terraform provider config |
| **connectorRef** | Scoped reference to a connector (`account.X`, `org.X`) | Fully-qualified resource reference |
| **Secret** | Encrypted sensitive value referenced by expression | Actions secret / Vault KV entry |
| **Secret Manager** | Backend storing/encrypting secrets (KMS or vault) | KMS / Vault backend config |
| **Delegate** | Customer-run worker executing all tasks, outbound-only | Self-hosted runner / GitLab runner + bastion role |
| **Delegate selector (tag)** | Pinning tasks to specific delegates | Runner labels |
| **Template** | Versioned reusable step/stage/pipeline definition | Actions reusable workflow / Jenkins shared library |
| **templateRef / templateInputs** | Link to a template + its declared arguments | `uses:` + `with:` in Actions |
| **Stable version** | The template version auto-followed by linked pipelines | Floating major tag (`@v2`) |
| **Variable** | Named value at account/org/project or pipeline/stage level | CI/CD variables (GitLab), org/repo variables (Actions) |
| **GitX / Git Experience** | Storing entity YAML in Git (`storeType: REMOTE`) | Config-as-code sync (e.g. JCasC, Actions-native files) |
| **Scope prefix (`org.` / `account.`)** | Upward cross-scope reference syntax | Qualified naming across namespaces |
| **v1 beta vs legacy NG APIs** | Two REST generations over one entity domain | API v1/v2 coexistence |
| **Manual intervention** | Pause-on-failure with human-chosen action | Jenkins input step on failure |
| **Failure strategy** | Declarative error→action mapping per step/stage | try/catch policy for pipelines |
| **Retry vs Rerun** | Resume failed execution vs fresh run with same inputs | Re-run failed jobs vs re-run all |
| **Queued execution** | Admitted run waiting on constraints/concurrency/locks | Runner queue / concurrency groups |
