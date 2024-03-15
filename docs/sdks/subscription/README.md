# Subscription
(*subscription*)

## Overview

Endpoint for subscription operations

### Available Operations

* [get_organization_subscriptions](#get_organization_subscriptions) - Get organization subscription details

## get_organization_subscriptions

Get organization subscription details

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.subscription.get_organization_subscriptions(org_id='<value>')

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
