# Admin
(*admin*)

## Overview

Endpoint for admin operations

### Available Operations

* [add_account_users_from_memberships](#add_account_users_from_memberships) - Adds account users for a managed organization and its child organizations based on existing memberships
* [delete_cache_key](#delete_cache_key) - Delete cache key
* [list_cache_keys](#list_cache_keys) - List cache keys
* [generate_report](#generate_report) - Generate an admin report
* [activate_marketplace_subscription_internal](#activate_marketplace_subscription_internal) - Activate Azure Marketplace subscription to an existing organization.
* [list_azure_marketplace_subscriptions](#list_azure_marketplace_subscriptions) - List Azure Marketplace subscriptions
* [post_monitor_config_validation_job](#post_monitor_config_validation_job) - Create a monitor config validation job for all configs

## add_account_users_from_memberships

Adds account users for a managed organization its child organizations based on existing memberships

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.add_account_users_from_memberships(org_id='<value>')

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


res = s.admin.delete_cache_key(key='<value>')

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


res = s.admin.list_cache_keys(cache_key_type=components.CacheKeyType.API_KEY_LAST_USED, pattern='<value>')

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


res = s.admin.generate_report(report_type=components.AdminReportType.SESSIONS)

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


res = s.admin.activate_marketplace_subscription_internal(org_id='<value>', subscription_id='<value>')

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


res = s.admin.list_azure_marketplace_subscriptions()

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


res = s.admin.post_monitor_config_validation_job()

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
