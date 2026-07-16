# Identifiers and names

Every Harness entity has two labels. The identifier is the machine address:
it appears in URLs, references, and expressions, and it cannot change after
the entity is saved. The name is the human display label, and you can change
it at any time.

| | Identifier | Name |
|---|---|---|
| Used for | Addressing: URLs, `*Ref` fields, expressions | Display |
| Mutability | Immutable once saved | Mutable |
| Pattern | `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$` | `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$` |
| Uniqueness | Unique within its scope | Not used as identity |

When you create an entity in the UI, Harness generates the identifier from
the name. You can edit it during creation only.

Because triggers, input sets, templates, and expressions all address
entities by identifier, an immutable identifier is what keeps those
references stable while teams rename things freely.

## Per-entity variations

A few entities use slightly different patterns. Patterns are quoted from the
API schema digest:

- Secret identifiers also allow hyphens: `^[a-zA-Z_][0-9a-zA-Z_$-]{0,127}$`.
- Environment group identifiers do not allow `$`:
  `^[a-zA-Z_][0-9a-zA-Z_]{0,127}$`.
- Connector names do not require a leading letter: `^[0-9a-zA-Z-_ ]{0,127}$`.

For the identity rules of each entity, see the
[Entity reference](../reference/entity-reference.md). For known
inconsistencies in these patterns, see
[Known issues and open questions](../reference/open-questions.md).

---
**Sources:** corpus/entity_schemas.md (PipelineCreateRequestBody, Secret,
EnvironmentGroupRequest, Connector — patterns quoted verbatim);
docs/platform/pipelines/add-a-stage.md ("once the stage is saved, the Id
becomes immutable. You can change the Name at any time").
