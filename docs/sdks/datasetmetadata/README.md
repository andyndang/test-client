# DatasetMetadata
(*dataset_metadata*)

## Overview

Endpoint for dataset metadata.

### Available Operations

* [get_dataset_metadata](#get_dataset_metadata) - Get dataset metadata for the specified dataset
* [put_dataset_metadata](#put_dataset_metadata) - Put dataset metadata for the specified dataset
* [delete_dataset_metadata](#delete_dataset_metadata) - Delete dataset metadata for the specified dataset

## get_dataset_metadata

Get dataset metadata for the specified dataset

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataset_metadata.get_dataset_metadata(org_id='org-123', dataset_id='model-123')

if res.get_dataset_metadata_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |


### Response

**[operations.GetDatasetMetadataResponse](../../models/operations/getdatasetmetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_dataset_metadata

Put dataset metadata for the specified dataset

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataset_metadata.put_dataset_metadata(org_id='org-123', dataset_id='model-123', request_body='<value>')

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

**[operations.PutDatasetMetadataResponse](../../models/operations/putdatasetmetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_dataset_metadata

Delete dataset metadata for the specified dataset

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataset_metadata.delete_dataset_metadata(org_id='org-123', dataset_id='model-123')

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |


### Response

**[operations.DeleteDatasetMetadataResponse](../../models/operations/deletedatasetmetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
