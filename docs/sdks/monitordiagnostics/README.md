# MonitorDiagnostics
(*monitor_diagnostics*)

## Overview

Endpoint for monitor diagnostics

### Available Operations

* [detect_noisy_columns](#detect_noisy_columns) - Endpoint to detect the noisiest columns for a specific analyzer and segment
* [detect_noisy_segments](#detect_noisy_segments) - Endpoint to detect the noisiest segments for a specific analyzer
* [detect_noisy_analyzers](#detect_noisy_analyzers) - Endpoint to detect noisy or failing analyzers
* [recommend_diagnostic_interval](#recommend_diagnostic_interval) - Endpoint to recommend a diagnostic interval

## detect_noisy_columns

Returns a list of column names sorted so the noisiest (most anomalies) is first. Also includes a similar list for columns with analyzer failures.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor_diagnostics.detect_noisy_columns(org_id='org-123', analyzer_segment_columns_diagnostic_request=components.AnalyzerSegmentColumnsDiagnosticRequest(
    interval='<value>',
    dataset_id='<value>',
    analyzer_id='<value>',
    segment=components.Segment(
        tags=[
            components.SegmentTag(
                key='<key>',
                value='<value>',
            ),
        ],
    ),
))

if res.analyzer_segment_columns_diagnostic_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              | Example                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `org_id`                                                                                                                 | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | N/A                                                                                                                      | org-123                                                                                                                  |
| `analyzer_segment_columns_diagnostic_request`                                                                            | [components.AnalyzerSegmentColumnsDiagnosticRequest](../../models/components/analyzersegmentcolumnsdiagnosticrequest.md) | :heavy_check_mark:                                                                                                       | N/A                                                                                                                      |                                                                                                                          |


### Response

**[operations.DetectNoisyColumnsResponse](../../models/operations/detectnoisycolumnsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## detect_noisy_segments

Returns a list of segments sorted so the noisiest (most anomalies per column) is first. Also includes a similar list for segments with analyzer failures.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor_diagnostics.detect_noisy_segments(org_id='org-123', analyzer_segments_diagnostic_request=components.AnalyzerSegmentsDiagnosticRequest(
    interval='<value>',
    dataset_id='<value>',
    analyzer_id='<value>',
))

if res.analyzer_segments_diagnostic_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  | Example                                                                                                      |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `org_id`                                                                                                     | *str*                                                                                                        | :heavy_check_mark:                                                                                           | N/A                                                                                                          | org-123                                                                                                      |
| `analyzer_segments_diagnostic_request`                                                                       | [components.AnalyzerSegmentsDiagnosticRequest](../../models/components/analyzersegmentsdiagnosticrequest.md) | :heavy_check_mark:                                                                                           | N/A                                                                                                          |                                                                                                              |


### Response

**[operations.DetectNoisySegmentsResponse](../../models/operations/detectnoisysegmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## detect_noisy_analyzers

Returns a list of analyzers sorted so the noisiest (most anomalies per column) is first. Also includes a similar list for analyzer failures.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor_diagnostics.detect_noisy_analyzers(org_id='org-123', analyzers_diagnostic_request=components.AnalyzersDiagnosticRequest(
    interval='<value>',
    dataset_id='<value>',
))

if res.analyzers_diagnostic_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    | Example                                                                                        |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `org_id`                                                                                       | *str*                                                                                          | :heavy_check_mark:                                                                             | N/A                                                                                            | org-123                                                                                        |
| `analyzers_diagnostic_request`                                                                 | [components.AnalyzersDiagnosticRequest](../../models/components/analyzersdiagnosticrequest.md) | :heavy_check_mark:                                                                             | N/A                                                                                            |                                                                                                |


### Response

**[operations.DetectNoisyAnalyzersResponse](../../models/operations/detectnoisyanalyzersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## recommend_diagnostic_interval

Returns an interval containing the last 30 batches of data

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor_diagnostics.recommend_diagnostic_interval(org_id='org-123', diagnostic_interval_request=components.DiagnosticIntervalRequest(
    dataset_id='<value>',
))

if res.diagnostic_interval_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `org_id`                                                                                     | *str*                                                                                        | :heavy_check_mark:                                                                           | N/A                                                                                          | org-123                                                                                      |
| `diagnostic_interval_request`                                                                | [components.DiagnosticIntervalRequest](../../models/components/diagnosticintervalrequest.md) | :heavy_check_mark:                                                                           | N/A                                                                                          |                                                                                              |


### Response

**[operations.RecommendDiagnosticIntervalResponse](../../models/operations/recommenddiagnosticintervalresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
