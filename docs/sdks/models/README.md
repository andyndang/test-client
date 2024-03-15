# Models
(*models*)

## Overview

Interactions related to models.

### Available Operations

* [list_models](#list_models) - Get a list of all of the model ids for an organization.
* [create_model](#create_model) - Create a model with a given name and a time period
* [get_entity_schema](#get_entity_schema) - Get the entity schema config for a given dataset.
* [put_entity_schema](#put_entity_schema) - Save the entity schema config for a given dataset.
* [delete_entity_schema](#delete_entity_schema) - Delete the entity schema config for a given dataset.
* [get_entity_schema_column](#get_entity_schema_column) - Get the entity schema of a single column for a given dataset.
* [put_entity_schema_column](#put_entity_schema_column) - Save the entity schema of a single column for a given dataset.
* [delete_entity_schema_column](#delete_entity_schema_column) - Delete the entity schema of a single column for a given dataset.
* [put_entity_schema_metric](#put_entity_schema_metric) - Save the schema of a single metric for a given dataset.
* [delete_entity_schema_metric](#delete_entity_schema_metric) - Delete the schema of a single metric for a given dataset.
* [get_model](#get_model) - Get a model metadata
* [update_model](#update_model) - Update a model's metadata
* [deactivate_model](#deactivate_model) - Mark a model as inactive

## list_models

Get a list of all of the model ids for an organization.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.models.list_models(org_id='org-123')

if res.list_models_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                             | Type                                  | Required                              | Description                           | Example                               |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `org_id`                              | *str*                                 | :heavy_check_mark:                    | Your company's unique organization ID | org-123                               |


### Response

**[operations.ListModelsResponse](../../models/operations/listmodelsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_model

Create a model

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components, operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.CreateModelRequest(
    org_id='org-123',
    model_name='Credit-Score-1',
    time_period=components.TimePeriod.P1_D,
    model_id='model-123',
)

res = s.models.create_model(req)

if res.model_metadata_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CreateModelRequest](../../models/operations/createmodelrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateModelResponse](../../models/operations/createmodelresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_entity_schema

Get the entity schema config for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.models.get_entity_schema(org_id='org-123', dataset_id='model-123')

if res.entity_schema is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |


### Response

**[operations.GetEntitySchemaResponse](../../models/operations/getentityschemaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_entity_schema

Save the entity schema config for a given dataset.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.models.put_entity_schema(org_id='org-123', dataset_id='model-123', entity_schema=components.EntitySchema(
    columns={
        'key': components.ColumnSchema(
            classifier='input',
            data_type='fractional',
            discreteness='discrete',
        ),
    },
))

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `org_id`                                                           | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                | org-123                                                            |
| `dataset_id`                                                       | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                | model-123                                                          |
| `entity_schema`                                                    | [components.EntitySchema](../../models/components/entityschema.md) | :heavy_check_mark:                                                 | N/A                                                                |                                                                    |


### Response

**[operations.PutEntitySchemaResponse](../../models/operations/putentityschemaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_entity_schema

Delete the entity schema config for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.models.delete_entity_schema(org_id='org-123', dataset_id='model-123')

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

**[operations.DeleteEntitySchemaResponse](../../models/operations/deleteentityschemaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_entity_schema_column

Get the entity schema of a single column for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.models.get_entity_schema_column(org_id='org-123', dataset_id='model-123', column_id='feature-123')

if res.column_schema is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |
| `column_id`        | *str*              | :heavy_check_mark: | N/A                | feature-123        |


### Response

**[operations.GetEntitySchemaColumnResponse](../../models/operations/getentityschemacolumnresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_entity_schema_column

Save the entity schema of a single column for a given dataset.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.models.put_entity_schema_column(org_id='org-123', dataset_id='model-123', column_id='feature-123', column_schema=components.ColumnSchema(
    classifier='input',
    data_type='fractional',
    discreteness='discrete',
))

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `org_id`                                                           | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                | org-123                                                            |
| `dataset_id`                                                       | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                | model-123                                                          |
| `column_id`                                                        | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                | feature-123                                                        |
| `column_schema`                                                    | [components.ColumnSchema](../../models/components/columnschema.md) | :heavy_check_mark:                                                 | N/A                                                                |                                                                    |


### Response

**[operations.PutEntitySchemaColumnResponse](../../models/operations/putentityschemacolumnresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_entity_schema_column

Delete the entity schema of a single column for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.models.delete_entity_schema_column(org_id='org-123', dataset_id='model-123', column_id='feature-123')

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |
| `column_id`        | *str*              | :heavy_check_mark: | N/A                | feature-123        |


### Response

**[operations.DeleteEntitySchemaColumnResponse](../../models/operations/deleteentityschemacolumnresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_entity_schema_metric

Save the schema of a single metric for a given dataset.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.models.put_entity_schema_metric(org_id='org-123', dataset_id='model-123', metric_schema=components.MetricSchema(
    label='estimated_prediction.median',
    column='estimated_prediction',
    default_metric='median',
))

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `org_id`                                                           | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                | org-123                                                            |
| `dataset_id`                                                       | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                | model-123                                                          |
| `metric_schema`                                                    | [components.MetricSchema](../../models/components/metricschema.md) | :heavy_check_mark:                                                 | N/A                                                                |                                                                    |


### Response

**[operations.PutEntitySchemaMetricResponse](../../models/operations/putentityschemametricresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_entity_schema_metric

Delete the schema of a single metric for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.models.delete_entity_schema_metric(org_id='org-123', dataset_id='model-123', metric_label='feature-123')

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |
| `metric_label`     | *str*              | :heavy_check_mark: | N/A                | feature-123        |


### Response

**[operations.DeleteEntitySchemaMetricResponse](../../models/operations/deleteentityschemametricresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_model

Returns various metadata about a model

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.models.get_model(org_id='org-123', model_id='model-123')

if res.model_metadata_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                   | Type                        | Required                    | Description                 | Example                     |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `org_id`                    | *str*                       | :heavy_check_mark:          | The name of an organization | org-123                     |
| `model_id`                  | *str*                       | :heavy_check_mark:          | The ID of a model           | model-123                   |


### Response

**[operations.GetModelResponse](../../models/operations/getmodelresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_model

Update a model's metadata

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components, operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.UpdateModelRequest(
    org_id='org-123',
    model_id='model-123',
    model_name='Credit-Score-1',
    time_period=components.TimePeriod.P1_D,
)

res = s.models.update_model(req)

if res.model_metadata_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.UpdateModelRequest](../../models/operations/updatemodelrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.UpdateModelResponse](../../models/operations/updatemodelresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## deactivate_model

Mark a model as inactive

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.models.deactivate_model(org_id='org-123', model_id='model-123')

if res.model_metadata_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter           | Type                | Required            | Description         | Example             |
| ------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| `org_id`            | *str*               | :heavy_check_mark:  | The organization ID | org-123             |
| `model_id`          | *str*               | :heavy_check_mark:  | The model ID        | model-123           |


### Response

**[operations.DeactivateModelResponse](../../models/operations/deactivatemodelresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
