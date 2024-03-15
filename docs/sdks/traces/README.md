# Traces
(*traces*)

## Overview

Endpoint for ingesting spans and traces

### Available Operations

* [export_traces_json](#export_traces_json) - Export traces into WhyLabs
* [export_traces_raw](#export_traces_raw) - Export traces into WhyLabs

## export_traces_json

API to export traces into WhyLabs

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.traces.export_traces_json(request_body=[
    '<value>',
], x_whylabs_resource='resource-1')

if res.export_trace_service_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter            | Type                 | Required             | Description          | Example              |
| -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| `request_body`       | List[*str*]          | :heavy_check_mark:   | N/A                  |                      |
| `x_whylabs_resource` | *Optional[str]*      | :heavy_minus_sign:   | N/A                  | resource-1           |


### Response

**[operations.ExportTracesJSONResponse](../../models/operations/exporttracesjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## export_traces_raw

API to export traces into WhyLabs

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.traces.export_traces_raw(request_body='0x13AeB07844'.encode(), x_whylabs_resource='resource-1')

if res.export_trace_service_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter            | Type                 | Required             | Description          | Example              |
| -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| `request_body`       | *bytes*              | :heavy_check_mark:   | N/A                  |                      |
| `x_whylabs_resource` | *Optional[str]*      | :heavy_minus_sign:   | N/A                  | resource-1           |


### Response

**[operations.ExportTracesRawResponse](../../models/operations/exporttracesrawresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
