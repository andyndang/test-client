# LogDebugEventRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `org_id`                                                       | *str*                                                          | :heavy_check_mark:                                             | Your company's unique organization ID                          | org-123                                                        |
| `dataset_id`                                                   | *str*                                                          | :heavy_check_mark:                                             | The resource ID to log the event to                            | model-123                                                      |
| `debug_event`                                                  | [components.DebugEvent](../../models/components/debugevent.md) | :heavy_check_mark:                                             | N/A                                                            |                                                                |