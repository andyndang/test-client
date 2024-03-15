# Key

Response when creating an API key successfully


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `key_id`                                                       | *str*                                                          | :heavy_check_mark:                                             | The key id. Can be used to identify keys for a given user      |
| `org_id`                                                       | *str*                                                          | :heavy_check_mark:                                             | The organization that the key belongs to                       |
| `user_id`                                                      | *str*                                                          | :heavy_check_mark:                                             | The user that the key represents                               |
| `creation_time`                                                | *str*                                                          | :heavy_check_mark:                                             | Creation time in human readable format                         |
| `key`                                                          | *Optional[str]*                                                | :heavy_minus_sign:                                             | The full value of the key. This is not persisted in the system |
| `expiration_time`                                              | *Optional[str]*                                                | :heavy_minus_sign:                                             | Expiration time in human readable format                       |
| `last_used_time`                                               | *Optional[str]*                                                | :heavy_minus_sign:                                             | Last used time in human readable format                        |
| `scopes`                                                       | List[*str*]                                                    | :heavy_minus_sign:                                             | Scope of the key                                               |
| `alias`                                                        | *Optional[str]*                                                | :heavy_minus_sign:                                             | Human-readable alias for the key                               |
| `revoked`                                                      | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Whether the key has been revoked                               |