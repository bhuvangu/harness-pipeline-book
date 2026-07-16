# Entity schema digest (from OpenAPI spec)

## AbstractServiceLevelObjective
> This is the Service Level Objective V2 entity defined in Harness
- required: identifier, name, sloTarget, spec, type, userJourneyRefs
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string
- `name`: string
- `description`: string
- `tags`: object
- `userJourneyRefs`: array
- `sloTarget`: obj
- `type`: string; enum: Simple, Composite
- `spec`: obj
- `notificationRuleRefs`: array
- `errorBudgetCalculationPeriod`: integer
- `errorBudgetCalculationValidity`: integer

## AccessKeySecretKey
- required: secretKeyIdentifier
- `accessKey`: string
- `accessKeySecretIdentifier`: string
- `accessKeySecretSpaceId`: integer
- `accessKeySecretSpacePath`: string
- `secretKeyIdentifier`: string
- `secretKeySpaceId`: integer
- `secretKeySpacePath`: string

## AcrArtifactTriggerSpec
- `connector_ref`: string
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `subscription_id`: string
- `repository`: string
- `tag`: string
- `registry`: string

## ActiveMonitoredService
> This is details of the Active Service Monitored entity defined in Harness.
- required: identifier
- `identifier`: string
- `monitoredServiceCount`: integer
- `name`: string
- `orgName`: string
- `envNames`: array
- `projectName`: string
- `accountIdentifier`: string
- `module`: string
- `timestamp`: integer

## ActiveServiceMonitoredFilterParams
> Active Services Monitored Filter Params
- `orgIdentifier`: string
- `projectIdentifier`: string
- `serviceIdentifier`: string

## ActivityExecutionInputDTO
> Input value for an activity execution
- required: name, value, type
- `name`: string
- `value`: obj
- `type`: obj

## ActivityTriggerInfo
> Trigger information for an activity
- `identifier`: string
- `name`: string
- `email`: string

## AmazonMachineImageArtifactTriggerSpec
- `connector_ref`: string
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `region`: string
- `tags`: array
- `filters`: array
- `version`: string
- `version_regex`: string

## AmazonS3ArtifactTriggerSpec
- `connector_ref`: string
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `region`: string
- `bucket_name`: string
- `file_path_regex`: string

## AnsibleVariable
> AnsibleVariable is the representation for a single variable associated with ansible.
- required: key, value, value_type
- `file_name`: string
- `key`: string; pattern `^[a-zA-Z0-9_]+$`; maxLen 128
- `uuid`: string
- `value`: string
- `value_type`: string

## AnthropicConnector
> This contains details of the Anthropic connector
- required: authentication

## AppDynamicsConnectorDTO
- required: accountname, controllerUrl

## AppdynamicsClientIdConnectorSpec
> This contains details of the appdynamics connector with client secrets

## AppdynamicsConnectorSpec
> This contains details of the appdynamics connector

## Approval
- required: account, org, project, pipeline_execution_id, pipeline_stage_id, workspace_id
- `account`: string; maxLen 128
- `org`: string; maxLen 128
- `pipeline_execution_id`: string
- `pipeline_stage_id`: string
- `project`: string; maxLen 128
- `status`: string; enum: pending, approved, rejected
- `workspace_id`: string

## ApprovalAction
- `id`: integer
- `status`: string; enum: APPROVED, REJECTED

## ApprovalEvent
- `id`: integer
- `category`: string
- `cloud_account_id`: string
- `account_id`: string
- `evaluated_at`: string
- `metadata`: object

## ApprovalEventSummary
- `savings_potential`: number
- `event_count`: integer
- `event_type`: string
- `event_status`: string

## ApprovalEventV2
- `id`: integer
- `category`: string
- `cloud_account_id`: string
- `cloud_account_name`: string
- `account_id`: string
- `evaluated_at`: string
- `status`: string; enum: PENDING, COMPLETED, EXPIRED, REJECTED
- `potential_savings`: number
- `potential_spend`: number
- `name`: string
- `metadata`: object

## ApprovalEventsSuccessResponse
- `ts`: integer
- `success`: boolean
- `errors`: string
- `response`: object

## ApprovalIdentifier
- required: account, org, project, id, pipeline_execution_id, pipeline_stage_id, workspace_id
- `account`: string; maxLen 128
- `id`: string
- `org`: string; maxLen 128
- `project`: string; maxLen 128

## ApprovalInfo
- `approved_by`: string
- `approved_at`: string
- `status`: string

## ApprovalInfoDTO
- required: approvedBy, approvedAt
- `approvedBy`: obj
- `approvedAt`: integer
- `comments`: string

## ApprovalInstanceDetailsDTO

## ApprovalInstanceResponse
> This contains details of Approval Instance response
- required: details, id, status, type
- `id`: string
- `type`: string; enum: HarnessApproval, JiraApproval, CustomApproval, ServiceNowApproval
- `status`: string; enum: WAITING, APPROVED, REJECTED, FAILED, ABORTED, EXPIRED
- `deadline`: integer
- `details`: obj
- `createdAt`: integer
- `lastModifiedAt`: integer
- `errorMessage`: string
- `approvedByCurrentUser`: boolean
- `rejectedByCurrentUser`: boolean

## ApprovalInstanceResponseBody
> Response body for Approval Instance
- `id`: string
- `type`: string; enum: HarnessApproval, JiraApproval, CustomApproval, ServiceNowApproval
- `status`: string; enum: WAITING, APPROVED, REJECTED, FAILED, ABORTED, EXPIRED
- `deadline`: integer
- `created`: integer
- `updated`: integer
- `error_message`: string
- `details`: object

## ApprovalOverviewSuccessResponse
- `ts`: integer
- `success`: boolean
- `errors`: string
- `response`: object

## ApprovalPayload
- `actions`: array

## ApprovalResourceCollection

## ApprovalServiceAccount
> Service Account details used in Approvals.
- required: identifier
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string

## ApprovalUpdate
> ApprovalUpdate defines the fields of an approval step that can be updated
- required: account, org, project, id, status, pipeline_execution_id, pipeline_stage_id, workspace_id
- `account`: string; maxLen 128
- `actioned_by`: string
- `actioned_by_email`: string
- `id`: string
- `org`: string; maxLen 128
- `project`: string; maxLen 128
- `status`: string; enum: approved, rejected, pending

## ApprovalUserGroup
> User Group details used in Approvals.
- required: identifier, name
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string
- `name`: string

## ApprovalsCreateApprovalResponseBodyCreation
> Create-ApprovalResponseBody result type (creation view)
- required: id
- `id`: string

## ApprovalsListRequestV2
- `pagination`: object
- `service`: string
- `statuses`: array
- `cloud_account_id`: string
- `event_types`: array
- `regions`: array

## ApprovalsListResponseV2
- `ts`: integer
- `success`: boolean
- `errors`: array
- `response`: object

## ApprovalsOverviewRequestFilters
- `regions`: array
- `cloud_account_ids`: array
- `service`: string; enum: Amazon Elastic Compute Cloud - Compute, Amazon Relational Database Service

## ApprovalsShowApprovalResponseBodyStatusInfo
> Show-ApprovalResponseBody result type (statusInfo view)
- required: status, created, updated
- `actioned_by`: string
- `actioned_by_email`: string
- `created`: integer
- `status`: string
- `updated`: integer

## ApprovePipelineExecutionRequestBody
- required: approvalID, action
- `action`: string; enum: APPROVE, REJECT
- `approvalID`: string
- `message`: string

## ArtifactListingPipelineRequestBody
- `search_term`: string
- `artifact_type`: string; enum: image, repository

## ArtifactListingPipelineResponse
- `org_id`: string
- `project_id`: string
- `pipeline_id`: string
- `pipeline_execution_id`: string
- `artifact`: obj
- `orchestration`: obj
- `enforcement`: obj
- `slsa`: obj
- `verification`: obj

## ArtifactModelPipeline
- `id`: string
- `type`: string; enum: image, repository
- `name`: string
- `registry_url`: string
- `variant`: obj
- `tag`: string
- `digest`: string
- `metadata`: object
- `source_id`: string

## ArtifactTriggerSource

## ArtifactTriggerSpec
> Spec for Artifact Triggers
- `type`: obj

## ArtifactoryAnonymousConnectorSpec
> This contains details of the artifactory connector with anonymous user

## ArtifactoryConnector
> This entity contains the details of the Artifactory Connectors
- required: artifactoryServerUrl

## ArtifactoryConnectorSpec
> This contains details of the artifactory connector with username/password

## ArtifactoryEncryptedConnectorSpec
> This contains details of the artifactory connector with encrypted username/password

## ArtifactoryRegistryArtifactTriggerSpec
- `connector_ref`: string
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `artifact_directory`: string
- `artifact_path`: string
- `repository`: string
- `repository_format`: string
- `repository_url`: string
- `artifact_filter`: string

## AssociatedTemplate
> AssociatedTemplate defines the template details with template_id and version.
- `template_id`: string; maxLen 128
- `version`: string; maxLen 64

## AsyncChainExecutableResponse
- `unknownFields`: obj
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `statusValue`: integer
- `status`: string; enum: NO_OP, RUNNING, INTERVENTION_WAITING, TIMED_WAITING, ASYNC_WAITING, TASK_WAITING, DISCONTINUING, PAUSING, QUEUED, SKIPPED, PAUSED, ABORTED
- `timeout`: integer
- `callbackIdsList`: array
- `callbackId`: string
- `callbackIdsCount`: integer
- `chainEnd`: boolean
- `passThroughData`: obj
- `logKeysList`: array
- `logKeysCount`: integer
- `unitsList`: array
- `unitsCount`: integer
- `callbackIdBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## AsyncChainExecutableResponseOrBuilder
- `statusValue`: integer
- `status`: string; enum: NO_OP, RUNNING, INTERVENTION_WAITING, TIMED_WAITING, ASYNC_WAITING, TASK_WAITING, DISCONTINUING, PAUSING, QUEUED, SKIPPED, PAUSED, ABORTED
- `timeout`: integer
- `callbackIdsList`: array
- `callbackId`: string
- `callbackIdsCount`: integer
- `chainEnd`: boolean
- `passThroughData`: obj
- `logKeysList`: array
- `logKeysCount`: integer
- `unitsList`: array
- `unitsCount`: integer
- `callbackIdBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## AsyncExecutableResponse
- `unknownFields`: obj
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `statusValue`: integer
- `status`: string; enum: NO_OP, RUNNING, INTERVENTION_WAITING, TIMED_WAITING, ASYNC_WAITING, TASK_WAITING, DISCONTINUING, PAUSING, QUEUED, SKIPPED, PAUSED, ABORTED
- `timeout`: integer
- `callbackIdsList`: array
- `callbackIdsCount`: integer
- `logKeysList`: array
- `logKeysCount`: integer
- `unitsList`: array
- `unitsCount`: integer
- `shouldRemoveAlreadyProcessedNotifyIds`: boolean
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## AsyncExecutableResponseOrBuilder
- `statusValue`: integer
- `status`: string; enum: NO_OP, RUNNING, INTERVENTION_WAITING, TIMED_WAITING, ASYNC_WAITING, TASK_WAITING, DISCONTINUING, PAUSING, QUEUED, SKIPPED, PAUSED, ABORTED
- `timeout`: integer
- `callbackIdsList`: array
- `callbackIdsCount`: integer
- `logKeysList`: array
- `logKeysCount`: integer
- `unitsList`: array
- `unitsCount`: integer
- `shouldRemoveAlreadyProcessedNotifyIds`: boolean
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## AuditEnvironment
> List of Environments
- required: identifier, type
- `type`: string; enum: PreProduction, Production
- `identifier`: string

## Auto Approval
> This contains details of the Auto Approval
- required: action, scheduledDeadline
- `scheduledDeadline`: obj
- `action`: string; enum: APPROVE
- `comments`: string

## AutoExecuteOnScheduleProperty
> Automatically execute releases when their scheduled time arrives

## AwsAccessKeyConnectorSpec
> This contains details of the AWS connector and needs AWS access and secret keys for an AWS IAM user.

## AwsCodeCommitConnector
> This contains details of the AWS Code Commit connector
- required: authentication, type, url

## AwsCodeCommitConnectorSpec
> This contains details of the AWS code commit connector

## AwsCodeCommitSecretKeyAccessKey
> This contains details of the AWS Code Commit secret references
- required: secretKeyRef

## AwsCodeCommitWebhookSpec

## AwsCodeCommitWebhookTriggerSpec
- `type`: string; enum: Push
- `spec`: obj

## AwsConnector
> This contains details of the AWS connector
- required: credential

## AwsEncryptedAccessKeyConnectorSpec
> This contains details of the AWS connector and needs AWS encrypted access and secret keys for an AWS IAM user.

## AwsIAMRoleConnectorSpec
> This contains details of the AWS connector. This assume IAM role on Delegate and uses the IAM role of a Harness Delegate running in your AWS account.

## AwsIRSAConnectorSpec
> This contains details of the AWS connector. This uses IRSA and forces the Harness kubernetes delegate in AWS EKS to use a specific IAM role.

## AwsKmsAccessKeyConnectorSpec
> This contains details of the AWS and needs AWS encrypted access and secret keys for the AWS KMS.

## AwsKmsAssumeIAMConnectorSpec
> This contains details of the AWS connector and Harness will authenticate using the IAM role assigned to the AWS host running the Delegate, you select using a Delegate Selector.

## AwsKmsAssumeSTSConnectorSpec
> This contains details of the AWS connector and Harness will authenticate using the IAM role assigned to the AWS host running the Delegate, you select using a Delegate Selector.

## AwsKmsConnector
> This has configuration details for the AWS KMS Secret Manager.
- required: credential, region

## AwsKmsConnectorCredential
> Returns the configuration details for the AWS KMS Secret Manager.
- required: type
- `type`: string; enum: AssumeIAMRole, AssumeSTSRole, ManualConfig, OidcAuthentication
- `spec`: obj

## AwsOidcTokenExchangeDetailsForDelegate
- `oidcIdToken`: string
- `idTokenExpiryTime`: integer

## AwsSecretManager
> Returns AWS Secret Manager configuration details.
- required: credential, region

## AwsSecretManagerAccessKeyConnectorSpec
> This contains details of the AWS and needs AWS encrypted access and secret keys for the AWS Secret Manager.

## AwsSecretManagerAssumeIAMConnectorSpec
> This contains details of the AWS connector and Harness will authenticate using the IAM role assigned to the AWS host running the Delegate, you select using a Delegate Selector.

## AwsSecretManagerAssumeSTSConnectorSpec
> This contains details of the AWS connector and Harness will authenticate using the STS role assigned to the AWS host running the Delegate, you select using a Delegate Selector.

## AwsSecretManagerCredential
> This contains the credential type and configuration of the AWS Secret Manager.
- required: type
- `type`: string; enum: AssumeIAMRole, AssumeSTSRole, ManualConfig, OidcAuthentication
- `spec`: obj

## AwsSecretManagerCredentialSpec
> This is interface that returns credentials specific to all roles for the AWS Secret Manager.

## AzureArtifactsArtifactTriggerSpec
- `connector_ref`: string
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `project`: string
- `package_name`: string
- `package_type`: string
- `feed`: string
- `version`: string
- `version_regex`: string

## AzureArtifactsConnector
> This contains details of AzureArtifacts connector
- required: auth, azureArtifactsUrl

## AzureClientCertificateConnectorSpec
> This contains details of the Azure connector and uses Azure client certificate details

## AzureClientSecretKey
> This contains azure client secret key details
- required: secretRef

## AzureClientSecretKeyConnectorSpec
> This contains details of the Azure connector and uses Azure client secret key details

## AzureConnector
> This contains details of the Azure connector
- required: azureEnvironmentType, credential

## AzureInheritFromDelegateDetails
> This contains Azure inherit from delegate credentials connector details
- required: auth

## AzureInheritFromDelegateSystemAssignedManagedIdentityConnectorSpec
> This contains details of the Azure connector for contains azure MSI auth details

## AzureInheritFromDelegateUserAssignedManagedIdentityConnectorSpec
> This contains details of the Azure connector and for azure UserAssigned MSI auth details

## AzureKeyVaultConnector
> Returns configuration details for the Azure Key Vault Secret Manager.
- required: subscription, vaultName

## AzureRepoWebhookSpec

## AzureRepoWebhookTriggerSpec
- `connector_ref`: string
- `repo_name`: string
- `header_conditions`: array
- `payload_conditions`: array
- `jexl_condition`: string
- `auto_abort_previous_executions`: boolean
- `type`: string; enum: PullRequest, Push, IssueComment

## BackfillTriggerDataV3
> Response payload returned when a backfill is successfully triggered.
- required: jobId
- `jobId`: integer

## BackfillTriggerRequestInputV3
> Request body for triggering an ES search backfill.
- required: entityTypes
- `entityTypes`: array
- `reindexAll`: boolean

## BackstageEnvConfigVariable

## BackstageEnvSecretVariable

## BackstageEnvVariable
> Backstage Env Variable
- required: env_name, type
- `identifier`: string
- `env_name`: string
- `created`: integer
- `updated`: integer
- `type`: string; enum: Config, Secret

## BackstageEnvVariableBatchRequest
- required: env_variables
- `env_variables`: array

## BackstageEnvVariableRequest
- `env_variable`: obj

## BackstageEnvVariableResponse
- required: env_variable
- `env_variable`: obj

## BambooArtifactTriggerSpec
- `connector_ref`: string
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `plan_key`: string
- `build`: string
- `artifact_paths`: array

## BambooConnector
> Bamboo Connector details.
- required: bambooUrl

## BaselineExecutions
- required: executionIds
- `executionIds`: array

## BatchInputSetsAPIRequest
- `pipelineIdentifiers`: array

## BatchRollbackRequestDTO
- required: targets
- `targets`: array

## BatchRollbackResponseDTO
- `results`: array
- `totalRollbacksTriggered`: integer
- `totalRollbacksFailed`: integer

## BitbucketConnector
> This contains details of Bitbucket connectors
- required: authentication, type, url

## BitbucketWebhookSpec

## BitbucketWebhookTriggerSpec
- `connector_ref`: string
- `repo_name`: string
- `header_conditions`: array
- `payload_conditions`: array
- `jexl_condition`: string
- `auto_abort_previous_executions`: boolean
- `type`: string; enum: PullRequest, Push, PRComment

## BulkInputSetsAPIRequest
- required: inputSetIdentifiers
- `inputSetIdentifiers`: array

## BulkInputSetsAPIResponse
- `inputSets`: array

## CEAwsConnector
> This contains the cost explorer of AWS connector
- required: featuresEnabled

## CEAzureConnector
> This contains the cost explorer of Azure connector
- required: featuresEnabled, subscriptionId, tenantId

## CICDHarnessPipelineYamlResponseBody
- required: pipeline_yaml
- `pipeline_yaml`: string
- `harness_pipeline_settings`: obj

## CIExecutionInfoDTO
- `event`: string
- `pullRequest`: obj

## CVNGRollbackSpec

## CVNGWebhookChannelSpec

## CatalogConnectorInfo
> Details of IDP catalog connector
- required: connector, repo, branch, path
- `connector`: obj
- `repo`: string
- `branch`: string
- `path`: string

## CfService
> A Harness service linked to a flag
- required: name, identifier
- `identifier`: string
- `name`: string

## ChildChainExecutableResponse
- `unknownFields`: obj
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `passThroughData`: obj
- `lastLink`: boolean
- `suspend`: boolean
- `nextChildIdBytes`: obj
- `previousChildId`: string
- `previousChildIdBytes`: obj
- `nextChildId`: string
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## ChildChainExecutableResponseOrBuilder
- `passThroughData`: obj
- `lastLink`: boolean
- `suspend`: boolean
- `nextChildIdBytes`: obj
- `previousChildId`: string
- `previousChildIdBytes`: obj
- `nextChildId`: string
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## ChildExecutableResponse
- `unknownFields`: obj
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `childNodeId`: string
- `skip`: boolean
- `logKeysList`: array
- `logKeysCount`: integer
- `unitsList`: array
- `unitsCount`: integer
- `childNodeIdBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## ChildExecutableResponseOrBuilder
- `childNodeId`: string
- `skip`: boolean
- `logKeysList`: array
- `logKeysCount`: integer
- `unitsList`: array
- `unitsCount`: integer
- `childNodeIdBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## ChildExecutionDetail
> This contains the Pipeline Execution details of Child Pipeline
- `pipelineExecutionSummary`: obj
- `executionGraph`: obj

## ChildrenExecutableResponse
- `unknownFields`: obj
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `maxConcurrency`: integer
- `shouldProceedIfFailed`: boolean
- `childrenCount`: integer
- `logKeysList`: array
- `logKeysCount`: integer
- `unitsList`: array
- `unitsCount`: integer
- `childrenOrBuilderList`: array
- `childrenList`: array
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## ChildrenExecutableResponseOrBuilder
- `maxConcurrency`: integer
- `shouldProceedIfFailed`: boolean
- `childrenCount`: integer
- `logKeysList`: array
- `logKeysCount`: integer
- `unitsList`: array
- `unitsCount`: integer
- `childrenOrBuilderList`: array
- `childrenList`: array
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## CommandExecutionStatus

## CommitmentService
- required: name, is_enabled, coverage, target_coverage, annualized_savings
- `name`: string
- `is_enabled`: boolean
- `coverage`: number
- `target_coverage`: number
- `annualized_savings`: string
- `approval_mode`: string
- `pending_actions_count`: integer
- `atomization_enabled`: boolean

## ComplianceArtifactWithExecution
- required: name, type, compliance_id, severity, standards, tags
- `url`: string
- `name`: string
- `type`: string
- `compliance_id`: string
- `title`: string
- `severity`: obj
- `description`: string
- `remediation`: string
- `standards`: array
- `tags`: array
- `updatedAt`: string
- `status`: obj
- `executions`: array
- `reason`: string
- `occurrences`: array
- `scan_type`: obj

## ComplianceExecutionByType
- `type`: obj
- `count`: integer
- `passed`: integer
- `failed`: integer

## CompositeServiceLevelObjectiveSpec
- required: serviceLevelObjectivesDetails

## ConfluenceConnector
> Confluence Connector details.
- required: apiAccessType

## Connector
- required: name, identifier, spec
- `name`: string; pattern `^[0-9a-zA-Z-_ ]{0,127}$`
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `description`: string
- `org`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`
- `project`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`
- `tags`: object
- `spec`: obj

## Connector1
- required: name, identifier
- `name`: string; pattern `^[0-9a-zA-Z-_ ]{0,127}$`
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `description`: string
- `org`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`
- `project`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`
- `tags`: object

## Connector2
> This is the view of Connector entity as defined in Harness.
- `connector`: obj

## ConnectorActivityDetails
> This contains details of any kind of activities corresponding to the Connector.
- `lastActivityTime`: integer

## ConnectorCatalogueItem
> This has details of the Connector Catalogue in Harness.
- `category`: string; enum: CLOUD_PROVIDER, SECRET_MANAGER, CLOUD_COST, ARTIFACTORY, CODE_REPO, MONITORING, TICKETING, DATABASE, COMMUNICATION, DOCUMENTATION, ML_OPS, MCP
- `connectors`: array

## ConnectorCatalogueResponse
> This has details of the retrieved Connector Catalogue.
- `catalogue`: array

## ConnectorConfig
> This is the view of the ConnectorConfig entity defined in Harness
- required: connectorType
- `connectorType`: string

## ConnectorConnectivityDetail
> This has details of the connectivity status of the Connector.
- `status`: string; enum: SUCCESS, PARTIAL, FAILURE, UNKNOWN
- `errors`: array
- `error_summary`: string
- `tested_at`: integer
- `connected_at`: integer

## ConnectorConnectivityDetails
> Details of the connectivity status of the Connector.
- `status`: string; enum: SUCCESS, FAILURE, PARTIAL, UNKNOWN, PENDING
- `errorSummary`: string
- `errors`: array
- `testedAt`: integer
- `lastTestedAt`: integer
- `lastConnectedAt`: integer

## ConnectorDetails
> Connector details containing identifier and type
- required: identifier, type
- `identifier`: string
- `type`: string; enum: Github, Gitlab, Bitbucket, AzureRepo

## ConnectorFilterProperties
> Properties of the Connector Filter defined in Harness
- `connectorNames`: array
- `connectorIdentifiers`: array
- `description`: string
- `types`: array
- `categories`: array
- `connectivityStatuses`: array
- `inheritingCredentialsFromDelegate`: boolean
- `connectorConnectivityModes`: array
- `tags`: object
- `filterType`: string; enum: Connector

## ConnectorInfo
> This has the Connector details defined in Harness
- required: identifier, name, spec, type
- `name`: string
- `identifier`: string
- `description`: string
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `tags`: object
- `type`: string; enum: K8sCluster, Git, Splunk, AppDynamics, Prometheus, Dynatrace, Vault, AzureKeyVault, DockerRegistry, Local, AwsKms, GcpKms
- `spec`: obj

## ConnectorInfoDTO
- `name`: string
- `identifier`: string
- `description`: string
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `type`: string
- `spec`: object
- `uniqueId`: string
- `parentUniqueId`: string

## ConnectorInfoRequest
- `connector_details`: obj

## ConnectorInfoResponse
- required: connector_details
- `connector_details`: obj

## ConnectorInputVariable
> Input variable for connector type
- required: type, metadata
- `type`: string; enum: connector
- `description`: string
- `default`: string
- `metadata`: obj

## ConnectorMetadata
- required: type
- `type`: string

## ConnectorPermissions
- required: canDelete
- `canDelete`: boolean

## ConnectorRequest
- required: connector
- `connector`: obj

## ConnectorResponse
> Connector response model
- `connector`: obj
- `created`: integer
- `updated`: integer
- `status`: obj
- `harness_managed`: boolean
- `governance_metadata`: object

## ConnectorResponse1
> This has the Connector details along with its metadata.
- `connector`: obj
- `createdAt`: integer
- `lastModifiedAt`: integer
- `status`: obj
- `activityDetails`: obj
- `harnessManaged`: boolean
- `gitDetails`: obj
- `entityValidityDetails`: obj
- `governanceMetadata`: obj
- `isFavorite`: boolean

## ConnectorSettings

## ConnectorSpec
> Details of the connector defined in Harness
- required: type
- `type`: string; enum: GitHttp, GitHttpEncrypted, GitSsh, Appdynamics, AppdynamicsClientId, Artifactory, ArtifactoryEncrypted, ArtifactoryAnonymous, AzureClientSecretKey, AzureClientCertificate, AzureInheritFromDelegateUserAssignedManagedIdentity, AzureInheritFromDelegateSystemAssignedManagedIdentity

## ConnectorStatistics
> This has the count for all Connector Types and Status defined in Harness
- `typeStats`: array
- `statusStats`: array

## ConnectorStatusStats
> Count of Connectors grouped by status.
- `status`: string; enum: SUCCESS, FAILURE, PARTIAL, UNKNOWN, PENDING
- `count`: integer

## ConnectorTestConnectionErrorDetail
> Connector test connection errors and their details.
- `reason`: string
- `message`: string
- `code`: integer

## ConnectorTestConnectionResponse
> This has test connection details for the Connector defined in Harness.
- `status`: string; enum: SUCCESS, PARTIAL, FAILURE, UNKNOWN
- `errors`: array
- `error_summary`: string
- `tested_at`: integer
- `delegate_id`: string

## ConnectorTypeStats
> Count of Connectors grouped by type.
- `type`: string; enum: K8sCluster, Git, Splunk, AppDynamics, Prometheus, Dynatrace, Vault, AzureKeyVault, DockerRegistry, Local, AwsKms, GcpKms
- `count`: integer

## ConnectorValidationResult
> This has validation details for the Connector defined in Harness.
- `status`: string; enum: SUCCESS, FAILURE, PARTIAL, UNKNOWN, PENDING
- `errors`: array
- `errorSummary`: string
- `testedAt`: integer
- `delegateId`: string
- `taskId`: string

## CountGroupedOnService
- `serviceReference`: string
- `serviceName`: string
- `count`: integer
- `executionCountGroupedOnStatusList`: array
- `executionCountGroupedOnArtifactList`: array

## CountServiceDTO
- `allServicesCount`: integer
- `servicesAtRiskCount`: integer

## CreateApprovalRequest
- required: pipeline_execution_id, pipeline_stage_id, workspace_id
- `pipeline_execution_id`: string
- `pipeline_stage_id`: string
- `status`: string; enum: pending, approved, rejected
- `workspace_id`: string

## CreateExecutionRequest
- required: pipeline_execution_id, pipeline_stage_id, workspace, pipeline
- `pipeline`: string
- `pipeline_execution_id`: string
- `pipeline_stage_id`: string
- `workspace`: string

## CreateExecutionResponse
- required: status, created, account, org, project, pipeline_execution_id, pipeline_stage_id, workspace, pipeline
- `account`: string; maxLen 128
- `created`: integer
- `org`: string; maxLen 128
- `pipeline`: string
- `pipeline_execution_id`: string
- `pipeline_stage_id`: string
- `project`: string; maxLen 128
- `status`: string; enum: none, success, failure
- `workspace`: string

## CreateGitXWebhookRequest
> Contains information about the GitX webhook creation request
- `webhook_identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`
- `repo_name`: string
- `connector_ref`: string
- `folder_paths`: array
- `webhook_name`: string; pattern `^[0-9a-zA-Z-_ ]{0,127}$`

## CreateGitXWebhookResponse
> Contains information about the GitX webhook creation 
- `webhook_identifier`: string

## CreateModuleExecutionRequest
- required: account, pipeline_org, pipeline_project, pipelineExecutionId, pipelineStageId, pipeline
- `account`: string
- `module_onboarding`: boolean
- `pipeline`: string
- `pipeline_org`: string
- `pipeline_project`: string
- `pipelineExecutionId`: string
- `pipelineStageId`: string

## CreateModuleExecutionResponse
- required: org, project, status, created, account, pipeline_org, pipeline_project, pipelineExecutionId, pipelineStageId, moduleId, pipeline
- `account`: string
- `created`: integer
- `metadata`: obj
- `module_onboarding`: boolean
- `moduleId`: string
- `org`: string
- `project`: string
- `status`: string

## CreateOnboardingPipelineRequest
- required: org, project
- `org`: string; maxLen 128
- `project`: string; maxLen 128

## CreateOrchestrationActivityInputSetRequestType
> Type of input set store. It helps in segregating the type of input set store.

## CreateRemoteExecutionRequest
- required: id, pipeline_execution_id, pipeline_execution_url, created, updated, executed, sha256_checksum
- `custom_arguments`: object

## CreateRemoteExecutionResponse
- required: account, org, project, id, workspace, pipeline_execution_id, pipeline_execution_url, created, updated, executed, sha256_checksum
- `account`: string; maxLen 128
- `created`: integer
- `custom_arguments`: object
- `executed`: boolean
- `id`: string
- `org`: string; maxLen 128
- `pipeline_execution_id`: string
- `pipeline_execution_url`: string
- `project`: string; maxLen 128
- `sha256_checksum`: string
- `updated`: integer
- `workspace`: string

## CreateRuleExecutionFilterDTO
- `policyExecutionFilter`: obj

## CreateTestingPipelineRequest
- required: pipeline_org, pipeline_project
- `pipeline_org`: string
- `pipeline_project`: string
- `type`: string

## CreateVariableSetRequestAccScope
- required: identifier, name
- `connectors`: array
- `created`: integer
- `description`: string
- `environment_variables`: object
- `id`: integer
- `identifier`: string; pattern `^[^/?#\s]+$`; maxLen 128
- `name`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `updated`: integer

## CreateVariableSetRequestOrgScope
- required: identifier, name
- `connectors`: array
- `created`: integer
- `description`: string
- `environment_variables`: object
- `id`: integer
- `identifier`: string; pattern `^[^/?#\s]+$`; maxLen 128
- `name`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `updated`: integer

## CreateVariableSetRequestProjScope
- required: identifier, name
- `connectors`: array
- `created`: integer
- `description`: string
- `environment_variables`: object
- `id`: integer
- `identifier`: string; pattern `^[^/?#\s]+$`; maxLen 128
- `name`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `updated`: integer

## CreateWebhookRequest
> Contains information about the webhook creation request
- required: webhook_identifier, webhook_name, spec
- `webhook_identifier`: string; pattern `^[0-9a-zA-Z-_ ]{0,127}$`
- `webhook_name`: string
- `spec`: obj

## CreateWebhookResponse
> Contains information about the webhook creation 
- `webhook_identifier`: string

## CreateWorkspaceVariableRequest
- required: key, value, value_type, kind
- `key`: string; pattern `^[a-zA-Z0-9_]+$`; maxLen 128
- `kind`: string; enum: env, tf
- `value`: string
- `value_type`: string; enum: string, secret

## CreateWorkspaceVariableResponse
- required: account, org, project, workspace, key, value, value_type, kind, created, updated
- `account`: string; maxLen 128
- `created`: integer
- `key`: string; pattern `^[a-zA-Z0-9_]+$`; maxLen 128
- `kind`: string; enum: env, tf
- `org`: string; maxLen 128
- `policy_evaluation`: obj
- `project`: string; maxLen 128
- `updated`: integer
- `value`: string
- `value_type`: string; enum: string, secret
- `workspace`: string

## CronScheduledTriggerSpec
> Spec for Cron Scheduled Triggers
- `type`: string
- `expression`: string

## CustomArtifactTriggerSpec
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `version`: string
- `script`: string
- `artifacts_array_path`: string
- `version_path`: string
- `metadata`: object
- `inputs`: array

## CustomDeploymentVariableProperties
- required: fqn, variableName
- `fqn`: string
- `variableName`: string
- `localName`: string
- `aliasFqn`: string
- `visible`: boolean

## CustomDeploymentVariableResponseDTO
- required: metadataMap, yaml
- `yaml`: string
- `metadataMap`: object

## CustomHealthConnectorDTO
- required: baseURL, method

## CustomHttpConnector
> This contains details of the CustomHttp connector for universal HTTP-based integrations
- required: authentication, baseUrl

## CustomNotificationTemplateDTO
- `template_ref`: string
- `version_label`: string
- `variables`: array

## CustomPagePipelineExecutionOutline
> This is the custom page implementation
- `content`: array
- `currentSize`: integer
- `lastSeenExecutionId`: string
- `lastSeenStartTime`: integer
- `hasMore`: boolean

## CustomSecretManager
> This contains details of Custom Secret Manager connectors
- required: template

## CustomWebhookSpec

## CustomWebhookTriggerSpec
- `header_conditions`: array
- `payload_conditions`: array
- `jexl_condition`: string

## CvEnvironmentResponse
- `environment`: obj
- `createdAt`: integer
- `lastModifiedAt`: integer
- `entityValidityDetails`: obj
- `governanceMetadata`: obj

## CvResponseDTOListEnvironmentResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: array
- `metaData`: object
- `correlationId`: string

## CvResponseDTOListServiceResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: array
- `metaData`: object
- `correlationId`: string

## CvServiceResponse
- `service`: obj
- `createdAt`: integer
- `lastModifiedAt`: integer
- `entityValidityDetails`: obj
- `governanceMetadata`: obj

## DashboardPipelineExecution
> This is the view of the Pipeline Executions for given Time Interval presented in day wise format
- `pipelineExecutionInfoList`: array

## DatadogConnectorDTO
- required: apiKeyRef, applicationKeyRef, url

## DefaultPipelineCollection

## DefaultPipelineIdentifier
- required: account, org, project, provisioner, operation
- `account`: string
- `operation`: string; enum: plan, apply, destroy, drift, synth, diff, deploy, remediation
- `org`: string
- `project`: string
- `provisioner`: string; enum: terraform, opentofu, terragrunt, awscdk
- `workspace`: string

## DefaultPipelineOverride
> Per-workspace override to the assigned default pipelines.
- `project_pipeline`: string
- `workspace_pipeline`: string

## DelegateConnectionDetails
- `uuid`: string
- `version`: string
- `lastHeartbeat`: integer
- `lastGrpcHeartbeat`: integer

## DelegateDeleteResponse
- `responseMsg`: string

## DelegateDownloadRequest
- required: name
- `name`: string
- `description`: string
- `size`: string; enum: LAPTOP, SMALL, MEDIUM, LARGE, CCM_SMALL
- `tags`: array
- `tokenName`: string
- `clusterPermissionType`: string; enum: CLUSTER_ADMIN, CLUSTER_VIEWER, NAMESPACE_ADMIN
- `customClusterNamespace`: string

## DelegateEventNotificationParamsDTO

## DelegateFilterPropertiesDTO
> Properties to filter delegates
- required: filterType
- `status`: string; enum: CONNECTED, DISCONNECTED, ENABLED, WAITING_FOR_APPROVAL, DISABLED, DELETED
- `description`: string
- `hostName`: string
- `delegateName`: string
- `delegateType`: string
- `delegateGroupIdentifier`: string
- `delegateTags`: array
- `delegateInstanceFilter`: string; enum: EXPIRED, AVAILABLE
- `autoUpgrade`: string
- `versionStatus`: string; enum: EXPIRED, EXPIRING, UNSUPPORTED, ACTIVE
- `runner`: boolean
- `tags`: object
- `filterType`: string; enum: Connector, Secret, DelegateProfile, Delegate, PipelineSetup, PipelineExecution, Deployment, Audit, Template, Trigger, EnvironmentGroup, FileStore

## DelegateGroupDTO
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `name`: string
- `identifier`: string
- `tags`: array

## DelegateGroupDetails
- `groupId`: string
- `delegateGroupIdentifier`: string
- `delegateType`: string
- `groupName`: string
- `delegateDescription`: string
- `delegateConfigurationId`: string
- `groupImplicitSelectors`: object
- `groupCustomSelectors`: array
- `lastHeartBeat`: integer
- `connectivityStatus`: string
- `activelyConnected`: boolean
- `grpcActive`: boolean
- `delegateInstanceDetails`: array
- `tokenActive`: boolean
- `autoUpgrade`: string; enum: ON, OFF, DETECTING
- `delegateGroupExpirationTime`: integer
- `delegateVersion`: string
- `upgraderLastUpdated`: integer
- `immutable`: boolean
- `groupVersion`: string
- `isUnsupported`: boolean
- `delegateGroupVersionStatus`: string; enum: EXPIRED, EXPIRING, UNSUPPORTED, ACTIVE
- `delegateVersionStatusInstanceLevelCount`: obj
- `ztsDetails`: obj
- `unsupported`: boolean

## DelegateGroupInner
- `uuid`: string
- `lastHeartbeat`: integer
- `activelyConnected`: boolean
- `hostName`: string
- `tokenActive`: boolean
- `version`: string
- `delegateExpirationTime`: integer
- `polllingModeEnabled`: boolean
- `connections`: array
- `delegateInstanceVersionStatus`: string; enum: EXPIRED, EXPIRING, UNSUPPORTED, ACTIVE
- `runner`: boolean
- `disabled`: boolean
- `ztsDetails`: obj

## DelegateGroupListing
- `delegateGroupDetails`: array
- `delegateVersionStatusAggregatedCount`: obj
- `autoUpgradeOffCount`: integer

## DelegateGroupTags
- `tags`: array

## DelegateInfo
- `id`: string
- `name`: string
- `taskId`: string
- `taskName`: string

## DelegateListResponse
- `type`: string
- `name`: string
- `description`: string
- `tags`: array
- `lastHeartBeat`: integer
- `connected`: boolean
- `delegateReplicas`: array
- `autoUpgrade`: string; enum: ON, OFF, DETECTING
- `legacy`: boolean
- `orgName`: string
- `projectName`: string

## DelegateReplica
- `uuid`: string
- `lastHeartbeat`: integer
- `connected`: boolean
- `hostName`: string
- `version`: string
- `expiringAt`: integer
- `status`: string
- `runner`: boolean

## DelegateSetupDetails
- required: delegateType, name
- `orgIdentifier`: string
- `projectIdentifier`: string
- `name`: string
- `description`: string
- `size`: string; enum: LAPTOP, SMALL, MEDIUM, LARGE, CCM_SMALL
- `hostName`: string
- `delegateConfigurationId`: string
- `identifier`: string
- `k8sConfigDetails`: obj
- `tags`: array
- `delegateType`: string
- `tokenName`: string
- `runAsRoot`: boolean
- `version`: string

## DelegateTokenDetails
- `uuid`: string
- `accountId`: string
- `name`: string
- `createdBy`: obj
- `createdByNgUser`: obj
- `createdAt`: integer
- `status`: string; enum: ACTIVE, REVOKED
- `value`: string
- `ownerIdentifier`: string
- `parentUniqueId`: string
- `revokeAfter`: integer

## DelegateVersionStatusInstanceLevelCount
- `counts`: object

## DeleteDefaultPipelineRequest
- required: provisioner, operation
- `operation`: string; enum: plan, apply, destroy, drift, synth, diff, deploy, remediation
- `provisioner`: string; enum: terraform, opentofu, terragrunt, awscdk
- `workspace`: string

## DeleteGitXWebhookResponse
> Contains information about the GitX webhooks that was deleted.
- `webhook_identifier`: string

## DeploymentPipeline
- required: identifier
- `identifier`: string
- `inputset`: string
- `type`: string
- `variables`: object

## DestroyWorkspaceVariableResponse
- `policy_evaluation`: obj

## DockerConnector
> Docker Connector details.
- required: dockerRegistryUrl, providerType

## DockerRegistryArtifactTriggerSpec
- `connector_ref`: string
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `tag`: string
- `image_path`: string

## DynamicPipelineExecuteRequestBody
> Please provide input Pipeline YAML, which needs to be executed.
- `yaml`: string

## DynatraceConnectorDTO

## ELKConnectorDTO
- required: url

## EcrArtifactTriggerSpec
- `connector_ref`: string
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `region`: string
- `image_path`: string
- `tag`: string
- `registry_id`: string

## EnforcementModelPipeline
- `enforcement_id`: string
- `stage_identifier`: string
- `stage_execution_identifier`: string
- `stage_name`: string
- `step_identifier`: string
- `step_name`: string
- `step_execution_identifier`: string
- `violations`: object

## EntityReferredByPipelineSetupUsageDetail

## EnumWebhookExecutionResult

## EnumWebhookParent

## EnumWebhookTrigger

## Environment
> This is the Environment entity defined in Harness
- required: identifier, name
- `account`: string; maxLen 128
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `org`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `project`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `harness_version`: string
- `yaml`: string

## Environment1
- `identifier`: string
- `type`: obj

## Environment2
- required: spec, apiVersion, identifier, name, kind
- `apiVersion`: string
- `identifier`: string
- `kind`: string
- `metadata`: obj
- `name`: string
- `orgIdentifier`: string
- `owner`: string
- `projectIdentifier`: string
- `scope`: string
- `spec`: obj
- `type`: string

## EnvironmentBatchResponse
> Response for batch environment creation with partial success support
- `successful`: array
- `failed`: array
- `totalRequested`: integer
- `totalSuccessful`: integer
- `totalFailed`: integer

## EnvironmentBlueprint
- required: spec, apiVersion, identifier, name, kind
- `apiVersion`: string
- `identifier`: string
- `kind`: string; enum: EnvironmentBlueprint
- `metadata`: obj
- `name`: string
- `orgIdentifier`: string
- `owner`: string
- `projectIdentifier`: string
- `scope`: string
- `spec`: obj
- `type`: string

## EnvironmentBlueprintMetadata
- `version`: string

## EnvironmentBlueprintSpec
- required: entities
- `entities`: array
- `inputs`: object
- `outputs`: object
- `ownedBy`: array

## EnvironmentConfig
- required: spec, apiVersion, identifier, name, kind
- `apiVersion`: string
- `identifier`: string
- `kind`: string; enum: EnvironmentConfig
- `metadata`: obj
- `name`: string
- `orgIdentifier`: string
- `owner`: string
- `projectIdentifier`: string
- `scope`: string
- `spec`: obj
- `type`: string

## EnvironmentConfigOptions
- required: inputs, entities
- `entities`: object
- `inputs`: object

## EnvironmentConfigSpec
- `config`: object
- `entities`: object

## EnvironmentCreateRequest
> Environment Request Body 
- required: identifier, name, type
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `type`: obj
- `color`: string
- `harness_version`: string
- `yaml`: string

## EnvironmentDTO
- required: identifier
- `identifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string

## EnvironmentDashboardDTO
- required: name, identifier, serviceInfo, type, infraInfo, scope
- `name`: string
- `identifier`: string
- `projectIdentifier`: string
- `orgIdentifier`: string
- `serviceInfo`: array
- `infraInfo`: object
- `infrastructures`: array
- `clusters`: array
- `scope`: string; enum: account, project, org, unknown
- `type`: obj

## EnvironmentFailureResponse
> Failed environment creation/update details with complete scope information
- required: accountId, errorMessage, identifier, status
- `accountId`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `errorCode`: string; enum: DEFAULT_ERROR_CODE, INVALID_ARGUMENT, INVALID_EMAIL, DOMAIN_NOT_ALLOWED_TO_REGISTER, COMMNITY_EDITION_NOT_FOUND, DEPLOY_MODE_IS_NOT_ON_PREM, USER_ALREADY_REGISTERED, USER_INVITATION_DOES_NOT_EXIST, USER_DOES_NOT_EXIST, USER_INVITE_OPERATION_FAILED, USER_DISABLED, ACCOUNT_DOES_NOT_EXIST
- `errorMessage`: string

## EnvironmentGitUpdateResponse
> Contains info about environment that is updated.
- `identifier`: string

## EnvironmentGroup
> This is the view of Environment Group Entity defined in Harness
- `envGroup`: obj
- `createdAt`: integer
- `lastModifiedAt`: integer

## EnvironmentGroupDelete
> This is the view of Environment Group Delete Response defined in Harness
- `deleted`: boolean
- `accountId`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string

## EnvironmentGroupRequest
> This is the EnvironmentGroupRequest entity defined in Harness
- required: yaml
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_]{0,127}$`
- `color`: string
- `yaml`: string

## EnvironmentGroupResponse
> This is the Environment Group Entity defined in Harness
- `accountId`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string
- `name`: string
- `description`: string
- `color`: string
- `deleted`: boolean
- `tags`: object
- `envIdentifiers`: array
- `envResponse`: array
- `yaml`: string
- `gitDetails`: obj

## EnvironmentIdentifierResponse
- required: identifier
- `identifier`: string
- `name`: string

## EnvironmentImportResponseDetails
> Details of Imported Environment.
- `envIdentifier`: string
- `governanceMetadata`: obj

## EnvironmentInfo
- required: identifier, name, type
- `identifier`: string
- `name`: string
- `type`: obj

## EnvironmentInputVariable
> Input variable for environment type
- required: type
- `type`: string; enum: environment
- `description`: string
- `default`: object
- `metadata`: obj

## EnvironmentMetadata
- required: deploymentType
- `deploymentType`: obj

## EnvironmentMoveConfigResponse
> Tells us if the environment move config operation was successful or not
- `identifier`: string
- `success`: boolean

## EnvironmentOutput
- required: value
- `description`: string
- `type`: string; enum: string, integer, number, object, boolean, array
- `value`: obj

## EnvironmentOverrides
- required: config, entities
- `config`: object
- `entities`: object

## EnvironmentPerspective
- required: environmentId, perspectiveId, perspectiveIdentifier, createdAt, updatedAt
- `createdAt`: integer
- `environmentId`: string
- `perspectiveId`: string
- `perspectiveIdentifier`: string
- `updatedAt`: integer

## EnvironmentProxyCreateRequest
> Information Environment to be created in catalog - environment name, identifier, owner, blueprint identifier, overrides
- required: environment_name, environment_identifier, owner, environment_blueprint_identifier, environment_blueprint_version, overrides
- `environment_name`: string
- `environment_identifier`: string
- `owner`: string
- `environment_blueprint_identifier`: string
- `environment_blueprint_version`: string
- `based_on_identifier`: string
- `overrides`: string
- `target_state`: obj; enum: running, inactive, paused
- `inputs`: string
- `type`: string
- `tags`: array
- `description`: string

## EnvironmentProxyUpdateRequest
- `environment_blueprint_version`: string
- `based_on_identifier`: string
- `overrides`: string
- `target_state`: obj; enum: running, inactive, paused
- `inputs`: string

## EnvironmentRequest
> This is the Environment entity defined in Harness
- required: type
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string
- `tags`: object
- `name`: string
- `description`: string
- `color`: string
- `type`: string; enum: PreProduction, Production
- `yaml`: string

## EnvironmentResponse
> Default response when a environment is returned
- `environment`: obj
- `created`: integer
- `updated`: integer

## EnvironmentResponse1
- `environment`: obj
- `createdAt`: integer
- `lastModifiedAt`: integer
- `entityValidityDetails`: obj
- `governanceMetadata`: obj

## EnvironmentResponseDetails
> This is the Environment entity defined in Harness
- `accountId`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string
- `name`: string
- `description`: string
- `color`: string
- `type`: string; enum: PreProduction, Production
- `deleted`: boolean
- `tags`: object
- `yaml`: string

## EnvironmentSpec
- required: environmentBlueprint, targetState, overrides
- `basedOn`: obj
- `config`: obj
- `environmentBlueprint`: obj
- `overrides`: obj
- `ownedBy`: array
- `targetState`: obj

## EnvironmentType

## EnvironmentType1

## EnvironmentType2

## EnvironmentTypeFilter

## EnvironmentUpdateRequest
> Environment Update Request Body 
- required: identifier, name, type
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `type`: obj
- `color`: string
- `harness_version`: string
- `yaml`: string

## ErrorTrackingConnectorDTO
- required: apiKeyRef, url

## ExecutableResponse
- `unknownFields`: obj
- `task`: obj
- `children`: obj
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `asyncOrBuilder`: obj
- `childOrBuilder`: obj
- `childrenOrBuilder`: obj
- `childChainOrBuilder`: obj
- `taskOrBuilder`: obj
- `taskChainOrBuilder`: obj
- `syncOrBuilder`: obj
- `skipTaskOrBuilder`: obj
- `asyncChainOrBuilder`: obj
- `facilitatorOrBuilder`: obj
- `responseCase`: string; enum: ASYNC, CHILD, CHILDREN, CHILDCHAIN, TASK, TASKCHAIN, SYNC, SKIPTASK, ASYNCCHAIN, FACILITATOR, RESPONSE_NOT_SET
- `async`: obj
- `child`: obj
- `childChain`: obj
- `taskChain`: obj
- `sync`: obj
- `skipTask`: obj
- `asyncChain`: obj
- `facilitator`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## ExecuteLlmAuthoringPipelineRequestBody
- required: conversationId, schemaId, instanceId, changeset
- `changeset`: string
- `conversationId`: string
- `instanceId`: string
- `pipelineIdentifier`: string
- `runtimeInputs`: object
- `schemaId`: string
- `useDefaultPipeline`: boolean

## ExecuteLlmAuthoringPipelineResponseBody
- required: executionId, pipelineIdentifier
- `executionId`: string
- `openInHarness`: string
- `pipelineIdentifier`: string

## ExecuteRequestBody
> Scope for the request, including account, org and project.
- required: infrastructureYaml
- `infrastructureYaml`: string
- `orgIdentifier`: string
- `projectIdentifier`: string

## Execution
> Execution defines an individual execution of a workspace workflow
- required: account, org, project, pipeline_execution_id, pipeline_stage_id, workspace, pipeline
- `account`: string; maxLen 128
- `org`: string; maxLen 128
- `pipeline`: string
- `pipeline_execution_id`: string
- `pipeline_stage_id`: string
- `project`: string; maxLen 128
- `workspace`: string

## ExecutionArtifactSummaryRequestBody
- `artifactFingerprints`: array
- `targetVariants`: array

## ExecutionConfigOperation
> Operations to set the images tag to particular version
- required: field, value
- `field`: string
- `value`: string

## ExecutionConfigTags
- `artifactoryTag`: string
- `bigQueryTag`: string
- `bigtableTag`: string
- `cloudSqlTag`: string
- `db2Tag`: string
- `defaultTag`: string
- `flywayDefaultTag`: string
- `flywayMongoTag`: string
- `flywaySpannerPsqlTag`: string
- `flywaySpannerTag`: string
- `gitCloneTag`: string
- `mongoTag`: string
- `perconaTag`: string
- `rdsTag`: string
- `snowflakeTag`: string
- `spannerTag`: string

## ExecutionConflict
- required: planExecutionId, status, releaseInfoList, createdAt, lastUpdatedAt, pipelineName, pipelineIdentifier, runSequenceId, orgIdentifier, projectIdentifier, triggerType, triggeredBy, executionStatus, startTs
- `planExecutionId`: string
- `status`: obj
- `type`: obj
- `releaseInfoList`: array
- `createdAt`: integer
- `lastUpdatedAt`: integer
- `conflictResolvedBy`: obj
- `conflictResolvedAt`: integer
- `pipelineName`: string
- `pipelineIdentifier`: string
- `runSequenceId`: integer
- `orgIdentifier`: string
- `projectIdentifier`: string
- `triggerType`: obj
- `triggeredBy`: obj
- `executionStatus`: obj
- `startTs`: integer
- `endTs`: integer
- `comment`: string

## ExecutionContext
- required: pipeline_id, stage_id, sequence_id, pipeline_execution_id, step_id, step_execution_id, stage_execution_id
- `pipeline_id`: string
- `stage_id`: string
- `sequence_id`: string
- `pipeline_execution_id`: string
- `step_id`: string
- `build_url`: string
- `step_execution_id`: string
- `step_name`: string
- `stage_name`: string
- `stage_execution_id`: string
- `stage_type`: string

## ExecutionContextV2
> Details of the Execution Context
- required: type
- `type`: string; enum: harness, github

## ExecutionDataResponse
> This contains Execution metadata details.
- `executionId`: string
- `executionYaml`: string

## ExecutionDetail
- required: type
- `type`: obj
- `github`: obj
- `harness`: obj

## ExecutionDetails
- `execution_id`: string
- `status`: string

## ExecutionErrorInfo
- `unknownFields`: obj
- `message`: string
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `messageBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## ExecutionEvent
- required: event, createdAt
- `createdAt`: string
- `event`: obj
- `message`: string

## ExecutionGraph
- `rootNodeId`: string
- `nodeMap`: object
- `nodeAdjacencyListMap`: object
- `executionMetadata`: object
- `representationStrategy`: string; enum: camelCase

## ExecutionInfo
> This is the view for a particular Execution in Retry History
- `uuid`: string
- `startTs`: integer
- `endTs`: integer
- `status`: string; enum: Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted, Discontinuing, Queued
- `runSequence`: integer

## ExecutionInputDTO
> Contains the template for Execution time inputs.
- `nodeExecutionId`: string
- `inputInstanceId`: string
- `inputTemplate`: string
- `userInput`: string
- `fieldYaml`: string

## ExecutionInputStatus
> Contains the Input Instance ID and the status If the Execution Input is valid
- `nodeExecutionId`: string
- `inputInstanceId`: string
- `status`: string; enum: Failed, Success

## ExecutionInputVariablesResponse
> Contains the yaml that was used to execute
- `variableMergeServiceResponse`: obj
- `pipelineYaml`: string

## ExecutionIssueCountsRequestBody
- `targetVariants`: array

## ExecutionLimitRequestBody
- `config_id`: string
- `configs`: array

## ExecutionLimitResponseBody
- `account_id`: string
- `config_id`: string
- `name`: string
- `type`: string
- `configs`: array

## ExecutionLogDTO

## ExecutionMetadata
- `unknownFields`: obj
- `initialized`: boolean
- `principalInfo`: obj
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `settingToValueMapMap`: object
- `featureFlagToValueMapMap`: object
- `triggerInfo`: obj
- `retryInfo`: obj
- `pipelineStageInfo`: obj
- `runSequence`: integer
- `pipelineIdentifier`: string
- `executionUuid`: string
- `gitSyncBranchContext`: obj
- `moduleType`: string
- `isNotificationConfigured`: boolean
- `pipelineConnectorRef`: string
- `harnessVersion`: string
- `isDebug`: boolean
- `originalPlanExecutionIdForRollbackMode`: string
- `processedYamlVersion`: string
- `isStagesExpressionsProvided`: boolean
- `branchSeqId`: integer
- `codebaseBranch`: string
- `normalizedRepoUrl`: string
- `enableDAG`: boolean
- `isPipelineConverted`: boolean
- `triggerInfoOrBuilder`: obj
- `pipelineIdentifierBytes`: obj
- `executionUuidBytes`: obj
- `principalInfoOrBuilder`: obj
- `moduleTypeBytes`: obj
- `retryInfoOrBuilder`: obj
- `pipelineStoreTypeValue`: integer
- `pipelineStoreType`: string; enum: UNDEFINED, INLINE, REMOTE, UNRECOGNIZED
- `pipelineConnectorRefBytes`: obj
- `pipelineStageInfoOrBuilder`: obj
- `harnessVersionBytes`: obj
- `executionModeValue`: integer
- `executionMode`: string; enum: UNDEFINED_MODE, NORMAL, POST_EXECUTION_ROLLBACK, PIPELINE_ROLLBACK, UNRECOGNIZED
- `originalPlanExecutionIdForRollbackModeBytes`: obj
- `settingToValueMapCount`: integer
- `settingToValueMap`: object
- `featureFlagToValueMapCount`: integer
- `featureFlagToValueMap`: object
- `processedYamlVersionBytes`: obj
- `codebaseBranchBytes`: obj
- `normalizedRepoUrlBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## ExecutionMetadataOrBuilder
- `principalInfo`: obj
- `settingToValueMapMap`: object
- `featureFlagToValueMapMap`: object
- `triggerInfo`: obj
- `retryInfo`: obj
- `pipelineStageInfo`: obj
- `runSequence`: integer
- `pipelineIdentifier`: string
- `executionUuid`: string
- `gitSyncBranchContext`: obj
- `moduleType`: string
- `isNotificationConfigured`: boolean
- `pipelineConnectorRef`: string
- `harnessVersion`: string
- `isDebug`: boolean
- `originalPlanExecutionIdForRollbackMode`: string
- `processedYamlVersion`: string
- `isStagesExpressionsProvided`: boolean
- `branchSeqId`: integer
- `codebaseBranch`: string
- `normalizedRepoUrl`: string
- `enableDAG`: boolean
- `isPipelineConverted`: boolean
- `triggerInfoOrBuilder`: obj
- `pipelineIdentifierBytes`: obj
- `executionUuidBytes`: obj
- `principalInfoOrBuilder`: obj
- `moduleTypeBytes`: obj
- `retryInfoOrBuilder`: obj
- `pipelineStoreTypeValue`: integer
- `pipelineStoreType`: string; enum: UNDEFINED, INLINE, REMOTE, UNRECOGNIZED
- `pipelineConnectorRefBytes`: obj
- `pipelineStageInfoOrBuilder`: obj
- `harnessVersionBytes`: obj
- `executionModeValue`: integer
- `executionMode`: string; enum: UNDEFINED_MODE, NORMAL, POST_EXECUTION_ROLLBACK, PIPELINE_ROLLBACK, UNRECOGNIZED
- `originalPlanExecutionIdForRollbackModeBytes`: obj
- `settingToValueMapCount`: integer
- `settingToValueMap`: object
- `featureFlagToValueMapCount`: integer
- `featureFlagToValueMap`: object
- `processedYamlVersionBytes`: obj
- `codebaseBranchBytes`: obj
- `normalizedRepoUrlBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## ExecutionNode
- `uuid`: string
- `setupId`: string
- `name`: string
- `identifier`: string
- `baseFqn`: string
- `outcomes`: object
- `stepParameters`: obj
- `createdAt`: integer
- `startTs`: integer
- `endTs`: integer
- `stepType`: string
- `status`: string; enum: Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted, Discontinuing, Queued
- `failureInfo`: obj
- `skipInfo`: obj
- `nodeRunInfo`: obj
- `retryNodeMetadata`: obj
- `executableResponses`: array
- `unitProgresses`: array
- `progressData`: obj
- `delegateInfoList`: array
- `interruptHistories`: array
- `stepDetails`: object
- `strategyMetadata`: obj
- `executionInputConfigured`: boolean
- `logBaseKey`: string
- `manualInterventionAvailableActions`: array
- `childrenCount`: integer

## ExecutionNodeAdjacencyList
- `children`: array
- `nextIds`: array

## ExecutionOutput
- required: value
- `description`: string
- `value`: obj

## ExecutionOutputDTO
> Output value for a phase execution
- required: name, value
- `name`: string
- `value`: obj

## ExecutionPrincipalInfo
- `unknownFields`: obj
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `principal`: string
- `shouldValidateRbac`: boolean
- `principalBytes`: obj
- `principalTypeValue`: integer
- `principalType`: string; enum: UNKNOWN, USER, USER_GROUP, API_KEY, SERVICE, SERVICE_ACCOUNT, UNRECOGNIZED
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## ExecutionPrincipalInfoOrBuilder
- `principal`: string
- `shouldValidateRbac`: boolean
- `principalBytes`: obj
- `principalTypeValue`: integer
- `principalType`: string; enum: UNKNOWN, USER, USER_GROUP, API_KEY, SERVICE, SERVICE_ACCOUNT, UNRECOGNIZED
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## ExecutionResourceCollection

## ExecutionSummaryInfo
> This is the view of the Execution Summary
- `numOfErrors`: array
- `deployments`: array
- `lastExecutionTs`: integer
- `lastExecutionStatus`: string; enum: Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted, Discontinuing, Queued
- `lastExecutionId`: string

## ExecutionTaskDTO
> Represents an execution task for a specific activity
- required: identifier, name, status, required, userGroups, expectedDuration
- `identifier`: string
- `name`: string
- `description`: string
- `status`: obj
- `required`: obj
- `userGroups`: obj
- `expectedDuration`: string
- `actualDuration`: string
- `createdAt`: integer
- `lastUpdatedAt`: integer
- `taskExecutionId`: string
- `failureInfo`: obj

## ExecutionTaskStatus
> Current status of the execution task

## ExecutionTriggerInfo
- `unknownFields`: obj
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `triggeredBy`: obj
- `rerunInfo`: obj
- `buildInfo`: obj
- `isRerun`: boolean
- `triggerTypeValue`: integer
- `triggerType`: string; enum: NOOP, MANUAL, WEBHOOK, WEBHOOK_CUSTOM, SCHEDULER_CRON, ARTIFACT, MANIFEST, UNRECOGNIZED
- `triggeredByOrBuilder`: obj
- `rerunInfoOrBuilder`: obj
- `buildInfoOrBuilder`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## ExecutionTriggerInfoOrBuilder
- `triggeredBy`: obj
- `rerunInfo`: obj
- `buildInfo`: obj
- `isRerun`: boolean
- `triggerTypeValue`: integer
- `triggerType`: string; enum: NOOP, MANUAL, WEBHOOK, WEBHOOK_CUSTOM, SCHEDULER_CRON, ARTIFACT, MANIFEST, UNRECOGNIZED
- `triggeredByOrBuilder`: obj
- `rerunInfoOrBuilder`: obj
- `buildInfoOrBuilder`: obj
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## ExecutionType

## ExecutorInfo
> Information regarding Executor of Pipeline.
- `trigger_type`: string; enum: NOOP, MANUAL, WEBHOOK, WEBHOOK_CUSTOM, SCHEDULER_CRON
- `username`: string
- `email`: string

## ExportPipelineSecurityIssuesCSVResponseBody
- required: headers, data, filename, totalRows, executionId
- `data`: array
- `executionId`: string
- `filename`: string
- `headers`: array
- `totalRows`: integer

## FacilitatorExecutableResponse
- `unknownFields`: obj
- `type`: string
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `typeBytes`: obj
- `statusValue`: integer
- `status`: string; enum: NO_OP, RUNNING, INTERVENTION_WAITING, TIMED_WAITING, ASYNC_WAITING, TASK_WAITING, DISCONTINUING, PAUSING, QUEUED, SKIPPED, PAUSED, ABORTED
- `startTs`: integer
- `callbackIdsList`: array
- `timeoutInSeconds`: integer
- `callbackIdsCount`: integer
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## FacilitatorExecutableResponseOrBuilder
- `type`: string
- `typeBytes`: obj
- `statusValue`: integer
- `status`: string; enum: NO_OP, RUNNING, INTERVENTION_WAITING, TIMED_WAITING, ASYNC_WAITING, TASK_WAITING, DISCONTINUING, PAUSING, QUEUED, SKIPPED, PAUSED, ABORTED
- `startTs`: integer
- `callbackIdsList`: array
- `timeoutInSeconds`: integer
- `callbackIdsCount`: integer
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## FeaturePipeline
> A pipeline configured to update a feature
- required: identifier, name
- `createdAt`: integer
- `description`: string
- `identifier`: string
- `lastUpdatedAt`: integer
- `name`: string

## FirewallExceptionApprovalRequestV3
> Request to approve or reject a firewall exception
- required: status
- `notes`: string
- `status`: obj

## FlywayCommandExecutionStatus

## FreezeDetailedResponse
> This contains detailed information of the Freeze Config
- required: accountId, identifier, name
- `accountId`: string
- `type`: string; enum: GLOBAL, MANUAL
- `status`: string; enum: Enabled, Disabled
- `name`: string
- `description`: string; maxLen 1024
- `tags`: object
- `orgIdentifier`: string
- `projectIdentifier`: string
- `windows`: array
- `currentOrUpcomingWindow`: obj
- `identifier`: string
- `createdAt`: integer
- `lastUpdatedAt`: integer
- `freezeScope`: string; enum: account, org, project, unknown
- `yaml`: string

## FreezeDetailsDTO
> Detailed freeze information with entity extraction
- required: freeze_identifier, orgIdentifier, projectIdentifier, name, entities, expectedStartTs, expectedEndTs
- `freeze_identifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `name`: string
- `description`: string
- `status`: string; enum: Enabled, Disabled
- `entities`: obj
- `expectedStartTs`: integer
- `expectedEndTs`: integer

## FreezeEntitiesDTO
> Entity information extracted from freeze YAML configuration
- required: services, environments, environmentTypes, projects, organizations, pipelines
- `services`: array
- `environments`: array
- `environmentTypes`: array
- `projects`: array
- `organizations`: array
- `pipelines`: array

## FreezeErrorResponseDTO
- `id`: string
- `name`: string
- `errorMessage`: string

## FreezeFilterPropertiesDTO
- `freezeIdentifiers`: array
- `sort`: array
- `freezeStatus`: string; enum: Enabled, Disabled
- `startTime`: integer
- `endTime`: integer
- `searchTerm`: string

## FreezeListItemDTO
> Basic freeze information for list view
- required: name, expectedStartTs, expectedEndTs, orgIdentifier, projectIdentifier, identifier
- `name`: string
- `expectedStartTs`: integer
- `expectedEndTs`: integer
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string

## FreezeListResponseDTO
> Paginated response containing freeze list items
- required: freezes, nextRequest, last
- `freezes`: array
- `nextRequest`: obj
- `last`: boolean

## FreezeResponse
> This contains details of the Freeze Response
- required: accountId, identifier, name, yaml
- `accountId`: string
- `type`: string; enum: GLOBAL, MANUAL
- `status`: string; enum: Enabled, Disabled
- `name`: string
- `description`: string; maxLen 1024
- `tags`: object
- `orgIdentifier`: string
- `projectIdentifier`: string
- `windows`: array
- `identifier`: string
- `yaml`: string
- `createdAt`: integer
- `lastUpdatedAt`: integer
- `freezeScope`: string; enum: account, org, project, unknown

## FreezeResponseWrapperDTO
- `noOfSuccess`: integer
- `noOfFailed`: integer
- `successfulFreezeResponseDTOList`: array
- `freezeErrorResponseDTOList`: array

## FreezeSummaryResponse
> This contains summary of the Freeze Response
- required: accountId, identifier, name
- `accountId`: string
- `type`: string; enum: GLOBAL, MANUAL
- `status`: string; enum: Enabled, Disabled
- `name`: string
- `description`: string; maxLen 1024
- `tags`: object
- `orgIdentifier`: string
- `projectIdentifier`: string
- `windows`: array
- `currentOrUpcomingWindow`: obj
- `identifier`: string
- `createdAt`: integer
- `lastUpdatedAt`: integer
- `freezeScope`: string; enum: account, org, project, unknown
- `yaml`: string

## FreezeWindow
- required: startTime, timeZone
- `timeZone`: string
- `startTime`: string
- `duration`: string
- `endTime`: string
- `recurrence`: obj

## FrontendPipelineSecurityIssuesResponseBody

## FrontendPipelineSecurityIssuesV2ResponseBody

## FrontendPipelineSecurityStepsResponseBody

## FrozenExecutionDetail
- `freeze`: obj
- `url`: string

## FrozenExecutionDetails
- `freezeList`: array

## GcpCloudCostConnectorDTO
- required: featuresEnabled, projectId, serviceAccountEmail

## GcpConnector
> This contains GCP connector details
- required: credential

## GcpConnectorCredential
> This contains GCP connector credentials
- required: type
- `type`: string; enum: InheritFromDelegate, ManualConfig, OidcAuthentication
- `spec`: obj

## GcpDelegateDetails
> This contains GCP connector delegate details
- required: delegateSelectors

## GcpKmsConnector
> This contains GCP KMS SecretManager configuration.
- required: keyName, keyRing, projectId, region

## GcpOidcServiceAccountAccessTokenResponse
- `accessToken`: string
- `expireTime`: integer

## GcpOidcTokenExchangeDetailsForDelegate
- `oidcIdToken`: string
- `oidcAccessTokenStsEndpoint`: string
- `oidcAccessTokenIamSaEndpoint`: string
- `gcpServiceAccountEmail`: string
- `oidcWorkloadAccessTokenRequestStructure`: obj
- `oidcChartmuseumGcpConfigStructure`: obj
- `idTokenExpiryTime`: integer

## GcpSecretManager
> This contains details of GCP Secret Manager

## GcrArtifactTriggerSpec
- `connector_ref`: string
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `registry_hostname`: string
- `image_path`: string
- `tag`: string

## GenAIServiceDTO
- `serviceName`: string
- `lastActivityTimestamp`: integer
- `status`: string; enum: ACTIVE, INACTIVE

## GenericWebhookAuthSpec
> Details of Authentication for Generic Webhook defined in Harness
- `auth_type`: string; enum: NoAuth, Hmac

## GenericWebhookResponse
> Details of the Generic Webhook Response defined in Harness

## GenericWebhookSpec
> Details of the Git Webhook Response defined in Harness

## GetGitXWebhookEventFileValidationResponse
> Get GitX Webhook Event File Validation Response
- `file_path`: string
- `file_url`: string
- `file_action_type`: string; enum: ADDED, MODIFIED, DELETED
- `entity_details`: array

## GetVariablesAndProvidersResponse
- required: terraform_variables, environment_variables, provider_connectors, variable_files
- `environment_variables`: array
- `provider_connectors`: array
- `terraform_variables`: array
- `variable_files`: array

## GitHttpConnectorSpec
> This contains details of the Generic Git http connector

## GitHttpEncryptedConnectorSpec
> This contains details of the Generic Git http connector

## GitHubMcpConnector
> GitHub MCP Server connector
- required: url

## GitSshConnectorSpec
> This contains details of the Generic Git ssh connector

## GitWebhookResponse
> Details of the Git Webhook Response defined in Harness

## GitWebhookSpec
> Details of the Git Webhook defined in Harness

## GitXWebhookEventResponse
> Contains information about the GitX webhook Events
- `author_name`: string
- `event_identifier`: string
- `webhook_identifier`: string
- `payload`: string
- `event_trigger_time`: integer
- `repo_name`: string
- `event_status`: string; enum: SKIPPED, FAILED, QUEUED, SUCCESSFUL, PROCESSING, WARNING, UNKNOWN
- `event_status_message`: obj
- `commit_message`: string
- `commit_id`: string
- `commit_url`: string
- `file_count`: integer
- `failure_file_count`: integer
- `branch`: string

## GitXWebhookResponse
> Contains information about the GitX webhooks 
- `webhook_identifier`: string
- `webhook_name`: string
- `connector_ref`: string
- `repo_name`: string
- `folder_paths`: array
- `is_enabled`: boolean
- `event_trigger_time`: integer

## GithubConnector
> This contains details of Github connectors
- required: authentication, type, url

## GithubExecutionContext
> Github Pipeline Execution Details

## GithubExecutionDetail
> Github Pipeline Execution Details
- `repository`: string
- `github_action`: string
- `action_path`: string
- `job_id`: string
- `run_id`: string
- `workflow_ref`: string
- `runner_detail`: obj

## GithubPackageRegistryArtifactTriggerSpec
- `connector_ref`: string
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `org`: string
- `package_name`: string
- `package_type`: string

## GithubWebhookSpec

## GithubWebhookTriggerSpec
- `connector_ref`: string
- `repo_name`: string
- `header_conditions`: array
- `payload_conditions`: array
- `jexl_condition`: string
- `auto_abort_previous_executions`: boolean
- `type`: string; enum: PullRequest, Push, IssueComment, Release

## GitlabConnector
> This contains details of Gitlab connectors
- required: authentication, type, url

## GitlabWebhookSpec

## GitlabWebhookTriggerSpec
- `connector_ref`: string
- `repo_name`: string
- `header_conditions`: array
- `payload_conditions`: array
- `jexl_condition`: string
- `auto_abort_previous_executions`: boolean
- `type`: string; enum: MergeRequest, Push, MRComment

## GoogleArtifactRegistryArtifactTriggerSpec
- `connector_ref`: string
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `version`: string
- `region`: string
- `project`: string
- `repository_name`: string
- `pkg`: string

## GoogleChatConnector
> Google Chat Connector details.
- required: apiAccessType

## GoogleCloudStorageArtifactTriggerSpec
- `connector_ref`: string
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `project`: string
- `bucket`: string
- `artifact_path`: string

## HarnessApprovalActivity
- required: action, user
- `user`: obj
- `action`: string; enum: APPROVE, REJECT
- `approverInputs`: array
- `comments`: string
- `approvedAt`: integer

## HarnessApprovalActivityRequest
> Details of approval activity requested
- required: action
- `action`: string; enum: APPROVE, REJECT
- `approverInputs`: array
- `comments`: string
- `autoApprove`: boolean

## HarnessApprovalActivityRequestBody
> Request Body for Harness Approval Activity
- `comments`: string
- `action`: string; enum: APPROVE, REJECT
- `approver_inputs`: array

## HarnessApprovalInstanceDetails
> This contains details of Harness Approval Instance
- required: approvers

## HarnessConnector
> This contains details of Harness connectors
- required: authentication, type, url

## HarnessExecutionContext
> Harness Pipeline Execution Details

## HarnessExecutionDetail
> Harness Pipeline Execution Details
- `org`: string
- `project`: string
- `pipeline_execution_id`: string
- `pipeline_id`: string
- `pipeline_name`: string
- `sequence_id`: string
- `step_id`: string
- `step_execution_id`: string
- `step_name`: string
- `stage_id`: string
- `stage_execution_id`: string
- `stage_name`: string
- `stage_type`: string
- `runner_detail`: obj

## HarnessIacmApproval
> Approval is the representation for a single approval
- required: account, org, project, pipeline_execution_id, pipeline_stage_id, workspace_id, id, status, created, updated
- `account`: string; maxLen 128
- `actioned_by`: string
- `actioned_by_email`: string
- `created`: integer
- `id`: string
- `org`: string; maxLen 128
- `pipeline_execution_id`: string
- `pipeline_stage_id`: string
- `project`: string; maxLen 128
- `status`: string
- `updated`: integer
- `workspace_id`: string

## HarnessIacmDefaultpipeline
- required: account, org, project, provisioner, operation, pipeline, updated
- `account`: string
- `operation`: string; enum: plan, apply, destroy, drift, synth, diff, deploy, remediation
- `org`: string
- `pipeline`: string
- `project`: string
- `provisioner`: string; enum: terraform, opentofu, terragrunt, awscdk
- `updated`: integer
- `workspace`: string

## HarnessIacmExecution
> ExecutionResource is the representation for a single workflow execution.
- required: status, created, account, org, project, pipeline_execution_id, pipeline_stage_id, workspace, pipeline
- `account`: string; maxLen 128
- `created`: integer
- `org`: string; maxLen 128
- `pipeline`: string
- `pipeline_execution_id`: string
- `pipeline_stage_id`: string
- `project`: string; maxLen 128
- `status`: string; enum: none, success, failure
- `workspace`: string

## HarnessIacmMigrationTrigger
> Acknowledgement that the migration job was triggered
- required: message
- `message`: string

## HarnessIacmModuleRegistryServiceDiscovery
> DiscoveryResponse returns the actions that the service provides
- required: modules.v1, providers.v1
- `modules.v1`: string
- `providers.v1`: string

## HarnessIacmModuleexecutionresource
> ModuleExecutionResource is the representation for a single module execution.
- required: org, project, status, created, account, pipeline_org, pipeline_project, pipelineExecutionId, pipelineStageId, moduleId, pipeline
- `account`: string
- `created`: integer
- `metadata`: obj
- `module_onboarding`: boolean
- `moduleId`: string
- `org`: string
- `project`: string
- `status`: string

## HarnessIacmVariableSet
> VariableSetResource is the representation for a variable-set association.
- required: account, org, project, identifier, name, env_vars_count, tf_vars_count, var_files_count
- `account`: string; maxLen 128
- `connectors`: array
- `created`: integer
- `description`: string
- `env_vars_count`: integer
- `environment_variables`: object
- `id`: integer
- `identifier`: string; pattern `^[^/?#\s]+$`; maxLen 128
- `name`: string; maxLen 128
- `org`: string; maxLen 128
- `project`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `tf_vars_count`: integer
- `updated`: integer
- `var_files_count`: integer

## HarnessIacmVariableSetList
- `items`: obj

## HarnessIacmVariableSetSaveresult
- required: account, org, project, identifier, name
- `account`: string; maxLen 128
- `connectors`: array
- `created`: integer
- `description`: string
- `environment_variables`: object
- `id`: integer
- `identifier`: string; pattern `^[^/?#\s]+$`; maxLen 128
- `name`: string; maxLen 128
- `org`: string; maxLen 128
- `project`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `updated`: integer

## HarnessIacmWorkspacevariable
> WorkspaceVariableResource is the representation for a single environment variable associated with a workspace.
- required: account, org, project, workspace, key, value, value_type, kind, created, updated
- `account`: string; maxLen 128
- `created`: integer
- `key`: string; pattern `^[a-zA-Z0-9_]+$`; maxLen 128
- `kind`: string; enum: env, tf
- `org`: string; maxLen 128
- `project`: string; maxLen 128
- `updated`: integer
- `value`: string
- `value_type`: string; enum: string, secret
- `workspace`: string

## HarnessIacmWorkspacevariableCreateresult
- required: account, org, project, workspace, key, value, value_type, kind, created, updated
- `account`: string; maxLen 128
- `created`: integer
- `key`: string; pattern `^[a-zA-Z0-9_]+$`; maxLen 128
- `kind`: string; enum: env, tf
- `org`: string; maxLen 128
- `policy_evaluation`: obj
- `project`: string; maxLen 128
- `updated`: integer
- `value`: string
- `value_type`: string; enum: string, secret
- `workspace`: string

## HarnessPipelineIntegrationResponse
- required: enabled
- `enabled`: boolean

## HarnessPipelineSettings
- `is_auth_enabled_for_custom_webhook`: boolean

## HarnessWebhookSpec

## HarnessWebhookTriggerSpec
- `repo_name`: string
- `header_conditions`: array
- `payload_conditions`: array
- `jexl_condition`: string
- `auto_abort_previous_executions`: boolean
- `type`: string; enum: PullRequest, Push, IssueComment

## HelmChartManifestTriggerSpec
- `event_conditions`: array
- `chart_name`: string
- `chart_version`: string
- `helm_version`: string; enum: V2, V3, V380
- `store`: obj

## HttpHelmConnector
> This contains http helm connector details
- required: helmRepoUrl

## IaCMServiceVersion
> Service version
- required: version, commit, deployment_mode
- `commit`: string
- `deployment_mode`: string; enum: saas, smp
- `version`: string

## IaCMVariable
> Variable is the representation for a single variable associated with a workspace.
- required: key, value, value_type, kind
- `key`: string; pattern `^[A-Za-z_][A-Za-z0-9_-]*$`; maxLen 128
- `value`: string
- `value_type`: string; enum: string, secret

## IaCMWebhookInfo
> WebhookInfo defines the webhook information for a unified execution
- required: type
- `connector`: string
- `link`: string
- `repo`: string
- `type`: string; enum: pull_request, merged, push, release, tag

## ImporterPipelineOption

## Infrastructure
> This is the Infrastructure entity defined in Harness
- required: identifier, name, type
- `account`: string; maxLen 128
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `org`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `project`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `environment`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `type`: obj
- `description`: string; maxLen 1024
- `tags`: object
- `harness_version`: string
- `yaml`: string

## Infrastructure1
- required: identifier, targetState
- `identifier`: string
- `instances`: array
- `metadata`: object
- `outputs`: object
- `targetState`: obj

## InfrastructureCreateRequest
> Infrastructure Request Body 
- required: identifier, name, type, yaml
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `type`: obj
- `harness_version`: string
- `yaml`: string

## InfrastructureDeploymentDTO
> Represents services deployed to a traditional infrastructure
- required: identifier, name, services
- `identifier`: string
- `name`: string
- `services`: array

## InfrastructureExecution
- required: id, infrastructureId, instanceIds, specRevision, spec, startedAt, targetState, progress, completedInstanceIds
- `approvals`: array
- `completedInstanceIds`: array
- `events`: array
- `id`: string
- `infrastructureId`: string
- `instanceIds`: array
- `message`: string
- `outputs`: object
- `pipelineUrl`: string
- `progress`: obj
- `spec`: obj
- `specRevision`: integer
- `startedAt`: string
- `stoppedAt`: string
- `targetState`: obj

## InfrastructureExecutionList
- `executions`: array
- `total`: integer

## InfrastructureGitUpdateResponse
> Contains info about infrastructure that is updated.
- `identifier`: string

## InfrastructureImportResponse
> Contains info about infrastructure that is imported.
- `identifier`: string
- `governanceMetadata`: obj

## InfrastructureInputVariable
> Input variable for infrastructure type
- required: type
- `type`: string; enum: infrastructure
- `description`: string
- `default`: array
- `metadata`: obj

## InfrastructureList
- `infrastructures`: array
- `total`: integer

## InfrastructureMetadata
- `deploymentType`: obj
- `environmentRef`: string

## InfrastructureOutput
- required: identifier, state, activeExecutions
- `activeExecutions`: array
- `identifier`: string
- `spec`: obj
- `state`: obj

## InfrastructureProgress
- required: progress
- `progress`: string; enum: unknown, pending, processing, done, failed, aborted, deleted, replaced

## InfrastructureRequest
> This is the InfrastructureRequest entity defined in Harness
- required: yaml
- `identifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `environmentRef`: string
- `name`: string
- `description`: string
- `tags`: object
- `type`: string; enum: KubernetesDirect, KubernetesGcp, KubernetesAzure, Pdc, SshWinRmAzure, ServerlessAwsLambda, AzureWebApp, AzureFunction, SshWinRmAws, CustomDeployment, ECS, Elastigroup
- `yaml`: string

## InfrastructureResponse
> Default response when a infrastructure is returned
- `infrastructure`: obj
- `created`: integer
- `updated`: integer

## InfrastructureResponse1
- `infrastructure`: obj
- `createdAt`: integer
- `lastModifiedAt`: integer
- `entityValidityDetails`: obj
- `governanceMetadata`: obj

## InfrastructureResponseDTO
> This is the InfrastructureResponseDTO entity defined in Harness
- `accountId`: string
- `identifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `environmentRef`: string
- `name`: string
- `description`: string
- `tags`: object
- `type`: string; enum: KubernetesDirect, KubernetesGcp, KubernetesAzure, Pdc, SshWinRmAzure, ServerlessAwsLambda, AzureWebApp, AzureFunction, SshWinRmAws, CustomDeployment, ECS, Elastigroup
- `deploymentType`: string; enum: Kubernetes, NativeHelm, Ssh, WinRm, ServerlessAwsLambda, AzureWebApp, AzureFunction, CustomDeployment, ECS, Elastigroup, TAS, Asg
- `yaml`: string

## InfrastructureSpec
- `createdAt`: string
- `infrastructure`: obj
- `revision`: integer

## InfrastructureSpecList
- `specs`: array
- `total`: integer

## InfrastructureState
- `createdAt`: string
- `sessionEndedAt`: string
- `sessionStartedAt`: string
- `updatedAt`: string

## InfrastructureType

## InfrastructureUpdateRequest
> Infrastructure Update Request Body 
- required: identifier, name, type, yaml
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `type`: obj
- `harness_version`: string
- `yaml`: string

## InputSetCreateRequestBody
> Input Set create request body
- required: input_set_yaml, identifier, name
- `input_set_yaml`: string
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `git_details`: obj

## InputSetDetails
> Details of an inputset used in a pipeline execution
- `identifier`: string
- `name`: string

## InputSetError
> Input Set error
- `field_name`: string
- `message`: string
- `identifier_of_error_source`: string

## InputSetErrorDetails
> Error details regarding Input Sets.
- `valid`: boolean
- `message`: string
- `outdated`: boolean
- `error_pipeline_yaml`: string
- `fqn_errors`: array
- `invalid_refs`: array

## InputSetErrorWrapper
> This contains the error response if the Input Set save failed
- `errorPipelineYaml`: string
- `uuidToErrorResponseMap`: object
- `invalidInputSetReferences`: array
- `type`: string

## InputSetErrorWrapperDTO
- `error_pipeline_yaml`: string
- `uuid_to_error_response_map`: object
- `invalid_inputset_references`: array

## InputSetGitUpdateDetails
> Contains parameters related to updating an Input Set for Git Experience.
- `branch_name`: string
- `commit_message`: string
- `last_object_id`: string
- `base_branch`: string
- `last_commit_id`: string
- `parent_entity_connector_ref`: string
- `parent_entity_repo_name`: string

## InputSetGitUpdateResponse
> Contains info about input-set that is updated.
- `identifier`: string

## InputSetImportRequestBody
> InputSet import request body
- `git_import_info`: obj
- `input_set_import_request`: obj

## InputSetImportRequestDTO
> Information of InputSet import request DTO
- `input_set_name`: string
- `input_set_description`: string

## InputSetImportResponseBody
> Response body for Input Set import.
- `input_set_identifier`: string

## InputSetListResponse
> This is the response of InputSet list call.
- `identifier`: string
- `name`: string
- `pipelineIdentifier`: string
- `inputSetIdWithPipelineId`: string
- `description`: string
- `inputSetType`: string; enum: INPUT_SET, OVERLAY_INPUT_SET

## InputSetMoveConfigRequestBody
> Request body for moving an input set configuration.
- `git_details`: obj
- `pipeline_identifier`: string
- `input_set_identifier`: string
- `move_config_operation_type`: obj

## InputSetMoveConfigResponseBody
> Response body for moving an input set configuration.
- `input_set_identifier`: string

## InputSetReferenceProtoDTO
- `unknownFields`: obj
- `pipelineIdentifier`: obj
- `parentUniqueId`: obj
- `accountIdentifier`: obj
- `orgIdentifier`: obj
- `projectIdentifier`: obj
- `orgIdentifierOrBuilder`: obj
- `projectIdentifierOrBuilder`: obj
- `accountIdentifierOrBuilder`: obj
- `pipelineIdentifierOrBuilder`: obj
- `identifierOrBuilder`: obj
- `parentUniqueIdOrBuilder`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `defaultInstanceForType`: obj
- `initialized`: boolean
- `identifier`: obj
- `allFields`: object
- `descriptorForType`: obj
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## InputSetReferenceProtoDTOOrBuilder
- `pipelineIdentifier`: obj
- `parentUniqueId`: obj
- `accountIdentifier`: obj
- `orgIdentifier`: obj
- `projectIdentifier`: obj
- `orgIdentifierOrBuilder`: obj
- `projectIdentifierOrBuilder`: obj
- `accountIdentifierOrBuilder`: obj
- `pipelineIdentifierOrBuilder`: obj
- `identifierOrBuilder`: obj
- `parentUniqueIdOrBuilder`: obj
- `identifier`: obj
- `allFields`: object
- `descriptorForType`: obj
- `defaultInstanceForType`: obj
- `initializationErrorString`: string
- `unknownFields`: obj
- `initialized`: boolean

## InputSetResponse
> This contains Input Set details.
- `accountId`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `pipelineIdentifier`: string
- `identifier`: string
- `inputSetYaml`: string
- `name`: string
- `description`: string
- `tags`: object
- `isOutdated`: boolean
- `isErrorResponse`: boolean
- `inputSetErrorWrapper`: obj
- `gitDetails`: obj
- `entityValidityDetails`: obj
- `errorResponse`: boolean
- `outdated`: boolean

## InputSetResponseBody
> Response body for Input Set
- `input_set_yaml`: string
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `org`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `project`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `pipeline`: string
- `description`: string; maxLen 1024
- `tags`: object
- `store_type`: string; enum: INLINE, REMOTE
- `connector_ref`: string
- `git_details`: obj
- `created`: integer
- `updated`: integer
- `error_details`: obj

## InputSetSummaryResponse
> This is the view of the Input Set Summary.
- `identifier`: string
- `name`: string
- `pipelineIdentifier`: string
- `description`: string
- `inputSetType`: string; enum: INPUT_SET, OVERLAY_INPUT_SET
- `tags`: object
- `gitDetails`: obj
- `createdAt`: integer
- `lastUpdatedAt`: integer
- `isOutdated`: boolean
- `inputSetErrorDetails`: obj
- `overlaySetErrorDetails`: object
- `entityValidityDetails`: obj
- `modules`: array

## InputSetTemplateRequest
> Contains Stage Identifiers to filter Runtime Input Template.
- `stageIdentifiers`: array
- `serviceWithGitInfoList`: array

## InputSetTemplateResponse
> This contains the Runtime Input YAML used during a Pipeline Execution.
- `inputSetTemplateYaml`: string
- `inputSetYaml`: string
- `inputSetDetails`: array
- `inputSetBranchName`: string
- `resolvedYaml`: string

## InputSetTemplateWithReplacedExpressionsResponse
> This is the Runtime Input Template for a Pipeline defined in Harness.
- `inputSetTemplateYaml`: string
- `replacedExpressions`: array
- `modules`: array
- `hasInputSets`: boolean
- `replacedExpressionsPerStage`: object
- `inputsMetadata`: array

## InputSetUpdateRequestBody
> Input Set update request body
- required: input_set_yaml, identifier, name
- `input_set_yaml`: string
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `git_details`: obj

## InputSetValidator
- `validatorType`: string; enum: ALLOWED_VALUES, REGEX, SELECT_ONE_FROM, SELECT_MANY_FROM
- `parameters`: string

## InputVariable
- required: type

## InputVariableType
> Type of an input variable for parameters and process inputs.

## InstanceApproval
- required: instanceId, pipelineApprovals
- `instanceId`: string
- `pipelineApprovals`: array

## IntegrityVerificationModelPipeline
- `stage_identifier`: string
- `stage_execution_identifier`: string
- `stage_name`: string
- `step_name`: string
- `step_identifier`: string
- `step_execution_identifier`: string
- `integrity_verification`: obj

## IssueCommentAzureRepoWebhookSpec

## IssueCommentGithubWebhookSpec

## IssueCommentHarnessWebhookSpec

## IssueCountsWithExecutionInfo
> The count of Security Issues, by severity code, for a given Harness Pipeline Execution along with this execution info
- required: critical, high, medium, low, info, targetId, targetVariantId, type, targetName, targetVariantName, executionId, pipelineId, lastScanned
- `artifactFingerprint`: string; maxLen 64
- `critical`: integer
- `executionId`: string; pattern `^[a-zA-Z0-9_-]{22}$`
- `high`: integer
- `ignored`: integer
- `info`: integer
- `lastScanned`: integer
- `low`: integer
- `medium`: integer
- `pipelineId`: string; pattern `^[A-Za-z_][A-Za-z0-9_]*$`; maxLen 128
- `targetId`: string; pattern `^[a-zA-Z0-9_-]{22}$`
- `targetName`: string
- `targetVariantId`: string; pattern `^[a-zA-Z0-9_-]{22}$`
- `targetVariantName`: string
- `type`: string; enum: container, repository, instance, configuration

## JDBCConnector
> This contains details of the JDBC connector
- required: url

## JDBCDelegateAccessDTO
> Inherit from delegate authentication - uses delegate's Application Default Credentials

## JDBCServiceAccountDTO
> This entity contains kubernetes service account details
- required: serviceAccountTokenRef

## JenkinsArtifactTriggerSpec
- `connector_ref`: string
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `job_name`: string
- `artifact_path`: string
- `build`: string

## JenkinsConnector
> Jenkins Connector details.
- required: jenkinsUrl

## JiraApprovalInstanceDetails
> This contains details of Jira Approval Instance
- required: approvalCriteria, connectorRef, issue, rejectionCriteria

## JiraConnector
> JIRA Connector details.
- required: auth, jiraUrl

## JsmConnector
> Jira Service Management Connector details.
- required: auth, baseUrl

## KubernetesServiceAccount
> This contains kubernetes service account details
- required: serviceAccountTokenRef

## LangSmithConnector
> This contains details of the LangSmith connector
- required: baseUrl

## LastTriggerExecutionDetails
- `lastExecutionTime`: integer
- `lastExecutionSuccessful`: boolean
- `lastExecutionStatus`: string
- `planExecutionId`: string
- `message`: string

## LifecycleExecutionItemResponseV3
> A single artifact version evaluated during a lifecycle execution.
- required: packageName, version, registryName, status
- `lastDownloadedAt`: integer
- `orgIdentifier`: obj
- `packageName`: string
- `packageType`: obj
- `projectIdentifier`: obj
- `reason`: string
- `registryName`: string
- `size`: string
- `status`: obj
- `version`: string
- `versionId`: string

## LifecycleExecutionItemStatusV3
> Outcome of a lifecycle execution item.

## LifecycleExecutionResponseV3
- required: id, policyId, policyName, status, triggerType, createdAt, registriesAffected, packagesAffected, versionsDeleted, storageReclaimed, protected
- `completedAt`: integer
- `createdAt`: integer
- `id`: string
- `message`: string
- `orgIdentifier`: obj
- `packagesAffected`: integer
- `policyId`: string
- `policyName`: string
- `projectIdentifier`: obj
- `protected`: integer
- `registriesAffected`: integer
- `startedAt`: integer
- `status`: obj
- `storageReclaimed`: string
- `triggerType`: obj
- `versionsDeleted`: integer

## LifecycleExecutionStatusV3

## LifecycleExecutionTriggerTypeV3

## ListGitXWebhookBranchesDTO
- `branches`: array

## ListLifecycleExecutionItemsResponseV3
- required: items, hasMore, page, size
- `hasMore`: boolean
- `items`: array
- `page`: integer
- `size`: integer

## ListLifecycleExecutionsResponseBodyV3
- required: items, hasMore, page, size
- `hasMore`: boolean
- `items`: array
- `page`: integer
- `size`: integer

## ListPipelineBuildInfoDetailsResponseBodyV3

## ListPipelinesResponse
- required: account, org, project
- `account`: string; maxLen 128
- `org`: string; maxLen 128
- `pipelines`: array
- `project`: string; maxLen 128

## ListWebhookRequest
> Contains information about the webhook list request
- `webhook_type`: string; enum: GIT, GENERIC, SLACK, EVENT_BRIDGE_TRIGGER

## ListWebhooks
> A list of Harness Registries webhooks
- required: webhooks
- `itemCount`: integer
- `pageCount`: integer
- `pageIndex`: integer
- `pageSize`: integer
- `webhooks`: array

## ListWebhooksExecutions
> A list of Harness Registries webhooks executions
- required: executions
- `executions`: array
- `itemCount`: integer
- `pageCount`: integer
- `pageIndex`: integer
- `pageSize`: integer

## LocalConnector
> This contains the local connector information.

## LwCOConnector
- `accountIdentifier`: string
- `identifier`: string
- `name`: string
- `type`: string
- `spec`: object

## LwService
- required: cloud_account_id, kind, name, org_id
- `id`: integer
- `name`: string
- `org_id`: string
- `account_identifier`: string
- `project_id`: string
- `fulfilment`: string
- `kind`: string
- `cloud_account_id`: string
- `idle_time_mins`: integer
- `host_name`: string
- `health_check`: object
- `custom_domains`: array
- `match_all_subdomains`: boolean
- `disabled`: boolean
- `routing`: obj
- `opts`: obj
- `created_at`: string
- `access_point_id`: string
- `metadata`: obj
- `status`: string

## LwServiceResponse
- `response`: obj

## MCPConnector
> MCP Server connector
- required: serverUrl

## MLFlowConnector
> This contains details of the MLFlow connector
- required: auth, baseUrl

## MRCommentGitlabWebhookSpec

## ManifestTriggerSource

## ManifestTriggerSpec
> Spec for Manifest Triggers
- `type`: string; enum: HelmChart
- `spec`: obj

## ManualExecutionRequest
> Request for marking manual execution as fail or resume
- required: action
- `action`: string; enum: MARK_AS_RESUME, MARK_AS_FAIL

## ManualExecutionResponse
> This contains response for the API to mark the manual execution as fail or resume
- `status`: boolean

## MergeInputSetRequest
> Contains list of Input Set references and Stage Ids
- `inputSetReferences`: array
- `withMergedPipelineYaml`: boolean
- `stageIdentifiers`: array
- `lastYamlToMerge`: string
- `inputSetBranchName`: string

## MergeInputSetRequestBody
- `input_set_references`: array
- `with_merged_pipeline_yaml`: boolean
- `stage_identifiers`: array
- `last_yaml_to_merge`: string
- `get_only_file_content`: boolean

## MergeInputSetResponse
> View of the Response of Merging of Input Sets of a Pipeline
- `pipelineYaml`: string
- `completePipelineYaml`: string
- `isErrorResponse`: boolean
- `inputSetErrorWrapper`: obj
- `errorResponse`: boolean

## MergeInputSetResponseBody
- `inputs_yaml_merged`: string
- `merged_pipeline_yaml`: string
- `is_error_response`: boolean
- `inputset_error_wrapper`: obj

## MergeRequestGitlabWebhookSpec

## MetricLessServiceLevelIndicatorSpec

## MicroserviceVersionInfo
> Microservice Version Info
- `name`: string
- `version`: string
- `version_url`: string

## MigrateTemplateConnectorsRequest
- required: dry_run
- `dry_run`: boolean

## MigrateTemplateConnectorsResponse
- required: message
- `message`: string

## MigrateWorkspaceConnectorsRequest
- required: dry_run
- `dry_run`: boolean

## MigrateWorkspaceConnectorsResponse
- required: message
- `message`: string

## ModuleExecution
> ModuleExecution defines an individual execution of a module pipeline
- required: account, pipeline_org, pipeline_project, pipelineExecutionId, pipelineStageId, moduleId, pipeline
- `account`: string
- `module_onboarding`: boolean
- `moduleId`: string
- `pipeline`: string
- `pipeline_org`: string
- `pipeline_project`: string
- `pipelineExecutionId`: string
- `pipelineStageId`: string

## ModuleExecutionMetadata
- `pipeline`: string
- `pipeline_execution_id`: string
- `pipeline_execution_number`: string
- `pipeline_name`: string
- `pipeline_stage_id`: string
- `trigger`: object

## ModuleExecutionResourceCollection

## MonitoredService
> This is the Monitored Service entity defined in Harness
- required: identifier, name, orgIdentifier, projectIdentifier, serviceRef, type
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string
- `name`: string
- `type`: string; enum: Application, Infrastructure
- `description`: string
- `serviceRef`: string
- `environmentRef`: string
- `environmentRefList`: array
- `tags`: object
- `sources`: obj
- `dependencies`: array
- `notificationRuleRefs`: array
- `template`: obj
- `enabled`: boolean

## MonitoredServiceChangeDetailSLO
- `identifier`: string
- `name`: string
- `outOfRange`: boolean

## MonitoredServiceDetail
- `monitoredServiceIdentifier`: string
- `monitoredServiceName`: string
- `healthSourceIdentifier`: string
- `healthSourceName`: string
- `serviceIdentifier`: string
- `serviceName`: string
- `environmentIdentifier`: string
- `environmentName`: string
- `projectParams`: obj
- `projectName`: string
- `orgName`: string

## MonitoredServiceListItemDTO
- `name`: string
- `identifier`: string
- `serviceRef`: string
- `environmentRef`: string
- `environmentRefList`: array
- `serviceName`: string
- `environmentName`: string
- `type`: string; enum: Application, Infrastructure
- `healthMonitoringEnabled`: boolean
- `currentHealthScore`: obj
- `dependentHealthScore`: array
- `historicalTrend`: obj
- `changeSummary`: obj
- `tags`: object
- `serviceMonitoringEnabled`: boolean
- `storeType`: string; enum: INLINE, REMOTE, INLINE_HC
- `connectorRef`: string
- `entityGitDetails`: obj
- `sloHealthIndicators`: array

## MonitoredServiceMoveConfigResponse
> Tells us if the monitored service move config operation was successful or not
- `identifier`: string

## MonitoredServicePlatformResponse
- `name`: string
- `identifier`: string
- `serviceRef`: string
- `environmentRefs`: array
- `serviceName`: string
- `type`: string; enum: Application, Infrastructure
- `tags`: object
- `configuredChangeSources`: integer
- `configuredHealthSources`: integer
- `storeType`: string; enum: INLINE, REMOTE, INLINE_HC
- `connectorRef`: string
- `entityGitDetails`: obj

## MonitoredServiceReference
- `orgIdentifier`: string
- `projectIdentifier`: string
- `accountIdentifier`: string
- `identifier`: string
- `serviceIdentifier`: string
- `environmentIdentifiers`: array
- `lastReconciledTimestamp`: integer
- `reconciliationStatus`: string; enum: NO_RECONCILIATION_REQUIRED, INPUT_REQUIRED_FOR_RECONCILIATION, NO_INPUT_REQUIRED_FOR_RECONCILIATION

## MonitoredServiceResponse
- required: monitoredService
- `createdAt`: integer
- `lastModifiedAt`: integer
- `entityGitDetails`: obj
- `connectorRef`: string
- `monitoredService`: obj

## MonitoredServiceWithHealthSources
- `identifier`: string
- `name`: string
- `healthSources`: array

## MsTeamsConnector
> MsTeams Connector details.
- required: apiAccessType

## MultiEnvironmentInputVariable
> Input variable for multiEnvironment type
- required: type
- `type`: string; enum: multiEnvironment
- `description`: string
- `default`: array
- `metadata`: obj

## MultiInfrastructureInputVariable
> Input variable for multiInfrastructure type
- required: type
- `type`: string; enum: multiInfrastructure
- `description`: string
- `default`: array
- `metadata`: obj

## MultiRegionArtifactTriggerSource

## MultiRegionArtifactTriggerSpec
> Spec for Multi Region Artifact Triggers
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `type`: obj
- `sources`: array

## MultiServiceInputVariable
> Input variable for multiService type
- required: type
- `type`: string; enum: multiService
- `description`: string
- `default`: array
- `metadata`: obj

## NGProcessWebhookResponse
> This contains details about the triggered webhook
- `eventCorrelationId`: string
- `apiUrl`: string
- `uiUrl`: string
- `uiSetupUrl`: string

## NGTriggerDetailsResponseDTO
- `name`: string
- `identifier`: string
- `description`: string
- `type`: string; enum: Webhook, Artifact, Manifest, Scheduled, MultiRegionArtifact, SystemEvent
- `triggerStatus`: obj
- `lastTriggerExecutionDetails`: obj
- `webhookDetails`: obj
- `buildDetails`: obj
- `tags`: object
- `executions`: array
- `yaml`: string
- `webhookUrl`: string
- `webhookCurlCommand`: string
- `registrationStatus`: string; enum: SUCCESS, FAILED, ERROR, TIMEOUT, UNAVAILABLE
- `enabled`: boolean
- `isPipelineInputOutdated`: boolean
- `yamlVersion`: string
- `executorInfo`: obj
- `pipelineInputOutdated`: boolean

## NGTriggerEventHistoryBaseDTO
- `triggerIdentifier`: string
- `accountId`: string
- `eventCorrelationId`: string
- `payload`: string
- `headers`: object
- `eventCreatedAt`: integer
- `finalStatus`: string; enum: SCM_SERVICE_CONNECTION_FAILED, INVALID_PAYLOAD, TRIGGER_DID_NOT_MATCH_EVENT_CONDITION, TRIGGER_DID_NOT_MATCH_METADATA_CONDITION, TRIGGER_DID_NOT_MATCH_ARTIFACT_JEXL_CONDITION, NO_MATCHING_TRIGGER_FOR_REPO, NO_MATCHING_TRIGGER_FOR_EVENT_ACTION, NO_MATCHING_TRIGGER_FOR_METADATA_CONDITIONS, NO_MATCHING_TRIGGER_FOR_PAYLOAD_CONDITIONS, NO_MATCHING_TRIGGER_FOR_JEXL_CONDITIONS, NO_MATCHING_TRIGGER_FOR_HEADER_CONDITIONS, INVALID_RUNTIME_INPUT_YAML
- `message`: string
- `exceptionOccurred`: boolean
- `createdAt`: integer
- `triggerEventStatus`: obj

## NGTriggerEventHistoryDTO
- `triggerIdentifier`: string
- `accountId`: string
- `eventCorrelationId`: string
- `payload`: string
- `headers`: object
- `eventCreatedAt`: integer
- `finalStatus`: string; enum: SCM_SERVICE_CONNECTION_FAILED, INVALID_PAYLOAD, TRIGGER_DID_NOT_MATCH_EVENT_CONDITION, TRIGGER_DID_NOT_MATCH_METADATA_CONDITION, TRIGGER_DID_NOT_MATCH_ARTIFACT_JEXL_CONDITION, NO_MATCHING_TRIGGER_FOR_REPO, NO_MATCHING_TRIGGER_FOR_EVENT_ACTION, NO_MATCHING_TRIGGER_FOR_METADATA_CONDITIONS, NO_MATCHING_TRIGGER_FOR_PAYLOAD_CONDITIONS, NO_MATCHING_TRIGGER_FOR_JEXL_CONDITIONS, NO_MATCHING_TRIGGER_FOR_HEADER_CONDITIONS, INVALID_RUNTIME_INPUT_YAML
- `message`: string
- `exceptionOccurred`: boolean
- `createdAt`: integer
- `triggerEventStatus`: obj
- `orgIdentifier`: string
- `projectIdentifier`: string
- `targetIdentifier`: string
- `targetExecutionSummary`: obj
- `type`: string; enum: Webhook, Artifact, Manifest, Scheduled, MultiRegionArtifact, SystemEvent
- `ngTriggerEventInfo`: obj

## NGTriggerEventInfo

## NGTriggerEventsApiResponse
- required: triggerIdentifier
- `triggerIdentifier`: string
- `name`: string
- `scope`: obj
- `eventCorrelationId`: string
- `eventCreatedAt`: integer
- `message`: string
- `triggerEventStatus`: obj
- `ngTriggerType`: string; enum: Webhook, Artifact, Manifest, Scheduled, MultiRegionArtifact, SystemEvent
- `subTriggerType`: string
- `ngTriggerMetaData`: obj

## NGTriggerMetaData
- `pollingDocumentId`: string
- `build`: string

## NGTriggerResponse
> This contains the trigger details
- `name`: string
- `identifier`: string
- `description`: string
- `type`: string; enum: Webhook, Artifact, Manifest, Scheduled, MultiRegionArtifact, SystemEvent
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `targetIdentifier`: string
- `yaml`: string
- `enabled`: boolean
- `errors`: object
- `errorResponse`: boolean
- `stagesToExecute`: obj
- `yamlVersion`: string
- `webhookUrl`: string
- `executorInfo`: obj

## NGTriggerYamlRequest
> Trigger YAML and optional executor identity for create/update
- required: yaml
- `yaml`: string
- `executorInfo`: obj

## NGVariable
- `type`: string; enum: String, Number
- `description`: string
- `required`: boolean
- `name`: string
- `metadata`: string

## NGVariable1
- `name`: string
- `type`: string; enum: String, Number, Secret
- `description`: string
- `required`: boolean
- `metadata`: string

## NewRelicConnectorDTO
- required: apiKeyRef, newRelicAccountId, url

## Nexus2RegistryArtifactTriggerSpec
- `connector_ref`: string
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `repository_name`: string
- `repository_format`: string
- `artifact_id`: string
- `package_name`: string
- `group_id`: string
- `repository_url`: string
- `classifier`: string
- `extension`: string
- `tag`: string

## Nexus3RegistryArtifactTriggerSpec
- `connector_ref`: string
- `event_conditions`: array
- `meta_data_conditions`: array
- `jexl_condition`: string
- `repository`: string
- `image_path`: string
- `repository_format`: string
- `artifact_id`: string
- `package_name`: string
- `group_id`: string
- `repository_url`: string
- `classifier`: string
- `extension`: string
- `group`: string
- `tag`: string

## NexusConnector
> Nexus Connector details.
- required: nexusServerUrl, version

## NodeExecutionDetails
> This contains the Node Execution Graph details.
- `executionGraph`: obj

## NodeExecutionEventData
- required: type

## NodeExecutionOutline
> This is the view of the Node Execution Outline
- `nodeType`: string
- `nodeGroup`: string
- `nodeIdentifier`: string
- `name`: string
- `nodeUuid`: string
- `status`: string; enum: Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted, Discontinuing, Queued
- `startTs`: integer
- `endTs`: integer
- `failureInfo`: string
- `nodeExecutionId`: string
- `edgeLayoutList`: obj

## NotificationTemplateInputsDTO
- required: name, value
- `name`: string
- `value`: string
- `type`: string

## NumberNGVariable

## NumberNGVariable1
- required: value

## OciHelmConnector
> This contains Oci helm connector details
- required: helmRepoUrl

## OpenAIConnector
> This contains details of the OpenAI connector
- required: authentication

## OpenapiCreateRepoWebhookRequest
- `description`: string
- `display_name`: string
- `enabled`: boolean
- `extra_headers`: array
- `identifier`: string
- `insecure`: boolean
- `secret`: string
- `triggers`: array
- `uid`: string
- `url`: string

## OpenapiUpdateRepoWebhookRequest
- `description`: string
- `display_name`: string
- `enabled`: boolean
- `extra_headers`: array
- `identifier`: string
- `insecure`: boolean
- `secret`: string
- `triggers`: array
- `uid`: string
- `url`: string

## OpenapiUpdateSpaceWebhookRequest
- `description`: string
- `display_name`: string
- `enabled`: boolean
- `extra_headers`: array
- `identifier`: string
- `insecure`: boolean
- `secret`: string
- `triggers`: array
- `uid`: string
- `url`: string

## OpenapiWebhookType
- `created`: integer
- `created_by`: integer
- `description`: string
- `display_name`: string
- `enabled`: boolean
- `extra_headers`: array
- `has_secret`: boolean
- `id`: integer
- `identifier`: string
- `insecure`: boolean
- `latest_execution_result`: obj
- `parent_id`: integer
- `parent_type`: obj
- `scope`: integer
- `triggers`: array
- `updated`: integer
- `url`: string
- `version`: integer

## OpsGenieConnectorDTO
- required: url, username

## OrchestrationActivityPipelineYaml
> Pipeline configuration for orchestration activities
- required: pipeline
- `pipeline`: string
- `inputSet`: object
- `stages`: array
- `expression`: object

## OrchestrationExecutionActivity
> Represents an activity in the orchestration execution
- required: identifier, name, status, yaml, depends_on
- `identifier`: string
- `name`: string
- `description`: string
- `status`: obj
- `start_ts`: integer
- `end_ts`: integer
- `yaml`: string
- `depends_on`: array
- `activity_execution_id`: string
- `retry_index`: integer
- `pipeline`: obj
- `subprocess`: obj
- `failureInfo`: obj

## OrchestrationExecutionActivityDetail
> Detailed information about an activity execution
- required: identifier, name, status, yaml, phaseIdentifier, phaseName, activity_execution_id, phase_execution_id, process_execution_id
- `identifier`: string
- `name`: string
- `status`: obj
- `yaml`: string
- `phaseIdentifier`: string
- `phaseName`: string
- `activity_execution_id`: string
- `phase_execution_id`: string
- `process_execution_id`: string
- `retry_index`: integer
- `retry_id`: string
- `root_retry_id`: string
- `start_ts`: integer
- `end_ts`: integer
- `triggerInfo`: obj
- `pipeline`: obj
- `subprocess`: obj
- `failureInfo`: obj

## OrchestrationExecutionActivityPaginated
> Represents an activity in the paginated orchestration execution activities response
- required: identifier, name, status, phaseIdentifier, phaseName, rootReleaseId, type, phaseExecutionId, processExecutionId
- `identifier`: string
- `name`: string
- `status`: obj
- `phaseIdentifier`: string
- `phaseName`: string
- `rootReleaseId`: string
- `type`: string; enum: PIPELINE, SUBPROCESS, MANUAL
- `startTs`: integer
- `endTs`: integer
- `processExecutionId`: string
- `phaseExecutionId`: string
- `activityExecutionId`: string
- `retryIndex`: integer
- `retryId`: string
- `failureInfo`: obj
- `triggerInfo`: obj
- `pipeline`: obj
- `subprocess`: obj
- `manual`: obj

## OrchestrationExecutionPhase
> Represents a phase in the orchestration execution
- required: name, identifier, status, completed_activities, total_activities, activityCounts
- `name`: string
- `identifier`: string
- `description`: string
- `owners`: array
- `depends_on`: array
- `status`: obj
- `start_ts`: integer
- `end_ts`: integer
- `phase_execution_id`: string
- `completed_activities`: integer
- `total_activities`: integer
- `activityCounts`: obj
- `failureInfo`: obj

## OrchestrationModelPipeline
- `scorecard`: object
- `orchestration_id`: string
- `stage_identifier`: string
- `stage_execution_identifier`: string
- `stage_name`: string
- `step_identifier`: string
- `step_name`: string
- `step_execution_identifier`: string
- `drift`: obj

## OverlayInputSetResponse
> This contains Overlay Input Set details.
- `accountId`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `pipelineIdentifier`: string
- `identifier`: string
- `name`: string
- `description`: string
- `inputSetReferences`: array
- `overlayInputSetYaml`: string
- `tags`: object
- `isOutdated`: boolean
- `isErrorResponse`: boolean
- `invalidInputSetReferences`: object
- `gitDetails`: obj
- `entityValidityDetails`: obj
- `errorResponse`: boolean
- `outdated`: boolean

## PMSPipelineResponse
> This contains pipeline yaml with the version.
- `yamlPipeline`: string
- `resolvedTemplatesPipelineYaml`: string
- `gitDetails`: obj
- `entityValidityDetails`: obj
- `modules`: array
- `governanceMetadata`: obj
- `yamlSchemaErrorWrapper`: obj
- `validateTemplateInputsResponse`: obj
- `cacheResponse`: obj
- `validationUuid`: string
- `storeType`: string; enum: INLINE, REMOTE, INLINE_HC
- `publicAccessResponse`: obj
- `connectorRef`: string
- `allowDynamicExecutions`: boolean
- `isInlineHCEntity`: boolean

## PMSPipelineSummaryResponse
> This is the view of the Pipeline Summary for Pipeline entity defined in Harness.
- `name`: string
- `identifier`: string
- `description`: string
- `tags`: object
- `version`: integer
- `numOfStages`: integer
- `createdAt`: integer
- `lastUpdatedAt`: integer
- `modules`: array
- `executionSummaryInfo`: obj
- `filters`: object
- `stageNames`: array
- `gitDetails`: obj
- `entityValidityDetails`: obj
- `storeType`: string; enum: INLINE, REMOTE, INLINE_HC
- `connectorRef`: string
- `isDraft`: boolean
- `yamlVersion`: string
- `isInlineHCEntity`: boolean
- `enableDAG`: boolean

## PRCommentBitbucketWebhookSpec

## PageActiveMonitoredService
- `totalElements`: integer
- `totalPages`: integer
- `last`: boolean
- `size`: integer
- `content`: array
- `number`: integer
- `sort`: obj
- `pageable`: obj
- `numberOfElements`: integer
- `first`: boolean
- `empty`: boolean

## PageNGTriggerEventHistoryBaseDTO
- `totalElements`: integer
- `totalPages`: integer
- `size`: integer
- `content`: array
- `number`: integer
- `sort`: obj
- `first`: boolean
- `pageable`: obj
- `numberOfElements`: integer
- `last`: boolean
- `empty`: boolean

## PageNGTriggerEventHistoryDTO
- `totalElements`: integer
- `totalPages`: integer
- `size`: integer
- `content`: array
- `number`: integer
- `sort`: obj
- `first`: boolean
- `pageable`: obj
- `numberOfElements`: integer
- `last`: boolean
- `empty`: boolean

## PageNGTriggerEventsApiResponse
- `totalElements`: integer
- `totalPages`: integer
- `size`: integer
- `content`: array
- `number`: integer
- `sort`: obj
- `first`: boolean
- `pageable`: obj
- `numberOfElements`: integer
- `last`: boolean
- `empty`: boolean

## PagePMSPipelineSummaryResponse
- `totalElements`: integer
- `totalPages`: integer
- `size`: integer
- `content`: array
- `number`: integer
- `sort`: obj
- `first`: boolean
- `pageable`: obj
- `numberOfElements`: integer
- `last`: boolean
- `empty`: boolean

## PagePipelineExecutionIdentifierSummary
- `totalElements`: integer
- `totalPages`: integer
- `size`: integer
- `content`: array
- `number`: integer
- `sort`: obj
- `first`: boolean
- `pageable`: obj
- `numberOfElements`: integer
- `last`: boolean
- `empty`: boolean

## PagePipelineExecutionSummary
- `totalElements`: integer
- `totalPages`: integer
- `size`: integer
- `content`: array
- `number`: integer
- `sort`: obj
- `first`: boolean
- `pageable`: obj
- `numberOfElements`: integer
- `last`: boolean
- `empty`: boolean

## PageQueuedPipelineExecution
> Paginated list of executions (queued, waiting, and/or running, depending on the requested mode)
- `totalElements`: integer
- `totalPages`: integer
- `size`: integer
- `content`: array
- `number`: integer
- `sort`: obj
- `first`: boolean
- `pageable`: obj
- `numberOfElements`: integer
- `last`: boolean
- `empty`: boolean

## PageResponseConnectorResponse
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseEnvironmentGroup
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseEnvironmentIdentifierResponse
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseEnvironmentResponse
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseFreezeSummaryResponse
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseInfrastructureResponse
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseInputSetListResponse
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseInputSetSummaryResponse
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseMonitoredServiceListItemDTO
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseMonitoredServicePlatformResponse
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseMonitoredServiceReference
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseMonitoredServiceResponse
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseNGTriggerDetailsResponseDTO
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseSecretResponse
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseServiceAccount
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseServiceAccountAggregate
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseServiceLevelObjectiveV2Response
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseServiceOverrideResponse
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseServiceResponse
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageResponseVariableResponseDTO
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `content`: array
- `pageIndex`: integer
- `empty`: boolean
- `pageToken`: string

## PageTemplateMetadataSummaryResponse
- `totalElements`: integer
- `totalPages`: integer
- `size`: integer
- `content`: array
- `number`: integer
- `sort`: obj
- `first`: boolean
- `pageable`: obj
- `numberOfElements`: integer
- `last`: boolean
- `empty`: boolean

## PagerDutyConnectorDTO
- required: apiTokenRef

## ParameterFieldSecretRefData
- `expressionValue`: string
- `expression`: boolean
- `value`: string
- `defaultValue`: string
- `typeString`: boolean
- `inputSetValidator`: obj
- `jsonResponseField`: boolean
- `responseField`: string
- `executionInput`: boolean

## ParserAsyncChainExecutableResponse

## ParserAsyncExecutableResponse

## ParserChildChainExecutableResponse

## ParserChildExecutableResponse

## ParserChildrenExecutableResponse

## ParserExecutableResponse

## ParserExecutionErrorInfo

## ParserExecutionMetadata

## ParserExecutionPrincipalInfo

## ParserExecutionTriggerInfo

## ParserFacilitatorExecutableResponse

## ParserInputSetReferenceProtoDTO

## ParserPipelineStageInfo

## ParserPostExecutionRollbackInfo

## ParserRetryExecutionInfo

## ParserServiceDescriptorProto

## ParserServiceOptions

## ParserSkipTaskExecutableResponse

## ParserSyncExecutableResponse

## ParserTaskChainExecutableResponse

## ParserTaskExecutableResponse

## ParserTemplateReferenceProtoDTO

## ParserTemplateReferenceSummary

## ParserTriggerPayload

## ParserTriggerReferenceProtoDTO

## ParserTriggeredBy

## PerpetualTaskInfoForTriggers
- `state`: string
- `unassignedReason`: string
- `taskDescription`: string
- `createdAt`: integer
- `delegateId`: string
- `delegateHostName`: string

## PhysicalDataCenterConnectorDTO
> This contains Physical Data Center connector details

## PipelineActivityInfo
> Pipeline execution information for activities
- required: executionId, identifier
- `executionId`: string
- `identifier`: string

## PipelineAnnotation
- required: contextId, priority, style, summary, timestamp
- `contextId`: string
- `timestamp`: integer
- `style`: string; enum: success, error, info, warning
- `summary`: string
- `priority`: integer

## PipelineAnnotationsResponseDTO
- required: accountId, annotations, createdAt, lastUpdatedAt, orgId, pipelineId, planExecutionId, projectId
- `accountId`: string
- `orgId`: string
- `projectId`: string
- `pipelineId`: string
- `planExecutionId`: string
- `annotations`: array
- `createdAt`: integer
- `lastUpdatedAt`: integer

## PipelineApproval
- required: approvalID, pipelineExecutionId, orgID, projectID, message
- `approvalID`: string
- `deadline`: string
- `message`: string
- `orgID`: string
- `pipelineExecutionId`: string
- `pipelineId`: string
- `pipelineUrl`: string
- `projectID`: string

## PipelineBuildInfoDetailV3
> Pipeline build info detail entry.
- required: pipelineIdentifier, orgIdentifier, projectIdentifier, stageIdentifier, stepIdentifier, violations, rootPackageName, rootPackageVersion, packageType, securityViolationCategories
- `lastExecutionTime`: integer
- `orgIdentifier`: string
- `packageType`: obj
- `pipelineExecutionIdentifier`: string
- `pipelineIdentifier`: string
- `projectIdentifier`: string
- `rootPackageName`: string
- `rootPackageVersion`: string
- `securityViolationCategories`: array
- `stageIdentifier`: string
- `stepIdentifier`: string
- `violations`: array

## PipelineBuildInfoMetaV3
> Aggregated metadata for pipeline build info results.
- `totalBlockedDependencies`: integer
- `totalBlockedPipelines`: integer

## PipelineBuildInfoViolationV3
> A violation entry mapping a package key to a scan ID.
- required: package, scanId, status, purl, securityViolationCategories
- `package`: string
- `purl`: string
- `scanId`: string
- `securityViolationCategories`: array
- `status`: string; enum: BLOCKED, WARN

## PipelineConfigUpdateRequest
- `target_version`: integer

## PipelineContextV3
> Pipeline execution context.
- required: pipelineId, executionId, orgId, projectId, stageId
- `executionId`: string
- `orgId`: string
- `pipelineId`: string
- `projectId`: string
- `stageId`: string
- `stepId`: string

## PipelineCount
> This is the view of the Pipeline Execution Count Info for a particular Date
- `total`: integer
- `success`: integer
- `failure`: integer
- `expired`: integer
- `aborted`: integer

## PipelineCreateRequestBody
> Pipeline request body object 
- required: pipeline_yaml, identifier, name
- `pipeline_yaml`: string
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `git_details`: obj

## PipelineCreateResponseBody
> Pipeline response body
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128

## PipelineDetails
- `org_id`: string
- `project_id`: string
- `name`: string
- `execution_id`: string
- `id`: string
- `triggered_by`: string
- `triggered_by_id`: string
- `triggered_at`: integer
- `triggered_type`: string
- `status`: string; enum: PASSED, FAILED, UNKNOWN
- `stage_execution_id`: string
- `step_execution_id`: string
- `stage_type`: string; enum: BUILD, DEPLOY, SECURITY

## PipelineEntityGitDetails
> This contains Validity Details of the Entity
- `valid`: boolean
- `invalidYaml`: string

## PipelineError
> This is Error entity as defined in Harness
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `code`: string; enum: DEFAULT_ERROR_CODE, INVALID_ARGUMENT, INVALID_EMAIL, DOMAIN_NOT_ALLOWED_TO_REGISTER, COMMNITY_EDITION_NOT_FOUND, DEPLOY_MODE_IS_NOT_ON_PREM, USER_ALREADY_REGISTERED, USER_INVITATION_DOES_NOT_EXIST, USER_DOES_NOT_EXIST, USER_INVITE_OPERATION_FAILED, USER_DISABLED, ACCOUNT_DOES_NOT_EXIST
- `message`: string
- `correlationId`: string
- `detailedMessage`: string
- `responseMessages`: array
- `metadata`: obj

## PipelineErrorMetadata
> This implements different error meta data objects
- `type`: string

## PipelineEventNotificationParamsDTO

## PipelineExecuteRequestBody
- `inputs_yaml`: string

## PipelineExecuteResponseBody
- `execution_details`: obj

## PipelineExecution
> This is the view of the Pipeline Executions for a particular Date
- `date`: integer
- `count`: obj

## PipelineExecutionCountInfo
- `executionCountGroupedOnServiceList`: array

## PipelineExecutionDetail
> This contains the Pipeline Execution details.
- `pipelineExecutionSummary`: obj
- `executionGraph`: obj
- `childGraph`: obj

## PipelineExecutionFilterProperties
> Filter properties for listing pipeline executions. The `filterType` field (inherited) is required and must be set to `PipelineExecution`.
- required: filterType
- `tags`: object
- `filterType`: string; enum: Connector, Secret, DelegateProfile, Delegate, PipelineSetup, PipelineExecution, Deployment, Audit, Template, Trigger, EnvironmentGroup, FileStore
- `pipelineTags`: array
- `pipelineTagsV2`: obj
- `pipelineLabels`: array
- `status`: array
- `pipelineName`: string
- `timeRange`: obj
- `moduleProperties`: obj
- `triggerTypes`: array
- `triggerIdentifiers`: array
- `executionModeFilter`: string; enum: ROLLBACK, ALL, DEFAULT
- `pipelineIdentifiers`: array
- `myDeployments`: boolean
- `branchName`: string
- `repo`: string
- `inputSetIdentifiers`: array
- `planExecutionIds`: array
- `executionNotes`: array

## PipelineExecutionIdentifierSummary
> This is the view of the Pipeline Execution Identifier Summary
- required: orgIdentifier, projectIdentifier
- `pipelineIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `planExecutionId`: string
- `status`: string; enum: Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted, Discontinuing, Queued
- `runSequence`: integer

## PipelineExecutionMetadata
> Pipeline execution details
- required: pipeline, planExecutionId, stageExecutionId
- `pipeline`: string
- `planExecutionId`: string
- `stageExecutionId`: string

## PipelineExecutionNotes
> Notes of a pipeline execution
- `notes`: string

## PipelineExecutionOutline
> This is the view of the Pipeline Execution Outline
- required: accountIdentifier, orgIdentifier, projectIdentifier
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `pipelineIdentifier`: string
- `planExecutionId`: string
- `name`: string
- `startingNodeId`: string
- `startingNodeIds`: array
- `isDagEnabled`: boolean
- `dependencyGraph`: object
- `status`: string; enum: Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted, Discontinuing, Queued
- `failureInfo`: string
- `stagesMap`: object
- `modules`: array
- `startTs`: integer
- `endTs`: integer
- `createdAt`: integer
- `lastUpdatedAt`: integer
- `runtimeInputYaml`: string
- `runSequence`: integer

## PipelineExecutionOutlineFilterDTO
- `status`: array
- `timeRange`: obj
- `pipelineIdentifier`: string
- `planExecutionIds`: array

## PipelineExecutionSummary
> This is the view of the Pipeline Execution Summary
- required: orgIdentifier, projectIdentifier
- `pipelineIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `planExecutionId`: string
- `name`: string
- `yamlVersion`: string
- `status`: string; enum: Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted, Discontinuing, Queued
- `tags`: array
- `labels`: array
- `executionTriggerInfo`: obj
- `executionErrorInfo`: obj
- `governanceMetadata`: obj
- `failureInfo`: obj
- `retryExecutionMetadata`: obj
- `moduleInfo`: object
- `layoutNodeMap`: object
- `modules`: array
- `startingNodeId`: string
- `startingNodeIds`: array
- `isDagEnabled`: boolean
- `dependencyGraph`: object
- `startTs`: integer
- `endTs`: integer
- `createdAt`: integer
- `canRetry`: boolean
- `canReExecute`: boolean
- `showRetryHistory`: boolean
- `isRetriedExecution`: boolean
- `runSequence`: integer
- `successfulStagesCount`: integer
- `runningStagesCount`: integer
- `failedStagesCount`: integer
- `totalStagesCount`: integer
- `gitDetails`: obj
- `storeType`: string; enum: INLINE, REMOTE, INLINE_HC
- `connectorRef`: string
- `executionInputConfigured`: boolean
- `isStagesExecution`: boolean
- `parentStageInfo`: obj
- `stagesExecuted`: array
- `stagesExecutedNames`: object
- `allowStageExecutions`: boolean
- `abortedBy`: obj
- `executionMode`: string; enum: UNDEFINED_MODE, NORMAL, POST_EXECUTION_ROLLBACK, PIPELINE_ROLLBACK, UNRECOGNIZED
- `notesExistForPlanExecutionId`: boolean
- `shouldUseSimplifiedKey`: boolean
- `isDynamicExecution`: boolean
- `isOriginalYamlUsedOnRerun`: boolean
- `inputSetIdentifiers`: array
- `queuedType`: string; enum: MAX_CONCURRENCY_REACHED, MAX_CONCURRENCY_NOT_REACHED, PRIORITY_CONCURRENCY_REACHED
- `queuedReason`: string
- `templateReferenceSummary`: obj
- `notes`: string
- `retriedExecution`: boolean
- `dynamicExecution`: boolean
- `originalYamlUsedOnRerun`: boolean
- `stagesExecution`: boolean

## PipelineFilterProperties
> Properties of the Pipelines Filter defined in Harness
- required: filterType
- `tags`: object
- `filterType`: string; enum: Connector, Secret, DelegateProfile, Delegate, PipelineSetup, PipelineExecution, Deployment, Audit, Template, Trigger, EnvironmentGroup, FileStore
- `pipelineTags`: array
- `pipelineIdentifiers`: array
- `name`: string
- `description`: string
- `moduleProperties`: object
- `repoName`: string

## PipelineGetResponseBody
> Pipeline response body.
- `pipeline_yaml`: string
- `template_applied_pipeline_yaml`: string
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `org`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `project`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `modules`: array
- `git_details`: obj
- `valid`: boolean
- `yaml_error_wrapper`: array
- `cache_response_metadata`: obj
- `created`: integer
- `updated`: integer
- `validation_uuid`: string

## PipelineGovernanceMetadata
- `unknownFields`: obj
- `message`: string
- `id`: string
- `type`: string
- `timestamp`: integer
- `initialized`: boolean
- `entity`: string
- `created`: integer
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `typeBytes`: obj
- `messageBytes`: obj
- `status`: string
- `idBytes`: obj
- `detailsOrBuilderList`: array
- `entityBytes`: obj
- `actionBytes`: obj
- `accountId`: string
- `orgId`: string
- `projectId`: string
- `statusBytes`: obj
- `accountIdBytes`: obj
- `orgIdBytes`: obj
- `projectIdBytes`: obj
- `deny`: boolean
- `detailsList`: array
- `action`: string
- `detailsCount`: integer
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## PipelineImportRequest
> Contains basic information required to be linked with imported Pipeline YAML
- `pipelineName`: string
- `pipelineDescription`: string
- `version`: string

## PipelineImportRequestBody
> Pipeline import request body
- `git_import_info`: obj
- `pipeline_import_request`: obj

## PipelineImportRequestDTO
> Information of Pipeline import request DTO
- `pipeline_name`: string
- `pipeline_description`: string

## PipelineInfo
- `name`: string
- `execution_id`: string
- `id`: string
- `triggered_by`: string
- `triggered_by_id`: string
- `triggered_at`: integer
- `triggered_type`: string

## PipelineInfraConfigRequestBody
> Infra Config Details of Pipeline
- required: spec
- `org`: string
- `project`: string
- `spec`: string
- `allow_override`: boolean

## PipelineInputSchemaDetailsResponseBody
- `inputs`: array

## PipelineInputSetError
> This contains the error details for a field while saving an Input Set
- `fieldName`: string
- `message`: string
- `identifierOfErrorSource`: string

## PipelineInputsSchemaRequestBody
- `pipeline_yaml`: string

## PipelineListResponseBody
> Pipeline List response body
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `created`: integer
- `updated`: integer
- `modules`: array
- `recent_execution_info`: array
- `store_type`: string; enum: INLINE, REMOTE
- `connector_ref`: string
- `valid`: boolean
- `git_details`: obj
- `yaml_version`: string

## PipelineMoveConfigRequestBody
> Request body for moving a pipeline configuration
- `git_details`: obj
- `pipeline_identifier`: string
- `move_config_operation_type`: obj

## PipelineMoveConfigResponseBody
> Response body for configuration to move a pipeline
- `pipeline_identifier`: string

## PipelineNodeInfo
- `identifier`: string
- `name`: string
- `localFqn`: string

## PipelinePatchRequestBody
> Pipeline Patch Request body (All the non empty values in this request body will be updated).
- `pipeline_yaml`: string
- `name`: string
- `desc`: string
- `tags`: object
- `git_details`: obj
- `version`: string

## PipelinePolicyMetadata
- `unknownFields`: obj
- `severity`: string
- `initialized`: boolean
- `identifier`: string
- `created`: integer
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `identifierBytes`: obj
- `status`: string
- `denyMessagesList`: array
- `policyId`: string
- `policyName`: string
- `accountId`: string
- `orgId`: string
- `projectId`: string
- `updated`: integer
- `error`: string
- `denyMessagesCount`: integer
- `policyIdBytes`: obj
- `policyNameBytes`: obj
- `severityBytes`: obj
- `statusBytes`: obj
- `accountIdBytes`: obj
- `orgIdBytes`: obj
- `projectIdBytes`: obj
- `errorBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## PipelinePolicySetMetadata
- `unknownFields`: obj
- `initialized`: boolean
- `description`: string
- `identifier`: string
- `created`: integer
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `identifierBytes`: obj
- `status`: string
- `accountId`: string
- `orgId`: string
- `projectId`: string
- `statusBytes`: obj
- `accountIdBytes`: obj
- `orgIdBytes`: obj
- `projectIdBytes`: obj
- `policySetId`: string
- `deny`: boolean
- `policyMetadataList`: array
- `policySetName`: string
- `policyMetadataCount`: integer
- `policySetIdBytes`: obj
- `policyMetadataOrBuilderList`: array
- `policySetNameBytes`: obj
- `descriptionBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## PipelinePolicySetMetadataOrBuilder
- `description`: string
- `identifier`: string
- `created`: integer
- `identifierBytes`: obj
- `status`: string
- `accountId`: string
- `orgId`: string
- `projectId`: string
- `statusBytes`: obj
- `accountIdBytes`: obj
- `orgIdBytes`: obj
- `projectIdBytes`: obj
- `policySetId`: string
- `deny`: boolean
- `policyMetadataList`: array
- `policySetName`: string
- `policyMetadataCount`: integer
- `policySetIdBytes`: obj
- `policyMetadataOrBuilderList`: array
- `policySetNameBytes`: obj
- `descriptionBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## PipelineSaveResponse
> Contains the Pipeline details for the given Pipeline ID
- `identifier`: string
- `governanceMetadata`: obj
- `publicAccessResponse`: obj

## PipelineSaveResponseBody
> Response body for pipeline save.
- `identifier`: string
- `governance_metadata`: array

## PipelineScope
- required: accountIdentifier
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `parentUniqueId`: string

## PipelineSecurityCounts
- required: new, existing, remediated, totalActive
- `activeIssueCount`: integer
- `existing`: obj
- `new`: obj
- `remediated`: obj
- `totalActive`: integer
- `totalApp`: integer
- `totalBase`: integer
- `totalDeduplicationRate`: number
- `totalExempted`: integer
- `totalNoLayer`: integer
- `totalNumOccurrence`: integer
- `totalPartiallyExempted`: integer
- `totalPending`: integer
- `totalRejected`: integer
- `totalRemediated`: integer

## PipelineSecurityIssuesResult
> Data needed by the PipelineSecurityView
- required: existing, new, counts, matchingSteps
- `counts`: obj
- `existing`: obj
- `matchingSteps`: array
- `new`: obj

## PipelineSecurityIssuesV2Result
> Combined, paginated list of pipeline security issues for the PipelineSecurityView
- required: issues, counts, matchingSteps
- `counts`: obj
- `issues`: obj
- `matchingSteps`: array

## PipelineSecurityStepsResult
- required: steps, reachabilityFlag, exploitabilityFlag
- `exploitabilityFlag`: boolean
- `reachabilityFlag`: boolean
- `steps`: array

## PipelineStageInfo
- `unknownFields`: obj
- `initialized`: boolean
- `identifier`: string
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `identifierBytes`: obj
- `runSequence`: integer
- `orgId`: string
- `projectId`: string
- `orgIdBytes`: obj
- `projectIdBytes`: obj
- `pipelineName`: string
- `hasParentPipeline`: boolean
- `stageNodeId`: string
- `executionId`: string
- `pipelineNameBytes`: obj
- `stageNodeIdBytes`: obj
- `executionIdBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## PipelineStageInfoOrBuilder
- `identifier`: string
- `identifierBytes`: obj
- `runSequence`: integer
- `orgId`: string
- `projectId`: string
- `orgIdBytes`: obj
- `projectIdBytes`: obj
- `pipelineName`: string
- `hasParentPipeline`: boolean
- `stageNodeId`: string
- `executionId`: string
- `pipelineNameBytes`: obj
- `stageNodeIdBytes`: obj
- `executionIdBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## PipelineStatusOutput
> Response body for Pipeline execution status
- required: status, response, metadata
- `metadata`: object
- `response`: string
- `status`: string

## PipelineStoreConfigRequestBody
> Remote Config Details of Pipeline
- required: scan_type, repo, base_branch
- `scan_type`: obj
- `connector_id`: string
- `repo`: string
- `base_branch`: string
- `yaml_path`: string

## PipelineTemplateResponse
> This contains details of the Template Response
- required: accountId, identifier, name, yaml
- `accountId`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string
- `name`: string
- `description`: string; maxLen 1024
- `tags`: object
- `yaml`: string
- `mergedYaml`: string
- `versionLabel`: string
- `isStableTemplate`: boolean
- `labels`: array
- `enableDAG`: boolean
- `templateEntityType`: string; enum: Step, Stage, Pipeline, CustomDeployment, MonitoredService, SecretManager, ArtifactSource, StepGroup, Workspace, Notification, Agent
- `childType`: string
- `templateScope`: string; enum: account, org, project, unknown
- `version`: integer
- `gitDetails`: obj
- `entityValidityDetails`: obj
- `lastUpdatedAt`: integer
- `storeType`: string; enum: INLINE, REMOTE, INLINE_HC
- `connectorRef`: string
- `icon`: string
- `cacheResponseMetadata`: obj
- `yamlVersion`: string
- `bulkReconcileUUID`: string
- `hasInsert`: boolean
- `isInlineHCEntity`: boolean
- `stableTemplate`: boolean

## PipelineUpdateRequestBody
> Pipeline request body object 
- required: pipeline_yaml, identifier, name
- `pipeline_yaml`: string
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `git_details`: obj

## PipelineUser
- `unknownFields`: obj
- `name`: string
- `id`: string
- `initialized`: boolean
- `created`: obj
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `nameBytes`: obj
- `idBytes`: obj
- `updated`: obj
- `email`: string
- `login`: string
- `avatar`: string
- `loginBytes`: obj
- `emailBytes`: obj
- `avatarBytes`: obj
- `createdOrBuilder`: obj
- `updatedOrBuilder`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## PipelineValidationResponseBody
> Pipeline Validation Response Body
- `status`: string
- `policy_eval`: object
- `start_ts`: integer
- `end_ts`: integer
- `template_validation_response`: obj

## PipelineValidationUUIDResponseBody
> Contains the UUID of the Pipeline Validation Event that's started
- `uuid`: string

## PipelineYamlInputDTO
- `name`: string
- `type`: obj
- `desc`: string
- `required`: boolean
- `execution`: boolean
- `default`: object
- `allowed_values`: array
- `regex`: string

## PipelineYamlInputDetailsDTO
- `details`: obj
- `metadata`: obj

## PipelineYamlInputMetadataDTO
- `field_properties`: array
- `dependencies`: obj

## PlanExecution
- `uuid`: string
- `createdAt`: integer
- `planId`: string
- `setupAbstractions`: object
- `validUntil`: string
- `status`: string; enum: NO_OP, RUNNING, INTERVENTION_WAITING, TIMED_WAITING, ASYNC_WAITING, TASK_WAITING, DISCONTINUING, PAUSING, QUEUED, SKIPPED, PAUSED, ABORTED
- `startTs`: integer
- `endTs`: integer
- `metadata`: obj
- `governanceMetadata`: obj
- `triggerHeader`: array
- `triggerJsonPayload`: string
- `expressionFunctorToken`: integer
- `triggerPayload`: obj
- `stageExpressionValuesMap`: object
- `stagesExecutionMetadata`: obj
- `processedYaml`: string
- `postExecutionRollbackInfos`: array
- `lastUpdatedAt`: integer
- `version`: integer
- `nextIteration`: integer
- `ambiance`: obj
- `failureInfo`: obj
- `priorityType`: string; enum: HIGH, LOW, NORMAL
- `nodeType`: string; enum: PLAN, PLAN_NODE, IDENTITY_PLAN_NODE
- `nodeId`: string

## PlanExecutionResponse
> This contains info about the Pipeline Execution
- `planExecution`: obj
- `gitDetails`: obj

## PollingInfoForTriggers
- `perpetualTaskId`: string
- `polledResponse`: obj
- `pollingDocId`: string
- `perpetualTaskInfoForTriggers`: obj

## PostExecutionRollbackInfo
- `unknownFields`: obj
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `originalStageExecutionId`: string
- `postExecutionRollbackStageId`: string
- `rollbackStageStrategyMetadata`: obj
- `postExecutionRollbackStageIdBytes`: obj
- `rollbackStageStrategyMetadataOrBuilder`: obj
- `originalStageExecutionIdBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## PostProdRollbackCheckDTO
- `isRollbackAllowed`: boolean
- `message`: string
- `swimLaneInfo`: obj
- `rollbackAllowed`: boolean

## PostProdRollbackRequestDTO
- required: infrastructureMappingId, instanceKey
- `instanceKey`: string
- `infrastructureMappingId`: string

## PostProdRollbackResponseDTO
- `isRollbackTriggered`: boolean
- `instanceKey`: string
- `infraMappingId`: string
- `planExecutionId`: string
- `message`: string
- `rollbackTriggered`: boolean

## PostProdRollbackSwimLaneInfo

## PrimitiveInputVariable
> Input variable for primitive types (string, list, boolean, number, object)
- required: type
- `type`: string; enum: string, list, boolean, number, object
- `description`: string
- `default`: string

## PrometheusConnectorDTO
- required: url

## ProtectionDefApprovals
- `require_code_owners`: boolean
- `require_latest_commit`: boolean
- `require_minimum_count`: integer
- `require_minimum_default_reviewer_count`: integer
- `require_no_change_request`: boolean

## ProviderConnectorWithPermissions
- required: uuid, connector_ref, type, created, updated, source, isInWorkspace, permissions, inUse, isLocked
- `associatedTemplate`: string
- `associatedVariableSet`: string
- `connector_ref`: string
- `created`: integer
- `inUse`: boolean
- `isInWorkspace`: boolean
- `isLocked`: boolean
- `permissions`: obj
- `source`: string; enum: workspace, template, variableSet
- `type`: string; enum: aws, azure, gcp, vault
- `updated`: integer
- `uuid`: string

## PullRequestAzureRepoWebhookSpec

## PullRequestBitbucketWebhookSpec

## PullRequestGithubWebhookSpec

## PullRequestHarnessWebhookSpec

## PushAwsCodeCommitWebhookTriggerSpec
- `connector_ref`: string
- `repo_name`: string
- `payload_conditions`: array
- `jexl_condition`: string

## PushAzureRepoWebhookSpec

## PushBitbucketWebhookSpec

## PushGithubWebhookSpec

## PushGitlabWebhookSpec

## PushHarnessWebhookSpec

## QueuedPipelineBulkAbortRequest
> Request to bulk abort queued pipeline executions
- required: planExecutionIds
- `planExecutionIds`: array

## QueuedPipelineBulkAbortResponse
> Response for bulk abort of queued pipeline executions
- `results`: array
- `successCount`: integer
- `failureCount`: integer

## QueuedPipelineBulkAbortResult
> Result of aborting a single queued pipeline execution
- `planExecutionId`: string
- `success`: boolean
- `errorMessage`: string

## QueuedPipelineExecution
> Represents a single queued pipeline execution with its global queue position
- `queuePosition`: integer
- `planExecutionId`: string
- `pipelineIdentifier`: string
- `pipelineName`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `status`: string; enum: Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted, Discontinuing, Queued
- `priorityType`: string; enum: HIGH, LOW, NORMAL
- `startTs`: integer
- `createdAt`: integer
- `executionTriggerInfo`: obj
- `runSequence`: integer
- `tags`: array
- `labels`: array

## QueuedPipelineFilter
> Filter criteria for listing queued pipeline executions. Pass inline as the request body, or save via POST /filters with filterType `QueuedPipeline` and reference by filterIdentifier.
- required: filterType
- `tags`: object
- `filterType`: string; enum: Connector, Secret, DelegateProfile, Delegate, PipelineSetup, PipelineExecution, Deployment, Audit, Template, Trigger, EnvironmentGroup, FileStore
- `orgIdentifiers`: array
- `projectIdentifiers`: array
- `pipelineIdentifiers`: array
- `statuses`: array
- `priorityTypes`: array
- `triggerTypes`: array
- `pipelineTags`: array
- `queuedTimeRange`: obj

## QueuedPipelineListResponse
> Paginated list of queued pipeline executions with queue metadata
- `queuedExecutions`: obj
- `totalQueuedInAccount`: integer
- `totalWaitingInAccount`: integer
- `totalRunningInAccount`: integer
- `maxConcurrency`: integer
- `currentRunning`: integer

## RancherConnector
> This contains Rancher connector details

## RancherConnectorBearerTokenAuthentication
> This contains rancher bearer token auth details
- required: passwordRef

## RancherConnectorConfig
> This contains rancher connector config details
- required: type
- `type`: string; enum: ManualConfig
- `spec`: obj

## RancherConnectorConfigAuth
> This contains rancher connector authentication details
- required: auth, rancherUrl
- `rancherUrl`: string
- `auth`: obj

## RancherConnectorConfigAuthentication
> This contains rancher auth credentials

## RecentExecutionInfo
> Recent Execution information of the Pipeline.
- `executor_info`: obj
- `execution_id`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `execution_status`: string; enum: Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted, Discontinuing, Queued
- `started`: integer
- `ended`: integer
- `run_number`: integer
- `parent_stage_info`: obj

## RecommendationECSServiceId
- `clusterName`: string
- `ecsServiceName`: string
- `ignoreUntilEpochMillis`: integer
- `ignoreComments`: string
- `ignoredByUserId`: string
- `ignoredByUserName`: string
- `ignoredAt`: integer

## RegistryEnvironmentType
> Environment Type

## ReleaseApprovalDTO
- required: orgIdentifier, projectIdentifier, pipelineIdentifier, planExecutionId, name, runSequenceId, status, type
- `orgIdentifier`: string
- `projectIdentifier`: string
- `pipelineIdentifier`: string
- `planExecutionId`: string
- `name`: string
- `runSequenceId`: integer
- `status`: obj
- `type`: obj
- `approvalInfo`: obj

## ReleaseApprovalType
> Type of the step (e.g., Approval, JiraUpdate, JiraCreate, JiraApproval).

## ReleaseGithubWebhookSpec

## ReleaseServiceDetails
> Response model of service release details
- `service_id`: string
- `service_name`: string
- `org`: string
- `project`: string

## RemoteExecution
> remote execution details for a specific workspace.
- required: account, org, project, id, workspace, pipeline_execution_id, pipeline_execution_url, created, updated, executed, sha256_checksum
- `account`: string; maxLen 128
- `created`: integer
- `custom_arguments`: object
- `executed`: boolean
- `id`: string
- `org`: string; maxLen 128
- `pipeline_execution_id`: string
- `pipeline_execution_url`: string
- `project`: string; maxLen 128
- `sha256_checksum`: string
- `updated`: integer
- `workspace`: string

## RequestBasedServiceLevelIndicatorSpec
- required: eventType, metric1, metric2

## RerunPipelineRequest
- `inputs_yaml`: string

## ResolvedEnvVariable
- `env_name`: string
- `decrypted_value`: string

## ResolvedEnvVariableResponse
- `resolved_env_variables`: string

## ResponseDTOApprovalInstanceResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOBatchRollbackResponseDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOBulkInputSetsAPIResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOConnectorCatalogueResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOConnectorResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOConnectorStatistics
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOConnectorValidationResult
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOCustomDeploymentVariableResponseDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOCustomPagePipelineExecutionOutline
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTODashboardPipelineExecution
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOEnvironmentBatchResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOEnvironmentGitUpdateResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOEnvironmentGroup
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOEnvironmentGroupDelete
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOEnvironmentImportResponseDetails
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOEnvironmentMoveConfigResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOEnvironmentResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOExecutionDataResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOExecutionGraph
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOExecutionInputDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOExecutionInputStatus
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOExecutionInputVariablesResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOFreezeDetailedResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOFreezeResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOFreezeResponseWrapperDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOFrozenExecutionDetails
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOGcpOidcServiceAccountAccessTokenResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOInfrastructureGitUpdateResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOInfrastructureImportResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOInfrastructureResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOInputSetGitUpdateResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOInputSetResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOInputSetTemplateResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOInputSetTemplateWithReplacedExpressionsResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOListConnectorResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: array
- `metaData`: object
- `correlationId`: string

## ResponseDTOListEnvironmentResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: array
- `metaData`: object
- `correlationId`: string

## ResponseDTOListGenAIServiceDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: array
- `metaData`: object
- `correlationId`: string

## ResponseDTOListMonitoredServiceWithHealthSources
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: array
- `metaData`: object
- `correlationId`: string

## ResponseDTOListRuleExecution
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: array
- `metaData`: object
- `correlationId`: string

## ResponseDTOListServiceAccount
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: array
- `metaData`: object
- `correlationId`: string

## ResponseDTOListServiceNowCatalogItemVariable
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: array
- `metaData`: object
- `correlationId`: string

## ResponseDTOListServiceResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: array
- `metaData`: object
- `correlationId`: string

## ResponseDTOManualExecutionResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOMergeInputSetResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOMonitoredServiceMoveConfigResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOMonitoredServiceResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTONGProcessWebhookResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTONGTriggerDetailsResponseDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTONGTriggerResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTONodeExecutionDetails
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOOverlayInputSetResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPMSPipelineResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPMSPipelineSummaryResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageActiveMonitoredService
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageNGTriggerEventHistoryBaseDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageNGTriggerEventHistoryDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageNGTriggerEventsApiResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPagePMSPipelineSummaryResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPagePipelineExecutionIdentifierSummary
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPagePipelineExecutionSummary
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseConnectorResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseEnvironmentGroup
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseEnvironmentIdentifierResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseEnvironmentResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseFreezeSummaryResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseInfrastructureResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseInputSetListResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseInputSetSummaryResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseMonitoredServiceListItemDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseMonitoredServicePlatformResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseMonitoredServiceResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseNGTriggerDetailsResponseDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseSecretResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseServiceAccount
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseServiceAccountAggregate
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseServiceLevelObjectiveV2Response
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseServiceOverrideResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseServiceResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageResponseVariableResponseDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPageTemplateMetadataSummaryResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPipelineAnnotationsResponseDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPipelineExecutionCountInfo
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPipelineExecutionDetail
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPipelineExecutionNotes
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPipelineSaveResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPlanExecutionResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPollingInfoForTriggers
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPostProdRollbackCheckDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOPostProdRollbackResponseDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOQueuedPipelineBulkAbortResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOQueuedPipelineListResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTORollbackResponseDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTORuleExecution
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTORuleExecutionInternalList
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTORuleExecutionList
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOSecretManagerMetadataDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOSecretResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOSecretValidationResult
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOServiceAccount
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOServiceAccountAggregate
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOServiceBatchResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOServiceGitUpdateResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOServiceImportResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOServiceInstanceUsageDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOServiceMoveConfigResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOServiceOverrideGitUpdateResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOServiceOverrideMoveConfigResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOServiceOverrideResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOServiceOverrideResponseV2
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOServiceResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOServiceUsageDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOSetServiceHookAction
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: array
- `metaData`: object
- `correlationId`: string

## ResponseDTOTemplateLabelMapResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOTemplateLabelsReplaceResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOTemplateMergeResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOTemplateMoveConfigResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOTemplateResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOTemplateUpdateGitDetailsResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOTemplateWrapperResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOTriggerCatalogResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOTriggerExecutorList
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOTriggerGitFullSyncResponse
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOValidateTemplateInputsResponseDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOVariableResponseDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOWebhookEventProcessingDetails
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## ResponseDTOWebhookExecutionDetails
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## RestResponseDelegateDeleteResponse
- `metaData`: object
- `resource`: obj
- `responseMessages`: array

## RestResponseDelegateGroupDTO
- `metaData`: object
- `resource`: obj
- `responseMessages`: array

## RestResponseDelegateGroupListing
- `metaData`: object
- `resource`: obj
- `responseMessages`: array

## RestResponseDelegateTokenDetails
- `metaData`: object
- `resource`: obj
- `responseMessages`: array

## RestResponseListDelegateGroupDTO
- `metaData`: object
- `resource`: array
- `responseMessages`: array

## RestResponseListDelegateListResponse
- `metaData`: object
- `resource`: array
- `responseMessages`: array

## RestResponseListDelegateTokenDetails
- `metaData`: object
- `resource`: array
- `responseMessages`: array

## RestResponseListMonitoredServiceChangeDetailSLO
- `metaData`: object
- `resource`: array
- `responseMessages`: array

## RestResponseListMonitoredServiceDetail
- `metaData`: object
- `resource`: array
- `responseMessages`: array

## RestResponseMonitoredServiceResponse
- `metaData`: object
- `resource`: obj
- `responseMessages`: array

## RestResponsePageResponseMonitoredServiceReference
- `metaData`: object
- `resource`: obj
- `responseMessages`: array

## RestResponseServiceLevelObjectiveV2Response
- `metaData`: object
- `resource`: obj
- `responseMessages`: array

## RestResponseSupportedDelegateVersion
- `metaData`: object
- `resource`: obj
- `responseMessages`: array

## RetryExecutionInfo
- `unknownFields`: obj
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `rootExecutionId`: string
- `isRetry`: boolean
- `parentRetryId`: string
- `rootExecutionIdBytes`: obj
- `parentRetryIdBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## RetryExecutionInfoOrBuilder
- `rootExecutionId`: string
- `isRetry`: boolean
- `parentRetryId`: string
- `rootExecutionIdBytes`: obj
- `parentRetryIdBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## RetryExecutionMetadata
> This gives the Parent and Root execution id of the Execution part of Retried Execution
- `startTs`: integer
- `endTs`: integer
- `runSequence`: integer
- `executedBy`: obj
- `parentExecutionId`: string
- `rootExecutionId`: string

## RetryPipelineRequest
> Request Parameters for retrying a Pipeline execution
- `runtimeInputYaml`: string
- `expressionValues`: object

## RmServiceMetadata
- required: deploymentType
- `deploymentType`: obj

## RollbackRequestDTO
- required: envIdentifier, serviceIdentifier
- `serviceIdentifier`: string
- `envIdentifier`: string
- `environmentType`: string; enum: PreProduction, Production
- `infraIdentifier`: string
- `artifact`: string
- `chartVersion`: string

## RollbackResponseDTO
- `isRollbackTriggered`: boolean
- `instanceKey`: string
- `infraMappingId`: string
- `planExecutionId`: string
- `message`: string
- `serviceIdentifier`: string
- `envIdentifier`: string
- `environmentType`: string
- `infraIdentifier`: string
- `rollbackTriggered`: boolean

## RollbackStateRequest
- `rollback_reason`: string

## RollbackStateResponse
- required: new_data_id, new_file_version, activity_id
- `activity_id`: string
- `new_data_id`: string
- `new_file_version`: integer

## RuleExecution
> This object will contain the complete definition of a Cloud Cost Policy Execution
- `uuid`: string
- `accountId`: string
- `jobId`: string
- `ruleEnforcementRecommendationIdentifier`: string
- `ruleEnforcementRecommendationName`: string
- `ruleEnforcementIdentifier`: string
- `ruleEnforcementName`: string
- `ruleIdentifier`: string
- `ruleName`: string
- `OOTB`: boolean
- `rulePackIdentifier`: string
- `cloudProvider`: string; enum: AWS, AZURE, GCP
- `isDryRun`: boolean
- `targetAccount`: string
- `targetAccountName`: string
- `targetRegions`: array
- `executionLogPath`: string
- `resourceCount`: integer
- `actionedResourceCount`: integer
- `actionFilePresent`: boolean
- `actionedResourceFileName`: string
- `executionLogBucketType`: string
- `executionType`: string; enum: INTERNAL, EXTERNAL, INVENTORY_INTERNAL
- `executionStatus`: string; enum: FAILED, ENQUEUED, PARTIAL_SUCCESS, SUCCESS
- `executionCompletedAt`: integer
- `orgIdentifier`: string
- `projectIdentifier`: string
- `createdAt`: integer
- `lastUpdatedAt`: integer
- `errorMessage`: string
- `resourceType`: string
- `actionType`: string
- `costComputed`: boolean
- `costComputationMessage`: string
- `cost`: number
- `savings`: number
- `costType`: string; enum: POTENTIAL, REALIZED
- `pricingCostType`: string
- `bqDataIngestionStatus`: string; enum: NOT_STARTED, FAILED, IN_PROGRESS, SUCCESSFUL
- `ttl`: string
- `isMultiPolicyRule`: boolean
- `subRuleExecutionDetails`: array
- `isCostBreakdownGenerated`: boolean
- `resourceBreakdownList`: array
- `tagBqIngestionStatus`: string; enum: NOT_STARTED, FAILED, IN_PROGRESS, SUCCESSFUL
- `ootb`: boolean

## RuleExecutionFilter
> This has the query to list the RuleExecution
- `accountId`: string
- `targetAccount`: array
- `executionStatus`: string; enum: FAILED, ENQUEUED, PARTIAL_SUCCESS, SUCCESS
- `region`: array
- `cloudProvider`: string; enum: AWS, AZURE, GCP
- `cloudProviders`: array
- `ruleIds`: array
- `ruleSetIds`: array
- `executionIds`: array
- `ruleEnforcementId`: array
- `ruleEnforcementRecommendationId`: array
- `time`: array
- `limit`: integer
- `offset`: integer
- `savings`: number
- `ruleExecutionSortType`: string; enum: COST, LAST_UPDATED_AT, RESOURCE_COUNT
- `sortOrder`: string; enum: ASCENDING, DESCENDING
- `resourceCountGreaterThanZero`: boolean
- `costType`: string; enum: POTENTIAL, REALIZED
- `isDryRun`: boolean
- `ccmTagDTOS`: array
- `ccmCostCategoryCostBucketsDTOS`: array

## RuleExecutionInternal
> This object will contain the complete definition of a Cloud Cost Policy Internal Execution
- `uuid`: string
- `accountId`: string
- `jobId`: string
- `ruleIdentifier`: string
- `ruleName`: string
- `OOTB`: boolean
- `cloudProvider`: string; enum: AWS, AZURE, GCP
- `isDryRun`: boolean
- `targetAccount`: string
- `targetAccountName`: string
- `targetRegions`: array
- `executionLogPath`: string
- `resourceCount`: integer
- `executionLogBucketType`: string
- `executionStatus`: string; enum: FAILED, ENQUEUED, PARTIAL_SUCCESS, SUCCESS
- `executionCompletedAt`: integer
- `orgIdentifier`: string
- `projectIdentifier`: string
- `createdAt`: integer
- `lastUpdatedAt`: integer
- `errorMessage`: string
- `resourceType`: string
- `actionType`: string
- `costComputed`: boolean
- `costComputationMessage`: string
- `cost`: number
- `bqDataIngestionStatus`: string; enum: NOT_STARTED, FAILED, IN_PROGRESS, SUCCESSFUL
- `ttl`: string
- `isCostBreakdownGenerated`: boolean
- `resourceBreakdownList`: array
- `pricingCostType`: string
- `ootb`: boolean

## RuleExecutionInternalList
> This object will contain the complete definition of a Cloud Cost Governance Internal Evaluation List
- `totalItems`: integer
- `ruleExecutionInternals`: array

## RuleExecutionList
> This object will contain the complete definition of a Cloud Cost Governance Evaluation List
- `totalItems`: integer
- `ruleExecution`: array

## RuleExecutionTagsFilter
> This has the query to list the tags for RuleExecution
- `tagKey`: string
- `search`: string
- `limit`: integer
- `offset`: integer
- `time`: array

## RuleRecommendationExecution
- `connectorId`: string
- `targetId`: string
- `targetName`: string
- `targetRegion`: string
- `executionId`: string
- `statusMessage`: string
- `status`: string; enum: FAILED, IN_PROGRESS, PARTIAL_SUCCESS, SUCCESS, IGNORED
- `potentialSavings`: number
- `isHarnessError`: boolean

## SPApprovalInfo
- `approved_by`: string
- `approved_at`: string
- `status`: string

## SalesforceConnector
> This contains details of the Salesforce connector
- required: credential

## SaveServiceRequest
- `deps`: array
- `service`: obj
- `apply_now`: boolean

## SaveServiceRequestV2
- `deps`: array
- `service`: obj
- `apply_now`: boolean

## SaveServiceRequestV2WithoutDisabled
- `deps`: array
- `service`: obj
- `apply_now`: boolean

## SaveServiceRequestWithoutDisabled
- `deps`: array
- `service`: obj
- `apply_now`: boolean

## ScanIssueCountsWithExecutionInfo
> The count of Security Issues, by severity code, for a given Harness Pipeline Execution along with this execution info
- required: scanners, targetId, targetVariantId, type, targetName, targetVariantName, executionId, pipelineId, lastScanned
- `artifactFingerprint`: string; maxLen 64
- `executionId`: string; pattern `^[a-zA-Z0-9_-]{22}$`
- `lastScanned`: integer
- `pipelineId`: string; pattern `^[A-Za-z_][A-Za-z0-9_]*$`; maxLen 128
- `scanners`: array
- `targetId`: string; pattern `^[a-zA-Z0-9_-]{22}$`
- `targetName`: string
- `targetVariantId`: string; pattern `^[a-zA-Z0-9_-]{22}$`
- `targetVariantName`: string
- `type`: string; enum: container, repository, instance, configuration

## Scheduled Approval
> This contains details of the Scheduled Approval
- required: time, timeZone
- `timeZone`: string
- `time`: string

## ScheduledTriggerSource

## ScheduledTriggerSpec
> Spec for Scheduled Triggers
- `type`: string; enum: Cron
- `spec`: obj

## ScopedExecutionID
- required: account, org, project, pipeline_execution_id, pipeline_stage_id
- `account`: string; maxLen 128
- `org`: string; maxLen 128
- `pipeline_execution_id`: string; maxLen 128
- `pipeline_stage_id`: string; maxLen 128
- `project`: string; maxLen 128

## ScopedPipelineID
- required: account, org, project, pipeline_execution_id
- `account`: string; maxLen 128
- `org`: string; maxLen 128
- `pipeline_execution_id`: string; maxLen 128
- `project`: string; maxLen 128

## ScopedPipelines
- required: account, org, project, totalItems, totalPages, pageSize
- `account`: string; maxLen 128
- `org`: string; maxLen 128
- `pageSize`: integer
- `pipelines`: array
- `project`: string; maxLen 128
- `totalItems`: integer
- `totalPages`: integer

## ScopedRemoteExecutionIdentifier
- required: account, org, project, workspace, id
- `account`: string; maxLen 128
- `id`: string
- `org`: string; maxLen 128
- `project`: string; maxLen 128
- `workspace`: string

## Secret
- required: name, identifier, spec
- `name`: string; pattern `^[0-9a-zA-Z-_ ]{0,127}$`
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$-]{0,127}$`; maxLen 128
- `org`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`
- `project`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`
- `tags`: object
- `description`: string
- `spec`: obj

## Secret1
> This is details of the secret entity defined in Harness.
- required: identifier, name, spec, type
- `type`: string; enum: SecretFile, SecretText, SSHKey, WinRmCredentials
- `name`: string
- `identifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `tags`: object
- `description`: string
- `spec`: obj

## SecretFileSpec
> This is the SSH key authentication details defined in Harness.

## SecretFileSpec1
> This has details of Secret File defined in harness
- required: secretManagerIdentifier

## SecretFilterProperties
> Properties of the Secret Filter defined in Harness
- `secretName`: string
- `secretIdentifier`: string
- `secretTypes`: array
- `secretManagerIdentifiers`: array
- `description`: string
- `searchTerm`: string
- `tags`: object
- `filterType`: string; enum: Secret

## SecretManagerMetadataDTO
- `encryptionType`: string; enum: LOCAL, KMS, GCP_KMS, AWS_SECRETS_MANAGER, AZURE_VAULT, VAULT, GCP_SECRETS_MANAGER, CUSTOM, VAULT_SSH, CUSTOM_NG
- `spec`: obj

## SecretManagerMetadataRequest
> This is the view of the SecretManagerMetadataRequest entity defined in Harness
- required: encryptionType, identifier, spec
- `encryptionType`: string; enum: LOCAL, KMS, GCP_KMS, AWS_SECRETS_MANAGER, AZURE_VAULT, VAULT, GCP_SECRETS_MANAGER, CUSTOM, VAULT_SSH, CUSTOM_NG
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string
- `spec`: obj

## SecretManagerMetadataRequestSpecDTO
> Spec of the Secret Manager.
- required: encryptionType
- `encryptionType`: string

## SecretManagerMetadataSpecDTO
- required: encryptionType
- `encryptionType`: string

## SecretNGVariable
- required: value

## SecretReferredByConnectorSetupUsageDetail

## SecretRequest
- required: secret
- `secret`: obj

## SecretRequestWrapper
- required: secret
- `secret`: obj

## SecretResourceFilter
> This has the filter information for the Secret in Harness.
- `identifiers`: array
- `searchTerm`: string
- `secretTypes`: array
- `sourceCategory`: string; enum: CLOUD_PROVIDER, SECRET_MANAGER, CLOUD_COST, ARTIFACTORY, CODE_REPO, MONITORING, TICKETING, DATABASE, COMMUNICATION, DOCUMENTATION, ML_OPS, MCP
- `includeSecretsFromEverySubScope`: boolean
- `includeAllSecretsAccessibleAtScope`: boolean

## SecretResponse
> Secret response model
- `secret`: obj
- `created`: integer
- `updated`: integer
- `draft`: boolean
- `governance_metadata`: object

## SecretResponse1
> This has details of the Secret along with its metadata.
- required: secret
- `secret`: obj
- `createdAt`: integer
- `updatedAt`: integer
- `draft`: boolean
- `governanceMetadata`: obj

## SecretSpec
> Details of the secret defined in Harness
- required: type
- `type`: string; enum: SSHKeyPath, SSHKeyReference, SSHPassword, SSHKerberosTGTKeyTabFile, SSHKerberosTGTPassword, SecretFile, SecretText, WinRmTGTKeyTabFile, WinRmTGTPassword, WinRmNTLM

## SecretSpec1
> This has details of the Secret defined in Harness.
- required: type
- `errorMessageForInvalidYaml`: string
- `type`: string

## SecretTextSpec
> This is the SSH key authentication details defined in Harness.

## SecretTextSpec1
> This has details of encrypted text secret.
- required: secretManagerIdentifier, valueType

## SecretUniqueIdentifier
- `kmsId`: string

## SecretValidationMetaData
- required: type
- `type`: string; enum: SecretFile, SecretText, SSHKey, WinRmCredentials

## SecretValidationMetadata
> Details of the secret reference
- required: secretManagerIdentifer, secretRefPath
- `secret_manager_identifier`: string
- `secret_ref_path`: string

## SecretValidationResponse
> Response of the secret reference validation
- `success`: boolean
- `message`: string

## SecretValidationResult
> This has validation details for the Secret defined in Harness.
- `success`: boolean
- `message`: string

## SelfServiceCard

## Service
> This is the Service entity defined in Harness
- required: identifier, name
- `account`: string; maxLen 128
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `org`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `project`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `yaml`: string
- `harness_version`: string

## ServiceAccount
> This has the details of Service Account in Harness.
- required: accountIdentifier, email, identifier, name
- `identifier`: string
- `name`: string
- `email`: string
- `description`: string; maxLen 1024
- `tags`: object
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `governanceMetadata`: obj

## ServiceAccountAggregate
> This contains the Service Account details and its metadata.
- required: createdAt, lastModifiedAt, serviceAccount
- `serviceAccount`: obj
- `createdAt`: integer
- `lastModifiedAt`: integer
- `tokensCount`: integer
- `roleAssignmentsMetadataDTO`: array

## ServiceAccountConfig
> Service Account configuration associated with this Account.
- `apiKeyLimit`: integer
- `tokenLimit`: integer

## ServiceBatchResponse
> Batch service creation response with partial success support
- `successfulServices`: array
- `failedServices`: array
- `totalRequested`: integer
- `totalSuccess`: integer
- `totalFailed`: integer

## ServiceCreateRequest
> Service Request Body 
- required: identifier, name
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `yaml`: string
- `harness_version`: string

## ServiceDep

## ServiceDepTree
- `service`: obj
- `children`: array

## ServiceDependencyDTO
- `monitoredServiceIdentifier`: string
- `type`: string; enum: KUBERNETES
- `dependencyMetadata`: obj

## ServiceDependencyMetadata
- `type`: string; enum: KUBERNETES
- `supportedChangeSourceTypes`: array

## ServiceDescriptor
- `index`: integer
- `proto`: obj
- `options`: obj
- `fullName`: string
- `file`: obj
- `methods`: array
- `name`: string

## ServiceDescriptorProto
- `unknownFields`: obj
- `name`: string
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `nameBytes`: obj
- `optionsOrBuilder`: obj
- `methodCount`: integer
- `methodList`: array
- `methodOrBuilderList`: array
- `initialized`: boolean
- `options`: obj
- `descriptorForType`: obj
- `initializationErrorString`: string
- `allFields`: object
- `memoizedSerializedSize`: integer

## ServiceDescriptorProtoOrBuilder
- `name`: string
- `nameBytes`: obj
- `optionsOrBuilder`: obj
- `methodCount`: integer
- `methodList`: array
- `methodOrBuilderList`: array
- `options`: obj
- `descriptorForType`: obj
- `initializationErrorString`: string
- `unknownFields`: obj
- `allFields`: object
- `defaultInstanceForType`: obj
- `initialized`: boolean

## ServiceDiagnostics
- `message`: string
- `name`: string
- `success`: boolean
- `type`: string

## ServiceDiagnosticsResponse
- `response`: array

## ServiceDiscoveryAuditEventData
- required: type

## ServiceError
- `error`: string
- `action`: string

## ServiceExpressionProperties
- `serviceName`: string
- `expression`: string

## ServiceFailureResponse
> Failed service creation/update details with complete scope information
- required: accountId, errorMessage, identifier, status
- `accountId`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `errorCode`: string; enum: DEFAULT_ERROR_CODE, INVALID_ARGUMENT, INVALID_EMAIL, DOMAIN_NOT_ALLOWED_TO_REGISTER, COMMNITY_EDITION_NOT_FOUND, DEPLOY_MODE_IS_NOT_ON_PREM, USER_ALREADY_REGISTERED, USER_INVITATION_DOES_NOT_EXIST, USER_DOES_NOT_EXIST, USER_INVITE_OPERATION_FAILED, USER_DISABLED, ACCOUNT_DOES_NOT_EXIST
- `errorMessage`: string
- `correlationId`: string
- `gitOpsEnabled`: boolean

## ServiceGitUpdateResponse
> Contains info about service that is updated.
- `identifier`: string

## ServiceHealthResponse
- `response`: object

## ServiceImportResponse
> Contains the details of the Saved Service
- `identifier`: string
- `governanceMetadata`: obj

## ServiceInfoDTO
> Holds the information of a given service along with its artifact version
- required: name, identifier, scope
- `name`: string
- `identifier`: string
- `artifactVersion`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `scope`: string; enum: account, project, org, unknown

## ServiceInputVariable
> Input variable for service type
- required: type
- `type`: string; enum: service
- `description`: string
- `default`: object
- `metadata`: obj

## ServiceInstanceUsageDTO
- `accountIdentifier`: string
- `module`: string
- `timestamp`: integer
- `activeServices`: obj
- `activeServiceInstances`: obj
- `cdLicenseType`: string; enum: SERVICES, SERVICE_INSTANCES, LEGACY_USER, DEVELOPER_360, CUSTOM, NAMED_USER

## ServiceLevelIndicatorDTO
- required: spec
- `name`: string
- `identifier`: string
- `type`: string; enum: Window, Request, MetricLess
- `spec`: obj
- `healthSourceRef`: string

## ServiceLevelIndicatorSpec
- required: type
- `type`: string

## ServiceLevelObjectiveDetailsDTO
- required: accountId, orgIdentifier, projectIdentifier, serviceLevelObjectiveRef, weightagePercentage
- `accountId`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `serviceLevelObjectiveRef`: string
- `weightagePercentage`: number

## ServiceLevelObjectiveSpec
- required: type
- `type`: string

## ServiceLevelObjectiveType
> Types of Service Level Objectives.
- `type`: string

## ServiceLevelObjectiveV2Response
- required: serviceLevelObjectiveV2
- `serviceLevelObjectiveV2`: obj
- `createdAt`: integer
- `lastModifiedAt`: integer

## ServiceMetadata
- `cloud_provider_details`: object
- `target_group_details`: object
- `service_errors`: array
- `kubernetes_connector_id`: string
- `autostopping_proxy_config`: object

## ServiceMoveConfigResponse
> Tells us if the service move config operation was successful or not

## ServiceNowADFS
> This entity contains the details of the Service Now ADFS
- required: adfsUrl, certificateRef, clientIdRef, privateKeyRef, resourceIdRef

## ServiceNowApprovalInstanceDetails
> This contains details of ServiceNow Approval Instance
- required: approvalCriteria, connectorRef, ticket

## ServiceNowAuthCredentials
> This contains details of credentials for Service Now Authentication

## ServiceNowAuthentication
> This entity contains the details for Service Now Authentication
- required: spec, type
- `type`: string; enum: UsernamePassword, AdfsClientCredentialsWithCertificate, RefreshTokenGrantType
- `spec`: obj

## ServiceNowCatalogItemVariable
- `key`: string
- `name`: string
- `required`: boolean

## ServiceNowChangeWindowSpec
> This contains details of the ServiceNow ChangeWindow
- required: endField, startField
- `startField`: string
- `endField`: string

## ServiceNowConnector
> ServiceNow Connector details.
- required: auth, serviceNowUrl

## ServiceNowFieldValueNG
- `value`: string
- `displayValue`: string

## ServiceNowRefreshToken
> This entity contains the details of the Service Now Refresh Token
- required: clientIdRef, refreshTokenRef, tokenUrl

## ServiceNowTicketKeyNG
- required: key, ticketType, url
- `url`: string
- `key`: string
- `ticketType`: string
- `ticketFields`: object

## ServiceNowTicketNG
- required: fields, number, url
- `url`: string
- `number`: string
- `fields`: object

## ServiceNowUserNamePassword
> This entity contains the details of the Service Now Username and Password
- required: passwordRef

## ServiceOptions
- `unknownFields`: obj
- `features`: obj
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `deprecated`: boolean
- `featuresOrBuilder`: obj
- `uninterpretedOptionList`: array
- `uninterpretedOptionCount`: integer
- `uninterpretedOptionOrBuilderList`: array
- `initialized`: boolean
- `allFields`: object
- `allFieldsRaw`: object
- `descriptorForType`: obj
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## ServiceOptionsOrBuilder
- `features`: obj
- `deprecated`: boolean
- `featuresOrBuilder`: obj
- `uninterpretedOptionList`: array
- `uninterpretedOptionCount`: integer
- `uninterpretedOptionOrBuilderList`: array
- `defaultInstanceForType`: obj
- `descriptorForType`: obj
- `initializationErrorString`: string
- `unknownFields`: obj
- `allFields`: object
- `initialized`: boolean

## ServiceOverrideGitUpdateResponse
> Contains info about ServiceOverride that is updated.
- required: environmentRef, type
- `identifier`: string
- `environmentRef`: string
- `serviceRef`: string
- `infraIdentifier`: string
- `type`: string; enum: ENV_GLOBAL_OVERRIDE, ENV_SERVICE_OVERRIDE, INFRA_GLOBAL_OVERRIDE, INFRA_SERVICE_OVERRIDE, CLUSTER_GLOBAL_OVERRIDE, CLUSTER_SERVICE_OVERRIDE

## ServiceOverrideMoveConfigResponse
> Tells us if the move config was successful or not
- required: environmentRef, type
- `identifier`: string
- `environmentRef`: string
- `serviceRef`: string
- `infraIdentifier`: string
- `type`: string; enum: ENV_GLOBAL_OVERRIDE, ENV_SERVICE_OVERRIDE, INFRA_GLOBAL_OVERRIDE, INFRA_SERVICE_OVERRIDE, CLUSTER_GLOBAL_OVERRIDE, CLUSTER_SERVICE_OVERRIDE

## ServiceOverrideRequest
> This is the Service Override Request entity defined in Harness
- `orgIdentifier`: string
- `projectIdentifier`: string
- `environmentIdentifier`: string
- `serviceIdentifier`: string
- `yaml`: string

## ServiceOverrideRequestV2
> This is the Service Override Request entity defined in Harness
- required: environmentRef, type
- `orgIdentifier`: string
- `projectIdentifier`: string
- `environmentRef`: string
- `serviceRef`: string
- `infraIdentifier`: string
- `clusterIdentifier`: string
- `type`: string; enum: ENV_GLOBAL_OVERRIDE, ENV_SERVICE_OVERRIDE, INFRA_GLOBAL_OVERRIDE, INFRA_SERVICE_OVERRIDE, CLUSTER_GLOBAL_OVERRIDE, CLUSTER_SERVICE_OVERRIDE
- `spec`: obj
- `yaml`: string
- `identifier`: string

## ServiceOverrideResponse
> This is the Service Override Response entity defined in Harness
- `accountId`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `environmentRef`: string
- `serviceRef`: string
- `yaml`: string
- `governanceMetadata`: obj

## ServiceOverrideResponseV2
> This is the Service Override Response entity defined in Harness
- `identifier`: string
- `accountId`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `environmentRef`: string
- `serviceRef`: string
- `infraIdentifier`: string
- `clusterIdentifier`: string
- `type`: string; enum: ENV_GLOBAL_OVERRIDE, ENV_SERVICE_OVERRIDE, INFRA_GLOBAL_OVERRIDE, INFRA_SERVICE_OVERRIDE, CLUSTER_GLOBAL_OVERRIDE, CLUSTER_SERVICE_OVERRIDE
- `spec`: obj
- `isNewlyCreated`: boolean
- `yaml`: string
- `governanceMetadata`: obj
- `newlyCreated`: boolean

## ServiceOverrideSpec
> This is the Service Override Spec entity defined in Harness
- `variables`: array
- `manifests`: array
- `configFiles`: array
- `applicationSettings`: obj
- `connectionStrings`: obj
- `cliEnvironmentVariables`: array
- `metadata`: string

## ServiceRequest
> Service Request details defined in Harness.
- `identifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `name`: string
- `description`: string
- `tags`: object
- `yaml`: string

## ServiceResponse
> Default response when a service is returned
- `service`: obj
- `created`: integer
- `updated`: integer

## ServiceResponse1
- `service`: obj
- `createdAt`: integer
- `lastModifiedAt`: integer
- `entityValidityDetails`: obj
- `governanceMetadata`: obj

## ServiceResponseDetails
> This is the Service entity defined in Harness
- `accountId`: string
- `identifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `name`: string
- `description`: string
- `deleted`: boolean
- `tags`: object
- `yaml`: string
- `type`: string; enum: Kubernetes, NativeHelm, Ssh, WinRm, ServerlessAwsLambda, AzureWebApp, AzureFunction, CustomDeployment, ECS, Elastigroup, TAS, Asg
- `gitOpsEnabled`: boolean

## ServiceResponseWithoutDisabled
- `response`: obj

## ServiceStatus
- `state`: string
- `target_url`: string
- `error`: string
- `id`: string

## ServiceUpdateRequest
> Service Update Request Body 
- required: identifier, name
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `yaml`: string
- `harness_version`: string

## ServiceUsageDTO
- `accountIdentifier`: string
- `module`: string
- `timestamp`: integer
- `activeServices`: obj
- `activeServiceInstances`: obj
- `cdLicenseType`: string; enum: SERVICES, SERVICE_INSTANCES, LEGACY_USER, DEVELOPER_360, CUSTOM, NAMED_USER
- `serviceLicenses`: obj

## ServiceUsageRecord
- `service_id`: number
- `path`: string
- `session_id`: string
- `idle_time_mins`: number
- `created_at`: string

## ServiceV2
- required: cloud_account_id, kind, name, org_id
- `id`: integer
- `name`: string
- `org_id`: string
- `account_identifier`: string
- `project_id`: string
- `fulfilment`: string
- `kind`: string
- `cloud_account_id`: string
- `idle_time_mins`: integer
- `host_name`: string
- `health_check`: object
- `custom_domains`: array
- `match_all_subdomains`: boolean
- `disabled`: boolean
- `routing`: obj
- `opts`: obj
- `created_at`: string
- `metadata`: obj
- `status`: string

## ServiceV2WithoutDisabled
- required: cloud_account_id, kind, name, org_id
- `id`: integer
- `name`: string
- `org_id`: string
- `account_identifier`: string
- `project_id`: string
- `fulfilment`: string
- `kind`: string
- `cloud_account_id`: string
- `idle_time_mins`: integer
- `host_name`: string
- `health_check`: object
- `custom_domains`: array
- `match_all_subdomains`: boolean
- `routing`: obj
- `opts`: obj
- `created_at`: string
- `access_point_id`: string
- `metadata`: obj
- `status`: string

## ServiceVersion
> Service version
- required: version, commit
- `commit`: string
- `version`: string

## ServiceWithoutDisabled
- required: cloud_account_id, kind, name, org_id
- `id`: integer
- `name`: string
- `org_id`: string
- `account_identifier`: string
- `project_id`: string
- `fulfilment`: string
- `kind`: string
- `cloud_account_id`: string
- `idle_time_mins`: integer
- `host_name`: string
- `health_check`: object
- `custom_domains`: array
- `match_all_subdomains`: boolean
- `routing`: obj
- `opts`: obj
- `created_at`: string
- `access_point_id`: string
- `metadata`: obj
- `status`: string

## ServicesResponse
- `response`: array

## ShowExecutionResponse
- required: status, created, account, org, project, pipeline_execution_id, pipeline_stage_id, workspace, pipeline
- `account`: string; maxLen 128
- `created`: integer
- `org`: string; maxLen 128
- `pipeline`: string
- `pipeline_execution_id`: string
- `pipeline_stage_id`: string
- `project`: string; maxLen 128
- `status`: string; enum: none, success, failure
- `workspace`: string

## ShowRemoteExecutionResponse
- required: account, org, project, id, workspace, pipeline_execution_id, pipeline_execution_url, created, updated, executed, sha256_checksum
- `account`: string; maxLen 128
- `created`: integer
- `custom_arguments`: object
- `executed`: boolean
- `id`: string
- `org`: string; maxLen 128
- `pipeline_execution_id`: string
- `pipeline_execution_url`: string
- `project`: string; maxLen 128
- `sha256_checksum`: string
- `updated`: integer
- `workspace`: string

## ShowWorkspaceVariableResponse
- required: account, org, project, workspace, key, value, value_type, kind, created, updated
- `account`: string; maxLen 128
- `created`: integer
- `key`: string; pattern `^[a-zA-Z0-9_]+$`; maxLen 128
- `kind`: string; enum: env, tf
- `org`: string; maxLen 128
- `project`: string; maxLen 128
- `updated`: integer
- `value`: string
- `value_type`: string; enum: string, secret
- `workspace`: string

## SignalFXConnectorDTO
- required: apiTokenRef, url

## SimpleServiceLevelObjectiveSpec
- required: monitoredServiceRef, serviceLevelIndicators

## SkipTaskExecutableResponse
- `unknownFields`: obj
- `message`: string
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `messageBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## SkipTaskExecutableResponseOrBuilder
- `message`: string
- `messageBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## SlackConnector
> Slack Connector details.
- required: apiAccessType

## SlackWebhookAuthSpec
> Details of Authentication for Slack Webhook defined in Harness
- `auth_type`: string; enum: NoAuth, Hmac

## SlackWebhookResponse
> Details of the Slack Webhook Response defined in Harness

## SlackWebhookSpec
> Details of the Slack Webhook defined in Harness

## SlsaModelPipeline
- `provenance`: object
- `verification`: object

## SplunkConnector
> This contains the Splunk Connector configuration
- required: accountId, splunkUrl

## SpotConnector
> This contains details of the Spot connector
- required: credential

## StageExecutionResponseBody
> This contains info about a Pipeline Stage needed for stage execution.
- `stage_identifier`: string
- `stage_name`: string
- `message`: string
- `is_to_be_blocked`: boolean
- `stages_required`: array

## StageExecutionResponseList

## StagesExecutionMetadata
- `isStagesExecution`: boolean
- `fullPipelineYaml`: string
- `stageIdentifiers`: array
- `expressionValues`: object
- `stageIdentifierToNameMap`: object
- `stagesExecution`: boolean

## StoServiceVersion
- required: version, commit
- `commit`: string
- `version`: string

## StringNGVariable

## StringNGVariable1
- required: value

## StringVariableConfigDTO
- required: fixedValue, valueType

## SubRuleExecutionDetails
> This object stores execution details for a policy execution of a multi policy rule.
- `policyName`: string
- `executionLogPath`: string
- `resourceCount`: integer
- `actionedResourceCount`: integer
- `actionFilePresent`: boolean
- `actionedResourceFileName`: string
- `executionLogBucketType`: string
- `executionType`: string; enum: INTERNAL, EXTERNAL, INVENTORY_INTERNAL
- `executionStatus`: string; enum: FAILED, ENQUEUED, PARTIAL_SUCCESS, SUCCESS
- `bqDataIngestionStatus`: string; enum: NOT_STARTED, FAILED, IN_PROGRESS, SUCCESSFUL
- `errorMessage`: string
- `executionCompletedAt`: integer
- `resourceType`: string
- `actionType`: string
- `costComputed`: boolean
- `costComputationMessage`: string
- `cost`: number
- `savings`: number
- `resourceBreakdownList`: array
- `isCostBreakdownGenerated`: boolean

## SubprocessTriggerRequest
- required: subprocessInfo
- `subprocessInfo`: obj

## SubprocessTriggerResponse
- required: activityExecutionId
- `activityExecutionId`: string

## SumoLogicConnectorDTO
- required: accessIdRef, accessKeyRef, url

## SupportedDelegateVersion
- `latestSupportedVersion`: string
- `latestSupportedMinimalVersion`: string

## SyncExecutableResponse
- `unknownFields`: obj
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `logKeysList`: array
- `logKeysCount`: integer
- `unitsList`: array
- `unitsCount`: integer
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## SyncExecutableResponseOrBuilder
- `logKeysList`: array
- `logKeysCount`: integer
- `unitsList`: array
- `unitsCount`: integer
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## TargetExecutionSummary
- `triggerId`: string
- `targetId`: string
- `runtimeInput`: string
- `planExecutionId`: string
- `runSequence`: integer
- `executionStatus`: string
- `startTs`: integer

## TasConnector
> This contains details of the Tas connector
- required: credential

## TaskChainExecutableResponse
- `unknownFields`: obj
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `taskId`: string
- `taskName`: string
- `chainEnd`: boolean
- `passThroughData`: obj
- `taskCategory`: string; enum: UNKNOWN_CATEGORY, DELEGATE_TASK_V1, DELEGATE_TASK_V2, UNRECOGNIZED
- `taskCategoryValue`: integer
- `taskIdBytes`: obj
- `logKeysList`: array
- `logKeysCount`: integer
- `unitsList`: array
- `unitsCount`: integer
- `taskNameBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## TaskChainExecutableResponseOrBuilder
- `taskId`: string
- `taskName`: string
- `chainEnd`: boolean
- `passThroughData`: obj
- `taskCategory`: string; enum: UNKNOWN_CATEGORY, DELEGATE_TASK_V1, DELEGATE_TASK_V2, UNRECOGNIZED
- `taskCategoryValue`: integer
- `taskIdBytes`: obj
- `logKeysList`: array
- `logKeysCount`: integer
- `unitsList`: array
- `unitsCount`: integer
- `taskNameBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## TaskExecutableResponse
- `unknownFields`: obj
- `initialized`: boolean
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `taskId`: string
- `taskName`: string
- `taskCategory`: string; enum: UNKNOWN_CATEGORY, DELEGATE_TASK_V1, DELEGATE_TASK_V2, UNRECOGNIZED
- `taskCategoryValue`: integer
- `taskIdBytes`: obj
- `logKeysList`: array
- `logKeysCount`: integer
- `unitsList`: array
- `unitsCount`: integer
- `taskNameBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## TaskExecutableResponseOrBuilder
- `taskId`: string
- `taskName`: string
- `taskCategory`: string; enum: UNKNOWN_CATEGORY, DELEGATE_TASK_V1, DELEGATE_TASK_V2, UNRECOGNIZED
- `taskCategoryValue`: integer
- `taskIdBytes`: obj
- `logKeysList`: array
- `logKeysCount`: integer
- `unitsList`: array
- `unitsCount`: integer
- `taskNameBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## TemplateApplyRequestDTO
- required: originalEntityYaml
- `originalEntityYaml`: string
- `checkForAccess`: boolean
- `getMergedYamlWithTemplateField`: boolean
- `getOnlyFileContent`: boolean
- `yamlVersion`: string

## TemplateCreateRequestBody
> Templates Create Request Body
- `template_yaml`: string
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `label`: string; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `git_details`: obj
- `is_stable`: boolean
- `comments`: string

## TemplateDTO
- required: templateRef
- `templateRef`: string
- `versionLabel`: string
- `templateInputs`: string
- `isTemplateByReference`: boolean
- `lastReconciliationTime`: integer

## TemplateEntityDetail
- `type`: string; enum: CreatePR, MergePR, Projects, Pipelines, PipelineSteps, Http, Email, JiraCreate, JiraUpdate, JiraApproval, HarnessApproval, CustomApproval
- `entityRef`: obj
- `name`: string
- `entityGitMetadata`: obj

## TemplateEntityGitDetails
> This contains Validity Details of the Entity
- `valid`: boolean
- `invalidYaml`: string

## TemplateEntityGitMetadata
- `branch`: string
- `repo`: string

## TemplateError
> This is Error entity as defined in Harness
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `code`: string; enum: DEFAULT_ERROR_CODE, INVALID_ARGUMENT, INVALID_EMAIL, DOMAIN_NOT_ALLOWED_TO_REGISTER, COMMNITY_EDITION_NOT_FOUND, DEPLOY_MODE_IS_NOT_ON_PREM, USER_ALREADY_REGISTERED, USER_INVITATION_DOES_NOT_EXIST, USER_DOES_NOT_EXIST, USER_INVITE_OPERATION_FAILED, USER_DISABLED, ACCOUNT_DOES_NOT_EXIST
- `message`: string
- `correlationId`: string
- `detailedMessage`: string
- `responseMessages`: array
- `metadata`: obj

## TemplateErrorMetadata
> This implements different error meta data objects
- `type`: string

## TemplateErrorNodeSummary
- `nodeInfo`: obj
- `templateInfo`: obj
- `templateResponse`: obj
- `childrenErrorNodes`: array

## TemplateEventData
- required: type

## TemplateFilterProperties
> This contains details of the Template Filter
- required: filterType
- `tags`: object
- `filterType`: string; enum: Connector, Secret, DelegateProfile, Delegate, PipelineSetup, PipelineExecution, Deployment, Audit, Template, Trigger, EnvironmentGroup, FileStore
- `templateNames`: array
- `templateIdentifiers`: array
- `description`: string
- `templateEntityTypes`: array
- `childTypes`: array
- `listingScope`: obj
- `repoName`: string
- `metadataFilter`: obj

## TemplateGovernanceMetadata
- `unknownFields`: obj
- `message`: string
- `id`: string
- `type`: string
- `timestamp`: integer
- `initialized`: boolean
- `entity`: string
- `created`: integer
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `typeBytes`: obj
- `messageBytes`: obj
- `status`: string
- `idBytes`: obj
- `detailsOrBuilderList`: array
- `entityBytes`: obj
- `actionBytes`: obj
- `accountId`: string
- `orgId`: string
- `projectId`: string
- `statusBytes`: obj
- `accountIdBytes`: obj
- `orgIdBytes`: obj
- `projectIdBytes`: obj
- `deny`: boolean
- `detailsList`: array
- `action`: string
- `detailsCount`: integer
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## TemplateImportRequestBody
> Template Import Request Body
- `git_import_details`: obj
- `template_import_request`: obj

## TemplateImportRequestDTO
> Information of Tempalte import request DTO
- `template_name`: string
- `template_version`: string
- `template_description`: string

## TemplateImportResponseBody
> Contains the Template details for the given Template ID and version
- `template_identifier`: string
- `template_version`: string

## TemplateInfo
- `templateIdentifier`: string
- `versionLabel`: string
- `templateEntityType`: string; enum: Step, Stage, Pipeline, CustomDeployment, MonitoredService, SecretManager, ArtifactSource, StepGroup, Workspace, Notification, Agent

## TemplateInputSchemaDetailsResponseBody
- `inputs`: array

## TemplateInputsSchemaRequestBody
- `template_yaml`: string

## TemplateLabelFailure
> One label value that failed validation.
- `label`: string
- `reason`: string
- `hint`: string
- `explanation`: string

## TemplateLabelMapResponse
> Per version: custom labels. "stable" is added on the stable version when that version is in the map. stableVersionLabel: stable row in scope, else null.
- required: accountId, identifier
- `accountId`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string
- `versionToLabelsMapping`: object
- `stableVersionLabel`: string

## TemplateLabelsReplaceRequest
> Labels to associate with a specific template version (batch replace for that version).
- required: labels, versionLabel
- `labels`: array
- `versionLabel`: string

## TemplateLabelsReplaceResponse
> Label validation failures, labels successfully stored for the version, and whether the stable pointer was updated.
- `labelFailures`: array
- `labelsApplied`: array
- `stableVersionUpdateApplied`: boolean

## TemplateLinkConfigForCustomSecretManager
- required: templateRef
- `templateRef`: string
- `versionLabel`: string; pattern `^[0-9a-zA-Z][^\s/&]{0,63}$`
- `label`: string
- `templateInputs`: object

## TemplateMergeResponse
> This is the view of the TemplateMergeResponse entity defined in Harness
- `mergedPipelineYaml`: string
- `templateReferenceSummaries`: array
- `mergedPipelineYamlWithTemplateRef`: string
- `cacheResponseMetadata`: obj
- `processedYamlVersion`: string
- `templateMetadata`: obj

## TemplateMetaDataList
> Template Meta Data List Model

## TemplateMetadata
> This is the view of the TemplateMetadata entity defined in Harness
- `hasInsert`: boolean

## TemplateMetadataFilterExpression
> Filter expression for template metadata. Type is inferred from structure.

## TemplateMetadataSummaryResponse
> Single Template Metadata Model
- `account`: string
- `org`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `project`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `version_label`: string
- `entity_type`: string; enum: Step, Stage, Pipeline, CustomDeployment, MonitoredService, SecretManager
- `child_type`: string
- `scope`: string; enum: org, project, account, unknown
- `version`: integer
- `git_details`: obj
- `updated`: integer
- `store_type`: string; enum: INLINE, REMOTE
- `connector_ref`: string
- `yaml_version`: string
- `stable_template`: boolean

## TemplateMoveConfigResponse
> Tells us if the template move config operation was successful or not
- `templateIdentifier`: string
- `versionLabel`: string

## TemplateNodeInfo
- `identifier`: string
- `name`: string
- `localFqn`: string

## TemplatePolicyMetadata
- `unknownFields`: obj
- `severity`: string
- `initialized`: boolean
- `identifier`: string
- `created`: integer
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `identifierBytes`: obj
- `status`: string
- `denyMessagesList`: array
- `policyId`: string
- `policyName`: string
- `accountId`: string
- `orgId`: string
- `projectId`: string
- `updated`: integer
- `error`: string
- `denyMessagesCount`: integer
- `policyIdBytes`: obj
- `policyNameBytes`: obj
- `severityBytes`: obj
- `statusBytes`: obj
- `accountIdBytes`: obj
- `orgIdBytes`: obj
- `projectIdBytes`: obj
- `errorBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## TemplatePolicySetMetadata
- `unknownFields`: obj
- `initialized`: boolean
- `description`: string
- `identifier`: string
- `created`: integer
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `identifierBytes`: obj
- `status`: string
- `accountId`: string
- `orgId`: string
- `projectId`: string
- `statusBytes`: obj
- `accountIdBytes`: obj
- `orgIdBytes`: obj
- `projectIdBytes`: obj
- `policySetId`: string
- `deny`: boolean
- `policyMetadataList`: array
- `policySetName`: string
- `policyMetadataCount`: integer
- `policySetIdBytes`: obj
- `policyMetadataOrBuilderList`: array
- `policySetNameBytes`: obj
- `descriptionBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## TemplatePolicySetMetadataOrBuilder
- `description`: string
- `identifier`: string
- `created`: integer
- `identifierBytes`: obj
- `status`: string
- `accountId`: string
- `orgId`: string
- `projectId`: string
- `statusBytes`: obj
- `accountIdBytes`: obj
- `orgIdBytes`: obj
- `projectIdBytes`: obj
- `policySetId`: string
- `deny`: boolean
- `policyMetadataList`: array
- `policySetName`: string
- `policyMetadataCount`: integer
- `policySetIdBytes`: obj
- `policyMetadataOrBuilderList`: array
- `policySetNameBytes`: obj
- `descriptionBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## TemplateReferenceProtoDTO
- `unknownFields`: obj
- `parentUniqueId`: obj
- `accountIdentifier`: obj
- `orgIdentifier`: obj
- `projectIdentifier`: obj
- `metadataMap`: object
- `metadataCount`: integer
- `orgIdentifierOrBuilder`: obj
- `projectIdentifierOrBuilder`: obj
- `metadata`: object
- `accountIdentifierOrBuilder`: obj
- `identifierOrBuilder`: obj
- `parentUniqueIdOrBuilder`: obj
- `versionLabelOrBuilder`: obj
- `scopeValue`: integer
- `parserForType`: obj
- `serializedSize`: integer
- `defaultInstanceForType`: obj
- `versionLabel`: obj
- `initialized`: boolean
- `identifier`: obj
- `scope`: string; enum: ACCOUNT, ORG, PROJECT, UNKNOWN, UNRECOGNIZED
- `allFields`: object
- `descriptorForType`: obj
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## TemplateReferenceProtoDTOOrBuilder
- `parentUniqueId`: obj
- `accountIdentifier`: obj
- `orgIdentifier`: obj
- `projectIdentifier`: obj
- `metadataMap`: object
- `metadataCount`: integer
- `orgIdentifierOrBuilder`: obj
- `projectIdentifierOrBuilder`: obj
- `metadata`: object
- `accountIdentifierOrBuilder`: obj
- `identifierOrBuilder`: obj
- `parentUniqueIdOrBuilder`: obj
- `versionLabelOrBuilder`: obj
- `scopeValue`: integer
- `versionLabel`: obj
- `identifier`: obj
- `scope`: string; enum: ACCOUNT, ORG, PROJECT, UNKNOWN, UNRECOGNIZED
- `allFields`: object
- `descriptorForType`: obj
- `defaultInstanceForType`: obj
- `initializationErrorString`: string
- `unknownFields`: obj
- `initialized`: boolean

## TemplateReferenceSummary
- `unknownFields`: obj
- `name`: string
- `initialized`: boolean
- `description`: string
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `nameBytes`: obj
- `templateRef`: string
- `versionLabel`: string
- `gitBranch`: string
- `uses`: string
- `iconName`: string
- `templateRefBytes`: obj
- `versionLabelBytes`: obj
- `gitBranchBytes`: obj
- `usesBytes`: obj
- `iconNameBytes`: obj
- `descriptionBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## TemplateResponse
> Default response when a template is returned
- required: account, identifier, name, yaml
- `account`: string
- `org`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `project`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `yaml`: string
- `version_label`: string
- `entity_type`: string; enum: Step, Stage, Pipeline, CustomDeployment, MonitoredService, SecretManager
- `child_type`: string
- `scope`: string; enum: org, project, account, unknown
- `updated`: integer
- `version`: integer
- `git_details`: obj
- `store_type`: string; enum: INLINE, REMOTE
- `connector_ref`: string
- `yaml_version`: string
- `stable_template`: boolean

## TemplateResponseDTOValidateTemplateInputsResponseDTO
- `status`: string; enum: SUCCESS, FAILURE, ERROR
- `data`: obj
- `metaData`: object
- `correlationId`: string

## TemplateSchemaResponse
- `data`: object

## TemplateScope
> This contains scope of template being created
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string

## TemplateTemplateMetadataSummaryResponse
> This contains details of the Template Metadata Summary Response
- `accountId`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string
- `name`: string
- `description`: string; maxLen 1024
- `tags`: object
- `versionLabel`: string
- `labels`: array
- `stableTemplate`: boolean
- `enableDAG`: boolean
- `templateEntityType`: string; enum: Step, Stage, Pipeline, CustomDeployment, MonitoredService, SecretManager, ArtifactSource, StepGroup, Workspace, Notification, Agent
- `childType`: string
- `templateScope`: string; enum: account, org, project, unknown
- `version`: integer
- `gitDetails`: obj
- `lastUpdatedAt`: integer
- `createdAt`: integer
- `storeType`: string; enum: INLINE, REMOTE, INLINE_HC
- `connectorRef`: string
- `icon`: string
- `yamlVersion`: string
- `iconName`: string
- `iconUrl`: string
- `isInlineHCEntity`: boolean
- `isReferenced`: boolean

## TemplateTemplateReferenceSummary
- `fqn`: string
- `templateIdentifier`: string
- `versionLabel`: string
- `scope`: string; enum: account, org, project, unknown
- `stableTemplate`: boolean
- `moduleInfo`: array

## TemplateTemplateResponse
> This contains details of the Template Response
- required: accountId, identifier, name, yaml
- `accountId`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `identifier`: string
- `name`: string
- `description`: string; maxLen 1024
- `tags`: object
- `yaml`: string
- `mergedYaml`: string
- `versionLabel`: string
- `isStableTemplate`: boolean
- `labels`: array
- `enableDAG`: boolean
- `templateEntityType`: string; enum: Step, Stage, Pipeline, CustomDeployment, MonitoredService, SecretManager, ArtifactSource, StepGroup, Workspace, Notification, Agent
- `childType`: string
- `templateScope`: string; enum: account, org, project, unknown
- `version`: integer
- `gitDetails`: obj
- `entityValidityDetails`: obj
- `lastUpdatedAt`: integer
- `storeType`: string; enum: INLINE, REMOTE, INLINE_HC
- `connectorRef`: string
- `icon`: string
- `cacheResponseMetadata`: obj
- `yamlVersion`: string
- `bulkReconcileUUID`: string
- `hasInsert`: boolean
- `isInlineHCEntity`: boolean
- `stableTemplate`: boolean

## TemplateUpdateGitDetailsRequest
> Lists down request params for template update git details request
- `filePath`: string
- `repoName`: string
- `connectorRef`: string

## TemplateUpdateGitDetailsResponse
> Tells status of update git details request for given template
- `status`: boolean

## TemplateUpdateGitMetadataRequest
> Lists down request params for template update git details request
- `version`: string
- `git_details`: obj

## TemplateUpdateRequestBody
> Templates Update Request Body
- `template_yaml`: string
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `label`: string; maxLen 128
- `description`: string; maxLen 1024
- `tags`: object
- `git_details`: obj
- `comments`: string

## TemplateUpdateStableResponse
> Template stable version update Response
- `stable_version`: string

## TemplateValidationResponseBody
> Has Template Resolution Response.
- `valid_yaml`: boolean
- `exception_message`: string

## TemplateWithInputsResponse
> Returns Template input YAML with template response
- `template`: obj
- `inputs`: string

## TemplateWrapperResponse
> This contains details of the Template Wrapper Response
- `isValid`: boolean
- `templateResponseDTO`: obj
- `governanceMetadata`: obj
- `templateLabelsApplyResult`: obj
- `valid`: boolean

## TemplateYamlInputDTO
- `name`: string
- `type`: obj
- `description`: string
- `required`: boolean
- `default`: object
- `allowed_values`: array
- `execution`: boolean
- `regex`: string

## TemplateYamlInputDetailsDTO
- `details`: obj
- `metadata`: obj

## TemplateYamlInputMetadataDTO
- `field_properties`: array
- `dependencies`: obj

## TerraformCloudConnector
> This contains details of the Terraform Cloud connector
- required: credential, terraformCloudUrl

## Trigger
> refers to trigger

## TriggerBody
> Trigger object 
- required: identifier, name, source
- `enabled`: boolean
- `encrypted_webhook_secret_identifier`: string
- `input_set_refs`: array
- `inputs`: string
- `pipeline_branch_name`: string
- `source`: obj
- `stages_to_execute`: array
- `tags`: object

## TriggerCatalogItem
> This has details of the Trigger Catalog.
- required: category, triggerCatalogType
- `category`: string; enum: Webhook, Artifact, Manifest, Scheduled, MultiRegionArtifact, SystemEvent
- `triggerCatalogType`: array

## TriggerCatalogResponse
> This has details of the retrieved Trigger Catalog.
- required: catalog
- `catalog`: array

## TriggerConditions
> Conditions for the Trigger
- `key`: string
- `operator`: string; enum: In, Equals, NotEquals, StartsWith, EndsWith, Contains, DoesNotContain, Regex, NotIn
- `value`: string

## TriggerEventStatus
- `status`: string; enum: SUCCESS, FAILED, SKIPPED
- `message`: string

## TriggerExecutor
> Details of a user or service account eligible to execute a trigger. For create/update requests, only 'uuid' and 'type' are required; name and email are fetched from user/service-account services. For responses, all fields are populated.
- required: type, uuid
- `uuid`: string
- `name`: string
- `email`: string
- `type`: string; enum: USER, SERVICE_ACCOUNT

## TriggerExecutorList
> List of users and service accounts eligible to execute a trigger
- `executors`: array
- `totalCount`: integer
- `isCurrentUserAdmin`: boolean
- `currentUserAdmin`: boolean

## TriggerFilterProperties
> This contains details of the Trigger Filter
- required: filterType
- `triggerNames`: array
- `triggerIdentifiers`: array
- `triggerTypes`: array
- `tags`: object
- `filterType`: string; enum: Connector, Secret, DelegateProfile, Delegate, PipelineSetup, PipelineExecution, Deployment, Audit, Template, Trigger, EnvironmentGroup, FileStore

## TriggerGetResponseBody
> Trigger response body.
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `name`: string; pattern `^[a-zA-Z_][0-9a-zA-Z-_ ]{0,127}$`; maxLen 128
- `org`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `project`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `pipeline`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128
- `description`: string; maxLen 1024
- `trigger`: obj

## TriggerGitFullSyncResponse
> This has details to trigger Git Full Sync.
- `isFullSyncTriggered`: boolean

## TriggerIssuer
- required: abortPrevConcurrentExecution, triggerRef
- `triggerRef`: string
- `abortPrevConcurrentExecution`: boolean

## TriggerPayload
- `unknownFields`: obj
- `type`: string; enum: CUSTOM, GIT, SCHEDULED, WEBHOOK, ARTIFACT, MANIFEST, UNRECOGNIZED
- `version`: integer
- `imagePath`: string
- `initialized`: boolean
- `headers`: object
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `connectorRef`: string
- `parsedPayload`: obj
- `sourceType`: string; enum: CUSTOM_REPO, GITHUB_REPO, GITLAB_REPO, BITBUCKET_REPO, AWS_CODECOMMIT_REPO, AZURE_REPO, HARNESS_REPO, UNRECOGNIZED
- `changedFilesList`: array
- `headersMap`: object
- `artifactData`: obj
- `manifestData`: obj
- `typeValue`: integer
- `headersCount`: integer
- `buildDataCase`: string; enum: ARTIFACTDATA, MANIFESTDATA, BUILDDATA_NOT_SET
- `changedFilesCount`: integer
- `parsedPayloadOrBuilder`: obj
- `sourceTypeValue`: integer
- `artifactDataOrBuilder`: obj
- `manifestDataOrBuilder`: obj
- `connectorRefBytes`: obj
- `imagePathBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## TriggerReferenceProtoDTO
- `unknownFields`: obj
- `pipelineIdentifier`: obj
- `parentUniqueId`: obj
- `accountIdentifier`: obj
- `orgIdentifier`: obj
- `projectIdentifier`: obj
- `metadataMap`: object
- `metadataCount`: integer
- `orgIdentifierOrBuilder`: obj
- `projectIdentifierOrBuilder`: obj
- `metadata`: object
- `accountIdentifierOrBuilder`: obj
- `pipelineIdentifierOrBuilder`: obj
- `identifierOrBuilder`: obj
- `parentUniqueIdOrBuilder`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `defaultInstanceForType`: obj
- `initialized`: boolean
- `identifier`: obj
- `allFields`: object
- `descriptorForType`: obj
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## TriggerReferenceProtoDTOOrBuilder
- `pipelineIdentifier`: obj
- `parentUniqueId`: obj
- `accountIdentifier`: obj
- `orgIdentifier`: obj
- `projectIdentifier`: obj
- `metadataMap`: object
- `metadataCount`: integer
- `orgIdentifierOrBuilder`: obj
- `projectIdentifierOrBuilder`: obj
- `metadata`: object
- `accountIdentifierOrBuilder`: obj
- `pipelineIdentifierOrBuilder`: obj
- `identifierOrBuilder`: obj
- `parentUniqueIdOrBuilder`: obj
- `identifier`: obj
- `allFields`: object
- `descriptorForType`: obj
- `defaultInstanceForType`: obj
- `initializationErrorString`: string
- `unknownFields`: obj
- `initialized`: boolean

## TriggerRequestBody
> Trigger request body object 
- required: type, identifier, name, source
- `description`: string
- `enabled`: boolean
- `encrypted_webhook_secret_identifier`: string
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_]{0,127}$`
- `input_set_refs`: array
- `inputs`: string
- `name`: string; pattern `^[a-zA-Z_0-9-.][-0-9a-zA-Z_\s.]{0,127}$`
- `pipeline_branch_name`: string
- `source`: obj
- `stages_to_execute`: array
- `tags`: object

## TriggerResponseBody
> Pipeline response body
- `identifier`: string; pattern `^[a-zA-Z_][0-9a-zA-Z_$]{0,127}$`; maxLen 128

## TriggerSource
- required: type, spec
- `poll_interval`: string; pattern `(((([1-9])+\d*[mh])+(\s/?\d+[mh])*)|(^$)|(0))$`
- `type`: string; enum: Webhook, Artifact, Manifest, Scheduled, MultiRegionArtifact
- `webhook_id`: string

## TriggerStatus
- `pollingSubscriptionStatus`: obj
- `validationStatus`: obj
- `webhookAutoRegistrationStatus`: obj
- `webhookInfo`: obj
- `status`: string; enum: SUCCESS, FAILED, UNKNOWN, PENDING
- `detailMessages`: array
- `lastPollingUpdate`: integer
- `lastPolled`: array

## TriggerType
> Unit of time used for repeating releases.

## TriggeredBy
- `unknownFields`: obj
- `initialized`: boolean
- `identifier`: string
- `defaultInstanceForType`: obj
- `parserForType`: obj
- `serializedSize`: integer
- `extraInfoMap`: object
- `uuid`: string
- `triggerIdentifier`: string
- `triggerName`: string
- `impersonateUsername`: string
- `impersonateEmail`: string
- `uuidBytes`: obj
- `identifierBytes`: obj
- `extraInfoCount`: integer
- `extraInfo`: object
- `triggerIdentifierBytes`: obj
- `triggerNameBytes`: obj
- `impersonateUsernameBytes`: obj
- `impersonateEmailBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `initializationErrorString`: string
- `memoizedSerializedSize`: integer

## TriggeredByDTO
> Details of the user who triggered the activity.
- `name`: string
- `id`: string
- `avatar`: string
- `triggerType`: obj

## TriggeredByInfoAuditDetails
- `type`: string
- `identifier`: string
- `extraInfo`: object

## TriggeredByOrBuilder
- `identifier`: string
- `extraInfoMap`: object
- `uuid`: string
- `triggerIdentifier`: string
- `triggerName`: string
- `impersonateUsername`: string
- `impersonateEmail`: string
- `uuidBytes`: obj
- `identifierBytes`: obj
- `extraInfoCount`: integer
- `extraInfo`: object
- `triggerIdentifierBytes`: obj
- `triggerNameBytes`: obj
- `impersonateUsernameBytes`: obj
- `impersonateEmailBytes`: obj
- `descriptorForType`: obj
- `allFields`: object
- `unknownFields`: obj
- `initializationErrorString`: string
- `defaultInstanceForType`: obj
- `initialized`: boolean

## TypesDefaultReviewerApprovalsResponse
- `current_count`: integer
- `evaluations`: array
- `minimum_required_count`: integer
- `minimum_required_count_latest`: integer
- `principals`: array
- `user_groups`: array

## TypesWebhookCreateInput
- `description`: string
- `display_name`: string
- `enabled`: boolean
- `extra_headers`: array
- `identifier`: string
- `insecure`: boolean
- `secret`: string
- `triggers`: array
- `uid`: string
- `url`: string

## TypesWebhookExecution
- `created`: integer
- `duration`: integer
- `error`: string
- `id`: integer
- `request`: obj
- `response`: obj
- `result`: obj
- `retrigger_of`: integer
- `retriggerable`: boolean
- `trigger_type`: obj
- `webhook_id`: integer

## TypesWebhookExecutionRequest
- `body`: string
- `headers`: string
- `url`: string

## TypesWebhookExecutionResponse
- `body`: string
- `headers`: string
- `status`: string
- `status_code`: integer

## UnifiedExecutionRequest
> UnifiedExecutionRequest defines an individual execution of unified execution
- required: account, org, project, pipeline_execution_id, pipeline_stage_id, pipeline_id
- `account`: string; maxLen 128
- `module_test`: string
- `org`: string; maxLen 128
- `pipeline_execution_id`: string
- `pipeline_id`: string
- `pipeline_stage_id`: string
- `project`: string; maxLen 128
- `remote_execution_id`: string
- `skip_adding_to_db`: boolean
- `webhook`: obj
- `workspace`: string

## UnifiedExecutionRequest2
- required: pipeline_execution_id, pipeline_stage_id, pipeline_id
- `module_test`: string
- `pipeline_execution_id`: string
- `pipeline_id`: string
- `pipeline_stage_id`: string
- `remote_execution_id`: string
- `skip_adding_to_db`: boolean
- `webhook`: obj
- `workspace`: string

## UnifiedExecutionResponse
> UnifiedExecutionResponse contains all data required for unified execution
- required: outputs, env_variables
- `env_variables`: object
- `outputs`: object
- `steps`: array

## UpdateApprovalRequest
- required: status, pipeline_execution_id, pipeline_stage_id, workspace_id
- `actioned_by`: string
- `actioned_by_email`: string
- `status`: string; enum: approved, rejected, pending

## UpdateExecutionRequest
- `audit`: obj

## UpdateGitXWebhookEventRequest
> Update GitX Webhook Event Request
- `event_status`: string

## UpdateGitXWebhookRequest
> Contains information about the GitX webhook updation 
- `repo_name`: string
- `webhook_name`: string
- `folder_paths`: array
- `is_enabled`: boolean
- `connector_ref`: string

## UpdateGitXWebhookResponse
> Contains information about the GitX webhook updation 
- `webhook_identifier`: string

## UpdateVariableSetRequestAccountScope
- required: name
- `connectors`: array
- `created`: integer
- `description`: string
- `environment_variables`: object
- `id`: integer
- `name`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `updated`: integer

## UpdateVariableSetRequestOrgScope
- required: name
- `connectors`: array
- `created`: integer
- `description`: string
- `environment_variables`: object
- `id`: integer
- `name`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `updated`: integer

## UpdateVariableSetRequestProjScope
- required: name
- `connectors`: array
- `created`: integer
- `description`: string
- `environment_variables`: object
- `id`: integer
- `name`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `updated`: integer

## UpdateWebhookRequest
> Contains information about the webhook updation 
- required: webhook_name, is_enabled, spec
- `webhook_name`: string
- `is_enabled`: boolean
- `spec`: obj

## UpdateWebhookResponse
> Contains information about the webhook updation 
- `webhook_identifier`: string

## UpdateWorkspaceVariableRequest
- required: value, value_type
- `value`: string
- `value_type`: string; enum: string, secret

## UpdateWorkspaceVariableResponse
- `policy_evaluation`: obj

## UploadRemoteExecutionResponse
- required: account, org, project, id, workspace, pipeline_execution_id, pipeline_execution_url, created, updated, executed, sha256_checksum
- `account`: string; maxLen 128
- `created`: integer
- `custom_arguments`: object
- `executed`: boolean
- `id`: string
- `org`: string; maxLen 128
- `pipeline_execution_id`: string
- `pipeline_execution_url`: string
- `project`: string; maxLen 128
- `sha256_checksum`: string
- `updated`: integer
- `workspace`: string

## UpsertDefaultPipelineRequest
- required: provisioner, operation, pipeline, updated
- `operation`: string; enum: plan, apply, destroy, drift, synth, diff, deploy, remediation
- `pipeline`: string
- `provisioner`: string; enum: terraform, opentofu, terragrunt, awscdk
- `updated`: integer
- `workspace`: string

## ValidateTemplateInputsResponseDTO
- `validYaml`: boolean
- `errorNodeSummary`: obj
- `type`: string

## Variable
- `default`: array
- `desc`: string
- `id`: string
- `name`: string
- `type`: string; enum: text, textMultiple, selectOne, selectMultiple
- `values`: array

## VariableConfigDTO
- required: type, valueType
- `valueType`: string; enum: FIXED
- `type`: string

## VariableDTO
- required: identifier, name, spec, type
- `identifier`: string
- `name`: string
- `description`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `type`: string; enum: String
- `governanceMetadata`: obj
- `spec`: obj

## VariableFilePermissions
- required: canDelete, canEdit
- `canDelete`: boolean
- `canEdit`: boolean

## VariableFileWithPermissions
- required: uuid, repository, source, isInWorkspace, permissions, inUse, repository_path, isLocked
- `associatedTemplate`: string
- `associatedVariableSet`: string
- `inUse`: boolean
- `isInWorkspace`: boolean
- `isLocked`: boolean
- `permissions`: obj
- `repository`: string
- `repository_branch`: string
- `repository_commit`: string
- `repository_connector`: string
- `repository_path`: string
- `repository_sha`: string
- `source`: string; enum: workspace, template, variableSet
- `uuid`: string

## VariableListRequestDTO
- `identifiers`: array

## VariableMergeServiceResponse
> This contains Pipeline YAML with the version.
- `yaml`: string
- `metadataMap`: object
- `errorResponses`: array
- `serviceExpressionPropertiesList`: array

## VariableMetadata
- `variable_default`: string
- `variable_description`: string
- `variable_name`: string
- `variable_required`: boolean
- `variable_sensitive`: boolean
- `variable_type`: string

## VariablePermissions
- required: canDelete, canEditKey, canEditValue, canEditValueType
- `canDelete`: boolean
- `canEditKey`: boolean
- `canEditValue`: boolean
- `canEditValueType`: boolean

## VariableRequestDTO
- `variable`: obj

## VariableResource
> Variable is the representation for a single variable associated with a workspace.
- required: key, value, value_type, kind, created, updated
- `created`: integer
- `key`: string; pattern `^[a-zA-Z0-9_]+$`; maxLen 128
- `updated`: integer
- `value`: string
- `value_type`: string; enum: string, secret

## VariableResponseDTO
- required: variable
- `variable`: obj
- `createdAt`: integer
- `lastModifiedAt`: integer

## VariableResponseMapValue
- `yamlProperties`: obj
- `yamlOutputProperties`: obj
- `yamlExtraProperties`: obj

## VariableSetAccScope
> Create VariableSet at account level.
- required: account, identifier, name
- `account`: string; maxLen 128
- `connectors`: array
- `created`: integer
- `description`: string
- `environment_variables`: object
- `id`: integer
- `identifier`: string; pattern `^[^/?#\s]+$`; maxLen 128
- `name`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `updated`: integer

## VariableSetConnector
> Variable Set provider connector
- required: connector_ref, type
- `connector_ref`: string; maxLen 128
- `created`: integer
- `id`: integer
- `type`: string; enum: aws, azure, gcp, vault
- `updated`: integer

## VariableSetOrgScope
> Create VariableSet at org level.
- required: account, org, identifier, name
- `account`: string; maxLen 128
- `connectors`: array
- `created`: integer
- `description`: string
- `environment_variables`: object
- `id`: integer
- `identifier`: string; pattern `^[^/?#\s]+$`; maxLen 128
- `name`: string; maxLen 128
- `org`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `updated`: integer

## VariableSetProjScope
> Create VariableSet at project level.
- required: account, org, project, identifier, name
- `account`: string; maxLen 128
- `connectors`: array
- `created`: integer
- `description`: string
- `environment_variables`: object
- `id`: integer
- `identifier`: string; pattern `^[^/?#\s]+$`; maxLen 128
- `name`: string; maxLen 128
- `org`: string; maxLen 128
- `project`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `updated`: integer

## VariableSetResourceCollection

## VariableSetUpdateAccScope
> Update VariableSet at account level.
- required: account, identifier, name
- `account`: string; maxLen 128
- `connectors`: array
- `created`: integer
- `description`: string
- `environment_variables`: object
- `id`: integer
- `identifier`: string; pattern `^[^/?#\s]+$`; maxLen 128
- `name`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `updated`: integer

## VariableSetUpdateOrgScope
> Update VariableSet at org level.
- required: account, org, identifier, name
- `account`: string; maxLen 128
- `connectors`: array
- `created`: integer
- `description`: string
- `environment_variables`: object
- `id`: integer
- `identifier`: string; pattern `^[^/?#\s]+$`; maxLen 128
- `name`: string; maxLen 128
- `org`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `updated`: integer

## VariableSetUpdateProjScope
> Update VariableSet at project level.
- required: account, org, project, identifier, name
- `account`: string; maxLen 128
- `connectors`: array
- `created`: integer
- `description`: string
- `environment_variables`: object
- `id`: integer
- `identifier`: string; pattern `^[^/?#\s]+$`; maxLen 128
- `name`: string; maxLen 128
- `org`: string; maxLen 128
- `project`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `updated`: integer

## VariableSetVar
> Variable is the representation for a single variable associated with a Variable Set.
- required: key, value, value_type
- `created`: integer
- `id`: integer
- `key`: string; pattern `^[A-Za-z_][A-Za-z0-9_-]*$`; maxLen 128
- `updated`: integer
- `value`: string
- `value_type`: string; enum: string, secret

## VariableSetVarFile
> VariableSetVarFile defines a variable file that lives in another repository than the workspace files.
- required: repository
- `created`: integer
- `id`: integer
- `repository`: string
- `repository_branch`: string
- `repository_commit`: string
- `repository_connector`: string
- `repository_path`: string
- `repository_sha`: string
- `updated`: integer

## VariableSetsCreateVariableSetAccountLevelResponseBody
> Create-Variable-Set-Account-LevelResponseBody result type (default view)
- required: account, org, project, identifier, name
- `account`: string; maxLen 128
- `connectors`: array
- `created`: integer
- `description`: string
- `environment_variables`: object
- `identifier`: string; pattern `^[^/?#\s]+$`; maxLen 128
- `name`: string; maxLen 128
- `org`: string; maxLen 128
- `project`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `updated`: integer

## VariableSetsGetVariableSetAccountLevelResponseBody
> Get-Variable-Set-Account-LevelResponseBody result type (default view)
- required: account, org, project, identifier, name
- `account`: string; maxLen 128
- `connectors`: array
- `created`: integer
- `description`: string
- `environment_variables`: object
- `identifier`: string; pattern `^[^/?#\s]+$`; maxLen 128
- `name`: string; maxLen 128
- `org`: string; maxLen 128
- `project`: string; maxLen 128
- `terraform_variable_files`: array
- `terraform_variables`: object
- `updated`: integer

## VariableWithPermissions
- required: uuid, key, value, value_type, source, kind, includeInWorkspace, isLocked, created, updated, permissions, inUse
- `associatedTemplate`: string
- `associatedVariableSet`: string
- `created`: integer
- `inUse`: boolean
- `includeInWorkspace`: boolean
- `isLocked`: boolean
- `key`: string
- `kind`: string
- `permissions`: obj
- `source`: string; enum: workspace, template, variableSet
- `updated`: integer
- `uuid`: string
- `value`: string
- `value_type`: string

## VariablesAndProvidersResult
- required: terraform_variables, environment_variables, provider_connectors, variable_files
- `environment_variables`: array
- `provider_connectors`: array
- `terraform_variables`: array
- `variable_files`: array

## VaultConnector
> This contains the Vault Connector configuration.
- required: renewalIntervalMinutes, vaultUrl

## WebHookHeaders
- `key`: string
- `value`: string

## Webhook
> Harness Regstries Webhook
- required: identifier, url, name, enabled, insecure
- `createdAt`: string
- `createdBy`: integer
- `description`: string
- `enabled`: boolean
- `extraHeaders`: array
- `identifier`: string
- `insecure`: boolean
- `internal`: boolean
- `latestExecutionResult`: obj
- `modifiedAt`: string
- `name`: string
- `secretIdentifier`: string
- `secretSpaceId`: integer
- `secretSpacePath`: string
- `triggers`: array
- `url`: string
- `version`: integer

## WebhookAutoRegistrationStatus
- `registrationResult`: string; enum: SUCCESS, FAILED, ERROR, TIMEOUT, UNAVAILABLE
- `detailedMessage`: string

## WebhookConfigDTO
- required: webhookUrl

## WebhookDetails
- `webhookSecret`: string
- `webhookSourceRepo`: string

## WebhookEventProcessingDetails
- `eventFound`: boolean
- `eventId`: string
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `triggerIdentifier`: string
- `pipelineIdentifier`: string
- `pipelineExecutionId`: string
- `exceptionOccured`: boolean
- `status`: string
- `message`: string
- `payload`: string
- `eventCreatedAt`: integer
- `runtimeInput`: string
- `warningMsg`: string

## WebhookExecRequest
> Harness Regstries HTTP Webhook Request
- `body`: string
- `headers`: string
- `url`: string

## WebhookExecResponse
> Harness Regstries HTTP Webhook Response
- `body`: string
- `headers`: string
- `status`: string
- `statusCode`: integer

## WebhookExecResult
> refers to webhook execution

## WebhookExecution
> Harness Regstries Webhook Execution
- `created`: integer
- `duration`: integer
- `error`: string
- `id`: integer
- `request`: obj
- `response`: obj
- `result`: obj
- `retriggerOf`: integer
- `retriggerable`: boolean
- `triggerType`: obj
- `webhookId`: integer

## WebhookExecutionDetails
- `webhookProcessingDetails`: obj
- `executionDetails`: object
- `executionUrl`: string

## WebhookInfo
- `webhookId`: string

## WebhookRequest
- required: insecure, enabled, identifier, url, name
- `description`: string
- `enabled`: boolean
- `extraHeaders`: array
- `identifier`: string
- `insecure`: boolean
- `name`: string
- `secretIdentifier`: string
- `secretSpaceId`: integer
- `secretSpacePath`: string
- `triggers`: array
- `url`: string

## WebhookResponse
> Contains information about the webhooks 
- `webhook_identifier`: string
- `webhook_name`: string
- `is_enabled`: boolean
- `event_trigger_time`: integer
- `spec`: obj

## WebhookResponseSpec
> Details of the Webhook Response defined in Harness
- `webhook_type`: string; enum: GIT, GENERIC, SLACK

## WebhookSpec
> Details of the Webhook defined in Harness
- `webhook_type`: string; enum: GIT, GENERIC, SLACK

## WebhookTriggerSource

## WebhookTriggerSpec
> Spec for Webhook Triggers
- required: type, spec
- `type`: string; enum: Github, Gitlab, Bitbucket, AwsCodeCommit, AzureRepo, Harness, Custom

## WindowBasedServiceLevelIndicatorSpec
- required: spec

## WorkspaceProviderConnector
> Workspace provider connector
- required: connector_ref, type
- `connector_ref`: string; maxLen 128
- `created`: integer
- `id`: integer
- `terragrunt_provider`: boolean
- `type`: string; enum: aws, azure, gcp, vault
- `updated`: integer
- `workspace_id`: integer

## WorkspaceVariable
> Workspace Variable describes a base variable associated with a workspace. It is intended to be extended
into specific types which are then used.
- required: account, org, project, workspace, key, value, value_type, kind
- `account`: string; maxLen 128
- `key`: string; pattern `^[a-zA-Z0-9_]+$`; maxLen 128
- `kind`: string; enum: env, tf
- `org`: string; maxLen 128
- `project`: string; maxLen 128
- `value`: string
- `value_type`: string; enum: string, secret
- `workspace`: string

## WorkspaceVariableResourceCollection

## XMattersConnectorDTO
- required: url

## ZoomConnector
> Zoom Connector details.
- required: apiAccessType

## action.ActionTemplateProperties
- `containerAction`: obj
- `customScriptAction`: obj
- `delayAction`: obj

## action.ActionTemplateRunProperties
- `initialDelay`: string
- `interval`: string
- `maxRetries`: obj
- `stopOnFailure`: boolean
- `timeout`: string
- `verbosity`: string

## action.CustomScriptActionTemplate
- `args`: array
- `command`: string
- `env`: array

## action.DelayActionTemplate
- `duration`: string

## actions.ExecutedByExperiment
- `experimentID`: string
- `experimentName`: string
- `experimentRunID`: string
- `notifyID`: string
- `updatedAt`: integer
- `updatedBy`: obj

## actions.ImportActionTemplateRequest
- required: actionRef, identity, importType, name
- `actionRef`: string
- `description`: string
- `hubIdentifiers`: obj
- `hubRef`: string
- `identity`: string
- `importType`: obj
- `managedBy`: obj
- `name`: string
- `tags`: array

## actions.InfrastructureType

## actions.ListActionTemplateResponse
- `data`: array
- `pagination`: obj

## actions.RecentExecutions
- `executedByExperiment`: obj
- `status`: string
- `stepName`: string

## api.GetHarnessInfrastructureResponse
- `connectorRef`: string
- `correlationID`: string
- `environmentRef`: string
- `identifier`: string
- `isCompatible`: boolean
- `isUsed`: boolean
- `name`: string
- `namespace`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `serviceAccount`: string
- `type`: string

## api.HarnessInfrastructure
- `connectorRef`: string
- `environmentRef`: string
- `identifier`: string
- `isCompatible`: boolean
- `isUsed`: boolean
- `name`: string
- `namespace`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `serviceAccount`: string
- `type`: string

## api.ListHarnessInfrastructureResponse
- `items`: array
- `page`: obj

## applicationsApplicationRollbackRequest
- `name`: string
- `id`: string
- `dryRun`: boolean
- `prune`: boolean
- `appNamespace`: string
- `project`: string

## applicationsApplicationSetTemplate
- `metadata`: obj
- `spec`: obj

## applicationsApplicationSetTemplateMeta
- `name`: string
- `namespace`: string
- `labels`: object
- `annotations`: object
- `finalizers`: array

## applicationsSecretRef
> SecretRef struct for a reference to a secret key.
- `secretName`: string
- `key`: string

## appprojectsApplicationDestinationServiceAccount
> ApplicationDestinationServiceAccount holds information about the service account to be impersonated for the application sync operation.
- `server`: string
- `namespace`: string
- `defaultServiceAccount`: string

## common.ContainerTemplate
- `affinity`: obj
- `annotations`: object
- `args`: string
- `command`: array
- `containerSecurityContext`: obj
- `env`: array
- `hostIPC`: boolean
- `hostNetwork`: boolean
- `hostPID`: boolean
- `image`: string
- `imagePullPolicy`: obj
- `imagePullSecrets`: array
- `labels`: object
- `namespace`: string
- `nodeSelector`: object
- `podSecurityContext`: obj
- `resources`: obj
- `serviceAccountName`: string
- `tolerations`: array
- `volumeMounts`: array
- `volumes`: array

## common.VolumeInputTemplate
- `defaultMode`: string
- `items`: object
- `name`: string
- `optional`: boolean

## database.DiscoveredKubernetesService
- `annotations`: object
- `clusterIP`: string
- `clusterIPs`: array
- `externalIPs`: array
- `externalName`: string
- `identity`: obj
- `labels`: object
- `loadBalancerIP`: string
- `ports`: array
- `type`: obj

## database.DiscoveredServiceCollection
- required: accountIdentifier, agentID, agentIdentity, environmentIdentifier, id, name, spec, type, version
- `accountIdentifier`: string
- `agentID`: string
- `agentIdentity`: string
- `createdAt`: string
- `createdBy`: string
- `environmentIdentifier`: string
- `id`: string
- `name`: string
- `organizationIdentifier`: string
- `projectIdentifier`: string
- `removed`: boolean
- `removedAt`: string
- `spec`: obj
- `type`: string
- `updatedAt`: string
- `updatedBy`: string
- `version`: string

## database.DiscoveredServiceKubernetesSpec
- `kind`: string
- `name`: string
- `namespace`: string
- `service`: obj
- `uid`: string
- `workloads`: array

## database.DiscoveredServiceSpec
- `fqdn`: array
- `harnessEnvironmentIdentity`: obj
- `harnessServiceIdentity`: obj
- `ip`: array
- `kubernetes`: obj
- `port`: array

## database.EnvironmentIdentity
- `accountIdentifier`: string
- `identifier`: string
- `infraIdentifier`: string
- `organizationIdentifier`: string
- `projectIdentifier`: string

## database.ServiceCollection
- required: accountIdentifier, agentID, apiVersion, environmentIdentifier, id, kind, name, namespace, resourceVersion, spec, uid
- `accountIdentifier`: string
- `agentID`: string
- `annotations`: object
- `apiVersion`: string
- `createdAt`: string
- `createdBy`: string
- `creationTimestamp`: string
- `deletionTimestamp`: string
- `environmentIdentifier`: string
- `id`: string
- `kind`: string
- `labels`: object
- `name`: string
- `namespace`: string
- `organizationIdentifier`: string
- `ownerReference`: array
- `projectIdentifier`: string
- `removed`: boolean
- `removedAt`: string
- `resourceVersion`: string
- `spec`: obj
- `status`: obj
- `uid`: string
- `updatedAt`: string
- `updatedBy`: string

## database.ServiceIdentity
- `accountIdentifier`: string
- `identifier`: string
- `organizationIdentifier`: string
- `projectIdentifier`: string

## experiment.Secret
- `defaultMode`: integer
- `mountPath`: string
- `name`: string

## experimenttemplate.Action
- `continueOnCompletion`: boolean
- `identity`: string
- `infraId`: string
- `isEnterprise`: boolean
- `name`: string
- `revision`: integer
- `values`: array

## experimenttemplate.Fault
- `authEnabled`: boolean
- `identity`: string
- `infraId`: string
- `isEnterprise`: boolean
- `name`: string
- `revision`: string
- `values`: array

## experimenttemplate.ListExperimentTemplateData
- `description`: string
- `identity`: string
- `infraType`: obj
- `name`: string
- `tags`: array

## experimenttemplate.Probe
- `conditions`: array
- `duration`: string
- `enableDataCollection`: boolean
- `identity`: string
- `infraId`: string
- `isEnterprise`: boolean
- `name`: string
- `revision`: integer
- `values`: array
- `weightage`: integer

## experimenttemplate.ProbeConditions
- `executeUpon`: string

## experimenttemplate.Spec
- required: infraType
- `actions`: array
- `cleanupPolicy`: obj
- `faults`: array
- `infraId`: string
- `infraType`: obj
- `probes`: array
- `statusCheckTimeouts`: obj
- `vertices`: array

## experimenttemplate.StatusCheckTimeout
- `delay`: integer
- `timeout`: integer

## experimenttemplate.Vertex
- required: name
- `end`: obj
- `name`: string
- `start`: obj

## experimenttemplate.VertexChild
- `actions`: array
- `faults`: array
- `probes`: array

## experimenttemplate.VertexResource
- required: name
- `name`: string

## fault.TemplateReference
- `hubIdentity`: string
- `identity`: string
- `organizationIdentifier`: string
- `projectIdentifier`: string
- `revision`: string

## faulttemplate.AWSAuth
- `identifier`: string

## faulttemplate.ApplicationTarget
- `application`: string
- `entrypoint`: string

## faulttemplate.Auth
- `aws`: obj
- `azure`: obj
- `gcp`: obj
- `redis`: obj
- `ssh`: obj
- `vmware`: obj

## faulttemplate.AzureAuth
- `identifier`: string

## faulttemplate.ConfigMapVolume
- `mountMode`: integer
- `mountPath`: string
- `name`: string

## faulttemplate.FaultTemplate
- required: identity, name
- `apiVersion`: string
- `category`: array
- `description`: string
- `identity`: string
- `infraType`: string
- `infras`: array
- `inputs`: array
- `isDefault`: boolean
- `keywords`: array
- `kind`: string
- `links`: array
- `name`: string
- `permissionsRequired`: string
- `platforms`: array
- `revision`: string
- `spec`: obj
- `tags`: array
- `type`: string
- `variables`: array

## faulttemplate.GCPAuth
- `identifier`: string

## faulttemplate.HostPathVolume
- `hostPath`: string
- `mountPath`: string
- `name`: string
- `type`: obj

## faulttemplate.KubernetesTarget
- `kind`: string
- `labels`: string
- `names`: string
- `namespace`: string

## faulttemplate.Link
- `name`: string
- `url`: string

## faulttemplate.RedisAuth
- `password`: string

## faulttemplate.ResourceRequirements
- `limits`: object
- `requests`: object

## faulttemplate.SSHAuth
- `key`: string
- `password`: string

## faulttemplate.SecretVolume
- `mountMode`: integer
- `mountPath`: string
- `name`: string

## faulttemplate.Spec
- `chaos`: obj
- `target`: obj

## faulttemplate.StatusCheckTimeout
- `delay`: integer
- `timeout`: integer

## faulttemplate.TLS
- `caFile`: string
- `certFile`: string
- `clientCertFile`: string
- `keyFile`: string

## faulttemplate.Target
- `application`: obj
- `kubernetes`: array

## faulttemplate.VMWareAuth
- `govcPassword`: string
- `govcUrl`: string
- `govcUsername`: string
- `vCenterPassword`: string
- `vCenterServer`: string
- `vCenterUsername`: string
- `vmPassword`: string

## github_com_harness_hce-saas_graphql_server_pkg_database_mongodb_probe.SecretManager
- `identifier`: string

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.AppDynamicsProbeInputs
- `appdMetrics`: obj
- `connectorID`: string

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.AppdMetrics
- `applicationName`: string
- `durationInMin`: obj
- `metricsFullPath`: string

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.DatadogApmProbeInputs
- `connectorID`: string
- `durationInMin`: obj
- `query`: string
- `syntheticsTest`: obj

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.DatadogSyntheticsTestType

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.DynatraceApmProbeInputs
- `connectorID`: string
- `durationInMin`: obj
- `metrics`: obj

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.ENV
- `name`: string
- `value`: string

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.GET
- `criteria`: string
- `responseBody`: string
- `responseCode`: string

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.GcpCloudMonitoringProbeInputs
- `projectID`: string
- `query`: string
- `serviceAccountKey`: string

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.Headers
- `key`: string
- `value`: string

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.Identifier
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.NewRelicMetric
- `query`: string
- `queryMetric`: string

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.NewRelicProbeInputs
- `connectorID`: string
- `newRelicMetric`: obj

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.POST
- `body`: string
- `bodyPath`: string
- `contentType`: string
- `criteria`: string
- `responseBody`: string
- `responseCode`: string

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.PrometheusProbeInputs
- `connectorID`: string
- `query`: string
- `tlsConfig`: obj

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.SecretManager
- `identifier`: string

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.SplunkObservabilityMetrics
- `durationInMin`: obj
- `query`: string

## github_com_harness_hce-saas_hce-sdk_template_schema_probe.SplunkObservabilityProbeInputs
- `connectorID`: string
- `splunkObservabilityMetrics`: obj

## infra_v2.GetKubernetesInfrastructureV2YamlRequest
- `annotation`: object
- `containers`: string
- `correlationId`: string
- `env`: array
- `environmentID`: string
- `identifier`: obj
- `identity`: string
- `infraNamespace`: string
- `insecureSkipVerify`: boolean
- `label`: object
- `mtls`: obj
- `nodeSelector`: object
- `proxy`: obj
- `runAsGroup`: integer
- `runAsUser`: integer
- `serviceAccount`: string
- `tolerations`: array
- `volumeMounts`: array
- `volumes`: array

## infra_v2.GetKubernetesInfrastructureV2YamlResponse
- `correlationId`: string
- `yaml`: string

## infra_v2.KubernetesInfrastructureV2Details
- `annotation`: object
- `containers`: string
- `createdAt`: string
- `createdBy`: obj
- `deploymentType`: string
- `description`: string
- `discoveryAgentID`: string
- `env`: array
- `environmentID`: string
- `harnessInfraType`: string
- `identifier`: obj
- `identity`: string
- `imageRegistry`: obj
- `infraID`: string
- `infraNamespace`: string
- `infraScope`: obj
- `infraType`: obj
- `insecureSkipVerify`: boolean
- `installationType`: obj
- `isAIEnabled`: boolean
- `isAutopilotEnabled`: boolean
- `isChaosEnabled`: boolean
- `k8sConnectorID`: string
- `label`: object
- `lastHeartbeat`: integer
- `lastWorkflowTimestamp`: string
- `mtls`: obj
- `name`: string
- `noOfSchedules`: integer
- `noOfWorkflows`: integer
- `nodeSelector`: object
- `platformName`: string
- `proxy`: obj
- `runAsGroup`: integer
- `runAsUser`: integer
- `serviceAccount`: string
- `status`: obj
- `tags`: array
- `tolerations`: array
- `updateStatus`: obj
- `updatedAt`: string
- `updatedBy`: obj
- `upgrade`: obj
- `version`: string
- `volumeMounts`: array
- `volumes`: array

## infra_v2.RegisterInfrastructureV2Request
- `aiEnabled`: boolean
- `annotation`: object
- `autopilotEnabled`: boolean
- `containers`: string
- `correlationId`: string
- `description`: string
- `discoveryAgentID`: string
- `env`: array
- `environmentID`: string
- `identifier`: obj
- `identity`: string
- `imageRegistry`: obj
- `infraID`: string
- `infraNamespace`: string
- `infraScope`: obj
- `infraType`: obj
- `insecureSkipVerify`: boolean
- `k8sConnectorID`: string
- `label`: object
- `mtls`: obj
- `name`: string
- `nodeSelector`: object
- `proxy`: obj
- `runAsGroup`: integer
- `runAsUser`: integer
- `serviceAccount`: string
- `tags`: array
- `tolerations`: array
- `volumeMounts`: array
- `volumes`: array

## infra_v2.RegisterInfrastructureV2Response
- `identity`: string
- `name`: string
- `token`: string

## infra_v2.UpdateKubernetesInfrastructureV2Request
- `aiEnabled`: boolean
- `annotation`: object
- `autopilotEnabled`: boolean
- `containers`: string
- `correlationId`: string
- `description`: string
- `env`: array
- `environmentID`: string
- `identity`: string
- `imageRegistry`: obj
- `infraNamespace`: string
- `insecureSkipVerify`: boolean
- `label`: object
- `mtls`: obj
- `name`: string
- `nodeSelector`: object
- `proxy`: obj
- `runAsGroup`: integer
- `runAsUser`: integer
- `serviceAccount`: string
- `tags`: array
- `tolerations`: array
- `volumeMounts`: array
- `volumes`: array

## infra_v2.UpdateKubernetesInfrastructureV2Response
- `correlationId`: string
- `message`: string

## inputset.InputSet
- required: accountID
- `accountID`: string
- `createdAt`: integer
- `createdBy`: string
- `description`: string
- `experimentID`: string
- `id`: string
- `identity`: string
- `isRemoved`: boolean
- `name`: string
- `orgID`: string
- `projectID`: string
- `spec`: string
- `updatedAt`: integer
- `updatedBy`: string
- `version`: string

## inputsets.CreateInputSetRequest
- `description`: string
- `identity`: string
- `name`: string
- `spec`: string

## inputsets.CreateInputSetResponse
- `correlationID`: string
- `data`: obj

## inputsets.DeleteInputSetResponse
- `correlationID`: string

## inputsets.GetInputSetResponse
- `correlationID`: string
- `data`: obj

## inputsets.ListInputSetResponse
- `correlationID`: string
- `data`: array
- `pagination`: obj

## inputsets.UpdateInputSetRequest
- `description`: string
- `name`: string
- `spec`: string

## inputsets.UpdateInputSetResponse
- `correlationID`: string
- `data`: obj

## kubernetes_infra.UpdateKubernetesInfrastructureResponse
- `correlationId`: string
- `message`: string

## kubernetes_infra.UpgradeKubernetesInfrastructureResponse
- `message`: string
- `name`: string

## model.Infrastructure
- `clusterType`: obj
- `createdAt`: string
- `createdBy`: obj
- `description`: string
- `environmentID`: string
- `identifiers`: obj
- `infraID`: string
- `infraNamespace`: string
- `infraScope`: obj
- `infraType`: obj
- `isActive`: boolean
- `isInfraConfirmed`: boolean
- `isRemoved`: boolean
- `lastHeartbeat`: string
- `name`: string
- `startTime`: string
- `tags`: array
- `updatedAt`: string
- `updatedBy`: obj
- `version`: string

## model.InfrastructureType

## model.TemplateRef
- `hubRef`: string
- `identity`: string
- `ref`: string
- `revision`: string

## networkmap.GetTargetServiceResponse
- `chaosDetails`: obj
- `discoveryDetails`: obj
- `workloadDetails`: obj

## networkmap.ListTargetService
- `chaosDetails`: obj
- `discoveryDetails`: obj

## networkmap.ListTargetServiceResponse
- `data`: array
- `page`: obj

## networkmap.TargetServiceDetails
- required: id, kind, name
- `averageResiliencyScore`: number
- `id`: string
- `kind`: obj
- `kubernetes`: obj
- `name`: string
- `removed`: boolean
- `resiliencyCoverage`: number
- `serviceIdentity`: obj

## pipelineonboarding.InfrastructureOnboardingMapping
- `environmentIdentity`: string
- `identity`: string
- `onboardingId`: string
- `status`: string

## pipelineonboarding.InfrastructuresStatus
- `isChaosEnabled`: boolean

## pipelineonboarding.ListPipelineOnboardingResponse
- `pipelineOnboardings`: array

## pipelineonboarding.PipelineOnboarding
- required: accountID, isRemoved
- `accountID`: string
- `chaosAdvanceConfiguration`: obj
- `createdAt`: integer
- `createdBy`: string
- `discoveryAdvanceConfiguration`: obj
- `infrastructures`: object
- `isAiEnabled`: boolean
- `isRemoved`: boolean
- `message`: string
- `orgID`: string
- `pipelineIdentity`: string
- `pipelineName`: string
- `projectID`: string
- `selectedExperiments`: array
- `services`: object
- `singleClickOnboardings`: array
- `status`: obj
- `updatedAt`: integer
- `updatedBy`: string

## pipelineonboarding.SelectedExperiment
- `environmentIdentity`: string
- `experimentId`: string
- `identity`: string
- `infraId`: string
- `infrastructureIdentity`: string
- `name`: string
- `serviceNames`: array
- `tags`: array

## pipelineonboarding.Status

## pipelines.BulkExperimentRunResponse
- `createPipelineResponse`: obj
- `stageID`: string

## pipelines.CreatePipelineResponse
- `code`: string
- `correlationId`: string
- `data`: object
- `message`: string
- `metaData`: obj
- `status`: string

## pipelines.ExecutorInfo
- `email`: string
- `triggerType`: string
- `username`: string

## pipelines.ExperimentSpec
- `expectedResilienceScore`: number
- `experimentID`: string
- `experimentName`: string

## probe.APMProbeTemplate
- `appDynamicsProbeInputs`: obj
- `comparator`: obj
- `datadogApmProbeInputs`: obj
- `dynatraceApmProbeInputs`: obj
- `gcpCloudMonitoringProbeInputs`: obj
- `newRelicProbeInputs`: obj
- `prometheusProbeInputs`: obj
- `splunkObservabilityProbeInputs`: obj
- `type`: obj

## probe.AuthorizationTemplate
- `credentials`: string
- `type`: string

## probe.CmdProbeTemplate
- `command`: string
- `comparator`: obj
- `env`: array
- `source`: string

## probe.ComparatorTemplate
- `criteria`: string
- `type`: string
- `value`: string

## probe.ContainerProbeTemplate
- `affinity`: obj
- `annotations`: object
- `args`: string
- `command`: array
- `comparator`: obj
- `containerSecurityContext`: obj
- `env`: array
- `hostIPC`: boolean
- `hostNetwork`: boolean
- `hostPID`: boolean
- `image`: string
- `imagePullPolicy`: obj
- `imagePullSecrets`: array
- `labels`: object
- `namespace`: string
- `nodeSelector`: object
- `podSecurityContext`: obj
- `resources`: obj
- `serviceAccountName`: string
- `tolerations`: array
- `volumeMounts`: array
- `volumes`: array

## probe.DatadogMetricsTemplate
- `comparator`: obj
- `query`: string
- `timeFrame`: string

## probe.DatadogProbeTemplate
- `datadogCredentialsSecretName`: string
- `datadogSite`: string
- `metrics`: obj
- `syntheticsTest`: obj

## probe.DynatraceMetricsTemplate
- `entitySelector`: string
- `metricsSelector`: string

## probe.DynatraceProbeTemplate
- `apiTokenSecretName`: string
- `comparator`: obj
- `endpoint`: string
- `metrics`: obj
- `timeFrame`: string

## probe.EvaluationWindowTemplate
- `evaluationEndTime`: obj
- `evaluationStartTime`: obj

## probe.HttpProbeTemplate
- `auth`: obj
- `headers`: array
- `method`: obj
- `tlsConfig`: obj
- `url`: string

## probe.InfrastructureType

## probe.K8SProbeTemplate
- `fieldSelector`: string
- `group`: string
- `labelSelector`: string
- `namespace`: string
- `operation`: string
- `resource`: string
- `resourceNames`: string
- `version`: string

## probe.MethodTemplate
- `get`: obj
- `post`: obj

## probe.ProbeTemplateProperties
- `apmProbe`: obj
- `cmdProbe`: obj
- `containerProbe`: obj
- `datadogProbe`: obj
- `dynatraceProbe`: obj
- `httpProbe`: obj
- `k8sProbe`: obj
- `promProbe`: obj
- `sloProbe`: obj

## probe.ProbeTemplateRunProperties
- `attempt`: obj
- `initialDelay`: string
- `interval`: string
- `pollingInterval`: string
- `retry`: obj
- `stopOnFailure`: boolean
- `timeout`: string
- `verbosity`: string

## probe.PromProbeTemplate
- `auth`: obj
- `comparator`: obj
- `endpoint`: string
- `query`: string
- `queryPath`: string
- `tlsConfig`: obj

## probe.SLOProbeTemplate
- `comparator`: obj
- `evaluationTimeout`: string
- `evaluationWindow`: obj
- `insecureSkipVerify`: boolean
- `platformEndpoint`: string
- `sloIdentifier`: string
- `sloSourceMetadata`: obj

## probe.SLOSourceMetadataTemplate
- `apiTokenSecret`: string
- `scope`: obj

## probe.SyntheticsTestTemplate
- `publicId`: string
- `testType`: obj

## probe.TLSConfigTemplate
- `caFile`: string
- `certFile`: string
- `insecureSkipVerify`: boolean
- `keyFile`: string

## recommendation.PipelineFilters
- `pipelineID`: string
- `pipelineName`: string
- `serviceID`: string
- `serviceName`: string

## recommendations.PipelineAddExperimentResponse
- `pipelineID`: string
- `pipelineName`: string
- `stageID`: string

## repositoriesAWSSecretRef
- `awsAccessKeyID`: string
- `awsSecretAccessKey`: string
- `awsSessionToken`: string

## repositoriesKsonnetEnvironment
- `name`: string
- `k8sVersion`: string
- `destination`: obj

## repositoriesKsonnetEnvironmentDestination
- `server`: string
- `namespace`: string

## repositoriesServiceAccountSelector
- `name`: string
- `namespace`: string
- `audiences`: array

## risks.ActiveExecutionResponse
- `duration`: string
- `executedBy`: obj
- `executionID`: integer
- `executionType`: obj
- `lastUpdatedAt`: integer
- `name`: string
- `parentIdentity`: string
- `probeID`: string
- `probeName`: string
- `runID`: string
- `startedAt`: integer
- `status`: obj

## risks.ExecutionType

## risks.Infrastructure

## risks.ListExecutionResponse
- `correlationID`: string
- `data`: array
- `pagination`: obj

## servicev1AppProject
> AppProject and AppProjectV2 currently only represent mapping and are lightweight objects
that persist the mapping between argocd projects and harness projects.
For managing ArgoCD Projects via Agent, there is AgentProjectService (older one with inconsistent implementation) and AgentArgoProjectService.
- `accountIdentifier`: string
- `projectIdentifier`: string
- `orgIdentifier`: string
- `name`: string
- `createdAt`: string
- `lastModifiedAt`: string
- `agentIdentifier`: string
- `autoCreateServiceEnv`: boolean

## servicev1AppProjectMapping
- `appProjMap`: object

## servicev1Application
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `agentIdentifier`: string
- `name`: string
- `clusterIdentifier`: string
- `repoIdentifier`: string
- `app`: obj
- `createdAt`: string
- `lastModifiedAt`: string
- `stale`: boolean
- `skipRepoValidation`: boolean
- `repoIdentifiers`: array
- `parentAppRef`: string
- `governanceMetadata`: obj

## servicev1ApplicationDeleteRequestOptions
- `removeExistingFinalizers`: boolean
- `forceDelete`: boolean

## servicev1ApplicationPatchRequest
- `agentIdentifier`: string
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `request`: obj

## servicev1ApplicationQuery
- `accountIdentifier`: string
- `projectIdentifier`: string
- `orgIdentifier`: string
- `searchTerm`: string
- `pageSize`: integer
- `pageIndex`: integer
- `filter`: object
- `sortBy`: obj
- `sortOrder`: obj
- `metadataOnly`: boolean
- `fields`: array

## servicev1ApplicationSet
- `identifier`: string
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `agentIdentifier`: string
- `createdAt`: string
- `lastModifiedAt`: string
- `owner`: string
- `appset`: obj

## servicev1ApplicationSetList
- `content`: array
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `pageIndex`: integer
- `empty`: boolean

## servicev1Applicationlist
- `content`: array
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `pageIndex`: integer
- `empty`: boolean

## servicev1Cluster
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `agentIdentifier`: string
- `identifier`: string
- `cluster`: obj
- `createdAt`: string
- `lastModifiedAt`: string
- `stale`: boolean
- `tags`: object

## servicev1ClusterQuery
- `accountIdentifier`: string
- `projectIdentifier`: string
- `orgIdentifier`: string
- `agentIdentifier`: string
- `identifier`: string
- `searchTerm`: string
- `pageSize`: integer
- `pageIndex`: integer
- `filter`: object
- `sortBy`: obj
- `sortOrder`: obj
- `includeChildScopes`: boolean

## servicev1GnuPGPublicKeyList
- `content`: array
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `pageIndex`: integer
- `empty`: boolean

## servicev1HealthStatus

## servicev1Project
- `projectIdentifier`: string
- `orgIdentifier`: string
- `autoCreateServiceEnv`: boolean

## servicev1ReconcilerFilter
- `projectNames`: array

## servicev1Repository
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `agentIdentifier`: string
- `identifier`: string
- `repository`: obj
- `createdAt`: string
- `lastModifiedAt`: string
- `stale`: boolean
- `repositoryCredentialsId`: string

## servicev1RepositoryCertificate
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `agentIdentifier`: string
- `cert`: obj
- `createdAt`: string
- `lastModifiedAt`: string

## servicev1RepositoryCredentials
- `accountIdentifier`: string
- `orgIdentifier`: string
- `projectIdentifier`: string
- `agentIdentifier`: string
- `identifier`: string
- `repoCreds`: obj
- `createdAt`: string
- `lastModifiedAt`: string
- `stale`: boolean

## servicev1RepositoryCredentialsList
- `content`: array
- `totalPages`: integer
- `totalItems`: integer
- `pageItemCount`: integer
- `pageSize`: integer
- `pageIndex`: integer
- `empty`: boolean

## targetservice.DiscoveredServiceSpec
- `id`: string
- `kind`: string
- `label`: object
- `name`: string
- `namespace`: string
- `uuid`: string

## targetservice.ServiceMetadata
- `id`: string
- `name`: string
- `namespace`: string
- `uid`: string

## targetservice.ServiceSpec
- `discoveredService`: obj

## targetservice.TargetService
- required: accountID, isRemoved
- `accountID`: string
- `averageResiliencyScore`: number
- `createdAt`: integer
- `createdBy`: string
- `environmentRef`: string
- `externalId`: string
- `id`: string
- `infrastructureId`: string
- `isRemoved`: boolean
- `licenseId`: string
- `name`: string
- `orgID`: string
- `projectID`: string
- `resiliencyCoverage`: number
- `spec`: obj
- `totalExperimentCount`: integer
- `type`: obj
- `updatedAt`: integer
- `updatedBy`: string

## template.InputCategory

## template.InputType

## template.RunTimeInputs
- `experiment`: array
- `tasks`: object

## template.Variable
- required: name, value
- `allowedValues`: array
- `category`: obj
- `default`: obj
- `description`: string
- `name`: string
- `path`: string
- `required`: boolean
- `stringify`: boolean
- `tags`: array
- `tooltipId`: string
- `type`: obj
- `validator`: string
- `value`: obj

## template.VariableMinimum
- required: name, value
- `name`: string
- `value`: obj

## types.CreateExperimentFromTemplateRequest
- required: accountIdentifier, name
- `accountIdentifier`: string
- `description`: string
- `identity`: string
- `importType`: obj
- `infraRef`: string
- `name`: string
- `organizationIdentifier`: string
- `projectIdentifier`: string
- `tags`: array

## types.ExecutedByExperiment
- `experimentID`: string
- `experimentName`: string
- `experimentRunID`: string
- `experimentType`: obj
- `notifyID`: string
- `updatedAt`: integer
- `updatedBy`: obj

## types.ImportProbeTemplateRequest
- required: identity, importType, name, probeRef
- `description`: string
- `hubIdentifiers`: obj
- `hubRef`: string
- `identity`: string
- `importType`: obj
- `managedBy`: obj
- `name`: string
- `probeRef`: string
- `tags`: array

## types.InfrastructureType

## types.ProbeRecentExecutions
- `executedByExperiment`: obj
- `faultName`: string
- `status`: obj

## types.TemplateResourceDetails
- `identity`: string
- `name`: string
- `revision`: string

## types.TemplateResources
- `actions`: array
- `faults`: array
- `probes`: array

## v1.PersistentVolumeClaimTemplate
- `metadata`: obj
- `spec`: obj

## v1.SecretEnvSource
- `name`: string
- `optional`: boolean

## v1.SecretKeySelector
- `key`: string
- `name`: string
- `optional`: boolean

## v1.SecretProjection
- `items`: array
- `name`: string
- `optional`: boolean

## v1.SecretVolumeSource
- `defaultMode`: integer
- `items`: array
- `optional`: boolean
- `secretName`: string

## v1.ServiceAccountTokenProjection
- `audience`: string
- `expirationSeconds`: integer
- `path`: string

## v1.ServiceAffinity

## v1.ServiceExternalTrafficPolicyType

## v1.ServiceInternalTrafficPolicyType

## v1.ServicePort
- `appProtocol`: string
- `name`: string
- `nodePort`: integer
- `port`: integer
- `protocol`: obj
- `targetPort`: obj

## v1.ServiceSpec
- `allocateLoadBalancerNodePorts`: boolean
- `clusterIP`: string
- `clusterIPs`: array
- `externalIPs`: array
- `externalName`: string
- `externalTrafficPolicy`: obj
- `healthCheckNodePort`: integer
- `internalTrafficPolicy`: obj
- `ipFamilies`: array
- `ipFamilyPolicy`: obj
- `loadBalancerClass`: string
- `loadBalancerIP`: string
- `loadBalancerSourceRanges`: array
- `ports`: array
- `publishNotReadyAddresses`: boolean
- `selector`: object
- `sessionAffinity`: obj
- `sessionAffinityConfig`: obj
- `topologyKeys`: array
- `type`: obj

## v1.ServiceStatus
- `conditions`: array
- `loadBalancer`: obj

## v1PersistentVolumeClaimTemplate
> PersistentVolumeClaimTemplate is used to produce
PersistentVolumeClaim objects as part of an EphemeralVolumeSource.
- `metadata`: obj
- `spec`: obj

## v1PodTemplateMetadata
- `labels`: object
- `annotations`: object

## v1PodTemplateSpec
- `metadata`: obj
- `spec`: obj

## v1RolloutAnalysisTemplate
- `templateName`: string
- `clusterScope`: boolean

## v1RolloutExperimentStepAnalysisTemplateRef
- `name`: string
- `templateName`: string
- `clusterScope`: boolean
- `args`: array
- `requiredForCompletion`: boolean

## v1RolloutExperimentTemplate
- `name`: string
- `specRef`: string
- `replicas`: integer
- `metadata`: obj
- `selector`: obj
- `weight`: integer
- `service`: obj

## v1SecretEnvSource
> SecretEnvSource selects a Secret to populate the environment
variables with.

The contents of the target Secret's Data field will represent the
key-value pairs as environment variables.
- `localObjectReference`: obj
- `optional`: boolean

## v1SecretKeySelector
- `localObjectReference`: obj
- `key`: string
- `optional`: boolean

## v1SecretProjection
> Adapts a secret into a projected volume.

The contents of the target Secret's Data field will be presented in a
projected volume as files using the keys in the Data field as the file names.
Note that this is identical to a secret volume source without the default
mode.
- `localObjectReference`: obj
- `items`: array
- `optional`: boolean

## v1SecretVolumeSource
> Adapts a Secret into a volume.

The contents of the target Secret's Data field will be presented in a volume
as files using the keys in the Data field as the file names.
Secret volumes support ownership management and SELinux relabeling.
- `secretName`: string
- `items`: array
- `defaultMode`: integer
- `optional`: boolean

## v1ServiceAccountTokenProjection
> ServiceAccountTokenProjection represents a projected service account token
volume. This projection can be used to insert a service account token into
the pods runtime filesystem for use against APIs (Kubernetes API Server or
otherwise).
- `audience`: string
- `expirationSeconds`: string
- `path`: string

## v1TemplateService
- `name`: string

## v2_onboarding.DiscoveredService
- `agentDetails`: obj
- `completedAgentCount`: integer
- `discoveredServiceCount`: integer
- `erroredAgentCount`: integer
- `isTracingEnabled`: boolean
- `pendingAgentCount`: integer
- `sDAgentID`: string
- `sDAgentIdentity`: string
- `status`: obj
- `totalAgentCount`: integer

## v2_onboarding.TargetServiceDetails
- `id`: string
- `name`: string

## v3.GetExperimentOrTemplateVariableData
- `name`: string
- `variables`: array

## v3.GetExperimentOrTemplateVariableResponse
- `items`: array

## v3.ListExperimentOrTemplateResponse
- `correlationId`: string
- `experiments`: array
- `pagination`: obj
- `templates`: array
