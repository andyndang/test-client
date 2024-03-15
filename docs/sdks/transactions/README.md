# Transactions
(*transactions*)

## Overview

Endpoint for log transactions

### Available Operations

* [transaction_status](#transaction_status) - Get the status of a log transaction
* [start_transaction](#start_transaction) - Start a log transaction
* [commit_transaction](#commit_transaction) - Commit a log transaction
* [log_transaction](#log_transaction) - Add to a log transaction

## transaction_status

API to get the status of a log transaction

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.transactions.transaction_status(transaction_id='28541e19-72c2-4c43-bbce-84e4de362101')

if res.transaction_status_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `transaction_id`                     | *str*                                | :heavy_check_mark:                   | N/A                                  | 28541e19-72c2-4c43-bbce-84e4de362101 |


### Response

**[operations.TransactionStatusResponse](../../models/operations/transactionstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## start_transaction

API to start a log transaction

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = components.TransactionStartRequest(
    dataset_id='<value>',
)

res = s.transactions.start_transaction(req)

if res.log_transaction_metadata is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.TransactionStartRequest](../../models/components/transactionstartrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.StartTransactionResponse](../../models/operations/starttransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## commit_transaction

API to commit a log transaction

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.transactions.commit_transaction(transaction_id='28541e19-72c2-4c43-bbce-84e4de362101', transaction_commit_request=components.TransactionCommitRequest())

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `transaction_id`                                                                           | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        | 28541e19-72c2-4c43-bbce-84e4de362101                                                       |
| `transaction_commit_request`                                                               | [components.TransactionCommitRequest](../../models/components/transactioncommitrequest.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |                                                                                            |


### Response

**[operations.CommitTransactionResponse](../../models/operations/committransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## log_transaction

API to add to a log transaction

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.transactions.log_transaction(transaction_id='28541e19-72c2-4c43-bbce-84e4de362101', transaction_log_request=components.TransactionLogRequest(
    dataset_timestamp=254316,
    segment_tags=[
        components.SegmentTag(
            key='<key>',
            value='<value>',
        ),
    ],
))

if res.async_log_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `transaction_id`                                                                     | *str*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  | 28541e19-72c2-4c43-bbce-84e4de362101                                                 |
| `transaction_log_request`                                                            | [components.TransactionLogRequest](../../models/components/transactionlogrequest.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |                                                                                      |


### Response

**[operations.LogTransactionResponse](../../models/operations/logtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
