# Payment
(*payment*)

## Overview

Endpoint for payment webhooks

### Available Operations

* [stripe_payment_endpoint](#stripe_payment_endpoint) - Endpoint for Stripe payment webhooks

## stripe_payment_endpoint

Endpoint for Stripe payment webhooks

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = '<value>'

res = s.payment.stripe_payment_endpoint(req)

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
