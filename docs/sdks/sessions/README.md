# Sessions
(*sessions*)

## Overview

Interactions related to sessions.

### Available Operations

* [create_session](#create_session) - Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.
* [get_session_profile_observatory_link](#get_session_profile_observatory_link) - Get observatory links for profiles in a given session. A max of 3 profiles can be viewed a a time.
* [get_session](#get_session) - Get information about a session.
* [claim_guest_session](#claim_guest_session) - Claim a guest session, copying its model data into another org and expiring the session.
* [create_reference_profile_upload](#create_reference_profile_upload) - Create a reference profile upload for a given session.
* [batch_create_reference_profile_upload](#batch_create_reference_profile_upload) - Create multiple reference profile uploads for a given session.
* [create_dataset_profile_upload](#create_dataset_profile_upload) - Create an upload for a given session.

## create_session

Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = components.CreateSessionRequest(
    user_id='<value>',
)

res = s.sessions.create_session(req)

if res.create_session_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.CreateSessionRequest](../../models/components/createsessionrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateSessionResponse](../../models/operations/createsessionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_session_profile_observatory_link

Get observatory links for profiles in a given session. A max of 3 profiles can be viewed a a time.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.sessions.get_session_profile_observatory_link(session_id='<value>', get_profile_observatory_link_request=components.GetProfileObservatoryLinkRequest(
    batch_profile_timestamps=[
        495187,
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
| `session_id`                                                                                               | *str*                                                                                                      | :heavy_check_mark:                                                                                         | N/A                                                                                                        |
| `get_profile_observatory_link_request`                                                                     | [components.GetProfileObservatoryLinkRequest](../../models/components/getprofileobservatorylinkrequest.md) | :heavy_check_mark:                                                                                         | N/A                                                                                                        |


### Response

**[operations.GetSessionProfileObservatoryLinkResponse](../../models/operations/getsessionprofileobservatorylinkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_session

Get information about a session.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.sessions.get_session(session_id='<value>')

if res.get_session_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `session_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetSessionResponse](../../models/operations/getsessionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## claim_guest_session

Claim a guest session, copying its model data into another org and expiring the session.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.sessions.claim_guest_session(session_id='<value>', org_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `session_id`       | *str*              | :heavy_check_mark: | N/A                |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.ClaimGuestSessionResponse](../../models/operations/claimguestsessionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_reference_profile_upload

Create a reference profile upload for a given session.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.sessions.create_reference_profile_upload(session_id='<value>', log_reference_request=components.LogReferenceRequest())

if res.log_session_reference_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `session_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              |
| `log_reference_request`                                                          | [components.LogReferenceRequest](../../models/components/logreferencerequest.md) | :heavy_check_mark:                                                               | N/A                                                                              |


### Response

**[operations.CreateReferenceProfileUploadResponse](../../models/operations/createreferenceprofileuploadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## batch_create_reference_profile_upload

Create multiple reference profile uploads for a given session.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.sessions.batch_create_reference_profile_upload(session_id='<value>', batch_log_reference_request=components.BatchLogReferenceRequest(
    references=[
        components.LogReferenceRequest(),
    ],
))

if res.batch_log_session_reference_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `session_id`                                                                               | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `batch_log_reference_request`                                                              | [components.BatchLogReferenceRequest](../../models/components/batchlogreferencerequest.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |


### Response

**[operations.BatchCreateReferenceProfileUploadResponse](../../models/operations/batchcreatereferenceprofileuploadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_dataset_profile_upload

Create an upload for a given session.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.sessions.create_dataset_profile_upload(session_id='<value>', log_async_request=components.LogAsyncRequest(
    dataset_timestamp=967561,
    segment_tags=[
        components.SegmentTag(
            key='<key>',
            value='<value>',
        ),
    ],
))

if res.create_dataset_profile_upload_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `session_id`                                                             | *str*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      |
| `log_async_request`                                                      | [components.LogAsyncRequest](../../models/components/logasyncrequest.md) | :heavy_check_mark:                                                       | N/A                                                                      |


### Response

**[operations.CreateDatasetProfileUploadResponse](../../models/operations/createdatasetprofileuploadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
