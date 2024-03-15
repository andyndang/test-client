# Account
(*account*)

## Overview

Endpoint for account provisioning

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

## get_account_memberships

Get memberships in the account organization and any managed organizations

### Example Usage

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


res = s.account.put_organization_memberships(org_id='org-123', managed_org_id='org-123', role=components.Role.VIEWER, put_account_memberships_request=components.PutAccountMembershipsRequest(
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


res = s.account.patch_organization_memberships(org_id='org-123', managed_org_id='org-123', role=components.Role.VIEWER, patch_account_memberships_request=components.PatchAccountMembershipsRequest(
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


res = s.account.list_managed_organizations(org_id='org-123')

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


res = s.account.update_account_user(org_id='org-123', user_id='user-123', update_account_user_request=components.UpdateAccountUserRequest())

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


res = s.account.create_account_user(org_id='org-123', create_account_user_request=components.CreateAccountUserRequest(
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


res = s.account.get_account_user_by_email(org_id='org-123', email='user@whylabs.ai')

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


res = s.account.get_account_user_by_id(org_id='org-123', user_id='user-123')

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


res = s.account.delete_account_user(org_id='org-123', user_id='user-123')

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


res = s.account.list_account_users(org_id='org-123')

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
