# Schema
(*schema*)

## Overview

Schema management.

### Available Operations

* [get_monitor_config_schema](#get_monitor_config_schema) - Get the current supported schema of the monitor configuration

## get_monitor_config_schema

Get the current supported schema of the  monitor configuration

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.schema.get_monitor_config_schema(org_id='org-123')

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |


### Response

**[operations.GetMonitorConfigSchemaResponse](../../models/operations/getmonitorconfigschemaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
