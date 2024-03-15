# DebugEvents
(*debug_events*)

## Overview

Endpoint for debug events

### Available Operations

* [log_debug_event](#log_debug_event) - Log a debug event

## log_debug_event

Create a debug event.
        

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.debug_events.log_debug_event(org_id='org-123', dataset_id='model-123', debug_event=components.DebugEvent(
    content='<value>',
))

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `org_id`                                                       | *str*                                                          | :heavy_check_mark:                                             | Your company's unique organization ID                          | org-123                                                        |
| `dataset_id`                                                   | *str*                                                          | :heavy_check_mark:                                             | The resource ID to log the event to                            | model-123                                                      |
| `debug_event`                                                  | [components.DebugEvent](../../models/components/debugevent.md) | :heavy_check_mark:                                             | N/A                                                            |                                                                |


### Response

**[operations.LogDebugEventResponse](../../models/operations/logdebugeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
