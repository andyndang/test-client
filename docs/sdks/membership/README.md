# Membership
(*membership*)

## Overview

Endpoint for organization user membership

### Available Operations

* [update_membership_by_email](#update_membership_by_email) - Updates the role in an membership
* [create_membership](#create_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [remove_membership_by_email](#remove_membership_by_email) - Removes membership in a given org from a user, using the user's email address.
* [get_default_membership_for_email](#get_default_membership_for_email) - Get the default membership for a user.
* [set_default_membership](#set_default_membership) - Sets the organization that should be used when logging a user in
* [get_memberships_by_org](#get_memberships_by_org) - Get memberships for an org.
* [get_memberships_by_email](#get_memberships_by_email) - Get memberships for a user given that user's email address.
* [get_memberships](#get_memberships) - Get memberships for a user.
* [list_organization_memberships](#list_organization_memberships) - List organization memberships
* [update_organization_membership](#update_organization_membership) - Updates the role in an membership
* [create_organization_membership](#create_organization_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [remove_organization_membership](#remove_organization_membership) - Removes membership in a given org from a user, using the user's email address.

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

res = s.membership.update_membership_by_email(req)

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

res = s.membership.create_membership(req)

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

res = s.membership.remove_membership_by_email(req)

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


res = s.membership.get_default_membership_for_email(email='<value>')

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

res = s.membership.set_default_membership(req)

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


res = s.membership.get_memberships_by_org(org_id='<value>')

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


res = s.membership.get_memberships_by_email(email='<value>')

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


res = s.membership.get_memberships(user_id='<value>')

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

## list_organization_memberships

list memberships for an organization

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.membership.list_organization_memberships(org_id='org-123')

if res.list_organization_memberships_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |


### Response

**[operations.ListOrganizationMembershipsResponse](../../models/operations/listorganizationmembershipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_organization_membership

Updates the role in an membership, given the organization and the user's email address.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.membership.update_organization_membership(org_id='org-123', email='user@whylabs.ai', role=components.Role.MEMBER)

if res.membership_metadata is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `org_id`                                           | *str*                                              | :heavy_check_mark:                                 | N/A                                                | org-123                                            |
| `email`                                            | *str*                                              | :heavy_check_mark:                                 | N/A                                                | user@whylabs.ai                                    |
| `role`                                             | [components.Role](../../models/components/role.md) | :heavy_check_mark:                                 | N/A                                                | admin                                              |


### Response

**[operations.UpdateOrganizationMembershipResponse](../../models/operations/updateorganizationmembershipresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_organization_membership

Create a membership for a user, making them apart of an organization. Uses the user's current email address.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.membership.create_organization_membership(org_id='org-123', email='user@whylabs.ai', role=components.Role.MEMBER, set_default=False)

if res.membership_metadata is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `org_id`                                           | *str*                                              | :heavy_check_mark:                                 | N/A                                                | org-123                                            |
| `email`                                            | *str*                                              | :heavy_check_mark:                                 | N/A                                                | user@whylabs.ai                                    |
| `role`                                             | [components.Role](../../models/components/role.md) | :heavy_check_mark:                                 | N/A                                                | admin                                              |
| `set_default`                                      | *Optional[bool]*                                   | :heavy_minus_sign:                                 | N/A                                                |                                                    |


### Response

**[operations.CreateOrganizationMembershipResponse](../../models/operations/createorganizationmembershipresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_organization_membership

Removes membership in a given org from a user, using the user's email address.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.membership.remove_organization_membership(org_id='org-123', email='user@whylabs.ai')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `email`            | *str*              | :heavy_check_mark: | N/A                | user@whylabs.ai    |


### Response

**[operations.RemoveOrganizationMembershipResponse](../../models/operations/removeorganizationmembershipresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
