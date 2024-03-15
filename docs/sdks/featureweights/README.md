# FeatureWeights
(*feature_weights*)

## Overview

Endpoint for feature weights

### Available Operations

* [get_column_weights](#get_column_weights) - Get column weights for the specified dataset
* [put_column_weights](#put_column_weights) - Put column weights for the specified dataset

## get_column_weights

Get column weights for the specified dataset

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.feature_weights.get_column_weights(org_id='org-123', dataset_id='model-123')

if res.entity_weight_record is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |


### Response

**[operations.GetColumnWeightsResponse](../../models/operations/getcolumnweightsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_column_weights

Put column weights for the specified dataset

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.feature_weights.put_column_weights(org_id='org-123', dataset_id='model-123', request_body='<value>')

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |                    |


### Response

**[operations.PutColumnWeightsResponse](../../models/operations/putcolumnweightsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
