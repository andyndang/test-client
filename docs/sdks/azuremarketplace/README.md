# AzureMarketplace
(*azure_marketplace*)

## Overview

Endpoint for Azure Marketplace webhooks

### Available Operations

* [activate_azure_subscription](#activate_azure_subscription) - Endpoint to activate Azure Marketplace subscriptions
* [azure_marketplace_webhook](#azure_marketplace_webhook) - Endpoint for Azure Marketplace webhooks

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

res = s.azure_marketplace.activate_azure_subscription(req)

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

res = s.azure_marketplace.azure_marketplace_webhook(req)

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
