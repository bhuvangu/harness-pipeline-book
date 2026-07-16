# Delegates

The delegate is a service you run in your own network or VPC. It connects
your artifact repositories, infrastructure, and other providers with Harness
Manager, and it performs all operations, including deployments and
integrations.

## Connectivity model

The delegate connects out to Harness Manager over HTTPS and a secure
WebSocket channel. The channel carries heartbeats and task-event
notifications — not task data. The delegate sends a heartbeat every minute;
the delegate list shows Connected or Not Connected based on it.

Install the delegate behind your firewall, in the same network as the
systems it must reach. It needs network access to your artifact servers,
deployment targets, and cloud providers — Harness needs no inbound access to
your network.

## Installing and scoping

Delegates exist at account, organization, or project scope. Install them on
Kubernetes, Docker, or VMs using the manifests, Helm values, or Terraform
modules the API provides. Delegates authenticate with delegate tokens.
Choose a size for the expected load — resource needs vary by task type (for
example, Terraform tasks are memory-hungry).

## How tasks are assigned

When you don't pin delegates, Harness picks one by:

1. **Heartbeat** — delegates without a recent heartbeat aren't assigned.
2. **Tags** — delegate selectors, if any, filter the candidates.
3. **Capability check** — the delegate verifies connectivity to the target
   system before taking the task.

You can pin work to specific delegates with selectors on steps, stages,
pipelines, and connectors. Pinning is strict: if the selected delegates
can't perform the task, Harness does not fall back to others.

## When delegates are not involved

Harness Cloud build infrastructure runs on Harness-managed VMs; delegate
selectors are not applicable there. See
[Choosing a build infrastructure](../ci/build-infrastructure.md).

---
**Sources:** docs/platform/delegates/delegate-concepts/delegate-overview.md
(all behavior described);
docs/platform/delegates/secure-delegates/secure-delegates-with-tokens.md;
corpus/entity_schemas.md (DelegateSetupDetails size enum);
corpus/path_tree.txt (`/ng/api/download-delegates/...`,
`/ng/api/delegate-setup/...`);
docs/continuous-integration/use-ci/set-up-build-infrastructure/which-build-infrastructure-is-right-for-me.md
(Harness Cloud: selectors not applicable).
