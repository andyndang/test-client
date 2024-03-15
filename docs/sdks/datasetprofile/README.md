# DatasetProfile
(*dataset_profile*)

## Overview

Endpoint for access dataset profiles

### Available Operations

* [list_delete_analyzer_results_requests](#list_delete_analyzer_results_requests) - List requests to delete analyzer results
* [list_delete_dataset_profiles_requests](#list_delete_dataset_profiles_requests) - List requests to delete dataset profiles
* [delete_dataset_profiles](#delete_dataset_profiles) - Deletes a set of dataset profiles
* [delete_analyzer_results](#delete_analyzer_results) - Deletes a set of analyzer results
* [create_reference_profile](#create_reference_profile) - Returns data needed to uploading the reference profile
* [hide_segments](#hide_segments) - Hides a list of segments
* [get_profile_traces](#get_profile_traces) - Returns a list for profile traces matching a trace id
* [list_reference_profiles](#list_reference_profiles) - Returns a list for reference profiles between the given time range filtered on the upload timestamp
* [get_reference_profile](#get_reference_profile) - Returns a single reference profile
* [delete_reference_profile](#delete_reference_profile) - Delete a single reference profile
* [list_segments](#list_segments) - Returns a list of segments

## list_delete_analyzer_results_requests

List the requests to delete analyzer results.

        

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataset_profile.list_delete_analyzer_results_requests(org_id='org-123')

if res.delete_analyzer_results is not None:
    # handle response
    pass

```

### Parameters

| Parameter                             | Type                                  | Required                              | Description                           | Example                               |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `org_id`                              | *str*                                 | :heavy_check_mark:                    | Your company's unique organization ID | org-123                               |


### Response

**[operations.ListDeleteAnalyzerResultsRequestsResponse](../../models/operations/listdeleteanalyzerresultsrequestsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_delete_dataset_profiles_requests

List the requests to delete dataset profiles.

        

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataset_profile.list_delete_dataset_profiles_requests(org_id='org-123')

if res.delete_profiles is not None:
    # handle response
    pass

```

### Parameters

| Parameter                             | Type                                  | Required                              | Description                           | Example                               |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `org_id`                              | *str*                                 | :heavy_check_mark:                    | Your company's unique organization ID | org-123                               |


### Response

**[operations.ListDeleteDatasetProfilesRequestsResponse](../../models/operations/listdeletedatasetprofilesrequestsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_dataset_profiles

Deletes a set of dataset profiles. Returns false if scheduling deletion encountered some error.
        Optionally deletes analyzer results for the same time range.

        

### Example Usage

```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.DeleteDatasetProfilesRequest(
    org_id='org-123',
    dataset_id='model-123',
    profile_start_timestamp=1577836800000,
    profile_end_timestamp=1893456000000,
    before_upload_timestamp=1577836800000,
    delete_analyzer_results=True,
)

res = s.dataset_profile.delete_dataset_profiles(req)

if res.delete_dataset_profiles_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.DeleteDatasetProfilesRequest](../../models/operations/deletedatasetprofilesrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.DeleteDatasetProfilesResponse](../../models/operations/deletedatasetprofilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_analyzer_results

Deletes a set of analyzer results. Returns false if scheduling deletion encountered some error.

        

### Example Usage

```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.DeleteAnalyzerResultsRequest(
    org_id='org-123',
    dataset_id='model-123',
    request_body=operations.DeleteAnalyzerResultsRequestBody(
        analyzer_id='model-123',
    ),
    start_timestamp=1577836800000,
    end_timestamp=1893456000000,
)

res = s.dataset_profile.delete_analyzer_results(req)

if res.delete_analyzer_results_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.DeleteAnalyzerResultsRequest](../../models/operations/deleteanalyzerresultsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.DeleteAnalyzerResultsResponse](../../models/operations/deleteanalyzerresultsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_reference_profile

Returns data needed to upload the reference profile. Supports uploading segmented reference profiles. 
            If segments are omitted, provides data needed to upload a single reference profile. 
            This replaces the deprecated LogReference operation.
        

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataset_profile.create_reference_profile(org_id='org-123', dataset_id='model-123', create_reference_profile_request=components.CreateReferenceProfileRequest())

if res.create_reference_profile_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `org_id`                                                                                             | *str*                                                                                                | :heavy_check_mark:                                                                                   | Your company's unique organization ID                                                                | org-123                                                                                              |
| `dataset_id`                                                                                         | *str*                                                                                                | :heavy_check_mark:                                                                                   | The unique model ID in your company.                                                                 | model-123                                                                                            |
| `create_reference_profile_request`                                                                   | [components.CreateReferenceProfileRequest](../../models/components/createreferenceprofilerequest.md) | :heavy_check_mark:                                                                                   | N/A                                                                                                  |                                                                                                      |


### Response

**[operations.CreateReferenceProfileResponse](../../models/operations/createreferenceprofileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## hide_segments

Returns a list of segments that were hidden for a dataset.

        

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataset_profile.hide_segments(org_id='org-123', dataset_id='model-123', segments_list_request=components.SegmentsListRequest(
    segments=[
        '<value>',
    ],
))

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `org_id`                                                                         | *str*                                                                            | :heavy_check_mark:                                                               | Your company's unique organization ID                                            | org-123                                                                          |
| `dataset_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | The unique dataset ID in your company.                                           | model-123                                                                        |
| `segments_list_request`                                                          | [components.SegmentsListRequest](../../models/components/segmentslistrequest.md) | :heavy_check_mark:                                                               | N/A                                                                              |                                                                                  |


### Response

**[operations.HideSegmentsResponse](../../models/operations/hidesegmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_profile_traces

Returns a list of profile traces matching a trace id

        

### Example Usage

```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetProfileTracesRequest(
    org_id='org-123',
    dataset_id='model-123',
    trace_id='a756f8bb-de30-48a2-be41-178ae6af7100',
    limit=50,
    offset=0,
)

res = s.dataset_profile.get_profile_traces(req)

if res.profile_traces_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetProfileTracesRequest](../../models/operations/getprofiletracesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetProfileTracesResponse](../../models/operations/getprofiletracesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_reference_profiles

Returns a list of Reference Profiles between a given time range filtered on the upload timestamp.

        

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataset_profile.list_reference_profiles(org_id='org-123', model_id='model-123', from_epoch=1577836800000, to_epoch=1893456000000)

if res.reference_profile_item_responses is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        | Example                                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `org_id`                                                                                           | *str*                                                                                              | :heavy_check_mark:                                                                                 | Your company's unique organization ID                                                              | org-123                                                                                            |
| `model_id`                                                                                         | *str*                                                                                              | :heavy_check_mark:                                                                                 | The unique model ID in your company.                                                               | model-123                                                                                          |
| `from_epoch`                                                                                       | *Optional[int]*                                                                                    | :heavy_minus_sign:                                                                                 | Milli epoch time that represents the end of the time range to query based on the upload timestamp. | 1577836800000                                                                                      |
| `to_epoch`                                                                                         | *Optional[int]*                                                                                    | :heavy_minus_sign:                                                                                 | Milli epoch time that represents the end of the time range to query based on the upload timestamp. | 1893456000000                                                                                      |


### Response

**[operations.ListReferenceProfilesResponse](../../models/operations/listreferenceprofilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_reference_profile

Returns a Reference Profile.

        

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataset_profile.get_reference_profile(org_id='org-123', model_id='model-123', reference_id='ref-xxy')

if res.reference_profile_item_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                             | Type                                  | Required                              | Description                           | Example                               |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `org_id`                              | *str*                                 | :heavy_check_mark:                    | Your company's unique organization ID | org-123                               |
| `model_id`                            | *str*                                 | :heavy_check_mark:                    | The unique model ID in your company.  | model-123                             |
| `reference_id`                        | *str*                                 | :heavy_check_mark:                    | Unique reference Id.                  | ref-xxy                               |


### Response

**[operations.GetReferenceProfileResponse](../../models/operations/getreferenceprofileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_reference_profile

Delete a a Reference Profile. Returns false if the deletion encountered some error.

        

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataset_profile.delete_reference_profile(org_id='org-123', model_id='model-123', reference_id='ref-xxy')

if res.boolean is not None:
    # handle response
    pass

```

### Parameters

| Parameter                             | Type                                  | Required                              | Description                           | Example                               |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `org_id`                              | *str*                                 | :heavy_check_mark:                    | Your company's unique organization ID | org-123                               |
| `model_id`                            | *str*                                 | :heavy_check_mark:                    | The unique model ID in your company.  | model-123                             |
| `reference_id`                        | *str*                                 | :heavy_check_mark:                    | Unique reference Id.                  | ref-xxy                               |


### Response

**[operations.DeleteReferenceProfileResponse](../../models/operations/deletereferenceprofileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_segments

Returns a list of segments for the dataset.

        

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataset_profile.list_segments(org_id='org-123', model_id='model-123')

if res.segment_list_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                             | Type                                  | Required                              | Description                           | Example                               |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `org_id`                              | *str*                                 | :heavy_check_mark:                    | Your company's unique organization ID | org-123                               |
| `model_id`                            | *str*                                 | :heavy_check_mark:                    | The unique model ID in your company.  | model-123                             |


### Response

**[operations.ListSegmentsResponse](../../models/operations/listsegmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
