# Webhook triggers

Webhook triggers start pipelines in response to Git events, such as a push
or a pull request, that match conditions you define. They are how you get
event-driven CI/CD: every commit building, every merge deploying.

## How webhook delivery works

All triggers in a Harness account share one webhook URL:
`https://app.harness.io/gateway/ng/api/webhook?accountIdentifier=ACCOUNT_ID`.
Every event delivered to that URL is evaluated against your triggers'
conditions. Because the URL doesn't select a pipeline, your conditions are
the only thing that determines which events start which pipelines. Configure
them carefully.

For supported Git providers, Harness registers the webhook in your
repository automatically. If automatic registration fails, or you use a
Custom trigger for an unsupported provider, copy the webhook URL from the
trigger and register it in the repository yourself. The trigger tracks its
registration status (`SUCCESS`, `FAILED`, `ERROR`, `TIMEOUT`,
`UNAVAILABLE`).

## Requirements

- The pipeline must have a default codebase for the trigger to listen on.
  See [Configuring the codebase](../ci/codebase.md).
- All Git providers except Custom and Harness Code require a code repository
  connector whose token can manage repository webhooks. For GitHub, the
  token owner must be a repository admin and the token needs the `repo`,
  `user`, and `admin:repo_hook` scopes.

## To add a webhook trigger to a pipeline

1. Go to your pipeline and select **Triggers** in the Pipeline Studio
   header.
2. Select **New Trigger**, and choose the trigger type for your SCM
   provider. For unsupported providers, choose **Custom**.
3. On the **Configuration** tab, enter a name, select the code repository
   connector, and select the **Event** and any **Actions**.
4. On the **Conditions** tab, add conditions to scope the trigger to the
   events you want (see the next section).
5. On the **Pipeline Input** tab, select an input set or provide runtime
   values.
6. Select **Create Trigger**. For supported providers, Harness registers
   the webhook in your repository; verify the registration status on the
   trigger.

## Events and conditions

You select an event (for GitHub: PullRequest, Push, IssueComment, or
Release) and optional actions, then add conditions on source branch, target
branch, changed files, headers, and payload fields.

Conditions are cumulative: the event payload must match all of them for the
trigger to fire. For OR or NOT logic, use a JEXL condition:

```
<+trigger.payload.pull_request.diff_url>.contains("triggerNgDemo")
  || <+trigger.payload.repository.owner.name> == "wings-software"
```

Reference payload fields as `<+eventPayload.repository.full_name>` in
condition attributes and `<+trigger.payload...>` or
`<+trigger.header['X-GitHub-Event']>` in expressions.

> **Tip**
> In a mono-repository, add a changed-files condition with a regular
> expression such as `payments/.*` so that only changes to the relevant
> directory start the pipeline.

## Loading remote pipelines from a branch or tag

If your pipeline and input sets are stored in Git, the trigger can select
which branch or tag to load them from using `pipelineBranchName` and
`inputSetBranchName`, including the `$tag:v1.0.0` syntax for tag-based
release workflows.

---
**Sources:** docs/platform/triggers/triggering-pipelines.md (all behavior
described, JEXL example quoted); corpus/entity_schemas.md
(GithubWebhookTriggerSpec event enum, NGTriggerDetailsResponseDTO
registrationStatus enum).
