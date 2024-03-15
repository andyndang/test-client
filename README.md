# whylabs-client

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+<UNSET>.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.account.get_account_memberships(org_id='org-123', user_id='user-123', managed_org_id='org-123', role=operations.Role.VIEWER)

if res.get_account_memberships_response is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [account](docs/sdks/account/README.md)

* [get_account_memberships](docs/sdks/account/README.md#get_account_memberships) - Get memberships in an account
* [put_organization_memberships](docs/sdks/account/README.md#put_organization_memberships) - Replace the memberships in a specific role and managed organization
* [patch_organization_memberships](docs/sdks/account/README.md#patch_organization_memberships) - Add or delete memberships in a specific role and managed organization
* [list_managed_organizations](docs/sdks/account/README.md#list_managed_organizations) - List managed organizations for a parent organization
* [update_account_user](docs/sdks/account/README.md#update_account_user) - Update account user
* [create_account_user](docs/sdks/account/README.md#create_account_user) - Create an account user
* [get_account_user_by_email](docs/sdks/account/README.md#get_account_user_by_email) - Get account user by email
* [get_account_user_by_id](docs/sdks/account/README.md#get_account_user_by_id) - Get account user by user_id
* [delete_account_user](docs/sdks/account/README.md#delete_account_user) - Delete account user
* [list_account_users](docs/sdks/account/README.md#list_account_users) - List users in an account

### [internal](docs/sdks/internal/README.md)

* [get_account_memberships](docs/sdks/internal/README.md#get_account_memberships) - Get memberships in an account
* [put_organization_memberships](docs/sdks/internal/README.md#put_organization_memberships) - Replace the memberships in a specific role and managed organization
* [patch_organization_memberships](docs/sdks/internal/README.md#patch_organization_memberships) - Add or delete memberships in a specific role and managed organization
* [list_managed_organizations](docs/sdks/internal/README.md#list_managed_organizations) - List managed organizations for a parent organization
* [update_account_user](docs/sdks/internal/README.md#update_account_user) - Update account user
* [create_account_user](docs/sdks/internal/README.md#create_account_user) - Create an account user
* [get_account_user_by_email](docs/sdks/internal/README.md#get_account_user_by_email) - Get account user by email
* [get_account_user_by_id](docs/sdks/internal/README.md#get_account_user_by_id) - Get account user by user_id
* [delete_account_user](docs/sdks/internal/README.md#delete_account_user) - Delete account user
* [list_account_users](docs/sdks/internal/README.md#list_account_users) - List users in an account
* [add_account_users_from_memberships](docs/sdks/internal/README.md#add_account_users_from_memberships) - Adds account users for a managed organization and its child organizations based on existing memberships
* [delete_cache_key](docs/sdks/internal/README.md#delete_cache_key) - Delete cache key
* [list_cache_keys](docs/sdks/internal/README.md#list_cache_keys) - List cache keys
* [generate_report](docs/sdks/internal/README.md#generate_report) - Generate an admin report
* [activate_marketplace_subscription_internal](docs/sdks/internal/README.md#activate_marketplace_subscription_internal) - Activate Azure Marketplace subscription to an existing organization.
* [list_azure_marketplace_subscriptions](docs/sdks/internal/README.md#list_azure_marketplace_subscriptions) - List Azure Marketplace subscriptions
* [post_monitor_config_validation_job](docs/sdks/internal/README.md#post_monitor_config_validation_job) - Create a monitor config validation job for all configs
* [get_feature_flags](docs/sdks/internal/README.md#get_feature_flags) - Get feature flags for the specified user/org
* [update_membership_by_email](docs/sdks/internal/README.md#update_membership_by_email) - Updates the role in an membership
* [create_membership](docs/sdks/internal/README.md#create_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [remove_membership_by_email](docs/sdks/internal/README.md#remove_membership_by_email) - Removes membership in a given org from a user, using the user's email address.
* [get_default_membership_for_email](docs/sdks/internal/README.md#get_default_membership_for_email) - Get the default membership for a user.
* [set_default_membership](docs/sdks/internal/README.md#set_default_membership) - Sets the organization that should be used when logging a user in
* [get_memberships_by_org](docs/sdks/internal/README.md#get_memberships_by_org) - Get memberships for an org.
* [get_memberships_by_email](docs/sdks/internal/README.md#get_memberships_by_email) - Get memberships for a user given that user's email address.
* [get_memberships](docs/sdks/internal/README.md#get_memberships) - Get memberships for a user.
* [get_notification_settings](docs/sdks/internal/README.md#get_notification_settings) - Get notification settings for an org
* [update_notification_settings](docs/sdks/internal/README.md#update_notification_settings) - Update notification settings for an org
* [list_organizations](docs/sdks/internal/README.md#list_organizations) - Get a list of all of the organization ids.
* [~~update_org~~](docs/sdks/internal/README.md#update_org) - Update an existing organization :warning: **Deprecated**
* [create_organization](docs/sdks/internal/README.md#create_organization) - Create an organization
* [partially_update_organization](docs/sdks/internal/README.md#partially_update_organization) - Update some fields of an organization to non-null values
* [get_organization](docs/sdks/internal/README.md#get_organization) - Get the metadata about an organization.
* [update_organization](docs/sdks/internal/README.md#update_organization) - Update an existing organization
* [delete_organization](docs/sdks/internal/README.md#delete_organization) - Delete an org
* [list_api_keys](docs/sdks/internal/README.md#list_api_keys) - List API key metadata for a given organization and user
* [get_api_key](docs/sdks/internal/README.md#get_api_key) - Get an api key by its id
* [hide_segments](docs/sdks/internal/README.md#hide_segments) - Hides a list of segments
* [get_aws_marketplace_metadata](docs/sdks/internal/README.md#get_aws_marketplace_metadata) - Get marketplace metadata for an org if any exists.
* [list_monitor_config_v3_versions](docs/sdks/internal/README.md#list_monitor_config_v3_versions) - List the monitor config document versions for a given dataset.
* [get_monitor_config_v3_version](docs/sdks/internal/README.md#get_monitor_config_v3_version) - Get the monitor config document version for a given dataset.
* [put_request_monitor_run_config](docs/sdks/internal/README.md#put_request_monitor_run_config) - Put the RequestMonitorRun config into S3.
* [stripe_payment_endpoint](docs/sdks/internal/README.md#stripe_payment_endpoint) - Endpoint for Stripe payment webhooks
* [provision_aws_marketplace_new_user](docs/sdks/internal/README.md#provision_aws_marketplace_new_user) - Create resources for a new user coming from AWS Marketplace
* [provision_new_user](docs/sdks/internal/README.md#provision_new_user) - Create the resources that a new user needs to use WhyLabs via the website.
* [why_labs_search](docs/sdks/internal/README.md#why_labs_search) - WhyLabs Search
* [why_labs_search_indexing](docs/sdks/internal/README.md#why_labs_search_indexing) - WhyLabs Search Indexing
* [get_organization_subscriptions](docs/sdks/internal/README.md#get_organization_subscriptions) - Get organization subscription details
* [get_user_by_email](docs/sdks/internal/README.md#get_user_by_email) - Get a user by their email.
* [update_user](docs/sdks/internal/README.md#update_user) - Update a user.
* [create_user](docs/sdks/internal/README.md#create_user) - Create a user.
* [get_user](docs/sdks/internal/README.md#get_user) - Get a user by their id.
* [activate_azure_subscription](docs/sdks/internal/README.md#activate_azure_subscription) - Endpoint to activate Azure Marketplace subscriptions
* [azure_marketplace_webhook](docs/sdks/internal/README.md#azure_marketplace_webhook) - Endpoint for Azure Marketplace webhooks

### [admin](docs/sdks/admin/README.md)

* [add_account_users_from_memberships](docs/sdks/admin/README.md#add_account_users_from_memberships) - Adds account users for a managed organization and its child organizations based on existing memberships
* [delete_cache_key](docs/sdks/admin/README.md#delete_cache_key) - Delete cache key
* [list_cache_keys](docs/sdks/admin/README.md#list_cache_keys) - List cache keys
* [generate_report](docs/sdks/admin/README.md#generate_report) - Generate an admin report
* [activate_marketplace_subscription_internal](docs/sdks/admin/README.md#activate_marketplace_subscription_internal) - Activate Azure Marketplace subscription to an existing organization.
* [list_azure_marketplace_subscriptions](docs/sdks/admin/README.md#list_azure_marketplace_subscriptions) - List Azure Marketplace subscriptions
* [post_monitor_config_validation_job](docs/sdks/admin/README.md#post_monitor_config_validation_job) - Create a monitor config validation job for all configs

### [feature_flags](docs/sdks/featureflags/README.md)

* [get_feature_flags](docs/sdks/featureflags/README.md#get_feature_flags) - Get feature flags for the specified user/org

### [membership](docs/sdks/membership/README.md)

* [update_membership_by_email](docs/sdks/membership/README.md#update_membership_by_email) - Updates the role in an membership
* [create_membership](docs/sdks/membership/README.md#create_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [remove_membership_by_email](docs/sdks/membership/README.md#remove_membership_by_email) - Removes membership in a given org from a user, using the user's email address.
* [get_default_membership_for_email](docs/sdks/membership/README.md#get_default_membership_for_email) - Get the default membership for a user.
* [set_default_membership](docs/sdks/membership/README.md#set_default_membership) - Sets the organization that should be used when logging a user in
* [get_memberships_by_org](docs/sdks/membership/README.md#get_memberships_by_org) - Get memberships for an org.
* [get_memberships_by_email](docs/sdks/membership/README.md#get_memberships_by_email) - Get memberships for a user given that user's email address.
* [get_memberships](docs/sdks/membership/README.md#get_memberships) - Get memberships for a user.
* [list_organization_memberships](docs/sdks/membership/README.md#list_organization_memberships) - List organization memberships
* [update_organization_membership](docs/sdks/membership/README.md#update_organization_membership) - Updates the role in an membership
* [create_organization_membership](docs/sdks/membership/README.md#create_organization_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [remove_organization_membership](docs/sdks/membership/README.md#remove_organization_membership) - Removes membership in a given org from a user, using the user's email address.

### [notification_settings](docs/sdks/notificationsettings/README.md)

* [get_email_notification_action_payload](docs/sdks/notificationsettings/README.md#get_email_notification_action_payload) - Get dummy notification action payload
* [get_pager_duty_notification_action_payload](docs/sdks/notificationsettings/README.md#get_pager_duty_notification_action_payload) - Get dummy notification action payload
* [get_slack_notification_action_payload](docs/sdks/notificationsettings/README.md#get_slack_notification_action_payload) - Get dummy notification action payload
* [get_notification_settings](docs/sdks/notificationsettings/README.md#get_notification_settings) - Get notification settings for an org
* [update_notification_settings](docs/sdks/notificationsettings/README.md#update_notification_settings) - Update notification settings for an org
* [list_notification_actions](docs/sdks/notificationsettings/README.md#list_notification_actions) - List notification actions for an org
* [get_notification_action](docs/sdks/notificationsettings/README.md#get_notification_action) - Get notification action for id
* [delete_notification_action](docs/sdks/notificationsettings/README.md#delete_notification_action) - Delete notification action
* [disable_notification_action](docs/sdks/notificationsettings/README.md#disable_notification_action) - Disable notification action
* [enable_notification_action](docs/sdks/notificationsettings/README.md#enable_notification_action) - Enable notification action
* [test_notification_action](docs/sdks/notificationsettings/README.md#test_notification_action) - Test a notification action
* [put_notification_action](docs/sdks/notificationsettings/README.md#put_notification_action) - Add new notification action
* [add_notification_action](docs/sdks/notificationsettings/README.md#add_notification_action) - Add new notification action
* [update_notification_action](docs/sdks/notificationsettings/README.md#update_notification_action) - Update notification action

### [organizations](docs/sdks/organizations/README.md)

* [list_organizations](docs/sdks/organizations/README.md#list_organizations) - Get a list of all of the organization ids.
* [~~update_org~~](docs/sdks/organizations/README.md#update_org) - Update an existing organization :warning: **Deprecated**
* [create_organization](docs/sdks/organizations/README.md#create_organization) - Create an organization
* [partially_update_organization](docs/sdks/organizations/README.md#partially_update_organization) - Update some fields of an organization to non-null values
* [get_organization](docs/sdks/organizations/README.md#get_organization) - Get the metadata about an organization.
* [update_organization](docs/sdks/organizations/README.md#update_organization) - Update an existing organization
* [delete_organization](docs/sdks/organizations/README.md#delete_organization) - Delete an org
* [get_aws_marketplace_metadata](docs/sdks/organizations/README.md#get_aws_marketplace_metadata) - Get marketplace metadata for an org if any exists.

### [api_key](docs/sdks/apikey/README.md)

* [list_api_keys](docs/sdks/apikey/README.md#list_api_keys) - List API key metadata for a given organization and user
* [create_api_key](docs/sdks/apikey/README.md#create_api_key) - Generate an API key for a user.
* [revoke_api_key](docs/sdks/apikey/README.md#revoke_api_key) - Revoke the given API Key, removing its ability to access WhyLabs systems
* [get_api_key](docs/sdks/apikey/README.md#get_api_key) - Get an api key by its id

### [dataset_profile](docs/sdks/datasetprofile/README.md)

* [list_delete_analyzer_results_requests](docs/sdks/datasetprofile/README.md#list_delete_analyzer_results_requests) - List requests to delete analyzer results
* [list_delete_dataset_profiles_requests](docs/sdks/datasetprofile/README.md#list_delete_dataset_profiles_requests) - List requests to delete dataset profiles
* [delete_dataset_profiles](docs/sdks/datasetprofile/README.md#delete_dataset_profiles) - Deletes a set of dataset profiles
* [delete_analyzer_results](docs/sdks/datasetprofile/README.md#delete_analyzer_results) - Deletes a set of analyzer results
* [create_reference_profile](docs/sdks/datasetprofile/README.md#create_reference_profile) - Returns data needed to uploading the reference profile
* [hide_segments](docs/sdks/datasetprofile/README.md#hide_segments) - Hides a list of segments
* [get_profile_traces](docs/sdks/datasetprofile/README.md#get_profile_traces) - Returns a list for profile traces matching a trace id
* [list_reference_profiles](docs/sdks/datasetprofile/README.md#list_reference_profiles) - Returns a list for reference profiles between the given time range filtered on the upload timestamp
* [get_reference_profile](docs/sdks/datasetprofile/README.md#get_reference_profile) - Returns a single reference profile
* [delete_reference_profile](docs/sdks/datasetprofile/README.md#delete_reference_profile) - Delete a single reference profile
* [list_segments](docs/sdks/datasetprofile/README.md#list_segments) - Returns a list of segments

### [dataset_metadata](docs/sdks/datasetmetadata/README.md)

* [get_dataset_metadata](docs/sdks/datasetmetadata/README.md#get_dataset_metadata) - Get dataset metadata for the specified dataset
* [put_dataset_metadata](docs/sdks/datasetmetadata/README.md#put_dataset_metadata) - Put dataset metadata for the specified dataset
* [delete_dataset_metadata](docs/sdks/datasetmetadata/README.md#delete_dataset_metadata) - Delete dataset metadata for the specified dataset

### [feature_weights](docs/sdks/featureweights/README.md)

* [get_column_weights](docs/sdks/featureweights/README.md#get_column_weights) - Get column weights for the specified dataset
* [put_column_weights](docs/sdks/featureweights/README.md#put_column_weights) - Put column weights for the specified dataset

### [debug_events](docs/sdks/debugevents/README.md)

* [log_debug_event](docs/sdks/debugevents/README.md#log_debug_event) - Log a debug event

### [monitor_diagnostics](docs/sdks/monitordiagnostics/README.md)

* [detect_noisy_columns](docs/sdks/monitordiagnostics/README.md#detect_noisy_columns) - Endpoint to detect the noisiest columns for a specific analyzer and segment
* [detect_noisy_segments](docs/sdks/monitordiagnostics/README.md#detect_noisy_segments) - Endpoint to detect the noisiest segments for a specific analyzer
* [detect_noisy_analyzers](docs/sdks/monitordiagnostics/README.md#detect_noisy_analyzers) - Endpoint to detect noisy or failing analyzers
* [recommend_diagnostic_interval](docs/sdks/monitordiagnostics/README.md#recommend_diagnostic_interval) - Endpoint to recommend a diagnostic interval

### [log](docs/sdks/log/README.md)

* [log_async](docs/sdks/log/README.md#log_async) - Like /log, except this api doesn't take the actual profile content. It returns an upload link that can be used to upload the profile to.
* [get_profile_observatory_link](docs/sdks/log/README.md#get_profile_observatory_link) - Get observatory links for profiles in a given org/model. A max of 3 profiles can be viewed a a time.
* [~~log_reference~~](docs/sdks/log/README.md#log_reference) - Returns a presigned URL for uploading the reference profile to. :warning: **Deprecated**

### [models](docs/sdks/models/README.md)

* [list_models](docs/sdks/models/README.md#list_models) - Get a list of all of the model ids for an organization.
* [create_model](docs/sdks/models/README.md#create_model) - Create a model with a given name and a time period
* [get_entity_schema](docs/sdks/models/README.md#get_entity_schema) - Get the entity schema config for a given dataset.
* [put_entity_schema](docs/sdks/models/README.md#put_entity_schema) - Save the entity schema config for a given dataset.
* [delete_entity_schema](docs/sdks/models/README.md#delete_entity_schema) - Delete the entity schema config for a given dataset.
* [get_entity_schema_column](docs/sdks/models/README.md#get_entity_schema_column) - Get the entity schema of a single column for a given dataset.
* [put_entity_schema_column](docs/sdks/models/README.md#put_entity_schema_column) - Save the entity schema of a single column for a given dataset.
* [delete_entity_schema_column](docs/sdks/models/README.md#delete_entity_schema_column) - Delete the entity schema of a single column for a given dataset.
* [put_entity_schema_metric](docs/sdks/models/README.md#put_entity_schema_metric) - Save the schema of a single metric for a given dataset.
* [delete_entity_schema_metric](docs/sdks/models/README.md#delete_entity_schema_metric) - Delete the schema of a single metric for a given dataset.
* [get_model](docs/sdks/models/README.md#get_model) - Get a model metadata
* [update_model](docs/sdks/models/README.md#update_model) - Update a model's metadata
* [deactivate_model](docs/sdks/models/README.md#deactivate_model) - Mark a model as inactive

### [monitor](docs/sdks/monitor/README.md)

* [list_constraints](docs/sdks/monitor/README.md#list_constraints) - List the constraints for a given dataset.
* [get_analyzer](docs/sdks/monitor/README.md#get_analyzer) - Get the analyzer config for a given dataset.
* [put_analyzer](docs/sdks/monitor/README.md#put_analyzer) - Save the analyzer config for a given dataset.
* [delete_analyzer](docs/sdks/monitor/README.md#delete_analyzer) - Delete the analyzer config for a given dataset.
* [get_monitor](docs/sdks/monitor/README.md#get_monitor) - Get the monitor config for a given dataset.
* [put_monitor](docs/sdks/monitor/README.md#put_monitor) - Save the monitor for a given dataset.
* [delete_monitor](docs/sdks/monitor/README.md#delete_monitor) - Delete the monitor for a given dataset.
* [get_monitor_config_v3](docs/sdks/monitor/README.md#get_monitor_config_v3) - Get the monitor config document for a given dataset.
* [put_monitor_config_v3](docs/sdks/monitor/README.md#put_monitor_config_v3) - Save the monitor config document for a given dataset.
* [patch_monitor_config_v3](docs/sdks/monitor/README.md#patch_monitor_config_v3) - Patch an updated monitor config document for a given dataset.
* [validate_monitor_config_v3](docs/sdks/monitor/README.md#validate_monitor_config_v3) - Validate the monitor config document for a given dataset.
* [list_monitor_config_v3_versions](docs/sdks/monitor/README.md#list_monitor_config_v3_versions) - List the monitor config document versions for a given dataset.
* [get_monitor_config_v3_version](docs/sdks/monitor/README.md#get_monitor_config_v3_version) - Get the monitor config document version for a given dataset.
* [put_request_monitor_run_config](docs/sdks/monitor/README.md#put_request_monitor_run_config) - Put the RequestMonitorRun config into S3.

### [schema](docs/sdks/schema/README.md)

* [get_monitor_config_schema](docs/sdks/schema/README.md#get_monitor_config_schema) - Get the current supported schema of the monitor configuration

### [payment](docs/sdks/payment/README.md)

* [stripe_payment_endpoint](docs/sdks/payment/README.md#stripe_payment_endpoint) - Endpoint for Stripe payment webhooks

### [provision](docs/sdks/provision/README.md)

* [provision_aws_marketplace_new_user](docs/sdks/provision/README.md#provision_aws_marketplace_new_user) - Create resources for a new user coming from AWS Marketplace
* [provision_new_user](docs/sdks/provision/README.md#provision_new_user) - Create the resources that a new user needs to use WhyLabs via the website.

### [search](docs/sdks/search/README.md)

* [why_labs_search](docs/sdks/search/README.md#why_labs_search) - WhyLabs Search
* [why_labs_search_indexing](docs/sdks/search/README.md#why_labs_search_indexing) - WhyLabs Search Indexing

### [sessions](docs/sdks/sessions/README.md)

* [create_session](docs/sdks/sessions/README.md#create_session) - Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.
* [get_session_profile_observatory_link](docs/sdks/sessions/README.md#get_session_profile_observatory_link) - Get observatory links for profiles in a given session. A max of 3 profiles can be viewed a a time.
* [get_session](docs/sdks/sessions/README.md#get_session) - Get information about a session.
* [claim_guest_session](docs/sdks/sessions/README.md#claim_guest_session) - Claim a guest session, copying its model data into another org and expiring the session.
* [create_reference_profile_upload](docs/sdks/sessions/README.md#create_reference_profile_upload) - Create a reference profile upload for a given session.
* [batch_create_reference_profile_upload](docs/sdks/sessions/README.md#batch_create_reference_profile_upload) - Create multiple reference profile uploads for a given session.
* [create_dataset_profile_upload](docs/sdks/sessions/README.md#create_dataset_profile_upload) - Create an upload for a given session.

### [subscription](docs/sdks/subscription/README.md)

* [get_organization_subscriptions](docs/sdks/subscription/README.md#get_organization_subscriptions) - Get organization subscription details

### [user](docs/sdks/user/README.md)

* [get_user_by_email](docs/sdks/user/README.md#get_user_by_email) - Get a user by their email.
* [update_user](docs/sdks/user/README.md#update_user) - Update a user.
* [create_user](docs/sdks/user/README.md#create_user) - Create a user.
* [get_user](docs/sdks/user/README.md#get_user) - Get a user by their id.

### [azure_marketplace](docs/sdks/azuremarketplace/README.md)

* [activate_azure_subscription](docs/sdks/azuremarketplace/README.md#activate_azure_subscription) - Endpoint to activate Azure Marketplace subscriptions
* [azure_marketplace_webhook](docs/sdks/azuremarketplace/README.md#azure_marketplace_webhook) - Endpoint for Azure Marketplace webhooks

### [traces](docs/sdks/traces/README.md)

* [export_traces_json](docs/sdks/traces/README.md#export_traces_json) - Export traces into WhyLabs
* [export_traces_raw](docs/sdks/traces/README.md#export_traces_raw) - Export traces into WhyLabs

### [transactions](docs/sdks/transactions/README.md)

* [transaction_status](docs/sdks/transactions/README.md#transaction_status) - Get the status of a log transaction
* [start_transaction](docs/sdks/transactions/README.md#start_transaction) - Start a log transaction
* [commit_transaction](docs/sdks/transactions/README.md#commit_transaction) - Commit a log transaction
* [log_transaction](docs/sdks/transactions/README.md#log_transaction) - Add to a log transaction
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

### Example

```python
import whylabs_client
from whylabs_client.models import errors, operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = None
try:
    res = s.account.get_account_memberships(org_id='org-123', user_id='user-123', managed_org_id='org-123', role=operations.Role.VIEWER)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.get_account_memberships_response is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.whylabsapp.com` | None |

#### Example

```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    server_idx=0,
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.account.get_account_memberships(org_id='org-123', user_id='user-123', managed_org_id='org-123', role=operations.Role.VIEWER)

if res.get_account_memberships_response is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    server_url="https://api.whylabsapp.com",
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.account.get_account_memberships(org_id='org-123', user_id='user-123', managed_org_id='org-123', role=operations.Role.VIEWER)

if res.get_account_memberships_response is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import whylabs_client
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = whylabs_client.WhylabsClient(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name           | Type           | Scheme         |
| -------------- | -------------- | -------------- |
| `api_key_auth` | apiKey         | API key        |

To authenticate with the API the `api_key_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.account.get_account_memberships(org_id='org-123', user_id='user-123', managed_org_id='org-123', role=operations.Role.VIEWER)

if res.get_account_memberships_response is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
