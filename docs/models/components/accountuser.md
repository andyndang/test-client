# AccountUser

Account User metadata


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `user_id`                              | *str*                                  | :heavy_check_mark:                     | The WhyLabs user id                    |
| `org_id`                               | *str*                                  | :heavy_check_mark:                     | The WhyLabs organization id            |
| `email`                                | *str*                                  | :heavy_check_mark:                     | The user's email address               |
| `external_id`                          | *Optional[str]*                        | :heavy_minus_sign:                     | External user id                       |
| `user_schema`                          | *Optional[str]*                        | :heavy_minus_sign:                     | User schema                            |
| `active`                               | *Optional[bool]*                       | :heavy_minus_sign:                     | Flag to indicate if the user is active |