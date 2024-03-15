# Monitor
(*monitor*)

## Overview

Interactions related to monitors.

### Available Operations

* [list_constraints](#list_constraints) - List the constraints for a given dataset.
* [get_analyzer](#get_analyzer) - Get the analyzer config for a given dataset.
* [put_analyzer](#put_analyzer) - Save the analyzer config for a given dataset.
* [delete_analyzer](#delete_analyzer) - Delete the analyzer config for a given dataset.
* [get_monitor](#get_monitor) - Get the monitor config for a given dataset.
* [put_monitor](#put_monitor) - Save the monitor for a given dataset.
* [delete_monitor](#delete_monitor) - Delete the monitor for a given dataset.
* [get_monitor_config_v3](#get_monitor_config_v3) - Get the monitor config document for a given dataset.
* [put_monitor_config_v3](#put_monitor_config_v3) - Save the monitor config document for a given dataset.
* [patch_monitor_config_v3](#patch_monitor_config_v3) - Patch an updated monitor config document for a given dataset.
* [validate_monitor_config_v3](#validate_monitor_config_v3) - Validate the monitor config document for a given dataset.
* [list_monitor_config_v3_versions](#list_monitor_config_v3_versions) - List the monitor config document versions for a given dataset.
* [get_monitor_config_v3_version](#get_monitor_config_v3_version) - Get the monitor config document version for a given dataset.
* [put_request_monitor_run_config](#put_request_monitor_run_config) - Put the RequestMonitorRun config into S3.

## list_constraints

List the constraints for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor.list_constraints(org_id='org-123', dataset_id='model-123')

if res.strings is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |


### Response

**[operations.ListConstraintsResponse](../../models/operations/listconstraintsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_analyzer

Get the analyzer config for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor.get_analyzer(org_id='org-123', dataset_id='model-123', analyzer_id='drift-analyzer')

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |
| `analyzer_id`      | *str*              | :heavy_check_mark: | N/A                | drift-analyzer     |


### Response

**[operations.GetAnalyzerResponse](../../models/operations/getanalyzerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_analyzer

Save the analyzer config for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor.put_analyzer(org_id='org-123', dataset_id='model-123', analyzer_id='drift-analyzer', request_body='<value>')

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |
| `analyzer_id`      | *str*              | :heavy_check_mark: | N/A                | drift-analyzer     |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |                    |


### Response

**[operations.PutAnalyzerResponse](../../models/operations/putanalyzerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_analyzer

Delete the analyzer config for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor.delete_analyzer(org_id='org-123', dataset_id='model-123', analyzer_id='drift-analyzer')

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |
| `analyzer_id`      | *str*              | :heavy_check_mark: | N/A                | drift-analyzer     |


### Response

**[operations.DeleteAnalyzerResponse](../../models/operations/deleteanalyzerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monitor

Get the monitor config for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor.get_monitor(org_id='org-123', dataset_id='model-123', monitor_id='drift-monitor-123')

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |
| `monitor_id`       | *str*              | :heavy_check_mark: | N/A                | drift-monitor-123  |


### Response

**[operations.GetMonitorResponse](../../models/operations/getmonitorresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_monitor

Save the monitor for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor.put_monitor(org_id='org-123', dataset_id='model-123', monitor_id='drift-monitor-123', request_body='<value>')

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |
| `monitor_id`       | *str*              | :heavy_check_mark: | N/A                | drift-monitor-123  |
| `request_body`     | *str*              | :heavy_check_mark: | N/A                |                    |


### Response

**[operations.PutMonitorResponse](../../models/operations/putmonitorresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_monitor

Delete the monitor for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor.delete_monitor(org_id='org-123', dataset_id='model-123', monitor_id='drift-monitor-123')

if res.response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |
| `monitor_id`       | *str*              | :heavy_check_mark: | N/A                | drift-monitor-123  |


### Response

**[operations.DeleteMonitorResponse](../../models/operations/deletemonitorresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monitor_config_v3

Get the monitor config document for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor.get_monitor_config_v3(org_id='org-123', dataset_id='model-123', include_entity_schema=False, include_entity_weights=False)

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                | Type                     | Required                 | Description              | Example                  |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `org_id`                 | *str*                    | :heavy_check_mark:       | N/A                      | org-123                  |
| `dataset_id`             | *str*                    | :heavy_check_mark:       | N/A                      | model-123                |
| `include_entity_schema`  | *Optional[bool]*         | :heavy_minus_sign:       | N/A                      |                          |
| `include_entity_weights` | *Optional[bool]*         | :heavy_minus_sign:       | N/A                      |                          |


### Response

**[operations.GetMonitorConfigV3Response](../../models/operations/getmonitorconfigv3response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_monitor_config_v3

Save the monitor config document for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor.put_monitor_config_v3(org_id='org-123', dataset_id='model-123', request_body='<value>')

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

**[operations.PutMonitorConfigV3Response](../../models/operations/putmonitorconfigv3response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_monitor_config_v3

Save an updated monitor config document for a given dataset.  Monitors and analyzers matching an existing ID are replaced.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor.patch_monitor_config_v3(org_id='org-123', dataset_id='model-123', request_body='<value>')

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

**[operations.PatchMonitorConfigV3Response](../../models/operations/patchmonitorconfigv3response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## validate_monitor_config_v3

Validate the monitor config document for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor.validate_monitor_config_v3(org_id='org-123', dataset_id='model-123', request_body='<value>', verbose=False)

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
| `verbose`          | *Optional[bool]*   | :heavy_minus_sign: | N/A                |                    |


### Response

**[operations.ValidateMonitorConfigV3Response](../../models/operations/validatemonitorconfigv3response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_monitor_config_v3_versions

List the monitor config document versions for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor.list_monitor_config_v3_versions(org_id='org-123', dataset_id='model-123')

if res.monitor_config_versions is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `dataset_id`       | *str*              | :heavy_check_mark: | N/A                | model-123          |


### Response

**[operations.ListMonitorConfigV3VersionsResponse](../../models/operations/listmonitorconfigv3versionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monitor_config_v3_version

Get the monitor config document version for a given dataset.

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor.get_monitor_config_v3_version(org_id='org-123', dataset_id='model-123', version_id='4920545486e2a4cdf0f770c09748e663')

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                        | Type                             | Required                         | Description                      | Example                          |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `org_id`                         | *str*                            | :heavy_check_mark:               | N/A                              | org-123                          |
| `dataset_id`                     | *str*                            | :heavy_check_mark:               | N/A                              | model-123                        |
| `version_id`                     | *str*                            | :heavy_check_mark:               | N/A                              | 4920545486e2a4cdf0f770c09748e663 |


### Response

**[operations.GetMonitorConfigV3VersionResponse](../../models/operations/getmonitorconfigv3versionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_request_monitor_run_config

Put the RequestMonitorRun config into S3.

### Example Usage

```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.monitor.put_request_monitor_run_config(org_id='org-123', dataset_id='model-123', request_body=operations.PutRequestMonitorRunConfigRequestBody(
    analyzer_ids=[
        'd',
        'r',
        'i',
        'f',
        't',
        '-',
        'a',
        'n',
        'a',
        'l',
        'y',
        'z',
        'e',
        'r',
    ],
    start_timestamp=1577836800000,
    end_timestamp=1893456000000,
))

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          | Example                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `org_id`                                                                                                             | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  | org-123                                                                                                              |
| `dataset_id`                                                                                                         | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  | model-123                                                                                                            |
| `request_body`                                                                                                       | [operations.PutRequestMonitorRunConfigRequestBody](../../models/operations/putrequestmonitorrunconfigrequestbody.md) | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  |                                                                                                                      |


### Response

**[operations.PutRequestMonitorRunConfigResponse](../../models/operations/putrequestmonitorrunconfigresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
