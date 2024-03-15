# FeatureFlags
(*feature_flags*)

## Overview

Endpoint for feature flags

### Available Operations

* [get_feature_flags](#get_feature_flags) - Get feature flags for the specified user/org

## get_feature_flags

Get feature flags for the specified user/org

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.feature_flags.get_feature_flags(user_id='<value>', org_id='<value>')

if res.feature_flags is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetFeatureFlagsResponse](../../models/operations/getfeatureflagsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
