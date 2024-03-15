# DebugEvent

A debug event object


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `content`                                                                              | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `trace_id`                                                                             | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `segment`                                                                              | [Optional[components.DebugEventSegment]](../../models/components/debugeventsegment.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `tags`                                                                                 | List[*str*]                                                                            | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `dataset_timestamp`                                                                    | *Optional[int]*                                                                        | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `creation_timestamp`                                                                   | *Optional[int]*                                                                        | :heavy_minus_sign:                                                                     | N/A                                                                                    |