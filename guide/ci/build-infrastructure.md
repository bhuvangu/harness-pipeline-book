# Choosing a build infrastructure

You can run builds on Harness-managed machines (Harness Cloud) or on your
own infrastructure. The choice is made per stage.

| Option | Model | When to choose it |
|---|---|---|
| Harness Cloud | Each stage runs on a fresh Harness-managed VM with common tools preinstalled; the VM terminates after the stage | Default choice; zero infrastructure to maintain; new CI features arrive here first; consumes build credits |
| Kubernetes cluster | Each stage runs as a pod in your cluster; steps share the pod's resources | You already operate Kubernetes and want builds inside your network |
| AWS/GCP/Azure VMs | Self-managed VM fleets | More freedom with Docker, native Windows; paid plans |
| Local (Docker) runner | Builds on a single machine | Small-scale or special-hardware builds, such as legacy Windows apps |

## Platform support

| OS | Architecture | Harness Cloud | Local runner | Kubernetes | Cloud VMs |
|---|---|---|---|---|---|
| Linux | amd64, arm64 | Yes | Yes | Yes | Yes |
| macOS | arm64 | Yes (recommended) | Yes | No | Supported, not recommended |
| Windows | amd64 | Yes | Yes | Yes | Yes |
| Windows | arm64 | No | No | No | No |

Harness recommends Harness Cloud for macOS builds because of licensing
requirements and the complexity of managing macOS VMs with Anka
virtualization.

## Feature compatibility varies by infrastructure

When a CI feature doesn't work, check the compatibility matrix first.
Highlights:

- Build Intelligence: Harness Cloud and Kubernetes only, Linux only.
- Delegate selectors: not applicable on Harness Cloud; not supported on
  cloud VM infrastructure.
- Bring-your-own secret manager: not supported on Harness Cloud.
- Bitrise steps: Harness Cloud only.
- Test Intelligence, test splitting, Cache Intelligence, and S3/GCS caching:
  supported everywhere.

## Configuration

Harness Cloud uses `platform` plus `runtime: {type: Cloud}` on the stage.
A Kubernetes build infrastructure uses an `infrastructure` block of type
`KubernetesDirect` with a cluster connector and namespace, and runs through
a delegate. For more information, see
[Delegates](../connect/delegates.md).

---
**Sources:** docs/continuous-integration/use-ci/set-up-build-infrastructure/which-build-infrastructure-is-right-for-me.md
(comparison, OS/arch matrix, feature matrix, macOS recommendation);
docs/continuous-integration/use-ci/set-up-build-infrastructure/use-harness-cloud-build-infrastructure.md;
docs/continuous-integration/use-ci/set-up-build-infrastructure/k8s-build-infrastructure/set-up-a-kubernetes-cluster-build-infrastructure.md.
