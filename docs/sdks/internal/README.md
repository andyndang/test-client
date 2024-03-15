# Internal
(*internal*)

## Overview

Internal API

### Available Operations

* [get_account_memberships](#get_account_memberships) - Get memberships in an account
* [put_organization_memberships](#put_organization_memberships) - Replace the memberships in a specific role and managed organization
* [patch_organization_memberships](#patch_organization_memberships) - Add or delete memberships in a specific role and managed organization
* [list_managed_organizations](#list_managed_organizations) - List managed organizations for a parent organization
* [update_account_user](#update_account_user) - Update account user
* [create_account_user](#create_account_user) - Create an account user
* [get_account_user_by_email](#get_account_user_by_email) - Get account user by email
* [get_account_user_by_id](#get_account_user_by_id) - Get account user by user_id
* [delete_account_user](#delete_account_user) - Delete account user
* [list_account_users](#list_account_users) - List users in an account
* [add_account_users_from_memberships](#add_account_users_from_memberships) - Adds account users for a managed organization and its child organizations based on existing memberships
* [delete_cache_key](#delete_cache_key) - Delete cache key
* [list_cache_keys](#list_cache_keys) - List cache keys
* [generate_report](#generate_report) - Generate an admin report
* [activate_marketplace_subscription_internal](#activate_marketplace_subscription_internal) - Activate Azure Marketplace subscription to an existing organization.
* [list_azure_marketplace_subscriptions](#list_azure_marketplace_subscriptions) - List Azure Marketplace subscriptions
* [post_monitor_config_validation_job](#post_monitor_config_validation_job) - Create a monitor config validation job for all configs
* [get_feature_flags](#get_feature_flags) - Get feature flags for the specified user/org
* [update_membership_by_email](#update_membership_by_email) - Updates the role in an membership
* [create_membership](#create_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [remove_membership_by_email](#remove_membership_by_email) - Removes membership in a given org from a user, using the user's email address.
* [get_default_membership_for_email](#get_default_membership_for_email) - Get the default membership for a user.
* [set_default_membership](#set_default_membership) - Sets the organization that should be used when logging a user in
* [get_memberships_by_org](#get_memberships_by_org) - Get memberships for an org.
* [get_memberships_by_email](#get_memberships_by_email) - Get memberships for a user given that user's email address.
* [get_memberships](#get_memberships) - Get memberships for a user.
* [get_notification_settings](#get_notification_settings) - Get notification settings for an org
* [update_notification_settings](#update_notification_settings) - Update notification settings for an org
* [list_organizations](#list_organizations) - Get a list of all of the organization ids.
* [~~update_org~~](#update_org) - Update an existing organization :warning: **Deprecated**
* [create_organization](#create_organization) - Create an organization
* [partially_update_organization](#partially_update_organization) - Update some fields of an organization to non-null values
* [get_organization](#get_organization) - Get the metadata about an organization.
* [update_organization](#update_organization) - Update an existing organization
* [delete_organization](#delete_organization) - Delete an org
* [list_api_keys](#list_api_keys) - List API key metadata for a given organization and user
* [get_api_key](#get_api_key) - Get an api key by its id
* [hide_segments](#hide_segments) - Hides a list of segments
* [get_aws_marketplace_metadata](#get_aws_marketplace_metadata) - Get marketplace metadata for an org if any exists.
* [list_monitor_config_v3_versions](#list_monitor_config_v3_versions) - List the monitor config document versions for a given dataset.
* [get_monitor_config_v3_version](#get_monitor_config_v3_version) - Get the monitor config document version for a given dataset.
* [put_request_monitor_run_config](#put_request_monitor_run_config) - Put the RequestMonitorRun config into S3.
* [stripe_payment_endpoint](#stripe_payment_endpoint) - Endpoint for Stripe payment webhooks
* [provision_aws_marketplace_new_user](#provision_aws_marketplace_new_user) - Create resources for a new user coming from AWS Marketplace
* [provision_new_user](#provision_new_user) - Create the resources that a new user needs to use WhyLabs via the website.
* [why_labs_search](#why_labs_search) - WhyLabs Search
* [why_labs_search_indexing](#why_labs_search_indexing) - WhyLabs Search Indexing
* [get_organization_subscriptions](#get_organization_subscriptions) - Get organization subscription details
* [get_user_by_email](#get_user_by_email) - Get a user by their email.
* [update_user](#update_user) - Update a user.
* [create_user](#create_user) - Create a user.
* [get_user](#get_user) - Get a user by their id.
* [activate_azure_subscription](#activate_azure_subscription) - Endpoint to activate Azure Marketplace subscriptions
* [azure_marketplace_webhook](#azure_marketplace_webhook) - Endpoint for Azure Marketplace webhooks

## get_account_memberships

Get memberships in the account organization and any managed organizations

### Example Usage

```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_account_memberships(org_id='org-123', user_id='user-123', managed_org_id='org-123', role=operations.Role.VIEWER)

if res.get_account_memberships_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `org_id`                                                     | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          | org-123                                                      |
| `user_id`                                                    | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          | user-123                                                     |
| `managed_org_id`                                             | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          | org-123                                                      |
| `role`                                                       | [Optional[operations.Role]](../../models/operations/role.md) | :heavy_minus_sign:                                           | N/A                                                          | admin                                                        |


### Response

**[operations.GetAccountMembershipsResponse](../../models/operations/getaccountmembershipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_organization_memberships

Replace all of the memberships in a specific role and managed organization

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.put_organization_memberships(org_id='org-123', managed_org_id='org-123', role=components.Role.VIEWER, put_account_memberships_request=components.PutAccountMembershipsRequest(
    user_ids=[
        '<value>',
    ],
))

if res.status_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        | Example                                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `org_id`                                                                                           | *str*                                                                                              | :heavy_check_mark:                                                                                 | N/A                                                                                                | org-123                                                                                            |
| `managed_org_id`                                                                                   | *str*                                                                                              | :heavy_check_mark:                                                                                 | N/A                                                                                                | org-123                                                                                            |
| `role`                                                                                             | [components.Role](../../models/components/role.md)                                                 | :heavy_check_mark:                                                                                 | N/A                                                                                                | admin                                                                                              |
| `put_account_memberships_request`                                                                  | [components.PutAccountMembershipsRequest](../../models/components/putaccountmembershipsrequest.md) | :heavy_check_mark:                                                                                 | N/A                                                                                                |                                                                                                    |


### Response

**[operations.PutOrganizationMembershipsResponse](../../models/operations/putorganizationmembershipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_organization_memberships

Add or delete all of the memberships in a specific role and managed organization

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.patch_organization_memberships(org_id='org-123', managed_org_id='org-123', role=components.Role.VIEWER, patch_account_memberships_request=components.PatchAccountMembershipsRequest(
    user_ids_to_add=[
        '<value>',
    ],
    user_ids_to_delete=[
        '<value>',
    ],
))

if res.status_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            | Example                                                                                                |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `org_id`                                                                                               | *str*                                                                                                  | :heavy_check_mark:                                                                                     | N/A                                                                                                    | org-123                                                                                                |
| `managed_org_id`                                                                                       | *str*                                                                                                  | :heavy_check_mark:                                                                                     | N/A                                                                                                    | org-123                                                                                                |
| `role`                                                                                                 | [components.Role](../../models/components/role.md)                                                     | :heavy_check_mark:                                                                                     | N/A                                                                                                    | admin                                                                                                  |
| `patch_account_memberships_request`                                                                    | [components.PatchAccountMembershipsRequest](../../models/components/patchaccountmembershipsrequest.md) | :heavy_check_mark:                                                                                     | N/A                                                                                                    |                                                                                                        |


### Response

**[operations.PatchOrganizationMembershipsResponse](../../models/operations/patchorganizationmembershipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_managed_organizations

List managed organizations for a parent organization

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.list_managed_organizations(org_id='org-123')

if res.account_organizations is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |


### Response

**[operations.ListManagedOrganizationsResponse](../../models/operations/listmanagedorganizationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_account_user

Update an account user's details

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.update_account_user(org_id='org-123', user_id='user-123', update_account_user_request=components.UpdateAccountUserRequest())

if res.account_user is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `org_id`                                                                                   | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        | org-123                                                                                    |
| `user_id`                                                                                  | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        | user-123                                                                                   |
| `update_account_user_request`                                                              | [components.UpdateAccountUserRequest](../../models/components/updateaccountuserrequest.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |                                                                                            |


### Response

**[operations.UpdateAccountUserResponse](../../models/operations/updateaccountuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_account_user

Create an account user

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.create_account_user(org_id='org-123', create_account_user_request=components.CreateAccountUserRequest(
    email='Jason_Skiles63@yahoo.com',
))

if res.account_user is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `org_id`                                                                                   | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        | org-123                                                                                    |
| `create_account_user_request`                                                              | [components.CreateAccountUserRequest](../../models/components/createaccountuserrequest.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |                                                                                            |


### Response

**[operations.CreateAccountUserResponse](../../models/operations/createaccountuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_account_user_by_email

Get account user by email

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_account_user_by_email(org_id='org-123', email='user@whylabs.ai')

if res.account_user is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `email`            | *str*              | :heavy_check_mark: | N/A                | user@whylabs.ai    |


### Response

**[operations.GetAccountUserByEmailResponse](../../models/operations/getaccountuserbyemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_account_user_by_id

Get account user by user_id

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_account_user_by_id(org_id='org-123', user_id='user-123')

if res.account_user is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                | user-123           |


### Response

**[operations.GetAccountUserByIDResponse](../../models/operations/getaccountuserbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_account_user

Delete an account user's details

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.delete_account_user(org_id='org-123', user_id='user-123')

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                | user-123           |


### Response

**[operations.DeleteAccountUserResponse](../../models/operations/deleteaccountuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_account_users

List users in the account organization and any managed organizations

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.list_account_users(org_id='org-123')

if res.account_users is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |


### Response

**[operations.ListAccountUsersResponse](../../models/operations/listaccountusersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## add_account_users_from_memberships

Adds account users for a managed organization its child organizations based on existing memberships

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.add_account_users_from_memberships(org_id='<value>')

if res.strings is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.AddAccountUsersFromMembershipsResponse](../../models/operations/addaccountusersfrommembershipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_cache_key

Delete cache key

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.delete_cache_key(key='<value>')

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `key`              | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteCacheKeyResponse](../../models/operations/deletecachekeyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_cache_keys

List cache keys

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.list_cache_keys(cache_key_type=components.CacheKeyType.API_KEY_LAST_USED, pattern='<value>')

if res.strings is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `cache_key_type`                                                   | [components.CacheKeyType](../../models/components/cachekeytype.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `pattern`                                                          | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |


### Response

**[operations.ListCacheKeysResponse](../../models/operations/listcachekeysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## generate_report

Generate an admin report

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.generate_report(report_type=components.AdminReportType.SESSIONS)

if res.admin_report_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `report_type`                                                            | [components.AdminReportType](../../models/components/adminreporttype.md) | :heavy_check_mark:                                                       | A type of admin report.                                                  |


### Response

**[operations.GenerateReportResponse](../../models/operations/generatereportresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## activate_marketplace_subscription_internal

Activate Azure Marketplace subscription to an existing organization.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.activate_marketplace_subscription_internal(org_id='<value>', subscription_id='<value>')

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                |
| `subscription_id`  | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.ActivateMarketplaceSubscriptionInternalResponse](../../models/operations/activatemarketplacesubscriptioninternalresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_azure_marketplace_subscriptions

List Azure Marketplace subscriptions

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.list_azure_marketplace_subscriptions()

if res.azure_marketplace_subscription_details is not None:
    # handle response
    pass

```


### Response

**[operations.ListAzureMarketplaceSubscriptionsResponse](../../models/operations/listazuremarketplacesubscriptionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_monitor_config_validation_job

Create a monitor config validation job for all configs

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.post_monitor_config_validation_job()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.PostMonitorConfigValidationJobResponse](../../models/operations/postmonitorconfigvalidationjobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_feature_flags

Get feature flags for the specified user/org

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_feature_flags(user_id='<value>', org_id='<value>')

if res.feature_flags is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetFeatureFlagsResponse](../../models/operations/getfeatureflagsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_membership_by_email

Updates the role in an membership, given the organization and the user's email address.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = components.UpdateMembershipRequest(
    org_id='<value>',
    email='Minnie42@hotmail.com',
    role=components.Role.VIEWER,
)

res = s.internal.update_membership_by_email(req)

if res.membership_metadata is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.UpdateMembershipRequest](../../models/components/updatemembershiprequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.UpdateMembershipByEmailResponse](../../models/operations/updatemembershipbyemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_membership

Create a membership for a user, making them apart of an organization. Uses the user's current email address.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = components.AddMembershipRequest(
    org_id='<value>',
    email='Willie1@gmail.com',
    role=components.Role.ADMIN,
)

res = s.internal.create_membership(req)

if res.membership_metadata is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.AddMembershipRequest](../../models/components/addmembershiprequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateMembershipResponse](../../models/operations/createmembershipresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_membership_by_email

Removes membership in a given org from a user, using the user's email address.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = components.RemoveMembershipRequest(
    org_id='<value>',
    email='Shaun79@gmail.com',
)

res = s.internal.remove_membership_by_email(req)

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.RemoveMembershipRequest](../../models/components/removemembershiprequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.RemoveMembershipByEmailResponse](../../models/operations/removemembershipbyemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_default_membership_for_email

Get the default membership for a user.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_default_membership_for_email(email='<value>')

if res.get_default_membership_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `email`            | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetDefaultMembershipForEmailResponse](../../models/operations/getdefaultmembershipforemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## set_default_membership

Sets the organization that should be used when logging a user in

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = components.SetDefaultMembershipRequest(
    org_id='<value>',
    user_id='<value>',
)

res = s.internal.set_default_membership(req)

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.SetDefaultMembershipRequest](../../models/components/setdefaultmembershiprequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.SetDefaultMembershipResponse](../../models/operations/setdefaultmembershipresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_memberships_by_org

Get memberships for an org.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_memberships_by_org(org_id='<value>')

if res.get_memberships_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetMembershipsByOrgResponse](../../models/operations/getmembershipsbyorgresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_memberships_by_email

Get memberships for a user given that user's email address.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_memberships_by_email(email='<value>')

if res.get_memberships_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `email`            | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetMembershipsByEmailResponse](../../models/operations/getmembershipsbyemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_memberships

Get memberships for a user.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_memberships(user_id='<value>')

if res.get_memberships_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetMembershipsResponse](../../models/operations/getmembershipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_notification_settings

Get notification settings for an org

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_notification_settings(org_id='<value>')

if res.get_notification_settings_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetNotificationSettingsResponse](../../models/operations/getnotificationsettingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_notification_settings

Update notification settings for an org

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.update_notification_settings(org_id='<value>', notification_settings=components.NotificationSettings(
    email_settings=components.UberNotificationSchedule(
        enabled=False,
        cadence=components.NotificationSqsMessageCadence.HOURLY,
    ),
    slack_settings=components.UberNotificationSchedule(
        enabled=False,
        cadence=components.NotificationSqsMessageCadence.DAILY,
    ),
    pager_duty_settings=components.UberNotificationSchedule(
        enabled=False,
        cadence=components.NotificationSqsMessageCadence.INDIVIDUAL,
    ),
))

if res.notification_settings is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `org_id`                                                                           | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `notification_settings`                                                            | [components.NotificationSettings](../../models/components/notificationsettings.md) | :heavy_check_mark:                                                                 | N/A                                                                                |


### Response

**[operations.UpdateNotificationSettingsResponse](../../models/operations/updatenotificationsettingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_organizations

Get a list of all of the organization ids.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.list_organizations()

if res.list_organizations_response is not None:
    # handle response
    pass

```


### Response

**[operations.ListOrganizationsResponse](../../models/operations/listorganizationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## ~~update_org~~

Update all fields of an existing organization

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.UpdateOrgRequest(
    name='ACME, Inc',
    request_body=operations.UpdateOrgRequestBody(
        org_id='<value>',
    ),
    subscription_tier=operations.SubscriptionTier.FREE,
    email_domains='acme.ai,acme.com',
    observatory_url='https://hub.whylabsapp.com',
    parent_org_id='org-123',
)

res = s.internal.update_org(req)

if res.organization_summary is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.UpdateOrgRequest](../../models/operations/updateorgrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.UpdateOrgResponse](../../models/operations/updateorgresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_organization

Create an organization

### Example Usage

```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.CreateOrganizationRequest(
    name='ACME, Inc',
    subscription_tier=operations.QueryParamSubscriptionTier.FREE,
    email_domains='acme.ai,acme.com',
    override_id='org-123',
    observatory_url='https://hub.whylabsapp.com',
    parent_org_id='org-123',
)

res = s.internal.create_organization(req)

if res.organization_summary is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateOrganizationRequest](../../models/operations/createorganizationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateOrganizationResponse](../../models/operations/createorganizationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## partially_update_organization

Update some fields of an organization to non-null values, leaving all other existing values the same

### Example Usage

```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.PartiallyUpdateOrganizationRequest(
    org_id='<value>',
    name='ACME, Inc',
    subscription_tier=operations.PartiallyUpdateOrganizationQueryParamSubscriptionTier.FREE,
    email_domains='acme.ai,acme.com',
    observatory_url='https://hub.whylabsapp.com',
    parent_org_id='org-123',
)

res = s.internal.partially_update_organization(req)

if res.organization_summary is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PartiallyUpdateOrganizationRequest](../../models/operations/partiallyupdateorganizationrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PartiallyUpdateOrganizationResponse](../../models/operations/partiallyupdateorganizationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_organization

Returns various metadata about an organization

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_organization(org_id='<value>')

if res.organization_metadata is not None:
    # handle response
    pass

```

### Parameters

| Parameter                        | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `org_id`                         | *str*                            | :heavy_check_mark:               | The unique ID of an organization |


### Response

**[operations.GetOrganizationResponse](../../models/operations/getorganizationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_organization

Update all fields of an existing organization

### Example Usage

```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.UpdateOrganizationRequest(
    org_id='<value>',
    name='ACME, Inc',
    subscription_tier=operations.UpdateOrganizationQueryParamSubscriptionTier.FREE,
    email_domains='acme.ai,acme.com',
    observatory_url='https://hub.whylabsapp.com',
    parent_org_id='org-123',
)

res = s.internal.update_organization(req)

if res.organization_summary is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateOrganizationRequest](../../models/operations/updateorganizationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UpdateOrganizationResponse](../../models/operations/updateorganizationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_organization

Delete an org

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.delete_organization(org_id='<value>')

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteOrganizationResponse](../../models/operations/deleteorganizationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_api_keys

Returns the API key metadata for a given organization and user

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.list_api_keys(org_id='org-123', user_id='user-123')

if res.list_user_api_keys is not None:
    # handle response
    pass

```

### Parameters

| Parameter                              | Type                                   | Required                               | Description                            | Example                                |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `org_id`                               | *str*                                  | :heavy_check_mark:                     | Your company's unique organization ID  | org-123                                |
| `user_id`                              | *Optional[str]*                        | :heavy_minus_sign:                     | The unique user ID in an organization. | user-123                               |


### Response

**[operations.ListAPIKeysResponse](../../models/operations/listapikeysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_key

Get an api key by its id

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_api_key(org_id='org-123', key_id='fh4dUNV3WQ')

if res.user_api_key_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `key_id`           | *str*              | :heavy_check_mark: | N/A                | fh4dUNV3WQ         |


### Response

**[operations.GetAPIKeyResponse](../../models/operations/getapikeyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## hide_segments

Returns a list of segments that were hidden for a dataset.

        

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.hide_segments(org_id='org-123', dataset_id='model-123', segments_list_request=components.SegmentsListRequest(
    segments=[
        '<value>',
    ],
))

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `org_id`                                                                         | *str*                                                                            | :heavy_check_mark:                                                               | Your company's unique organization ID                                            | org-123                                                                          |
| `dataset_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | The unique dataset ID in your company.                                           | model-123                                                                        |
| `segments_list_request`                                                          | [components.SegmentsListRequest](../../models/components/segmentslistrequest.md) | :heavy_check_mark:                                                               | N/A                                                                              |                                                                                  |


### Response

**[operations.HideSegmentsResponse](../../models/operations/hidesegmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_aws_marketplace_metadata

Get marketplace metadata for an org if any exists.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_aws_marketplace_metadata(org_id='<value>')

if res.get_marketplace_metadata_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAWSMarketplaceMetadataResponse](../../models/operations/getawsmarketplacemetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_monitor_config_v3_versions

List the monitor config document versions for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.list_monitor_config_v3_versions(org_id='org-123', dataset_id='model-123')

if res.monitor_config_versions is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |


### Response

**[operations.ListMonitorConfigV3VersionsResponse](../../models/operations/listmonitorconfigv3versionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monitor_config_v3_version

Get the monitor config document version for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_monitor_config_v3_version(org_id='org-123', dataset_id='model-123', version_id='4920545486e2a4cdf0f770c09748e663')

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                        | Type                             | Required                         | Description                      | Example                          |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `org_id`                         | *str*                            | :heavy_check_mark:               | N/A                              | org-123                          |
| `dataset_id`                     | *str*                            | :heavy_check_mark:               | N/A                              | model-123                        |
| `version_id`                     | *str*                            | :heavy_check_mark:               | N/A                              | 4920545486e2a4cdf0f770c09748e663 |


### Response

**[operations.GetMonitorConfigV3VersionResponse](../../models/operations/getmonitorconfigv3versionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_request_monitor_run_config

Put the RequestMonitorRun config into S3.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.put_request_monitor_run_config(org_id='org-123', dataset_id='model-123', request_body=operations.PutRequestMonitorRunConfigRequestBody(
    analyzer_ids=[
        'd',
        'r',
        'i',
        'f',
        't',
        '-',
        'a',
        'n',
        'a',
        'l',
        'y',
        'z',
        'e',
        'r',
    ],
    start_timestamp=1577836800000,
    end_timestamp=1893456000000,
))

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          | Example                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `org_id`                                                                                                             | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  | org-123                                                                                                              |
| `dataset_id`                                                                                                         | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  | model-123                                                                                                            |
| `request_body`                                                                                                       | [operations.PutRequestMonitorRunConfigRequestBody](../../models/operations/putrequestmonitorrunconfigrequestbody.md) | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  |                                                                                                                      |


### Response

**[operations.PutRequestMonitorRunConfigResponse](../../models/operations/putrequestmonitorrunconfigresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## stripe_payment_endpoint

Endpoint for Stripe payment webhooks

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = '<value>'

res = s.internal.stripe_payment_endpoint(req)

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [str](../../models/.md)                    | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.StripePaymentEndpointResponse](../../models/operations/stripepaymentendpointresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## provision_aws_marketplace_new_user

Create resources for a new user coming from AWS Marketplace

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = components.ProvisionNewMarketplaceUserRequest(
    email='Karina72@yahoo.com',
    org_name='<value>',
    model_name='<value>',
    customer_id_token='<value>',
)

res = s.internal.provision_aws_marketplace_new_user(req)

if res.provision_new_aws_marketplace_user_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.ProvisionNewMarketplaceUserRequest](../../models/components/provisionnewmarketplaceuserrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.ProvisionAWSMarketplaceNewUserResponse](../../models/operations/provisionawsmarketplacenewuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## provision_new_user

Create the resources that a new user needs to use WhyLabs via the website.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = components.ProvisionNewUserRequest(
    email='Alec40@hotmail.com',
    org_name='<value>',
    model_name='<value>',
    subscription_tier=components.SubscriptionTier.FREE,
)

res = s.internal.provision_new_user(req)

if res.provision_new_user_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.ProvisionNewUserRequest](../../models/components/provisionnewuserrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ProvisionNewUserResponse](../../models/operations/provisionnewuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## why_labs_search

WhyLabs Search

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.why_labs_search(query='<value>')

if res.search_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `query`            | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.WhyLabsSearchResponse](../../models/operations/whylabssearchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## why_labs_search_indexing

WhyLabs Search Indexing

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = components.SearchIndexRequest(
    org_id='<value>',
    type=components.SearchIndexType.MODELS,
)

res = s.internal.why_labs_search_indexing(req)

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.SearchIndexRequest](../../models/components/searchindexrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.WhyLabsSearchIndexingResponse](../../models/operations/whylabssearchindexingresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_organization_subscriptions

Get organization subscription details

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_organization_subscriptions(org_id='<value>')

if res.subscription_summaries is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetOrganizationSubscriptionsResponse](../../models/operations/getorganizationsubscriptionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_user_by_email

Get a user by their email.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_user_by_email(email='<value>')

if res.user is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `email`            | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetUserByEmailResponse](../../models/operations/getuserbyemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_user

Update a user.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = components.User(
    user_id='<value>',
    email='Madison.Jacobi47@yahoo.com',
)

res = s.internal.update_user(req)

if res.user is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `request`                                          | [components.User](../../models/components/user.md) | :heavy_check_mark:                                 | The request object to use for the request.         |


### Response

**[operations.UpdateUserResponse](../../models/operations/updateuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_user

Create a user.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = components.CreateUserRequest(
    email='Richie.Kuhic95@yahoo.com',
)

res = s.internal.create_user(req)

if res.user is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.CreateUserRequest](../../models/components/createuserrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CreateUserResponse](../../models/operations/createuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_user

Get a user by their id.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.get_user(user_id='<value>')

if res.user is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetUserResponse](../../models/operations/getuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## activate_azure_subscription

Endpoint to activate Azure Marketplace subscriptions

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = components.ActivateAzureSubscriptionRequest(
    email='Travis_Cummings7@gmail.com',
    org_name='<value>',
    model_name='<value>',
    marketplace_token='<value>',
)

res = s.internal.activate_azure_subscription(req)

if res.activate_azure_subscription_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [components.ActivateAzureSubscriptionRequest](../../models/components/activateazuresubscriptionrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.ActivateAzureSubscriptionResponse](../../models/operations/activateazuresubscriptionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## azure_marketplace_webhook

Endpoint for Azure Marketplace webhooks

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = '<value>'

res = s.internal.azure_marketplace_webhook(req)

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [str](../../models/.md)                    | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.AzureMarketplaceWebhookResponse](../../models/operations/azuremarketplacewebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
