# APIKey
(*api_key*)

## Overview

API key management.

### Available Operations

* [list_api_keys](#list_api_keys) - List API key metadata for a given organization and user
* [create_api_key](#create_api_key) - Generate an API key for a user.
* [revoke_api_key](#revoke_api_key) - Revoke the given API Key, removing its ability to access WhyLabs systems
* [get_api_key](#get_api_key) - Get an api key by its id

## list_api_keys

Returns the API key metadata for a given organization and user

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.api_key.list_api_keys(org_id='org-123', user_id='user-123')

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

## create_api_key

Generates an API key for a given user. Must be called either by system administrator or by the user themselves

### Example Usage

```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.CreateAPIKeyRequest(
    org_id='org-123',
    user_id='user-123',
    expiration_time=1577836800000,
    alias='MLApplicationName',
)

res = s.api_key.create_api_key(req)

if res.user_api_key is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreateAPIKeyRequest](../../models/operations/createapikeyrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateAPIKeyResponse](../../models/operations/createapikeyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## revoke_api_key

Revokes the given API Key

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.api_key.revoke_api_key(org_id='org-123', user_id='user-123', key_id='HMiFAgQeNb')

if res.user_api_key is not None:
    # handle response
    pass

```

### Parameters

| Parameter               | Type                    | Required                | Description             | Example                 |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `org_id`                | *str*                   | :heavy_check_mark:      | N/A                     | org-123                 |
| `user_id`               | *str*                   | :heavy_check_mark:      | N/A                     | user-123                |
| `key_id`                | *str*                   | :heavy_check_mark:      | ID of the key to revoke | HMiFAgQeNb              |


### Response

**[operations.RevokeAPIKeyResponse](../../models/operations/revokeapikeyresponse.md)**
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


res = s.api_key.get_api_key(org_id='org-123', key_id='fh4dUNV3WQ')

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
