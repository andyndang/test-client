# User

User metadata


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The id of the user.                                                 |
| `email`                                                             | *str*                                                               | :heavy_check_mark:                                                  | The user's email address.                                           |
| `preferences`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The user's JSON serialized preferences. Schema defined in Dashbird. |