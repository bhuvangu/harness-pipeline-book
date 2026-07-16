# Appendix C. Glossary

Harness term → definition → nearest industry equivalent. Definitions
compress the cited chapters/Appendix A sections; equivalents are the
author's mapping (treat as orientation, not identity).

| Harness term | Definition | Nearest industry equivalent |
|---|---|---|
| **Account** | Root scope owning all orgs, projects, and resources (A.1) | AWS Organization root / GitHub Enterprise account |
| **Organization** | Grouping scope under account (A.2) | AWS OU / GitHub organization |
| **Project** | Working scope holding pipelines and their callers (A.3) | GitLab project group / Azure DevOps project |
| **Pipeline** | YAML-defined workflow; aggregate of stages and steps (A.4, Ch 2) | Jenkins pipeline / GitHub Actions workflow |
| **Stage** | Typed major segment of a pipeline (Build, Deploy, Approval…) (A.5) | GitLab stage / Actions job (typed) |
| **Step** | Atomic action in a stage (A.6) | Actions step / Jenkins sh block |
| **Step Group** | Steps sharing settings/containers, can run parallel (A.7) | Actions composite step / Tekton task grouping |
| **Execution** | One run of a pipeline: plan + node graph + statuses (A.8, Ch 5) | Build/run instance (Jenkins build, Actions run) |
| **planExecutionId** | System id of an execution's compiled plan (Ch 5.1) | Run id |
| **Runtime input (`<+input>`)** | Declared parameter filled at run time (Ch 3.1) | Workflow input / parameterized build param |
| **Expression (`<+...>`)** | Value resolved from live pipeline context (Ch 3.1) | `${{ }}` contexts in Actions / Jenkins env vars |
| **Input Set** | Saved values for a pipeline's runtime inputs (A.9) | Saved parameter preset (no exact mainstream equivalent) |
| **Overlay Input Set** | Ordered, last-wins composition of input sets (A.10) | Layered config files (base + override) |
| **Trigger** | Rule starting a pipeline on webhook/cron/artifact events (A.11, Ch 4) | Actions `on:` block / Jenkins trigger |
| **Webhook (shared endpoint)** | One account-wide URL receiving all Git events (Ch 4.2) | Provider webhook endpoint |
| **Artifact trigger** | Polling-based trigger on new registry versions (Ch 4.4) | Registry webhook + deploy automation |
| **Approval** | Human/ticket gate pausing execution (A.13, Ch 5.8) | Actions environment approval / ServiceNow change gate |
| **Deployment Freeze** | Scheduled window blocking CD deployments per scope/rules (A.14) | Change moratorium / blackout window |
| **Build Infrastructure** | Where CI stage steps run: Cloud VM, K8s pod, VMs, local (A.15, Ch 6.1) | Hosted vs self-hosted runners |
| **Harness Cloud** | Harness-managed ephemeral build VMs (Ch 6.1) | GitHub-hosted runners |
| **Codebase** | Pipeline-level Git repo config cloned by CI stages (A.16) | Checkout config / SCM definition |
| **Test Intelligence (TI)** | Diff-based unit-test selection (A.18, Ch 6.4) | Predictive test selection (e.g. Bazel/TIA-style) |
| **Cache Intelligence** | Automatic dependency cache save/restore (A.19, Ch 6.5) | actions/cache with auto-detection |
| **Artifact (CI)** | Build output pushed to a registry / listed on Artifacts tab (A.20) | Build artifact |
| **Service** | What you deploy: manifests + artifact sources + variables (A.21, Ch 7.1) | Helm release definition / Spinnaker application-ish |
| **Service Definition** | The manifest/artifact/variable payload inside a Service (Ch 7.1) | Chart + values + image coordinates |
| **Environment** | Where you deploy; PreProduction or Production (A.22, Ch 7.2) | Deploy environment (Actions environments) |
| **Infrastructure Definition** | Concrete target in an environment (cluster+namespace…) (A.23) | Kubernetes context/namespace binding |
| **Environment Group** | Named set of environments for bulk targeting (A.24) | Environment tier grouping |
| **Service Override** | Per env(-service/-infra) config replacing service settings (A.25, Ch 7.3) | Per-env values files / kustomize overlays |
| **Rolling / Canary / Blue-Green** | Stage execution strategies (Ch 7.5) | Same industry terms |
| **Rollback steps** | Pre-declared mirror steps run on StageRollback (Ch 7.6) | Automated rollback hooks |
| **Connector** | Typed credentials + endpoint for an external system (A.26, Ch 8.2) | Jenkins credential+endpoint config / Terraform provider config |
| **connectorRef** | Scoped reference to a connector (`account.X`, `org.X`) (Ch 1.1) | Fully-qualified resource reference |
| **Secret** | Encrypted sensitive value referenced by expression (A.27) | Actions secret / Vault KV entry |
| **Secret Manager** | Backend storing/encrypting secrets (KMS or vault) (A.28, Ch 8.4) | KMS / Vault backend config |
| **Delegate** | Customer-run worker executing all tasks, outbound-only (A.29, Ch 8.1) | Self-hosted runner / GitLab runner + bastion role |
| **Delegate selector (tag)** | Pinning tasks to specific delegates (Ch 8.1) | Runner labels |
| **Template** | Versioned reusable step/stage/pipeline definition (A.30, Ch 9) | Actions reusable workflow / Jenkins shared library |
| **templateRef / templateInputs** | Link to a template + its declared arguments (Ch 9.2) | `uses:` + `with:` in Actions |
| **Stable version** | The template version auto-followed by linked pipelines (Ch 9.3) | Floating major tag (`@v2`) |
| **Variable** | Named value at account/org/project or pipeline/stage level (A.31, Ch 3.2) | CI/CD variables (GitLab), org/repo variables (Actions) |
| **GitX / Git Experience** | Storing entity YAML in Git (`storeType: REMOTE`) (Ch 1.4) | Config-as-code sync (e.g. JCasC, Actions-native files) |
| **Scope prefix (`org.` / `account.`)** | Upward cross-scope reference syntax (Ch 1.1) | Qualified naming across namespaces |
| **v1 beta vs legacy NG APIs** | Two REST generations over one entity domain (Ch 1.5) | API v1/v2 coexistence |
| **Manual intervention** | Pause-on-failure with human-chosen action (Ch 5.5) | Jenkins input step on failure |
| **Failure strategy** | Declarative error→action mapping per step/stage (Ch 5.6) | try/catch policy for pipelines |
| **Retry vs Rerun** | Resume failed execution vs fresh run with same inputs (Ch 5.7) | Re-run failed jobs vs re-run all |
| **Queued execution** | Admitted run waiting on constraints/concurrency/locks (Ch 5.4) | Runner queue / concurrency groups |
