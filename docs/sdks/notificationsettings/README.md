# NotificationSettings
(*notification_settings*)

## Overview

TODO

### Available Operations

* [get_email_notification_action_payload](#get_email_notification_action_payload) - Get dummy notification action payload
* [get_pager_duty_notification_action_payload](#get_pager_duty_notification_action_payload) - Get dummy notification action payload
* [get_slack_notification_action_payload](#get_slack_notification_action_payload) - Get dummy notification action payload
* [get_notification_settings](#get_notification_settings) - Get notification settings for an org
* [update_notification_settings](#update_notification_settings) - Update notification settings for an org
* [list_notification_actions](#list_notification_actions) - List notification actions for an org
* [get_notification_action](#get_notification_action) - Get notification action for id
* [delete_notification_action](#delete_notification_action) - Delete notification action
* [disable_notification_action](#disable_notification_action) - Disable notification action
* [enable_notification_action](#enable_notification_action) - Enable notification action
* [test_notification_action](#test_notification_action) - Test a notification action
* [put_notification_action](#put_notification_action) - Add new notification action
* [add_notification_action](#add_notification_action) - Add new notification action
* [update_notification_action](#update_notification_action) - Update notification action

## get_email_notification_action_payload

Get dummy notification action payload

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.notification_settings.get_email_notification_action_payload()

if res.email_notification_action is not None:
    # handle response
    pass

```


### Response

**[operations.GetEmailNotificationActionPayloadResponse](../../models/operations/getemailnotificationactionpayloadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_pager_duty_notification_action_payload

Get dummy notification action payload

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.notification_settings.get_pager_duty_notification_action_payload()

if res.pager_duty_notification_action is not None:
    # handle response
    pass

```


### Response

**[operations.GetPagerDutyNotificationActionPayloadResponse](../../models/operations/getpagerdutynotificationactionpayloadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_slack_notification_action_payload

Get dummy notification action payload

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.notification_settings.get_slack_notification_action_payload()

if res.slack_notification_action is not None:
    # handle response
    pass

```


### Response

**[operations.GetSlackNotificationActionPayloadResponse](../../models/operations/getslacknotificationactionpayloadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_notification_settings

Get notification settings for an org

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.notification_settings.get_notification_settings(org_id='<value>')

if res.get_notification_settings_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetNotificationSettingsResponse](../../models/operations/getnotificationsettingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_notification_settings

Update notification settings for an org

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.notification_settings.update_notification_settings(org_id='<value>', notification_settings=components.NotificationSettings(
    email_settings=components.UberNotificationSchedule(
        enabled=False,
        cadence=components.NotificationSqsMessageCadence.HOURLY,
    ),
    slack_settings=components.UberNotificationSchedule(
        enabled=False,
        cadence=components.NotificationSqsMessageCadence.DAILY,
    ),
    pager_duty_settings=components.UberNotificationSchedule(
        enabled=False,
        cadence=components.NotificationSqsMessageCadence.INDIVIDUAL,
    ),
))

if res.notification_settings is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `org_id`                                                                           | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `notification_settings`                                                            | [components.NotificationSettings](../../models/components/notificationsettings.md) | :heavy_check_mark:                                                                 | N/A                                                                                |


### Response

**[operations.UpdateNotificationSettingsResponse](../../models/operations/updatenotificationsettingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_notification_actions

Get notification actions for an org

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.notification_settings.list_notification_actions(org_id='org-123')

if res.notification_actions is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |


### Response

**[operations.ListNotificationActionsResponse](../../models/operations/listnotificationactionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_notification_action

Get notification action for id

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.notification_settings.get_notification_action(org_id='org-123', action_id='user-action')

if res.notification_action is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `action_id`        | *str*              | :heavy_check_mark: | N/A                | user-action        |


### Response

**[operations.GetNotificationActionResponse](../../models/operations/getnotificationactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_notification_action

Delete notification action

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.notification_settings.delete_notification_action(org_id='org-123', action_id='user-action')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `action_id`        | *str*              | :heavy_check_mark: | N/A                | user-action        |


### Response

**[operations.DeleteNotificationActionResponse](../../models/operations/deletenotificationactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## disable_notification_action

Disable notification action

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.notification_settings.disable_notification_action(org_id='org-123', action_id='user-action')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `action_id`        | *str*              | :heavy_check_mark: | N/A                | user-action        |


### Response

**[operations.DisableNotificationActionResponse](../../models/operations/disablenotificationactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## enable_notification_action

Enable notification action

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.notification_settings.enable_notification_action(org_id='org-123', action_id='user-action')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `action_id`        | *str*              | :heavy_check_mark: | N/A                | user-action        |


### Response

**[operations.EnableNotificationActionResponse](../../models/operations/enablenotificationactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## test_notification_action

Test a notification action

### Example Usage

```python
import whylabs_client

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.notification_settings.test_notification_action(org_id='org-123', action_id='user-action')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `org_id`           | *str*              | :heavy_check_mark: | N/A                | org-123            |
| `action_id`        | *str*              | :heavy_check_mark: | N/A                | user-action        |


### Response

**[operations.TestNotificationActionResponse](../../models/operations/testnotificationactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_notification_action

Add new notification action

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.notification_settings.put_notification_action(org_id='org-123', type=components.ActionType.EMAIL, action_id='user-action', request_body='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `org_id`                                                       | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            | org-123                                                        |
| `type`                                                         | [components.ActionType](../../models/components/actiontype.md) | :heavy_check_mark:                                             | N/A                                                            | EMAIL                                                          |
| `action_id`                                                    | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            | user-action                                                    |
| `request_body`                                                 | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            |                                                                |


### Response

**[operations.PutNotificationActionResponse](../../models/operations/putnotificationactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## add_notification_action

Add new notification action

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.notification_settings.add_notification_action(org_id='org-123', type=components.ActionType.EMAIL, action_id='user-action', request_body='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `org_id`                                                       | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            | org-123                                                        |
| `type`                                                         | [components.ActionType](../../models/components/actiontype.md) | :heavy_check_mark:                                             | N/A                                                            | EMAIL                                                          |
| `action_id`                                                    | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            | user-action                                                    |
| `request_body`                                                 | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            |                                                                |


### Response

**[operations.AddNotificationActionResponse](../../models/operations/addnotificationactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_notification_action

Update notification action

### Example Usage

```python
import whylabs_client
from whylabs_client.models import components

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.notification_settings.update_notification_action(org_id='org-123', type=components.ActionType.EMAIL, action_id='user-action', request_body='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `org_id`                                                       | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            | org-123                                                        |
| `type`                                                         | [components.ActionType](../../models/components/actiontype.md) | :heavy_check_mark:                                             | N/A                                                            | EMAIL                                                          |
| `action_id`                                                    | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            | user-action                                                    |
| `request_body`                                                 | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            |                                                                |


### Response

**[operations.UpdateNotificationActionResponse](../../models/operations/updatenotificationactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
