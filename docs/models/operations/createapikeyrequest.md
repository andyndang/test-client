# CreateAPIKeyRequest


## Fields

| Field                                  | Type                                   | Required                               | Description                            | Example                                |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `org_id`                               | *str*                                  | :heavy_check_mark:                     | Your company's unique organization ID  | org-123                                |
| `user_id`                              | *str*                                  | :heavy_check_mark:                     | The unique user ID in an organization. | user-123                               |
| `expiration_time`                      | *Optional[int]*                        | :heavy_minus_sign:                     | Expiration time in epoch milliseconds  | 1577836800000                          |
| `scopes`                               | List[*str*]                            | :heavy_minus_sign:                     | Scopes of the token                    |                                        |
| `alias`                                | *Optional[str]*                        | :heavy_minus_sign:                     | A human-friendly name for the API Key  | MLApplicationName                      |