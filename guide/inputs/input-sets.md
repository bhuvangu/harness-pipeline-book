# Input sets and overlays

Input sets are collections of runtime input values for a pipeline. Instead
of typing every value on the Run form, you select an input set that contains
the values for your scenario. Overlays combine several input sets into one
selection.

An input set belongs to exactly one pipeline, and it can only contain values
for settings the pipeline declares as `<+input>`. It doesn't have to be
complete — you can leave some fields for manual input or split values across
several sets.

## Input set YAML

An input set mirrors the pipeline's YAML shape, containing only the runtime
input fields:

```yaml
inputSet:
  name: My Input Set 1
  identifier: My_Input_Set
  orgIdentifier: default
  projectIdentifier: CD_Examples
  pipeline:
    identifier: YAML
    stages:
      - stage:
          identifier: Deploy
          type: Deployment
          spec:
            infrastructure:
              infrastructureDefinition:
                type: KubernetesDirect
                spec:
                  connectorRef: Kubernetes_Quickstart
                  namespace: default
```

## To create an input set

1. In the Pipeline Studio header, select **Input Sets**.
2. Select **New Input Set**.
3. Enter a **Name**. **Description** and **Tags** are optional.
4. Enter values for the settings that use runtime input, and then select
   **Save**. You can't define values for settings that aren't `<+input>`,
   and you don't have to provide a value for every input.

To capture a known-good set of values quickly, run the pipeline and choose
**Save as New Input Set** on the Run form. You can also import input sets
from a Git repository.

## Overlays

An overlay is an ordered list of input sets:

```yaml
overlayInputSet:
  name: My Overlay Set
  identifier: My_Overlay_Set
  pipelineIdentifier: YAML
  inputSetReferences:
    - My_Input_Set      # resolved first
    - My_Input_Set_2    # resolved last; wins on conflicts
```

### To create an overlay

1. Create the input sets you want to combine.
2. On the **Input Sets** page, select **New Input Set**, and then select
   **Overlay Input Set**.
3. Enter a **Name**, select the input sets to include, and select
   **Apply Input Sets**.
4. Drag the input sets into the order in which they should resolve, and
   select **Save**.

Input sets are resolved in order. A later set replaces values that earlier
sets defined and fills values they left empty. The final value of any
setting is the value assigned by the last input set that defines it.

A common pattern is one input set with shared defaults used by every run,
plus one input set per service or scenario, combined per run in an overlay.

## Using input sets with triggers

When a trigger supplies pipeline input, you can use an input set or provide
runtime values directly, but not both. To override a few values on top of an
input set, use the trigger's override-YAML configuration. For more
information, see [Starting pipelines with triggers](../triggers/README.md).

## Access control

Input sets support View, Create/Edit, and Delete permissions. To run a
pipeline with an input set, you need View on the input set and Execute on
the pipeline. (This is feature-flagged; see
[Known issues and open questions](../../api-reference/open-questions.md).)

---
**Sources:** docs/platform/pipelines/input-sets.md (all behavior described);
yaml_examples/platform__pipelines__harness-yaml-quickstart.md.yaml
(examples 20 and 22); corpus/path_tree.txt
(`/v1/.../input-sets/merge`, `/pipeline/api/inputSets/overlay`).
