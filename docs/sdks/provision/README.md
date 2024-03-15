# Provision
(*provision*)

## Overview

Endpoint for creating sets of resources.

### Available Operations

* [provision_aws_marketplace_new_user](#provision_aws_marketplace_new_user) - Create resources for a new user coming from AWS Marketplace
* [provision_new_user](#provision_new_user) - Create the resources that a new user needs to use WhyLabs via the website.

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

res = s.provision.provision_aws_marketplace_new_user(req)

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

res = s.provision.provision_new_user(req)

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
