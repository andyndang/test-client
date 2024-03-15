# Log
(*log*)

## Overview

Endpoint for logging dataset profiles

### Available Operations

* [log_async](#log_async) - Like /log, except this api doesn't take the actual profile content. It returns an upload link that can be used to upload the profile to.
* [get_profile_observatory_link](#get_profile_observatory_link) - Get observatory links for profiles in a given org/model. A max of 3 profiles can be viewed a a time.
* [~~log_reference~~](#log_reference) - Returns a presigned URL for uploading the reference profile to. :warning: **Deprecated**

## log_async

Like /log, except this api doesn't take the actual profile content. It returns an upload link that can be used to upload the profile to.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.log.log_async(org_id='org-123', dataset_id='model-123', log_async_request=components.LogAsyncRequest(
    dataset_timestamp=506585,
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

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `org_id`                                                                 | *str*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      | org-123                                                                  |
| `dataset_id`                                                             | *str*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      | model-123                                                                |
| `log_async_request`                                                      | [components.LogAsyncRequest](../../models/components/logasyncrequest.md) | :heavy_check_mark:                                                       | N/A                                                                      |                                                                          |


### Response

**[operations.LogAsyncResponse](../../models/operations/logasyncresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_profile_observatory_link

Get observatory links for profiles in a given org/model. A max of 3 profiles can be viewed a a time.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.log.get_profile_observatory_link(dataset_id='<value>', org_id='<value>', get_profile_observatory_link_request=components.GetProfileObservatoryLinkRequest(
    batch_profile_timestamps=[
        926863,
    ],
    reference_profile_ids=[
        '<value>',
    ],
))

if res.get_profile_observatory_link_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `dataset_id`                                                                                               | *str*                                                                                                      | :heavy_check_mark:                                                                                         | N/A                                                                                                        |
| `org_id`                                                                                                   | *str*                                                                                                      | :heavy_check_mark:                                                                                         | N/A                                                                                                        |
| `get_profile_observatory_link_request`                                                                     | [components.GetProfileObservatoryLinkRequest](../../models/components/getprofileobservatorylinkrequest.md) | :heavy_check_mark:                                                                                         | N/A                                                                                                        |


### Response

**[operations.GetProfileObservatoryLinkResponse](../../models/operations/getprofileobservatorylinkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## ~~log_reference~~

Reference profiles can be used for.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.log.log_reference(org_id='org-123', model_id='model-123', log_reference_request=components.LogReferenceRequest())

if res.log_reference_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `org_id`                                                                         | *str*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              | org-123                                                                          |
| `model_id`                                                                       | *str*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              | model-123                                                                        |
| `log_reference_request`                                                          | [components.LogReferenceRequest](../../models/components/logreferencerequest.md) | :heavy_check_mark:                                                               | N/A                                                                              |                                                                                  |


### Response

**[operations.LogReferenceResponse](../../models/operations/logreferenceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
