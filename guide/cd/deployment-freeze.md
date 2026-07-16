# Deployment freeze

A deployment freeze blocks deployments during a scheduled window — for
example, a holiday change moratorium. You define a freeze window with rules
(which organizations, projects, services, and environments to freeze) and a
schedule (when, and how it recurs).

Freeze windows can be created at account, organization, or project scope. At
each scope, rules can select all subordinate entities with exceptions — for
example, all projects in an organization except one.

```yaml
freeze:
  name: example
  identifier: example
  entityConfigs:
    - name: myapp freeze
      entities:
        - type: Org
          filterType: All
        - type: Service
          filterType: All
        - type: EnvType
          filterType: All
  status: Disabled
  windows:
    - timeZone: America/Los_Angeles
      startTime: 2023-07-03 10:08 AM
      endTime: 2023-07-05 10:38 AM
```

## Behavior during a freeze

- **Freeze applies to CD stages only.** CI and other module stages in the
  same pipeline continue to run.
- **Running pipelines finish their current stage**, then stop. Executions
  stopped this way are marked "Aborted By Freeze."
- **Trigger invocations of frozen pipelines are rejected.** Custom webhook
  triggers can override a freeze if their API key has the freeze-override
  permission.
- **The API is frozen too.** You cannot start deployments on frozen entities
  through the API during the window.
- **Account admins can always bypass** freeze windows, and a Global freeze
  switch exists alongside scheduled windows.

## Managing freeze windows

You cannot edit an enabled freeze window. Disable it, make your changes,
then enable it again. Freeze access control has three permissions: Manage
(create/edit/delete), Override (deploy during a freeze), and Global
(enable/disable the global freeze).

---
**Sources:** docs/continuous-delivery/manage-deployments/deployment-freeze.md
(all behavior described);
yaml_examples/continuous-delivery__manage-deployments__deployment-freeze.md.yaml
(YAML); corpus/entity_schemas.md (FreezeResponse type/status/freezeScope
enums); corpus/path_tree.txt (`/ng/api/freeze/manageGlobalFreeze`).
